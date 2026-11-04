r"""Figuras de las correcciones del 1er Parcial de Física I.

Ejercicio 1: trayectorias con la velocidad correcta y la del parcial frente al muro.
Ejercicio 2: vista superior de los bloques y DCL en la dirección radial.
Ejercicio 3: DCL de los bloques apilados, sin rozamiento con el piso.
Ejercicio 4: recorrido por el resorte y el plano, y DCL sobre el plano.
Ejercicio 5: marcha de rayos de la lente convergente, a escala.

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
from matplotlib.patches import Arc, Polygon, Rectangle
from matplotlib.ticker import FuncFormatter

# --- Datos del ejercicio 1 --------------------------------------------------
G = 10.0
Y0 = 1.5
X_MURO = 15.0
H_MURO = 5.0
THETA = np.radians(45)
V_PARCIAL = 75 / (11.5 * np.cos(THETA))    # sin el cuadrado de t
V_CORRECTA = np.sqrt(G * X_MURO ** 2 / (2 * np.cos(THETA) ** 2 * (X_MURO * np.tan(THETA) - (H_MURO - Y0))))


def altura(x, v0):
    """y(x) de la trayectoria, eliminando t."""
    return Y0 + x * np.tan(THETA) - G * x ** 2 / (2 * (v0 * np.cos(THETA)) ** 2)


def alcance(v0):
    """x donde la piedra llega al suelo (y = 0)."""
    a = G / (2 * (v0 * np.cos(THETA)) ** 2)
    return (np.tan(THETA) + np.sqrt(np.tan(THETA) ** 2 + 4 * a * Y0)) / (2 * a)


# Comprobaciones: si alguna falla, la figura no se genera
assert np.isclose(V_CORRECTA, 13.99, atol=0.005)
assert np.isclose(V_PARCIAL, 9.223, atol=0.0005)
assert np.isclose(altura(X_MURO, V_CORRECTA), H_MURO)
assert np.isclose(altura(X_MURO, V_PARCIAL), -9.95, atol=0.005)
assert np.isclose(alcance(V_PARCIAL), 9.8, atol=0.05)

# --- Datos del ejercicio 2 --------------------------------------------------
M1, M2 = 2.0, 1.0
R1, R2 = 0.75, 1.25
OMEGA = 4 * np.pi
T2 = M2 * OMEGA ** 2 * R2
T1 = T2 + M1 * OMEGA ** 2 * R1

assert np.isclose(T2, 197.39, atol=0.005)
assert np.isclose(T1, 434.26, atol=0.005)
assert np.isclose(T1, (M1 * R1 + M2 * R2) * OMEGA ** 2)   # sistema completo

# --- Datos del ejercicio 3 --------------------------------------------------
M1_3, M2_3 = 50.0, 20.0
F_3 = 200.0
N1_3 = M2_3 * G
N2_3 = (M1_3 + M2_3) * G
FRE_3, FRD_3 = 0.5 * N1_3, 0.25 * N1_3
A2_3 = (F_3 - FRD_3) / M2_3
A1_3 = FRD_3 / M1_3

assert np.isclose(M1_3 * F_3 / (M1_3 + M2_3), 142.857, atol=0.001) and FRE_3 == 100   # deslizan
assert np.isclose(FRE_3 * (M1_3 + M2_3) / M1_3, 140)    # F límite
assert np.isclose(A2_3, 7.5) and np.isclose(A1_3, 1)
assert np.isclose(M1_3 * A1_3 + M2_3 * A2_3, F_3)       # sistema completo

# --- Datos del ejercicio 4 --------------------------------------------------
K_4, X_4, M_4 = 400.0, 0.22, 2.0
ALFA = np.radians(37)
W_4 = K_4 * X_4 ** 2 / 2
V_4 = np.sqrt(2 * W_4 / M_4)
WX_4, WY_4 = M_4 * G * np.cos(np.radians(233)), M_4 * G * np.sin(np.radians(233))
N_4 = -WY_4
FRD_4, FRE_4 = 0.5 * N_4, 0.8 * N_4
H_4 = W_4 / (FRD_4 / np.sin(ALFA) + M_4 * G)
D_4 = H_4 / np.sin(ALFA)

assert np.isclose(W_4, 9.68) and np.isclose(V_4, 3.11, atol=0.005)
assert np.isclose(WX_4, -12.04, atol=0.005) and np.isclose(N_4, 15.97, atol=0.005)
assert np.isclose(FRD_4, 7.99, atol=0.005) and np.isclose(FRE_4, 12.78, atol=0.005)
assert np.isclose(H_4, 0.29, atol=0.005) and np.isclose(D_4, 0.48, atol=0.005)
assert np.isclose(D_4, V_4 ** 2 / (2 * (-WX_4 + FRD_4) / M_4))   # segunda ley
assert -WX_4 < FRE_4 and np.tan(ALFA) < 0.8                      # no desciende

# --- Datos del ejercicio 5 --------------------------------------------------
DO_5, DI_5 = 2.0, 8.0
F_5 = 1 / (1 / DO_5 + 1 / DI_5)
Y_5 = 1.0
YI_5 = -Y_5 * DI_5 / DO_5

assert np.isclose(DO_5 + DI_5, 10) and np.isclose(F_5, 1.6) and np.isclose(YI_5, -4)
assert np.allclose(sorted(np.roots([1, -10, 16])), [2, 8])     # las dos posiciones

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

C_CORRECTO = "#27ae60"  # mismo verde que el recuadro de respuesta correcta
C_PROBADO = "#8e44ad"   # valor obtenido en el parcial
C_MURO = "0.75"
C_T1 = "#1f4e9c"         # tensión de la cuerda interior
C_T2 = "#d98a00"         # tensión de la cuerda entre bloques

coma = FuncFormatter(lambda v, _: f"{v:g}".replace(".", ",").replace("-", "−"))


def guardar(fig, nombre):
    """Guarda el PDF vectorial y su PNG de vista previa."""
    pdf = OUT / nombre
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(pdf.with_suffix(".png"), bbox_inches="tight", dpi=150)
    plt.close(fig)
    print("ok:", pdf, "(+ .png)")


# --- Ejercicio 1: trayectorias frente al muro -------------------------------
fig, ax = plt.subplots(figsize=(6.4, 3.1))
ax.set_xlim(-0.5, 17)
ax.set_ylim(0, 7.5)
ax.set_aspect("equal")
ax.grid(True, color="0.9", lw=0.6)
ax.xaxis.set_major_formatter(coma)
ax.yaxis.set_major_formatter(coma)
ax.set_xticks([0, 5, 10, 15])
ax.set_yticks([0, 1.5, 5])
ax.set_xlabel("$x$ (m)")
ax.set_ylabel("$y$ (m)", rotation=0, labelpad=14)

ax.add_patch(Rectangle((X_MURO - 0.5, 0), 0.5, H_MURO, color=C_MURO, zorder=2))
ax.text(X_MURO + 0.2, 2.5, "muro", va="center")
ax.plot([0, 0], [0, Y0], color="black", lw=2, zorder=3)
ax.text(0.2, 0.55, "muchacho", va="center")

xs = np.linspace(0, X_MURO, 300)
ax.plot(xs, altura(xs, V_CORRECTA), color=C_CORRECTO, lw=2, zorder=4)
xs = np.linspace(0, alcance(V_PARCIAL), 300)
ax.plot(xs, altura(xs, V_PARCIAL), color=C_PROBADO, lw=2, zorder=4)

ax.plot([X_MURO], [H_MURO], "o", color=C_CORRECTO, ms=5, zorder=5)
ax.plot([alcance(V_PARCIAL)], [0], "o", color=C_PROBADO, ms=5, zorder=5, clip_on=False)

ax.add_patch(Arc((0, Y0), 3, 3, theta1=0, theta2=45, color="black", lw=0.8, zorder=3))
ax.plot([0, 2.2], [Y0, Y0], color="black", lw=0.8, ls=":", zorder=3)
ax.text(1.75, Y0 + 0.42, "45°", va="center")

ax.text(8.0, 6.8, r"$v_0 \approx 13{,}99$ m/s", color=C_CORRECTO, ha="center")
ax.text(5.1, 2.0, r"$9{,}223$ m/s", color=C_PROBADO, ha="center", va="center",
        bbox=dict(fc="white", ec="none", pad=1), zorder=3)
ax.text(alcance(V_PARCIAL) + 0.25, 0.4, r"$x \approx 9{,}8$ m", color=C_PROBADO)

guardar(fig, "fig1_ej1_tiro_muro.pdf")


# --- Ejercicio 2: vista superior y DCL --------------------------------------
def flecha(ax, x0, x1, y, color):
    ax.annotate("", xy=(x1, y), xytext=(x0, y),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8, shrinkA=0, shrinkB=0))


fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.3, 3.0), width_ratios=[1, 1.15])

# Vista superior
a1.set_aspect("equal")
a1.set_xlim(-1.45, 2.3)
a1.set_ylim(-2.0, 1.4)
a1.axis("off")
for r in (R1, R2):
    tita = np.linspace(0, 2 * np.pi, 300)
    a1.plot(r * np.cos(tita), r * np.sin(tita), color="0.75", lw=0.8)
a1.plot([0, R2], [0, 0], color="black", lw=1)
a1.plot([0], [0], "o", color="black", ms=3.5)
a1.text(-0.07, 0, "O", ha="right", va="center")
for r in (R1, R2):
    a1.add_patch(Rectangle((r - 0.08, -0.08), 0.16, 0.16, fc="0.75", ec="black", lw=0.8, zorder=3))
a1.text(R1, 0.13, "$m_1$", ha="center", va="bottom")
a1.text(R2, 0.13, "$m_2$", ha="center", va="bottom")
for r, y, txt in ((R1, -1.5, r"$R_1 = 0{,}75$ m"), (R2, -1.82, r"$R_2 = 1{,}25$ m")):
    a1.plot([r, r], [-0.08, y - 0.05], color="0.45", lw=0.5, ls=":")
    a1.annotate("", xy=(r, y), xytext=(0, y), arrowprops=dict(arrowstyle="<->", color="black", lw=0.7, shrinkA=0, shrinkB=0))
    a1.text(r + 0.06, y, txt, ha="left", va="center")
a1.plot([0, 0], [0, -1.87], color="0.45", lw=0.5, ls=":")
a1.add_patch(Arc((0, 0), 1.0, 1.0, theta1=50, theta2=130, color="black", lw=0.8))
a1.text(0, 0.56, r"$\omega$", ha="center", va="bottom")

# DCL en la dirección radial: largo de las flechas proporcional a la tensión
a2.set_xlim(-2.2, 1.6)
a2.set_ylim(-1.3, 1.3)
a2.axis("off")
ESC = 1.55 / T1
L = 0.13
for y, nombre in ((0.55, "$m_1$"), (-0.6, "$m_2$")):
    a2.add_patch(Rectangle((-L, y - L), 2 * L, 2 * L, fc="0.75", ec="black", lw=0.8, zorder=3))
    a2.text(0, y - L - 0.05, nombre, ha="center", va="top")
flecha(a2, -L, -L - T1 * ESC, 0.55, C_T1)
flecha(a2, L, L + T2 * ESC, 0.55, C_T2)
flecha(a2, -L, -L - T2 * ESC, -0.6, C_T2)
a2.text(-L - 0.05, 0.72, r"$T_1 \approx 434{,}26$ N", color=C_T1, ha="right", va="bottom")
a2.text(L + T2 * ESC / 2, 0.72, r"$T_2$", color=C_T2, ha="center", va="bottom")
a2.text(-L - 0.05, -0.43, r"$T_2 \approx 197{,}39$ N", color=C_T2, ha="right", va="bottom")
a2.annotate("", xy=(-1.0, 1.15), xytext=(0.2, 1.15), arrowprops=dict(arrowstyle="-|>", color="black", lw=0.8, shrinkA=0, shrinkB=0))
a2.text(0.3, 1.15, "hacia O", va="center")

guardar(fig, "fig2_ej2_tensiones.pdf")


# --- Ejercicio 3: DCL de los dos bloques ------------------------------------
def fuerza(ax, x0, y0, dx, dy, txt, color, tx, ty, ha="center", va="center"):
    ax.annotate("", xy=(x0 + dx, y0 + dy), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.6, shrinkA=0, shrinkB=0), zorder=4)
    ax.text(tx, ty, txt, color=color, ha=ha, va=va)


C_HORIZ = "#1f4e9c"
C_VERT = "0.25"
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.3, 2.7), width_ratios=[1, 1.15])
for ax in (a1, a2):
    ax.set_aspect("equal")
    ax.set_xlim(-3.0, 2.6)
    ax.set_ylim(-1.75, 1.45)
    ax.axis("off")

# Bloque 2
a1.add_patch(Rectangle((-0.4, -0.4), 0.8, 0.8, fc="0.85", ec="black", lw=0.8))
a1.text(0, 0, "$m_2$", ha="center", va="center")
fuerza(a1, -0.4, 0, -1.3, 0, r"$F = 200$ N", C_HORIZ, -0.5, 0.22, ha="right")
fuerza(a1, 0.4, 0, 0.5, 0, r"$f_{rd} = 50$ N", C_HORIZ, 0.5, 0.3, ha="left")
fuerza(a1, 0, 0.4, 0, 0.7, r"$N_1 = 200$ N", C_VERT, 0.1, 0.9, ha="left")
fuerza(a1, 0, -0.4, 0, -0.7, r"$w_2 = 200$ N", C_VERT, 0.1, -0.9, ha="left")
fuerza(a1, -1.0, -1.55, -1.0, 0, r"$a_2 = 7{,}5$ m/s²", C_CORRECTO, -0.9, -1.55, ha="left")

# Bloque 1
a2.add_patch(Rectangle((-0.8, -0.4), 1.6, 0.8, fc="0.85", ec="black", lw=0.8))
a2.text(0, 0, "$m_1$", ha="center", va="center")
fuerza(a2, -0.8, 0, -0.5, 0, r"$f_{rd} = 50$ N", C_HORIZ, -1.3, 0.22, ha="right")
fuerza(a2, -0.4, -0.4, 0, -0.7, r"$N_1 = 200$ N", C_VERT, -0.5, -0.9, ha="right")
fuerza(a2, 0.4, -0.4, 0, -0.7, r"$w_1 = 500$ N", C_VERT, 0.5, -0.9, ha="left")
fuerza(a2, 0, 0.4, 0, 0.7, r"$N_2 = 700$ N", C_VERT, 0.1, 0.9, ha="left")
fuerza(a2, -1.9, 1.05, -1.0, 0, r"$a_1 = 1$ m/s²", C_CORRECTO, -1.8, 1.05, ha="left")

guardar(fig, "fig3_ej3_dcl.pdf")


# --- Ejercicio 4: recorrido y DCL sobre el plano ----------------------------
def caja(ax, centro, lado, ang):
    """Bloque cuadrado girado ang (radianes) alrededor de su centro."""
    ex = np.array([np.cos(ang), np.sin(ang)]) * lado / 2
    ey = np.array([-np.sin(ang), np.cos(ang)]) * lado / 2
    c = np.array(centro)
    ax.add_patch(Polygon([c - ex - ey, c + ex - ey, c + ex + ey, c - ex + ey],
                         fc="0.8", ec="black", lw=0.8, zorder=3))


EX = np.array([np.cos(ALFA), np.sin(ALFA)])
EY = np.array([-np.sin(ALFA), np.cos(ALFA)])

fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.3, 2.9), width_ratios=[1.5, 1])
for ax in (a1, a2):
    ax.set_aspect("equal")
    ax.axis("off")

# Recorrido completo (distancias en metros; el tramo horizontal, a criterio)
PIE = np.array([1.0, 0.0])
TOPE = PIE + 0.68 * EX
a1.set_xlim(-0.08, 2.0)
a1.set_ylim(-0.2, 0.55)
a1.plot([0, 0, PIE[0], TOPE[0]], [0.3, 0, 0, TOPE[1]], color="black", lw=1.2)
xs = np.linspace(0, 0.3, 41)
a1.plot(xs, 0.07 + 0.035 * np.sin(xs * 2 * np.pi * 6 / 0.3), color="black", lw=0.8)
a1.text(0.15, 0.13, "$k$", ha="center")
a1.add_patch(Rectangle((0.3, 0), 0.14, 0.14, fc="0.8", ec="black", lw=0.8, zorder=3))
a1.annotate("", xy=(0.3, -0.06), xytext=(0.08, -0.06), arrowprops=dict(arrowstyle="<->", color="black", lw=0.7, shrinkA=0, shrinkB=0))
a1.text(0.19, -0.09, "0,22 m", ha="center", va="top")
a1.annotate("", xy=(0.86, 0.07), xytext=(0.58, 0.07), arrowprops=dict(arrowstyle="-|>", color=C_CORRECTO, lw=1.6, shrinkA=0, shrinkB=0))
a1.text(0.72, 0.14, r"$v \approx 3{,}11$ m/s", color=C_CORRECTO, ha="center", va="bottom")
ARRIBA = PIE + D_4 * EX
caja(a1, ARRIBA + 0.05 * EY, 0.1, ALFA)
a1.plot([ARRIBA[0], ARRIBA[0]], [0, ARRIBA[1]], color="0.35", lw=0.8, ls="--")
a1.plot([PIE[0], 1.68], [0, 0], color="0.35", lw=0.8, ls="--")
a1.text(ARRIBA[0] + 0.03, ARRIBA[1] / 2 - 0.02, r"$h \approx 0{,}29$ m", va="center", color=C_CORRECTO)
M = PIE + D_4 / 2 * EX - 0.04 * EY
a1.text(1.14, 0.31, r"$d \approx 0{,}48$ m", ha="right", va="center")
a1.add_patch(Arc(PIE, 0.26, 0.26, theta1=0, theta2=37, color="black", lw=0.8))
a1.text(PIE[0] + 0.15, 0.015, "37°", va="bottom", fontsize=9)

# DCL sobre el plano, con los ejes del desarrollo
a2.set_xlim(-2.05, 1.75)
a2.set_ylim(-1.75, 1.55)
BASE = -0.3 * EY
a2.plot(*zip(BASE - 1.6 * EX, BASE + 1.6 * EX), color="black", lw=1.2)
caja(a2, (0, 0), 0.6, ALFA)
a2.annotate("", xy=tuple(1.45 * EX), xytext=tuple(0.3 * EX), arrowprops=dict(arrowstyle="-|>", color="0.45", lw=0.7, shrinkA=0, shrinkB=0))
a2.text(*(1.5 * EX + 0.14 * EY), "$x$", color="0.35", ha="center", va="center")
fuerza(a2, 0, 0, *(1.2 * EY), r"$N \approx 15{,}97$ N", C_VERT, -0.92, 1.25, ha="center")
fuerza(a2, 0, 0, 0, -1.4, r"$w = 20$ N", C_VERT, 0.1, -1.3, ha="left")
fuerza(a2, *(-0.3 * EX), *(-0.8 * EX), r"$f_{rd} \approx 7{,}99$ N", C_HORIZ, -1.35, -0.1, ha="center")
a2.add_patch(Arc((0, 0), 1.1, 1.1, theta1=37, theta2=270, color=C_CORRECTO, lw=0.9, zorder=2))
a2.text(-0.72, 0.42, "233°", color=C_CORRECTO, ha="center", va="center")

guardar(fig, "fig4_ej4_resorte_plano.pdf")


# --- Ejercicio 5: marcha de rayos -------------------------------------------
fig, ax = plt.subplots(figsize=(6.3, 3.6))
ax.set_aspect("equal")
ax.axis("off")
ax.set_xlim(-3.0, 9.4)
ax.set_ylim(-5.9, 2.5)
ax.plot([-2.8, 9.2], [0, 0], color="0.45", lw=0.7)
# Lente (símbolo: línea con puntas hacia afuera)
ax.annotate("", xy=(0, 1.7), xytext=(0, -4.7), arrowprops=dict(arrowstyle="<|-|>", color="black", lw=1.2, shrinkA=0, shrinkB=0))
ax.text(0, 1.85, "lente", ha="center", va="bottom")
# Pantalla
ax.plot([DI_5, DI_5], [-4.7, 1.7], color="0.35", lw=2.5)
ax.text(DI_5, 1.85, "pantalla", ha="center", va="bottom")
# Lámpara e imagen
ax.annotate("", xy=(-DO_5, Y_5), xytext=(-DO_5, 0), arrowprops=dict(arrowstyle="-|>", color=C_T1, lw=2, shrinkA=0, shrinkB=0))
ax.text(-DO_5, Y_5 + 0.2, "lámpara", color=C_T1, ha="center", va="bottom")
ax.annotate("", xy=(DI_5, YI_5), xytext=(DI_5, 0), arrowprops=dict(arrowstyle="-|>", color=C_CORRECTO, lw=2, shrinkA=0, shrinkB=0), zorder=5)
ax.text(DI_5 + 0.15, YI_5 / 2, "imagen", color=C_CORRECTO, ha="left", va="center")
# Rayos principales
for xs, ys in (([-DO_5, 0, DI_5], [Y_5, Y_5, YI_5]),        # paralelo al eje -> por el foco
               ([-DO_5, DI_5], [Y_5, YI_5]),                # por el centro
               ([-DO_5, 0, DI_5], [Y_5, YI_5, YI_5])):      # por el foco -> paralelo al eje
    ax.plot(xs, ys, color=C_T2, lw=0.9, zorder=2)
# Focos
for x, ha, tx, ty, txt in ((-F_5, "right", -F_5 - 0.08, -0.32, "$F$"), (F_5, "left", F_5 + 0.05, 0.3, "$F'$")):
    ax.plot([x], [0], "o", color="black", ms=3.5, zorder=4)
    ax.text(tx, ty, txt, ha=ha, va="center")
# Cotas
for x0, x1, txt in ((-DO_5, 0, "$d_o = 2$ m"), (0, DI_5, "$d_i = 8$ m")):
    ax.annotate("", xy=(x1, -5.15), xytext=(x0, -5.15), arrowprops=dict(arrowstyle="<->", color="black", lw=0.7, shrinkA=0, shrinkB=0))
    ax.text((x0 + x1) / 2, -5.3, txt, ha="center", va="top")

guardar(fig, "fig5_ej5_lente.pdf")
