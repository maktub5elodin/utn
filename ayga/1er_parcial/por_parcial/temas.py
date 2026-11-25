r"""Frecuencia de temas en los parciales modelo del 1er parcial de AyGA.

Lee las marcas `<!-- temas: COD COD -->` que tiene cada ejercicio del Tema 1 en
Parciales_1er_Parcial.md (el Tema 2 repite los temas del Tema 1) y:

genera figuras/fig_frecuencia_temas.{pdf,png}: en cuántos parciales aparece cada tema.

Las mismas marcas (con el detalle de en qué ejercicio aparece cada tema) son las que
va a usar el documento por tema (pendiente).
Uso: python3 temas.py   (o `make` desde esta carpeta)
"""
import logging
import re
from pathlib import Path

import matplotlib

matplotlib.use("pgf")
import matplotlib.pyplot as plt

AQUI = Path(__file__).resolve().parent
MD = AQUI / "Parciales_1er_Parcial.md"
OUT = AQUI / "figuras"

# Código -> (nombre, bloque). El orden dentro de cada bloque es el del programa.
TEMAS = {
    "REC": ("Posición relativa de rectas", "Geometría"),
    "DIST": ("Distancias", "Geometría"),
    "PLANO": ("Plano con condiciones", "Geometría"),
    "HAZ": ("Haz de planos", "Geometría"),
    "PROY": ("Proyección ortogonal", "Geometría"),
    "DET": ("Determinante con columnas combinadas", "Álgebra"),
    "RANGO": ("Rango e inversibilidad", "Álgebra"),
    "SIST": ("Clasificación de sistemas", "Álgebra"),
    "LI": ("Independencia lineal y bases", "Álgebra"),
    "COORD": ("Coordenadas en una base", "Álgebra"),
    "SUBESP": ("Subespacio dado por una condición", "Álgebra"),
    "INTSUM": ("Intersección y suma de subespacios", "Álgebra"),
    "ORTC": ("Complemento ortogonal", "Álgebra"),
    "VF": ("Formato verdadero o falso", "Formato"),
}
UNIDAD = {"Geometría": "U. I", "Álgebra": "U. II–V", "Formato": "—"}

texto = MD.read_text(encoding="utf-8")

# Recorre el .md: parcial actual (## P<n>), ejercicio actual (### Ejercicio <n>) y marcas.
apariciones = {c: [] for c in TEMAS}       # código -> [(parcial, ejercicio)]
parcial = ejercicio = None
for linea in texto.splitlines():
    if m := re.match(r"## (P\d+) ", linea):
        parcial, ejercicio = m.group(1), None
    elif m := re.match(r"### Ejercicio (\d+)", linea):
        ejercicio = int(m.group(1))
    elif m := re.match(r"<!-- temas: (.+?) -->", linea):
        assert parcial and ejercicio, f"marca fuera de un ejercicio: {linea}"
        for c in m.group(1).split():
            assert c in TEMAS, f"código desconocido: {c}"
            apariciones[c].append((parcial, ejercicio))

parciales = sorted({p for lista in apariciones.values() for p, _ in lista},
                   key=lambda p: int(p[1:]))
N = len(parciales)
assert N == 7, f"se esperaban 7 parciales, hay {N}"
# Todo ejercicio del Tema 1 tiene que tener su marca: 7 parciales x 5 ejercicios.
marcados = {pe for lista in apariciones.values() for pe in lista}
assert len(marcados) == 5 * N, f"ejercicios marcados: {len(marcados)} de {5 * N}"


def n_parciales(c):
    return len({p for p, _ in apariciones[c]})


orden = sorted(TEMAS, key=lambda c: (list(UNIDAD).index(TEMAS[c][1]), -n_parciales(c)))

# Figura: barras horizontales, una por tema, color por bloque (validado:
# azul/ámbar pasan CVD; el ámbar tiene poco contraste, por eso el valor va escrito).
logging.getLogger("fontTools").setLevel(logging.ERROR)
OUT.mkdir(exist_ok=True)
plt.rcParams.update({
    "pgf.texsystem": "xelatex",
    "pgf.rcfonts": False,
    "pgf.preamble": "\n".join([
        r"\usepackage{fontspec}",
        r"\setmainfont{Latin Modern Roman}",
    ]),
    "font.family": "serif",
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
})
COLOR = {"Geometría": "#1f4e9c", "Álgebra": "#d98a00"}
temas_fig = [c for c in orden if TEMAS[c][1] != "Formato"]

fig, ax = plt.subplots(figsize=(6.4, 4.2))
ys = range(len(temas_fig))[::-1]
for yv, c in zip(ys, temas_fig):
    v = n_parciales(c)
    ax.barh(yv, v, height=0.62, color=COLOR[TEMAS[c][1]])
    ax.text(v + 0.12, yv, f"{v}", va="center", color="#333333")
ax.set_yticks(list(ys), [TEMAS[c][0] for c in temas_fig])
ax.set_xlim(0, N + 0.6)
ax.set_xticks(range(N + 1))
ax.set_xlabel(f"parciales en los que aparece (de {N})")
ax.tick_params(axis="y", length=0)
ax.grid(axis="x", color="#dddddd", linewidth=0.6)
ax.set_axisbelow(True)
ax.legend(handles=[plt.Rectangle((0, 0), 1, 1, color=COLOR[b]) for b in COLOR],
          labels=["Geometría (U. I)", "Álgebra (U. II–V)"],
          loc="lower right", frameon=False)
fig.tight_layout()
for ext in ("pdf", "png"):
    fig.savefig(OUT / f"fig_frecuencia_temas.{ext}", dpi=200)
print("figura generada")
