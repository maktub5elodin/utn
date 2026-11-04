# Figuras de la explicación de movimiento circular uniforme de hoja_formulas.md.
#   python3 figuras_mcu.py  (o: make figuras)  -> figuras/mcu_*.png
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, FancyArrowPatch

plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm", "font.size": 13})

AZUL, ROJO, VERDE, GRIS, TINTA = "#1F5FA8", "#B03A2E", "#2E7D32", "#8A8A8A", "#222222"


def lienzo(ancho, alto, xlim, ylim):
    fig, ax = plt.subplots(figsize=(ancho, alto))
    ax.set(xlim=xlim, ylim=ylim, aspect="equal")
    ax.axis("off")
    return fig, ax


def flecha(ax, a, b, color=TINTA, lw=2.2):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=16, lw=lw, color=color,
                                 shrinkA=0, shrinkB=0, zorder=4))


def punto(ax, p, color=TINTA):
    ax.plot(*p, "o", color=color, ms=6, zorder=5)


def polar(r, grados):
    t = np.radians(grados)
    return np.array([r * np.cos(t), r * np.sin(t)])


def guardar(fig, nombre):
    fig.savefig(f"figuras/{nombre}.png", dpi=200, bbox_inches="tight", facecolor="white",
                metadata={"Software": None})
    plt.close(fig)


def arco():
    fig, ax = lienzo(5, 3.7, (-0.3, 3.5), (-0.4, 2.8))
    R, th = 3, 50
    ax.add_patch(Arc((0, 0), 2 * R, 2 * R, theta1=-8, theta2=62, color=GRIS, lw=1.2, ls="--"))
    ax.add_patch(Arc((0, 0), 2 * R, 2 * R, theta1=0, theta2=th, color=VERDE, lw=3.5))
    ax.add_patch(Arc((0, 0), 1.3, 1.3, theta1=0, theta2=th, color=ROJO, lw=1.6))
    p1, p2 = polar(R, 0), polar(R, th)
    ax.plot([0, p1[0]], [0, p1[1]], color=TINTA, lw=1.8)
    ax.plot([0, p2[0]], [0, p2[1]], color=TINTA, lw=1.8)
    for p in ((0, 0), p1, p2):
        punto(ax, p)
    ax.text(*polar(0.95, th / 2), r"$\theta$", color=ROJO, fontsize=17, ha="center", va="center")
    ax.text(1.5, -0.26, r"$R$", ha="center")
    ax.text(*(polar(1.5, th) + (-0.2, 0.14)), r"$R$", ha="center")
    ax.text(*polar(3.3, th / 2), r"$s = R\,\theta$", color=VERDE, fontsize=15, va="center")
    ax.text(-0.12, -0.14, r"$O$", ha="right", va="top")
    ax.text(p1[0] + 0.08, -0.2, r"$P_1$")
    ax.text(p2[0] - 0.02, p2[1] + 0.12, r"$P_2$")
    guardar(fig, "mcu_arco")


def disco():
    fig, ax = lienzo(5.2, 3.7, (-3.2, 4.3), (-3.2, 3.2))
    ax.add_patch(plt.Circle((0, 0), 3, fc="#EEF3F9", ec=GRIS, lw=1.5))
    ra, rb, w = 1.3, 3, 0.75
    ax.plot([0, rb], [0, 0], color=TINTA, lw=1.8)
    punto(ax, (0, 0))
    punto(ax, (ra, 0), AZUL)
    punto(ax, (rb, 0), AZUL)
    flecha(ax, (ra, 0), (ra, w * ra), AZUL)
    flecha(ax, (rb, 0), (rb, w * rb), AZUL)
    ax.text(ra - 0.1, w * ra + 0.08, r"$v_A = \omega R_A$", color=AZUL, ha="center", va="bottom")
    ax.text(rb + 0.14, w * rb, r"$v_B = \omega R_B$", color=AZUL, va="center")
    ax.text(-0.15, 0.1, r"$O$", ha="right")
    ax.text(ra, -0.15, r"$A$", ha="center", va="top")
    ax.text(rb - 0.1, -0.15, r"$B$", ha="right", va="top")
    ax.annotate("", (ra, -0.85), (0, -0.85), arrowprops=dict(arrowstyle="<->", color=GRIS))
    ax.text(ra / 2, -1.0, r"$R_A$", ha="center", va="top")
    ax.annotate("", (rb, -1.6), (0, -1.6), arrowprops=dict(arrowstyle="<->", color=GRIS))
    ax.text(rb / 2, -1.75, r"$R_B$", ha="center", va="top")
    guardar(fig, "mcu_disco")


def aceleracion():
    fig, ax = lienzo(4.8, 4.8, (-3.9, 3.9), (-3.9, 3.9))
    R = 2.5
    ax.add_patch(plt.Circle((0, 0), R, fc="none", ec=GRIS, lw=1.5))
    punto(ax, (0, 0))
    ax.text(0.14, 0.14, r"$O$")
    for g in (0, 90, 180, 270):
        p, t, r = polar(R, g), polar(1, g + 90), polar(1, g)
        punto(ax, p)
        flecha(ax, p, p + 1.15 * t, AZUL)
        flecha(ax, p, p - 1.1 * r, ROJO)
        ax.text(*(p + 1.15 * t + 0.28 * t + 0.16 * r), r"$\vec v$", color=AZUL, fontsize=16, ha="center", va="center")
        ax.text(*(p - 1.1 * r - 0.28 * r + 0.2 * t), r"$\vec a$", color=ROJO, fontsize=16, ha="center", va="center")
    guardar(fig, "mcu_aceleracion")


def triangulos():
    fig, (izq, der) = plt.subplots(1, 2, figsize=(9.5, 4.3))
    th1, th2 = 55, 125
    R, v = 3, 3

    izq.set(xlim=(-4.3, 4.3), ylim=(-0.75, 4.3), aspect="equal", title="Posiciones")
    izq.axis("off")
    p1, p2 = polar(R, th1), polar(R, th2)
    izq.add_patch(Arc((0, 0), 2 * R, 2 * R, theta1=25, theta2=155, color=GRIS, lw=1.3, ls="--"))
    izq.plot([0, p1[0]], [0, p1[1]], color=TINTA, lw=1.8)
    izq.plot([0, p2[0]], [0, p2[1]], color=TINTA, lw=1.8)
    izq.plot([p1[0], p2[0]], [p1[1], p2[1]], color=VERDE, lw=3)
    izq.add_patch(Arc((0, 0), 1.5, 1.5, theta1=th1, theta2=th2, color=ROJO, lw=1.6))
    izq.text(0, 1.03, r"$\Delta\theta$", color=ROJO, fontsize=15, ha="center")
    izq.text(0, p1[1] - 0.42, r"$\Delta s$", color=VERDE, fontsize=15, ha="center")
    izq.text(*(polar(1.5, th1) + (0.28, -0.1)), r"$R$")
    izq.text(*(polar(1.5, th2) + (-0.5, -0.1)), r"$R$")
    izq.text(0, -0.28, r"$O$", ha="center", va="top")
    for p, g, n, etiqueta, rotulo in ((p1, th1, "1", (0, 0.13), (0.2, -0.3)), (p2, th2, "2", (-0.3, -0.05), (-0.15, 0.2))):
        punto(izq, p)
        q = p + 1.2 * polar(1, g + 90)
        flecha(izq, p, q, AZUL)
        izq.text(q[0] + etiqueta[0], q[1] + etiqueta[1], rf"$\vec v_{n}$", color=AZUL, fontsize=15, ha="center")
        izq.text(p[0] + rotulo[0], p[1] + rotulo[1], rf"$P_{n}$", ha="left" if n == "1" else "right")
    punto(izq, (0, 0))

    der.set(xlim=(-5.4, 3.2), ylim=(-2.525, 2.525), aspect="equal", title="Velocidades")
    der.axis("off")
    v1, v2 = polar(v, th1 + 90), polar(v, th2 + 90)
    flecha(der, (0, 0), v1, AZUL)
    flecha(der, (0, 0), v2, AZUL)
    flecha(der, v1, v2, ROJO, lw=2.8)
    der.add_patch(Arc((0, 0), 1.7, 1.7, theta1=th1 + 90, theta2=th2 + 90, color=ROJO, lw=1.6))
    der.text(-1.4, 0, r"$\Delta\theta$", color=ROJO, fontsize=15, ha="center", va="center")
    der.text(v1[0] + 0.05, v1[1] + 0.14, r"$\vec v_1$", color=AZUL, fontsize=15, ha="center")
    der.text(v2[0] + 0.05, v2[1] - 0.14, r"$\vec v_2$", color=AZUL, fontsize=15, ha="center", va="top")
    der.text(v1[0] - 0.15, 0, r"$\Delta\vec v$", color=ROJO, fontsize=16, ha="right", va="center")
    der.text(*(v1 / 2 + (0.2, 0.12)), r"$v$", fontsize=14)
    der.text(*(v2 / 2 + (0.2, -0.3)), r"$v$", fontsize=14)
    punto(der, (0, 0))
    guardar(fig, "mcu_triangulos")


arco()
disco()
aceleracion()
triangulos()
