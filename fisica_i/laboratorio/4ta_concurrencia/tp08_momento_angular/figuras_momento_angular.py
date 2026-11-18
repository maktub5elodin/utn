# Figuras de la monografía del TP N°8 (conservación del momento angular).
#   python3 figuras_momento_angular.py  (o: make figuras)  -> figuras/*.png y *.pdf
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch, Rectangle, Circle, Arc

plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm", "font.size": 13})

AZUL, ROJO, VERDE, GRIS, TINTA = "#1F5FA8", "#B03A2E", "#2E7D32", "#8A8A8A", "#222222"


def flecha(ax, a, b, color=TINTA, lw=2.4, estilo="-|>", ms=16):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=estilo, mutation_scale=ms, lw=lw, color=color,
                                 shrinkA=0, shrinkB=0, zorder=6))


def guardar(fig, nombre):
    for ext in ("png", "pdf"):
        fig.savefig(f"figuras/{nombre}.{ext}", dpi=200, bbox_inches="tight", facecolor="white",
                    metadata={"Software": None} if ext == "png" else {"Creator": None, "Producer": None,
                                                                       "CreationDate": None})
    plt.close(fig)


def banquito(ax):
    ax.add_patch(Rectangle((-0.45, 0.0), 0.9, 0.12, color=GRIS, zorder=1))
    ax.plot([0, 0], [-0.35, 0.0], color=GRIS, lw=5, zorder=1)
    ax.add_patch(Rectangle((-0.35, -0.42), 0.7, 0.08, color=GRIS, zorder=1))


def cuerpo(ax, brazos):
    """Persona de frente, parada sobre el banquito. brazos: lista de (hombro→codo→mano)."""
    k = dict(color=TINTA, lw=3, solid_capstyle="round", zorder=3)
    ax.plot([-0.15, 0, 0.15], [0.12, 0.95, 0.12], **k)       # piernas
    ax.plot([0, 0], [0.95, 1.75], **k)                        # torso
    ax.add_patch(Circle((0, 1.95), 0.17, fill=False, ec=TINTA, lw=3, zorder=3))
    for tramo in brazos:
        xs, ys = zip(*tramo)
        ax.plot(xs, ys, **k)


def eje(ax, ytop):
    ax.plot([0, 0], [-0.5, ytop], ls=(0, (6, 4)), color=AZUL, lw=1.3, zorder=0)


def giro(ax, y, ancho, color=AZUL, lw=2.4):
    """Flecha curva de giro alrededor del eje vertical (vista en perspectiva)."""
    t = np.linspace(200, 520, 60)
    x, yy = ancho * np.cos(np.radians(t)), y + 0.12 * np.sin(np.radians(t))
    ax.plot(x[:-3], yy[:-3], color=color, lw=lw, zorder=5)
    flecha(ax, (x[-4], yy[-4]), (x[-1], yy[-1]), color=color, lw=lw)


# ---------------------------------------------------------------- figura 1
def fig_pesas():
    fig, axs = plt.subplots(1, 3, figsize=(11, 4.6))
    casos = [
        ("(a) pesas junto al pecho",
         [[(0, 1.65), (-0.28, 1.35), (-0.12, 1.5)], [(0, 1.65), (0.28, 1.35), (0.12, 1.5)]],
         [(-0.12, 1.5), (0.12, 1.5)], 0.35, r"$I$ chico, $\omega$ grande", 3),
        ("(b) brazos horizontales",
         [[(0, 1.65), (-1.1, 1.65)], [(0, 1.65), (1.1, 1.65)]],
         [(-1.1, 1.65), (1.1, 1.65)], 0.9, r"$I$ grande, $\omega$ chica", 1),
        ("(c) brazos verticales",
         [[(0, 1.65), (-0.27, 1.9), (-0.2, 2.75)], [(0, 1.65), (0.27, 1.9), (0.2, 2.75)]],
         [(-0.2, 2.75), (0.2, 2.75)], 0.3, r"$I$ mínimo, $\omega$ máxima", 3),
    ]
    for ax, (tit, brazos, pesas, r, leyenda, nflechas) in zip(axs, casos):
        ax.set(xlim=(-1.4, 1.4), ylim=(-0.75, 3.25), aspect="equal")
        ax.axis("off")
        eje(ax, 3.15)
        banquito(ax)
        cuerpo(ax, brazos)
        for p in pesas:
            ax.add_patch(Circle(p, 0.09, color=ROJO, zorder=4))
        giro(ax, 3.0, r, lw=1.6 + 0.6 * nflechas)
        ax.text(0, -0.68, leyenda, ha="center", va="top", fontsize=13)
        ax.set_title(tit, fontsize=13, pad=4)
    # distancia r al eje en (b)
    axs[1].annotate("", (0, 1.45), (1.1, 1.45),
                    arrowprops=dict(arrowstyle="<->", color=ROJO, lw=1.3))
    axs[1].text(0.55, 1.38, r"$r$", color=ROJO, ha="center", va="top")
    guardar(fig, "fig1_pesas")


# ---------------------------------------------------------------- figura 2
def rueda(ax, centro, theta_deg):
    """Rueda vista de frente, con el eje en el plano del dibujo, inclinado theta respecto de la
    horizontal y tomado por sus dos extremos. La rueda queda de canto (elipse angosta)."""
    th = np.radians(theta_deg)
    u = np.array([np.cos(th), np.sin(th)])            # dirección del eje (y de L_rueda)
    c = np.array(centro)
    ax.add_patch(Ellipse(c, 0.2, 1.0, angle=theta_deg, fc="white", ec=TINTA, lw=3, zorder=4))
    izq, der = c - 0.62 * u, c + 0.62 * u
    ax.plot(*zip(izq, der), color=TINTA, lw=3.5, solid_capstyle="round", zorder=5)
    for mano in (izq, der):                            # una mano en cada extremo del eje
        ax.add_patch(Circle(mano, 0.07, color=TINTA, zorder=6))
    return c, u, izq, der


def fig_rueda():
    fig, axs = plt.subplots(1, 2, figsize=(10.5, 5.4))
    L = 1.15
    for ax, theta, tit in zip(axs, (0, 35), ("(a) eje de la rueda horizontal",
                                              r"(b) eje inclinado un ángulo $\theta$")):
        ax.set(xlim=(-1.6, 1.9), ylim=(-0.75, 3.3), aspect="equal")
        ax.axis("off")
        eje(ax, 3.2)
        banquito(ax)
        c, u, izq, der = rueda(ax, (0, 1.25), theta)
        brazos = []
        for lado, mano in ((-1, izq), (1, der)):
            hombro = np.array([0.22 * lado, 1.6])
            codo = (hombro + mano) / 2 + np.array([0.15 * lado, -0.12])
            brazos.append([(0, 1.65), tuple(hombro), tuple(codo), tuple(mano)])
        cuerpo(ax, brazos)
        tip = c + L * u
        flecha(ax, tuple(der), tuple(tip), color=ROJO, lw=2.6)
        ax.text(*(tip + np.array([0.06, 0.1])), r"$\vec L_{\mathrm{rueda}}$", color=ROJO,
                ha="left", va="bottom")
        if theta == 0:
            ax.text(0, -0.68, r"$L_z = 0$: la persona no gira", ha="center", va="top")
        else:
            th = np.radians(theta)
            ax.plot([tip[0], tip[0]], [c[1], tip[1]], ls=":", color=ROJO, lw=1.3)
            ax.plot([der[0], tip[0]], [c[1], c[1]], ls=":", color=GRIS, lw=1.0)
            ax.add_patch(Arc(c, 1.5, 1.5, theta1=0, theta2=theta, color=TINTA, lw=1.2))
            ax.text(c[0] + 0.82, c[1] + 0.2, r"$\theta$", fontsize=13)
            ax.text(tip[0] + 0.08, (c[1] + tip[1]) / 2, r"$L_{\mathrm{rueda}}\,\mathrm{sen}\,\theta$",
                    color=ROJO, fontsize=12, va="center")
            # momento angular de persona + banquito: vertical, hacia abajo
            flecha(ax, (-0.95, 2.75), (-0.95, 2.75 - L * np.sin(th)), color=AZUL, lw=2.6)
            ax.text(-1.02, 2.75 - 0.5 * L * np.sin(th), r"$\vec L_{\mathrm{persona}}$", color=AZUL,
                    ha="right", va="center")
            giro(ax, 3.0, 0.35)
            ax.text(0.15, -0.68, r"$L_{\mathrm{persona}} = -L_{\mathrm{rueda}}\,\mathrm{sen}\,\theta$",
                    ha="center", va="top")
        ax.set_title(tit, fontsize=13, pad=4)
    guardar(fig, "fig2_rueda")


if __name__ == "__main__":
    fig_pesas()
    fig_rueda()
