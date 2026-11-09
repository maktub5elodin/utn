r"""Figura del ejercicio 2 de las resoluciones del 1er Parcial de AM1.

Distancia mínima de P(0; 6) a la hipérbola x^2 - y^2 = 16. Es la de las
correcciones (../figuras_correcciones.py) sin los puntos particulares probados
en el parcial; las otras cuatro figuras se comparten desde ../figuras/.

Genera en ./figuras/ el PDF vectorial y el PNG de vista previa del .md.
Uso: python3 figuras_resoluciones.py   (o `make` desde esta carpeta)
"""
import logging
from pathlib import Path

import matplotlib

matplotlib.use("pgf")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

P = np.array([0.0, 6.0])
Q1 = np.array([5.0, 3.0])                  # óptimo por desarrollo
Q2 = np.array([-5.0, 3.0])                 # óptimo por simetría
d2 = lambda q: float(np.sum((q - P) ** 2))

# Comprobaciones: si alguna falla, la figura no se genera
for q in (Q1, Q2):
    assert np.isclose(q[0] ** 2 - q[1] ** 2, 16)
    assert np.isclose(d2(q), 34)

logging.getLogger("fontTools").setLevel(logging.ERROR)

OUT = Path(__file__).parent / "figuras"
OUT.mkdir(exist_ok=True)

plt.rcParams.update({
    # Mismo motor y fuentes que el documento (ver pipeline_pdf/base.yaml)
    "pgf.texsystem": "xelatex",
    "pgf.rcfonts": False,
    "pgf.preamble": "\n".join([
        r"\usepackage{amsmath}",
        r"\usepackage{fontspec}",
        r"\usepackage{unicode-math}",
        r"\setmainfont{Latin Modern Roman}",
        r"\setmathfont{Latin Modern Math}",
    ]),
    "font.family": "serif",
    "font.size": 10,  # = \small de un documento a 11 pt
    "axes.spines.top": False,
    "axes.spines.right": False,
})

C_CURVA = "#1f4e9c"     # hipérbola
C_CORRECTO = "#27ae60"  # mismo verde que el recuadro de respuesta
C_CATETO = "#d98a00"    # catetos

coma = FuncFormatter(lambda v, _: f"{v:g}".replace(".", ",").replace("-", "−"))

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.set_xlim(-10.5, 10.5)
ax.set_ylim(-3.5, 10.5)
ax.set_aspect("equal")
ax.axhline(0, color="black", lw=0.8)
ax.axvline(0, color="black", lw=0.8)
ax.grid(True, color="0.9", lw=0.6)
ax.xaxis.set_major_formatter(coma)
ax.yaxis.set_major_formatter(coma)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$", rotation=0)

y = np.linspace(-3.5, 10.5, 400)
x = np.sqrt(16 + y ** 2)
ax.plot(x, y, color=C_CURVA, lw=2, label=r"$x^2 - y^2 = 16$")
ax.plot(-x, y, color=C_CURVA, lw=2)

# Triángulo rectángulo P–R–Q1, recto en R = (0; 3): catetos x = 5 (horizontal)
# e y − 6 = −3 (vertical, sobre el eje y); hipotenusa d
R = np.array([P[0], Q1[1]])
ax.plot(*zip(P, R), color=C_CATETO, lw=2, zorder=4)
ax.plot(*zip(R, Q1), color=C_CATETO, lw=2, zorder=4)
m = 0.35  # marca de ángulo recto
ax.plot([R[0] + m, R[0] + m, R[0]], [R[1], R[1] + m, R[1] + m], color=C_CATETO, lw=0.9)
ax.text(3.7, 2.75, r"$x = 5$", color=C_CATETO, ha="center", va="top")
ax.text(-0.25, 3.6, r"$\lvert y - 6 \rvert = 3$", color=C_CATETO, ha="right", va="center")

ax.plot(*zip(P, Q1), color=C_CORRECTO, lw=2.4, label=r"$d^2 = 5^2 + (-3)^2 = 34$")
ax.plot(*zip(P, Q2), "--", color=C_CORRECTO, lw=1.8)
ax.plot(*np.array([Q1, Q2]).T, "o", color=C_CORRECTO, ms=5)
ax.text(Q1[0] + 0.3, Q1[1] - 0.6, r"$Q_1 = (5;\,3)$" "\n" rf"$d \approx {np.sqrt(d2(Q1)):.2f}$".replace(".", "{,}"),
        color=C_CORRECTO, ha="left", va="top")
ax.text(Q2[0] - 0.3, Q2[1] - 0.6, r"$Q_2 = (-5;\,3)$" "\n(simetría)", color=C_CORRECTO,
        ha="right", va="top")

ax.plot(*P, "o", color="black", ms=5, zorder=5)
ax.text(P[0] - 0.4, P[1] + 0.4, r"$P = (0;\,6)$", ha="right", va="bottom")

ax.legend(loc="lower left", fontsize=8, framealpha=0.95)
pdf = OUT / "fig1_ej2_distancia_minima.pdf"
fig.savefig(pdf, bbox_inches="tight")
fig.savefig(pdf.with_suffix(".png"), bbox_inches="tight", dpi=150)
plt.close(fig)
print("ok:", pdf, "(+ .png)")
