r"""Figuras de las correcciones del 1er Parcial de AM1.

Ejercicio 1: a) Bolzano para 3x^2 + ln x; b) asíntota oblicua de (3x^2 - 10)/(9x - 54).
Ejercicio 2: distancia mínima de P(0; 6) a la hipérbola x^2 - y^2 = 16.
Ejercicio 3: rectas tangentes a f(x) = x^3 - x que pasan por (-2; 2).
Ejercicio 4: continuidad y derivabilidad en x = 0 de una función partida.
Ejercicio 5: dominio, crecimiento y concavidad de f(x) = ln(x^2 + 4x - 5).

Genera en ./figuras/:
  - PDF vectoriales para el documento final (\includegraphics).
  - PNG solo para la vista previa del .md en VS Code / GitHub.

El texto y las fórmulas se componen con el backend pgf + xelatex, usando las
mismas fuentes que el documento (Latin Modern Roman + Latin Modern Math).
Uso: python3 figuras_correcciones.py   (o `make` desde esta carpeta)
"""
import logging
from pathlib import Path

import matplotlib

matplotlib.use("pgf")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# --- Datos del ejercicio 2 --------------------------------------------------
P = np.array([0.0, 6.0])
Q1 = np.array([5.0, 3.0])                  # óptimo por desarrollo
Q2 = np.array([-5.0, 3.0])                 # óptimo por simetría
PROBADOS = [Q1, np.array([4.0, 0.0]), np.array([4 * np.sqrt(5), 8.0])]  # parcial


def d2(q):
    return float(np.sum((q - P) ** 2))


# Comprobaciones: si alguna falla, la figura no se genera
for q in PROBADOS + [Q2]:
    assert np.isclose(q[0] ** 2 - q[1] ** 2, 16)
assert np.isclose(d2(Q1), 34) and np.isclose(d2(Q2), 34)
assert np.isclose(d2(PROBADOS[1]), 52)     # d ≈ 7,21
assert np.isclose(d2(PROBADOS[2]), 84)     # d ≈ 9,17

logging.getLogger("fontTools").setLevel(logging.ERROR)

# --- Estilo -----------------------------------------------------------------
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
C_CORRECTO = "#27ae60"  # mismo verde que el recuadro de respuesta correcta
C_CATETO = "#d98a00"    # catetos
C_PROBADO = "#8e44ad"   # puntos probados en el parcial (fuerza bruta)

coma = FuncFormatter(lambda v, _: f"{v:g}".replace(".", ",").replace("-", "−"))


def ejes(ax, xlim, ylim):
    """Ejes cartesianos con grilla suave, escala 1:1 y coma decimal."""
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.grid(True, color="0.9", lw=0.6)
    ax.xaxis.set_major_formatter(coma)
    ax.yaxis.set_major_formatter(coma)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$", rotation=0)


def guardar(fig, nombre):
    """Guarda el PDF vectorial y su PNG de vista previa."""
    pdf = OUT / nombre
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(pdf.with_suffix(".png"), bbox_inches="tight", dpi=150)
    plt.close(fig)
    print("ok:", pdf, "(+ .png)")


# --- Ejercicio 1: a) Bolzano; b) asíntota oblicua ---------------------------
def f1a(x):
    return 3 * x ** 2 + np.log(x)


def f1b(x):
    return (3 * x ** 2 - 10) / (9 * x - 54)


assert f1a(0.4) < 0 < f1a(0.5)
assert abs(f1b(1e6) - (1e6 / 3 + 2)) < 1e-3   # se acerca a y = x/3 + 2

fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.6, 3.2))
for ax in (a1, a2):
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.grid(True, color="0.9", lw=0.6)
    ax.xaxis.set_major_formatter(coma)
    ax.yaxis.set_major_formatter(coma)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$", rotation=0)

a1.set_title("a)", loc="left")
a1.set_xlim(0.3, 0.6)
a1.set_ylim(-1, 0.7)
xa = np.linspace(0.3, 0.6, 300)
a1.plot(xa, f1a(xa), color=C_CURVA, lw=2, label=r"$3x^2 + \ln x$")
for x0, va in ((0.4, "top"), (0.5, "bottom")):
    a1.plot(x0, f1a(x0), "o", color=C_CURVA, ms=5, zorder=5)
r = 0.4
for _ in range(50):                        # Newton: raíz en (0,4; 0,5)
    r = r - f1a(r) / (6 * r + 1 / r)
a1.text(0.39, f1a(0.4), r"$f(0{,}4) < 0$", ha="right", va="center", color=C_CURVA)
a1.text(0.51, -0.08, r"$f(0{,}5) > 0$", ha="left", va="top", color=C_CURVA)
a1.plot(r, 0, "o", color=C_CORRECTO, ms=6, zorder=6)
a1.text(r - 0.006, 0.05, "$c$", color=C_CORRECTO, ha="right", va="bottom")
a1.axvspan(0.4, 0.5, color=C_CORRECTO, alpha=0.1, lw=0)
a1.legend(loc="upper left", fontsize=8, framealpha=0.95)

a2.set_title("b)", loc="left")
a2.set_xlim(-25, 35)
a2.set_ylim(-20, 30)
for xs in (np.linspace(-25, 5.6, 300), np.linspace(6.4, 35, 300)):
    a2.plot(xs, f1b(xs), color=C_CURVA, lw=2)
a2.plot([], [], color=C_CURVA, lw=2, label=r"$\dfrac{3x^2 - 10}{9x - 54}$")
xr = np.array([-25, 35])
a2.plot(xr, xr / 3 + 2, "--", color=C_CORRECTO, lw=1.6, label=r"$y = \frac{x}{3} + 2$")
a2.legend(loc="upper left", fontsize=8, framealpha=0.95)

fig.tight_layout()
guardar(fig, "fig0_ej1_bolzano_asintota.pdf")


# --- Figura: ejercicio 2 ----------------------------------------------------
fig, ax = plt.subplots(figsize=(6.4, 4.6))
ejes(ax, (-10.5, 10.5), (-3.5, 10.5))

y = np.linspace(-3.5, 10.5, 400)
x = np.sqrt(16 + y ** 2)
ax.plot(x, y, color=C_CURVA, lw=2, label=r"$x^2 - y^2 = 16$")
ax.plot(-x, y, color=C_CURVA, lw=2)

# Puntos probados en el parcial (fuerza bruta), con su distancia a P
for q in PROBADOS[1:]:
    ax.plot(*zip(P, q), ":", color=C_PROBADO, lw=1.2)
ax.plot(*np.array(PROBADOS).T, "o", ms=9, mfc="none", mec=C_PROBADO, mew=1.4,
        label="probados en el parcial (fuerza bruta)")
ax.text(6, -2.6, rf"$(4;\,0)$: $d \approx {np.sqrt(d2(PROBADOS[1])):.2f}$".replace(".", "{,}"),
        color=C_PROBADO, ha="left")
ax.text(8.6, 9.3, rf"$(4\sqrt{{5}};\,8)$: $d \approx {np.sqrt(d2(PROBADOS[2])):.2f}$".replace(".", "{,}"),
        color=C_PROBADO, ha="right")

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
ax.text(Q1[0] + 0.3, Q1[1] - 0.6, r"$Q_1 = (5;\,3)$" "\n" rf"$d \approx {np.sqrt(d2(Q1)):.2f}$".replace(".", "{,}"), color=C_CORRECTO, ha="left", va="top")
ax.text(Q2[0] - 0.3, Q2[1] - 0.6, r"$Q_2 = (-5;\,3)$" "\n(simetría)", color=C_CORRECTO,
        ha="right", va="top")

ax.plot(*P, "o", color="black", ms=5, zorder=5)
ax.text(P[0] - 0.4, P[1] + 0.4, r"$P = (0;\,6)$", ha="right", va="bottom")

ax.legend(loc="lower left", fontsize=8, framealpha=0.95)
guardar(fig, "fig1_ej2_distancia_minima.pdf")


# --- Ejercicio 3: tangentes a f(x) = x^3 - x por el punto (-2; 2) ------------
def f(x):
    return x ** 3 - x


def fp(x):
    return 3 * x ** 2 - 1


E = np.array([-2.0, 2.0])                  # punto exterior (no está en la gráfica)
TANG = [0.0, -3.0]                         # abscisas de tangencia (2a²(a + 3) = 0)
XE = np.sqrt(3) / 3                        # extremos locales: f'(x) = 0
C_ERROR = "#c0392b"                        # mismo rojo que el recuadro de error

for a in TANG:
    assert np.isclose(f(a) + fp(a) * (E[0] - a), E[1])
assert np.isclose(f(E[0]), -6)
assert np.isclose(fp(XE), 0) and np.isclose(f(-XE), 2 * np.sqrt(3) / 9)

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.set_xlim(-4, 2.5)
ax.set_ylim(-32, 16)
ax.axhline(0, color="black", lw=0.8)
ax.axvline(0, color="black", lw=0.8)
ax.grid(True, color="0.9", lw=0.6)
ax.xaxis.set_major_formatter(coma)
ax.yaxis.set_major_formatter(coma)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$", rotation=0)

x = np.linspace(-4, 2.5, 400)
ax.plot(x, f(x), color=C_CURVA, lw=2, label=r"$f(x) = x^3 - x$")
ax.plot(x, -x, color=C_CORRECTO, lw=1.6, label=r"$y = -x$")
ax.plot(x, 26 * x + 54, color=C_CORRECTO, lw=1.6, ls="--", label=r"$y = 26x + 54$")
ax.plot(TANG, [f(a) for a in TANG], "o", color=C_CORRECTO, ms=5, zorder=5)
ax.text(-3 + 0.15, f(-3), r"$(-3;\,-24)$", color=C_CORRECTO, ha="left", va="top")

# El punto dado y el de la gráfica con la misma abscisa: el error del parcial
ax.plot(*E, "o", color="black", ms=5, zorder=6)
ax.text(E[0] - 0.12, E[1] + 1, r"$(-2;\,2)$", ha="right", va="bottom")
ax.plot([E[0], E[0]], [E[1], f(E[0])], ":", color=C_ERROR, lw=1.2)
ax.plot(E[0], f(E[0]), "o", ms=7, mfc="none", mec=C_ERROR, mew=1.3, zorder=6)
ax.text(E[0] + 0.12, f(E[0]) - 0.5, r"$f(-2) = -6 \neq 2$", color=C_ERROR, ha="left", va="top")
ax.legend(loc="upper left", fontsize=8, framealpha=0.95)

# Ampliación alrededor del origen: raíces, extremos locales y tangencia en (0; 0)
ins = ax.inset_axes([0.6, 0.07, 0.37, 0.36])
xi = np.linspace(-1.35, 1.35, 300)
ins.plot(xi, f(xi), color=C_CURVA, lw=1.6)
ins.plot(xi, -xi, color=C_CORRECTO, lw=1.2)
ins.axhline(0, color="black", lw=0.6)
ins.axvline(0, color="black", lw=0.6)
ins.plot([-1, 0, 1], [0, 0, 0], "o", color=C_CURVA, ms=3.5, zorder=5)
ins.plot([-XE, XE], [f(-XE), f(XE)], "o", ms=5, mfc="white", mec=C_CURVA, mew=1.1, zorder=5)
ins.text(-XE, f(-XE) + 0.12, r"máx.", ha="center", va="bottom", fontsize=7)
ins.text(XE, f(XE) - 0.12, r"mín.", ha="center", va="top", fontsize=7)
ins.set_xlim(-1.35, 1.35)
ins.set_ylim(-0.75, 0.75)
ins.set_xticks([-1, 0, 1])
ins.set_yticks([])
ins.tick_params(labelsize=7)
ins.xaxis.set_major_formatter(coma)
ins.set_facecolor("white")
for lado in ins.spines.values():
    lado.set_visible(True)
    lado.set_color("0.6")
ax.indicate_inset_zoom(ins, edgecolor="0.6")
guardar(fig, "fig2_ej3_tangentes.pdf")


# --- Ejercicio 4: continuidad y derivabilidad en x = 0 ----------------------
def f_izq(x):
    return np.log(1 + x ** 2) / x ** 2    # x < 0


def f_der(x):
    return np.sin(x) / x                   # x > 0 (modelo: −cos(x + π/2)/x)


assert np.isclose(f_izq(-1e-4), 1) and np.isclose(f_der(1e-4), 1)
assert np.allclose(-np.cos(np.linspace(0.1, 9, 50) + np.pi / 2), np.sin(np.linspace(0.1, 9, 50)))
h = 1e-3                                   # cocientes incrementales con f(0) = 1
assert abs((f_izq(-h) - 1) / -h) < 1e-2 and abs((f_der(h) - 1) / h) < 1e-2

C_DER = "#5b8bd6"                          # rama x > 0, azul más claro

fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.set_xlim(-10, 13)
ax.set_ylim(-0.35, 1.3)
ax.axhline(0, color="black", lw=0.8)
ax.axvline(0, color="black", lw=0.8)
ax.grid(True, color="0.9", lw=0.6)
ax.xaxis.set_major_formatter(coma)
ax.yaxis.set_major_formatter(coma)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$", rotation=0)

xi = np.linspace(-10, -1e-3, 400)
xd = np.linspace(1e-3, 13, 600)
ax.plot(xi, f_izq(xi), color=C_CURVA, lw=2, label=r"$\ln(1 + x^2) / x^2$, si $x < 0$")
ax.plot(xd, f_der(xd), color=C_DER, lw=2, label=r"$\operatorname{sen} x / x$, si $x > 0$")
ax.plot([-3, 3], [1, 1], "--", color=C_CORRECTO, lw=1.6, label=r"tangente $y = 1$, $f'(0) = 0$")
ax.plot(0, 1, "o", color=C_CORRECTO, ms=6, zorder=5)
ax.text(-0.3, 1.06, r"$f(0) = 1$", color=C_CORRECTO, ha="right", va="bottom")
ax.legend(loc="upper right", fontsize=8, framealpha=0.95)
guardar(fig, "fig3_ej4_continuidad.pdf")


# --- Ejercicio 5: dominio, crecimiento y concavidad de ln(x^2 + 4x - 5) ------
def g(x):
    return x ** 2 + 4 * x - 5              # argumento del logaritmo


assert np.isclose(g(1), 0) and np.isclose(g(-5), 0) and np.isclose(g(-2), -9)
xs = np.concatenate([np.linspace(-12, -5.01, 50), np.linspace(1.01, 8, 50)])
fpp = -2 * (xs ** 2 + 4 * xs + 13) / g(xs) ** 2
assert np.all(fpp < 0)                     # concavidad negativa en todo el dominio

fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.set_xlim(-11, 7)
ax.set_ylim(-10.5, 6)
ax.axhline(0, color="black", lw=0.8)
ax.axvline(0, color="black", lw=0.8)
ax.grid(True, color="0.9", lw=0.6)
ax.xaxis.set_major_formatter(coma)
ax.yaxis.set_major_formatter(coma)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$", rotation=0)

# Cuadrática del argumento: raíces y vértice
xg = np.linspace(-9, 5, 300)
ax.plot(xg, g(xg), color="0.6", lw=1.3, label=r"$x^2 + 4x - 5$")
ax.plot([-5, 1], [0, 0], "o", ms=5, mfc="white", mec="0.4", mew=1.2, zorder=5)
ax.plot(-2, -9, "o", color="0.4", ms=4, zorder=5)
ax.text(-2, -9.4, r"$(-2;\,-9)$", color="0.4", ha="center", va="top")

# f en cada intervalo del dominio
xi = np.linspace(-11, -5 - 1e-4, 400)
xd = np.linspace(1 + 1e-4, 7, 400)
ax.plot(xi, np.log(g(xi)), color=C_CURVA, lw=2, label=r"$f(x) = \ln(x^2 + 4x - 5)$")
ax.plot(xd, np.log(g(xd)), color=C_CURVA, lw=2)
ax.text(-9.5, np.log(g(-9.5)) + 0.5, "decrece", color=C_CURVA, ha="center", va="bottom")
ax.text(5.5, np.log(g(5.5)) + 0.5, "crece", color=C_CURVA, ha="center", va="bottom")

# Fuera del dominio: x = -2 anula f' pero no pertenece a D_f
ax.axvspan(-5, 1, color=C_ERROR, alpha=0.07, lw=0)
ax.text(-2, 4.8, "fuera del dominio", color=C_ERROR, ha="center", va="center")
ax.plot([-2, -2], [0, -9], ":", color=C_ERROR, lw=1.2)
ax.text(-1.85, -1.2, r"$x = -2$", color=C_ERROR, ha="left", va="top")

ax.legend(loc="lower left", fontsize=8, framealpha=0.95)
guardar(fig, "fig4_ej5_dominio_ln.pdf")
