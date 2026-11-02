# -*- coding: utf-8 -*-
"""
Verificación por consola, sin ventana:
    ~/Aplicaciones/FreeCAD.AppImage freecadcmd verificar.py

Mueve el mecanismo por todo el recorrido, busca choques con los sólidos reales
y escribe los números en resultados.json. Termina con error si el modelo base
choca: así un cambio en parametros.py no puede romperlo sin que se note.
"""
import json, math, os, sys

CARPETA = (os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals()
           else os.getcwd())
sys.path.insert(0, CARPETA)

import FreeCAD as App
import Part

import parametros as P
import piezas as Z

UMBRAL = 1.0     # mm³: por debajo es contacto o error numérico, no un choque
res = {}
fallas = []


def comun(a, b):
    return a.common(b).Volume


def en_estado(pz, nombre, est):
    forma, grupo, centro, clave = pz[nombre]
    f = forma.copy()
    f.Placement = Z.colocar(forma, grupo, centro, clave, est)
    return f


# Contactos que el diseño busca a propósito
PERMITIDOS = {
    frozenset(("Guias", "Carro")),                  # patines sobre las guías
    frozenset(("Eje", "NucleoRodillo")),
    frozenset(("Rodillo", "NucleoRodillo")),
    frozenset(("Eje", "Manivela")),
    frozenset(("Eje", "EngranajeZ1")),
    frozenset(("Mordaza", "RodamientoCuello")),
    frozenset(("SoporteCuello", "RodamientoCuello")),
    frozenset(("Collares", "Placa1")),
    frozenset(("Collares", "EngranajeZ2")),
    frozenset(("Portacuchilla", "Cuchilla")),
    frozenset(("Portacuchilla", "Base")),
    frozenset(("Tuerca", "Base")),
    frozenset(("Guias", "Base")),
    frozenset(("Carro", "SoporteCuello")),
    frozenset(("Carro", "Placa1")),
    frozenset(("Carro", "Placa2")),
}

pz = Z.formas()
pz["Husillo"] = (Z.husillo_liso(), "gira", (P.Y_H, P.Z_H), "husillo")
pz["Botella"] = (Z.botella_solida(), "gira", (0.0, P.H_EJE), "botella")
PERMITIDOS |= {frozenset(("Husillo", "Tuerca")),      # enrosca
               frozenset(("Husillo", "Collares")),
               frozenset(("Husillo", "EngranajeZ2")),
               frozenset(("Botella", "Mordaza")),     # la sostiene
               frozenset(("Botella", "Cuchilla"))}    # corta

# ------------------------------------------------- choques en todo el recorrido
nombres = sorted(pz)
pasos = [P.VUELTAS_MANIVELA_TOTAL * k / 12 for k in range(13)]
choques = {}
for v in pasos:
    est = P.estado(v)
    formas = {n: en_estado(pz, n, est) for n in nombres}
    for i, a in enumerate(nombres):
        for b in nombres[i + 1:]:
            if frozenset((a, b)) in PERMITIDOS:
                continue
            fa, fb = formas[a], formas[b]
            if not fa.BoundBox.intersect(fb.BoundBox):
                continue
            vol = comun(fa, fb)
            if vol > UMBRAL and vol > choques.get((a, b), (0,))[0]:
                choques[(a, b)] = (vol, est["s"])
res["choques_modelo_base"] = [
    {"a": a, "b": b, "mm3": round(v, 1), "s_mm": round(s, 1)}
    for (a, b), (v, s) in sorted(choques.items())]
if choques:
    fallas.append(f"el modelo base choca: {sorted(choques)}")

# El husillo tiene que seguir enroscado en la tuerca al principio y al final
ok_rosca = (P.X_HUSILLO_FIN > P.X_TUERCA[1]
            and P.X_HUSILLO_INI + P.RECORRIDO < P.X_TUERCA[0])
res["husillo_enroscado_todo_el_recorrido"] = ok_rosca
if not ok_rosca:
    fallas.append("el husillo se sale de la tuerca")

# ---------------------------------- los dientes reales engranan con z1/z2 y no otra
g1, g2 = pz["EngranajeZ1"], pz["EngranajeZ2"]
max_bien, max_mal = 0.0, 0.0
for k in range(24):
    v = k / 24 * 2 / P.Z_1 * 7.3         # recorre varios dientes, ángulos no enteros
    est = P.estado(v)
    a = en_estado(pz, "EngranajeZ1", est)
    b = en_estado(pz, "EngranajeZ2", est)
    max_bien = max(max_bien, comun(a, b))
    malo = dict(est)
    malo["husillo"] = -est["rodillo"] / 1.8     # relación equivocada, de control
    c = en_estado(pz, "EngranajeZ2", malo)
    max_mal = max(max_mal, comun(a, c))
res["engrane"] = {"solape_max_relacion_real_mm3": round(max_bien, 2),
                  "solape_max_relacion_1_8_control_mm3": round(max_mal, 1),
                  "distancia_entre_ejes_mm": P.DIST_EJES}
if max_bien > UMBRAL or max_mal < 10:
    fallas.append("el control de engrane no da lo esperado")

# ---------------------------------------- el paso, medido sobre la trayectoria
# Punto de la cuchilla visto desde la botella, en 2000 pasos de la simulación.
# Se mide el corrimiento axial entre cruces sucesivos del mismo ángulo.
cruces = []
n = 2000
ult = 0
for k in range(n + 1):
    est = P.estado(P.VUELTAS_MANIVELA_TOTAL * k / n)
    vueltas = int(est["botella"] // 360)
    if vueltas > ult or k == 0:
        cruces.append(P.X_CUCHILLA - est["s"])
        ult = vueltas
difs = [cruces[i] - cruces[i + 1] for i in range(len(cruces) - 1)]
res["paso"] = {
    "ecuacion_E2_mm": round(P.PASO_A, 3),
    "medido_en_simulacion_mm": round(sum(difs) / len(difs), 2),
    "angulo_helice_grados": round(math.degrees(math.atan(P.PASO_A / (math.pi * P.D_B))), 2),
    "vueltas_manivela": round(P.VUELTAS_MANIVELA_TOTAL, 1),
    "vueltas_botella": round(P.VUELTAS_BOTELLA_TOTAL, 1),
    "largo_tira_m": round(P.LARGO_TIRA / 1000, 2),
}

# ------------------------------------------------------- sentidos (E2, 5.3 lo pide)
# Solo se cumple para rosca derecha si el husillo gira según +X cuando el carro
# avanza hacia +X. Se comprueba con el signo de la cinemática.
e = P.estado(1)
res["sentidos"] = {
    "rosca": "derecha" if e["husillo"] * e["s"] > 0 else "izquierda",
    "manivela_vista_desde_el_borde_abierto": "horaria" if e["rodillo"] < 0 else "antihoraria",
    "pared_en_la_cuchilla": "baja" if e["botella"] > 0 else "sube",
}

# ------------------------------------ dónde va la manivela: tres ubicaciones
bot = Z.botella_solida()
caso = {}
x_tras = P.X_RODILLO[1] + 12
caso["sobre_el_cuerpo_como_imagen_IA"] = comun(Z.barrido_manivela(x_tras, +1), bot)
caso["detras_del_soporte_modelo"] = comun(Z.barrido_manivela(), bot)
res["manivela"] = {k: round(v) for k, v in caso.items()}
hueco = P.DIST_BR - P.R_B
res["manivela"]["hueco_eje_a_botella_mm"] = hueco
res["manivela"]["radio_max_sobre_el_cuerpo_mm"] = round(hueco - P.R_MANGO, 1)
# Figura del choque
caso_forma = Z.barrido_manivela(x_tras, +1).common(bot)
os.makedirs(os.path.join(CARPETA, "build"), exist_ok=True)
caso_forma.exportBrep(os.path.join(CARPETA, "build", "choque_manivela.brep"))

# ------------------------------------------- cuánto módulo admite el eje de Ø30
pared = 2.5      # [SUP] material mínimo entre el agujero y el fondo del diente
filas = []
for m in (1.0, 1.25, 1.5, 2.0, 2.5):
    df = m * (P.Z_1 - 2.5)
    filas.append({"modulo": m, "fondo_diente_mm": df, "entra": df >= P.D_EJE + 2 * pared})
res["pinon_sobre_eje_30"] = filas

# ---------------------------------- rodillo para otras botellas: ¿se conserva el engrane?
# Si la caja pivota sobre el husillo, el centro del rodillo se mueve por un arco
# de radio DIST_EJES y los engranajes no se separan. ¿Llega a tocar cada botella?
d0 = math.hypot(P.Y_H, P.H_EJE - P.Z_H)
filas = []
for db in (65, 75, 88, 100, 110):
    d = (db + P.D_R) / 2
    r = P.DIST_EJES
    alcanza = abs(r - d) <= d0 <= r + d
    giro = None
    if alcanza:
        cosb = (d0 ** 2 + r ** 2 - d ** 2) / (2 * d0 * r)
        giro = math.degrees(math.acos(cosb))
    filas.append({"Db": db, "alcanza": alcanza,
                  "angulo_caja_grados": None if giro is None else round(giro, 1),
                  "a_mm": round(P.L_HUSILLO * db / (P.I * P.D_R), 2)})
res["pivote_sobre_husillo"] = filas
if filas:
    angs = [f["angulo_caja_grados"] for f in filas if f["angulo_caja_grados"] is not None]
    res["pivote_barrido_grados"] = round(max(angs) - min(angs), 1)

# ------------------------------------------------------------------- envolvente
xmin = P.X_MANIVELA - 8 - P.LARGO_MANGO
# La botella no pasa de la cuchilla (se va consumiendo): lo que más sale es el husillo.
xmax = P.X_HUSILLO_FIN + P.RECORRIDO
res["envolvente"] = {
    "largo_total_mm": round(xmax - xmin),
    "largo_base_mm": round(P.X_BASE[1] - P.X_BASE[0]),
    "largo_husillo_mm": round(P.X_HUSILLO_FIN - P.X_HUSILLO_INI),
    "husillo_fuera_de_base_al_final_mm": round(xmax - P.X_BASE[1]),
    "voladizo_botella_desde_el_cuello_mm": round(P.X_BORDE - P.X_MORDAZA[1]),
    "voladizo_rodillo_mm": round(P.X_RODILLO[0] - P.X_PLACA_2[1]),
    "holgura_placa2_botella_mm": round(
        P.DIST_BR - P.R_PLACA_EJE - P.radio_botella(P.X_PLACA_2[1]), 1),
}

res["fallas"] = fallas
# Lo que agregan los pasos siguientes de make (STEP y planos) no se pierde.
ruta_res = os.path.join(CARPETA, "resultados.json")
if os.path.exists(ruta_res):
    with open(ruta_res, encoding="utf-8") as f:
        previo = json.load(f)
    for clave in ("step", "planos"):
        if clave in previo:
            res[clave] = previo[clave]
with open(os.path.join(CARPETA, "resultados.json"), "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
print("VERIFICACION", "CON FALLAS" if fallas else "OK", flush=True)
if fallas:
    os._exit(1)
os._exit(0)
