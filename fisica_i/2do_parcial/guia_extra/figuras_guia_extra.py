r"""Figuras de la guía de ejercicios extra del 2do parcial de Física I.

Fluidos (F1–F5), cuerpo rígido (R1–R10), momento cinético (MC1–MC3) y
movimiento oscilatorio armónico (MAS1, MAS2, MAS4, MAS5; el MAS3 repite el MAS1).

Genera en ./figuras/ el PDF vectorial (documento) y el PNG (vista previa del .md).
Uso: python3 figuras_guia_extra.py   (o `make` desde esta carpeta)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from figuras_comun import *  # noqa: E402,F403
from matplotlib.patches import Arc  # noqa: E402

OUT = salida(__file__)
G = 10.0

# =============================================================================
# Comprobaciones numéricas (si alguna falla, no se genera ninguna figura)
# =============================================================================
# F1
V_F1 = 5 / 7900
B_F1 = 5 * G - 22.5
RHO_F1 = B_F1 / (G * V_F1)
assert np.isclose(B_F1, 27.5) and np.isclose(RHO_F1, 4345, atol=0.5)
# F3
W_F3 = 0.3e3 * 1500e-6 * G
B_F3 = W_F3 + 3
VS_F3 = B_F3 / (1000 * G)
assert np.isclose(W_F3, 4.5) and np.isclose(B_F3, 7.5) and np.isclose(VS_F3 / 1500e-6, 0.5)
# F4
assert np.isclose(5 * 0.4 * G - 0.4 * G, 16)
# F5
V2_F5 = (25 / 12) ** 2
P2_F5 = 1e5 + 0.5 * 1000 * (1 - V2_F5 ** 2) + 1000 * G * 3.0   # 3 m (errata «3 mm» de la guía; ver 2º parcial Z1054 2020)
assert np.isclose(V2_F5, 4.34, atol=5e-3) and np.isclose(P2_F5, 121081, atol=1)
MDOT_F5 = 1000 * np.pi * 0.0125 ** 2 * 1
assert np.isclose(MDOT_F5, 0.49, atol=5e-3)
# R1
assert np.isclose(1 ** 2 / (2 * G), 0.05)
# R2
assert 3 / 3 <= 0.4 * 0.5 * G and 8 / 3 > 0.4 * 0.5 * G
A_R2 = (8 - 0.1 * 0.5 * G) / 0.5
assert np.isclose(A_R2, 15) and np.isclose(A_R2 * 3, 45)
# R3
M2_R3 = 24 * 1.2 / 0.4
ALFA_R3 = (36 * G * 1.2 - M2_R3 * G * 0.4) / (40 + 36 * 1.2 ** 2 + M2_R3 * 0.4 ** 2)
assert np.isclose(M2_R3, 72) and np.isclose(ALFA_R3, 1.393, atol=5e-4)
# R4 (M = 1, R = 0,2, r = 0,1, I = MR²/2 = 0,02)
I_R4 = 0.5 * 1 * 0.2 ** 2
assert np.isclose((-6 * 0.2 + 2 * 0.1) / I_R4, -50)
F_R4 = (1.0 - 0.1 * 8) / (0.2 + 0.1)      # (I/R) a + R f = 1 y a = 8 + f
assert np.isclose(F_R4, 2 / 3) and np.isclose(8 + F_R4, 26 / 3)
# R5
P_R5 = 100 * np.cos(np.radians(30)) - 10 * G * 0.5
N_R5 = 10 * G * np.cos(np.radians(30)) + 100 * 0.5
A_R5 = 2 * P_R5 / 30
assert np.isclose(A_R5, 2.44, atol=5e-3) and np.isclose(0.5 * 10 * A_R5, 12.2, atol=5e-3)
assert 0.5 * 10 * A_R5 <= 0.35 * N_R5
# R6 (centro de masa en A a 0,9 m; pista en B a 0,2 m; R = 0,1 m)
VB_R6 = np.sqrt(G * (0.9 - 0.3) / 0.7)
assert np.isclose(VB_R6, 2.928, atol=5e-4) and np.isclose(3 * G * (0.9 - 0.1), 24)
# R7
ACM_R7 = 1 * G / (0.75 * 4 + 2 * 1)
assert np.isclose(ACM_R7, 2) and np.isclose(2 * ACM_R7 * 5, 20)
# R8
V_R8 = np.sqrt(2 * G * 0.12)
V0_R8 = 1.808 / 0.008 * V_R8
assert np.isclose(V0_R8, 350.1, atol=0.05)
# R9
assert np.isclose(0.1 * 200 / 20 - 0.1, 0.9) and np.isclose(0.5 * 1 * 400 - 0.5 * 0.1 * 200 ** 2, -1800)
# R10
L10, M10 = 1.4, 1.0
I10, D10, W10 = M10 * L10 ** 2 / 12, L10 / 6, 3.3
MM10 = M10 / 4
V0_R10 = (MM10 * D10 ** 2 * 0 + (I10 * W10 / (MM10 * D10)) ** 2 - I10 * W10 ** 2 / MM10) / (2 * I10 * W10 / (MM10 * D10))
VX_R10 = -V0_R10 + I10 * W10 / (MM10 * D10)
assert np.isclose(V0_R10, 4.235, atol=5e-4) and np.isclose(VX_R10, 5.005, atol=5e-4)
assert np.isclose(MM10 * V0_R10 ** 2 + I10 * W10 ** 2, MM10 * VX_R10 ** 2)
# MC1
IO = 1 * 0.4 ** 2 / 3
TAU_MC1 = (1 * G * 0.2 - 0.5 * IO * 5 ** 2) / (np.pi / 2)
assert np.isclose(TAU_MC1, 0.849, atol=5e-4) and np.isclose(IO * 5, 0.2667, atol=5e-5)
# MC2 (impacto en el punto opuesto a A)
IA = 1.5 * 0.2 * 0.2 ** 2 + 0.2 * 0.4 ** 2
W_MC2 = np.sqrt(2 * 0.4 * G * 0.3 * (1 - np.cos(np.radians(30))) / IA)
V_MC2 = IA * W_MC2 / (0.2 * 0.4)
assert np.isclose(V_MC2, 1.487, atol=5e-4)
# MAS1
T2_MAS1 = 0.93 * np.sqrt(((1 / 12 + 0.3 ** 2) / 0.3) / ((1 / 3) / 0.5))
assert np.isclose(T2_MAS1, 0.866, atol=5e-4)
# MAS2
assert np.isclose(np.pi * 4, 12.566, atol=5e-4) and np.isclose(np.pi ** 2 * 3, 29.609, atol=5e-4)
# MAS4 / MC3
assert np.isclose(2 * G / 200, 0.1) and np.isclose(np.sqrt(200 / 2), 10)
# MAS5
assert np.isclose(0.5 * (2 / 0.1) ** 2, 200)


def recipiente(ax, x0, x1, y0, y1, nivel, color=C_LIQUIDO):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, nivel - y0, fc=color, ec="none", zorder=1))
    ax.plot([x0, x0, x1, x1], [y1, y0, y0, y1], color=C_SUELO, lw=1.5, zorder=3)
    ax.plot([x0, x1], [nivel, nivel], color=C_EMPUJE, lw=0.8, zorder=2)


# =============================================================================
# FLUIDOS
# =============================================================================
# F1: cuerpo colgado de un hilo, sumergido; DCL
fig, (a1, a2) = plt.subplots(1, 2, figsize=(5.6, 2.5), width_ratios=[1.2, 1])
for ax in (a1, a2):
    ax.set_aspect("equal")
    ax.axis("off")
a1.set_xlim(-0.1, 2.1)
a1.set_ylim(-0.1, 1.9)
recipiente(a1, 0.1, 1.9, 0.0, 1.2, 1.0)
a1.plot([0.0, 2.0], [1.65, 1.65], color=C_SUELO, lw=2)
a1.plot([1.0, 1.0], [1.65, 0.6], color="0.2", lw=0.9)
bloque(a1, (1.0, 0.45), 0.7, 0.3, "hierro", fs=8)
a1.text(1.6, 0.15, r"$\rho_L$", color=C_EMPUJE)
a2.set_xlim(-1.0, 1.0)
a2.set_ylim(-1.1, 1.1)
bloque(a2, (0, 0), 0.5, 0.26)
flecha(a2, (-0.1, 0.13), (0, 0.55), C_TENSION, r"$\vec T$", dx=-0.17)
flecha(a2, (0.1, 0.13), (0, 0.7), C_EMPUJE, r"$\vec B$", dx=0.17)
flecha(a2, (0, -0.13), (0, -0.85), C_PESO, r"$\vec w$", dx=0.17)
guardar(fig, OUT, "f1_sumergido")

# F2: dos cuerpos unidos por una soga
fig, (a1, a2) = plt.subplots(1, 2, figsize=(5.6, 2.8), width_ratios=[1, 1.3])
for ax in (a1, a2):
    ax.set_aspect("equal")
    ax.axis("off")
a1.set_xlim(-0.1, 1.5)
a1.set_ylim(-0.1, 2.1)
recipiente(a1, 0.1, 1.3, 0.0, 2.0, 1.5)
disco(a1, (0.7, 1.55), 0.17, "1")
a1.plot([0.7, 0.7], [1.38, 0.55], color="0.2", lw=0.9)
disco(a1, (0.7, 0.42), 0.12, "2", color="0.6")
a2.set_xlim(-1.2, 1.4)
a2.set_ylim(-1.25, 1.25)
disco(a2, (-0.55, 0.45), 0.17, "1")
flecha(a2, (-0.55, 0.62), (0, 0.6), C_EMPUJE, r"$\vec B_1$", dx=0.2)
flecha(a2, (-0.6, 0.28), (0, -0.4), C_PESO, r"$\vec w_1$", dx=-0.2)
flecha(a2, (-0.5, 0.28), (0, -0.35), C_TENSION, r"$\vec T$", dx=0.2)
disco(a2, (0.65, -0.35), 0.12, "2", color="0.6")
flecha(a2, (0.6, -0.23), (0, 0.4), C_TENSION, r"$\vec T$", dx=-0.2)
flecha(a2, (0.7, -0.23), (0, 0.3), C_EMPUJE, r"$\vec B_2$", dx=0.22)
flecha(a2, (0.65, -0.47), (0, -0.6), C_PESO, r"$\vec w_2$", dx=0.2)
guardar(fig, OUT, "f2_dos_cuerpos")

# F3: esfera atada al fondo
fig, (a1, a2) = plt.subplots(1, 2, figsize=(5.6, 2.5), width_ratios=[1.2, 1])
for ax in (a1, a2):
    ax.set_aspect("equal")
    ax.axis("off")
a1.set_xlim(-0.1, 2.1)
a1.set_ylim(-0.1, 1.8)
recipiente(a1, 0.1, 1.9, 0.0, 1.6, 1.2)
disco(a1, (1.0, 1.2), 0.3, "esfera")
a1.plot([1.0, 1.0], [0.9, 0.0], color="0.2", lw=0.9)
a1.text(1.1, 0.4, "cuerda", fontsize=8)
a1.text(0.25, 0.15, "agua", color=C_EMPUJE)
a2.set_xlim(-1.0, 1.0)
a2.set_ylim(-1.1, 1.1)
disco(a2, (0, 0), 0.22)
flecha(a2, (0, 0.22), (0, 0.75), C_EMPUJE, r"$\vec B$", dx=0.17)
flecha(a2, (-0.08, -0.2), (0, -0.45), C_PESO, r"$\vec w$", dx=-0.2)
flecha(a2, (0.08, -0.2), (0, -0.3), C_TENSION, r"$\vec T$", dx=0.2)
guardar(fig, OUT, "f3_esfera_atada")

# F4: cubo flotando y cubo sumergido con F
fig, ax = lienzo(5.0, 2.0, (-0.1, 3.3), (-0.1, 1.45))
for x0 in (0.1, 1.8):
    recipiente(ax, x0, x0 + 1.4, 0.0, 1.3, 0.9)
bloque(ax, (0.8, 0.9 + 0.5 * 0.5 - 0.5 / 5), 0.5, 0.5)
ax.text(0.8, 1.38, r"flota: $V_s = V/5$", ha="center", fontsize=9)
bloque(ax, (2.5, 0.45), 0.5, 0.5)
flecha(ax, (2.5, 1.25), (0, -0.55), C_FUERZA, r"$\vec F$", dx=0.2, dy=0.35)
ax.text(2.5, 1.38, "totalmente sumergido", ha="center", fontsize=9)
guardar(fig, OUT, "f4_cubo")

# F5: cañería que se angosta y desciende
fig, ax = lienzo(6.0, 1.9, (-0.1, 6.2), (-0.65, 0.95))
y1, y2, r1, r2 = 0.35, 0.05, 0.3, 0.15
xs = np.array([0, 2.4, 3.4, 6.0])
ax.plot(xs, [y1 + r1, y1 + r1, y2 + r2, y2 + r2], color=C_SUELO, lw=1.4)
ax.plot(xs, [y1 - r1, y1 - r1, y2 - r2, y2 - r2], color=C_SUELO, lw=1.4)
ax.add_patch(Polygon(np.c_[np.r_[xs, xs[::-1]], np.r_[[y1 + r1, y1 + r1, y2 + r2, y2 + r2],
                                                       [y2 - r2, y2 - r2, y1 - r1, y1 - r1]]],
                     fc=C_LIQUIDO, ec="none", zorder=1))
ax.plot([0, 6], [y1, y1], color="0.6", lw=0.6, ls="--")
flecha(ax, (0.5, y1), (0.6, 0), C_VEL, r"$v_1$", dy=0.12)
flecha(ax, (4.2, y2), (1.2, 0), C_VEL, r"$v_2$", dy=0.12)
ax.text(1.5, y1 - 0.12, r"$d_1 = 25$ mm, $p_1$", ha="center", va="top", fontsize=9)
ax.text(4.8, y2 - 0.2, r"$d_2 = 12$ mm, $p_2$", ha="center", va="top", fontsize=9)
cota(ax, (5.9, y2), (5.9, y1), r"$\Delta y$", off=(0.22, 0))
ax.text(3.0, -0.6, "(fuera de escala)", ha="center", color="0.4", fontsize=8)
guardar(fig, OUT, "f5_caneria")

# =============================================================================
# CUERPO RÍGIDO
# =============================================================================
# R1: cilindro que sube por una rampa sin rozamiento
fig, ax = lienzo(5.6, 1.9, (-0.2, 5.2), (-0.25, 1.5))
suelo(ax, -0.1, 5.1, 0, paso=0.13)
ax.plot([2.2, 4.0, 5.1], [0, 1.0, 1.0], color=C_SUELO, lw=1.3)
disco(ax, (0.5, 0.22), 0.22)
punto(ax, (0.5, 0.22), ms=2)
flecha(ax, (0.75, 0.22), (0.45, 0), C_VEL, r"$v_{\mathrm{cm}} = 1$ m/s", dy=0.2, dx=0.05)
ax.add_patch(Arc((0.5, 0.22), 0.6, 0.6, theta1=40, theta2=140, color=C_VEL, lw=1.0))
ax.text(0.5, 0.62, r"$\omega$", color=C_VEL, ha="center")
pc = np.array([3.2, 0.667]) + 0.22 * np.array([-0.486, 0.874])
disco(ax, pc, 0.22, color="white", ls="--")
ax.plot([0.5, 4.6], [pc[1], pc[1]], color="0.6", lw=0.6, ls=":")
cota(ax, (4.6, 0.22), (4.6, pc[1]), r"$H$", off=(0.18, 0))
ax.text(3.0, 0.15, "sin rozamiento", ha="left", color=C_ROCE, fontsize=8, rotation=29)
guardar(fig, OUT, "r1_rampa")

# R2: DCL del disco tirado del centro
fig, ax = lienzo(4.0, 2.1, (-1.2, 2.0), (-0.85, 0.95))
suelo(ax, -1.1, 1.9, -0.45, paso=0.12)
disco(ax, (0, 0), 0.45)
punto(ax, (0, 0), ms=2)
flecha(ax, (0, 0), (1.1, 0), C_FUERZA, r"$\vec F$", dy=0.13)
flecha(ax, (0, -0.45), (-0.5, 0), C_ROCE, r"$\vec f$", dy=-0.15)
flecha(ax, (0.08, 0), (0, -0.75), C_PESO, r"$\vec w$", dx=0.2, dy=0.1)
flecha(ax, (-0.1, -0.45), (0, 0.75), C_NORMAL, r"$\vec N$", dx=-0.2)
guardar(fig, OUT, "r2_disco_F")

# R3: dos ruedas solidarias
fig, ax = lienzo(3.6, 2.8, (-1.7, 1.7), (-2.0, 1.4))
disco(ax, (0, 0), 1.2, color="0.93")
disco(ax, (0, 0), 0.4, color="0.85")
punto(ax, (0, 0), ms=2.5)
ax.plot([-1.2, -1.2], [0, -1.35], color="0.2", lw=0.9)
ax.plot([0.4, 0.4], [0, -1.55], color="0.2", lw=0.9)
bloque(ax, (-1.2, -1.55), 0.42, 0.4, r"$m_1$")
bloque(ax, (0.4, -1.75), 0.42, 0.4, r"$m_2$")
ax.plot([0, -1.2 * 0.6], [0, 1.2 * 0.8], color="0.25", lw=0.9, zorder=6)
ax.text(-0.5, 0.55, r"$r_1$", ha="center", zorder=7)
ax.plot([0, 0.4], [0, 0], color="0.25", lw=0.9, zorder=6)
ax.text(0.2, 0.1, r"$r_2$", ha="center", zorder=7)
guardar(fig, OUT, "r3_ruedas")

# R4: yo-yo con F1 arriba y F2 abajo del disco interior
fig, ax = lienzo(4.4, 2.3, (-0.4, 0.75), (-0.27, 0.32))
suelo(ax, -0.35, 0.7, -0.2, paso=0.04)
disco(ax, (0, 0), 0.2, color="0.93")
disco(ax, (0, 0), 0.1, color="0.85")
punto(ax, (0, 0), ms=2)
flecha(ax, (0, 0.2), (0.35, 0), C_FUERZA, r"$\vec F_1$", dx=0.05, dy=0.04)
flecha(ax, (0, -0.1), (0.35, 0), C_FUERZA, r"$\vec F_2$", dx=0.05, dy=0.04)
flecha(ax, (0, -0.2), (0.12, 0), C_ROCE, r"$\vec f$", dx=0.03, dy=-0.04)
ejes(ax, (0.5, -0.12), 0.08, etiquetas=("$x$", "$y$"), sep=0.02)
guardar(fig, OUT, "r4_yoyo")

# R5: disco en plano de 30° con fuerza horizontal
fig, ax = lienzo(5.0, 2.7, (-0.2, 3.7), (-0.2, 1.95))
ang = 30
u = np.array([np.cos(np.radians(-ang)), np.sin(np.radians(-ang))])     # baja por el plano
nv = np.array([np.sin(np.radians(ang)), np.cos(np.radians(ang))])
top = np.array([0.0, 1.7])
base = top + 3.4 * u
ax.add_patch(Polygon([top, base, (0, base[1])], closed=True, fc="0.93", ec=C_SUELO, lw=1.2))
c = top + 1.55 * u + 0.3 * nv
disco(ax, c, 0.3)
punto(ax, c, ms=2)
flecha(ax, c + np.array([0.95, 0]), (-0.85, 0), C_FUERZA, r"$\vec F$", dx=0.95, dy=0.0)
flecha(ax, c, (0, -0.75), C_PESO, r"$\vec w$", dx=0.18)
pc = c - 0.3 * nv
flecha(ax, pc, 0.6 * nv, C_NORMAL, r"$\vec N$", dx=-0.13, dy=0.12)
flecha(ax, pc, 0.45 * u, C_ROCE, r"$\vec f$", dx=0.18, dy=0.02)
arco_angulo(ax, base, 0.5, 180 - ang, 180, r"$30^\circ$", rt=0.75)
guardar(fig, OUT, "r5_plano_F")

# R6: esfera que baja por la pista y sale horizontal en B
fig, ax = lienzo(5.4, 3.0, (-0.25, 1.75), (-0.08, 1.05))
suelo(ax, -0.2, 1.7, 0, paso=0.05)
xa, ya = 0.1, 0.9
xb, yb = 0.75, 0.2
t = np.linspace(0, 1, 100)
xs = xa + (xb - xa) * t
ys = yb + (ya - 0.1 - yb) * (1 - (3 * t ** 2 - 2 * t ** 3))
ax.plot(xs, ys, color=C_SUELO, lw=1.4)
disco(ax, (xa, ya), 0.1, color="0.5")
disco(ax, (xb, yb + 0.1), 0.1, color="white", ls="--")
tt = np.linspace(0, 0.2, 30)
ax.plot(xb + VB_R6 * tt, yb + 0.1 - 0.5 * G * tt ** 2, color=C_VEL, lw=1.0, ls="--")
punto(ax, (xa, ya), "A", dx=0.17, dy=0.04)
punto(ax, (xb, yb), "B", dx=0.06, dy=-0.06)
punto(ax, (xb + VB_R6 * 0.2, 0.1), "C", dx=0.1, dy=0.06)
cota(ax, (-0.12, 0), (-0.12, ya), r"$0{,}9$ m", off=(-0.03, 0), ha="right")
cota(ax, (xb, 0), (xb, yb), r"$0{,}2$ m", off=(-0.13, 0))
ax.plot([-0.12, xa], [ya, ya], color="0.6", lw=0.6, ls=":")
flecha(ax, (xb + 0.12, yb + 0.1), (0.25, 0), C_VEL, r"$\vec v_B$", dy=0.07)
guardar(fig, OUT, "r6_esfera_pista")

# R7: disco rodando sobre la mesa, cuerda desde arriba, bloque colgante
fig, ax = lienzo(5.0, 2.6, (-0.1, 3.4), (-0.75, 1.15))
ax.plot([0, 2.5, 2.5], [0, 0, -0.75], color=C_SUELO, lw=1.4)
disco(ax, (0.8, 0.4), 0.4)
punto(ax, (0.8, 0.4), ms=2)
rp = 0.1
cp = np.array([2.6, 0.8 - rp])
ax.plot([2.5, cp[0]], [0, cp[1]], color="0.3", lw=1.0)
disco(ax, cp, rp, color="0.85")
ax.plot([0.8, cp[0]], [0.8, 0.8], color="0.2", lw=0.9)
ax.plot([cp[0] + rp, cp[0] + rp], [cp[1], -0.25], color="0.2", lw=0.9)
bloque(ax, (cp[0] + rp, -0.42), 0.32, 0.32, r"$m_2$")
ax.text(0.8, 0.4, r"$m_1$", ha="center", va="top")
flecha(ax, (1.3, 0.92), (0.5, 0), C_VEL, r"$v = 2\,v_{\mathrm{cm}}$", dx=0.45, ha="left")
flecha(ax, (0.8, 0.4), (0.3, 0), C_VEL, r"$v_{\mathrm{cm}}$", dx=0.12, dy=0.12, ha="left")
punto(ax, (0.8, 0), "P", dy=-0.13, ms=2.5)
flecha(ax, (cp[0] + rp + 0.3, -0.1), (0, -0.4), C_VEL, r"$v$", dx=0.12)
guardar(fig, OUT, "r7_disco_mesa")

# R8: péndulo balístico
fig, ax = lienzo(4.6, 2.5, (-0.9, 1.3), (-0.15, 1.15))
o = np.array([0.0, 1.05])
ax.plot([-0.3, 0.3], [o[1], o[1]], color=C_SUELO, lw=2)
Lp = 0.85
th = np.radians(32)
p1 = o + Lp * np.array([0, -1])
p2 = o + Lp * np.array([np.sin(th), -np.cos(th)])
ax.plot([o[0], p1[0]], [o[1], p1[1]], color="0.2", lw=0.9)
ax.plot([o[0], p2[0]], [o[1], p2[1]], color="0.2", lw=0.9, ls="--")
bloque(ax, p1, 0.16, 0.16, r"$M$", fs=8)
bloque(ax, p2, 0.16, 0.16, color="white")
ax.add_patch(Arc(o, 2 * Lp, 2 * Lp, theta1=270, theta2=270 + 32, color="0.5", lw=0.8, ls=":"))
cota(ax, (p2[0] + 0.22, p1[1]), (p2[0] + 0.22, p2[1]), r"$h$", off=(0.12, 0))
ax.plot([p1[0] + 0.08, p2[0] + 0.25], [p1[1], p1[1]], color="0.6", lw=0.6, ls=":")
punto(ax, (-0.6, p1[1]), r"$m_p$", dy=-0.1, ms=3)
flecha(ax, (-0.55, p1[1]), (0.35, 0), C_VEL, r"$\vec v_{0p}$", dy=0.1)
guardar(fig, OUT, "r8_pendulo_balistico")

# R9: bala que se incrusta en un bloque
fig, (a1, a2) = plt.subplots(1, 2, figsize=(5.6, 1.3))
for ax in (a1, a2):
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-0.2, 2.0)
    ax.set_ylim(-0.15, 0.55)
    suelo(ax, -0.1, 1.9, 0, paso=0.09)
punto(a1, (0.1, 0.15), ms=3)
flecha(a1, (0.15, 0.15), (0.45, 0), C_VEL, r"$200$ m/s", dy=0.13)
bloque(a1, (1.3, 0.2), 0.4, 0.4, r"$M$")
a1.text(-0.1, 0.48, "antes", color="0.35")
bloque(a2, (0.55, 0.2), 0.7, 0.4, r"$M + m$")
flecha(a2, (0.95, 0.2), (0.45, 0), C_VEL, r"$20$ m/s", dy=0.13)
a2.text(-0.1, 0.48, "después", color="0.35")
guardar(fig, OUT, "r9_bala_bloque")

# R10: varilla que gira y pelotita (vista superior)
fig, ax = lienzo(3.6, 2.9, (-1.0, 1.6), (-0.85, 0.95))
ax.add_patch(Rectangle((-0.04, -0.7), 0.08, 1.4, fc="0.88", ec="black", lw=1.0, zorder=3))
punto(ax, (0, 0), "O", dx=-0.15, ms=3)
yb = 0.7 - 1.4 / 3
flecha(ax, (1.2, yb), (-0.5, 0), C_VEL, r"$\vec V_0$", dy=0.12)
punto(ax, (1.25, yb), r"$m$", dx=0.15, ms=4)
cota(ax, (-0.25, 0.7), (-0.25, yb), r"$x = L/3$", off=(-0.07, 0), ha="right")
cota(ax, (0.25, 0), (0.25, yb), r"$d$", off=(0.12, 0))
ax.add_patch(Arc((0, 0), 1.7, 1.7, theta1=60, theta2=120, color=C_VEL, lw=1.0))
flecha(ax, (0.43, 0.74), (0.04, -0.03), C_VEL, lw=1.0)
ax.text(0.0, 0.9, r"$\omega_0$", color=C_VEL, ha="center")
ejes(ax, (0.9, -0.7), 0.25, etiquetas=("$x$", "$y$"))
guardar(fig, OUT, "r10_varilla_pelota")

# =============================================================================
# MOMENTO CINÉTICO
# =============================================================================
# MC1: barra que cae desde la horizontal
fig, ax = lienzo(3.8, 2.6, (-0.75, 1.3), (-1.05, 0.3))
ax.add_patch(Rectangle((0, -0.03), 1.0, 0.06, fc="0.88", ec="black", lw=0.9, zorder=3))
ax.add_patch(Rectangle((-0.03, -1.0), 0.06, 1.0, fc="white", ec="black", lw=0.9, ls="--", zorder=3))
punto(ax, (0, 0), "O", dy=0.13, ms=3.5)
punto(ax, (0, -0.5), dx=0.0, ms=2.5)
flecha(ax, (0, -0.5), (-0.4, 0), C_VEL, r"$\vec v_{\mathrm{cm}}$", dy=-0.12)
ax.add_patch(Arc((0, 0), 1.3, 1.3, theta1=275, theta2=355, color="0.4", lw=0.9))
flecha(ax, np.array([0.65 * np.cos(np.radians(278)), 0.65 * np.sin(np.radians(278))]),
       (-0.03, -0.0), "0.4", lw=0.9)
ax.text(0.65, -0.55, "cae", color="0.4")
ax.text(0.25, -0.2, r"$\otimes\ \vec L_O$", color=C_VEL)
guardar(fig, OUT, "mc1_barra")

# MC2: disco colgado de A y bala que impacta en el punto opuesto
fig, ax = lienzo(3.6, 2.6, (-1.3, 1.1), (-0.75, 0.95))
r = 0.35
a = np.array([0.0, 0.75])
disco(ax, a + np.array([0, -r]), r)
punto(ax, a, "A", dy=0.12, ms=4)
ax.plot([-0.2, 0.2], [a[1] + 0.05, a[1] + 0.05], color=C_SUELO, lw=2)
pb = a + np.array([0, -2 * r])
punto(ax, pb, dy=-0.1, ms=2.5)
punto(ax, (-1.0, pb[1]), r"$m$", dy=-0.12, ms=4)
flecha(ax, (-0.95, pb[1]), (0.5, 0), C_VEL, r"$\vec v$", dy=0.12)
ax.text(0.0, a[1] - r, r"$m$", ha="center", va="center")
cr = a + 0.35 * np.array([np.sin(np.radians(30)), -np.cos(np.radians(30))])
disco(ax, cr, r, color="none", ls="--", z=2)
ax.plot([a[0], a[0]], [a[1], a[1] - 0.55], color="0.5", lw=0.6, ls=":")
ax.plot([a[0], a[0] + 0.55 * np.sin(np.radians(30))], [a[1], a[1] - 0.55 * np.cos(np.radians(30))],
        color="0.5", lw=0.6, ls=":")
ax.add_patch(Arc(a, 0.9, 0.9, theta1=270, theta2=300, color="0.3", lw=0.9, zorder=6))
ax.text(0.17, 0.15, r"$30^\circ$", color="0.3", zorder=7)
guardar(fig, OUT, "mc2_disco_bala")

# MC3 y MAS4: posición en función del tiempo
t = np.linspace(0, 1.3, 400)
fig, ax = plt.subplots(figsize=(5.2, 2.2))
ejes_grafico(ax, "$t$ (s)", "$y$ (m)")
ax.plot(t, 0.1 * np.cos(10 * t + np.pi), color=C_PESO, lw=1.6)
ax.axhline(0, color="0.4", lw=0.7)
ax.plot([0], [-0.1], "o", color=C_PESO, ms=4)
ax.set_yticks([-0.1, 0, 0.1])
ax.set_xticks([0, 2 * np.pi / 10, 4 * np.pi / 10])
ax.set_xticklabels(["0", r"$T \approx 0{,}63$", r"$2T$"])
ax.text(0.05, -0.085, r"$t = 0$: $y = -0{,}1$ m", va="bottom", fontsize=9)
guardar(fig, OUT, "mc3_ecuacion_horaria")

fig, ax = plt.subplots(figsize=(5.2, 2.2))
ejes_grafico(ax, "$t$ (s)", "$y$ (m)")
ax.plot(t, 0.2 * np.cos(10 * t), color=C_PESO, lw=1.6, label="$y$")
ax.axhline(0, color="0.4", lw=0.7)
ax.set_yticks([-0.2, 0, 0.2])
ax.set_xticks([0, 2 * np.pi / 10, 4 * np.pi / 10])
ax.set_xticklabels(["0", r"$T \approx 0{,}63$", r"$2T$"])
ax.plot([0], [0.2], "o", color=C_PESO, ms=4)
guardar(fig, OUT, "mas4_ecuacion_horaria")

# =============================================================================
# MOVIMIENTO OSCILATORIO ARMÓNICO
# =============================================================================
# MAS1: varilla colgada del extremo y a L/5
fig, (a1, a2) = plt.subplots(1, 2, figsize=(4.6, 2.6))
for ax, dpiv, tit in ((a1, 0.0, r"pivote en el extremo"), (a2, 0.2, r"pivote a $L/5$")):
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-0.6, 0.6)
    ax.set_ylim(-1.1, 0.35)
    ax.add_patch(Rectangle((-0.03, -1.0 + dpiv), 0.06, 1.0, fc="0.88", ec="black", lw=0.9))
    punto(ax, (0, 0), "O", dx=0.13, ms=4)
    punto(ax, (0, -0.5 + dpiv), dx=0.0, ms=2.5)
    ax.text(0.1, -0.5 + dpiv, "cm", fontsize=8, va="center")
    cota(ax, (-0.15, 0), (-0.15, -0.5 + dpiv), r"$d$", off=(-0.1, 0))
    ax.text(0, 0.25, tit, ha="center", fontsize=9)
guardar(fig, OUT, "mas1_pendulo_fisico")

# MAS2: x(t) con los pasos por x = 3 cm
t = np.linspace(0, 4, 400)
fig, ax = plt.subplots(figsize=(5.2, 2.2))
ejes_grafico(ax, "$t$ (s)", "$x$ (cm)")
ax.plot(t, 5 * np.cos(np.pi * t), color=C_PESO, lw=1.6)
ax.axhline(3, color=C_VEL, lw=0.8, ls="--")
for tc in (np.arccos(0.6) / np.pi, 2 - np.arccos(0.6) / np.pi, 2 + np.arccos(0.6) / np.pi,
           4 - np.arccos(0.6) / np.pi):
    ax.plot([tc], [3], "o", color=C_VEL, ms=4)
ax.set_yticks([-5, 0, 3, 5])
ax.set_xticks([0, 1, 2, 3, 4])
ax.text(3.0, 3.6, r"$x = 3$ cm", color=C_VEL, fontsize=9)
guardar(fig, OUT, "mas2_xt")

# MAS5: resorte horizontal en sus longitudes extremas
fig, ax = lienzo(5.0, 1.8, (-0.05, 0.85), (-0.06, 0.25))
for y0, l in ((0.17, 0.3), (0.03, 0.5)):
    pared(ax, 0, y0 - 0.02, y0 + 0.06, lado=-1, paso=0.02)
    resorte(ax, (0, y0 + 0.02), (l, y0 + 0.02), n=9, amp=0.012)
    bloque(ax, (l + 0.05, y0 + 0.02), 0.1, 0.07, r"$m$", fs=8)
ax.plot([0.4, 0.4], [-0.03, 0.25], color="0.5", lw=0.7, ls=":")
ax.text(0.4, -0.05, r"$\ell_0$", ha="center", va="top", fontsize=9)
ax.text(0.7, 0.19, r"$\ell_{\min} = 30$ cm", fontsize=9)
ax.text(0.7, 0.05, r"$\ell_{\max} = 50$ cm", fontsize=9)
suelo(ax, 0, 0.66, -0.0, paso=0.02, rayado=False)
guardar(fig, OUT, "mas5_resorte_horizontal")
