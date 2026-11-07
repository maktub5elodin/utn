# -*- coding: utf-8 -*-
"""
Modelo para abrir en FreeCAD (modelo/cortadora_v2.FCStd) y figuras de vista
previa (figuras/*.png). Necesita la interfaz, sin pantalla:
    CARPETA_MODELO=$PWD QT_QPA_PLATFORM=offscreen ~/Aplicaciones/FreeCAD.AppImage vista.py
"""
import os, sys, traceback

CARPETA = os.environ.get("CARPETA_MODELO", os.getcwd())
sys.path.insert(0, CARPETA)

import FreeCAD as App
import FreeCADGui as Gui

import parametros as P
import piezas as Z

ANCHO, ALTO = 1600, 1000


def color(nombre, tipo):
    if nombre in ("Base", "Taco"):
        return Z.COLORES["mdf"]
    if nombre == "Tira":
        return Z.COLORES["tira"]
    return Z.COLORES[tipo]


def main():
    doc = App.newDocument("Cortadora_v2")
    pz = Z.conjunto(0.0)
    for n, d in pz.items():
        o = doc.addObject("Part::Feature", n)
        o.Shape = d["forma"]
        o.ViewObject.ShapeColor = color(n, d["tipo"])
        if n in ("Botella", "Tapa"):
            o.ViewObject.Transparency = 60
        if n == "Lastre":
            o.ViewObject.Transparency = 40
    doc.recompute()
    os.makedirs(os.path.join(CARPETA, "modelo"), exist_ok=True)
    os.makedirs(os.path.join(CARPETA, "figuras"), exist_ok=True)
    doc.saveAs(os.path.join(CARPETA, "modelo", "cortadora_v2.FCStd"))

    vista = Gui.getDocument(doc.Name).activeView()
    vista.setAnimationEnabled(False)
    vista.viewIsometric()
    vista.fitAll()
    vista.saveImage(os.path.join(CARPETA, "figuras", "conjunto.png"), ANCHO, ALTO, "White")

    # Detalle del cabezal: sin la botella, se ve la ranura, la hoja y la tira
    for n in ("Botella", "Tapa", "Lastre", "Varilla"):
        doc.getObject(n).ViewObject.Visibility = False
    Gui.Selection.clearSelection()
    for n in ("Cabezal", "Hoja", "Pisador", "Ojal"):
        Gui.Selection.addSelection(doc.getObject(n))
    vista.viewIsometric()
    Gui.SendMsgToActiveView("ViewSelection")
    Gui.Selection.clearSelection()
    vista.saveImage(os.path.join(CARPETA, "figuras", "detalle_cabezal.png"), ANCHO, ALTO, "White")
    return True


codigo = 1
try:
    codigo = 0 if main() else 1
except Exception:
    with open(os.path.join(CARPETA, "build", "vista_error.txt"), "w") as f:
        f.write(traceback.format_exc())
finally:
    sys.stdout.flush()
    os._exit(codigo)
