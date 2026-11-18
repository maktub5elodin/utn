# -*- coding: utf-8 -*-
"""
Planos 2D del modelo 2.0, generados desde el modelo 3D (proyección con líneas ocultas
de TechDraw), con el método del modelo 1. Si cambia parametros.py, `make` los regenera.
    ~/Aplicaciones/FreeCAD.AppImage freecadcmd planos.py
Deja un JSON por lámina en build/planos_json/; dxf.py escribe los DXF con ezdxf.

Cada lámina está en mm reales: el marco A3 se agranda según la escala (1:E), así
medir sobre el DXF da la medida de la pieza. Termina con error si dos textos se
superponen o si alguno se sale del marco.

Juego: 01 conjunto (1:2,5) · 02 cabezal de corte (1:1, detalle 5:1) ·
03 carrete, manivela y zócalo (1:1) · 04 esquema de funcionamiento (sin escala).
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
FECHA = "19/11/2026"
LEYENDA = "Prototipo: piezas impresas en PLA; medidas de diseño"
SALIDA = os.path.join(CARPETA, "planos")
LAMINAS_DEL_JUEGO = 4

# Filas de la matriz: u (derecha del papel), v (arriba), w (hacia el observador)
MAPAS = {
    "frente": ((-1, 0, 0), (0, 0, 1), (0, 1, 0)),     # desde +Y, el lado de la cuchilla
    "planta": ((-1, 0, 0), (0, -1, 0), (0, 0, 1)),    # método E: debajo de la frontal
    "lateral": ((0, 1, 0), (0, 0, 1), (1, 0, 0)),     # método E: desde +X, a la derecha
    "largo": ((1, 0, 0), (0, 0, 1), (0, -1, 0)),      # pieza suelta desde -Y, X a la derecha
    "arriba": ((1, 0, 0), (0, 1, 0), (0, 0, 1)),      # pieza suelta desde arriba (E: abajo de "largo")
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

    def documento(self):
        return (60, "LÁMINA", f"{self.numero} de {LAMINAS_DEL_JUEGO}")

    def pp(self, x, y):
        """De mm de papel a coordenadas del dibujo."""
        return x * self.E, y * self.E

    def t(self, x, y, h, s, alin="i", capa="Texto", rot=0.0):
        X, Y = self.pp(x, y)
        self.texto(capa, X, Y, h, s, alin, rot)

    def rectangulo(self, capa, a, b):
        """Rectángulo entre dos esquinas, en coordenadas del dibujo."""
        self.polilinea(capa, [(a[0], a[1]), (b[0], a[1]), (b[0], b[1]), (a[0], b[1])], True)

    def relleno(self, capa, a, b):
        """Rectángulo ennegrecido (sección delgada, ISO 128-50)."""
        self.solido(capa, (a[0], a[1]), (b[0], a[1]), (b[0], b[1]))
        self.solido(capa, (a[0], a[1]), (b[0], b[1]), (a[0], b[1]))

    def rayado(self, a, b, paso=2.5, sentido=1):
        """Rayado de sección a 45° (sentido 1) o 135° (-1) dentro del rectángulo a-b.
        paso en mm de papel. Las líneas de una misma familia quedan alineadas entre
        rectángulos vecinos: el rayado de una pieza partida en varios se ve continuo."""
        E = self.E
        paso *= E
        x0, x1 = sorted((a[0], b[0]))
        y0, y1 = sorted((a[1], b[1]))
        ks = [y - sentido * x for x in (x0, x1) for y in (y0, y1)]
        k = math.floor(min(ks) / paso) * paso
        while k <= max(ks):
            pts = set()
            for x in (x0, x1):
                y = sentido * x + k
                if y0 - 1e-9 <= y <= y1 + 1e-9:
                    pts.add((round(x, 6), round(y, 6)))
            for y in (y0, y1):
                x = (y - k) / sentido
                if x0 - 1e-9 <= x <= x1 + 1e-9:
                    pts.add((round(x, 6), round(y, 6)))
            pts = sorted(pts)
            if len(pts) >= 2 and math.hypot(pts[-1][0] - pts[0][0], pts[-1][1] - pts[0][1]) > 0.05:
                self.linea("Cotas", pts[0], pts[-1])
            k += paso

    def guia(self, a, b, s, h=2.5, alin="i"):
        """Línea de referencia de a (punto de la pieza) a b (codo), con texto a la derecha
        o izquierda del codo, en coordenadas del dibujo."""
        E = self.E
        self.linea("Cotas", a, b)
        self.circulo("Cotas", a, 0.3 * E)
        w = 1.0 * E
        if alin == "i":
            self.linea("Cotas", b, (b[0] + w, b[1]))
            self.texto("Texto", b[0] + w + 0.8 * E, b[1] + 0.8 * E, h, s, "i")
        else:
            self.linea("Cotas", b, (b[0] - w, b[1]))
            self.texto("Texto", b[0] - w - 0.8 * E, b[1] + 0.8 * E, h, s, "d")


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
ROT_X0, ROT_X1 = 230.0, 410.0   # bloque de 180 × 40 mm, abajo a la derecha
ROT_Y0, ROT_Y1 = 10.0, 50.0
SUBTITULO = "Cortadora manual de botellas PET - Prototipo"


def marco_y_rotulo(L, escala, metodo=True):
    """Rótulo de cursada: celdas con rótulo chico y valor más grande."""
    pp = L.pp
    L.polilinea("Texto", [pp(0, 0), pp(420, 0), pp(420, 297), pp(0, 297)], True)
    # Sin marcas de centrado en el medio de cada lado: criterio de los técnicos que
    # revisaron los planos (no van y se ven feas).
    L.polilinea("Marco", [pp(25, 10), pp(410, 10), pp(410, 287), pp(25, 287)], True)
    x0, x1, y0, y1 = ROT_X0, ROT_X1, ROT_Y0, ROT_Y1
    L.polilinea("Marco", [pp(x0, y0), pp(x1, y0), pp(x1, y1), pp(x0, y1)], True)
    ya, yb = y0 + 11, y0 + 22
    L.linea("Texto", pp(x0, ya), pp(x1, ya))
    L.linea("Texto", pp(x0, yb), pp(x1, yb))

    def fila(y_inf, y_sup, celdas):
        x = x0
        for ancho, rotulo, valor in celdas:
            if x > x0:
                L.linea("Texto", pp(x, y_inf), pp(x, y_sup))
            L.t(x + 1.5, y_sup - 3.4, 2.5, rotulo)
            L.t(x + 1.5, y_inf + 1.8, 3.5, valor)
            x += ancho
    fila(y0, ya, ((60, "ESCALA", escala), (60, "FECHA", FECHA), L.documento()))
    fila(ya, yb, ((114, "ASIGNATURA", "UTN FRBA - Ingeniería Mecánica I"),
                  (66, "CURSO", "S1091 - Grupo 1")))
    if metodo:   # símbolo del método E: el cono se mira desde el lado angosto
        xs, yc = x0 + 36, y0 + 4
        L.polilinea("Contornos", [pp(xs, yc - 1.2), pp(xs + 7, yc - 2.6), pp(xs + 7, yc + 2.6),
                                  pp(xs, yc + 1.2)], True)
        L.circulo("Contornos", pp(xs + 12.5, yc), 2.6 * L.E)
        L.circulo("Contornos", pp(xs + 12.5, yc), 1.2 * L.E)
    L.t(x0 + 1.5, y1 - 3.4, 2.5, "TÍTULO")
    L.t((x0 + x1) / 2, yb + 8, 5, L.titulo, "c")
    L.t((x0 + x1) / 2, yb + 2.4, 3.5, SUBTITULO, "c")
    L.t(x1 - 1, y1 + 1.2, 2.5, LEYENDA, "d")


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
    L.circulo("Cotas", ancla, 0.3 * E)
    L.texto("Texto", cx, cy - 1.75 * E, 3.5, str(n), "c")


def flecha(L, punta, desde, largo=3.5, ancho=0.45):
    """Punta de flecha rellena en `punta`, viniendo desde `desde` (mm de papel)."""
    E = L.E
    dx, dy = punta[0] - desde[0], punta[1] - desde[1]
    d = math.hypot(dx, dy) or 1.0
    ux, uy = dx / d, dy / d
    L.solido("Cotas", punta, (punta[0] - ux * largo * E + uy * ancho * E, punta[1] - uy * largo * E - ux * ancho * E),
             (punta[0] - ux * largo * E - uy * ancho * E, punta[1] - uy * largo * E + ux * ancho * E))


def flecha_giro(L, c, r, a0, a1, horaria=False):
    """Arco con punta, para indicar un sentido de giro (coordenadas del dibujo)."""
    L.arco("Cotas", c, r, a0, a1)
    a = math.radians(a0 if horaria else a1)
    px, py = c[0] + r * math.cos(a), c[1] + r * math.sin(a)
    t = -1 if horaria else 1
    tx, ty = -math.sin(a) * t, math.cos(a) * t
    flecha(L, (px, py), (px - tx, py - ty))


# ------------------------------------------------------------ formas auxiliares
def botella_simple(s=0.0):
    """Botella como sólido de revolución, sin pared ni hélice: para la proyección."""
    largo = P.ALTO_BOTELLA - s
    zt = P.z_superior_botella(s)
    xs = [0.0, P.X_CUELLO_FIN] + [P.X_CUELLO_FIN + (P.X_HOMBRO_FIN - P.X_CUELLO_FIN) * k / 12
                                  for k in range(1, 13)] + [largo]
    perfil = [(0.0, zt)] + [(P.radio_botella(x), zt - x) for x in xs] + [(0.0, zt - largo)]
    return Z.revolucion(perfil)


def xy_polar(r, a):
    return r * math.cos(math.radians(a)), r * math.sin(math.radians(a))


XC, YC = P.X_CARRETE, P.Y_CARRETE
DIAM = "%%c"


def d_(v):
    return DIAM + formato(v)


# ------------------------------------------------------------------ lámina 1
LISTA = [  # n.°, denominación, cantidad, material u observación
    (1, "Base", 1, "MDF 18, 345 x 200"),
    (2, "Zócalo de la varilla", 1, "PLA"),
    (3, "Varilla lisa", 1, "Acero, %%c8 x 400"),
    (4, "Prisionero M3 x 16 y tuerca", 1, "Comercial"),
    (5, "Taco del cabezal", 1, "MDF 18, 2 recortes"),
    (6, "Placa del cabezal", 1, "PLA"),
    (7, "Chapita de apoyo", 1, "Galga 0,5, 18 x 12,7"),
    (8, "Labio exterior", 1, "PLA"),
    (9, "Calce (ancho de tira w)", 1, "PLA, juego 7 a 10"),
    (10, "Hoja", 1, "Trincheta de 18"),
    (11, "Pisador", 1, "PLA"),
    (12, "Tornillo M3 x 25 y tuerca", 2, "Comercial"),
    (13, "Ojal", 1, "PLA"),
    (14, "Torre del carrete", 1, "PLA"),
    (15, "Rodamiento 608ZZ", 2, "8 x 22 x 7"),
    (16, "Eje del carrete, M8 x 60", 1, "Con 2 arandelas"),
    (17, "Carrete inferior", 1, "PLA, tuerca M8 caut."),
    (18, "Carrete superior", 1, "PLA"),
    (19, "Manivela", 1, "PLA, tuerca M8 caut."),
    (20, f"Mango y tornillo M5 x {P.TORNILLO_MANGO_L:.0f} Allen", 1, "PLA, tuerca M5 aut."),
    (21, "Botella y tapa perforada", 1, "PET, tapa a %%c9"),
    (22, "Vaso de lastre (opcional)", 1, "PLA"),
    (23, "Tornillo para madera 3,5 x 16", 14, "Comercial"),
    (24, "Tornillo 3,5 x 45 fresado", 2, "Taco, desde abajo"),
]
LISTA_X, LISTA_ANCHOS = 294.0, [9, 58, 10, 39]


def lista_piezas(L, x, y):
    """Se lee hacia arriba, desde el encabezado."""
    filas = [(a, b, c, d) for a, b, c, d in reversed(LISTA)]
    filas.append(("N.°", "DENOMINACIÓN", "CANT.", "MATERIAL / OBS."))
    fila = 5.3
    tabla(L, x, y + fila * len(filas), LISTA_ANCHOS, filas, 2.5, fila)


def lamina_conjunto():
    L = Lamina(2.5, 1, "Plano de conjunto")
    marco_y_rotulo(L, "1:2,5")
    pz = Z.conjunto(0.0)
    formas = [d["forma"] for n, d in pz.items() if n not in ("Botella", "Sargento")]
    formas.append(botella_simple(0.0))
    zb = -P.MDF[2]
    x0, y0 = P.MDF_ORIGEN
    x1, y1 = x0 + P.MDF[0], y0 + P.MDF[1]
    x_mango = XC + P.R_MANIVELA + P.MANGO_R
    X_F, Y_F = 44.0 + x_mango / 2.5, 117.2     # eje de la botella y cara del MDF, en papel

    # --- Frontal, desde el lado de la cuchilla
    F = Vista(L, "frente", (0, 0, 0), X_F, Y_F)
    F.formas(formas)
    F.eje((0, 0, zb - 8), (0, 0, P.ZOCALO_FONDO + P.VARILLA_L + 8))
    F.eje((XC, YC, zb - 8), (XC, YC, P.Z_MANIVELA + P.CUBO_ALTO + 8))
    F.eje((x_mango - P.MANGO_R, YC, P.Z_MANIVELA - 8), (x_mango - P.MANGO_R, YC, 132))
    L.t(X_F, 281.5, 3.5, "Vista frontal", "c")
    L.cota(F.pt(P.CAB_X[0], 104, 0), F.pt(P.CAB_X[0], 104, P.Z_PISO), -8, direc="v")
    L.cota(F.pt(x0, 104, zb), F.pt(x0, 104, 0), -6, direc="v")

    # --- Superior (método E: debajo de la frontal; el lado de la cuchilla queda abajo)
    S = Vista(L, "planta", (0, 0, 0), X_F, 70.0)
    S.formas(formas)
    S.cruz((0, 0, 0), P.R_B)
    S.cruz((XC, YC, 0), P.R_DISCO)
    S.eje((XC, YC, 0), (x_mango + 4, YC, 0))
    L.t(X_F, 104.5, 3.5, "Vista superior", "c")
    L.cota(S.pt(x0, y1, 0), S.pt(x1, y1, 0), -6, direc="h")
    L.cota(S.pt(x0, y0, 0), S.pt(x0, y1, 0), -6, direc="v")
    L.cota(S.pt(0, 0, 0), S.pt(XC, YC, 0), 25, direc="h")
    L.cota(S.pt(XC, YC, 0), S.pt(XC + P.R_MANIVELA, YC, 0), 18, direc="h")

    # --- Lateral izquierda (método E: desde el lado del carrete, a la derecha)
    Lat = Vista(L, "lateral", (0, 0, 0), 238.0, Y_F)
    Lat.formas(formas)
    Lat.eje((0, 0, zb - 8), (0, 0, P.ZOCALO_FONDO + P.VARILLA_L + 8))
    Lat.eje((XC, YC, zb - 8), (XC, YC, P.Z_MANIVELA + P.CUBO_ALTO + 8))
    L.t(248, 281.5, 3.5, "Vista lateral izquierda", "c")

    # --- Lista de piezas y notas
    lista_piezas(L, LISTA_X, ROT_Y1 + 5)
    for k, s in enumerate(("Botella al inicio del corte (s = 0).",
                           "El extremo libre de la base se fija a la",
                           "mesa con una prensa tipo sargento (no se",
                           "dibuja). Tornillos para madera: 3 del zócalo,",
                           "4 de la placa, 2 del labio, 2 del ojal y 3",
                           "de la torre.")):
        L.t(208, 96 - 5 * k, 2.5, s)

    # --- Globos
    g = lambda n, v, p, dx, dy: globo(L, n, v.pt(*p), dx, dy)
    g(21, F, (-P.R_B, 0, 230), 14, 6)
    g(3, F, (-P.VARILLA_D / 2, 0, 388), 14, 4)
    g(22, F, (-P.LASTRE_R, 0, 352), 14, 4)
    g(5, F, (P.CAB_X[0], 104, 30), 14, 0)        # arriba del 42 de la altura de la guía
    g(6, F, (P.CAB_X[0], 104, 39), 14, 9)
    g(8, F, (-20, 49, 57), 16, 14)
    g(9, F, (P.CALCE_X[1], 97, 46), -16, 14)
    g(11, F, (P.CALCE_X[1], 97, 54), -14, 20)
    g(13, F, (P.X_OJAL, 49, 52), -14, 4)
    g(14, F, (XC + P.TORRE_R, YC, 22), -12, -6)
    g(15, F, (XC + P.D_608 / 2, YC, 33), 14, -6)
    g(17, F, (XC + P.R_DISCO, YC, 39), -14, -4)
    g(18, F, (XC + P.R_DISCO, YC, 55), 6, 16)
    g(19, F, (XC + 40, YC, P.Z_BRAZO_SUP), 0, 20)
    g(16, F, (XC, YC, 36.8), 16, 10)
    g(20, F, (x_mango, YC, 100), -8, 10)
    g(1, S, (x0, 100, 0), 10, 0)
    g(2, S, (-P.ZOCALO_R, 0, 28), 22, 10)
    g(4, S, (-22, 0, 14), 22, -6)
    g(12, S, (P.TORNILLOS_HOJA[1][0], 80, 59.4), 22, -12)
    g(10, S, (9, 47, 51.4), 14, -10)
    g(7, S, (5, 47.5, 41.9), 24, -16)
    g(23, S, (58, 43.9, 5), 0, -12)
    g(24, Lat, (36, 68, -9), 14, -6)
    return L


# ------------------------------------------------------------------ lámina 2
def plano_de_corte(L, V_, x_plano, y_a, y_b, letra="A"):
    """Traza del plano de corte en una vista 'arriba': trazo largo y punto, con flechas que
    miran hacia +X (el observador está en -X) y la letra en los extremos."""
    E = L.E
    a, b = V_.pt(x_plano, y_a, 0), V_.pt(x_plano, y_b, 0)
    L.linea("Ejes", a, b)
    for p in (a, b):
        L.linea("Contornos", p, (p[0], p[1] + (3 * E if p is b else -3 * E)))
        L.linea("Cotas", p, (p[0] + 6 * E, p[1]))
        flecha(L, (p[0] + 6 * E, p[1]), p)
        L.texto("Texto", p[0] + 7.5 * E, p[1] - 1.75 * E, 3.5, letra)


def lamina_cabezal():
    L = Lamina(1, 2, "Cabezal de corte")
    marco_y_rotulo(L, "1:1 (detalle 4:1)")
    pz = Z.conjunto(0.0)
    zb, zg = P.TACO_ALTO, P.Z_PISO
    r_int = P.R_B - P.PARED - P.HOLG_RANURA
    r_ext = P.R_B + P.HOLG_RANURA
    e9 = Z.espesor_calce(P.W)

    # --- Pieza 6: placa del cabezal. Frente arriba y planta abajo (método E).
    L.t(32, 283, 3.5, "Pieza 6: placa del cabezal")
    placa = pz["Cabezal"]["forma"]
    Pf = Vista(L, "largo", (0, 0, zb), 70, 266)
    Pf.formas([placa], ocultas=False)
    L.cota(Pf.pt(P.CAB_X[1], 0, zg), Pf.pt(P.CAB_X[1], 0, zb), -6, direc="v")
    L.cota(Pf.pt(P.CAB_X[0], 0, zg + P.ALTO_LABIO_INT), Pf.pt(P.CAB_X[0], 0, zg), 6, direc="v")
    L.t(122, 268, 2.5, "Se imprime con la cara de abajo en la cama")
    Pa = Vista(L, "arriba", (0, 0, 0), 70, 150)
    Pa.formas([placa], ocultas=False)
    Pa.cruz((0, 0, 0), 3)
    L.arco("Ejes", Pa.pt(0, 0, 0), P.R_B, 62, 140)        # la botella, como referencia
    L.cota(Pa.pt(P.CAB_X[0], P.CAB_Y[0], zg), Pa.pt(P.CAB_X[1], P.CAB_Y[0], zg), -14, direc="h")
    L.cota(Pa.pt(P.CAB_X[0], P.CAB_Y[0], zg), Pa.pt(P.CAB_X[0], P.CAB_Y[1], zg), 6, direc="v")
    L.cota(Pa.pt(P.CAB_X[0], 0, 0), Pa.pt(P.CAB_X[0], P.CAB_Y[0], zg), 6, direc="v")
    L.cota(Pa.pt(0, 0, 0), Pa.pt(P.CAB_X[0], 0, 0), -6, direc="h")
    L.cota(Pa.pt(P.TORNILLOS_HOJA[0][0], 80, zg), Pa.pt(P.TORNILLOS_HOJA[1][0], 80, zg), 30,
           direc="h")
    plano_de_corte(L, Pa, -3.0, 20, 106)
    L.guia(Pa.pt(*xy_polar(41.7, 112), zg), Pa.pt(-26, -14, 0),
           "Labio interior R40 / R43,45, de 80%%d a 125%%d")
    L.guia(Pa.pt(*xy_polar(52, 108), zg), Pa.pt(-26, -22, 0),
           "2 agujeros %%c3,9 para los tornillos del labio exterior")
    L.guia(Pa.pt(P.TORNILLOS_CABEZAL[3][0] - 1.2, 97.2, zg), Pa.pt(54, 102, zg),
           "4 agujeros %%c3,9 con caja %%c7,6: tornillos al taco")
    L.guia(Pa.pt(P.TORNILLOS_HOJA[1][0] + 1.2, 81.2, zg), Pa.pt(54, 84, zg),
           "2 agujeros %%c3,4 con tuerca M3 cautiva por abajo")
    L.guia(Pa.pt(6, P.CHAPITA_Y[1] - 1, zg), Pa.pt(54, 70, zg),
           f"Rebaje de la chapita {formato(P.CHAPITA_LARGO + 2 * P.HOLG_CHAPITA)} x "
           f"{formato(P.CHAPITA_ANCHO + 1.5 * P.HOLG_CHAPITA)}, {formato(P.POZO_ALTO)} de profundidad")

    # --- Piezas 9 y 11: calce y pisador, abajo a la izquierda
    L.t(32, 112, 3.5, "Piezas 9 y 11: calce y pisador")
    calce = pz["Calce"]["forma"]
    Cf = Vista(L, "largo", (P.CALCE_X[0], 0, zg), 50, 96)
    Cf.formas([calce], ocultas=False)
    L.cota(Cf.pt(P.CALCE_X[1], 0, zg + e9), Cf.pt(P.CALCE_X[1], 0, zg), -6, formato(e9), "v")
    Ca = Vista(L, "arriba", (P.CALCE_X[0], P.CALCE_Y[0], zg), 50, 40)
    Ca.formas([calce], ocultas=False)
    L.cota(Ca.pt(P.CALCE_X[0], P.CALCE_Y[0], zg), Ca.pt(P.CALCE_X[1], P.CALCE_Y[0], zg), -6, direc="h")
    L.cota(Ca.pt(P.CALCE_X[1], P.CALCE_Y[0], zg), Ca.pt(P.CALCE_X[1], P.CALCE_Y[1], zg), -6, direc="v")
    L.cota(Ca.pt(P.TORNILLOS_HOJA[0][0], 80, zg), Ca.pt(P.TORNILLOS_HOJA[1][0], 80, zg), 22, direc="h")
    for k, s in enumerate(("Calces: uno por ancho de tira w,",
                           "espesor w - 0,1: 6,9 / 7,9 / 8,9 / 9,9",
                           "para w = 7, 8, 9 y 10 mm.",
                           "Pisador (11): mismo contorno y",
                           "agujeros, 5 de espesor.",
                           "Agujeros %%c3,4, tornillos M3 x 25.")):
        L.t(108, 78 - 5 * k, 2.5, s)

    # --- Pieza 8: labio exterior
    L.t(150, 166, 3.5, "Pieza 8: labio exterior")
    labio = pz["LabioExterior"]["forma"]
    Lf = Vista(L, "largo", (0, 0, zg), 200, 142)
    Lf.formas([labio], ocultas=False)
    L.cota(Lf.pt(-29, 0, zg), Lf.pt(-29, 0, zg + P.LABIO_PIE_ESP), 8, direc="v")
    L.cota(Lf.pt(-29, 0, zg), Lf.pt(-29, 0, zg + P.ALTO_LABIO_EXT), 16, direc="v")
    La = Vista(L, "arriba", (0, 0, 0), 200, 70)
    La.formas([labio], ocultas=False)
    L.arco("Ejes", La.pt(0, 0, 0), P.R_B, 86, 124)
    L.linea("Ejes", La.pt(0, P.R_B - 6, 0), La.pt(0, 60, 0))
    L.cota(La.pt(0, P.R_B, 0), La.pt(0, r_ext + P.LABIO_ESP, 0), -18, direc="v")
    for k, s in enumerate((f"Arco de R{formato(r_ext)} a R{formato(r_ext + P.LABIO_ESP)}, de 90,8%%d a 125%%d:",
                           "termina 0,6 antes del filo.",
                           f"Pie R{formato(P.LABIO_PIE_R)}, {formato(P.LABIO_PIE_ESP)} de alto, de 103%%d a 125%%d,",
                           "con 2 agujeros %%c3,9. Retiene la chapita.")):
        L.t(150, 106 - 5 * k, 2.5, s)

    # --- Detalle A: corte por la ranura, 3 mm antes del filo, 4:1
    K = 4.0
    Y0, Z0, X0P, Y0P = 38.0, 34.0, 292.0, 62.0
    Yw, Zw = 57.0, 60.0

    def dp(y, z):
        return L.pp(X0P + (y - Y0) * K, Y0P + (z - Z0) * K)

    def izq(y, z, s, dz=0.0):
        L.guia(dp(y, z), L.pp(X0P - 20, Y0P + (z + dz - Z0) * K), s, 2.5, "d")

    def der(y, z, s, dz=0.0):
        L.guia(dp(y, z), L.pp(X0P + (Yw - Y0) * K + 6, Y0P + (z + dz - Z0) * K), s, 2.5, "i")

    y_top = Y0P + (Zw - Z0) * K
    L.t(X0P - 60, y_top + 16, 3.5, "Detalle A: corte por la ranura, 3 mm antes del filo (4:1)")
    L.t(X0P - 60, y_top + 10, 2.5, "La hoja (10), a 3 mm detrás del plano, se ve sin cortar. Rebaje de la chapita")
    L.t(X0P - 60, y_top + 5.5, 2.5, "abierto hacia arriba: la retienen el labio exterior y el calce.")
    zc = P.Z_GUIA                 # cara de la chapita
    zp = zg - P.POZO_ALTO         # fondo del rebaje
    y_pz0, y_pz1 = P.CHAPITA_Y[0] - P.HOLG_CHAPITA / 2, P.CHAPITA_Y[1] + P.HOLG_CHAPITA
    contorno = [(Y0, zb), (Yw, zb), (Yw, zg), (y_pz1, zg), (y_pz1, zp), (y_pz0, zp),
                (y_pz0, zg - P.RANURA_PROF), (r_int, zg - P.RANURA_PROF), (r_int, zg + P.ALTO_LABIO_INT),
                (P.LABIO_INT_R0, zg + P.ALTO_LABIO_INT), (P.LABIO_INT_R0, zg), (Y0, zg)]
    L.polilinea("Contornos", [dp(*q) for q in contorno], True)
    for a, b in (((Y0, zb), (y_pz0, zp)), ((y_pz0, zb), (y_pz1, zp)), ((y_pz1, zb), (Yw, zg)),
                 ((P.LABIO_INT_R0, zp), (r_int, zg + P.ALTO_LABIO_INT)), ((Y0, zp), (P.LABIO_INT_R0, zg))):
        L.rayado(dp(*a), dp(*b), 2.5, 1)
    L.rectangulo("Contornos", dp(Y0, Z0), dp(Yw, zb))                 # taco de MDF
    L.rayado(dp(Y0, Z0), dp(Yw, zb), 4.0, -1)
    L.relleno("Contornos", dp(P.CHAPITA_Y[0], zc - P.CHAPITA_ESP), dp(P.CHAPITA_Y[1], zc))
    L.rectangulo("Contornos", dp(r_ext, zg), dp(r_ext + P.LABIO_ESP, zg + P.ALTO_LABIO_EXT))
    L.rayado(dp(r_ext, zg), dp(r_ext + P.LABIO_ESP, zg + P.ALTO_LABIO_EXT), 2.5, -1)
    z_h = Z.z_hoja()
    L.rectangulo("Contornos", dp(P.CALCE_Y[0], zg), dp(Yw, z_h))
    L.rayado(dp(P.CALCE_Y[0], zg), dp(Yw, z_h), 2.5, -1)
    L.rectangulo("Contornos", dp(P.CALCE_Y[0], z_h + P.HOJA[1]), dp(Yw, z_h + P.HOJA[1] + P.PISADOR_ESP))
    L.rayado(dp(P.CALCE_Y[0], z_h + P.HOJA[1]), dp(Yw, z_h + P.HOJA[1] + P.PISADOR_ESP), 2.5, 1)
    L.polilinea("Contornos", [dp(Yw, z_h), dp(P.HOJA_Y0, z_h), dp(P.HOJA_Y0, z_h + P.HOJA[1]),
                              dp(Yw, z_h + P.HOJA[1])])
    yb0 = P.R_B - P.PARED
    L.polilinea("Extremas", [dp(yb0, Zw - 1), dp(yb0, zc), dp(P.R_B, zc), dp(P.R_B, Zw - 1)])
    # cotas con el texto escrito: el dibujo está a 4:1
    L.cota(dp(r_int, zg + P.ALTO_LABIO_EXT), dp(r_ext, zg + P.ALTO_LABIO_EXT), 4, f"{r_ext - r_int:.2f}".replace(".", ","), "h")
    L.cota(dp(P.LABIO_INT_R0, zg), dp(P.LABIO_INT_R0, zg + P.ALTO_LABIO_INT), 8, formato(P.ALTO_LABIO_INT), "v")
    L.cota(dp(Y0, zb), dp(Y0, zg), 8, formato(zg - zb), "v")
    y_w = (r_ext + P.LABIO_ESP + P.CALCE_Y[0]) / 2       # en el hueco entre el labio y el calce
    L.cota(dp(y_w, zc), dp(y_w, z_h), 0, f"w = {formato(P.W)}", "v")
    izq(41.7, zg + 5.5, "Labio interior", 4.5)
    izq(yb0, Zw - 2, "Pared de la botella")
    der(r_ext + P.LABIO_ESP - 0.5, zg + 15, "Labio ext. (8)")
    der(Yw - 0.5, z_h + P.HOJA[1] + 3.5, "Pisador (11)")
    der(Yw - 0.5, z_h + 0.25, "Hoja (10)", 1.4)
    der(Yw - 0.5, zg + 4, "Calce (9)")
    der(P.CHAPITA_Y[1] - 0.3, zc - 0.25, "Chapita (7)", -1.2)
    der(Yw - 0.3, zb + 2, "Placa (6)")
    der(Yw - 0.3, Z0 + 1, "Taco MDF (5)")
    return L


# ------------------------------------------------------------------ lámina 3
def lamina_carrete():
    L = Lamina(1, 3, "Carrete, manivela y zócalo")
    marco_y_rotulo(L, "1:1")
    pz = Z.conjunto(0.0)

    # --- Pieza 14: torre
    L.t(32, 277, 3.5, "Pieza 14: torre del carrete")
    torre = pz["Torre"]["forma"]
    rb, eb = P.TORRE_BRIDA
    Ta = Vista(L, "arriba", (XC, YC, 0), 75, 220)
    Ta.formas([torre], ocultas=False)
    Ta.cruz((XC, YC, 0), rb)
    L.circulo("Ejes", Ta.pt(XC, YC, 0), P.TORRE_TORNILLOS_R)
    L.guia(Ta.pt(*Z.tornillos_torre()[0], 0), Ta.pt(XC + 36, YC + 36, 0), f"3 agujeros %%c3,9 en R{formato(P.TORRE_TORNILLOS_R)}")
    L.cota(Ta.pt(XC - P.D_608_ALOJ / 2, YC, 0), Ta.pt(XC + P.D_608_ALOJ / 2, YC, 0), 8, d_(P.D_608_ALOJ), "h")
    Tf = Vista(L, "largo", (XC, YC, 0), 75, 150)
    Tf.formas([torre])
    Tf.eje((XC, YC, -6), (XC, YC, P.TORRE_ALTO + 6))
    L.cota(Tf.pt(XC - rb, YC, 0), Tf.pt(XC + rb, YC, 0), -8, d_(2 * rb), "h")
    L.cota(Tf.pt(XC - P.TORRE_R, YC, P.TORRE_ALTO), Tf.pt(XC + P.TORRE_R, YC, P.TORRE_ALTO), 6, d_(2 * P.TORRE_R), "h")
    L.cota(Tf.pt(XC + rb, YC, 0), Tf.pt(XC + rb, YC, eb), -8, direc="v")
    L.cota(Tf.pt(XC + rb, YC, 0), Tf.pt(XC + rb, YC, P.TORRE_ALTO), -16, direc="v")
    L.cota(Tf.pt(XC - rb, YC, 0), Tf.pt(XC - rb, YC, P.TORRE_CAVIDAD[1]), 8, direc="v")
    L.cota(Tf.pt(XC - P.TORRE_CAVIDAD[0], YC, 0), Tf.pt(XC + P.TORRE_CAVIDAD[0], YC, 0), -16, d_(2 * P.TORRE_CAVIDAD[0]), "h")
    L.t(32, 128, 2.5, "Dos 608ZZ a presión; cavidad para la cabeza del M8.")

    # --- Piezas 17 y 18: carrete
    L.t(135, 277, 3.5, "Piezas 17 y 18: carrete")
    carrete = pz["CarreteInferior"]["forma"]
    Ra = Vista(L, "arriba", (XC, YC, 0), 185, 220)
    Ra.formas([carrete], ocultas=False)
    Ra.cruz((XC, YC, 0), P.R_DISCO)
    L.cota(Ra.pt(XC - P.R_NUCLEO, YC, 0), Ra.pt(XC + P.R_NUCLEO, YC, 0), 8, d_(2 * P.R_NUCLEO), "h")
    L.guia(Ra.pt(XC + 0.6, YC - P.R_NUCLEO + 2, 0), Ra.pt(XC + 42, YC - 52, 0), f"Ranura 1,2 x {formato(P.RANURA_ENGANCHE)}: engancha la tira")
    L.guia(Ra.pt(XC - 3.2, YC + 2.7, 0), Ra.pt(XC - 40, YC + 48, 0), f"Hexágono {formato(P.M8_EC + P.HOLG_TUERCA)} e/c, tuerca M8 cautiva", 2.5, "d")
    z0 = P.Z_CORE0 - P.DISCO_ESP
    Rf = Vista(L, "largo", (XC, YC, z0), 185, 150)
    Rf.formas([carrete])
    Rf.eje((XC, YC, z0 - 6), (XC, YC, P.Z_CORE1 + 6))
    L.cota(Rf.pt(XC - P.R_DISCO, YC, z0), Rf.pt(XC + P.R_DISCO, YC, z0), -8, d_(2 * P.R_DISCO), "h")
    L.cota(Rf.pt(XC + P.R_DISCO, YC, z0), Rf.pt(XC + P.R_DISCO, YC, P.Z_CORE0), -8, direc="v")
    L.cota(Rf.pt(XC + P.R_DISCO, YC, P.Z_CORE0), Rf.pt(XC + P.R_DISCO, YC, P.Z_CORE1), -8, direc="v")
    L.cota(Rf.pt(XC - 4.2, YC, P.Z_CORE1), Rf.pt(XC + 4.2, YC, P.Z_CORE1), 6, d_(P.VARILLA_D + P.HOLG_AGUJERO), "h")
    L.t(135, 128, 2.5, f"Disco superior (18): igual, {formato(P.DISCO_ESP)} de espesor, sin núcleo ni hexágono.")

    # --- Pieza 19: manivela
    L.t(252, 277, 3.5, "Pieza 19: manivela")
    man = pz["Manivela"]["forma"]
    zm = P.Z_MANIVELA
    Ma = Vista(L, "arriba", (XC, YC, zm), 262, 250)
    Ma.formas([man], ocultas=False)
    Ma.eje((XC - 16, YC, zm), (XC + P.R_MANIVELA + 16, YC, zm))
    Ma.eje((XC, YC - 16, zm), (XC, YC + 16, zm))
    Ma.eje((XC + P.R_MANIVELA, YC - 14, zm), (XC + P.R_MANIVELA, YC + 14, zm))
    L.cota(Ma.pt(XC, YC + P.CUBO_R, zm), Ma.pt(XC + P.R_MANIVELA, YC + P.CUBO_R, zm), 8, direc="h")
    L.cota(Ma.pt(XC + 40, YC - P.MANIVELA_ANCHO / 2, zm), Ma.pt(XC + 40, YC + P.MANIVELA_ANCHO / 2, zm), 0, direc="v")
    L.guia(Ma.pt(XC - P.CUBO_R * 0.7, YC - P.CUBO_R * 0.7, zm), Ma.pt(XC - 4, YC - 22, zm), f"Cubo %%c{formato(2 * P.CUBO_R)}, agujero %%c{formato(P.VARILLA_D + P.HOLG_AGUJERO)}")
    L.guia(Ma.pt(XC + P.R_MANIVELA + 2.5, YC - 1.2, zm), Ma.pt(XC + P.R_MANIVELA + 14, YC - 18, zm), f"Agujero %%c{formato(5 + P.HOLG_AGUJERO)} (M5)")
    Mf = Vista(L, "largo", (XC, YC, zm), 262, 212)
    Mf.formas([man])
    L.cota(Mf.pt(XC - P.CUBO_R, YC, zm), Mf.pt(XC - P.CUBO_R, YC, zm + P.CUBO_ALTO), 6, direc="v")
    L.cota(Mf.pt(XC + P.R_MANIVELA + 10, YC, P.Z_BRAZO), Mf.pt(XC + P.R_MANIVELA + 10, YC, P.Z_BRAZO_SUP), -6, direc="v")
    L.t(252, 204, 2.5, "Tuerca M8 en el cubo, abierta hacia la cama; se arma con esa cara arriba.")
    L.t(252, 199, 2.5, "Mango (20): tubo %%c22 x 55, con tornillo " + P.TORNILLO_MANGO_TXT.replace("×", "x") + ".")

    # --- Pieza 2: zócalo
    L.t(252, 190, 3.5, "Pieza 2: zócalo de la varilla")
    L.t(252, 184, 2.5, "Orejas a 30%%d, 150%%d y 270%%d: ninguna bajo el cabezal.")
    zoc = pz["Zocalo"]["forma"]
    Za = Vista(L, "arriba", (0, 0, 0), 300, 140)
    Za.formas([zoc], ocultas=False)
    Za.cruz((0, 0, 0), P.OREJA_R + 7)
    L.circulo("Ejes", Za.pt(0, 0, 0), P.OREJA_R)
    L.cota(Za.pt(-(P.VARILLA_D + P.HOLG_VARILLA) / 2, 0, 0), Za.pt((P.VARILLA_D + P.HOLG_VARILLA) / 2, 0, 0), -12, d_(P.VARILLA_D + P.HOLG_VARILLA), "h")
    L.guia(Za.pt(*xy_polar(P.OREJA_R, 30), 0), Za.pt(46, 40, 0), f"3 agujeros %%c3,9 en R{formato(P.OREJA_R)}")
    L.guia(Za.pt(-11.4, 2.5, 0), Za.pt(-42, -8, 0), "Ranura de la tuerca M3", 2.5, "d")
    Zf = Vista(L, "largo", (0, 0, 0), 300, 62)
    Zf.formas([zoc])
    Zf.eje((0, 0, -6), (0, 0, P.ZOCALO_ALTO + 6))
    L.cota(Zf.pt(P.ZOCALO_R, 0, 0), Zf.pt(P.ZOCALO_R, 0, P.ZOCALO_ALTO), -22, direc="v")
    L.cota(Zf.pt(P.ZOCALO_R, 0, 0), Zf.pt(P.ZOCALO_R, 0, P.Z_PRISIONERO), -14, direc="v")
    L.cota(Zf.pt(-P.ZOCALO_R, 0, 0), Zf.pt(-P.ZOCALO_R, 0, P.ZOCALO_FONDO), 22, direc="v")
    L.cota(Zf.pt(-P.ZOCALO_R, 0, P.ZOCALO_ALTO), Zf.pt(P.ZOCALO_R, 0, P.ZOCALO_ALTO), 6, d_(2 * P.ZOCALO_R), "h")
    L.guia(Zf.pt(-P.ZOCALO_R - 1, 0, P.Z_PRISIONERO + 1.5), Zf.pt(-42, 0, 40), "Agujero del prisionero M3, en rombo (sin soporte)", 2.5, "d")
    return L


# ------------------------------------------------------------------ lámina 4
def lamina_esquema():
    L = Lamina(1, 4, "Esquema de funcionamiento")
    marco_y_rotulo(L, "Sin escala", metodo=False)
    t = L.t
    res = json.load(open(os.path.join(CARPETA, "resultados.json"), encoding="utf-8"))["funcionamiento"]

    # --- Planta esquemática: la tira tira de la botella
    t(32, 277, 3.5, "Vista desde arriba")
    cb, rb = (95.0, 212.0), 28.0
    L.circulo("Contornos", cb, rb)
    L.circulo("Ejes", cb, 1.0)
    L.linea("Ejes", (cb[0] - rb - 6, cb[1]), (cb[0] + rb + 6, cb[1]))
    L.linea("Ejes", (cb[0], cb[1] - rb - 6), (cb[0], cb[1] + rb + 6))
    t(cb[0], cb[1] - rb - 8, 3.5, "Botella, %%cD, sobre la varilla", "c")
    flecha_giro(L, cb, 14, 110, 340, horaria=True)   # vista desde arriba: horaria
    # cabezal con la hoja en el punto (0, R): la tira sale hacia +X
    xh, yh = cb[0], cb[1] + rb
    L.polilinea("Contornos", [(xh - 18, yh - 6), (xh + 10, yh - 6), (xh + 10, yh + 10), (xh - 18, yh + 10)], True)
    L.polilinea("Contornos", [(xh, yh), (xh + 9, yh + 1.6), (xh + 9, yh - 1.6)], True)
    t(xh - 18, yh + 13, 2.5, "Cabezal: guía, labios y hoja fija")
    # tira, ojal y carrete
    cc, r0, rf = (200.0, 204.0), 10.0, 17.0
    L.linea("Contornos", (xh, yh), (cc[0], cc[1] + r0))
    L.linea("Contornos", (xh, yh + 0.8), (cc[0], cc[1] + r0 + 0.8))
    xo = 150.0
    y_t = yh + (cc[1] + r0 - yh) * (xo - xh) / (cc[0] - xh)
    L.rectangulo("Contornos", (xo - 5, y_t - 3.5), (xo + 5, y_t - 1.0))
    L.rectangulo("Contornos", (xo - 5, y_t + 2.2), (xo + 5, y_t + 4.7))
    t(xo, y_t - 9, 2.5, "Ojal fijo", "c")
    L.circulo("Contornos", cc, r0)
    L.circulo("Extremas", cc, rf)
    L.linea("Ejes", (cc[0] - 50, cc[1]), (cc[0] + 50, cc[1]))
    L.linea("Ejes", (cc[0], cc[1] - 24), (cc[0], cc[1] + 24))
    L.rectangulo("Contornos", (cc[0], cc[1] - 3), (cc[0] + 32, cc[1] + 3))
    L.circulo("Contornos", (cc[0] + 32, cc[1]), 4.5)
    flecha_giro(L, cc, 22, 150, 20, horaria=True)
    t(cc[0] - 40, cc[1] - 30, 2.5, "Carrete: núcleo r0, rollo r (crece)")
    t(cc[0] + 2, cc[1] + 9, 2.5, "Manivela, brazo R")
    t(xo + 22, y_t + 1, 2.5, "Tira, tiro T")
    t(32, 168, 2.5, "Vistos desde arriba, la botella y el carrete giran en sentido horario.")
    t(32, 163, 2.5, "El eje M8 tiene rosca derecha: ese giro aprieta la tuerca de la manivela.")

    # --- Alzado esquemático: el paso lo fija la guía
    t(32, 150, 3.5, "Vista de frente")
    xv, zg = 100.0, 95.0
    L.linea("Contornos", (xv, 68), (xv, 148))                  # varilla
    L.polilinea("Contornos", [(xv - 22, zg), (xv - 22, 128), (xv - 8, 142), (xv + 8, 142), (xv + 22, 128), (xv + 22, zg)])
    L.rectangulo("Contornos", (xv - 7, 140), (xv + 7, 146))           # tapa
    L.rectangulo("Contornos", (xv - 32, 68), (xv + 32, 74))           # taco
    L.rectangulo("Contornos", (xv - 32, 74), (xv + 32, zg))           # cabezal, hasta la guía
    L.linea("Contornos", (xv - 32, 68), (xv + 32, 68))
    for x in range(int(xv - 60), int(xv + 100), 5):
        L.linea("Cotas", (x + 3, 68), (x, 65))
    L.linea("Contornos", (xv - 60, 68), (xv + 100, 68))
    # hoja a la altura w sobre la guía, y la tira saliendo
    L.linea("Contornos", (xv + 22, zg + 9), (xv + 40, zg + 9))
    L.rectangulo("Contornos", (xv + 22, zg), (xv + 100, zg + 9))
    t(xv + 42, zg + 11, 2.5, "Hoja, a w sobre la guía")
    t(xv + 60, zg + 2.5, 2.5, "Tira, ancho w")
    L.cota((xv + 22, zg), (xv + 22, zg + 9), -6, "w", "v")
    L.linea("Cotas", (xv - 22, zg + 9), (xv + 22, zg))           # borde en hélice, inclinación alfa
    t(xv - 52, zg + 15, 2.5, "Borde cortado:")
    t(xv - 52, zg + 10.5, 2.5, "hélice de paso w")
    t(xv - 46, 80, 2.5, "Base de MDF")
    t(xv - 10, 150, 2.5, "Tapa perforada: centra")
    t(xv - 60, 128, 2.5, "La botella baja w por")
    t(xv - 60, 123, 2.5, "vuelta: el borde vuelve")
    t(xv - 60, 118, 2.5, "a apoyar en la guía")

    # --- Cadena de cuentas
    x = 245.0
    t(x, 277, 5, "Cadena del movimiento")
    ecs = (("Paso del corte, lo fija la guía:", "p = w"),
           ("Inclinación de la hélice:", "tg(alfa) = w / (pi·D)"),
           ("Vueltas de botella:", "nb = s / w"),
           ("Largo de la tira:", "L = pi·D·nb"),
           ("Radio del rollo lleno:", "rf^2 = r0^2 + L·t / pi"),
           ("Vueltas de manivela (carrete directo, i = 1):", "nm = (rf - r0) / t"),
           ("Fuerza en la mano:", "F = T·r / R"))
    y = 266
    for a, b in ecs:
        t(x, y, 3.5, a)
        t(x, y - 5.5, 3.5, b, capa="Texto")
        y -= 13
    L.rectangulo("Contornos", (x, 158), (x + 100, 172))
    t(x + 50, 162, 6, "F = T·rf / R", "c")
    t(x, 152, 2.5, "La tensión de la tira la pone el corte, no la mano: la manivela solo fija la velocidad.")
    t(x, 147, 2.5, "Un brazo R más largo baja F sin agregar engranajes.")
    filas = [("Símbolo", "Magnitud", "Valor"),
             ("D", "Diámetro de la botella", f"{formato(P.D_B)} mm"),
             ("t", "Espesor de pared", f"{P.PARED:.2f}".replace(".", ",") + " mm"),
             ("w", "Ancho de tira (calce)", f"{formato(P.W)} mm"),
             ("s", "Tramo cortado", f"{formato(P.RECORRIDO)} mm"),
             ("alfa", "Inclinación de la hélice", f"{res['helice_grados']:.2f}".replace(".", ",") + "%%d"),
             ("nb", "Vueltas de botella", formato(res["vueltas_botella"])),
             ("L", "Largo de la tira", f"{res['largo_tira_m']:.2f}".replace(".", ",") + " m"),
             ("r0 / rf", "Radio del rollo, vacío / lleno", f"{formato(res['radio_rollo_mm'][0])} / {formato(res['radio_rollo_mm'][1])} mm"),
             ("nm", "Vueltas de manivela", formato(res["vueltas_manivela"])),
             ("R", "Brazo de la manivela", f"{formato(P.R_MANIVELA)} mm"),
             ("T", "Tiro de diseño (supuesto)", f"{formato(P.T_DISENO)} N"),
             ("F", "Fuerza en la mano, rollo lleno", f"{formato(res['fuerza_mano_N'])} N (criterio: hasta {formato(P.F_MANO_MAX)} N)")]
    tabla(L, x, 140, [16, 58, 86], filas, 2.5, 5.0)
    t(x, 70, 2.5, "Valores calculados con el modelo digital del prototipo.")
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
    pedidas = [a for a in sys.argv[1:] if not a.endswith(".py")]
    laminas = (("01_conjunto", lamina_conjunto), ("02_cabezal", lamina_cabezal),
               ("03_carrete", lamina_carrete), ("04_esquema", lamina_esquema))
    informe, ok = {}, True
    for nombre, f in laminas:
        if pedidas and nombre not in pedidas:
            continue
        L = f()
        L.guardar(os.path.join(intermedio, nombre + ".json"), 420, 297, nombre + ".dxf")
        malos = superposiciones(L)
        ok = ok and not malos
        informe[nombre] = {"escala": L.E, "entidades": len(L.ops),
                           "cotas": sum(1 for o in L.ops if o[0] == "d"),
                           "textos_superpuestos": malos}
        print(nombre, informe[nombre])
    ruta = os.path.join(CARPETA, "resultados.json")
    with open(ruta, encoding="utf-8") as fh:
        todo = json.load(fh)
    todo.setdefault("planos", {}).update(informe)
    with open(ruta, "w", encoding="utf-8") as fh:
        json.dump(todo, fh, ensure_ascii=False, indent=1)
    return ok


codigo = 1
try:
    codigo = 0 if main() else 1
except Exception:
    with open(os.path.join(CARPETA, "build_error.txt"), "a") as fh:
        fh.write(traceback.format_exc())
    traceback.print_exc()
finally:
    sys.stdout.flush()
    os._exit(codigo)
