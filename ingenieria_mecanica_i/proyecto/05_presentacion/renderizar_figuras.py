# -*- coding: utf-8 -*-
"""
Renders del modelo 2.0 para la presentación (figuras/render_explotada.png y figuras/render_carrete_manivela.png).
Usa las piezas de ../08_modelo_2 sin modificarlas. Necesita la interfaz de FreeCAD, sin pantalla:
    QT_QPA_PLATFORM=offscreen ~/Aplicaciones/FreeCAD.AppImage renderizar_figuras.py
Escribe en build/render.json la luz medida entre la tuerca del mango y la tira.
"""
import json, math, os, sys, traceback

AQUI = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
AQUI = os.environ.get("CARPETA_PRESENTACION", AQUI)
MODELO = os.path.join(AQUI, "..", "08_modelo_2")
sys.path.insert(0, MODELO)

import FreeCAD as App
import FreeCADGui as Gui

import parametros as P
import piezas as Z

ANCHO, ALTO = 1600, 1000
FIG = os.path.join(AQUI, "figuras")
OCULTAS = ("Sargento", "Botella", "Tapa", "Lastre", "Tira")

# Vista explotada: cada pieza sube por su eje de armado (mm).
SUBE = {
    "Zocalo": 25, "TuercaPrisionero": 25, "Prisionero": 25, "Varilla": 70,
    "Taco": 0, "TuercasHoja": 22, "Cabezal": 40, "Chapita": 58, "LabioExterior": 72, "Calce": 88,
    "Hoja": 106, "Pisador": 124, "TornillosHoja": 150,
    "Ojal": 25,
    "Torre": 20, "EjeCarrete": 20, "Rodamientos": 48, "ArandelaCarrete": 72,
    "CarreteInferior": 92, "TuercaCarrete": 92, "CarreteSuperior": 112,
    "Manivela": 134, "TuercaManivela": 134, "TuercaMango": 134, "Mango": 160, "TornilloMango": 160,
}
# Las piezas que bajan del lado de la mano, en el mismo orden en que se arman
GIRA_CON_MANIVELA = ("Manivela", "TuercaManivela", "Mango", "TornilloMango", "TuercaMango")


def color(nombre, tipo):
    if nombre in ("Base", "Taco"):
        return Z.COLORES["mdf"]
    if nombre == "Tira":
        return Z.COLORES["tira"]
    return Z.COLORES[tipo]


def documento(nombre, pz):
    doc = App.newDocument(nombre)
    for n, d in pz.items():
        o = doc.addObject("Part::Feature", n)
        o.Shape = d["forma"]
        o.ViewObject.ShapeColor = color(n, d["tipo"])
        o.ViewObject.Visibility = n not in OCULTAS
    doc.recompute()
    vista = Gui.getDocument(doc.Name).activeView()
    vista.setAnimationEnabled(False)
    return doc, vista


def explotada():
    pz = Z.conjunto(0.0)
    for n, d in pz.items():
        if n in SUBE:
            f = d["forma"].copy()
            f.translate(App.Vector(0, 0, SUBE[n]))
            d["forma"] = f
    doc, vista = documento("Explotada", pz)
    doc.getObject("Varilla").ViewObject.Visibility = False   # 400 mm: achica todo lo demás
    vista.viewIsometric()
    vista.fitAll()
    vista.saveImage(os.path.join(FIG, "render_explotada.png"), 2 * ANCHO, 2 * ALTO, "White")
    App.closeDocument(doc.Name)


def girar(forma, grados):
    f = forma.copy()
    f.rotate(App.Vector(P.X_CARRETE, P.Y_CARRETE, 0), App.Vector(0, 0, 1), grados)
    return f


def carrete_manivela():
    """La manivela, girada hasta pasar sobre la tira: ahí la tuerca del mango queda más cerca."""
    pz = Z.conjunto(0.0)
    tira = pz["Tira"]["forma"]
    tuerca = pz["TuercaMango"]["forma"]
    mejor = min(range(0, 360, 2), key=lambda a: girar(tuerca, a).distToShape(tira)[0])
    luz = girar(tuerca, mejor).distToShape(tira)[0]
    for n in GIRA_CON_MANIVELA:
        pz[n]["forma"] = girar(pz[n]["forma"], mejor)
    doc, vista = documento("Carrete", pz)
    for n in ("Tira",):
        doc.getObject(n).ViewObject.Visibility = True
    for n in ("Zocalo", "Varilla", "Prisionero", "TuercaPrisionero"):
        doc.getObject(n).ViewObject.Visibility = False
    Gui.Selection.clearSelection()
    for n in ("Torre", "CarreteInferior", "Manivela", "Mango", "Ojal"):
        Gui.Selection.addSelection(doc.getObject(n))
    vista.setCameraOrientation(App.Rotation(App.Vector(0, 0, 1), -35).multiply(App.Rotation(App.Vector(1, 0, 0), 68)))
    Gui.SendMsgToActiveView("ViewSelection")
    Gui.Selection.clearSelection()
    ruta = os.path.join(FIG, "render_carrete_manivela.png")
    vista.saveImage(ruta, ANCHO, ALTO, "White")
    App.closeDocument(doc.Name)
    return {"angulo_manivela_grados": mejor, "luz_tuerca_mango_tira_mm": round(luz, 2)}


def main():
    os.makedirs(FIG, exist_ok=True)
    os.makedirs(os.path.join(AQUI, "build"), exist_ok=True)
    explotada()
    datos = carrete_manivela()
    with open(os.path.join(AQUI, "build", "render.json"), "w") as f:
        json.dump(datos, f, indent=1)
    return True


codigo = 1
try:
    codigo = 0 if main() else 1
except Exception:
    os.makedirs(os.path.join(AQUI, "build"), exist_ok=True)
    with open(os.path.join(AQUI, "build", "render_error.txt"), "w") as f:
        f.write(traceback.format_exc())
finally:
    sys.stdout.flush()
    os._exit(codigo)
