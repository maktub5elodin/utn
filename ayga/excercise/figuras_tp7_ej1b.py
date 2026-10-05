r"""Figuras del TP 7, Ej. 1 b): x^2 + 2x + 4y^2 - 8y = 0, x >= 0.

Genera en ./figuras/:
  - PDF vectoriales para el documento final (\includegraphics).
  - PNG solo para la vista previa del .md en VS Code / GitHub.

El texto y las fórmulas se componen con el backend pgf + xelatex, usando las
mismas fuentes que el documento (Latin Modern Roman + Latin Modern Math).
Uso: python3 figuras_tp7_ej1b.py   (o `make` desde esta carpeta)
"""
import logging
from pathlib import Path

import matplotlib

matplotlib.use("pgf")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc
from matplotlib.ticker import FuncFormatter

# --- Datos del ejercicio ----------------------------------------------------
H, K = -1.0, 1.0                  # centro C(-1, 1)
A, B = np.sqrt(5), np.sqrt(5) / 2  # semiejes
T0 = np.arctan(2)                  # = arccos(1/sqrt5) ≈ 1,107 rad

# Comprobaciones: si alguna falla, la figura no se genera
assert np.isclose(T0, np.arccos(1 / np.sqrt(5)))
assert np.allclose((H + A * np.cos(T0), K + B * np.sin(T0)), (0, 2))
assert np.allclose((H + A * np.cos(-T0), K + B * np.sin(-T0)), (0, 0))

logging.getLogger("fontTools").setLevel(logging.ERROR)

# --- Estilo -----------------------------------------------------------------
OUT = Path(__file__).parent / "figuras"
OUT.mkdir(exist_ok=True)

plt.rcParams.update({
    # Mismo motor y fuentes que el documento (ver pdf.yaml)
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

C_ELIPSE = "#1f4e9c"   # elipse / ángulo polar φ
C_ARCO = "#c0392b"     # arco x >= 0
C_AUX = "#d98a00"      # circunferencia auxiliar / ángulo excéntrico θ
C_GRIS = "0.55"

coma = FuncFormatter(lambda v, _: f"{v:g}".replace(".", ",").replace("-", "\u2212"))


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


def elipse(h, k, a, b, t):
    return h + a * np.cos(t), k + b * np.sin(t)


def punto(ax, x, y, texto, dx=0.12, dy=0.12, color="black", ha="left"):
    ax.plot(x, y, "o", color=color, ms=4, zorder=5)
    ax.annotate(texto, (x, y), xytext=(x + dx, y + dy), ha=ha, color=color)


def angulo(ax, centro, r, desde, hasta, color, texto, r_texto):
    """Arco de ángulo (en grados) con su etiqueta en la bisectriz."""
    ax.add_patch(Arc(centro, 2 * r, 2 * r, theta1=desde, theta2=hasta,
                     color=color, lw=1.2))
    m = np.radians((desde + hasta) / 2)
    ax.text(centro[0] + r_texto * np.cos(m), centro[1] + r_texto * np.sin(m),
            texto, color=color, ha="center", va="center")


def guardar(fig, nombre):
    """Guarda el PDF vectorial y su PNG de vista previa."""
    pdf = OUT / nombre
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(pdf.with_suffix(".png"), bbox_inches="tight", dpi=150)
    plt.close(fig)
    print("ok:", pdf, "(+ .png)")


t_full = np.linspace(0, 2 * np.pi, 400)
t_arco = np.linspace(-T0, T0, 200)

# --- Figura 1: el ejercicio -------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 3.6))
ejes(ax, (-3.6, 2.1), (-0.8, 2.6))
ax.plot(*elipse(H, K, A, B, t_full), "--", color=C_GRIS, lw=1, label="elipse completa")
ax.plot(*elipse(H, K, A, B, t_arco), color=C_ARCO, lw=2.4,
        label=r"arco $x \geq 0$:  $\theta \in [-\arctan 2,\ \arctan 2]$")
# flecha de sentido de recorrido (antihorario)
p0, p1 = elipse(H, K, A, B, np.array([0.30, 0.42]))
ax.annotate("", xy=(p0[1], p1[1]), xytext=(p0[0], p1[0]),
            arrowprops=dict(arrowstyle="-|>", color=C_ARCO, lw=1.5, mutation_scale=14))
punto(ax, H, K, "$C(-1,\\,1)$", dy=0.15)
punto(ax, 0, 0, r"$(0,0)$  inicio ($\theta=-\arctan 2$)", dx=0.12, dy=-0.35)
punto(ax, 0, 2, r"$(0,2)$  fin ($\theta=\arctan 2$)", dx=0.12, dy=0.18)
punto(ax, H + A, K, "$(-1+\\sqrt{5},\\,1)$\n$\\theta=0$", dx=0.1, dy=-0.55)
ax.plot([H, H + A], [K, K], ":", color=C_GRIS, lw=1)
ax.plot([H, H], [K, K + B], ":", color=C_GRIS, lw=1)
ax.text(H + A / 2, K - 0.06, "$a=\\sqrt{5}$", ha="center", va="top", color=C_GRIS)
ax.text(H - 0.08, K + B / 2, "$b=\\frac{\\sqrt{5}}{2}$", ha="right", color=C_GRIS)
ax.legend(loc="lower left", fontsize=8, frameon=False)
guardar(fig, "fig1_elipse_arco.pdf")

# --- Figura 2: circunferencia auxiliar, θ vs φ ------------------------------
fig, ax = plt.subplots(figsize=(6, 5.2))
ejes(ax, (-3.6, 3.0), (-1.6, 3.6))
ax.plot(*elipse(H, K, A, A, t_full), color=C_AUX, lw=1.2,
        label=r"circunferencia auxiliar (radio $a=\sqrt{5}$)")
ax.plot(*elipse(H, K, A, B, t_full), color=C_ELIPSE, lw=1.2, label="elipse")
ax.plot(*elipse(H, K, A, B, t_arco), color=C_ARCO, lw=2.4, label=r"arco $x\geq 0$")
for s in (1, -1):
    q = (0, K + A * np.sin(s * T0))   # (0, 3) y (0, -1)
    p = (0, K + B * np.sin(s * T0))   # (0, 2) y (0, 0)
    ax.plot([H, q[0]], [K, q[1]], color=C_AUX, lw=1)
    ax.plot([H, p[0]], [K, p[1]], color=C_ELIPSE, lw=1)
    ax.annotate("", xy=p, xytext=q,
                arrowprops=dict(arrowstyle="-|>", color=C_GRIS, lw=1, ls=":"))
punto(ax, 0, 3, "$Q(0,3)$", color=C_AUX)
punto(ax, 0, -1, "$Q'(0,-1)$", color=C_AUX, dy=-0.3)
punto(ax, 0, 2, "$P(0,2)$", color=C_ELIPSE)
punto(ax, 0, 0, "$P'(0,0)$", color=C_ELIPSE, dy=-0.3)
punto(ax, H, K, "$C$", dx=-0.3, dy=0.1)
angulo(ax, (H, K), 0.75, 0, np.degrees(T0), C_AUX, r"$\theta$", 0.0)
ax.texts[-1].set_position((H + 0.88 * np.cos(np.radians(54)), K + 0.88 * np.sin(np.radians(54))))
angulo(ax, (H, K), 0.40, 0, 45, C_ELIPSE, r"$\varphi$", 0.55)
ax.text(-3.5, 3.35, r"$\tan\varphi = \dfrac{b}{a}\,\tan\theta$", fontsize=11)
ax.text(1.35, 3.3, "$\\theta \\approx 63{,}43^\\circ$\n(parámetro)", color=C_AUX, fontsize=9, va="top")
ax.text(1.35, 2.75, "$\\varphi = 45^\\circ$\n(ángulo polar)", color=C_ELIPSE, fontsize=9, va="top")
ax.text(1.35, 1.95, "compresión\nvertical\n$\\times\\, b/a = 1/2$", fontsize=8,
        color=C_GRIS, va="center")
ax.legend(loc="lower left", fontsize=8, frameon=False)
guardar(fig, "fig2_circunferencia_auxiliar.pdf")

# --- Figura 4: ¿centro desplazado o forma elíptica? -------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 3.1))

# Izquierda: circunferencia de centro C por (0,0) y (0,2) -> θ = φ = 45°
R = np.sqrt(2)
ejes(ax1, (-2.7, 1.0), (-0.9, 2.9))
ax1.plot(*elipse(H, K, R, R, t_full), "--", color=C_GRIS, lw=1)
ax1.plot(*elipse(H, K, R, R, np.linspace(-np.pi / 4, np.pi / 4, 100)),
         color=C_ARCO, lw=2.4)
for s in (1, -1):
    ax1.plot([H, 0], [K, K + s], color=C_ELIPSE, lw=1)
punto(ax1, H, K, "$C$", dx=-0.3, dy=0.1)
punto(ax1, 0, 2, "$(0,2)$")
punto(ax1, 0, 0, "$(0,0)$", dy=-0.3)
angulo(ax1, (H, K), 0.4, 0, 45, C_ELIPSE, "", 0.0)
ax1.annotate(r"$\theta=\varphi=45^\circ$", xy=(H + 0.4 * np.cos(np.radians(22)), K + 0.4 * np.sin(np.radians(22))),
             xytext=(-2.6, 2.55), color=C_ELIPSE,
             arrowprops=dict(arrowstyle="-", color=C_ELIPSE, lw=0.6))
ax1.set_title("Circunferencia ($a=b=\\sqrt{2}$), centro $(-1,1)$\n"
              r"rango: $[-\pi/4,\ \pi/4]$", fontsize=9)

# Derecha: misma elipse trasladada al origen, recta x = 1 -> sigue arctan 2
ejes(ax2, (-2.6, 2.6), (-3.2, 2.6))
ax2.plot(*elipse(0, 0, A, A, t_full), color=C_AUX, lw=1)
ax2.plot(*elipse(0, 0, A, B, t_full), "--", color=C_GRIS, lw=1)
ax2.plot(*elipse(0, 0, A, B, t_arco), color=C_ARCO, lw=2.4)
ax2.axvline(1, color=C_GRIS, lw=0.8, ls=":")
ax2.plot([0, 1], [0, 2], color=C_AUX, lw=1)
ax2.plot([0, 1], [0, 1], color=C_ELIPSE, lw=1)
punto(ax2, 1, 2, "$(1,2)$", color=C_AUX)
punto(ax2, 1, 1, "$(1,1)$", color=C_ELIPSE, dy=-0.05)
ax2.annotate("", xy=(1, 1), xytext=(1, 2),
             arrowprops=dict(arrowstyle="-|>", color=C_GRIS, lw=1, ls=":"))
angulo(ax2, (0, 0), 0.6, 0, np.degrees(T0), C_AUX, r"$\theta$", 0.0)
ax2.texts[-1].set_position((0.72 * np.cos(np.radians(55)), 0.72 * np.sin(np.radians(55))))
angulo(ax2, (0, 0), 0.35, 0, 45, C_ELIPSE, r"$\varphi$", 0.5)
ax2.text(-2.5, -2.6, r"$\theta\approx 63{,}43^\circ$", color=C_AUX, fontsize=9)
ax2.text(-2.5, -3.05, r"$\varphi = 45^\circ$", color=C_ELIPSE, fontsize=9)
ax2.set_title("Misma elipse trasladada al origen, recta $x=1$\n"
              r"rango: $[-\arctan 2,\ \arctan 2]$ (no cambia)", fontsize=9)
fig.tight_layout()
guardar(fig, "fig4_hipotesis.pdf")

# --- Figura 3: φ en función de θ --------------------------------------------
th = np.linspace(-np.pi / 2 + 1e-3, np.pi / 2 - 1e-3, 400)
phi = np.arctan((B / A) * np.tan(th))
assert np.isclose(np.arctan((B / A) * np.tan(T0)), np.pi / 4)

fig, ax = plt.subplots(figsize=(5.2, 4.2))
ax.plot(th, th, "--", color=C_GRIS, lw=1, label=r"$\varphi=\theta$ (circunferencia)")
ax.plot(th, phi, color=C_ELIPSE, lw=1.8,
        label=r"$\varphi=\arctan\left(\frac{1}{2}\tan\theta\right)$ (esta elipse)")
for s in (1, -1):
    ax.plot([s * T0, s * T0], [0, s * np.pi / 4], ":", color=C_AUX, lw=1)
    ax.plot([0, s * T0], [s * np.pi / 4, s * np.pi / 4], ":", color=C_ELIPSE, lw=1)
    ax.plot(s * T0, s * np.pi / 4, "o", color=C_ARCO, ms=5, zorder=5)
ax.annotate(r"$(\arctan 2,\ \pi/4)$" "\n" r"extremo $(0,2)$", (T0, np.pi / 4),
            xytext=(0.95, -0.75), ha="center", color=C_ARCO, fontsize=9,
            arrowprops=dict(arrowstyle="-", color=C_ARCO, lw=0.6))
ticks = [-np.pi / 2, -T0, -np.pi / 4, 0, np.pi / 4, T0, np.pi / 2]
labels = [r"$-\frac{\pi}{2}$", r"$-1{,}107$", r"$-\frac{\pi}{4}$", "$0$",
          r"$\frac{\pi}{4}$", r"$1{,}107$", r"$\frac{\pi}{2}$"]
ax.set_xticks(ticks, labels, fontsize=8)
ax.set_yticks(ticks[::3] + [-np.pi / 4, np.pi / 4],
              labels[::3] + [r"$-\frac{\pi}{4}$", r"$\frac{\pi}{4}$"], fontsize=8)
ax.set_xlim(-np.pi / 2, np.pi / 2)
ax.set_ylim(-np.pi / 2, np.pi / 2)
ax.set_aspect("equal")
ax.axhline(0, color="black", lw=0.8)
ax.axvline(0, color="black", lw=0.8)
ax.grid(True, color="0.9", lw=0.6)
ax.set_xlabel(r"$\theta$ (parámetro, ángulo excéntrico) [rad]")
ax.set_ylabel(r"$\varphi$ (ángulo polar desde $C$) [rad]")
ax.legend(loc="upper left", fontsize=8, frameon=False)
guardar(fig, "fig3_phi_vs_theta.pdf")
