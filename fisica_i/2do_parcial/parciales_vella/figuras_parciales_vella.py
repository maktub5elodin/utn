r"""Figuras de los parciales del 2do parcial de Física I, curso Z1054 (Prof. R. Vella).

Evaluación de hidrostática (ago/2020), 2º parcial (1/12/2020), 1º recuperatorio
(18/12/2020), recuperatorio (23/2/2021) y dos temas sin fecha (fotos A y B).

Genera en ./figuras/ el PDF vectorial (documento) y el PNG (vista previa del .md).
Uso: python3 figuras_parciales_vella.py   (o `make` desde esta carpeta)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from figuras_comun import *  # noqa: E402,F403
from matplotlib.patches import Arc  # noqa: E402

OUT = salida(__file__)
G = 10.0
PI = np.pi

# =============================================================================
# Comprobaciones numéricas (si alguna falla, no se genera ninguna figura)
# =============================================================================
# H1: tronco que sostiene a un hombre
D_H1 = np.sqrt(4 * 80 / (PI * 1 * (1000 - 800)))
assert np.isclose(D_H1, 0.714, atol=5e-4)
# H2 = A1: cuerpo entre dos líquidos
RHO_H2 = 2 / 3 * 800 + 1 / 3 * 1000
assert np.isclose(RHO_H2, 866.67, atol=5e-3)

# P1: choque plástico en 2D + rozamiento
VX_P1, VY_P1 = 10 * 2 / 11, 1 * 20 / 11
V_P1 = np.hypot(VX_P1, VY_P1)
D_P1 = V_P1 ** 2 / (2 * 0.2 * G)
assert np.isclose(V_P1, 2.571, atol=5e-4) and np.isclose(D_P1, 1.653, atol=5e-4)
assert np.isclose(2.55 ** 2 / (2 * 0.2 * G), 1.63, atol=5e-3)       # valor de la resolución
# P2: resorte vertical
K_P2 = 1 * G / 0.02
T_P2 = 2 * PI * np.sqrt(1 / K_P2)
assert K_P2 == 500 and np.isclose(T_P2, 0.281, atol=5e-4)
assert np.isclose(np.sqrt(K_P2 / 1) * 0.05, 1.118, atol=5e-4) and np.isclose(K_P2 * 0.07, 35)
# P3: cañería que baja 3 m
V2_P3 = (25 / 12) ** 2
P2_P3 = 1e5 + 0.5 * 1000 * (1 - V2_P3 ** 2) + 1000 * G * 3
MDOT_P3 = 1000 * PI * 0.0125 ** 2 * 1
assert np.isclose(V2_P3, 4.34, atol=5e-3) and np.isclose(P2_P3, 121081, atol=1)
assert np.isclose(MDOT_P3, 0.491, atol=5e-4)
# P4 = B4: cilindro que baja rodando y estira un resorte
V_P4 = np.sqrt((10 * G * 0.2 * 0.5 - 0.5 * 250 * 0.2 ** 2) / (0.75 * 10))
assert np.isclose(V_P4, 0.8165, atol=5e-5)
# P5: cilindro tirado desde la periferia por el plano
A_P5 = (2 * 10 - 1 * G * 0.5) / 1.5
F_P5 = 10 - 0.5 * 1 * A_P5
assert np.isclose(A_P5, 10) and np.isclose(F_P5, 5)

# R1 = Q1: choque plástico + resorte con rozamiento
VP_R1 = 0.1 * 7 / 1.0
X_R1 = (-2.5 + np.sqrt(2.5 ** 2 + 4 * 49 * 0.245)) / 98
assert np.isclose(VP_R1, 0.7) and np.isclose(X_R1, 0.0497, atol=5e-5)
# R2: energías en el MAS
assert np.isclose(1 - 0.25 ** 2, 15 / 16)
# R3: bloque de madera atado a un resorte bajo el agua
X_R3 = 5 * G * (1000 - 650) / (160 * 650)
assert np.isclose(X_R3, 0.168, atol=5e-4)
B_R3, W_R3 = 1000 * G * 5 / 650, 5 * G
# R4: cilindro tirado desde arriba
A_R4 = 4 / 3 * 30 / 4
F_R4 = 30 - 0.5 * 4 * A_R4
V_R4 = A_R4 * 5
K_R4 = 0.5 * (0.5 * 4 * 0.5 ** 2) * (V_R4 / 0.5) ** 2 + 0.5 * 4 * V_R4 ** 2
assert np.isclose(A_R4, 10) and np.isclose(F_R4, 10) and np.isclose(K_R4, 7500)
assert np.isclose(30 * 2 * (0.5 * A_R4 * 5 ** 2), K_R4)                # trabajo de F
# R5: resorte + polea + dos masas
V_R5 = np.sqrt((0.5 * 20 * 1 ** 2 - 0.5 * 20 * 5 ** 2 + 15 * G * 4 - 8 * G * 4) / (0.5 * (8 + 15 + 1)))
assert np.isclose(V_R5, 1.826, atol=5e-4)

# Q2: amplitud a partir de T y Fmax
K_Q2 = 4 * PI ** 2 * 0.04 / 0.32 ** 2
assert np.isclose(K_Q2, 15.42, atol=5e-3) and np.isclose(10 / K_Q2, 0.648, atol=5e-4)
# Q3: balsa de troncos
V_Q3 = PI * 0.15 ** 2 * 1.8
N_Q3 = 120 / ((1000 - 800) * V_Q3)
assert np.isclose(V_Q3, 0.1272, atol=5e-5) and np.ceil(N_Q3) == 5
# Q4: barra unida al pivote por una cuerda (sistema rígido)
I_Q4 = 1 / 12 * 1 * 2 ** 2 + 1 * 2 ** 2
W_Q4 = np.sqrt(2 * 1 * G * 2 / I_Q4)
assert np.isclose(W_Q4 * 2, 6.08, atol=5e-3) and np.isclose(1 * G + 1 * W_Q4 ** 2 * 2, 28.46, atol=5e-3)
# Q5: esfera y aro
A_ESF, A_ARO = G * 0.5 / 1.4, G * 0.5 / 2
assert np.isclose(np.sqrt(10 / A_ESF), 1.673, atol=5e-4) and np.isclose(np.sqrt(10 / A_ARO), 2)

# A2: péndulo + choque elástico + resorte con rozamiento
V_A2 = np.sqrt(2 * G * 2 * (1 - np.cos(np.radians(30))))
V2_A2 = 2 * 2 / 3 * V_A2
X_A2 = (-2 + np.sqrt(4 + 4 * 500 * (0.5 * V2_A2 ** 2 - 0.2 * G * 1))) / 1000
assert np.isclose(V_A2, 2.315, atol=5e-4) and np.isclose(V2_A2, 3.087, atol=5e-4)
assert np.isclose(X_A2, 0.0724, atol=5e-5)
# A3: resortes en serie
KEQ_A3 = 4 * PI ** 2 * 3 / 1 ** 2
K2_A3 = KEQ_A3 * 236.8 / (236.8 - KEQ_A3)
assert np.isclose(KEQ_A3, 118.4, atol=0.05) and np.isclose(K2_A3, 236.9, atol=0.05)
# A4: cilindro con tambor
F_A4 = 30 * (0.4 - 0.6 / 2) / (1.5 * 0.6)
assert np.isclose(F_A4, 10 / 3)

# B1: esfera que cae en un líquido
A_B1 = G * (1 - 1 / 3)
assert np.isclose(np.sqrt(2 * 11 / A_B1), 1.817, atol=5e-4)
# B2: choque 1D
V2_B2 = (5 * 20 + 20 * (-10) - 5 * (-20)) / 20
assert V2_B2 == 0 and np.isclose((V2_B2 + 20) / 30, 2 / 3)
# B3: estiramiento estático a partir de T
assert np.isclose(G * 0.5 ** 2 / (4 * PI ** 2), 0.0633, atol=5e-5)
# B5: volante frenado
I_B5 = 0.5 * 4 * 0.2 ** 2
assert np.isclose(2 / I_B5, 25) and np.isclose(400 / (2 * 25) / (2 * PI), 1.273, atol=5e-4)

C_LIQ2 = "#aed6f1"


def plano(ax, largo, ang, origen=(0.0, 0.0)):
    """Plano inclinado que sube hacia la derecha; devuelve (u, n, tope)."""
    a = np.radians(ang)
    u = np.array([np.cos(a), np.sin(a)])
    n = np.array([-np.sin(a), np.cos(a)])
    o = np.asarray(origen, float)
    tope = o + largo * u
    ax.add_patch(Polygon([o, tope, (tope[0], o[1])], closed=True, fc="0.93", ec=C_SUELO, lw=1.2))
    arco_angulo(ax, o, 0.45, 0, ang, rf"${ang:g}^\circ$", rt=0.72)
    return u, n, tope


# =============================================================================
# HIDROSTÁTICA
# =============================================================================
# H1: tronco con el hombre parado encima (justo al ras del agua) y DCL
fig, ax = lienzo(4.2, 2.8, (-1.3, 2.4), (-0.85, 1.65))
ax.add_patch(Rectangle((-1.3, -0.85), 2.3, 1.35, fc=C_LIQUIDO, ec="none", zorder=1))
ax.plot([-1.3, 1.0], [0.5, 0.5], color=C_EMPUJE, lw=1.0)
disco(ax, (0, 0), 0.5, color="#d5b895")
ax.plot([0, 0], [1.2, 0.85], color="0.2", lw=1.3, zorder=5)
ax.plot([-0.12, 0, 0.12], [0.5, 0.85, 0.5], color="0.2", lw=1.3, zorder=5)
ax.plot([-0.2, 0.2], [1.05, 1.05], color="0.2", lw=1.3, zorder=5)
disco(ax, (0, 1.3), 0.1, color="white", z=5)
cota(ax, (-0.72, -0.5), (-0.72, 0.5), r"$d$", off=(-0.15, 0))
ax.text(-1.2, -0.7, "agua", color=C_EMPUJE, fontsize=9)
c = np.array([1.75, 0.3])
punto(ax, c, ms=3)
flecha(ax, c, (0, 1.1), C_EMPUJE, r"$\vec B$", dx=0.2)
flecha(ax, c + (0.12, 0), (0, -0.55), C_PESO, r"$\vec w_{\mathrm{tronco}}$", dx=0.32, dy=0.05)
flecha(ax, c - (0.12, 0), (0, -0.85), C_PESO, r"$\vec w_{\mathrm{hombre}}$", dx=-0.3, dy=0.05)
guardar(fig, OUT, "h1_tronco")

# H2 = A1: cuerpo entre dos líquidos
fig, ax = lienzo(3.6, 2.1, (-0.1, 3.6), (-0.1, 2.0))
ax.add_patch(Rectangle((0, 0), 2.6, 1.0, fc=C_LIQ2, ec="none", zorder=1))
ax.add_patch(Rectangle((0, 1.0), 2.6, 0.85, fc=C_LIQUIDO, ec="none", zorder=1))
ax.plot([0, 0, 2.6, 2.6], [1.95, 0, 0, 1.95], color=C_SUELO, lw=1.4)
ax.plot([0, 2.6], [1.0, 1.0], color=C_EMPUJE, lw=0.8)
bloque(ax, (1.45, 1.15), 0.9, 0.9, r"$\rho_c$")
ax.text(0.3, 1.45, r"$\rho_1$")
ax.text(0.3, 0.45, r"$\rho_2$")
cota(ax, (2.05, 1.0), (2.05, 1.6), r"$\tfrac23 V$", off=(0.4, 0))
cota(ax, (2.05, 0.7), (2.05, 1.0), r"$\tfrac13 V$", off=(0.4, -0.05))
guardar(fig, OUT, "h2_dos_liquidos")

# =============================================================================
# 2º PARCIAL 2020
# =============================================================================
# P1: choque plástico en 2D (vista superior)
fig, ax = lienzo(3.9, 3.0, (-1.75, 2.1), (-1.6, 1.6))
ax.plot([-1.7, 1.9], [0, 0], color="0.6", lw=0.7)
ax.plot([0, 0], [-1.55, 1.55], color="0.6", lw=0.7)
ax.text(1.95, -0.12, r"$x$", color="0.4")
ax.text(0.1, 1.5, r"$y$", color="0.4")
punto(ax, (-1.3, 0), r"$m_1$", dy=-0.17, ms=5)
flecha(ax, (-1.3, 0), (0.6, 0), C_VEL, r"$\vec v_1$", dy=0.17)
punto(ax, (0, -1.3), r"$m_2$", dx=0.25, ms=4)
flecha(ax, (0, -1.3), (0, 0.6), C_VEL, r"$\vec v_2$", dx=-0.22)
punto(ax, (0, 0), ms=6)
flecha(ax, (0, 0), (0.55, 0.55), C_VEL, r"$\vec v_f$", dx=-0.12, dy=0.12)
ax.plot([0.55, 1.15], [0.55, 1.15], color="0.5", lw=0.8, ls="--")
punto(ax, (1.15, 1.15), r"$v = 0$", dx=0.33, ms=3)
cota(ax, (0.25, -0.25), (1.4, 0.9), r"$d$", off=(0.12, -0.12))
arco_angulo(ax, (0, 0), 0.3, 0, 45, r"$45^\circ$", rt=0.5)
guardar(fig, OUT, "p1_choque_2d")

# P2: resorte vertical: natural, equilibrio, punto más bajo
fig, ax = lienzo(3.8, 2.5, (-0.7, 3.6), (-2.05, 0.25))
ax.plot([-0.4, 3.3], [0, 0], color=C_SUELO, lw=1.4)
for xi in np.arange(-0.35, 3.3, 0.12):
    ax.plot([xi, xi + 0.1], [0, 0.1], color=C_SUELO, lw=0.6)
for xc, L, et, masa in ((0, 1.0, "natural", False), (1.4, 1.2, "equilibrio", True),
                        (2.8, 1.7, "más abajo", True)):
    resorte(ax, (xc, 0), (xc, -L), n=7, amp=0.1)
    if masa:
        disco(ax, (xc, -L - 0.1), 0.1, color="0.5")
    ax.text(xc, -2.0, et, ha="center", fontsize=8, color="0.3")
for y in (-1.0, -1.2):
    ax.plot([-0.25, 3.1], [y, y], color="0.6", lw=0.5, ls=":")
cota(ax, (-0.3, 0), (-0.3, -1.0), r"$\ell_0$", off=(-0.15, 0))
cota(ax, (1.75, -1.0), (1.75, -1.2), r"$x_e$", off=(0.2, 0))
cota(ax, (3.15, -1.2), (3.15, -1.7), r"$A$", off=(0.17, 0))
guardar(fig, OUT, "p2_resorte_vertical")

# P3: cañería que baja 3 m hasta un subsuelo
fig, ax = lienzo(4.6, 2.5, (-0.2, 4.6), (-0.35, 3.75))
ax.plot([-0.1, 2.0], [2.75, 2.75], color=C_SUELO, lw=1.2)
ax.plot([0, 2.0], [3.0, 3.0], color="#5dade2", lw=9, solid_capstyle="butt", zorder=3)
ax.plot([2.0, 2.6, 2.6, 3.7], [3.0, 3.0, 0.3, 0.3], color="#5dade2", lw=4.5,
        solid_joinstyle="miter", zorder=3)
suelo(ax, 1.9, 4.0, 0.05, paso=0.1)
ax.text(0.9, 3.55, r"$d_1 = 25$ mm, $p_1 = 10^5$ Pa", ha="center", fontsize=8)
flecha(ax, (0.1, 3.0), (0.5, 0), C_VEL, r"$v_1$", dy=0.22, z=8)
ax.text(3.35, 0.75, r"$d_2 = 12$ mm", ha="center", fontsize=8)
flecha(ax, (3.2, 0.3), (0.45, 0), C_VEL, r"$v_2$", dy=0.2, z=8)
cota(ax, (4.25, 0.3), (4.25, 3.0), r"$3$ m", off=(0, 0))
ax.plot([3.75, 4.35], [0.3, 0.3], color="0.6", lw=0.5, ls=":")
ax.plot([2.1, 4.35], [3.0, 3.0], color="0.6", lw=0.5, ls=":")
ax.text(1.0, 2.55, "superficie", ha="center", fontsize=8, color="0.4")
ax.text(1.0, 0.2, "subsuelo", ha="center", fontsize=8, color="0.4")
guardar(fig, OUT, "p3_caneria")

# P4 = B4: cilindro que baja rodando y estira el resorte
fig, ax = lienzo(3.7, 1.95, (-0.3, 4.2), (-0.15, 2.2))
u, n, tope = plano(ax, 4.0, 30)
ax.plot(*np.c_[tope, tope + 0.55 * n], color=C_SUELO, lw=1.6)
r = 0.3
c = 1.6 * u + r * n
disco(ax, c, r)
punto(ax, c, ms=2.5)
resorte(ax, c, tope + r * n, n=9, amp=0.07)
ax.text(*(c + 1.2 * u + 0.25 * n), r"$k$", ha="center")
c2 = c - 0.75 * u
disco(ax, c2, r, color="white", ls="--", z=3)
cota(ax, c2 + 0.5 * n, c + 0.5 * n, r"$d$", off=-0.12 * n + (0, 0.1))
guardar(fig, OUT, "p4_cilindro_resorte")

# P5: DCL del cilindro tirado desde la periferia, paralelo al plano
fig, ax = lienzo(3.7, 2.15, (-0.3, 4.2), (-0.15, 2.4))
u, n, tope = plano(ax, 4.0, 30)
r = 0.4
pc = 2.0 * u
c = pc + r * n
disco(ax, c, r)
punto(ax, c, ms=2.5)
flecha(ax, c + r * n, 0.8 * u, C_FUERZA, r"$\vec F$", dx=0.15, dy=0.1)
flecha(ax, c, (0, -0.8), C_PESO, r"$\vec w$", dx=0.18)
flecha(ax, pc, 0.6 * n, C_NORMAL, r"$\vec N$", dx=-0.12, dy=-0.12)
flecha(ax, pc, 0.45 * u, C_ROCE, r"$\vec f$", dx=0.08, dy=-0.18)
ax.add_patch(Arc(c, 1.15, 1.15, theta1=150, theta2=200, color="0.3", lw=0.9))
ax.text(*(c + 0.78 * np.array([np.cos(np.radians(175)), np.sin(np.radians(175))])), r"$\gamma_z$",
        ha="center", color="0.3")
guardar(fig, OUT, "p5_cilindro_F")

# =============================================================================
# 1º RECUPERATORIO 2020
# =============================================================================
# R1 = Q1: partícula, bloque y resorte
fig, ax = lienzo(4.6, 1.3, (-0.2, 4.5), (-0.25, 0.85))
suelo(ax, -0.1, 4.4, 0, paso=0.12)
pared(ax, 4.2, 0, 0.75, lado=1, paso=0.12)
punto(ax, (0.3, 0.25), r"$m$", dy=0.2, ms=5)
flecha(ax, (0.4, 0.25), (0.6, 0), C_VEL, r"$v = 7$ m/s", dy=0.18, dx=0.05)
bloque(ax, (2.0, 0.25), 0.5, 0.5, r"$M$")
resorte(ax, (2.25, 0.25), (4.2, 0.25), n=10, amp=0.08)
ax.text(2.4, 0.5, r"$k$", ha="center")
rayado_segmento(ax, (1.6, 0), (4.1, 0), n=14, largo=0.07, lado=1)
ax.text(3.0, 0.62, r"$\mu_k = 0{,}25$", color=C_ROCE, ha="center", fontsize=8)
guardar(fig, OUT, "r1_choque_resorte")

# R2: fracciones de energía en el MAS
fig, ax = plt.subplots(figsize=(4.3, 2.3))
xs = np.linspace(-1, 1, 200)
ax.plot(xs, xs ** 2, color=C_TENSION, lw=1.5, label=r"$U/E$")
ax.plot(xs, 1 - xs ** 2, color=C_VEL, lw=1.5, label=r"$K/E$")
ax.plot([0.25, 0.25], [0, 15 / 16], color="0.5", lw=0.7, ls="--")
ax.plot([0.25], [1 / 16], "o", color=C_TENSION, ms=4)
ax.plot([0.25], [15 / 16], "o", color=C_VEL, ms=4)
for s in (-1, 1):
    ax.plot([s / np.sqrt(2)], [0.5], "o", color="black", ms=4)
    ax.plot([s / np.sqrt(2)] * 2, [0, 0.5], color="0.5", lw=0.7, ls=":")
ax.set_xticks([-1, -1 / np.sqrt(2), 0, 0.25, 1 / np.sqrt(2), 1])
ax.set_xticklabels([r"$-A$", r"$-\frac{A}{\sqrt2}$", "0", r"$\frac{A}{4}$", r"$\frac{A}{\sqrt2}$", r"$A$"])
ax.set_yticks([0, 1 / 16, 0.5, 15 / 16, 1])
ax.set_yticklabels(["0", r"$\frac{1}{16}$", r"$\frac12$", r"$\frac{15}{16}$", "1"])
ax.grid(True, color="0.9", lw=0.6)
ax.set_xlabel(r"$x$")
ax.legend(loc="center left", bbox_to_anchor=(1.0, 0.5), frameon=False)
guardar(fig, OUT, "r2_energias_mas")

# R3: bloque de madera atado al resorte en el fondo; DCL
fig, ax = lienzo(3.3, 2.0, (-0.1, 3.9), (-0.1, 2.3))
ax.add_patch(Rectangle((0, 0), 2.0, 1.9, fc=C_LIQUIDO, ec="none", zorder=1))
ax.plot([0, 0, 2.0, 2.0], [2.1, 0, 0, 2.1], color=C_SUELO, lw=1.4)
resorte(ax, (1.0, 0), (1.0, 0.85), n=7, amp=0.09)
bloque(ax, (1.0, 1.1), 0.5, 0.5, "")
ax.text(0.15, 1.65, "agua", color=C_EMPUJE, fontsize=8)
c = np.array([3.0, 1.0])
punto(ax, c, ms=3)
s = 0.012
flecha(ax, c, (0, B_R3 * s), C_EMPUJE, r"$\vec B$", dx=0.2)
flecha(ax, c - (0.1, 0), (0, -W_R3 * s), C_PESO, r"$\vec w$", dx=-0.2, dy=0.05)
flecha(ax, c + (0.1, 0), (0, -(B_R3 - W_R3) * s), C_TENSION, r"$\vec F_e$", dx=0.25)
guardar(fig, OUT, "r3_bloque_agua")

# R4: DCL del cilindro tirado desde arriba, horizontal
fig, ax = lienzo(3.3, 1.8, (-1.2, 2.3), (-0.85, 1.0))
suelo(ax, -1.1, 2.2, -0.5, paso=0.12)
disco(ax, (0, 0), 0.5)
punto(ax, (0, 0), ms=2.5)
flecha(ax, (0, 0.5), (1.0, 0), C_FUERZA, r"$\vec F$", dy=0.15)
flecha(ax, (0, -0.5), (0.5, 0), C_ROCE, r"$\vec f$", dx=0.15, dy=-0.15)
flecha(ax, (0.1, 0), (0, -0.38), C_PESO, r"$\vec w$", dx=0.17, dy=0.08)
flecha(ax, (-0.1, -0.5), (0, 0.65), C_NORMAL, r"$\vec N$", dx=-0.17, dy=-0.08)
ax.add_patch(Arc((0, 0), 1.35, 1.35, theta1=110, theta2=170, color="0.3", lw=0.9))
ax.text(-0.62, 0.58, r"$\gamma_z$", color="0.3")
guardar(fig, OUT, "r4_cilindro_F")

# R5: resorte, polea y dos masas
fig, ax = lienzo(1.75, 2.4, (-1.3, 1.5), (-0.2, 6.2))
suelo(ax, -1.2, 1.4, 0, paso=0.13)
ax.plot([-0.6, 0.6], [5.95, 5.95], color=C_SUELO, lw=1.6)
for xi in np.arange(-0.55, 0.6, 0.12):
    ax.plot([xi, xi + 0.1], [5.95, 6.05], color=C_SUELO, lw=0.6)
ax.plot([0, 0], [5.95, 5.3], color="0.3", lw=1.2)
disco(ax, (0, 5.3), 0.4, color="0.85")
punto(ax, (0, 5.3), ms=2)
for xc, et in ((-0.4, r"$m_1$"), (0.4, r"$m_2$")):
    ax.plot([xc, xc], [5.3, 4.4], color="0.2", lw=0.9)
    bloque(ax, (xc, 4.2), 0.42, 0.4, et, fs=8)
resorte(ax, (-0.4, 0), (-0.4, 4.0), n=14, amp=0.1)
ax.text(-0.75, 2.0, r"$k$", ha="center")
cota(ax, (0.95, 0), (0.95, 4.0), r"$4$ m", off=(0.08, 0))
ax.plot([0.6, 1.05], [4.0, 4.0], color="0.6", lw=0.5, ls=":")
guardar(fig, OUT, "r5_polea_resorte")

# =============================================================================
# RECUPERATORIO 2021
# =============================================================================
# Q4: barra unida al pivote O por una cuerda
fig, ax = lienzo(2.9, 2.3, (-0.6, 3.3), (-3.25, 0.45))
punto(ax, (0, 0), r"$O$", dx=-0.2, dy=0.12, ms=5)
ax.plot([0, 1], [0, 0], color="0.2", lw=0.9)
ax.add_patch(Rectangle((1, -0.06), 2, 0.12, fc=C_CUERPO, ec="black", lw=1.0, zorder=4))
punto(ax, (2, 0), r"cm", dy=-0.2, ms=3)
ax.plot([0, 0], [0, -1], color="0.5", lw=0.9, ls="--")
ax.add_patch(Rectangle((-0.06, -3), 0.12, 2, fc="white", ec="0.4", lw=0.9, ls="--", zorder=4))
punto(ax, (0, -2), r"cm", dx=0.28, ms=3, color="0.4")
cota(ax, (0, 0.3), (1, 0.3), r"$1$ m", off=(0, 0.0))
cota(ax, (1, 0.3), (3, 0.3), r"$2$ m", off=(0, 0.0))
ax.add_patch(Arc((0, 0), 2.6, 2.6, theta1=-80, theta2=-15, color="0.3", lw=0.9))
ax.annotate("", xy=(0.3, -1.27), xytext=(0.42, -1.22),
            arrowprops=dict(arrowstyle="-|>", color="0.3", lw=0.9, mutation_scale=10))
guardar(fig, OUT, "q4_barra_cuerda")

# =============================================================================
# TEMAS SIN FECHA
# =============================================================================
# A2: péndulo que choca a una partícula que va a un resorte
fig, ax = lienzo(4.8, 2.6, (-1.5, 3.0), (-0.2, 2.5))
o = np.array([0.0, 2.35])
ax.plot([-0.3, 0.3], [o[1], o[1]], color=C_SUELO, lw=2)
pb = np.array([0.0, 0.33])
pa = o + 2.0 * np.array([-np.sin(np.radians(30)), -np.cos(np.radians(30))])
ax.plot(*np.c_[o, pa], color="0.2", lw=0.9)
disco(ax, pa, 0.12, color="0.5")
ax.plot(*np.c_[o, pb], color="0.5", lw=0.7, ls="--")
disco(ax, pb, 0.12, color="white", ls="--")
arco_angulo(ax, o, 0.5, 240, 270, r"$30^\circ$", rt=0.75)
ax.text(-0.8, 1.55, r"$L = 2$ m", ha="right", fontsize=9)
suelo(ax, -1.4, 2.9, 0.08, paso=0.12)
bloque(ax, (0.29, 0.21), 0.22, 0.22, "")
pared(ax, 2.8, 0.08, 0.6, lado=1, paso=0.1)
resorte(ax, (1.4, 0.21), (2.8, 0.21), n=8, amp=0.07)
cota(ax, (0.4, 0.5), (1.4, 0.5), r"$d = 1$ m", off=(0, 0.13))
ax.text(2.1, 0.42, r"$k$", ha="center")
ax.text(1.4, -0.12, r"$\mu_k = 0{,}2$", color=C_ROCE, ha="center", fontsize=8)
guardar(fig, OUT, "a2_pendulo_resorte")

# A3: dos resortes en serie
fig, ax = lienzo(1.3, 1.9, (-0.7, 1.0), (-2.5, 0.2))
ax.plot([-0.4, 0.4], [0, 0], color=C_SUELO, lw=1.6)
resorte(ax, (0, 0), (0, -1.0), n=6, amp=0.1)
punto(ax, (0, -1.0), ms=2.5)
resorte(ax, (0, -1.0), (0, -2.0), n=6, amp=0.1)
disco(ax, (0, -2.15), 0.15, color="0.5")
ax.text(0.25, -0.5, r"$k_1$")
ax.text(0.25, -1.5, r"$k_2$")
ax.text(0.25, -2.2, r"$3$ kg", fontsize=8)
guardar(fig, OUT, "a3_resortes_serie")

# A4: cilindro con tambor tirado desde arriba del tambor
fig, ax = lienzo(4.2, 2.3, (-0.95, 2.4), (-0.9, 0.95))
suelo(ax, -0.9, 2.3, -0.6, paso=0.12)
disco(ax, (0, 0), 0.6, color="0.93")
disco(ax, (0, 0), 0.4, color="0.82")
punto(ax, (0, 0), ms=2.5)
ax.plot([0, 1.0], [0.4, 0.4], color="0.2", lw=0.9)
flecha(ax, (1.0, 0.4), (0.8, 0), C_FUERZA, r"$\vec F$", dy=0.15)
flecha(ax, (0, -0.6), (0.4, 0), C_ROCE, r"$\vec f$", dx=0.15, dy=-0.15)
ax.plot([0, 0.6 * np.cos(np.radians(-30))], [0, 0.6 * np.sin(np.radians(-30))], color="0.25", lw=0.8)
ax.text(0.3, -0.33, r"$R$", fontsize=9)
ax.plot([0, -0.4 * np.cos(np.radians(30))], [0, 0.4 * np.sin(np.radians(30))], color="0.25", lw=0.8)
ax.text(-0.22, 0.25, r"$r$", fontsize=9)
guardar(fig, OUT, "a4_cilindro_tambor")
