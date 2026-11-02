# -*- coding: utf-8 -*-
"""
Control independiente de los DXF, con el Python del sistema:
    /usr/bin/python3 control_dxf.py
Relee cada archivo y lo audita (make falla si hay errores). Lo dibuja con ezdxf y
matplotlib, un lector distinto de LibreCAD, y compara los dos dibujos.
"""
import json, os, sys

import ezdxf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from ezdxf.addons.drawing import Frontend, RenderContext
from ezdxf.addons.drawing.config import (BackgroundPolicy, ColorPolicy, Configuration,
                                         LineweightPolicy)
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from PIL import Image

CARPETA = os.path.dirname(os.path.abspath(__file__))
LAMINAS = {"01_conjunto": 2.5, "02_despiece": 1.0, "03_esquema_cinematico": 1.0,
           "04_hallazgo_manivela": 2.0}
ANCHO, ALTO, DPI = 420, 297, 110
TOLERANCIA_PX = 4


def dibujar(doc, E, ruta):
    fig = plt.figure(figsize=(ANCHO / 25.4, ALTO / 25.4), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    cfg = Configuration(background_policy=BackgroundPolicy.WHITE,
                        color_policy=ColorPolicy.BLACK,
                        lineweight_policy=LineweightPolicy.ABSOLUTE)
    Frontend(RenderContext(doc), MatplotlibBackend(ax), config=cfg).draw_layout(
        doc.modelspace(), finalize=True)
    ax.set_xlim(0, ANCHO * E)
    ax.set_ylim(0, ALTO * E)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(ruta, dpi=DPI)
    plt.close(fig)


def oscuro(ruta, tam):
    return np.asarray(Image.open(ruta).convert("L").resize(tam)) < 160


def dilatar(m, n):
    r = m.copy()
    for _ in range(n):
        r = r | np.roll(r, 1, 0) | np.roll(r, -1, 0) | np.roll(r, 1, 1) | np.roll(r, -1, 1)
    return r


def comparar(a, b):
    """Qué parte de lo dibujado por cada lector cae cerca de lo dibujado por el otro."""
    tam = Image.open(a).size
    A, B = oscuro(a, tam), oscuro(b, tam)
    return (round(float((A & dilatar(B, TOLERANCIA_PX)).sum() / max(1, A.sum())), 3),
            round(float((B & dilatar(A, TOLERANCIA_PX)).sum() / max(1, B.sum())), 3))


def main():
    informe, errores = {}, 0
    for nombre, E in LAMINAS.items():
        ruta = os.path.join(CARPETA, "planos", nombre + ".dxf")
        doc = ezdxf.readfile(ruta)
        aud = doc.audit()
        errores += len(aud.errors)
        png = os.path.join(CARPETA, "build", "planos", nombre + "_ezdxf.png")
        dibujar(doc, E, png)
        lc = os.path.join(CARPETA, "build", "planos", nombre + ".png")
        libre, ez = comparar(lc, png)
        informe[nombre] = {"version": doc.dxfversion, "errores": len(aud.errors),
                           "corregidos": len(aud.fixes),
                           "librecad_cerca_de_ezdxf": libre, "ezdxf_cerca_de_librecad": ez}
        print(nombre, informe[nombre])
    ruta = os.path.join(CARPETA, "resultados.json")
    with open(ruta, encoding="utf-8") as f:
        todo = json.load(f)
    todo["auditoria_ezdxf"] = informe
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(todo, f, ensure_ascii=False, indent=1)
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
