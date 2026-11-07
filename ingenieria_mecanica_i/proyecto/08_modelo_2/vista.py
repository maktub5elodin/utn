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
    miniaturas(pz)
    return True


def miniaturas(pz):
    """Una imagen chica por pieza impresa, tal como va en la cama, para la ficha."""
    formas = {n: d["forma"] for n, d in pz.items() if d["tipo"] == "impresa" and n != "Calce"}
    formas.update(Z.calces_todos())
    carpeta = os.path.join(CARPETA, "ficha", "miniaturas")
    os.makedirs(carpeta, exist_ok=True)
    doc = App.newDocument("Miniaturas")
    pieza = doc.addObject("Part::Feature", "Pieza")
    cama = doc.addObject("Part::Feature", "Cama")
    pieza.ViewObject.ShapeColor = Z.COLORES["impresa"]
    cama.ViewObject.ShapeColor = (0.80, 0.82, 0.85)
    vista = Gui.getDocument(doc.Name).activeView()
    vista.setAnimationEnabled(False)
    for n, forma in sorted(formas.items()):
        f = forma.copy()
        f.Placement = Z.a_la_cama(forma).multiply(f.Placement)
        b = f.BoundBox
        m = max(6.0, 0.15 * max(b.XLength, b.YLength))      # borde de cama alrededor
        pieza.Shape = f
        cama.Shape = Z.caja((-m, b.XLength + m), (-m, b.YLength + m), (-1.0, 0.0))
        doc.recompute()
        vista.viewIsometric()
        vista.fitAll()
        ruta = os.path.join(carpeta, f"{n}.png")
        vista.saveImage(ruta, 880, 660, "White")
        recortar(ruta)


def recortar(ruta, ancho=400, alto=300, margen=10):
    """Recorta el blanco alrededor y centra la pieza en una imagen de 4:3."""
    from PIL import Image, ImageChops
    img = Image.open(ruta).convert("RGB")
    caja = ImageChops.difference(img, Image.new("RGB", img.size, "white")).getbbox()
    img = img.crop(caja)
    k = min((ancho - 2 * margen) / img.width, (alto - 2 * margen) / img.height)
    img = img.resize((round(img.width * k), round(img.height * k)), Image.LANCZOS)
    lienzo = Image.new("RGB", (ancho, alto), "white")
    lienzo.paste(img, ((ancho - img.width) // 2, (alto - img.height) // 2))
    # fondo transparente, así la miniatura no corta el rayado de la tabla
    rgba = lienzo.convert("RGBA")
    rgba.putdata([(r, g, b, 0) if min(r, g, b) >= 250 else (r, g, b, 255) for r, g, b, _ in rgba.getdata()])
    rgba.save(ruta)


codigo = 1
try:
    codigo = 0 if main() else 1
except Exception:
    with open(os.path.join(CARPETA, "build", "vista_error.txt"), "w") as f:
        f.write(traceback.format_exc())
finally:
    sys.stdout.flush()
    os._exit(codigo)
