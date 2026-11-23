r"""Estilo y primitivas de dibujo comunes a las figuras de fisica_i/2do_parcial/.

Lo importan los scripts de cada documento (parcial_2002/, examen_tipo/,
guia_extra/, parciales_vella/). Mismo motor y fuentes que el PDF (pgf + xelatex, Latin Modern),
igual que fisica_i/1er_parcial/figuras_correcciones.py.

Colores fijos por tipo de magnitud, iguales en todos los documentos:
peso azul, normal verde, rozamiento rojo, tensión naranja, fuerza aplicada
negra, velocidad violeta, empuje celeste.
"""
import logging
from pathlib import Path

import matplotlib

matplotlib.use("pgf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle, Polygon, Rectangle  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

logging.getLogger("fontTools").setLevel(logging.ERROR)

plt.rcParams.update({
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
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

C_PESO = "#1f4e9c"
C_NORMAL = "#27ae60"
C_ROCE = "#c0392b"
C_TENSION = "#d98a00"
C_FUERZA = "black"
C_VEL = "#8e44ad"
C_EMPUJE = "#2e86c1"
C_CUERPO = "0.82"
C_LIQUIDO = "#d6eaf8"
C_SUELO = "0.35"

coma = FuncFormatter(lambda v, _: f"{v:g}".replace(".", ",").replace("-", "−"))


def salida(script):
    """Carpeta figuras/ junto al script que llama."""
    out = Path(script).parent / "figuras"
    out.mkdir(exist_ok=True)
    return out


def guardar(fig, out, nombre):
    """PDF vectorial para el documento y PNG para la vista previa del .md."""
    pdf = out / f"{nombre}.pdf"
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(pdf.with_suffix(".png"), bbox_inches="tight", dpi=150,
                metadata={"Software": None})
    plt.close(fig)
    print("ok:", pdf, "(+ .png)")


def lienzo(ancho, alto, xlim, ylim):
    """Figura sin ejes, escala 1:1."""
    fig, ax = plt.subplots(figsize=(ancho, alto))
    ax.set_aspect("equal")
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    return fig, ax


def flecha(ax, p, v, color, texto=None, dx=0.0, dy=0.0, lw=1.6, ha="center", va="center", z=6):
    """Vector v aplicado en p; el rótulo se ubica en la punta + (dx, dy)."""
    p = np.asarray(p, float)
    v = np.asarray(v, float)
    ax.annotate("", xy=p + v, xytext=p, zorder=z,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, shrinkA=0, shrinkB=0,
                                mutation_scale=11))
    if texto:
        q = p + v
        ax.text(q[0] + dx, q[1] + dy, texto, color=color, ha=ha, va=va, zorder=z)


def cota(ax, p0, p1, texto, off=(0, 0), color="0.25", ha="center", va="center"):
    """Cota con flechas en ambos extremos y rótulo en el medio + off."""
    p0 = np.asarray(p0, float)
    p1 = np.asarray(p1, float)
    ax.annotate("", xy=p1, xytext=p0,
                arrowprops=dict(arrowstyle="<|-|>", color=color, lw=0.8, shrinkA=0, shrinkB=0,
                                mutation_scale=7))
    m = (p0 + p1) / 2
    ax.text(m[0] + off[0], m[1] + off[1], texto, color=color, ha=ha, va=va,
            bbox=dict(fc="white", ec="none", pad=0.5))


def suelo(ax, x0, x1, y=0.0, rayado=True, paso=None, color=C_SUELO):
    """Línea de suelo con rayado inferior."""
    ax.plot([x0, x1], [y, y], color=color, lw=1.4, zorder=2)
    if rayado:
        paso = paso or (x1 - x0) / 30
        h = paso * 0.9
        for x in np.arange(x0 + paso / 2, x1, paso):
            ax.plot([x, x - h], [y, y - h], color=color, lw=0.6, zorder=2)


def pared(ax, x, y0, y1, lado=-1, paso=None, color=C_SUELO):
    """Pared vertical en x con rayado hacia el lado indicado (-1 izquierda)."""
    ax.plot([x, x], [y0, y1], color=color, lw=1.4, zorder=2)
    paso = paso or (y1 - y0) / 8
    for y in np.arange(y0 + paso / 2, y1, paso):
        ax.plot([x, x + lado * paso * 0.9], [y, y - paso * 0.9], color=color, lw=0.6, zorder=2)


def rayado_segmento(ax, p0, p1, n=12, largo=0.08, lado=-1, color=C_ROCE, lw=0.9):
    """Marcas cortas a lo largo de un segmento (tramo con rozamiento)."""
    p0 = np.asarray(p0, float)
    p1 = np.asarray(p1, float)
    t = (p1 - p0) / np.linalg.norm(p1 - p0)
    nrm = np.array([-t[1], t[0]]) * lado
    for s in np.linspace(0.03, 0.97, n):
        q = p0 + s * (p1 - p0)
        ax.plot([q[0], q[0] + largo * (nrm[0] - t[0] * 0.7)],
                [q[1], q[1] + largo * (nrm[1] - t[1] * 0.7)], color=color, lw=lw, zorder=2)


def bloque(ax, c, w, h, texto=None, ang=0.0, color=C_CUERPO, z=4, fs=None):
    """Bloque rectangular centrado en c, girado ang grados."""
    c = np.asarray(c, float)
    a = np.radians(ang)
    rot = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
    esq = np.array([[-w / 2, -h / 2], [w / 2, -h / 2], [w / 2, h / 2], [-w / 2, h / 2]]) @ rot.T + c
    ax.add_patch(Polygon(esq, closed=True, fc=color, ec="black", lw=1.0, zorder=z))
    if texto:
        ax.text(c[0], c[1], texto, ha="center", va="center", zorder=z + 1,
                fontsize=fs or plt.rcParams["font.size"])


def disco(ax, c, r, texto=None, color=C_CUERPO, z=4, ec="black", lw=1.0, ls="-"):
    ax.add_patch(Circle(c, r, fc=color, ec=ec, lw=lw, zorder=z, ls=ls))
    if texto:
        ax.text(c[0], c[1], texto, ha="center", va="center", zorder=z + 1)


def resorte(ax, p0, p1, n=8, amp=0.06, color="0.2", lw=1.0, z=3):
    """Resorte en zigzag entre p0 y p1."""
    p0 = np.asarray(p0, float)
    p1 = np.asarray(p1, float)
    d = p1 - p0
    largo = np.linalg.norm(d)
    t = d / largo
    nrm = np.array([-t[1], t[0]])
    s = np.linspace(0, 1, 2 * n + 3)
    off = np.zeros_like(s)
    off[2:-2:2] = amp
    off[3:-2:2] = -amp
    pts = p0 + np.outer(s * largo, t) + np.outer(off, nrm)
    ax.plot(pts[:, 0], pts[:, 1], color=color, lw=lw, zorder=z)


def punto(ax, p, texto=None, dx=0.0, dy=0.0, color="black", ms=3.5, ha="center", va="center"):
    ax.plot([p[0]], [p[1]], "o", color=color, ms=ms, zorder=7)
    if texto:
        ax.text(p[0] + dx, p[1] + dy, texto, ha=ha, va=va, color=color, zorder=7)


def ejes(ax, o, largo, ang=0.0, color="0.3", etiquetas=("$x$", "$y$"), sep=0.06):
    """Par de ejes x-y con origen en o, girados ang grados."""
    o = np.asarray(o, float)
    a = np.radians(ang)
    ux = np.array([np.cos(a), np.sin(a)])
    uy = np.array([-np.sin(a), np.cos(a)])
    for u, et in zip((ux, uy), etiquetas):
        flecha(ax, o, u * largo, color, lw=0.9)
        q = o + u * (largo + sep * 1.6)
        ax.text(q[0], q[1], et, color=color, ha="center", va="center")


def arco_angulo(ax, c, r, a0, a1, texto=None, rt=None, color="black", lw=0.8):
    """Arco de ángulo (grados) con rótulo a radio rt."""
    from matplotlib.patches import Arc
    ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=a0, theta2=a1, color=color, lw=lw, zorder=3))
    if texto:
        am = np.radians((a0 + a1) / 2)
        rt = rt or r * 1.45
        ax.text(c[0] + rt * np.cos(am), c[1] + rt * np.sin(am), texto, ha="center", va="center",
                color=color)


def ejes_grafico(ax, xlabel, ylabel):
    """Ejes de gráfico x(t) con coma decimal."""
    ax.grid(True, color="0.9", lw=0.6)
    ax.xaxis.set_major_formatter(coma)
    ax.yaxis.set_major_formatter(coma)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


__all__ = [n for n in dir() if not n.startswith("_")]
