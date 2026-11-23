r"""Figuras del examen tipo propuesto de Física I (publicado por la FRBA).

Problema 1: resorte, choque plástico y vía circular con rozamiento en la mitad izquierda.
Problema 2: bloque entre dos resortes con un tramo AB con rozamiento.
Problema 3: cilindro que rueda por el plano, cuerda por una polea y bloque colgante.
Problema 4: esfera que rueda por el plano y la superficie horizontal, y cae.

Genera en ./figuras/ el PDF vectorial (documento) y el PNG (vista previa del .md).
Uso: python3 figuras_examen_tipo.py   (o `make` desde esta carpeta)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from figuras_comun import *  # noqa: E402,F403

OUT = salida(__file__)
G = 10.0

# --- Problema 1 -------------------------------------------------------------
M1 = M2 = 4.5
DX1, R1 = 0.75, 0.9
VC_IN, VC_OUT = 10.0, 6.0
VD = np.sqrt(VC_IN ** 2 - 2 * G * 2 * R1)
ND = (M1 + M2) * VD ** 2 / R1 - (M1 + M2) * G
WROZ = 0.5 * (M1 + M2) * (VC_OUT ** 2 - VC_IN ** 2)
V1 = (M1 + M2) * VC_IN / M1
K1 = M1 * V1 ** 2 / DX1 ** 2
assert np.isclose(VD, 8) and np.isclose(ND, 550) and np.isclose(WROZ, -288)
assert np.isclose(V1, 20) and np.isclose(K1, 3200)

# --- Problema 2 -------------------------------------------------------------
M, MU, AB = 1.0, 0.25, 2.0
WR = MU * M * G * AB                    # una pasada por AB
K1_2 = 2 * (2 * WR) / 1 ** 2
K2_2 = 2 * (0.5 * K1_2 - WR) / 1 ** 2
assert np.isclose(WR, 5) and np.isclose(K1_2, 20) and np.isclose(K2_2, 10)

# --- Problema 3 -------------------------------------------------------------
MC, MB, RC, H3 = 2.0, 3.0, 0.5, 1.0
S37 = 0.6
E3 = MB * G * H3 - MC * G * (H3 / 2) * S37
V3 = np.sqrt(E3 / (0.5 * MB + 0.75 * MC * 0.25))
V3_EJE = np.sqrt((MB * G * H3 - MC * G * H3 * S37) / (0.5 * MB + 0.75 * MC))
H3_CLAVE = 4 * (0.5 * MB + 0.75 * MC * 0.25) / (MB * G - MC * G * 0.5 * S37)
A_CM = (MB * G - MC * G * S37 / 2) / (0.75 * MC + 2 * MB) * 1  # Newton: a_cm
assert np.isclose(V3, 3.578, atol=5e-4) and np.isclose(V3_EJE, 2.449, atol=5e-4)
assert np.isclose(H3_CLAVE, 0.3125)
assert np.isclose(2 * (2 * A_CM) * H3, V3 ** 2)          # Newton = energía

# --- Problema 4 -------------------------------------------------------------
AB4, CD4 = 0.7, 2.45
V4 = np.sqrt(G * AB4 * S37 / 0.7)
T4 = np.sqrt(2 * CD4 / G)
X4 = V4 * T4
assert np.isclose(V4 ** 2, 6) and np.isclose(T4, 0.7) and np.isclose(X4, 1.71, atol=5e-3)


# --- Figura 1 ---------------------------------------------------------------
fig, ax = lienzo(6.3, 3.0, (-0.25, 4.4), (-0.35, 2.05))
suelo(ax, 0, 4.3, 0, paso=0.12)
pared(ax, 0, 0, 0.45, lado=-1, paso=0.1)
resorte(ax, (0, 0.12), (0.45, 0.12), n=8, amp=0.06)
bloque(ax, (0.6, 0.15), 0.3, 0.3, "1", fs=9)
bloque(ax, (1.8, 0.15), 0.3, 0.3, "2", fs=9)
punto(ax, (0.6, 0), "A", dy=-0.17, ms=2)
punto(ax, (1.8, 0), "B", dy=-0.17, ms=2)
c = np.array([3.3, R1])
t = np.linspace(0, 2 * np.pi, 300)
ax.plot(c[0] + R1 * np.cos(t), c[1] + R1 * np.sin(t), color=C_SUELO, lw=1.4)
for th in np.linspace(np.pi / 2 + 0.08, 1.5 * np.pi - 0.08, 16):   # mitad izquierda con rozamiento
    p = c + R1 * np.array([np.cos(th), np.sin(th)])
    q = c + (R1 + 0.08) * np.array([np.cos(th + 0.06), np.sin(th + 0.06)])
    ax.plot([p[0], q[0]], [p[1], q[1]], color=C_ROCE, lw=0.9)
punto(ax, (c[0], 0), "C", dy=-0.17)
punto(ax, (c[0], 2 * R1), "D", dy=0.15)
cota(ax, c, c + R1 * np.array([np.cos(np.radians(-30)), np.sin(np.radians(-30))]), r"$R$", off=(0.05, 0.12))
flecha(ax, (2.05, 0.55), (0.4, 0), C_VEL, r"$v_C = 10$ m/s", dx=-0.44, ha="right")
flecha(ax, (c[0] + 0.15, 2 * R1 + 0.1), (-0.45, 0), C_VEL, r"$\vec v_D$", dx=-0.13, dy=0.08)
ax.text(c[0] - R1 - 0.2, R1, r"$\mu$", color=C_ROCE, ha="right", va="center")
guardar(fig, OUT, "fig1_p1_via_circular")

# DCL en D
fig, ax = lienzo(3.0, 2.3, (-1.1, 1.6), (-1.35, 0.85))
t = np.linspace(np.radians(60), np.radians(120), 50)
ax.plot(0.9 * np.cos(t), 0.9 * np.sin(t) - 0.9 + 0.18, color=C_SUELO, lw=1.4)
bloque(ax, (0, 0), 0.32, 0.32)
ax.text(-0.28, 0.0, r"$m$", ha="center", va="center")
flecha(ax, (0.08, 0), (0, -0.6), C_NORMAL, r"$\vec N$", dx=0.2, dy=0.05)
flecha(ax, (-0.08, 0), (0, -0.95), C_PESO, r"$\vec w$", dx=-0.2, dy=0.05)
flecha(ax, (-0.35, 0.33), (-0.45, 0), C_VEL, r"$\vec v_D$", dy=0.13)
ejes(ax, (0.75, -0.6), 0.3, etiquetas=("$x$", "$y$"))
ax.text(0.25, 0.7, "DCL en D (parte superior de la vía)", ha="center", color="0.35")
guardar(fig, OUT, "fig1b_p1_dcl_D")


# --- Figura 2 ---------------------------------------------------------------
fig, ax = lienzo(6.3, 1.5, (-0.2, 6.3), (-0.4, 1.05))
suelo(ax, 0, 6.1, 0, paso=0.14)
pared(ax, 0, 0, 0.75, lado=-1, paso=0.12)
pared(ax, 6.1, 0, 0.75, lado=1, paso=0.12)
resorte(ax, (0, 0.2), (1.1, 0.2), n=9, amp=0.08)
resorte(ax, (4.9, 0.2), (6.1, 0.2), n=9, amp=0.08)
bloque(ax, (1.35, 0.25), 0.5, 0.5, r"$M$")
ax.add_patch(Rectangle((2.3, -0.06), 2.0, 0.06, fc="0.6", ec="none", zorder=3))
punto(ax, (2.3, 0), "A", dy=-0.2, ms=2)
punto(ax, (4.3, 0), "B", dy=-0.2, ms=2)
ax.text(3.3, 0.12, r"$\mu_k = 0{,}25$", color=C_ROCE, ha="center")
ax.text(0.55, 0.55, r"$k_1$", ha="center")
ax.text(5.5, 0.55, r"$k_2$", ha="center")
flecha(ax, (1.25, 0.65), (0.6, 0), C_VEL, r"$\vec v$", dx=0.18)
guardar(fig, OUT, "fig2_p2_resortes_AB")


# --- Figura 3 ---------------------------------------------------------------
fig, ax = lienzo(6.0, 3.6, (-0.3, 4.4), (-0.35, 3.1))
ang = 37
u = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
nv = np.array([-u[1], u[0]])
o = np.array([0.0, 0.0])
top = o + 3.0 * u
ax.add_patch(Polygon([o, top, (top[0], 0)], closed=True, fc="0.93", ec=C_SUELO, lw=1.2))
suelo(ax, -0.2, 4.3, 0, paso=0.13)
rp = 0.09
rc = 0.36
cc = o + 1.4 * u + rc * nv
ptop0 = cc + rc * nv
cp = ptop0 + (top[0] + 0.15 - ptop0[0]) / u[0] * u - rp * nv   # tangente sobre la cuerda
ax.plot([top[0], cp[0]], [top[1], cp[1]], color="0.3", lw=1.2)
disco(ax, cp, rp, color="0.85")
disco(ax, cc, rc)
ax.text(cc[0] - 0.15, cc[1] + 0.12, r"$m$", ha="center", va="center", zorder=6)
punto(ax, cc, ms=2)
ptop = cc + rc * nv
pt_polea = cp + rp * nv
ax.plot([ptop[0], pt_polea[0]], [ptop[1], pt_polea[1]], color="0.2", lw=0.9)
xr = cp[0] + rp
ax.plot([xr, xr], [cp[1], 0.95], color="0.2", lw=0.9)
bloque(ax, (xr, 0.78), 0.32, 0.32, r"$M$")
flecha(ax, (xr + 0.3, 1.1), (0, -0.45), C_VEL, r"$v$", dx=0.13)
flecha(ax, ptop, 0.55 * u, C_VEL, r"$v$", dx=0.02, dy=0.15)
flecha(ax, cc, 0.28 * u, C_VEL, r"$v_{\mathrm{cm}}$", dx=0.12, dy=-0.15)
punto(ax, cc - rc * nv, "P", dx=0.12, dy=-0.1, ms=2.5)
arco_angulo(ax, o, 0.45, 0, ang, r"$37^\circ$", rt=0.7)
cota(ax, (xr + 0.55, 0.62), (xr + 0.55, 0.62 - 0.6), r"$h$", off=(0.12, 0))
guardar(fig, OUT, "fig3_p3_cilindro_polea")


# --- Figura 4 ---------------------------------------------------------------
fig, ax = lienzo(6.3, 3.8, (-0.35, 5.0), (-0.5, 3.55))
yb = CD4
B = np.array([1.1, yb])
A = B + 1.4 * np.array([-0.8, S37])     # plano dibujado fuera de escala
C = np.array([B[0] + 1.0, yb])
ax.plot([A[0], B[0], C[0], C[0]], [A[1], B[1], C[1], 0], color=C_SUELO, lw=1.4)
suelo(ax, C[0], 4.5, 0, paso=0.13)
r = 0.1
disco(ax, A + r * np.array([0.6, 0.8]), r)
tt = np.linspace(0, T4, 60)
ax.plot(C[0] + V4 * tt, yb + r - 0.5 * G * tt ** 2, color=C_VEL, lw=1.0, ls="--")
E = np.array([C[0] + X4, 0])
disco(ax, E + np.array([0, r]), r, color="white")
for p, n_, d in ((A, "A", (-0.15, -0.05)), (B, "B", (0.0, -0.17)), (C, "C", (-0.14, -0.15)),
                 ((C[0], 0), "D", (-0.12, -0.15)), (E, "E", (0, -0.17))):
    punto(ax, p, n_, dx=d[0], dy=d[1], ms=2)
cota(ax, (C[0] - 0.25, 0), (C[0] - 0.25, yb), r"$2{,}45$ m", off=(-0.32, 0))
cota(ax, (C[0], -0.3), (E[0], -0.3), r"$x$", off=(0, -0.12))
cota(ax, (B[0], yb + 0.45), (C[0], yb + 0.45), r"$\overline{BC} = 1$ m", off=(0, 0.13))
arco_angulo(ax, B, 0.45, 180 - 37, 180, r"$37^\circ$", rt=0.68)
ax.plot([B[0] - 0.6, B[0]], [yb, yb], color="0.5", lw=0.6, ls=":")
flecha(ax, C + np.array([0.1, r + 0.12]), (0.45, 0), C_VEL, r"$\vec v_C$", dx=0.18, dy=0.0, ha="left")
guardar(fig, OUT, "fig4_p4_esfera")
