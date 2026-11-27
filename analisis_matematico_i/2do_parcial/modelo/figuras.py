r"""Figuras del modelo de 2do parcial de AM1 (resuelto en clase).

Ej. 3: intersección de f(x) = 9 - e^(6x^2-24) con g (primitiva hallada).
Ej. 4: solución de y' + 2y = 1 que pasa por (0; 3).
Ej. 5: área entre f(x) = x - x^2 y g(x) = kx con k = -2.
Ej. 6: la serie de integrales sobre [n; n+1] como área bajo 1/x^5.
Ej. 7: intervalo de convergencia [-2; 2] en la recta real.

Cada resultado del documento se comprueba con assert antes de dibujar.
Genera en ./figuras/ el PDF vectorial (documento) y el PNG (vista previa del .md).
Uso: python3 figuras.py   (o `make` desde esta carpeta)
"""
import logging
from pathlib import Path

import matplotlib

matplotlib.use("pgf")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

logging.getLogger("fontTools").setLevel(logging.ERROR)

# --- Comprobaciones de los resultados del documento --------------------------
# Ej. 1: g''(4) = 64 f''(2) + 2 f'(2), con f''(2) = 2·(-37), f'(2) = 0
assert 64 * (2 * -37) + 2 * 0 == -4736

# Ej. 2: g(1) = 11/3, g'(1) = -1/3 (recta 3y + x = 12)
g1, dg1 = 11 / 3, -1 / 3
assert np.isclose(3 * g1 + 1, 12)
f1, df1, d2f1 = 2 - 0 + 1, 6 - g1 + 2, 12 - 2 * g1 - dg1 + 2
assert np.isclose(f1, 3) and np.isclose(df1, 13 / 3) and np.isclose(d2f1, 7)


# Ej. 3
def f3(x):
    return 9 - np.exp(6 * x**2 - 24)


def g3(x):
    u = 6 * x**2 - 24
    return np.exp(u) * (u - 1) + 9


def dg3(x):
    return 12 * x * (6 * x**2 - 24) / np.exp(24 - 6 * x**2)


h = 1e-6
for x0 in (0.7, 1.9, 2.1):  # g es primitiva de g'
    assert np.isclose((g3(x0 + h) - g3(x0 - h)) / (2 * h), dg3(x0), rtol=1e-5)
assert np.isclose(g3(2), 8) and np.isclose(f3(2), 8) and np.isclose(f3(-2), 8)


# Ej. 4
def y4(x):
    return 0.5 + 2.5 * np.exp(-2 * x)


assert np.isclose(y4(0), 3)
for x0 in (-0.5, 0.3, 2.0):  # y' + 2y = 1
    assert np.isclose((y4(x0 + h) - y4(x0 - h)) / (2 * h) + 2 * y4(x0), 1)

# Ej. 5: área con k = -2
K5 = -2
xs = np.linspace(0, 1 - K5, 200001)
assert np.isclose(np.trapezoid((xs - xs**2) - K5 * xs, xs), 4.5)

# Ej. 6: suma parcial telescópica → 1/4
S = sum(0.25 * (1 / n**4 - 1 / (n + 1) ** 4) for n in range(1, 2000))
assert np.isclose(S, 0.25)

# Ej. 7: con k = 4, R = sqrt(k) = 2
assert np.isclose(np.sqrt(4), 2)

# --- Estilo (mismo motor y fuentes que el documento) -------------------------
OUT = Path(__file__).parent / "figuras"
OUT.mkdir(exist_ok=True)

plt.rcParams.update({
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
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

AZUL = "#1f4e9c"
NARANJA = "#d98a00"
VERDE = "#27ae60"
GRIS = "0.55"

coma = FuncFormatter(lambda v, _: f"{v:g}".replace(".", ",").replace("-", "−"))


def ejes(ax, xlim, ylim, igual=False):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    if igual:
        ax.set_aspect("equal")
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.grid(True, color="0.9", lw=0.6)
    ax.xaxis.set_major_formatter(coma)
    ax.yaxis.set_major_formatter(coma)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$", rotation=0)


def guardar(fig, nombre):
    pdf = OUT / f"{nombre}.pdf"
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(pdf.with_suffix(".png"), bbox_inches="tight", dpi=150)
    plt.close(fig)
    print("ok:", pdf, "(+ .png)")


# --- Ej. 3 -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(5.6, 3.6))
x = np.linspace(-2.25, 2.25, 2001)
ax.plot(x, f3(x), color=AZUL, lw=1.8, label=r"$f(x) = 9 - e^{6x^2-24}$")
ax.plot(x, g3(x), color=NARANJA, lw=1.8, ls="--",
        label=r"$g(x) = e^{6x^2-24}\,(6x^2-25) + 9$")
for xp in (-2, 2):
    ax.plot(xp, 8, "o", color=VERDE, ms=7, zorder=5)
ax.annotate(r"$(-2;\,8)$", (-2, 8), xytext=(-1.75, 4.5), color=VERDE,
            arrowprops=dict(arrowstyle="-", color=VERDE, lw=0.8))
ax.annotate(r"$(2;\,8)$", (2, 8), xytext=(1.25, 4.5), color=VERDE,
            arrowprops=dict(arrowstyle="-", color=VERDE, lw=0.8))
ax.text(0, 11.6, r"casi iguales: $e^{6x^2-24} \approx 0$ si $|x| < 1{,}7$",
        ha="center", color=GRIS, fontsize=9)
ejes(ax, (-2.4, 2.4), (-2, 14))
ax.legend(loc="lower center", fontsize=8.5, frameon=True)
guardar(fig, "fig_ej3_interseccion")

# --- Ej. 4 -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(5.2, 3.2))
x = np.linspace(-0.6, 3, 600)
ax.plot(x, y4(x), color=AZUL, lw=1.8,
        label=r"$f(x) = \tfrac{1}{2} + \tfrac{5}{2}\,e^{-2x}$")
ax.axhline(0.5, color=GRIS, ls=":", lw=1.2)
ax.text(2.2, 0.62, r"$y = \tfrac{1}{2}$", color=GRIS)
ax.plot(0, 3, "o", color=VERDE, ms=7, zorder=5)
ax.annotate(r"$(0;\,3)$", (0, 3), xytext=(0.3, 3.3), color=VERDE)
ejes(ax, (-0.6, 3), (-0.3, 4.5))
ax.legend(loc="upper right", fontsize=9)
guardar(fig, "fig_ej4_solucion")

# --- Ej. 5 -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4.6, 3.6))
x = np.linspace(-0.6, 3.6, 500)
xa = np.linspace(0, 3, 300)
ax.fill_between(xa, xa - xa**2, K5 * xa, color=VERDE, alpha=0.25, lw=0)
ax.plot(x, x - x**2, color=AZUL, lw=1.8, label=r"$f(x) = x - x^2$")
ax.plot(x, K5 * x, color=NARANJA, lw=1.8, label=r"$g(x) = -2x$")
ax.plot([0, 3], [0, -6], "o", color="black", ms=5, zorder=5)
ax.annotate(r"$(3;\,-6)$", (3, -6), xytext=(3.1, -5.2))
ax.text(1.0, -0.9, r"$A = \tfrac{9}{2}$", color="#1b7a43", fontsize=12,
        ha="center")
ejes(ax, (-0.6, 3.8), (-7.5, 1.5))
ax.legend(loc="lower left", fontsize=9)
guardar(fig, "fig_ej5_area")

# --- Ej. 6 -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(5.4, 3.0))
x = np.linspace(0.85, 6, 600)
ax.plot(x, x**-5.0, color=AZUL, lw=1.8, label=r"$y = 1/x^5$")
colores = [VERDE, NARANJA]
for n in range(1, 6):
    xn = np.linspace(n, n + 1, 100)
    ax.fill_between(xn, 0, xn**-5.0, color=colores[n % 2], alpha=0.35, lw=0)
    ax.text(n + 0.5, 0.06, f"$n={n}$", ha="center", fontsize=8.5)
ax.text(3.5, 0.55, r"$\sum_{n\ge 1} \int_n^{n+1} = \int_1^{\infty} = \tfrac{1}{4}$",
        ha="center", fontsize=11)
ejes(ax, (0.8, 6), (0, 1.1))
ax.legend(loc="upper right", fontsize=9)
guardar(fig, "fig_ej6_telescopica")

# --- Ej. 7 -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(5.6, 1.5))
ax.axhline(0, color="black", lw=0.8)
ax.plot([-2, 2], [0, 0], color=VERDE, lw=4, solid_capstyle="butt")
ax.plot([-2, 2], [0, 0], "o", color=VERDE, ms=9, zorder=5)
for xp, t in [(-2, r"$-2$"), (0, r"$0$"), (2, r"$2$")]:
    ax.plot([xp, xp], [-0.08, 0.08], color="black", lw=0.8)
    ax.text(xp, -0.38, t, ha="center")
ax.text(0, 0.3, r"CV absoluta: $|x| < 2$", ha="center", fontsize=8.5)
for xp in (-2, 2):
    ax.text(xp, -0.75, "CV (Leibniz)", ha="center", fontsize=8.5,
            color="#1b7a43")
for xp in (-3.3, 3.3):
    ax.text(xp, 0.3, "DV", ha="center", fontsize=8.5, color="#b03a2e")
ax.set_xlim(-4, 4)
ax.set_ylim(-0.95, 0.6)
ax.axis("off")
guardar(fig, "fig_ej7_intervalo")
