# -*- coding: utf-8 -*-
"""
Imágenes y datos del instructivo de armado (instructivo/), sin pantalla:
    CARPETA_MODELO=$PWD QT_QPA_PLATFORM=offscreen ~/Aplicaciones/FreeCAD.AppImage vistas_armado.py
Lo lanza el Makefile (make armado_pdf).

  instructivo/pasos/paso_NN.png   un render por paso de armado.PASOS: lo ya armado en
                                  gris claro, la pieza nueva en color y una flecha que
                                  indica por dónde entra; la misma cámara en toda la etapa
  instructivo/pasos/portada.png   la máquina armada
  build/armado.json               contornos y agujeros de la base, y medidas del modelo
                                  que cita el texto

PASOS=1,5 renderiza solo esos pasos (para probar cámaras).
"""
import json, math, os, sys, traceback

CARPETA = os.environ.get("CARPETA_MODELO", os.getcwd())
sys.path.insert(0, CARPETA)

import FreeCAD as App
import FreeCADGui as Gui
import Part
from PIL import Image
from pivy import coin

import armado as A
import parametros as P
import piezas as Z

V = App.Vector
ANCHO, ALTO, SS = 1500, 900, 2
GRIS, GRIS_BASE = (0.90, 0.90, 0.91), (0.96, 0.96, 0.96)
NUEVA, FLECHA = (0.96, 0.45, 0.08), (0.78, 0.08, 0.10)
FONDO = "#FFFFFF"

# Cámara de cada etapa: (posición, punto al que mira, ángulo vertical) y largo de la flecha
CAMARAS = [
    (((-230.0, -200.0, 190.0), (0.0, 5.0, 30.0), 19.0), 24.0),
    (((170.0, -150.0, 210.0), (2.0, 60.0, 30.0), 25.0), 26.0),
    (((-40.0, -190.0, 180.0), (50.0, 50.0, 22.0), 24.0), 26.0),
    (((70.0, -230.0, 250.0), (205.0, 23.0, 68.0), 29.0), 34.0),
    (((-330.0, -420.0, 420.0), (20.0, 30.0, 140.0), 32.0), 50.0),
    (((120.0, 240.0, 210.0), (6.0, 64.0, 48.0), 28.0), 28.0),
    (((-430.0, 780.0, 600.0), (20.0, 20.0, 150.0), 24.0), 45.0),
]
ACERCAR = 0.6          # subconjuntos fuera de la base: misma dirección de la cámara, más cerca
# Flechas que no van pegadas a la pieza: la varilla y la botella son largas y la
# punta de la pieza queda fuera del cuadro. (punta de la flecha, largo)
FLECHA_EN = {
    "varilla": ((16.0, 0.0, P.ZOCALO_ALTO + 45), 45.0),
}
TRANSPARENTES = {               # lo ya armado que taparía la pieza nueva
    "tuercas_cabezal": ["Cabezal"],
    "rodamientos": ["Torre"],
    "eje_carrete": ["Torre", "Rodamientos"],
    "hoja": ["Botella"],
    "pisador": ["Botella"],
    "tornillos_hoja": ["Botella"],
}
SIEMPRE_TRANSLUCIDAS = {"Botella": 55, "Tapa": 40}


def flecha(punta, direc, largo):
    """Flecha sólida que termina en punta y apunta en direc."""
    d = V(*direc)
    r = max(1.6, largo * 0.07)
    cabeza = largo * 0.35
    inicio = punta - d * largo
    cuerpo = Part.makeCylinder(r, largo - cabeza, inicio, d)
    cono = Part.makeCone(r * 2.4, 0, cabeza, punta - d * cabeza, d)
    return cuerpo.fuse(cono)


class Escena:
    def __init__(self, pz):
        self.doc = App.newDocument("Instructivo")
        self.obj = {}
        for n, d in pz.items():
            if n == "Tira":
                continue
            o = self.doc.addObject("Part::Feature", n)
            o.Shape = d["forma"]
            self.obj[n] = o
        self.flecha = self.doc.addObject("Part::Feature", "Flecha")
        self.flecha.Shape = Part.makeBox(1, 1, 1)
        self.flecha.ViewObject.ShapeColor = FLECHA
        self.doc.recompute()
        self.vista = Gui.getDocument(self.doc.Name).activeView()
        self.vista.setAnimationEnabled(False)
        self.vista.setCameraType("Perspective")
        self.cam = self.vista.getCameraNode()

    def camara(self, pos, obj, angulo):
        self.cam.position.setValue(coin.SbVec3f(*pos))
        self.cam.pointAt(coin.SbVec3f(*obj), coin.SbVec3f(0, 0, 1))
        self.cam.heightAngle.setValue(math.radians(angulo))
        self.cam.nearDistance.setValue(20)
        self.cam.farDistance.setValue(5000)

    def foto(self, ruta):
        crudo = ruta + ".crudo.png"
        self.vista.saveImage(crudo, ANCHO * SS, ALTO * SS, FONDO)
        img = Image.open(crudo).convert("RGB").resize((ANCHO, ALTO), Image.LANCZOS)
        os.remove(crudo)
        img.save(ruta, optimize=True)


def pintar(esc, grises, nuevas, transparentes):
    for n, o in esc.obj.items():
        vo = o.ViewObject
        vo.Visibility = n in grises or n in nuevas
        if not vo.Visibility:
            continue
        if n in nuevas:
            vo.ShapeColor = NUEVA
        else:
            vo.ShapeColor = GRIS_BASE if n == "Base" else GRIS
        t = SIEMPRE_TRANSLUCIDAS.get(n, 0)
        if n in transparentes:
            t = 70
        vo.Transparency = t


def pasos(esc, pz, solo):
    armadas = ["Base"]
    carpeta = os.path.join(CARPETA, "instructivo", "pasos")
    os.makedirs(carpeta, exist_ok=True)
    for i, paso in enumerate(A.PASOS, 1):
        mueven = paso["mueven"]
        grises = paso["contra"] if paso["contra"] is not None else list(armadas)
        if not solo or i in solo:
            pintar(esc, grises, mueven, TRANSPARENTES.get(paso["clave"], []))
            (pos, obj, ang), largo = CAMARAS[paso["etapa"]]
            if paso["clave"] in FLECHA_EN:
                punta, largo = FLECHA_EN[paso["clave"]]
                punta = V(*punta)
            else:
                caja = App.BoundBox()
                for m in mueven:
                    caja.add(pz[m]["forma"].BoundBox)
                d = V(*paso["direc"])
                c = caja.Center
                medio = abs(d.x) * caja.XLength / 2 + abs(d.y) * caja.YLength / 2 + abs(d.z) * caja.ZLength / 2
                punta = c - d * (medio + 4.0)
            if paso["contra"] is not None:
                caja = App.BoundBox()
                for m in grises + mueven:
                    caja.add(pz[m]["forma"].BoundBox)
                c = caja.Center
                pos = [c[k] + (pos[k] - obj[k]) * ACERCAR for k in range(3)]
                obj = (c.x, c.y, c.z)
                largo *= 0.6
            esc.flecha.Shape = flecha(punta, paso["direc"], largo)
            esc.flecha.ViewObject.Visibility = True
            esc.doc.recompute()
            esc.camara(pos, obj, ang)
            esc.foto(os.path.join(carpeta, f"paso_{i:02d}.png"))
        for m in mueven:
            if m not in armadas:
                armadas.append(m)
    # portada: la máquina armada, con sus colores
    if not solo or 0 in solo:
        for n, o in esc.obj.items():
            vo = o.ViewObject
            vo.Visibility = True
            tipo = pz[n]["tipo"]
            vo.ShapeColor = Z.COLORES["mdf"] if n in ("Base", "Taco") else Z.COLORES[tipo]
            vo.Transparency = SIEMPRE_TRANSLUCIDAS.get(n, 0)
        esc.flecha.ViewObject.Visibility = False
        tira = esc.doc.addObject("Part::Feature", "Tira")
        tira.Shape = pz["Tira"]["forma"]
        tira.ViewObject.ShapeColor = Z.COLORES["tira"]
        esc.doc.recompute()
        esc.camara((-430.0, 780.0, 600.0), (60.0, 20.0, 150.0), 33.0)
        esc.foto(os.path.join(carpeta, "portada.png"))


# ------------------------------------------------------------------ datos
def r1(x):
    return round(x, 2)


def contorno(forma, z=0.3):
    """Contornos de la pieza a la altura z sobre la base, como listas de (x, y)."""
    out = []
    for w in forma.slice(V(0, 0, 1), z):
        pts = w.discretize(Deflection=0.05)
        out.append([(r1(p.x), r1(p.y)) for p in pts])
    return out


def datos(pz):
    x0, y0 = P.MDF_ORIGEN
    sarg = [c for c in contorno(pz["Sargento"]["forma"], 0.5)
            if x0 < sum(p[0] for p in c) / len(c) < x0 + P.MDF[0]]
    piezas = {n: contorno(pz[n]["forma"]) for n in ("Zocalo", "Taco", "Ojal", "Torre")}
    piezas["Sargento"] = sarg
    b = {n: pz[n]["forma"].BoundBox for n in pz}
    out = {
        "base": {"origen": [x0, y0], "largo": P.MDF[0], "ancho": P.MDF[1], "espesor": P.MDF[2]},
        "contornos": piezas,
        "agujeros": [{"pieza": n, "x": r1(x), "y": r1(y), "desde": "abajo" if e is None else "arriba",
                      "espesor_pieza": e} for n, x, y, e in Z.tornillos_a_la_base()],
        "varilla_xy": [0.0, 0.0],
        "calces": {str(int(w)): r1(Z.espesor_calce(w)) for w in P.CALCES},
        "medidas": {
            "varilla_en_zocalo": r1(P.ZOCALO_ALTO - P.ZOCALO_FONDO),
            "varilla_arriba_de_la_base": r1(b["Varilla"].ZMax),
            "placa_arriba_de_la_base": r1(b["Cabezal"].ZMin + (P.Z_PISO - P.TACO_ALTO)),
            "chapita_bajo_el_piso": r1(P.Z_PISO - P.Z_GUIA),
            "pozo_chapita": r1(P.POZO_ALTO),
            "ranura_labios": r1(P.PARED + 2 * P.HOLG_RANURA),
            "punta_hoja_dentro": r1(P.R_B - b["Hoja"].YMin),
            "hoja_sobresale_afuera": r1(b["Hoja"].YMax - P.CALCE_Y[1]),
            "tornillo_m8_sobre_torre": r1(b["EjeCarrete"].ZMax - P.TORRE_ALTO),
            "cabeza_m8_sobre_base": r1(b["EjeCarrete"].ZMin),
            "rodamientos_separacion": r1(P.TORRE_ALTO - P.TORRE_CAVIDAD[1] - 2 * P.ANCHO_608),
            "mango_juego": r1(b["Mango"].ZMin - (P.Z_MANIVELA + P.MANIVELA_ESP)),
            "tornillo_hoja_en_taco": r1(P.TACO_ALTO - b["TornillosHoja"].ZMin),
            "tuerca_m3_hundida": r1(P.PROF_TUERCA - P.M3_ALTO),
            "tapa_a_la_varilla": r1(P.TAPA_AGUJERO - P.VARILLA_D),
            "manivela_a_botella": r1(math.hypot(P.X_CARRETE, P.Y_CARRETE) - P.R_MANIVELA - P.MANGO_R - P.R_B),
            "ojal_ranura": P.OJAL_HUECO,
            "hoja_a_carrete": r1(P.X_CARRETE + math.pi * P.R_NUCLEO),
            "ranura_nucleo": P.RANURA_ENGANCHE,
        },
    }
    with open(os.path.join(CARPETA, "build", "armado.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)


def main():
    pz = Z.conjunto(0.0)
    solo = {int(x) for x in os.environ["PASOS"].split(",")} if os.environ.get("PASOS") else None
    if not solo:
        datos(pz)
    pasos(Escena(pz), pz, solo)


codigo = 1
try:
    main()
    codigo = 0
except Exception:
    with open(os.path.join(CARPETA, "build", "armado_error.txt"), "w") as fh:
        fh.write(traceback.format_exc())
finally:
    sys.stdout.flush()
    os._exit(codigo)
