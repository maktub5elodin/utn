# Figuras de 03_lanzamiento_de_bala_shot_put.md y 04_lanzamiento_de_jabalina_javelin.md.
#   python3 figuras_casos_limite.py  -> figuras/*.png
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Rectangle

plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm", "font.size": 13})

AZUL, ROJO, VERDE, GRIS, TINTA = "#1F5FA8", "#B03A2E", "#2E7D32", "#8A8A8A", "#222222"


def lienzo(ancho, alto, xlim, ylim):
    fig, ax = plt.subplots(figsize=(ancho, alto))
    ax.set(xlim=xlim, ylim=ylim, aspect="equal")
    ax.axis("off")
    return fig, ax


def cota(ax, a, b, color=TINTA):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="<|-|>", mutation_scale=13, lw=1.4, color=color,
                                 shrinkA=0, shrinkB=0, zorder=4))


def polar(r, grados):
    t = np.radians(grados)
    return np.array([r * np.cos(t), r * np.sin(t)])


def guardar(fig, nombre):
    fig.savefig(f"figuras/{nombre}.png", dpi=200, bbox_inches="tight", facecolor="white",
                metadata={"Software": None})
    plt.close(fig)


def circulo_bala():
    fig, ax = lienzo(9, 4.4, (-1.5, 5.2), (-2.3, 1.75))
    R, medio = 2.135 / 2, 34.92 / 2
    ax.add_patch(Circle((0, 0), R, fc="#EEF3F9", ec=TINTA, lw=2.2, zorder=2))
    ax.add_patch(Arc((0, 0), 2 * R, 2 * R, theta1=-35, theta2=35, color=ROJO, lw=6, zorder=3))
    ax.plot(0, 0, "o", color=TINTA, ms=4, zorder=5)
    for s in (-1, 1):
        ax.plot(*zip((0, 0), polar(4.6, s * medio)), color=VERDE, lw=1.8, zorder=1)
        ax.plot(*zip((0, 0), polar(R, s * medio)), color=VERDE, lw=1.1, ls="--", zorder=3)
    ax.add_patch(Arc((0, 0), 8.4, 8.4, theta1=-medio, theta2=medio, color=VERDE, lw=1.4))
    ax.text(4.3, 0, "$34{,}92^\\circ$", color=VERDE, ha="left", va="center", backgroundcolor="white")
    ax.text(2.75, 0, "sector de caída", color=VERDE, ha="center", va="center")
    cota(ax, (0, -R), (0, R))
    ax.text(-0.1, 0, "diámetro\n2,135 m", ha="right", va="center", fontsize=12, zorder=6)
    ax.annotate("tope («stop board»), 10 cm de alto,\nal frente del círculo", xy=polar(R, -28),
                xytext=(0.9, -1.95), color=ROJO, ha="left", va="center",
                arrowprops=dict(arrowstyle="-|>", color=ROJO, lw=1.3, shrinkB=4))
    guardar(fig, "circulo_bala")


def pista_jabalina():
    fig, ax = lienzo(11, 3.9, (-27, 31), (-9.5, 10))
    R, medio = 8, 28.96 / 2  # el arco de la línea de falta toca los dos bordes de la pista
    x_fin = R * np.cos(np.radians(medio))
    ax.add_patch(Rectangle((-25, -2), 25 + x_fin, 4, fc="#EEF3F9", ec=TINTA, lw=1.8, zorder=2))
    ax.add_patch(Arc((0, 0), 2 * R, 2 * R, theta1=-medio, theta2=medio, color=ROJO, lw=4, zorder=3))
    for s in (-1, 1):
        ax.plot(*zip(polar(R, s * medio), polar(30.5, s * medio)), color=VERDE, lw=1.8, zorder=1)
        ax.plot(*zip((0, 0), polar(R, s * medio)), color=VERDE, lw=1.1, ls="--", zorder=3)
    ax.add_patch(Arc((0, 0), 56, 56, theta1=-medio, theta2=medio, color=VERDE, lw=1.4))
    ax.text(14, 0, "sector de caída", color=VERDE, ha="center", va="center")
    ax.text(24.2, 0, "$\\approx 28{,}96^\\circ$", color=VERDE, ha="center", va="center")
    ax.annotate("ángulo desde los extremos del arco", xy=polar(R, medio), xytext=(-3, 7.6), color=VERDE,
                ha="left", va="center", fontsize=12,
                arrowprops=dict(arrowstyle="-|>", color=VERDE, lw=1.2, shrinkB=2))
    ax.text(-12, 0, "carrera: 6-10 zancadas + 2-3 cruzadas", ha="center", va="center", fontsize=12, zorder=5)
    cota(ax, (-25, 3.2), (x_fin, 3.2))
    ax.text((x_fin - 25) / 2, 4.1, "30 a 36,5 m", ha="center", va="bottom")
    cota(ax, (-26, -2), (-26, 2))
    ax.text(-25, -3.4, "ancho mínimo 4 m", ha="left", va="center", fontsize=12)
    ax.annotate("línea de falta (foul line)", xy=polar(R, -9), xytext=(-5, -6.5), color=ROJO, ha="left",
                va="center", arrowprops=dict(arrowstyle="-|>", color=ROJO, lw=1.3, shrinkB=3))
    guardar(fig, "pista_jabalina")


circulo_bala()
pista_jabalina()
