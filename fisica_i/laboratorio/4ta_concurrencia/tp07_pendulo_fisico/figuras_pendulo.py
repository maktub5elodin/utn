# Figuras del TP N°7 (péndulo físico).
#   python3 figuras_pendulo.py  (o: make figuras)  -> figuras/*.png y *.pdf
#
# Los valores salen de las mediciones de la hoja firmada (04/11/2026) con las
# mismas fórmulas del Anexo de Cálculos; al imprimirlos se pueden cotejar con
# el informe.
from math import pi

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, FancyArrowPatch

plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm", "font.size": 13})

MEDIDO, CALCULADO = "#1F5FA8", "#C8691C"      # azul / naranja (validados para daltonismo)
TINTA, GRIS, SUAVE = "#222222", "#8A8A8A", "#E9EEF5"

# ------------------------------------------------------------ datos y cálculos
g = 10.0                                  # m/s², valor adoptado en la hoja firmada
m, dm = 0.500, 0.002                      # lámina [kg]
mc, dmc = 0.183, 0.002                    # cilindro [kg]
d, dd = 0.430, 0.004                      # S → G_L [m]
dp, ddp = 0.795, 0.004                    # S → cilindro en B (d') [m]
r, dr = 0.01275, 0.00005                  # radio del cilindro [m] (D = 25,5 ± 0,1 mm)
T = {"L": 1.501, "A": 1.477, "B": 1.644}  # períodos [s]
dT = 0.03

mA, dmA = m + mc, dm + dmc


def I_periodo(masa, dist, per):
    return masa * g * dist * per**2 / (4 * pi**2)


IL = I_periodo(m, d, T["L"])
dIL = (dm / m + dd / d + 2 * dT / T["L"]) * IL
IA_med = I_periodo(mA, d, T["A"])
dIA_med = (dmA / mA + dd / d + 2 * dT / T["A"]) * IA_med

z = 0.5 * mc * r**2
dz = (dmc / mc + 2 * dr / r) * z
wA, wB = mc * d**2, mc * dp**2
dwA = (dmc / mc + 2 * dd / d) * wA
dwB = (dmc / mc + 2 * ddp / dp) * wB
IA_cal, dIA_cal = IL + z + wA, dIL + dz + dwA
IB_cal, dIB_cal = IL + z + wB, dIL + dz + dwB

# Resultados redondeados (incerteza a 1 cifra significativa) — los del informe
R = {
    "IL": (0.123, 0.007),
    "IA_med": (0.162, 0.009),
    "IA_cal": (0.157, 0.008),
    "IB_cal": (0.238, 0.009),
}


def guardar(fig, nombre):
    for ext in ("png", "pdf"):
        fig.savefig(f"figuras/{nombre}.{ext}", dpi=200, bbox_inches="tight", facecolor="white",
                    metadata={"Software": None} if ext == "png" else {"Creator": None, "Producer": None,
                                                                       "CreationDate": None})
    plt.close(fig)


def cota(ax, a, b, texto, lado=1, color=TINTA, desplaz=0.035):
    """Segmento acotado entre a y b, con el texto al costado."""
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="<|-|>", mutation_scale=11, lw=1.3, color=color,
                                 shrinkA=0, shrinkB=0, zorder=5))
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    vx, vy = b[0] - a[0], b[1] - a[1]
    n = (vx**2 + vy**2) ** 0.5
    ax.text(mx + lado * desplaz * (-vy) / n * 1.6, my + lado * desplaz * vx / n * 1.6, texto,
            ha="center", va="center", fontsize=14, color=color, zorder=6,
            bbox=dict(fc="white", ec="none", pad=0.5))


# ------------------------------------------------------------ figura 1
def fig_cuerpos():
    S = (0.0, 0.0)
    GL = (0.07, -0.424)                    # |S G_L| = 0,43 m
    P = (-0.20, -0.769)                    # |S P| = 0,795 m (esquina alejada)
    GB = ((m * GL[0] + mc * P[0]) / mA, (m * GL[1] + mc * P[1]) / mA)
    contorno = [(-0.10, 0.06), (0.10, 0.07), (0.20, -0.10), (0.33, -0.42), (0.36, -0.62),
                (0.22, -0.80), (-0.06, -0.86), (-0.27, -0.83), (-0.30, -0.62), (-0.20, -0.30)]
    agujeros = [(-0.05, -0.16), (0.12, -0.25), (-0.15, -0.45), (0.22, -0.55), (0.02, -0.68),
                (-0.18, -0.66), (0.15, -0.74)]

    fig, axs = plt.subplots(1, 3, figsize=(11.5, 5.4))
    for ax, caso in zip(axs, ("L", "A", "B")):
        ax.set(xlim=(-0.42, 0.48), ylim=(-0.95, 0.15), aspect="equal")
        ax.axis("off")
        ax.add_patch(Polygon(contorno, closed=True, fc=SUAVE, ec=TINTA, lw=1.8, zorder=1))
        for h in agujeros:
            ax.add_patch(Circle(h, 0.018, fc="white", ec=GRIS, lw=1, zorder=2))
        ax.add_patch(Circle(S, 0.022, fc="white", ec=TINTA, lw=2, zorder=7))
        ax.text(S[0] - 0.075, S[1] - 0.01, "$S$", fontsize=15, zorder=7)

        if caso in ("L", "A"):
            cota(ax, S, GL, "$d$", lado=1)
            if caso == "A":
                ax.add_patch(Circle(GL, 0.045, fc=GRIS, ec=TINTA, lw=1.5, zorder=4))
            ax.plot(*GL, "o", ms=6, color=TINTA, zorder=6)
            ax.text(GL[0] + 0.06, GL[1] - 0.04, "$G_L$", fontsize=15)
        else:
            cota(ax, S, P, "$d'$", lado=1)
            ax.add_patch(Circle(P, 0.045, fc=GRIS, ec=TINTA, lw=1.5, zorder=4))
            ax.plot(*GL, "o", ms=6, color=TINTA, zorder=6)
            ax.text(GL[0] + 0.05, GL[1] + 0.02, "$G_L$", fontsize=15)
            ax.plot(*GB, "o", ms=7, mfc="white", mec=TINTA, mew=1.6, zorder=6)
            ax.plot([GL[0], P[0]], [GL[1], P[1]], ls=(0, (2, 2)), color=TINTA, lw=1, zorder=3)
            ax.text(GB[0] + 0.05, GB[1] - 0.03, "$G_B$", fontsize=15)

        titulos = {"L": "Cuerpo L: lámina sola",
                   "A": "Cuerpo A: cilindro en $G_L$",
                   "B": "Cuerpo B: cilindro alejado"}
        ax.set_title(titulos[caso], fontsize=14, pad=6)
    guardar(fig, "fig1_cuerpos")


# ------------------------------------------------------------ figuras 2 y 3
def intervalo(ax, y, centro, error, color, etiqueta, extremos=True):
    a, b = centro - error, centro + error
    ax.plot([a, b], [y, y], color=color, lw=2.4, solid_capstyle="butt", zorder=4)
    for x in (a, b):
        ax.plot([x, x], [y - 0.13, y + 0.13], color=color, lw=2, zorder=4)
    ax.plot(centro, y, "o", ms=8, color=color, mec="white", mew=1.5, zorder=5)
    ax.text(b + 0.0015, y, f"  {etiqueta}", va="center", fontsize=12.5, color=TINTA)
    if not extremos:
        coma = lambda v: f"{v:.3f}".replace(".", ",")
        ax.text(centro, y - 0.24, f"({coma(centro)} ± {coma(error)})", ha="center", va="top",
                fontsize=10.5, color=TINTA)
        return
    ax.text(a, y - 0.24, f"{a:.3f}".replace(".", ","), ha="center", va="top", fontsize=10.5, color=TINTA)
    ax.text(b, y - 0.24, f"{b:.3f}".replace(".", ","), ha="center", va="top", fontsize=10.5, color=TINTA)


def ejes_I(ax, xmin, xmax):
    ax.set_xlim(xmin, xmax)
    ax.set_yticks([])
    for lado in ("left", "right", "top"):
        ax.spines[lado].set_visible(False)
    ax.spines["bottom"].set_color(GRIS)
    ax.tick_params(axis="x", colors=TINTA, labelsize=11)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:.2f}".replace(".", ",")))
    ax.set_xlabel(r"$I$ respecto del eje por $S$  (kg$\cdot$m$^2$)", fontsize=12.5)
    ax.grid(axis="x", color="#DDDDDD", lw=0.8, zorder=0)


def fig_intervalos_A():
    (cm_, em), (cc, ec) = R["IA_med"], R["IA_cal"]
    lo, hi = max(cm_ - em, cc - ec), min(cm_ + em, cc + ec)
    fig, ax = plt.subplots(figsize=(9, 3.2))
    ax.axvspan(lo, hi, color="#DCDCDC", zorder=1)
    ax.text((lo + hi) / 2, 2.62, "superposición", ha="center", fontsize=11.5, color=TINTA)
    intervalo(ax, 2.0, cm_, em, MEDIDO, r"$I_A$ medido (período)")
    intervalo(ax, 1.0, cc, ec, CALCULADO, r"$I_A$ calculado (Steiner + aditividad)")
    ax.set_ylim(0.4, 2.85)
    ejes_I(ax, 0.140, 0.205)
    guardar(fig, "fig2_intervalos_A")


def fig_momentos():
    fig, ax = plt.subplots(figsize=(9, 3.9))
    filas = [
        (3.0, "IL", MEDIDO, r"$I_L$ medido: lámina sola"),
        (2.0, "IA_med", MEDIDO, r"$I_A$ medido: cilindro en $G_L$"),
        (1.0, "IB_cal", CALCULADO, r"$I_B$ calculado: cilindro alejado"),
    ]
    for y, k, color, et in filas:
        intervalo(ax, y, *R[k], color, et, extremos=False)
    ax.set_ylim(0.4, 3.5)
    ejes_I(ax, 0.10, 0.34)
    guardar(fig, "fig3_momentos")


if __name__ == "__main__":
    print(f"I_L    = {IL:.5f} ± {dIL:.5f}")
    print(f"I_A med= {IA_med:.5f} ± {dIA_med:.5f}")
    print(f"z      = {z:.4e} ± {dz:.1e};  w_A = {wA:.5f} ± {dwA:.5f};  w_B = {wB:.5f} ± {dwB:.5f}")
    print(f"I_A cal= {IA_cal:.5f} ± {dIA_cal:.5f}")
    print(f"I_B cal= {IB_cal:.5f} ± {dIB_cal:.5f}")
    fig_cuerpos()
    fig_intervalos_A()
    fig_momentos()
