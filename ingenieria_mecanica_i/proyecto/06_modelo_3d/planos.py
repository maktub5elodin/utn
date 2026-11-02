# -*- coding: utf-8 -*-
"""
Planos 2D generados desde el modelo 3D (proyección con líneas ocultas de TechDraw).
Si cambia parametros.py, `make` los regenera.
    ~/Aplicaciones/FreeCAD.AppImage freecadcmd planos.py
Deja un JSON por lámina en build/planos_json/; dxf.py escribe los DXF con ezdxf.


Cada lámina está en mm reales: el marco A3 se agranda según la escala (1:E), así
medir sobre el DXF da la medida de la pieza. Termina con error si dos textos se
superponen o si alguno se sale del marco.
"""
import json, math, os, sys, traceback

CARPETA = (os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals()
           else os.getcwd())
sys.path.insert(0, CARPETA)

import FreeCAD as App
import Part
import TechDraw

import parametros as P
import piezas as Z
from dibujo import Dibujo, formato

V = App.Vector
FECHA = "02/11/2026"
LEYENDA = "Plano de estudio: medidas de referencia, no definitivas"
SALIDA = os.path.join(CARPETA, "planos")

# Filas de la matriz: u (derecha del papel), v (arriba), w (hacia el observador)
MAPAS = {
    "frente": ((-1, 0, 0), (0, 0, 1), (0, 1, 0)),     # desde +Y: se ve la transmisión
    "planta": ((-1, 0, 0), (0, -1, 0), (0, 0, 1)),    # método E: abajo de la frontal
    "lateral": ((0, 1, 0), (0, 0, 1), (1, 0, 0)),     # método E: desde +X, a la derecha
    "largo": ((1, 0, 0), (0, 0, 1), (0, -1, 0)),      # pieza suelta, X hacia la derecha
}
CIRCULO_TOL = 0.01


def matriz(nombre):
    (a, b, c), (d, e, f), (g, h, i) = MAPAS[nombre]
    m = App.Matrix()
    m.A11, m.A12, m.A13 = a, b, c
    m.A21, m.A22, m.A23 = d, e, f
    m.A31, m.A32, m.A33 = g, h, i
    return m


def _circulo_de(p0, p1, p2):
    ax, ay, bx, by, cx, cy = p0.x, p0.y, p1.x, p1.y, p2.x, p2.y
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    if abs(d) < 1e-9:
        return None
    a2, b2, c2 = ax * ax + ay * ay, bx * bx + by * by, cx * cx + cy * cy
    x = (a2 * (by - cy) + b2 * (cy - ay) + c2 * (ay - by)) / d
    y = (a2 * (cx - bx) + b2 * (ax - cx) + c2 * (bx - ax)) / d
    return x, y, math.hypot(ax - x, ay - y)


def primitiva(e):
    """Arista proyectada → línea, círculo, arco o polilínea (editables en CAD)."""
    largo = e.Length
    if largo < 0.02:
        return None
    pts = e.discretize(Number=17)
    a, b = pts[0], pts[-1]
    if isinstance(e.Curve, Part.Line):
        return ("l", (a.x, a.y), (b.x, b.y))
    # ¿Es recta o circunferencia, aunque HLR la entregue como BSpline?
    dx, dy = b.x - a.x, b.y - a.y
    lg = math.hypot(dx, dy)
    if lg > 1e-6 and all(abs((p.x - a.x) * dy - (p.y - a.y) * dx) / lg < CIRCULO_TOL for p in pts):
        return ("l", (a.x, a.y), (b.x, b.y))
    cir = _circulo_de(pts[0], pts[6], pts[11])
    if cir:
        x, y, r = cir
        if r < 5000 and all(abs(math.hypot(p.x - x, p.y - y) - r) < CIRCULO_TOL for p in pts):
            if lg < 1e-4:
                return ("c", (x, y), r)
            a0 = math.degrees(math.atan2(a.y - y, a.x - x))
            a1 = math.degrees(math.atan2(b.y - y, b.x - x))
            m = pts[8]
            am = math.degrees(math.atan2(m.y - y, m.x - x))
            if (am - a0) % 360 < (a1 - a0) % 360:
                return ("a", (x, y), r, a0, a1)
            return ("a", (x, y), r, a1, a0)
    n = max(8, min(60, int(largo / 1.5)))
    return ("p", [(p.x, p.y) for p in e.discretize(Number=n)])


def _clave(p):
    if p[0] == "l":
        a, b = sorted((tuple(round(v, 2) for v in p[1]), tuple(round(v, 2) for v in p[2])))
        return ("l", a, b)
    if p[0] == "c":
        return ("c", round(p[1][0], 2), round(p[1][1], 2), round(p[2], 2))
    if p[0] == "a":
        return ("a", round(p[1][0], 2), round(p[1][1], 2), round(p[2], 2),
                round(p[3] % 360, 1), round(p[4] % 360, 1))
    return ("p", tuple(round(v, 2) for q in p[1] for v in q))


def proyectar(formas, mapa, ocultas=True):
    """Devuelve (visibles, ocultas) en coordenadas del papel, sin escala."""
    c = Part.makeCompound(formas).transformed(matriz(mapa))
    r = TechDraw.projectEx(c, V(0, 0, 1))
    vis, ocu, vistos = [], [], set()
    for idx, destino in ((0, vis), (3, vis), (5, ocu), (8, ocu)):
        if destino is ocu and not ocultas:
            continue
        comp = r[idx]
        if comp is None or comp.isNull():
            continue
        for e in comp.Edges:
            p = primitiva(e)
            if p is None:
                continue
            k = _clave(p)
            if k not in vistos:
                vistos.add(k)
                destino.append(p)
    return vis, ocu


class Lamina(Dibujo):
    def __init__(self, escala, numero, titulo):
        super().__init__(escala)
        self.numero, self.titulo = numero, titulo

    def pp(self, x, y):
        """De mm de papel a coordenadas del dibujo."""
        return x * self.E, y * self.E

    def t(self, x, y, h, s, alin="i", capa="Texto", rot=0.0):
        X, Y = self.pp(x, y)
        self.texto(capa, X, Y, h, s, alin, rot)


class Vista:
    """Una vista: lleva puntos 3D al dibujo. ref (x, y, z) cae en papel (px, py)."""

    def __init__(self, lam, mapa, ref, px, py):
        self.L, self.m = lam, MAPAS[mapa]
        self.mapa = mapa
        X, Y = lam.pp(px, py)
        u0, v0 = self._uv(ref)
        self.ox, self.oy = X - u0, Y - v0

    def _uv(self, p):
        (a, b, c), (d, e, f) = self.m[0], self.m[1]
        return (a * p[0] + b * p[1] + c * p[2], d * p[0] + e * p[1] + f * p[2])

    def pt(self, x, y, z):
        u, v = self._uv((x, y, z))
        return self.ox + u, self.oy + v

    def trazar(self, prims, capa):
        L, ox, oy = self.L, self.ox, self.oy
        for p in prims:
            if p[0] == "l":
                L.linea(capa, (p[1][0] + ox, p[1][1] + oy), (p[2][0] + ox, p[2][1] + oy))
            elif p[0] == "c":
                L.circulo(capa, (p[1][0] + ox, p[1][1] + oy), p[2])
            elif p[0] == "a":
                L.arco(capa, (p[1][0] + ox, p[1][1] + oy), p[2], p[3], p[4])
            else:
                L.polilinea(capa, [(q[0] + ox, q[1] + oy) for q in p[1]])

    def formas(self, formas, ocultas=True):
        vis, ocu = proyectar(formas, self.mapa, ocultas)
        self.trazar(ocu, "Ocultas")
        self.trazar(vis, "Contornos")

    def eje(self, a, b):
        self.L.linea("Ejes", self.pt(*a), self.pt(*b))

    def cruz(self, p, r):
        """Ejes de una circunferencia vista de frente."""
        x, y = self.pt(*p)
        s = 4 * self.L.E
        self.L.linea("Ejes", (x - r - s, y), (x + r + s, y))
        self.L.linea("Ejes", (x, y - r - s), (x, y + r + s))


# ------------------------------------------------------------- marco y rótulo
ROT_X0, ROT_X1 = 25.0, 410.0    # todo el ancho del recuadro, como la plantilla de la cátedra
ROT_Y0, ROT_Y1 = 10.0, 30.0
COL_1, COL_2, COL_3 = 102.0, 333.0, 371.5


def marco_y_rotulo(L, escala, metodo=True):
    """Rótulo de la plantilla de la cátedra (dos filas y tres columnas), llevado a A3."""
    pp = L.pp
    L.polilinea("Texto", [pp(0, 0), pp(420, 0), pp(420, 297), pp(0, 297)], True)
    L.polilinea("Marco", [pp(25, 10), pp(410, 10), pp(410, 287), pp(25, 287)], True)
    for a, b in (((0, 148.5), (25, 148.5)), ((410, 148.5), (420, 148.5)),
                 ((210, 0), (210, 10)), ((210, 287), (210, 297))):
        L.linea("Marco", pp(*a), pp(*b))
    x0, x1, y0, y1 = ROT_X0, ROT_X1, ROT_Y0, ROT_Y1
    ym = (y0 + y1) / 2
    L.polilinea("Marco", [pp(x0, y0), pp(x1, y0), pp(x1, y1), pp(x0, y1)], True)
    L.linea("Marco", pp(x0, ym), pp(x1, ym))
    L.linea("Marco", pp(COL_1, y0), pp(COL_1, y1))
    L.linea("Marco", pp(COL_2, y0), pp(COL_2, y1))
    L.linea("Texto", pp(COL_3, y0), pp(COL_3, ym))
    arriba, abajo = ym + 2.5, y0 + 3.25
    L.t((x0 + COL_1) / 2, arriba, 5, "UTN FRBA", "c")
    L.t((COL_1 + COL_2) / 2, arriba, 5, L.titulo, "c")
    L.t((COL_2 + x1) / 2, arriba, 5, f"Lámina {L.numero} de 4", "c")
    L.t((x0 + COL_1) / 2, abajo, 3.5, "Curso S1091 - Grupo 1", "c")
    L.t((COL_1 + COL_2) / 2, abajo, 3.5, "Ingeniería Mecánica I", "c")
    L.t((COL_2 + COL_3) / 2, abajo, 3.5,
        f"Escala {escala}" if escala[0].isdigit() else escala, "c")
    L.t((COL_3 + x1) / 2, abajo, 3.5, FECHA, "c")
    if metodo:   # símbolo del método E: el cono se mira desde el lado angosto
        xs, yc = COL_2 - 24, y0 + 5
        L.polilinea("Contornos", [pp(xs, yc - 1.2), pp(xs + 7, yc - 2.6), pp(xs + 7, yc + 2.6),
                                  pp(xs, yc + 1.2)], True)
        L.circulo("Contornos", pp(xs + 12.5, yc), 2.6 * L.E)
        L.circulo("Contornos", pp(xs + 12.5, yc), 1.2 * L.E)
    L.t(x1 - 2, y1 + 1.5, 3.5, LEYENDA, "d")


def tabla(L, x, ytop, anchos, filas, h=2.5, fila=5.0):
    """Tabla con grilla fina; la primera fila es el encabezado."""
    pp = L.pp
    total = sum(anchos)
    n = len(filas)
    for k in range(n + 1):
        L.linea("Texto", pp(x, ytop - k * fila), pp(x + total, ytop - k * fila))
    xx = x
    for a in anchos + [0]:
        L.linea("Texto", pp(xx, ytop), pp(xx, ytop - n * fila))
        xx += a
    for k, f in enumerate(filas):
        xx = x
        for a, val in zip(anchos, f):
            L.t(xx + 1.5, ytop - k * fila - fila + (fila - h) / 2, h, str(val))
            xx += a


def globo(L, n, ancla, dx, dy):
    """Número en círculo con línea de referencia. dx, dy en mm de papel."""
    E = L.E
    cx, cy = ancla[0] + dx * E, ancla[1] + dy * E
    r = 4.0 * E
    d = math.hypot(ancla[0] - cx, ancla[1] - cy) or 1.0
    L.linea("Cotas", (cx + (ancla[0] - cx) / d * r, cy + (ancla[1] - cy) / d * r), ancla)
    L.circulo("Cotas", (cx, cy), r)
    a = 0.5 * E
    L.circulo("Cotas", ancla, a * 0.6)
    L.texto("Texto", cx, cy - 1.75 * E, 3.5, str(n), "c")


def engranaje_simple(z, y, zc):
    """Representación convencional: cilindro del diámetro exterior."""
    return Z.cil(P.MODULO * (z + 2) / 2, *P.X_ENGRANAJES, y, zc)


# ------------------------------------------------------------------ lámina a
LISTA = [  # n.°, denominación, cantidad
    (1, "Base", 1),
    (2, "Guía con apoyos", 2),
    (3, "Carro con patines", 1),
    (4, "Soporte del cuello", 1),
    (5, "Rodamiento del cuello", 1),
    (6, "Mordaza del cuello", 1),
    (7, "Botella", 1),
    (8, "Placa de la caja", 2),
    (9, "Eje del rodillo", 1),
    (10, "Rodillo", 1),
    (11, "Manivela", 1),
    (12, "Engranaje conductor", 1),
    (13, "Engranaje conducido", 1),
    (14, "Husillo", 1),
    (15, "Collar del husillo", 2),
    (16, "Tuerca con poste", 1),
    (17, "Portacuchilla", 1),
    (18, "Cuchilla", 1),
]


def lista_piezas(L, x, y):
    """Se lee hacia arriba, desde el encabezado."""
    filas = [(a, b, c) for a, b, c in reversed(LISTA)]
    filas.append(("N.°", "DENOMINACIÓN", "CANT."))
    fila = 5.3
    tabla(L, x, y + fila * len(filas), [12, 72, 15], filas, 2.5, fila)


def primitivo_de_costado(vista, y, zc, dp, planta=False):
    """ISO 2203: la superficie primitiva en trazo largo y punto, y sobresale del contorno."""
    L = vista.L
    xa, xb = P.X_ENGRANAJES[0] - 3, P.X_ENGRANAJES[1] + 3
    for s in (-1, 1):
        if planta:
            L.linea("Ejes", vista.pt(xa, y + s * dp / 2, 0), vista.pt(xb, y + s * dp / 2, 0))
        else:
            L.linea("Ejes", vista.pt(xa, y, zc + s * dp / 2), vista.pt(xb, y, zc + s * dp / 2))


def rosca_de_costado(vista, planta=False):
    """ISO 6410-1: cresta en gruesa (la da la proyección) y fondo en fina continua."""
    rf = P.D_HUSILLO_FONDO / 2
    L = vista.L
    for s in (-1, 1):
        if planta:
            L.linea("Finas", vista.pt(P.X_HUSILLO_INI, P.Y_H + s * rf, 0),
                    vista.pt(P.X_HUSILLO_FIN, P.Y_H + s * rf, 0))
        else:
            L.linea("Finas", vista.pt(P.X_HUSILLO_INI, P.Y_H, P.Z_H + s * rf),
                    vista.pt(P.X_HUSILLO_FIN, P.Y_H, P.Z_H + s * rf))


def lamina_conjunto():
    L = Lamina(2.5, 1, "Plano de conjunto")
    marco_y_rotulo(L, "1:2,5")
    pz = Z.formas()
    formas = [d[0] for n, d in pz.items() if n not in ("EngranajeZ1", "EngranajeZ2")]
    formas += [engranaje_simple(P.Z_1, P.Y_R, P.Z_R), engranaje_simple(P.Z_2, P.Y_H, P.Z_H),
               Z.botella_solida(), Z.husillo_liso()]
    H, yr, zr, yh, zh = P.H_EJE, P.Y_R, P.Z_R, P.Y_H, P.Z_H
    xman = P.X_MANIVELA - 8 - P.LARGO_MANGO
    xfin = P.X_HUSILLO_FIN + P.RECORRIDO
    X_F, Y_F = 228.0, 186.0

    # --- Frontal
    F = Vista(L, "frente", (0, 0, 0), X_F, Y_F)
    F.formas(formas)
    F.eje((-12, 0, H), (P.X_BORDE + 8, 0, H))
    F.eje((xman - 6, yr, zr), (P.X_EJE[1] + 8, yr, zr))
    F.eje((P.X_HUSILLO_INI - 6, yh, zh), (xfin + 6, yh, zh))
    # Posición final del carro y del husillo
    s = P.RECORRIDO
    c = P.X_CARRO
    zc = P.Z_CARRO
    esq = [F.pt(c[0] + s, 0, zc[0]), F.pt(c[1] + s, 0, zc[0]), F.pt(c[1] + s, 0, zc[1]),
           F.pt(c[0] + s, 0, zc[1]), F.pt(c[0] + s, 0, zc[0])]
    for a, b in zip(esq, esq[1:]):
        L.linea("Extremas", a, b)
    rh = P.D_HUSILLO / 2
    for d in (-rh, rh):
        L.linea("Extremas", F.pt(P.X_HUSILLO_FIN, 0, zh + d), F.pt(xfin, 0, zh + d))
    L.linea("Extremas", F.pt(xfin, 0, zh - rh), F.pt(xfin, 0, zh + rh))
    L.t(112, Y_F + 92, 3.5, "Vista frontal", "c")
    dp1, dp2 = P.MODULO * P.Z_1, P.MODULO * P.Z_2
    primitivo_de_costado(F, yr, zr, dp1)
    primitivo_de_costado(F, yh, zh, dp2)
    rosca_de_costado(F)

    bz = -P.ESPESOR_BASE
    L.cota(F.pt(c[1] + s, 0, bz), F.pt(c[1], 0, bz), -6, f"Recorrido {formato(s)}", "h")
    L.cota(F.pt(P.X_BASE[1], 0, bz), F.pt(P.X_BASE[0], 0, bz), -12, direc="h")
    L.cota(F.pt(xfin, 0, bz), F.pt(xman, 0, bz), -18, direc="h")

    # --- Superior (método E: debajo de la frontal)
    S = Vista(L, "planta", (0, 0, 0), X_F, 110.0)
    S.formas(formas)
    S.eje((-12, 0, 0), (P.X_BORDE + 8, 0, 0))
    S.eje((xman - 6, yr, 0), (P.X_EJE[1] + 8, yr, 0))
    S.eje((P.X_HUSILLO_INI - 6, yh, 0), (P.X_HUSILLO_FIN + 6, yh, 0))
    L.t(180, 158.5, 3.5, "Vista superior", "c")
    primitivo_de_costado(S, yr, zr, dp1, True)
    primitivo_de_costado(S, yh, zh, dp2, True)
    rosca_de_costado(S, True)
    L.cota(S.pt(P.X_BASE[1], P.Y_BASE[0], 0), S.pt(P.X_BASE[1], P.Y_BASE[1], 0), 20, direc="v")

    # --- Lateral (método E: a la derecha de la frontal)
    Lat = Vista(L, "lateral", (0, 0, 0), 342.0, Y_F)
    Lat.formas(formas)
    Lat.cruz((0, 0, H), P.R_B)
    Lat.cruz((0, yr, zr), P.D_R / 2)
    Lat.cruz((0, yh, zh), 6)
    L.t(370, Y_F + 92, 3.5, "Vista lateral", "c")
    L.circulo("Ejes", Lat.pt(0, yr, zr), dp1 / 2)
    L.circulo("Ejes", Lat.pt(0, yh, zh), dp2 / 2)
    # Fondo de rosca en la vista de extremo: fina, unas tres cuartas partes (ISO 6410-1)
    L.arco("Finas", Lat.pt(0, yh, zh), P.D_HUSILLO_FONDO / 2, 90, 360)
    L.cota(Lat.pt(0, P.Y_BASE[1], 0), Lat.pt(0, P.Y_BASE[1], H), -11, direc="v")

    # --- Lista de piezas y nota
    lista_piezas(L, 311, 37)
    L.t(30, 34, 2.5, "Trazo largo y dos puntos: posición final del carro y del husillo.")

    # --- Globos
    g = lambda n, v, p, dx, dy: globo(L, n, v.pt(*p), dx, dy)
    g(7, F, (190, 0, H + P.R_B), 0, 8)
    g(4, F, (14, 0, H + 40), -10, 8)
    g(11, F, (-90, yr, zr + P.R_MANIVELA), 13, 5)
    g(9, F, (-10, yr, zr), 24, 1)
    g(10, F, (100, yr, zr - 23), -12, -7)
    g(8, F, (60, yr, P.Z_CARRO[1] + 15), -22, -3)
    g(12, F, (47, yr, zr - 10), 34, -10)
    g(13, F, (47, yr, zh - 25), 30, -5)
    g(14, F, (160, yh, zh - 4), 0, -8)
    g(15, F, (26.5, yh, zh + 6), 24, -2)
    g(3, F, (-5, 0, 25), 34, -3)
    g(16, F, (P.X_TUERCA[0] + 10, yh, 40), 22, 8)
    g(17, F, (P.X_CUCHILLA - 8, 0, H - 40), -15, 12)
    g(1, S, (300, 100, 0), -16, 0)
    g(2, S, (200, P.Y_GUIAS[0], 0), 0, 10)
    g(18, S, (P.X_CUCHILLA - 1, -P.R_B - 2, 0), -18, -5)
    g(6, Lat, (0, -14, H + 14), -26, 18)
    g(5, Lat, (0, -25, H + 10), -32, 9)
    return L


# ------------------------------------------------------------------ lámina b
def lamina_despiece():
    L = Lamina(1, 2, "Despiece de piezas clave")
    marco_y_rotulo(L, "1:1")
    pz = Z.formas()
    yr, zr, zh = P.Y_R, P.Z_R, P.Z_H

    # --- Eje con rodillo
    Y_E = 238.0
    L.t(32, 277, 3.5, "Piezas 9 y 10: eje con rodillo")
    eje = [pz["Eje"][0], pz["NucleoRodillo"][0], pz["Rodillo"][0]]
    x0, x1 = P.X_EJE
    E1 = Vista(L, "largo", (x0, yr, zr), 40, Y_E)
    E1.formas(eje)
    E1.eje((x0 - 6, yr, zr), (x1 + 6, yr, zr))
    L.cota(E1.pt(x0, yr, zr - P.D_EJE / 2), E1.pt(x1, yr, zr - P.D_EJE / 2), -21, direc="h")
    L.cota(E1.pt(P.X_RODILLO[0], yr, zr + P.D_R / 2), E1.pt(P.X_RODILLO[1], yr, zr + P.D_R / 2),
           6, direc="h")
    L.cota(E1.pt(x0, yr, zr + P.D_EJE / 2), E1.pt(P.X_RODILLO[0], yr, zr + P.D_EJE / 2),
           16, direc="h")
    L.cota(E1.pt(x0 + 12, yr, zr - P.D_EJE / 2), E1.pt(x0 + 12, yr, zr + P.D_EJE / 2),
           0, f"%%c{P.D_EJE:.0f}", "v")
    E2 = Vista(L, "lateral", (0, yr, zr), 218, Y_E)
    E2.formas(eje)
    E2.cruz((0, yr, zr), P.D_R / 2)
    L.cota(E2.pt(0, yr - P.D_R / 2, zr), E2.pt(0, yr + P.D_R / 2, zr), 31, f"%%c{P.D_R:.0f}", "h")

    # --- Engranajes
    L.t(32, 195, 3.5, "Piezas 12 y 13: par de engranajes")
    g1, g2 = pz["EngranajeZ1"][0], pz["EngranajeZ2"][0]
    Y_G = 108.0
    G = Vista(L, "lateral", (0, yr, zh), 92, Y_G)
    # Representación convencional: cada rueda como sólido hasta la cabeza, sin dientes, con
    # el primitivo en trazo largo y punto. En la zona de engrane ninguna tapa a la otra.
    M = P.MODULO
    dp1, dp2 = M * P.Z_1, M * P.Z_2
    for zc, z, dp, agujero in ((zr, P.Z_1, dp1, P.D_EJE), (zh, P.Z_2, dp2, P.D_HUSILLO)):
        c = G.pt(0, yr, zc)
        L.circulo("Contornos", c, M * (z + 2) / 2)
        L.circulo("Ejes", c, dp / 2)
        L.circulo("Finas", c, M * (z - 2.5) / 2)
        L.circulo("Contornos", c, agujero / 2)
    x_, y_ = G.pt(0, yr, zr)
    L.linea("Ejes", (x_ - 28, y_), (x_ + 28, y_))
    x2, y2 = G.pt(0, yr, zh)
    L.linea("Ejes", (x2 - 48, y2), (x2 + 48, y2))
    L.linea("Ejes", (x2, y2 - 45), (x_, y_ + 26))
    L.cota(G.pt(0, yr + 22, zh), G.pt(0, yr + 22, zr), -42, direc="v")
    # De costado: el contorno de cada rueda, también en la zona de engrane
    Gl = Vista(L, "largo", (47, yr, zh), 168, Y_G)
    xa, xb = P.X_ENGRANAJES
    for zc, z in ((zr, P.Z_1), (zh, P.Z_2)):
        ra = M * (z + 2) / 2
        L.polilinea("Contornos", [Gl.pt(xa, yr, zc - ra), Gl.pt(xb, yr, zc - ra),
                                  Gl.pt(xb, yr, zc + ra), Gl.pt(xa, yr, zc + ra)], True)
    for zc, ag in ((zr, P.D_EJE), (zh, P.D_HUSILLO)):
        for sg in (-1, 1):
            L.linea("Ocultas", Gl.pt(xa, yr, zc + sg * ag / 2), Gl.pt(xb, yr, zc + sg * ag / 2))
    Gl.eje((47, yr, zh - 45), (47, yr, zr + 26))
    for zc, dp in ((zr, dp1), (zh, dp2)):
        for sg in (-1, 1):
            L.linea("Ejes", Gl.pt(xa - 3, yr, zc + sg * dp / 2), Gl.pt(xb + 3, yr, zc + sg * dp / 2))
    L.cota(Gl.pt(P.X_ENGRANAJES[0], yr, zr + 22), Gl.pt(P.X_ENGRANAJES[1], yr, zr + 22),
           4, direc="h")

    def dat(z):
        return (z, formato(M), formato(M * z), formato(M * (z + 2)), formato(M * (z - 2.5)))
    d1, d2 = dat(P.Z_1), dat(P.Z_2)
    filas = [("Dato", "Conductor", "Conducido")]
    for nom, a, b in zip(("Dientes z", "Módulo m", "Ø primitivo", "Ø exterior", "Ø de fondo"), d1, d2):
        filas.append((nom.replace("Ø", "%%c"), a, b))
    tabla(L, 30, 61, [40, 18, 18], filas, 2.5, 5.0)
    filas = [("Dato", "Valor"),
             ("Distancia entre ejes", f"{formato(P.DIST_EJES)} mm"),
             ("Relación i = z2 / z1", formato(P.I)),
             ("Ángulo de presión", "20%%d"),
             ("Ancho de cara", f"{formato(P.X_ENGRANAJES[1] - P.X_ENGRANAJES[0])} mm")]
    tabla(L, 112, 61, [62, 44], filas, 2.5, 5.0)

    # --- Placa de la caja
    L.t(248, 222, 3.5, "Pieza 8: placa (2)")
    placa = pz["Placa1"][0]
    zb = P.Z_CARRO[1]
    Y_C = 74.0
    C = Vista(L, "lateral", (0, yr, zb), 250, Y_C)
    C.formas([placa], ocultas=False)
    C.cruz((0, yr, zr), P.D_EJE / 2)
    C.cruz((0, yr, zh), P.D_HUSILLO / 2)
    xc_, yc_ = C.pt(0, yr, zr)
    L.texto("Texto", xc_ + 16.5, yc_ + 1.5, 2.5, f"%%c{formato(P.D_EJE + 0.6)}")
    L.texto("Texto", xc_ + 8, yc_ + 22, 2.5, f"R{formato(P.R_PLACA_EJE)}")
    xh_, yh_ = C.pt(0, yr, zh)
    L.texto("Texto", xh_ + 7, yh_ + 2, 2.5, f"%%c{formato(P.D_HUSILLO + 0.6)}")
    L.cota(C.pt(0, yr - P.R_PLACA_EJE, zh), C.pt(0, yr - P.R_PLACA_EJE, zr), 4, direc="v")
    L.cota(C.pt(0, yr - P.R_PLACA_EJE, zb), C.pt(0, yr - P.R_PLACA_EJE, zr), 15, direc="v")
    L.cota(C.pt(0, yr - P.R_PLACA_HUSILLO, zb), C.pt(0, yr + P.R_PLACA_HUSILLO, zb), -6,
           direc="h")
    Cl = Vista(L, "largo", (P.X_PLACA_1[0], yr, zb), 287, Y_C)
    Cl.formas([placa])
    L.cota(Cl.pt(P.X_PLACA_1[0], yr, zb), Cl.pt(P.X_PLACA_1[1], yr, zb), -6, direc="h")

    # --- Soporte del cuello
    L.t(310, 277, 3.5, "Pieza 4: soporte del cuello")
    sop = pz["SoporteCuello"][0]
    H = P.H_EJE
    a, h = P.ANCHO_SOPORTE / 2, P.ALTO_SOPORTE / 2
    Y_S = 76.0
    So = Vista(L, "lateral", (0, 0, zb), 345, Y_S)
    So.formas([sop])
    So.cruz((0, 0, H), P.D_ROD_CUELLO[1] / 2)
    L.cota(So.pt(0, -a, H + h), So.pt(0, a, H + h), 6, direc="h")
    L.cota(So.pt(0, -a, H - h), So.pt(0, -a, H + h), 9, direc="v")
    L.cota(So.pt(0, a * 0.7, zb), So.pt(0, a * 0.7, H), -14, direc="v")
    L.cota(So.pt(0, -a * 0.7, zb), So.pt(0, a * 0.7, zb), -7, direc="h")
    L.cota(So.pt(0, -P.D_ROD_CUELLO[1] / 2, H), So.pt(0, P.D_ROD_CUELLO[1] / 2, H), 13,
           f"%%c{P.D_ROD_CUELLO[1]:.0f}", "h")
    Sl = Vista(L, "largo", (P.X_SOPORTE[0], 0, zb), 387, Y_S)
    Sl.formas([sop])
    Sl.eje((P.X_SOPORTE[0] - 2, 0, H), (P.X_SOPORTE[1] + 2, 0, H))
    L.cota(Sl.pt(P.X_SOPORTE[0], 0, zb), Sl.pt(P.X_SOPORTE[1], 0, zb), -7, direc="h")
    return L


# ------------------------------------------------------------------ lámina c
def flecha_giro(L, c, r, a0, a1, horaria=False):
    """Arco con punta, para indicar un sentido de giro."""
    L.arco("Cotas", c, r, a0, a1)
    a = math.radians(a0 if horaria else a1)
    px, py = c[0] + r * math.cos(a), c[1] + r * math.sin(a)
    t = -1 if horaria else 1
    tx, ty = -math.sin(a) * t, math.cos(a) * t
    nx, ny = math.cos(a), math.sin(a)
    largo, ancho = 3.5, 0.45
    L.solido("Cotas", (px + tx * largo, py + ty * largo),
             (px + nx * ancho, py + ny * ancho), (px - nx * ancho, py - ny * ancho))


def rect(L, capa, x0, y0, x1, y1):
    L.polilinea(capa, [(x0, y0), (x1, y0), (x1, y1), (x0, y1)], True)


def tierra(L, x0, x1, y):
    """Bastidor fijo: línea con rayado por debajo."""
    L.linea("Contornos", (x0, y), (x1, y))
    x = x0
    while x < x1 - 0.1:
        L.linea("Cotas", (x + 3, y), (x, y - 3))
        x += 4


def apoyo(L, x, y):
    """Rodamiento: rectángulo con cruz."""
    rect(L, "Contornos", x - 2.5, y - 5, x + 2.5, y + 5)
    L.linea("Contornos", (x - 2.5, y - 5), (x + 2.5, y + 5))
    L.linea("Contornos", (x - 2.5, y + 5), (x + 2.5, y - 5))


def lamina_esquema():
    L = Lamina(1, 3, "Esquema cinemático")
    marco_y_rotulo(L, "Sin escala", metodo=False)
    t = L.t
    yb, yr, yh = 238.0, 193.0, 154.0     # ejes de botella, rodillo y husillo

    # Carro: todo lo que se traslada (la botella asoma hasta la cuchilla)
    L.polilinea("Extremas", [(36, 124), (268, 124), (268, 205), (303, 205), (303, 270),
                             (36, 270)], True)
    t(40, 263, 3.5, "Carro: se traslada con velocidad v")
    tierra(L, 30, 395, 112)
    t(34, 104, 2.5, "Base fija y guías")
    for x in (90, 230):       # patines
        L.circulo("Contornos", (x, 118), 6)
        L.linea("Contornos", (x - 18, 124), (x + 18, 124))
    L.linea("Contornos", (274, 118), (296, 118))
    L.solido("Contornos", (300, 118), (290, 119.2), (290, 116.8))
    t(275, 120.5, 3.5, "v")

    # Botella
    L.linea("Ejes", (112, yb), (312, yb))
    L.polilinea("Contornos", [(150, yb - 22), (300, yb - 22), (300, yb + 22), (150, yb + 22)])
    L.polilinea("Contornos", [(150, yb - 22), (132, yb - 8), (122, yb - 8), (122, yb + 8),
                              (132, yb + 8), (150, yb + 22)])
    t(236, yb + 25, 3.5, "Botella, Db", "c")
    flecha_giro(L, (232, yb), 9, 20, 300)
    t(246, yb - 3.5, 3.5, "nb")
    apoyo(L, 126, yb + 13)
    apoyo(L, 126, yb - 13)
    L.linea("Contornos", (126, yb - 18), (126, 124))
    t(138, yb + 20, 2.5, "Sujeción", "c")

    # Cuchilla, fija a la base
    xc = 300
    L.polilinea("Contornos", [(xc, yb - 22), (xc + 9, yb - 17), (xc + 9, yb - 27)], True)
    L.polilinea("Contornos", [(xc + 9, yb - 22), (xc + 52, yb - 22), (xc + 52, 112)])
    t(xc + 56, yb - 21, 3.5, "Cuchilla fija")
    t(xc + 56, yb - 28, 2.5, "Paso del corte: a")

    # Eje del rodillo y manivela
    L.linea("Contornos", (80, yr), (222, yr))
    L.linea("Ejes", (72, yr), (230, yr))
    rect(L, "Contornos", 196, yr - 23, 220, yr + 23)
    t(224, yr + 3, 3.5, "Rodillo, Dr")
    # Contacto en la tangencia con la botella
    xk, yk = 208, yb - 22
    L.circulo("Cotas", (xk, yk), 2.0)
    L.linea("Cotas", (xk + 1.5, yk + 1.5), (xk + 22, yk + 8))
    L.linea("Cotas", (xk + 22, yk + 8), (xk + 60, yk + 8))
    t(xk + 23, yk + 9, 2.5, "Contacto sin deslizamiento")
    L.linea("Contornos", (80, yr), (80, yr + 26))
    L.linea("Contornos", (80, yr + 26), (66, yr + 26))
    rect(L, "Contornos", 48, yr + 22, 66, yr + 30)
    t(40, yr + 34, 3.5, "Manivela (única entrada)")
    flecha_giro(L, (80, yr), 13, 200, 340, True)
    t(96, yr - 14, 3.5, "nr")

    # Las dos placas de la caja sostienen ambos ejes a distancia fija
    for x in (112, 162):
        apoyo(L, x, yr)
        apoyo(L, x, yh)
        L.linea("Contornos", (x, yr - 5), (x, yh + 5))
        L.linea("Contornos", (x, yh - 5), (x, 124))
    t(167, 136, 2.5, "Placas de la caja")

    # Par de engranajes
    xg = 142
    rect(L, "Contornos", xg - 4, yr - 13, xg + 4, yr + 13)
    rect(L, "Contornos", xg - 4, yh - 26, xg + 4, yh + 26)
    t(xg + 6, yr + 8, 3.5, "z1")
    t(xg + 6, yh - 24, 3.5, "z2")

    # Husillo y tuerca
    L.linea("Contornos", (102, yh), (372, yh))
    L.linea("Ejes", (96, yh), (380, yh))
    x = 176
    while x < 368:            # rosca como zigzag
        L.linea("Contornos", (x, yh - 2.5), (x + 3, yh + 2.5))
        L.linea("Contornos", (x + 3, yh + 2.5), (x + 6, yh - 2.5))
        x += 6
    flecha_giro(L, (200, yh), 8, 200, 340)
    t(212, yh + 5, 3.5, "nh")
    t(212, yh - 12, 3.5, "Husillo, avance L")
    rect(L, "Contornos", 310, yh - 9, 334, yh + 9)
    L.linea("Contornos", (310, yh - 9), (334, yh + 9))
    L.linea("Contornos", (310, yh + 9), (334, yh - 9))
    L.linea("Contornos", (322, yh - 9), (322, 112))
    t(310, yh + 12, 3.5, "Tuerca fija")

    # Ecuaciones
    t(32, 92, 5, "Cadena del movimiento")
    for y, a, b in ((83, "Rodadura en el contacto:", "nb = nr · Dr / Db"),
                    (76, "Engranajes:", "nh = nr / i,  con i = z2 / z1"),
                    (69, "Husillo y tuerca:", "v = L · nh")):
        t(32, y, 3.5, a)
        t(103, y, 3.5, b)
    rect(L, "Contornos", 32, 49, 204, 64)
    t(118, 53, 7, "a = L·Db / (i·Dr)", "c")
    t(32, 43, 3.5, "a: avance por vuelta de botella, sin deslizamiento.")
    t(32, 37.5, 3.5, f"Referencia: a = {formato(P.L_HUSILLO)} · {formato(P.D_B)} / "
                   f"({formato(P.I)} · {formato(P.D_R)}) = " + f"{P.PASO_A:.2f}".replace(".", ",")
                   + " mm/vuelta")
    t(32, 32, 3.5, "Rosca derecha; manivela horaria vista desde el borde abierto.")
    filas = [("Símbolo", "Magnitud", "Valor"),
             ("L", "Avance del husillo por vuelta", f"{formato(P.L_HUSILLO)} mm"),
             ("Db / Dr", "Botella / rodillo", f"{formato(P.D_B)} / {formato(P.D_R)} mm"),
             ("i", "Reducción z2 / z1", f"{formato(P.I)}  ({P.Z_2}/{P.Z_1})"),
             ("s", "Tramo cortado", f"{formato(P.RECORRIDO)} mm")]
    tabla(L, 225, 95, [24, 90, 45], filas, 2.5, 5.0)
    return L


# ------------------------------------------------------------------ lámina d
def lamina_hallazgo():
    L = Lamina(2, 4, "Hallazgo: manivela del lado del cuerpo")
    marco_y_rotulo(L, "1:2")
    pz = Z.formas()
    H, yr, zr = P.H_EJE, P.Y_R, P.Z_R
    x_tras = P.X_RODILLO[1] + 12
    # Manivela girada hacia el eje de la botella: la peor posición de la vuelta
    giro = math.degrees(math.atan2(P.Y_R, H - zr))
    centro = V(0, yr, zr)
    man = Z.manivela(x_tras, +1).rotated(centro, V(1, 0, 0), giro)
    D = Vista(L, "lateral", (0, 0, 0), 112, 100)
    D.formas([pz["Base"][0], pz["Carro"][0]], ocultas=False)
    D.formas([pz["Eje"][0], pz["Rodillo"][0], man], ocultas=False)
    r_b = P.R_B
    r_b_xy = D.pt(0, 0, H)
    L.circulo("Contornos", r_b_xy, r_b)
    D.cruz((0, 0, H), r_b)
    cman = D.pt(0, yr, zr)
    R = P.R_MANIVELA + P.R_MANGO
    L.circulo("Extremas", cman, R)
    D.cruz((0, yr, zr), P.D_R / 2)

    # Rayado: lo que barre la manivela dentro de la botella
    paso = 6.0
    k = -300.0
    while k < 300.0:
        tramos = []
        for c, r in ((r_b_xy, r_b), (cman, R)):
            # Recta y = x + k; intersección con la circunferencia
            A, B = 2.0, 2 * (k + c[0] * 0 - c[1]) - 2 * c[0] + 0
            ox, oy = c
            B = 2 * (k + r_b_xy[1] - r_b_xy[0] - oy) - 2 * ox
            C = ox * ox + (k + r_b_xy[1] - r_b_xy[0] - oy) ** 2 - r * r
            disc = B * B - 4 * A * C
            if disc <= 0:
                tramos = None
                break
            s = math.sqrt(disc)
            tramos.append(((-B - s) / (2 * A), (-B + s) / (2 * A)))
        if tramos:
            x0 = max(t_[0] for t_ in tramos)
            x1 = min(t_[1] for t_ in tramos)
            if x1 > x0:
                y_ = lambda x: x + k + r_b_xy[1] - r_b_xy[0]
                L.linea("Cotas", (x0, y_(x0)), (x1, y_(x1)))
        k += paso

    # Cotas: el hueco, la botella y el barrido
    dirx, diry = -P.Y_R / P.DIST_BR, (H - zr) / P.DIST_BR
    hueco = P.DIST_BR - r_b
    pared = (cman[0] + dirx * hueco, cman[1] + diry * hueco)
    L.cota(cman, pared, -16)
    L.cota((r_b_xy[0] - r_b, r_b_xy[1]), (r_b_xy[0] + r_b, r_b_xy[1]), 34, f"%%c{P.D_B:.0f}", "h")
    a = math.radians(-20)
    L.cota(cman, (cman[0] + R * math.cos(a), cman[1] + R * math.sin(a)), 6,
           f"R{formato(R)}")

    # Notas
    x, y = 232.0, 270.0
    t = L.t
    t(x, y, 5, "Qué muestra")
    y -= 9
    res = json.load(open(os.path.join(CARPETA, "resultados.json"), encoding="utf-8"))
    vol = res["manivela"]["sobre_el_cuerpo_como_imagen_IA"]
    rmax = res["manivela"]["radio_max_sobre_el_cuerpo_mm"]
    for s in (
        "Vista desde el borde abierto, con la manivela",
        "del lado del cuerpo de la botella.",
        "",
        f"Del eje del rodillo a la pared hay {formato(hueco)} mm (Dr / 2).",
        f"La manivela de radio {formato(P.R_MANIVELA)} mm, con mango de radio",
        f"{formato(P.R_MANGO)} mm, barre una circunferencia de radio {formato(R)} mm.",
        "",
        "Rayado: lo que barre dentro de la botella. En todo",
        "el ancho barrido son unos " + str(round(vol / 1000)) + " cm3.",
        "",
        f"De este lado, el radio no puede superar {formato(rmax)} mm.",
    ):
        if s:
            t(x, y, 3.5, s)
        y -= 7
    y -= 8
    t(x, y, 5, "Cómo se evita en el modelo")
    y -= 9
    for s in ("El eje se prolonga más allá del soporte del cuello",
              f"y la manivela queda detrás: {formato(P.X_EJE[1] - P.X_EJE[0])} mm de eje, sin choque.",
              "",
              "No es una decisión del grupo: es una opción más,",
              "junto con un reenvío u otra posición de entrada."):
        if s:
            t(x, y, 3.5, s)
        y -= 7
    L.t(112, 232, 3.5, "Vista desde el borde abierto", "c")
    return L


# -------------------------------------------------------------------------- main
def superposiciones(L):
    """Pares de textos que se pisan, y textos fuera del marco."""
    malos = []
    E = L.E
    r = L.rect
    m = 0.15 * E
    for i in range(len(r)):
        a = r[i]
        if a[0] < 25 * E or a[1] < 10 * E or a[2] > 410 * E or a[3] > 287 * E:
            malos.append(f"fuera del marco: {a[4]}")
        for b in r[i + 1:]:
            if a[0] < b[2] - m and b[0] < a[2] - m and a[1] < b[3] - m and b[1] < a[3] - m:
                malos.append(f"{a[4]} / {b[4]}")
    return malos


def main():
    os.makedirs(SALIDA, exist_ok=True)
    intermedio = os.path.join(CARPETA, "build", "planos_json")
    os.makedirs(intermedio, exist_ok=True)
    laminas = (("01_conjunto", lamina_conjunto), ("02_despiece", lamina_despiece),
               ("03_esquema_cinematico", lamina_esquema), ("04_hallazgo_manivela", lamina_hallazgo))
    informe, ok = {}, True
    for nombre, f in laminas:
        L = f()
        L.guardar(os.path.join(intermedio, nombre + ".json"), 420, 297)
        malos = superposiciones(L)
        ok = ok and not malos
        informe[nombre] = {"escala": L.E, "entidades": len(L.ops),
                           "cotas": sum(1 for o in L.ops if o[0] == "d"),
                           "textos_superpuestos": malos}
    ruta = os.path.join(CARPETA, "resultados.json")
    with open(ruta, encoding="utf-8") as fh:
        todo = json.load(fh)
    todo["planos"] = informe
    with open(ruta, "w", encoding="utf-8") as fh:
        json.dump(todo, fh, ensure_ascii=False, indent=1)
    return ok


codigo = 1
try:
    codigo = 0 if main() else 1
except Exception:
    with open(os.path.join(CARPETA, "build_error.txt"), "a") as fh:
        fh.write(traceback.format_exc())
finally:
    sys.stdout.flush()
    os._exit(codigo)
