# -*- coding: utf-8 -*-
"""
STEP para SolidWorks: posición inicial del corte, un sólido por pieza, con su
nombre y su color. Necesita la interfaz de FreeCAD (sin pantalla), porque los
colores viven en la vista:
    CARPETA_MODELO=$PWD QT_QPA_PLATFORM=offscreen ~/Aplicaciones/FreeCAD.AppImage exportar_step.py

Lo vuelve a abrir, compara cantidad de sólidos y volumen, y deja el resultado
en resultados.json. La tira no se exporta: es ilustrativa.
"""
import json, os, re, sys, traceback

CARPETA = os.environ.get("CARPETA_MODELO", os.getcwd())
sys.path.insert(0, CARPETA)

import FreeCAD as App
import FreeCADGui as Gui
import Import
import ImportGui
import Part

import parametros as P
import piezas as Z

FECHA_FIJA = "2026-11-02T00:00:00"     # para que el archivo no cambie sin motivo
RUTA = os.path.join(CARPETA, "salida", "cortadora_pet.step")
TOL_VOLUMEN = 1e-5                     # diferencia relativa admitida


def huella(texto):
    """Geometría (todo lo anterior a los colores) más la paleta."""
    corte = texto.find("MECHANICAL_DESIGN_GEOMETRIC_PRESENTATION")
    paleta = sorted(set(re.findall(r"COLOUR_RGB\([^;]*;", texto)))
    return texto[:corte], paleta


def solidos():
    """(nombre, sólido, color). Una pieza con varios sólidos se numera."""
    lista = []
    pz = {n: (d[0], d[1]) for n, d in Z.formas().items()}
    pz["Botella"] = (Z.botella_solida(), None)
    pz["Husillo"] = (Z.husillo_liso(), "gira")
    for nombre, (forma, grupo) in pz.items():
        color = Z.COLOR_PET if grupo is None else Z.COLORES[grupo]
        partes = forma.Solids
        for k, s in enumerate(partes):
            sufijo = f"_{k + 1}" if len(partes) > 1 else ""
            lista.append((nombre + sufijo, s, color))
    return lista


def main():
    os.makedirs(os.path.dirname(RUTA), exist_ok=True)
    doc = App.newDocument("Cortadora_STEP")
    objetos = []
    for nombre, solido, color in solidos():
        o = doc.addObject("Part::Feature", nombre)
        o.Label = nombre
        o.Shape = solido
        o.ViewObject.ShapeColor = color
        objetos.append(o)
    doc.recompute()
    TEMPORAL = RUTA + ".tmp.step"
    ImportGui.export(objetos, TEMPORAL)
    n_orig = len(objetos)
    v_orig = sum(o.Shape.Volume for o in objetos)
    nombres_orig = sorted(o.Name for o in objetos)
    App.closeDocument(doc.Name)

    # Sin fecha de generación: el mismo modelo da el mismo archivo.
    with open(TEMPORAL, encoding="utf-8", errors="surrogateescape", newline="") as f:
        texto = f.read()
    os.remove(TEMPORAL)
    texto = re.sub(r"(FILE_NAME\('[^']*',')[^']*'",
                   lambda m: m.group(1) + FECHA_FIJA + "'", texto, count=1)
    texto = re.sub(r"(FILE_NAME\(')[^']*'", r"\1cortadora_pet.step'", texto, count=1)
    # OCCT ordena los colores al azar en cada exportación: si la geometría y la
    # paleta no cambiaron, se conserva el archivo anterior y git no ve diferencias.
    previo = None
    if os.path.exists(RUTA):
        with open(RUTA, encoding="utf-8", errors="surrogateescape", newline="") as f:
            previo = f.read()
    if previo is None or huella(previo) != huella(texto):
        with open(RUTA, "w", encoding="utf-8", errors="surrogateescape", newline="") as f:
            f.write(texto)

    # Reapertura: como forma y como documento con nombres y colores.
    forma = Part.read(RUTA)
    n_step = len(forma.Solids)
    v_step = sum(s.Volume for s in forma.Solids)
    doc2 = App.newDocument("Reapertura")
    ImportGui.insert(RUTA, doc2.Name)
    doc2.recompute()
    etiquetas = sorted(o.Label for o in doc2.Objects
                       if o.TypeId == "Part::Feature" and o.Shape.Solids)
    colores = set()
    for o in doc2.Objects:
        if o.TypeId == "Part::Feature" and o.Shape.Solids:
            colores.add(tuple(round(c, 2) for c in o.ViewObject.ShapeColor[:3]))
    dif = abs(v_step - v_orig) / v_orig
    res = {
        "solidos_modelo": n_orig,
        "solidos_step": n_step,
        "volumen_modelo_mm3": round(v_orig, 1),
        "volumen_step_mm3": round(v_step, 1),
        "diferencia_relativa": float(f"{dif:.2e}"),
        "nombres_conservados": etiquetas == nombres_orig,
        "colores_distintos_al_reabrir": len(colores),
        "tamano_bytes": os.path.getsize(RUTA),
    }
    ok = n_step == n_orig and dif <= TOL_VOLUMEN and etiquetas == nombres_orig
    res["ok"] = ok
    if not ok:
        res["etiquetas_step"] = etiquetas
    ruta_res = os.path.join(CARPETA, "resultados.json")
    with open(ruta_res, encoding="utf-8") as f:
        todo = json.load(f)
    todo["step"] = res
    with open(ruta_res, "w", encoding="utf-8") as f:
        json.dump(todo, f, ensure_ascii=False, indent=1)
    return ok


codigo = 1
try:
    codigo = 0 if main() else 1
except Exception:
    with open(os.path.join(CARPETA, "build_error.txt"), "a") as f:
        f.write(traceback.format_exc())
finally:
    sys.stdout.flush()
    os._exit(codigo)
