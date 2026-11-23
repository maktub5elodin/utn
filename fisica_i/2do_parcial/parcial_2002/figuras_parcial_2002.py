r"""Figuras del parcial de Física I de 2002 (resolución de H. Cassia), con los
enunciados reconstruidos.

Problema 1: pista circular, choque elástico en B y tramo BC con rozamiento.
Problema 2: dos bloques impulsados por resortes, choque plástico.
Problema 3: polea con inercia que frena a un bloque que sube por el plano (y DCL).
Problema 4: bloque en el plano, cuerda por una polea con masa y resorte.

Genera en ./figuras/ el PDF vectorial (documento) y el PNG (vista previa del .md).
Uso: python3 figuras_parcial_2002.py   (o `make` desde esta carpeta)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from figuras_comun import *  # noqa: E402,F403
from matplotlib.patches import Arc  # noqa: E402

OUT = salida(__file__)
G = 10.0

# --- Problema 1 -------------------------------------------------------------
R1, BC = 0.8, 1.7
VB = np.sqrt(2 * G * R1)
V1P, V2P = -VB / 3, 2 * VB / 3          # m2 = 2 m1
MU1 = V2P ** 2 / (2 * G * BC)
HD = V1P ** 2 / (2 * G)
assert np.isclose(VB, 4) and np.isclose(V1P, -4 / 3) and np.isclose(V2P, 8 / 3)
assert np.isclose(MU1, 0.209, atol=5e-4) and np.isclose(HD, 0.0889, atol=5e-5)
assert np.isclose(1 * VB, 1 * V1P + 2 * V2P)                    # cantidad de movimiento
assert np.isclose(VB ** 2, V1P ** 2 + 2 * V2P ** 2)             # energía cinética

# --- Problema 2 -------------------------------------------------------------
M1, M2 = 1.0, 4.0
K1, K2 = 1280.0, 1600.0
X1, X2 = 6 / np.sqrt(K1 / M1), 0.1
V10, V20 = 6.0, -2.0
VP = (M1 * V10 + M2 * V20) / (M1 + M2)
XC = np.sqrt((M1 + M2) / K1) * abs(VP)
assert np.isclose(np.sqrt(K1 / M1) * X1, 6) and np.isclose(np.sqrt(K2 / M2) * X2, 2)
assert np.isclose(VP, -0.4) and np.isclose(XC, 0.025) and np.isclose(X1, 0.1677, atol=5e-5)

# --- Problema 3 -------------------------------------------------------------
S53, C53 = 0.8, 0.6
A3 = 4.75
MU3 = (2 * A3 / G - S53) / C53
T3 = 5 / A3
D3 = 5 ** 2 / (2 * A3)
assert np.isclose(MU3, 0.25)
assert np.isclose(A3, G * (S53 + MU3 * C53) / (1 + 1))           # m + I/R² = 2m
assert np.isclose(T3, 1.05, atol=5e-3) and np.isclose(D3, 2.63, atol=5e-3)
assert G * (S53 + MU3 * C53) > A3                                  # la cuerda no se afloja

# --- Problema 4 -------------------------------------------------------------
M4, MP4, DX4, K4 = 2.0, 2.0, 0.5, 36.0
S37 = 0.6
VB4 = np.sqrt((2 * M4 * G * DX4 * S37 - K4 * DX4 ** 2) / (M4 + MP4 / 2))
assert np.isclose(VB4, 1.0)


# --- Figura 1 ---------------------------------------------------------------
fig, ax = lienzo(6.3, 2.6, (-0.35, 2.95), (-0.32, 1.05))
c = np.array([R1, R1])
t = np.linspace(np.pi, 1.5 * np.pi, 100)
ax.plot(c[0] + R1 * np.cos(t), c[1] + R1 * np.sin(t), color=C_SUELO, lw=1.4)
suelo(ax, R1, R1 + BC + 0.25, 0, rayado=False)
rayado_segmento(ax, (R1, 0), (R1 + BC, 0), n=18, largo=0.07, lado=-1)
pared(ax, -0.0, 0, 0.85, lado=-1, paso=0.1)
ax.plot([0, 0.0], [0.8, 0.8], color=C_SUELO)
bloque(ax, (0.07, 0.86), 0.12, 0.12, "1", fs=8)
bloque(ax, (R1 + 0.09, 0.07), 0.14, 0.14, "2", fs=8)
punto(ax, (0, R1), "A", dx=-0.12, dy=0.05)
punto(ax, (R1, 0), "B", dy=-0.13)
punto(ax, (R1 + BC, 0), "C", dy=-0.13)
yd = R1 - np.sqrt(R1 ** 2 - (R1 - HD) ** 2) if False else HD
xd = c[0] - np.sqrt(R1 ** 2 - (R1 - yd) ** 2)
punto(ax, (xd, yd), "D", dx=-0.1, dy=0.05)
ax.plot([xd, R1 + 0.35], [yd, yd], color="0.5", lw=0.6, ls=":")
cota(ax, (R1 + 0.35, 0), (R1 + 0.35, yd), "", off=(0, 0))
ax.text(R1 + 0.42, yd / 2 + 0.01, r"$h_D$", va="center", ha="left")
cota(ax, (-0.22, 0), (-0.22, R1), r"$R$", off=(-0.07, 0))
cota(ax, (R1, -0.2), (R1 + BC, -0.2), r"$\overline{BC} = 1{,}7$ m", off=(0, -0.07))
flecha(ax, (R1 - 0.03, 0.2), (-0.35, 0), C_VEL, r"$v_1'$", dy=0.07)
flecha(ax, (R1 + 0.2, 0.2), (0.6, 0), C_VEL, r"$v_2'$", dy=0.07)
ax.text(R1 + BC / 2 + 0.25, 0.08, r"$\mu_k$", color=C_ROCE, ha="center")
guardar(fig, OUT, "fig1_p1_pista")


# --- Figura 2 ---------------------------------------------------------------
fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.3, 3.0))
for ax in (a1, a2):
    ax.set_aspect("equal")
    ax.set_xlim(-0.1, 3.1)
    ax.set_ylim(-0.12, 0.52)
    ax.axis("off")
    suelo(ax, 0, 3.0, 0, paso=0.1)
    pared(ax, 0, 0, 0.35, lado=-1, paso=0.09)
    pared(ax, 3.0, 0, 0.35, lado=1, paso=0.09)
# antes del choque: resortes ya en su longitud natural
resorte(a1, (0, 0.12), (0.55, 0.12), n=7, amp=0.045)
resorte(a1, (2.35, 0.17), (3.0, 0.17), n=7, amp=0.045)
bloque(a1, (1.05, 0.11), 0.2, 0.2, "1", fs=9)
bloque(a1, (1.95, 0.15), 0.3, 0.3, "2", fs=9)
flecha(a1, (0.95, 0.3), (0.4, 0), C_VEL, r"$v_1 = 6$ m/s", dx=-0.2, dy=0.08)
flecha(a1, (2.05, 0.38), (-0.2, 0), C_VEL, r"$v_2 = -2$ m/s", dx=0.1, dy=0.08)
a1.text(0.27, 0.27, r"$k_1$", ha="center")
a1.text(2.68, 0.32, r"$k_2$", ha="center")
a1.text(-0.05, 0.42, "antes del choque", ha="left", color="0.35")
# después: el conjunto comprime el resorte 1
resorte(a2, (0, 0.12), (0.5, 0.12), n=9, amp=0.045)
resorte(a2, (2.35, 0.17), (3.0, 0.17), n=7, amp=0.045)
bloque(a2, (0.6, 0.11), 0.2, 0.2, "1", fs=9)
bloque(a2, (0.85, 0.15), 0.3, 0.3, "2", fs=9)
flecha(a2, (1.55, 0.2), (-0.4, 0), C_VEL, r"$v' = -0{,}4$ m/s", dx=0.46, dy=0.0, ha="left")
a2.text(-0.05, 0.42, "después del choque plástico", ha="left", color="0.35")
flecha(a2, (1.3, 0.05), (0.35, 0), "0.3", r"$+x$", dx=0.1, lw=0.9)
fig.subplots_adjust(hspace=0.15)
guardar(fig, OUT, "fig2_p2_resortes")


# --- Figura 3 ---------------------------------------------------------------
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.3, 3.0), width_ratios=[1.15, 1])
ang = 53
u = np.array([np.cos(np.radians(-ang)), np.sin(np.radians(-ang))])   # hacia abajo del plano
nvec = np.array([np.sin(np.radians(ang)), np.cos(np.radians(ang))])   # normal saliente
a1.set_aspect("equal")
a1.axis("off")
top = np.array([0.0, 2.0])
base = top + 2.6 * u
a1.add_patch(Polygon([top, base, (top[0], base[1])], closed=True, fc="0.93", ec=C_SUELO, lw=1.2))
rp = 0.22
cp = top + rp * nvec + 0.05 * u
disco(a1, cp, rp, color="0.88")
a1.text(cp[0] + 0.33, cp[1] - 0.05, r"$m_p = 2m$", ha="left", va="center")
punto(a1, cp, ms=2)
a1.text(cp[0] - 0.28, cp[1] + 0.16, "O", ha="center")
pb = top + 1.55 * u + 0.11 * nvec
bloque(a1, pb, 0.26, 0.22, r"$m$", ang=-ang)
p_cuerda0 = cp - rp * nvec          # la cuerda sale tangente, paralela al plano
a1.plot([p_cuerda0[0], pb[0] - 0.13 * u[0]], [p_cuerda0[1], pb[1] - 0.13 * u[1]], color="0.2", lw=0.9)
arco_angulo(a1, base, 0.35, 180 - ang, 180, r"$53^\circ$", rt=0.55)
flecha(a1, pb + 0.2 * nvec, -0.45 * u, C_VEL, r"$\vec v_0$", dx=-0.05, dy=0.12)
a1.add_patch(Arc(cp, 2 * rp + 0.14, 2 * rp + 0.14, theta1=20, theta2=110, color=C_VEL, lw=1.0))
flecha(a1, cp + (rp + 0.07) * np.array([np.cos(np.radians(22)), np.sin(np.radians(22))]),
       0.03 * np.array([np.sin(np.radians(22)), -np.cos(np.radians(22))]), C_VEL, lw=1.0)
a1.text(cp[0] + 0.38, cp[1] + 0.28, r"$\omega_0$", color=C_VEL)
a1.set_xlim(-0.2, 1.8)
a1.set_ylim(-0.2, 2.45)
# DCL del bloque en ejes del plano
a2.set_aspect("equal")
a2.axis("off")
a2.set_xlim(-1.25, 1.35)
a2.set_ylim(-1.35, 1.2)
bloque(a2, (0, 0), 0.34, 0.28, ang=-ang)
a2.text(-0.32, -0.22, r"$m$", ha="center")
s = 0.9
flecha(a2, (0, 0), (0, -s), C_PESO, r"$\vec w$", dx=0.15)
flecha(a2, (0, 0), 0.6 * s * nvec, C_NORMAL, r"$\vec N$", dx=0.12, dy=0.05)
flecha(a2, (0, 0), -0.7 * s * u, C_TENSION, r"$\vec T$", dx=-0.1, dy=0.12)
flecha(a2, (0, 0), 0.35 * s * u, C_ROCE, r"$\vec f_k$", dx=0.2, dy=-0.02)
ejes(a2, (0.55, -0.95), 0.35, ang=-ang, etiquetas=("$x$", "$y$"))
a2.text(0, 1.05, "DCL del bloque (sube)", ha="center", color="0.35")
guardar(fig, OUT, "fig3_p3_polea_plano")


# --- Figura 4 ---------------------------------------------------------------
fig, ax = lienzo(6.0, 2.9, (-0.2, 3.3), (-0.45, 1.75))
ang = 37
u = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])       # hacia arriba del plano
nvec = np.array([-u[1], u[0]])
o = np.array([0.0, 0.0])
top = o + 2.4 * u
ax.add_patch(Polygon([o, top, (top[0], 0)], closed=True, fc="0.93", ec=C_SUELO, lw=1.2))
suelo(ax, -0.1, 3.2, 0, paso=0.11)
rp = 0.16
cp = top + rp * nvec + 0.12 * u
ax.plot([top[0], cp[0]], [top[1], cp[1]], color="0.3", lw=1.2)
disco(ax, cp, rp, color="0.85")
punto(ax, cp, ms=2)
ax.text(cp[0] - 0.05, cp[1] + 0.3, r"$M,\,R$", ha="center")
pa = o + 1.55 * u + 0.1 * nvec
pbb = o + 0.75 * u + 0.1 * nvec
bloque(ax, pa, 0.22, 0.18, r"$m$", ang=ang)
bloque(ax, pbb, 0.22, 0.18, r"$m$", ang=ang, color="white")
ax.plot([pa[0] + 0.11 * u[0], cp[0] + rp * nvec[0] * 0 - rp * nvec[0]],
        [pa[1] + 0.11 * u[1], cp[1] - rp * nvec[1]], color="0.2", lw=0.9)
xr = cp[0] + rp
ax.plot([xr, xr], [cp[1], 0.95], color="0.2", lw=0.9)
resorte(ax, (xr, 0.95), (xr, 0.0), n=8, amp=0.05)
ax.text(xr + 0.12, 0.5, r"$k$", va="center")
punto(ax, pa - 0.17 * nvec, "A", dx=0.12, dy=-0.06, ms=2.5)
punto(ax, pbb - 0.17 * nvec, "B", dx=0.12, dy=-0.06, ms=2.5)
cota(ax, pbb + 0.5 * nvec, pa + 0.5 * nvec, r"$\Delta x$", off=(-0.12, 0.1))
arco_angulo(ax, o, 0.4, 0, ang, r"$37^\circ$", rt=0.6)
flecha(ax, pbb + 0.24 * nvec + 0.05 * u, -0.4 * u, C_VEL, r"$\vec v_B$", dx=-0.12, dy=0.1)
guardar(fig, OUT, "fig4_p4_polea_resorte")
