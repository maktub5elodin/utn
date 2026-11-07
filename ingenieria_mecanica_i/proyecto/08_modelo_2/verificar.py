# -*- coding: utf-8 -*-
"""
Verificación del modelo 2.0, por consola y sin ventana:
    ~/Aplicaciones/FreeCAD.AppImage freecadcmd verificar.py

Cinco controles, y resultados.json con los números:
  1. choques en el armado, con la botella al inicio y al final del corte;
  2. la manivela gira una vuelta completa sin tocar nada;
  3. armado en orden: cada pieza llega a su lugar sin atravesar lo ya armado;
  4. impresión: tamaño de cama, voladizos y puentes de cada pieza impresa;
  5. funcionamiento: fuerza en la mano, resistencia de la tira, avance,
     anclajes y ancho de la tira.
Termina con error si algo falla: un cambio en parametros.py no puede romper
el modelo sin que se note.
"""
import json, math, os, sys

CARPETA = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
sys.path.insert(0, CARPETA)

import FreeCAD as App
import Part

import parametros as P
import piezas as Z

V = App.Vector
UMBRAL = 0.5          # mm³: por debajo es contacto o error numérico, no un choque
res, fallas = {}, []

# Pares que se tocan o se cruzan a propósito
PERMITIDOS = {frozenset(p) for p in [
    ("Botella", "Hoja"),        # la hoja corta la pared: es el corte
    ("Botella", "Tira"),        # la tira es la botella que sale
]}


def comun(a, b):
    if not a.BoundBox.intersect(b.BoundBox):
        return 0.0
    return a.common(b).Volume


def choques(pz, nombres=None):
    nombres = sorted(pz) if nombres is None else nombres
    out = []
    for i, a in enumerate(nombres):
        for b in nombres[i + 1:]:
            if frozenset((a, b)) in PERMITIDOS:
                continue
            v = comun(pz[a]["forma"], pz[b]["forma"])
            if v > UMBRAL:
                out.append({"a": a, "b": b, "mm3": round(v, 1)})
    return out


# ------------------------------------------------------- 1. choques armado
for s in (0.0, P.RECORRIDO):
    c = choques(Z.conjunto(s))
    res[f"choques_s{int(s)}"] = c
    if c:
        fallas.append(f"choques con s = {s:.0f} mm: {[(x['a'], x['b']) for x in c]}")

pz0 = Z.conjunto(0.0)
pz1 = Z.conjunto(P.RECORRIDO)

# ------------------------------------------- 2. la manivela da la vuelta
GIRAN = ["Manivela", "Mango", "TornilloMango", "TuercaMango"]
FIJAS_PARA_MANIVELA = [n for n in pz0 if n not in GIRAN + ["CarreteSuperior", "TuercaCarrete", "TuercaManivela",
                                                          "EjeCarrete", "CarreteInferior"]]
peor = []
eje_c = V(P.X_CARRETE, P.Y_CARRETE, 0)
for k in range(36):
    for n in GIRAN:
        f = pz0[n]["forma"].copy()
        f.rotate(eje_c, V(0, 0, 1), 10.0 * k)
        for m in FIJAS_PARA_MANIVELA:
            for pz in (pz0, pz1):
                v = comun(f, pz[m]["forma"])
                if v > UMBRAL:
                    peor.append((n, m, 10 * k, round(v, 1)))
res["manivela_vuelta_completa"] = {"choques": peor[:10], "posiciones": 36}
if peor:
    fallas.append(f"la manivela choca al girar: {peor[:3]}")

# Lugar para la mano: del mango a la botella, en la posición más cercana
d_ejes = math.hypot(P.X_CARRETE, P.Y_CARRETE)
luz = d_ejes - P.R_MANIVELA - P.MANGO_R - P.R_B
res["luz_mano_botella_mm"] = round(luz, 1)
if luz < P.LUZ_MANO:
    fallas.append(f"la mano pasa a {luz:.0f} mm de la botella (mínimo {P.LUZ_MANO:.0f})")

# ----------------------------------------------------- 3. armado en orden
# (paso, piezas que se mueven juntas, dirección de llegada, recorrido en mm)
PASOS = [
    ("Zócalo sobre la base", ["Zocalo"], (0, 0, -1), 40, None),
    ("Tuerca M3 del prisionero, por su ranura", ["TuercaPrisionero"], (0, 0, -1), 20, None),
    ("Varilla lisa en el zócalo, desde arriba", ["Varilla"], (0, 0, -1), 60, None),
    ("Prisionero, desde afuera", ["Prisionero"], (1, 0, 0), 20, None),
    ("Taco de MDF sobre la base", ["Taco"], (0, 0, -1), 60, None),
    ("Tuercas M3 al cabezal, desde abajo", ["TuercasHoja"], (0, 0, 1), 20, ["Cabezal"]),
    ("Cabezal sobre el taco", ["Cabezal", "TuercasHoja"], (0, 0, -1), 40, None),
    ("Chapita en su rebaje, desde arriba", ["Chapita"], (0, 0, -1), 20, None),
    ("Labio exterior, sobre la chapita", ["LabioExterior"], (0, 0, -1), 30, None),
    ("Calce", ["Calce"], (0, 0, -1), 30, None),
    ("Ojal", ["Ojal"], (0, 0, -1), 60, None),
    ("Rodamientos a la torre, desde arriba", ["Rodamientos"], (0, 0, -1), 40, ["Torre"]),
    ("Tornillo M8 a la torre, desde abajo", ["EjeCarrete"], (0, 0, 1), 70, ["Torre", "Rodamientos"]),
    ("Torre sobre la base", ["Torre", "Rodamientos", "EjeCarrete"], (0, 0, -1), 60, None),
    ("Arandela sobre el rodamiento", ["ArandelaCarrete"], (0, 0, -1), 40, None),
    ("Carrete inferior con su tuerca, enroscado", ["CarreteInferior", "TuercaCarrete"], (0, 0, -1), 40, None),
    ("Disco superior del carrete", ["CarreteSuperior"], (0, 0, -1), 30, None),
    ("Manivela con su tuerca, enroscada", ["Manivela", "TuercaManivela"], (0, 0, -1), 40, None),
    ("Mango y su tornillo, desde arriba", ["Mango", "TornilloMango"], (0, 0, -1), 80, None),
    ("Tuerca del mango, desde abajo", ["TuercaMango"], (0, 0, 1), 20, None),
    ("Botella con su tapa, bajando por la varilla", ["Botella", "Tapa"], (0, 0, -1), 400, None),
    ("Hoja, deslizada desde afuera por la lengüeta", ["Hoja"], (0, -1, 0), 70, None),
    ("Pisador", ["Pisador"], (0, 0, -1), 30, None),
    ("Tornillos de la hoja", ["TornillosHoja"], (0, 0, -1), 40, None),
    ("Vaso de lastre, opcional", ["Lastre"], (0, 0, -1), 60, None),
    ("Sargento a la mesa", ["Sargento"], (0, 0, -1), 40, None),
]
# Contactos de armado que no son choque: rosca sobre rosca, tuerca en su hexágono
PERMITIDOS_ARMADO = PERMITIDOS | {frozenset(p) for p in [
    ("TuercaCarrete", "CarreteInferior"),
]}
armadas = ["Base"]
pasos_res = []
for nombre_paso, mueven, direc, recorrido, contra in PASOS:
    d = V(*direc)
    contra = contra if contra is not None else armadas
    paso_mm = 3.0 if recorrido > 100 else 1.0
    n = int(recorrido / paso_mm)
    malos = []
    for k in range(n + 1):
        desp = d * (-(recorrido - k * paso_mm))       # llega desde -direc
        for m in mueven:
            f = pz0[m]["forma"].copy()
            f.translate(desp)
            for c in contra:
                if c in mueven or frozenset((m, c)) in PERMITIDOS_ARMADO:
                    continue
                v = comun(f, pz0[c]["forma"])
                if v > UMBRAL:
                    malos.append((m, c, round(recorrido - k * paso_mm, 1), round(v, 1)))
    pasos_res.append({"paso": nombre_paso, "ok": not malos, "choques": malos[:5]})
    if malos:
        fallas.append(f"armado: «{nombre_paso}» choca: {malos[:2]}")
    for m in mueven:
        if m not in armadas:
            armadas.append(m)
res["armado"] = pasos_res

# ------------------------------------------------------------- 4. impresión
cos_vol = math.cos(math.radians(90 - P.ANG_VOLADIZO))     # componente Z de la normal
lim_cama = P.CAMA - 2 * P.MARGEN_CAMA
impresas = {n: d["forma"] for n, d in pz0.items() if d["tipo"] == "impresa"}
impresas.pop("Calce")
impresas.update(Z.calces_todos())
fichas = {}
for n, forma in sorted(impresas.items()):
    f = forma.copy()
    f.Placement = Z.a_la_cama(forma).multiply(f.Placement)
    b = f.BoundBox
    tam = (round(b.XLength, 1), round(b.YLength, 1), round(b.ZLength, 1))
    cabe = max(tam[0], tam[1]) <= lim_cama and tam[2] <= P.CAMA
    voladizo, puentes = 0.0, []
    for cara in f.Faces:
        try:
            u0, u1, v0, v1 = cara.ParameterRange
            nrm = cara.normalAt((u0 + u1) / 2, (v0 + v1) / 2)
        except Exception:
            continue
        cb = cara.BoundBox
        if cb.ZMin < 0.2:
            continue                       # apoyada en la cama
        if cara.Surface.__class__.__name__ == "Plane" and nrm.z < -0.999:
            # luz del puente: el menor entre el ancho de la caja y 4·área/perímetro
            # (un anillo alrededor de un agujero puentea su ancho, no su diámetro)
            perim = sum(e.Length for e in cara.Edges)
            luz = min(cb.XLength, cb.YLength, 4 * cara.Area / perim)
            puentes.append(round(luz, 1))
        elif nrm.z < -cos_vol:
            # superficie curva: se mide por triángulos
            pts, tri = cara.tessellate(0.1)
            for i, j, k in tri:
                a, b2, c = pts[i], pts[j], pts[k]
                nn = (b2 - a).cross(c - a)
                area = nn.Length / 2
                if area > 0 and nn.z / nn.Length < -cos_vol:
                    voladizo += area
    puente_max = max(puentes) if puentes else 0.0
    soportes = voladizo > 5.0 or puente_max > P.PUENTE_MAX
    if len(forma.Solids) != 1:
        fallas.append(f"{n} queda en {len(forma.Solids)} partes sueltas")
    fichas[n] = {"tamano_mm": tam, "entra_en_la_cama": cabe, "solidos": len(forma.Solids),
                 "volumen_cm3": round(forma.Volume / 1000, 1),
                 "voladizo_mm2": round(voladizo, 1), "puente_max_mm": puente_max,
                 "puentes": len(puentes), "necesita_soportes": soportes}
    if not cabe:
        fallas.append(f"{n} no entra en la cama: {tam}")
    if soportes:
        fallas.append(f"{n} necesitaría soportes (voladizo {voladizo:.0f} mm², puente {puente_max} mm)")
res["impresion"] = fichas

# ------------------------------------------------------- 5. funcionamiento
T = P.T_DISENO
func = {}
func["ancho_tira_mm"] = P.W
func["vueltas_botella"] = round(P.VUELTAS_BOTELLA, 1)
func["largo_tira_m"] = round(P.LARGO_TIRA / 1000, 2)
func["helice_grados"] = round(math.degrees(P.ALFA), 2)
r_med = (P.R_NUCLEO + P.R_ROLLO_FIN) / 2
func["radio_rollo_mm"] = [P.R_NUCLEO, round(P.R_ROLLO_FIN, 1)]
func["vueltas_manivela"] = round(P.LARGO_TIRA / (2 * math.pi * r_med))
f_mano = T * P.R_ROLLO_FIN / P.R_MANIVELA
func["fuerza_mano_N"] = round(f_mano, 1)
func["tiro_admisible_N"] = round(P.F_MANO_MAX * P.R_MANIVELA / P.R_ROLLO_FIN)
func["tiro_admisible_rollo_mas_grueso_N"] = round(P.F_MANO_MAX * P.R_MANIVELA / P.R_ROLLO_MAX)
if f_mano > P.F_MANO_MAX:
    fallas.append(f"fuerza en la mano {f_mano:.1f} N > {P.F_MANO_MAX:.0f} N")
area = P.W * P.PARED
rotura = area * P.SIGMA_PET
func["rotura_tira_N"] = round(rotura)
func["seguridad_tira"] = round(rotura / T, 1)
if rotura / T < 2:
    fallas.append("la tira rompe con menos del doble del tiro de diseño")

# Avance: el empuje hacia la guía tiene que ganarle a la componente axial del rozamiento
peso_bot = pz0["Botella"]["forma"].Volume * P.DENS_PET / 1000 * P.G
peso_bot_fin = pz1["Botella"]["forma"].Volume * P.DENS_PET / 1000 * P.G
roz_labios = P.MU_PLA_PET * P.FRACCION_NORMAL * T * math.sin(P.ALFA)
# En la tapa el contacto está sobre la varilla, a 4 mm del eje: por vuelta la tapa
# baja w y gira solo 2π·4 mm, así que la bajada pesa mucho más en el deslizamiento
avance_tapa = P.W / math.hypot(P.W, 2 * math.pi * P.VARILLA_D / 2)
roz_tapa = P.MU_TAPA * P.FRACCION_TAPA * T * avance_tapa
roz_axial = roz_labios + roz_tapa
lastre_vacio = pz0["Lastre"]["forma"].Volume * 1.24e-3 / 1000 * P.G
func["peso_botella_N"] = [round(peso_bot, 2), round(peso_bot_fin, 2)]
func["rozamiento_axial_N"] = {"labios": round(roz_labios, 2), "tapa": round(roz_tapa, 2),
                               "total": round(roz_axial, 2)}
func["tapa_inclinacion_deslizamiento"] = round(math.degrees(math.asin(avance_tapa)), 1)
func["peso_vaso_lastre_vacio_N"] = round(lastre_vacio, 2)
falta = max(0.0, 2 * roz_axial - peso_bot_fin)           # margen de 2
func["lastre_total_g"] = math.ceil(falta / P.G * 1000 / 5) * 5
func["agregar_al_vaso_g"] = max(0, math.ceil((falta - lastre_vacio) / P.G * 1000 / 5) * 5)
func["autoavance_sin_lastre"] = peso_bot_fin >= 2 * roz_axial


def lastre_para(mu_tapa):
    """Gramos de lastre total con margen 2, para un rozamiento dado de la tapa."""
    roz = roz_labios + mu_tapa * P.FRACCION_TAPA * T * avance_tapa
    return math.ceil(max(0.0, 2 * roz - peso_bot_fin) / P.G * 1000 / 5) * 5


func["lastre_segun_mu_tapa_g"] = {"diseño (0,30)": lastre_para(P.MU_TAPA)}
for estado, mu in P.MU_PE_ACERO.items():
    func["lastre_segun_mu_tapa_g"][f"PE-acero, {estado} ({mu:.2f})".replace(".", ",")] = lastre_para(mu)
r_in = P.LASTRE_R - P.LASTRE_PARED
vol_vaso = math.pi * (r_in ** 2 - (P.VARILLA_D / 2 + 0.6 + P.LASTRE_PARED) ** 2) * (P.LASTRE_ALTO - P.LASTRE_PARED)
func["vaso_capacidad_tuercas_g"] = round(vol_vaso * P.DENS_TUERCAS)
if func["vaso_capacidad_tuercas_g"] < func["agregar_al_vaso_g"]:
    fallas.append("el lastre necesario no entra en el vaso")

# Anclajes
func["corte_por_tornillo_cabezal_N"] = round(T / len(P.TORNILLOS_CABEZAL), 1)
h = P.Z_GUIA + P.W / 2
ro, ri = P.TORRE_R, P.D_608_ALOJ / 2
w_sec = math.pi * (ro ** 4 - ri ** 4) / (4 * ro)
func["torre_tension_flexion_MPa"] = round(T * h / w_sec, 2)    # tiro aplicado a la altura de la tira
func["torre_seguridad_entre_capas"] = round(15.0 / (T * h / w_sec), 1)  # [REF] ~15 MPa entre capas de PLA

# Ancho: el borde apoya bajo el filo y la pared no puede escaparse
func["ancho_por_construccion_mm"] = round(Z.z_hoja() - P.Z_GUIA, 3)
y_ranura = P.R_B - P.PARED / 2
func["chapita_llega_bajo_el_filo"] = (P.CHAPITA_X[1] >= 0.0 and P.CHAPITA_Y[0] < y_ranura < P.CHAPITA_Y[1])
func["chapita_aguas_arriba_mm"] = round(math.sqrt(y_ranura ** 2 - P.CHAPITA_Y[0] ** 2), 1)
func["chapita_aguas_abajo_mm"] = P.CHAPITA_X[1]
func["placa_cabezal_mm"] = P.Z_PISO - P.TACO_ALTO
func["ranura_mm"] = round(P.PARED + 2 * P.HOLG_RANURA, 2)
func["espesor_calce_mm"] = round(Z.espesor_calce(P.W), 2)
# el borde de la botella toca la chapita y no el PLA del cabezal
d_pla = min(pz0["Botella"]["forma"].distToShape(pz0[n]["forma"])[0] for n in ("Cabezal", "LabioExterior"))
d_met = pz0["Botella"]["forma"].distToShape(pz0["Chapita"]["forma"])[0]
func["borde_a_pla_mm"] = round(d_pla, 3)
func["borde_apoya_en_chapita"] = d_met < 1e-3 and d_pla >= 0.05
func["labio_interior_bajo_la_hoja"] = P.ALTO_LABIO_INT < P.W_MIN
func["carrete_toma_la_tira"] = (P.Z_CORE0 <= P.Z_GUIA - 0.5 and P.Z_CORE1 >= P.Z_GUIA + P.W_MAX + 0.5)
for clave in ("chapita_llega_bajo_el_filo", "labio_interior_bajo_la_hoja", "carrete_toma_la_tira",
              "borde_apoya_en_chapita"):
    if not func[clave]:
        fallas.append(f"funcionamiento: {clave} = False")
if abs(func["ancho_por_construccion_mm"] - P.W) > 1e-6:
    fallas.append("el ancho no coincide con el calce")
res["funcionamiento"] = func

res["fallas"] = fallas
with open(os.path.join(CARPETA, "resultados.json"), "w", encoding="utf-8") as fh:
    json.dump(res, fh, ensure_ascii=False, indent=1)
sys.stdout.flush()
os._exit(1 if fallas else 0)
