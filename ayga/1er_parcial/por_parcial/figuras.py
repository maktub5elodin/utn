r"""Figuras 3D de los parciales modelo del 1er parcial de AyGA.

Una figura por ejercicio de geometría (y por los subespacios de R^3): planos,
rectas, intersecciones, distancias y haces. Cada figura comprueba con assert
que lo que dibuja cumple el resultado del documento: si algo no cierra, no se
genera.

Genera en ./figuras/ el PDF vectorial (para el documento) y el PNG (vista
previa del .md). La figura de frecuencia de temas la genera temas.py.

Uso: python3 figuras.py            (todas; o `make` desde esta carpeta)
     python3 figuras.py p3_e2      (solo las que contienen ese texto)
"""
import logging
import sys
from pathlib import Path

import matplotlib

matplotlib.use("pgf")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import MaxNLocator

logging.getLogger("fontTools").setLevel(logging.ERROR)
OUT = Path(__file__).resolve().parent / "figuras"
OUT.mkdir(exist_ok=True)

plt.rcParams.update({
    # Mismo motor y fuentes que el documento (ver pipeline_pdf/base.yaml)
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
    "font.size": 9,
})

# Colores: azul y ámbar para los datos, violeta para un tercer objeto,
# verde (el del recuadro de respuesta) para el resultado, rojo para distancias.
AZUL, AMBAR, VIOLETA = "#1f4e9c", "#d98a00", "#7b3fa0"
VERDE, ROJO, GRIS = "#27ae60", "#c0392b", "#444444"

V = lambda *c: np.array(c, dtype=float)


def unit(v):
    return v / np.linalg.norm(v)


# ---------------------------------------------------------------- comprobaciones
def en_plano(P, n, d):
    assert np.isclose(np.dot(n, P) + d, 0), f"{P} no está en el plano {n}·x + {d} = 0"


def en_recta(P, A, u):
    assert np.allclose(np.cross(P - A, u), 0), f"{P} no está en la recta {A} + t{u}"


def paralelos(u, v):
    assert np.allclose(np.cross(u, v), 0), f"{u} y {v} no son paralelos"


def perp(u, v):
    assert np.isclose(np.dot(u, v), 0), f"{u} y {v} no son perpendiculares"


def d_punto_plano(P, n, d):
    return abs(np.dot(n, P) + d) / np.linalg.norm(n)


def pie_en_plano(P, n, d):
    return P - (np.dot(n, P) + d) / np.dot(n, n) * n


def pie_en_recta(P, A, u):
    return A + np.dot(P - A, u) / np.dot(u, u) * u


def vista_auto(planos=(), rectas=(), frente=0.55):
    """Elige (elevación, azimut) como se rota la vista en GeoGebra, pero con un criterio fijo.

    Cada plano tiene que verse oblicuo: |cos| entre la visual y su normal cerca de
    `frente` (0 = de canto, 1 = de frente). Cada recta o distancia tiene que verse
    lo más larga posible: visual perpendicular a su dirección. Se prefiere una
    elevación moderada (~25°), que es la más natural para leer los ejes.
    """
    ns = [unit(V(*n)) for n in planos]
    us = [unit(V(*u)) for u in rectas]
    mejor = None
    for e in range(8, 47, 2):
        for a in range(-180, 180, 3):
            er, ar = np.radians(e), np.radians(a)
            c = V(np.cos(er) * np.cos(ar), np.cos(er) * np.sin(ar), np.sin(er))
            s = 2 * sum((abs(c @ n) - frente) ** 2 for n in ns)
            s += sum((c @ u) ** 2 for u in us)
            s += 0.05 * ((e - 25) / 25) ** 2
            if mejor is None or s < mejor[0]:
                mejor = (s, e, a)
    return mejor[1], mejor[2]


# ---------------------------------------------------------------- dibujo
def ejes(ax, lim, titulo=None, vista=(22, -55)):
    """Caja cúbica con los límites dados ((x0,x1),(y0,y1),(z0,z1))."""
    (x0, x1), (y0, y1), (z0, z1) = lim
    ax.set_xlim(x0, x1); ax.set_ylim(y0, y1); ax.set_zlim(z0, z1)
    ax.set_box_aspect((x1 - x0, y1 - y0, z1 - z0))
    ax.set_xlabel("$x$", labelpad=-6); ax.set_ylabel("$y$", labelpad=-6)
    ax.set_zlabel("$z$", labelpad=-7)
    ax.tick_params(labelsize=6, pad=-2)
    for eje in (ax.xaxis, ax.yaxis, ax.zaxis):     # pocas marcas: que no se encimen al rotar
        eje.set_major_locator(MaxNLocator(nbins=4, integer=True))
    for a in (ax.xaxis, ax.yaxis, ax.zaxis):
        a.pane.set_facecolor((1, 1, 1, 0))
        a.pane.set_edgecolor("#cccccc")
        a._axinfo["grid"]["color"] = "#e6e6e6"
    ax.view_init(*vista)
    if titulo:
        ax.set_title(titulo, fontsize=9, pad=0)


def plano(ax, n, d, c, a=3.0, b=None, color=AZUL, alpha=0.22, e1=None):
    """Rectángulo del plano n·x + d = 0 centrado en c (que tiene que estar en él)."""
    n = V(*n); c = V(*c)
    en_plano(c, n, d)
    if e1 is None:
        aux = V(1, 0, 0) if abs(unit(n)[0]) < 0.9 else V(0, 1, 0)
        e1 = unit(np.cross(n, aux))
    else:
        e1 = unit(V(*e1)); perp(e1, n)
    e2 = unit(np.cross(unit(n), e1))
    b = a if b is None else b
    s, t = np.meshgrid(np.linspace(-a, a, 2), np.linspace(-b, b, 2))
    X, Y, Z = (c[i] + s * e1[i] + t * e2[i] for i in range(3))
    ax.plot_surface(X, Y, Z, color=color, alpha=alpha, linewidth=0, shade=False, zorder=1)
    borde = np.array([c + p * a * e1 + q * b * e2 for p, q in ((-1, -1), (1, -1), (1, 1), (-1, 1), (-1, -1))])
    ax.plot(*borde.T, color=color, lw=0.7, alpha=0.8, zorder=2)


def recta(ax, A, u, t0, t1, color=GRIS, ls="-", lw=1.6):
    A, u = V(*A), V(*u)
    P = np.array([A + t * u for t in (t0, t1)])
    ax.plot(*P.T, color=color, ls=ls, lw=lw, zorder=5)


def segmento(ax, P, Q, color=ROJO, ls="--", lw=1.4):
    ax.plot(*np.array([P, Q]).T, color=color, ls=ls, lw=lw, zorder=6)


def punto(ax, P, texto="", color="black", dx=(0.25, 0.25, 0.25), s=18):
    ax.scatter(*P, color=color, s=s, depthshade=False, zorder=8)
    if texto:
        ax.text(P[0] + dx[0], P[1] + dx[1], P[2] + dx[2], texto, fontsize=8, zorder=9)


def flecha(ax, P, v, color=GRIS, lw=1.2):
    ax.quiver(*P, *v, color=color, lw=lw, arrow_length_ratio=0.18, zorder=7)


def etiqueta(ax, P, texto, color="black"):
    ax.text(*P, texto, fontsize=8, color=color, zorder=9)


def leyenda(fig, items, ncol=3):
    """items: [(texto, color, 'plano'|'recta'|'dist'|'punto')]."""
    h = []
    for texto, color, tipo in items:
        if tipo == "plano":
            h.append(Patch(facecolor=color, alpha=0.35, edgecolor=color, label=texto))
        elif tipo == "punto":
            h.append(Line2D([], [], marker="o", ls="", color=color, label=texto))
        else:
            h.append(Line2D([], [], color=color, ls="--" if tipo == "dist" else "-", lw=1.6, label=texto))
    fig.legend(handles=h, loc="lower center", ncol=ncol, frameon=False, fontsize=8,
               handlelength=1.6, columnspacing=1.2)


def figura(ancho=6.4, alto=4.0, n=1):
    fig = plt.figure(figsize=(ancho, alto))
    axs = [fig.add_subplot(1, n, i + 1, projection="3d", computed_zorder=False) for i in range(n)]
    return fig, axs


FIGURAS = {}


def registrar(f):
    FIGURAS[f.__name__] = f
    return f


# ================================================================ P1 Tema 1
@registrar
def fig_p1t1_e1():
    """Plano por r2 paralelo al eje x; r1 (k = 5) corta a r2."""
    A2, u2 = V(1, -7, 0), V(2, 3, -1)
    n, d = V(0, 1, 3), 7                         # y + 3z + 7 = 0
    I, u1 = V(3, -4, -1), V(4, -7, -3)           # r1 con k = 5
    perp(n, u2); perp(n, V(1, 0, 0)); en_plano(A2, n, d)
    en_recta(I, A2, u2)
    en_plano(I, V(1, 1, -1), 0); en_plano(I, V(3, 0, 4), -5)
    paralelos(u1, np.cross(V(1, 1, -1), V(3, 0, 4)))
    fig, (ax,) = figura()
    plano(ax, n, d, I, a=5, b=3, e1=(1, 0, 0))
    recta(ax, A2, u2, -1.6, 2.6, color=AMBAR)
    recta(ax, I, u1, -0.9, 0.7, color=VIOLETA)
    flecha(ax, V(-1.5, -1, -2), V(2.5, 0, 0), color=AZUL)
    etiqueta(ax, V(-1.2, -1, -1.6), r"$\vec\imath$", AZUL)
    punto(ax, A2, r"$(1,-7,0)$", dx=(0.3, 0, 0.4))
    punto(ax, I, r"$(3,-4,-1)$", color=VERDE, dx=(0.3, 0.2, 0.4))
    ejes(ax, ((-2, 7), (-10, 2), (-4, 3)), vista=vista_auto([n], [u2, u1]))
    leyenda(fig, [(r"plano $y+3z+7=0$", AZUL, "plano"), (r"$r_2$", AMBAR, "recta"),
                  (r"$r_1$ con $k=5$", VIOLETA, "recta")])
    return fig


@registrar
def fig_p1t1_e2():
    """a) Haz: dos planos, su recta y el plano por P. b) Proyección de P en π."""
    P = V(1, 2, -1)
    n1, d1, n2, d2 = V(3, 1, 1), 3, V(1, -2, 1), 1
    nh, dh = V(16, -11, 10), 16
    assert np.allclose(nh, 3 * n1 + 7 * n2) and dh == 3 * d1 + 7 * d2
    en_plano(P, nh, dh)
    ue = np.cross(n1, n2)                         # eje del haz
    E = V(-1, 0, 0); en_plano(E, n1, d1); en_plano(E, n2, d2)
    n, d = V(1, -1, -1), -1                       # π
    Q = V(4 / 3, 5 / 3, -4 / 3)
    assert np.allclose(pie_en_plano(P, n, d), Q)
    en_plano(V(1, -1, 1), n, d)

    fig, (a1, a2) = figura(ancho=6.6, alto=3.6, n=2)
    plano(a1, n1, d1, E, a=2.2, color=AZUL, alpha=0.22)
    plano(a1, n2, d2, E, a=2.2, color=AMBAR, alpha=0.22)
    plano(a1, nh, dh, pie_en_plano(P, nh, dh) * 0.5 + E * 0.5, a=2.2, color=VERDE, alpha=0.3)
    recta(a1, E, ue, -0.6, 0.6, color=GRIS)
    punto(a1, P, r"$P$", color=VERDE)
    ejes(a1, ((-3, 3), (-3, 3), (-3, 3)), r"a) haz y plano por $P$", vista=vista_auto([n1, n2, nh], [ue]))

    plano(a2, n, d, Q, a=1.8, color=VIOLETA)
    recta(a2, Q, n, -1.3, 1.3, color=VERDE)
    segmento(a2, P, Q, color=ROJO)
    punto(a2, P, r"$P$")
    punto(a2, Q, r"$\mathrm{proy}_\pi P$", color=VERDE, dx=(0.25, 0.25, -0.5))
    ejes(a2, ((-1, 3), (-0.5, 3.5), (-3, 1)), r"b) recta ortogonal a $\pi$", vista=vista_auto([n], [n]))
    leyenda(fig, [(r"$3x+y+z+3=0$", AZUL, "plano"), (r"$x-2y+z+1=0$", AMBAR, "plano"),
                  (r"$16x-11y+10z+16=0$", VERDE, "plano"), (r"$\pi: x-y-z-1=0$", VIOLETA, "plano"),
                  (r"recta pedida", VERDE, "recta")], ncol=5)
    return fig


# ================================================================ P2
@registrar
def fig_p2_e1():
    """El plano del haz perpendicular a L: L lo atraviesa en un solo punto."""
    n1, d1, n2, d2 = V(1, 1, -1), 2, V(1, 1, 0), 0
    n, d = V(1, 1, -3), 6
    assert np.allclose(n, 3 * n1 - 2 * n2) and d == 3 * d1 - 2 * d2
    uL = np.cross(V(1, -1, 0), V(1, 2, 1)); paralelos(uL, n)
    P = V(-15, -15, 12) / 11
    en_plano(P, n, d); en_plano(P, V(1, -1, 0), 0); en_plano(P, V(1, 2, 1), 3)
    E = V(-1, 1, 2); en_plano(E, n1, d1); en_plano(E, n2, d2)   # eje del haz
    fig, (ax,) = figura()
    plano(ax, n1, d1, E, a=2.4, color=AZUL, alpha=0.2)
    plano(ax, n2, d2, E, a=2.4, color=AMBAR, alpha=0.2)
    plano(ax, n, d, P, a=2.4, color=VERDE, alpha=0.3)
    recta(ax, E, np.cross(n1, n2), -2.4, 2.4, color=GRIS, lw=1)
    recta(ax, P, V(1, 1, -3), -0.8, 0.8, color=VIOLETA, lw=2)
    punto(ax, P, r"$P$", color=VERDE, dx=(0.3, 0.3, 0.2))
    ejes(ax, ((-4, 2), (-4, 2), (-1, 4)), vista=vista_auto([n1, n2, n], [uL, np.cross(n1, n2)]))
    leyenda(fig, [(r"$x+y-z+2=0$", AZUL, "plano"), (r"$x+y=0$", AMBAR, "plano"),
                  (r"$x+y-3z+6=0$", VERDE, "plano"), (r"$L$", VIOLETA, "recta"),
                  ("eje del haz", GRIS, "recta")], ncol=5)
    return fig


@registrar
def fig_p2_e2():
    """a) L corta a r (a = -1/3) o se cruza con ella (a = 0). b) r paralela a π."""
    A, u = V(2, -2, 0), V(1, 1, -1)
    AL = V(1, 0, 0)
    uL = lambda a: V(3 * a + 1, -3, 1)
    I = V(1, -3, 1); en_recta(I, A, u); en_recta(I, AL, uL(-1 / 3))
    assert not np.isclose(np.dot(np.cross(uL(1), u), V(1, -2, 0)), 0)   # a = 1: alabeadas
    n, d = V(1, 0, 1), -4
    perp(u, n)
    F = pie_en_plano(A, n, d)
    assert np.isclose(np.linalg.norm(A - F), np.sqrt(2))

    fig, (a1, a2) = figura(ancho=6.6, alto=3.6, n=2)
    recta(a1, A, u, -2.5, 1.5, color=AZUL)
    recta(a1, AL, uL(-1 / 3), -1.0, 2.0, color=VERDE)
    recta(a1, AL, uL(1), -0.6, 0.8, color=AMBAR, ls="--")
    punto(a1, I, r"$(1,-3,1)$", color=VERDE, dx=(0.2, 0.2, 0.3))
    ejes(a1, ((-2, 5), (-5, 2.5), (-2, 3)), r"a) concurrentes o alabeadas", vista=vista_auto([], [u, uL(-1 / 3), uL(1)]))

    plano(a2, n, d, F + V(0, 0.5, 0), a=2.6, b=2.6, e1=(0, 1, 0))
    recta(a2, A, u, -2, 2, color=AZUL)
    segmento(a2, A, F)
    punto(a2, A, r"$(2,-2,0)$", dx=(-0.4, 0.2, -0.6))
    etiqueta(a2, (A + F) / 2 + V(0.2, 0, 0.2), r"$\sqrt2$", ROJO)
    ejes(a2, ((-1, 5), (-5, 2), (-2, 4)), r"b) $r \parallel \pi$", vista=vista_auto([n], [u, n]))
    leyenda(fig, [(r"$r$", AZUL, "recta"), (r"$L$ con $a=-\frac13$", VERDE, "recta"),
                  (r"$L$ con $a=1$", AMBAR, "dist"), (r"$\pi: x+z-4=0$", AZUL, "plano"),
                  ("distancia", ROJO, "dist")], ncol=5)
    return fig


# ================================================================ P3
@registrar
def fig_p3_e1():
    """Plano que contiene a r y es perpendicular a L (a = 1)."""
    A, u = V(2, -1, 0), V(1, 1, -1)
    n, d = V(4, -3, 1), -11
    en_plano(A, n, d); perp(u, n)
    uL = np.cross(V(1, 1, -1), V(0, 1, 3)); paralelos(uL, n)
    AL = V(1, 0, 0); en_plano(AL, V(1, 1, -1), -1); en_plano(AL, V(0, 1, 3), 0)
    t = -(np.dot(n, AL) + d) / np.dot(n, uL); X = AL + t * uL
    fig, (ax,) = figura()
    plano(ax, n, d, A, a=3, b=3, e1=u)
    recta(ax, A, u, -2.6, 2.6, color=AMBAR)
    recta(ax, X, uL, -0.5, 0.5, color=VIOLETA, lw=2)
    punto(ax, A, r"$(2,-1,0)$", dx=(0.2, 0.2, 0.3))
    punto(ax, X, "", color=VIOLETA)
    ejes(ax, ((-1, 5), (-4, 3), (-3, 3)), vista=vista_auto([n], [u, uL]))
    leyenda(fig, [(r"$4x-3y+z-11=0$", AZUL, "plano"), (r"$r$ (contenida)", AMBAR, "recta"),
                  (r"$L$ con $a=1$ (perpendicular)", VIOLETA, "recta")])
    return fig


@registrar
def fig_p3_e2():
    """Los puntos a distancia 1 de L forman un cilindro; P recorre una recta que lo corta dos veces."""
    u = unit(V(1, 0, 1))
    P = lambda b: V(1, b, b)
    for b in (1, -1 / 3):
        assert np.isclose(np.linalg.norm(np.cross(P(b), u)), 1)
    fig, (ax,) = figura(alto=4.2)
    e1 = V(0, 1, 0); e2 = np.cross(u, e1)
    th, s = np.meshgrid(np.linspace(0, 2 * np.pi, 40), np.linspace(-1.2, 2.8, 2))
    X, Y, Z = (s * u[i] + np.cos(th) * e1[i] + np.sin(th) * e2[i] for i in range(3))
    ax.plot_surface(X, Y, Z, color=AZUL, alpha=0.2, linewidth=0, shade=False, zorder=1)
    ax.plot_wireframe(X, Y, Z, color=AZUL, alpha=0.25, lw=0.4, rstride=1, cstride=4, zorder=2)
    recta(ax, V(0, 0, 0), V(1, 0, 1), -0.8, 2, color=GRIS)
    recta(ax, V(1, 0, 0), V(0, 1, 1), -1.4, 1.6, color=AMBAR)
    for b, txt in ((1, r"$b=1$"), (-1 / 3, r"$b=-\frac13$")):
        Q = pie_en_recta(P(b), V(0, 0, 0), u)
        segmento(ax, P(b), Q)
        punto(ax, P(b), txt, color=VERDE, dx=(0.15, 0.1, 0.25))
    ejes(ax, ((-1, 2.5), (-1.7, 1.8), (-1, 2.5)), vista=(18, -70))
    leyenda(fig, [(r"$L$", GRIS, "recta"), (r"cilindro: distancia 1 a $L$", AZUL, "plano"),
                  (r"puntos $(1,b,b)$", AMBAR, "recta"), ("distancia 1", ROJO, "dist")], ncol=4)
    return fig


# ================================================================ P4
@registrar
def fig_p4_e1():
    """π y los dos planos paralelos a distancia 1/√11."""
    n = V(-3, 1, 1)
    C = V(1, 2, 3); en_plano(C, n, -2)
    for dd in (-1, -3):
        assert np.isclose(abs(dd - (-2)) / np.linalg.norm(n), 1 / np.sqrt(11))
    fig, (ax,) = figura()
    k = n / np.dot(n, n)                    # paso entre planos: d cambia en 1
    for dd, col, al in ((-1, VERDE, 0.25), (-2, AZUL, 0.3), (-3, VERDE, 0.25)):
        c = C - (dd + 2) * k
        plano(ax, n, dd, c, a=0.9, color=col, alpha=al, e1=(1, 2, 1))
    flecha(ax, C, unit(n) * 0.9, color=GRIS)
    segmento(ax, C, C - (-1 + 2) * k, color=ROJO, ls="-", lw=2)
    segmento(ax, C, C - (-3 + 2) * k, color=ROJO, ls="-", lw=2)
    punto(ax, C, r"$(1,2,3)$", dx=(0.2, 0.2, 0.25))
    ejes(ax, ((0, 2), (1, 3), (2, 4)), vista=vista_auto([n], [n], frente=0.3))
    leyenda(fig, [(r"$\pi: -3x+y+z-2=0$", AZUL, "plano"),
                  (r"$-3x+y+z-1=0$ y $-3x+y+z-3=0$", VERDE, "plano"),
                  (r"distancia $\frac{1}{\sqrt{11}}$", ROJO, "recta")])
    return fig


@registrar
def fig_p4_e2():
    """r y L se cortan en (1,-3,1); distancia de r al origen."""
    A, u = V(2, -2, 0), V(1, 1, -1)
    I = V(1, -3, 1); en_recta(I, A, u)
    uL = V(0, -3, 1); en_plano(I, V(1, -1 / 3, -1), -1); en_plano(I, V(0, 1, 3), 0)
    paralelos(uL, np.cross(V(1, -1 / 3, -1), V(0, 1, 3)))
    O = V(0, 0, 0); F = pie_en_recta(O, A, u)
    assert np.allclose(F, A) and np.isclose(np.linalg.norm(F), 2 * np.sqrt(2))
    fig, (ax,) = figura()
    recta(ax, A, u, -2.5, 1.5, color=AZUL)
    recta(ax, I, uL, -0.8, 1.2, color=AMBAR)
    segmento(ax, O, F)
    punto(ax, O, r"$O$", dx=(-0.3, 0.2, 0.2))
    punto(ax, F, r"$(2,-2,0)$", dx=(0.2, 0.1, 0.3))
    punto(ax, I, r"$(1,-3,1)$", color=VERDE, dx=(0.2, -0.4, 0.3))
    etiqueta(ax, F / 2 + V(0.1, 0.1, 0.25), r"$2\sqrt2$", ROJO)
    ejes(ax, ((-1, 4), (-6, 1), (-2, 3)), vista=vista_auto([], [u, uL, F]))
    leyenda(fig, [(r"$r$", AZUL, "recta"), (r"$L$ con $a=-\frac13$", AMBAR, "recta"),
                  (r"$d(r,O)$", ROJO, "dist")])
    return fig


@registrar
def fig_p4_e5():
    """a = 1: la recta T está dentro del plano S; S⊥ es la recta normal."""
    g1, g2 = V(1, 1, 2), V(0, 1, 1)
    n = np.cross(g1, g2); paralelos(n, V(-1, -1, 1))
    t = V(0, 1, 1); perp(t, n)
    O = V(0, 0, 0)
    fig, (ax,) = figura()
    plano(ax, n, 0, O, a=2.2, color=AZUL, e1=t)
    recta(ax, O, t, -1.6, 1.6, color=AMBAR, lw=2)
    recta(ax, O, unit(n), -2, 2, color=VERDE, lw=2)
    flecha(ax, O, g1 * 0.8, color=AZUL); flecha(ax, O, g2 * 1.2, color=AZUL)
    etiqueta(ax, g1 * 0.85, r"$(1,1,2)$", AZUL)
    punto(ax, O, "")
    ejes(ax, ((-2, 2), (-2, 2), (-2, 2)), vista=vista_auto([n], [t, n, g1]))
    leyenda(fig, [(r"$S$ con $a=1$: $x+y-z=0$", AZUL, "plano"), (r"$T=\mathrm{gen}\{(0,1,1)\}$", AMBAR, "recta"),
                  (r"$S^\perp=\mathrm{gen}\{(-1,-1,1)\}$", VERDE, "recta")])
    return fig


# ================================================================ P5
@registrar
def fig_p5_e1():
    """r ∥ L a distancia √2; el plano del haz de r que pasa por el origen."""
    A, u = V(0, -2, -3), V(1, 1, 2)
    en_plano(A, V(1, 1, -1), -1); en_plano(A, V(1, -1, 0), -2)
    paralelos(u, np.cross(V(1, 1, -1), V(1, -1, 0)))
    B = V(1, 1, 1); F = pie_en_recta(B, A, u)
    assert np.allclose(F, V(2, 0, 1)) and np.isclose(np.linalg.norm(B - F), np.sqrt(2))
    n = V(1, 3, -2); en_plano(A, n, 0); perp(u, n)
    fig, (ax,) = figura()
    plano(ax, n, 0, V(1, -1, -1), a=3.2, b=1.8, e1=u)
    recta(ax, A, u, -0.5, 3, color=AMBAR)
    recta(ax, B, u, -2, 1.5, color=VIOLETA)
    segmento(ax, B, F)
    punto(ax, V(0, 0, 0), r"$O$", dx=(-0.4, 0, 0.2))
    punto(ax, B, r"$(1,1,1)$", dx=(-0.6, 0.3, 0.4))
    etiqueta(ax, (B + F) / 2 + V(0.2, 0, 0.2), r"$\sqrt2$", ROJO)
    ejes(ax, ((-2, 4), (-4, 3), (-4, 4)), vista=vista_auto([n], [u, B - F]))
    leyenda(fig, [(r"$r$", AMBAR, "recta"), (r"$L$", VIOLETA, "recta"),
                  (r"$x+3y-2z=0$ (haz de $r$, por $O$)", AZUL, "plano"), ("distancia", ROJO, "dist")], ncol=4)
    return fig


@registrar
def fig_p5_e2():
    """Dos planos verticales ⟂ π a distancia √2 de P, uno a cada lado."""
    npi, dpi = V(1, 1, -1), -4
    en_plano(V(1, 2, -1), npi, dpi)
    P = V(1, 1, 3)
    fig, (ax,) = figura()
    plano(ax, npi, dpi, V(2, 2, 0), a=2.6, color=AZUL, alpha=0.18)
    for D in (2, -2):
        n = V(1, -1, 0); perp(n, npi); perp(n, V(0, 0, 1))
        assert np.isclose(d_punto_plano(P, n, D), np.sqrt(2))
        F = pie_en_plano(P, n, D)
        plano(ax, n, D, F + V(0, 0, -1.5), a=2.4, b=2.8, color=VERDE, alpha=0.25, e1=(1, 1, 0))
        segmento(ax, P, F)
    punto(ax, P, r"$P$", dx=(0.2, 0.2, 0.3))
    ejes(ax, ((-2, 4), (-2, 4), (-3, 5)), vista=vista_auto([npi, V(1, -1, 0)], [V(1, -1, 0)]))
    leyenda(fig, [(r"$\pi$", AZUL, "plano"), (r"$x-y+2=0$ y $x-y-2=0$", VERDE, "plano"),
                  (r"distancia $\sqrt2$", ROJO, "dist")])
    return fig


# ================================================================ P6
@registrar
def fig_p6_e1():
    """k = 1: r1 y r2 se cortan en (3,1,1) y están en el plano x - z - 2 = 0."""
    A1, u1, A2, u2 = V(1, 0, -1), V(2, 1, 2), V(2, 1, 0), V(1, 0, 1)
    I = V(3, 1, 1); en_recta(I, A1, u1); en_recta(I, A2, u2)
    n = np.cross(u1, u2); paralelos(n, V(1, 0, -1)); en_plano(A1, V(1, 0, -1), -2)
    fig, (ax,) = figura()
    plano(ax, V(1, 0, -1), -2, I, a=3.5, b=2.2, e1=(1, 0, 1))
    recta(ax, A1, u1, -1, 2.0, color=AMBAR)
    recta(ax, A2, u2, -2.5, 2.5, color=VIOLETA)
    punto(ax, I, r"$(3,1,1)$", color=VERDE, dx=(0.2, 0.2, 0.3))
    ejes(ax, ((-1, 6), (-2, 3), (-3, 4)), vista=vista_auto([V(1, 0, -1)], [u1, u2], frente=0.85))
    leyenda(fig, [(r"$r_1$", AMBAR, "recta"), (r"$r_2$ con $k=1$", VIOLETA, "recta"),
                  (r"plano que las contiene: $x-z-2=0$", AZUL, "plano")])
    return fig


@registrar
def fig_p6_e2():
    n1, d1, n2, d2 = V(2, -1, 0), 0, V(1, -1, -1), 1
    E, ue = V(0, 0, 1), np.cross(n1, n2)
    en_plano(E, n1, d1); en_plano(E, n2, d2); paralelos(ue, V(1, 2, -1))
    na, da = V(1, 0, 1), -1
    assert np.allclose(na, n1 - n2) and da == d1 - d2
    Q = V(1, 3, 0); en_plano(Q, na, da); en_plano(E, na, da); perp(ue, na)
    fig, (a1, a2) = figura(ancho=6.6, alto=3.6, n=2)
    plano(a1, n1, d1, E, a=2.4, color=AZUL, alpha=0.22, e1=ue)
    plano(a1, n2, d2, E, a=2.4, color=AMBAR, alpha=0.22, e1=ue)
    plano(a1, na, da, E + 0.5 * V(1, 2, -1), a=2.6, color=VERDE, alpha=0.3, e1=ue)
    recta(a1, E, ue, -1.2, 1.8, color=GRIS)
    punto(a1, Q, r"$(1,3,0)$", color=VERDE, dx=(0.2, 0.2, 0.3))
    ejes(a1, ((-2.5, 3.5), (-2, 4), (-2.5, 3.5)), r"a) plano del haz por $(1,3,0)$", vista=vista_auto([n1, n2, na], [ue]))
    O = V(0, 0, 0)
    plano(a2, n2, d2, E, a=1.8, color=AMBAR, alpha=0.2)
    plano(a2, n2, 0, O, a=1.8, color=VERDE, alpha=0.3)
    flecha(a2, O, unit(n2) * 0.8, color=GRIS)
    punto(a2, O, r"$O$", dx=(0.15, 0.1, -0.35))
    ejes(a2, ((-2, 2), (-2, 2), (-2, 2)), r"b) paralelo por el origen", vista=vista_auto([n2], [n2]))
    leyenda(fig, [(r"$2x-y=0$", AZUL, "plano"), (r"$x-y-z+1=0$", AMBAR, "plano"),
                  (r"planos pedidos", VERDE, "plano"), ("eje del haz", GRIS, "recta")], ncol=4)
    return fig


@registrar
def fig_p6_e5():
    """S es una recta dentro del plano T (x = y); S⊥ es el plano perpendicular a S."""
    s = V(1, 1, -1)
    nT = np.cross(V(1, 1, 1), V(1, 1, -1)); paralelos(nT, V(1, -1, 0)); perp(s, nT)
    en_plano(V(1, 1, 0), nT, 0)
    O = V(0, 0, 0)
    fig, (ax,) = figura()
    plano(ax, V(1, -1, 0), 0, O, a=2.2, color=AMBAR, alpha=0.22, e1=(0, 0, 1))
    plano(ax, s, 0, O, a=2.0, color=VERDE, alpha=0.22)
    recta(ax, O, unit(s), -2.4, 2.4, color=AZUL, lw=2.2)
    punto(ax, O, "")
    ejes(ax, ((-2, 2), (-2, 2), (-2, 2)), vista=vista_auto([V(1, -1, 0), s], [s]))
    leyenda(fig, [(r"$S=\mathrm{gen}\{(1,1,-1)\}$", AZUL, "recta"), (r"$T: x=y$  ($S\subset T$)", AMBAR, "plano"),
                  (r"$S^\perp: x+y-z=0$", VERDE, "plano")])
    return fig


# ================================================================ P7
@registrar
def fig_p7_e1():
    A1, u1 = V(0, 1, 1), V(1, 2, -1)
    I = V(1, 3, 0); en_recta(I, A1, u1)
    u2 = V(2, 1, 1)
    n, d = V(1, -1, 1), 3
    F = pie_en_plano(I, n, d)
    assert np.isclose(np.linalg.norm(I - F), 1 / np.sqrt(3))
    fig, (ax,) = figura()
    plano(ax, n, d, F + V(-0.5, 0, 0.5), a=1.7)
    recta(ax, A1, u1, -0.3, 2.0, color=AMBAR)
    recta(ax, I, u2, -0.9, 0.9, color=VIOLETA)
    segmento(ax, I, F)
    punto(ax, I, r"$(1,3,0)$", color=VERDE, dx=(0.25, 0.2, 0.3))
    etiqueta(ax, (I + F) / 2 + V(-0.6, 0, -0.35), r"$\frac{\sqrt3}{3}$", ROJO)
    ejes(ax, ((-1, 3), (1, 5), (-2, 2)), vista=vista_auto([n], [u1, u2, n]))
    leyenda(fig, [(r"$L_1$", AMBAR, "recta"), (r"$L_2$ con $k=2$", VIOLETA, "recta"),
                  (r"$\pi: x-y+z+3=0$", AZUL, "plano"), ("distancia", ROJO, "dist")], ncol=4)
    return fig


@registrar
def fig_p7_e2():
    n1, d1, n2, d2 = V(1, 1, 1), 3, V(1, -2, 1), 1
    nh, dh = V(8, -7, 8), 14
    assert np.allclose(nh, 3 * n1 + 5 * n2) and dh == 3 * d1 + 5 * d2
    Y = V(0, 2, 0); en_plano(Y, nh, dh)
    E = V(0, -2 / 3, -7 / 3); en_plano(E, n1, d1); en_plano(E, n2, d2); ue = np.cross(n1, n2)
    P = V(3, 1, 2)
    fig, (a1, a2) = figura(ancho=6.6, alto=3.6, n=2)
    plano(a1, n1, d1, E, a=2.4, color=AZUL, alpha=0.22, e1=ue)
    plano(a1, n2, d2, E, a=2.4, color=AMBAR, alpha=0.22, e1=ue)
    plano(a1, nh, dh, (E + Y) / 2, a=2.6, color=VERDE, alpha=0.3, e1=ue)
    recta(a1, E, ue, -0.9, 0.9, color=GRIS)
    recta(a1, V(0, -2, 0), V(0, 1, 0), 0, 5, color="black", lw=0.8)
    punto(a1, Y, r"$(0,2,0)$", color=VERDE, dx=(0.2, 0.2, 0.3))
    ejes(a1, ((-3.5, 2.5), (-3, 3), (-5, 1)), r"a) ordenada al origen 2", vista=vista_auto([n1, n2, nh], [ue, V(0, 1, 0)]))
    F = pie_en_plano(P, n2, d2)
    plano(a2, n2, d2, F, a=2.2, color=AMBAR, alpha=0.22)
    recta(a2, P, n2, -1.6, 0.8, color=VERDE, lw=2)
    punto(a2, F, "", color=VERDE)
    punto(a2, P, r"$(3,1,2)$", dx=(0.2, 0.2, 0.3))
    ejes(a2, ((0, 5), (-1, 4), (-0.5, 4.5)), r"b) recta ortogonal a $\pi$", vista=vista_auto([n2], [n2]))
    leyenda(fig, [(r"$x+y+z+3=0$", AZUL, "plano"), (r"$\pi: x-2y+z+1=0$", AMBAR, "plano"),
                  (r"$8x-7y+8z+14=0$", VERDE, "plano"), ("recta pedida", VERDE, "recta")], ncol=4)
    return fig


# ================================================================ Apéndice A
@registrar
def fig_sarrus():
    """Regla de Sarrus: diagonales que suman (azul) y que restan (naranja).

    Colores = RoyalBlue y BurntOrange de dvipsnames, los mismos de las fórmulas del apéndice.
    """
    AZ, NA = (0, 0.5, 1), (1, 0.49, 0)
    L = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
    # Comprobación: la regla coincide con el determinante en una matriz cualquiera
    M = np.array([[3, 2, 0], [-12, 0, 3], [-6, -1, 1]], dtype=float)
    (a, b, c), (d, e, f), (g, h, i) = M
    assert np.isclose((a*e*i + b*f*g + c*d*h) - (c*e*g + a*f*h + b*d*i), np.linalg.det(M))
    fig, ax = plt.subplots(figsize=(4.6, 2.5))
    for k in range(3):                                   # diagonales
        ax.annotate("", xy=(k + 2.25, -2.25), xytext=(k - 0.25, 0.25),
                    arrowprops=dict(arrowstyle="-|>", color=AZ, lw=1.6, alpha=0.75, shrinkA=0, shrinkB=0))
        ax.annotate("", xy=(k - 0.25, -2.25), xytext=(k + 2.25, 0.25),
                    arrowprops=dict(arrowstyle="-|>", color=NA, lw=1.6, alpha=0.75, shrinkA=0, shrinkB=0))
    for r in range(3):
        for c_ in range(5):
            ax.text(c_, -r, f"${L[r][c_ % 3]}$", ha="center", va="center", fontsize=15,
                    color="black" if c_ < 3 else "#999999",
                    bbox=dict(boxstyle="circle,pad=0.12", fc="white", ec="none"), zorder=5)
    ax.plot([2.5, 2.5], [0.45, -2.45], color="#bbbbbb", ls=":", lw=1)
    for k, txt in enumerate(("aei", "bfg", "cdh")):
        ax.text(k + 2.35, -2.6, f"$+{txt}$", color=AZ, ha="center", va="top", fontsize=11)
    for k, txt in enumerate(("ceg", "afh", "bdi")):
        ax.text(k - 0.35, -2.6, f"$-{txt}$", color=NA, ha="center", va="top", fontsize=11)
    ax.set_xlim(-0.9, 4.9); ax.set_ylim(-3.15, 0.55)
    ax.set_aspect("equal"); ax.axis("off")
    return fig


if __name__ == "__main__":
    filtro = sys.argv[1] if len(sys.argv) > 1 else ""
    for nombre, f in FIGURAS.items():
        if filtro not in nombre:
            continue
        fig = f()
        fig.subplots_adjust(left=0, right=1, top=0.97, bottom=0.1, wspace=0.02)
        for ext in ("pdf", "png"):
            fig.savefig(OUT / f"{nombre}.{ext}", dpi=170, bbox_inches="tight", pad_inches=0.04)
        plt.close(fig)
        print("ok", nombre)
