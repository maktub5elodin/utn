# -*- coding: utf-8 -*-
"""
DXF R2000 con ezdxf, a partir de lo que registró planos.py. Corre en el Python del sistema:
    /usr/bin/python3 dxf.py
Audita cada archivo al escribirlo y termina con error si ezdxf encuentra alguno.
"""
import glob, json, os, sys

import ezdxf
from ezdxf.enums import TextEntityAlignment

CARPETA = os.path.dirname(os.path.abspath(__file__))
# Metadatos fijos: el mismo modelo da el mismo archivo y git no ve cambios falsos.
ezdxf.options.write_fixed_meta_data_for_testing = True

CAPAS = [  # nombre, color, tipo de línea, grosor en centésimas de mm
    ("Contornos", 3, "Continuous", 50),     # gruesa continua
    ("Ocultas", 6, "DASHED", 25),           # fina de trazos
    ("Ejes", 1, "CENTER", 25),              # fina de trazo largo y punto
    ("Cotas", 5, "Continuous", 25),         # fina continua
    ("Texto", 8, "Continuous", 25),         # rótulo, tablas y notas
    ("Extremas", 30, "DIVIDE", 25),         # fina de trazo largo y dos puntos
    ("Finas", 4, "Continuous", 25),         # fondo de rosca y de diente
    ("Marco", 7, "Continuous", 70),         # recuadro y marcas de centrado
]
# Nombres estándar (LibreCAD no admite otros). Patrón con d = 0,25 mm: 12d, 3d, 24d y 0,5d.
TIPOS = [
    ("DASHED", "Trazos", [3.75, 3.0, -0.75]),
    ("CENTER", "Trazo largo y punto", [7.625, 6.0, -0.75, 0.125, -0.75]),
    ("DIVIDE", "Trazo largo y dos puntos",
     [8.5, 6.0, -0.75, 0.125, -0.75, 0.125, -0.75]),
]
ALIN = {"i": TextEntityAlignment.LEFT, "c": TextEntityAlignment.CENTER,
        "d": TextEntityAlignment.RIGHT}
FUENTE = "iso3098.shx"
ALTO_COTA, FLECHA = 3.5, 3.5


def documento(E, ancho, alto):
    doc = ezdxf.new("R2000", setup=False, units=ezdxf.units.MM)
    h = doc.header
    h["$MEASUREMENT"] = 1
    h["$LUNITS"] = 2
    h["$LTSCALE"] = E
    h["$LWDISPLAY"] = 1
    h["$LIMMAX"] = (ancho * E, alto * E)
    h["$PLIMMIN"] = (0, 0)
    h["$PLIMMAX"] = (ancho, alto)
    h["$TEXTSTYLE"] = "IRAM"
    h["$CLAYER"] = "Contornos"
    for var, val in (("$DIMSCALE", E), ("$DIMASZ", FLECHA), ("$DIMEXO", 1.0), ("$DIMEXE", 2.0),
                     ("$DIMGAP", 1.0), ("$DIMTXT", ALTO_COTA), ("$DIMTAD", 1), ("$DIMTIH", 0),
                     ("$DIMTOH", 0), ("$DIMDEC", 0), ("$DIMDSEP", 44), ("$DIMLUNIT", 2)):
        h[var] = val
    for nombre, desc, patron in TIPOS:
        doc.linetypes.add(nombre, pattern=patron, description=desc)
    for nombre, color, tipo, gros in CAPAS:
        doc.layers.add(nombre, color=color, linetype=tipo, lineweight=gros)
    doc.styles.add("IRAM", font=FUENTE)
    # Flecha de la cátedra: triángulo ennegrecido, largo 4 veces el ancho
    bloque = doc.blocks.new("FLECHA41")
    bloque.add_solid([(0, 0), (-1, 0.125), (-1, -0.125)], dxfattribs={"layer": "0"})
    estilo = doc.dimstyles.add("IRAM")
    estilo.dxf.dimscale = E
    estilo.dxf.dimasz = FLECHA
    estilo.dxf.dimblk = "FLECHA41"
    estilo.dxf.dimexo = 1.0
    estilo.dxf.dimexe = 2.0
    estilo.dxf.dimgap = 1.0
    estilo.dxf.dimtxt = ALTO_COTA
    estilo.dxf.dimtad = 1
    estilo.dxf.dimtih = 0
    estilo.dxf.dimtoh = 0
    estilo.dxf.dimdec = 0
    estilo.dxf.dimdsep = 44
    estilo.dxf.dimlunit = 2
    estilo.dxf.dimtxsty = "IRAM"
    h["$DIMSTYLE"] = "IRAM"
    return doc


def escribir(ruta_json, ruta_dxf):
    with open(ruta_json, encoding="utf-8") as f:
        dat = json.load(f)
    doc = documento(dat["escala"], dat["ancho"], dat["alto"])
    msp = doc.modelspace()
    for op in dat["ops"]:
        t = op[0]
        if t == "l":
            msp.add_line(op[2], op[3], dxfattribs={"layer": op[1]})
        elif t == "c":
            msp.add_circle(op[2], op[3], dxfattribs={"layer": op[1]})
        elif t == "a":
            msp.add_arc(op[2], op[3], op[4], op[5], dxfattribs={"layer": op[1]})
        elif t == "p":
            msp.add_lwpolyline(op[2], close=op[3], dxfattribs={"layer": op[1]})
        elif t == "s":
            msp.add_solid([op[2], op[3], op[4]], dxfattribs={"layer": op[1]})
        elif t == "t":
            _, capa, x, y, H, s, alin, rot = op
            msp.add_text(s, height=H, rotation=rot,
                         dxfattribs={"layer": capa, "style": "IRAM"}
                         ).set_placement((x, y), align=ALIN[alin])
        elif t == "d":
            _, a, b, base, ang, s = op
            msp.add_linear_dim(base=base, p1=a, p2=b, angle=ang, text=s, dimstyle="IRAM",
                               dxfattribs={"layer": "Cotas"}).render()
    auditoria = doc.audit()
    doc.saveas(ruta_dxf)
    return len(auditoria.errors), len(auditoria.fixes)


def main():
    salida = os.path.join(CARPETA, "planos")
    fallas = 0
    for ruta in sorted(glob.glob(os.path.join(CARPETA, "build", "planos_json", "*.json"))):
        nombre = os.path.splitext(os.path.basename(ruta))[0]
        err, fix = escribir(ruta, os.path.join(salida, nombre + ".dxf"))
        print(f"{nombre}: {err} errores, {fix} corregidos")
        fallas += err
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
