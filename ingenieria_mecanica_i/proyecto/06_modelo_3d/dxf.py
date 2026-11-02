# -*- coding: utf-8 -*-
"""
Escritor mínimo de DXF R2000 (AC1015), sin bibliotecas externas.

Las cotas son entidades DIMENSION de verdad: se pueden editar y miden solas.
Cada una lleva además su bloque *Dn ya dibujado, como hace AutoCAD; LibreCAD lo
ignora y la vuelve a dibujar con las variables de cota del encabezado.
"""
import math

CAPAS = [  # nombre, color, tipo de línea, grosor en centésimas de mm (IRAM 4502)
    ("Contornos", 3, "Continuous", 50),     # 01.2 gruesa continua
    ("Ocultas", 6, "DASHED", 25),      # 02.1 fina de trazos
    ("Ejes", 1, "CENTER", 25),            # 04.1 fina de raya y punto
    ("Cotas", 5, "Continuous", 25),         # 01.1 fina continua
    ("Texto", 8, "Continuous", 25),         # rótulo, tablas y notas
    ("Extremas", 30, "DIVIDE", 25),   # 05.1 fina de raya y dos puntos
]
TIPOS = [  # nombre estándar (LibreCAD no admite otros), descripción, patrón en mm de papel
    ("DASHED", "IRAM 4502 tipo 02", [6.0, -1.5]),
    ("CENTER", "IRAM 4502 tipo 04", [12.0, -1.5, 0.5, -1.5]),
    ("DIVIDE", "IRAM 4502 tipo 05", [12.0, -1.5, 0.5, -1.5, 0.5, -1.5]),
]
ANCHO_LETRA = 0.72      # ancho medio de un carácter respecto de la altura


def _n(v):
    t = f"{v:.4f}".rstrip("0").rstrip(".")
    return "0" if t in ("-0", "") else t


def formato(v):
    """Número con coma decimal, sin decimales si es entero."""
    if abs(v - round(v)) < 0.005:
        return str(int(round(v)))
    return f"{v:.1f}".replace(".", ",")


def ancho_texto(texto, h):
    limpio = texto.replace("%%c", "Ø").replace("%%d", "°")
    return len(limpio) * h * ANCHO_LETRA


class Dibujo:
    def __init__(self, escala):
        self.E = escala
        self._h = 0x100
        self.mod = []          # entidades del espacio modelo
        self.bloques = []      # (nombre, entidades como funciones de owner)
        self.brec_modelo = self._nuevo()
        self.brec_papel = self._nuevo()
        self.lay_modelo = self._nuevo()
        self.lay_papel = self._nuevo()
        self.rect = []         # rectángulos de texto, para buscar superposiciones
        self.ext = [1e18, 1e18, -1e18, -1e18]

    def _nuevo(self):
        self._h += 1
        return f"{self._h:X}"

    def _ext(self, x, y):
        e = self.ext
        e[0], e[1], e[2], e[3] = min(e[0], x), min(e[1], y), max(e[2], x), max(e[3], y)

    # ------------------------------------------------------------ entidades
    def _ent(self, tipo, capa, sub, grupos, destino=None, owner=None):
        d = self.mod if destino is None else destino
        s = [(0, tipo), (5, self._nuevo()), (330, owner or self.brec_modelo),
             (100, "AcDbEntity"), (8, capa)]
        s += grupos if sub is None else [(100, sub)] + grupos
        d.append(s)

    def linea(self, capa, a, b, destino=None, owner=None):
        self._ent("LINE", capa, "AcDbLine",
                  [(10, a[0]), (20, a[1]), (30, 0), (11, b[0]), (21, b[1]), (31, 0)],
                  destino, owner)
        self._ext(*a)
        self._ext(*b)

    def circulo(self, capa, c, r):
        self._ent("CIRCLE", capa, "AcDbCircle", [(10, c[0]), (20, c[1]), (30, 0), (40, r)])
        self._ext(c[0] - r, c[1] - r)
        self._ext(c[0] + r, c[1] + r)

    def arco(self, capa, c, r, a0, a1):
        """Antihorario, de a0 a a1, en grados."""
        self._ent("ARC", capa, None,
                  [(100, "AcDbCircle"), (10, c[0]), (20, c[1]), (30, 0), (40, r),
                   (100, "AcDbArc"), (50, a0 % 360), (51, a1 % 360)])
        self._ext(c[0] - r, c[1] - r)
        self._ext(c[0] + r, c[1] + r)

    def polilinea(self, capa, pts, cerrada=False):
        g = [(90, len(pts)), (70, 1 if cerrada else 0)]
        for p in pts:
            g += [(10, p[0]), (20, p[1])]
            self._ext(*p)
        self._ent("LWPOLYLINE", capa, "AcDbPolyline", g)

    def solido(self, capa, a, b, c, destino=None, owner=None):
        """Triángulo relleno: la flecha ennegrecida de la cátedra."""
        g = []
        for k, p in enumerate((a, b, c, c)):
            g += [(10 + k, p[0]), (20 + k, p[1]), (30 + k, 0)]
        self._ent("SOLID", capa, "AcDbTrace", g, destino, owner)

    def texto(self, capa, x, y, h, s, alin="i", rot=0.0, destino=None, owner=None,
              registrar=True):
        """x, y en el modelo; h en mm de papel; alin: i(zquierda), c(entro), d(erecha)."""
        H = h * self.E
        g = [(10, x), (20, y), (30, 0), (40, H), (1, s), (50, rot), (7, "IRAM")]
        if alin != "i":
            g += [(72, 1 if alin == "c" else 2), (11, x), (21, y), (31, 0)]
        g += [(100, "AcDbText")]
        self._ent("TEXT", capa, "AcDbText", g, destino, owner)
        if registrar:
            w = ancho_texto(s, H)
            dx = {"i": 0.0, "c": -w / 2, "d": -w}[alin]
            r = math.radians(rot)
            esq = []
            for u, v in ((dx, 0), (dx + w, 0), (dx + w, H), (dx, H)):
                esq.append((x + u * math.cos(r) - v * math.sin(r),
                            y + u * math.sin(r) + v * math.cos(r)))
            xs, ys = [p[0] for p in esq], [p[1] for p in esq]
            self.rect.append((min(xs), min(ys), max(xs), max(ys), s))

    # ----------------------------------------------------------------- cotas
    def cota(self, a, b, d, s=None, direc=None, h=3.5):
        """Cota lineal entre a y b, con la línea a d mm de papel de la recta que
        los une. direc: 'h', 'v' o None (paralela a ab). s: texto; None = medida."""
        E = self.E
        if direc == "h":
            ang = 0.0
        elif direc == "v":
            ang = 90.0
        else:
            ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
        # El número se lee de abajo o desde la derecha (IRAM)
        if ang > 90.001 or ang <= -89.999:
            ang -= 180 if ang > 0 else -180
            a, b = b, a
        r = math.radians(ang)
        ux, uy = math.cos(r), math.sin(r)
        nx, ny = -uy, ux
        # Pies de las auxiliares sobre la línea de cota
        base = (a[0] + nx * d * E, a[1] + ny * d * E)
        ta = (a[0] - base[0]) * ux + (a[1] - base[1]) * uy
        tb = (b[0] - base[0]) * ux + (b[1] - base[1]) * uy
        p1 = (base[0] + ux * ta, base[1] + uy * ta)
        p2 = (base[0] + ux * tb, base[1] + uy * tb)
        if d < 0:
            pass
        med = abs(tb - ta)
        if s is None:
            rotulo = formato(med)
            grupo1 = "<>" if abs(med - round(med)) < 0.005 else rotulo
        else:
            rotulo = s
            grupo1 = s
        H = h * E
        w = ancho_texto(rotulo, H)
        flecha = 3.5 * E
        cabe = med >= 2 * flecha + w + 2 * E
        c = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
        if not cabe:      # espacio reducido: número afuera, del lado de b
            lejos = w / 2 + 2 * flecha + 1 * E
            sentido = 1 if tb > ta else -1
            c = (p2[0] + ux * sentido * lejos, p2[1] + uy * sentido * lejos)
        tx = c[0] + nx * 1.0 * E
        ty = c[1] + ny * 1.0 * E
        medio = (c[0] + nx * (1.0 * E + H / 2), c[1] + ny * (1.0 * E + H / 2))

        n = len(self.bloques) + 1
        nombre = f"*D{n}"
        brec = self._nuevo()
        ents = []
        sal = 2.0 * E
        sep = 1.0 * E
        for pie, ori in ((p1, a), (p2, b)):
            vx, vy = pie[0] - ori[0], pie[1] - ori[1]
            lg = math.hypot(vx, vy)
            if lg < 1e-6:
                continue
            vx, vy = vx / lg, vy / lg
            self.linea("Cotas", (ori[0] + vx * sep, ori[1] + vy * sep),
                       (pie[0] + vx * sal, pie[1] + vy * sal), ents, brec)
        if cabe:
            self.linea("Cotas", p1, p2, ents, brec)
        else:
            sgn = 1 if tb > ta else -1
            ext = 2 * flecha
            self.linea("Cotas", (p1[0] - ux * sgn * ext, p1[1] - uy * sgn * ext),
                       (p2[0] + ux * sgn * ext, p2[1] + uy * sgn * ext), ents, brec)
        sgn = 1 if tb > ta else -1
        if not cabe:
            sgn = -sgn
        ancho = flecha / 4 / 2     # relación 4:1 de la cátedra
        for pie, sen in ((p1, sgn), (p2, -sgn)):
            m = (pie[0] + ux * sen * flecha, pie[1] + uy * sen * flecha)
            self.solido("Cotas", pie, (m[0] + nx * ancho, m[1] + ny * ancho),
                        (m[0] - nx * ancho, m[1] - ny * ancho), ents, brec)
        texto_visible = rotulo
        self.texto("Cotas", tx, ty, h, texto_visible, "c", ang, ents, brec)
        self.bloques.append((nombre, brec, ents))

        g = [(100, "AcDbDimension"), (2, nombre), (10, p2[0]), (20, p2[1]), (30, 0),
             (11, medio[0]), (21, medio[1]), (31, 0), (70, 32), (71, 5),
             (1, grupo1), (3, "IRAM"),
             (100, "AcDbAlignedDimension"),
             (13, a[0]), (23, a[1]), (33, 0), (14, b[0]), (24, b[1]), (34, 0),
             (50, ang), (100, "AcDbRotatedDimension")]
        self._ent("DIMENSION", "Cotas", None, g)
        for p in (a, b, p1, p2):
            self._ext(*p)

    # ----------------------------------------------------------------- salida
    def _tablas(self):
        E = self.E
        h_tabla = {}
        out = []

        def tabla(nombre, entradas, extra=None):
            th = self._nuevo()
            h_tabla[nombre] = th
            out.extend([(0, "TABLE"), (2, nombre), (5, th), (330, 0),
                        (100, "AcDbSymbolTable"), (70, len(entradas))])
            out.extend(extra or [])
            for e in entradas:
                out.extend(e(th))
            out.append((0, "ENDTAB"))

        def registro(tipo, sub, grupos, handle=None, cod=5):
            def f(th):
                return [(0, tipo), (cod, handle or self._nuevo()), (330, th),
                        (100, "AcDbSymbolTableRecord"), (100, sub)] + grupos
            return f

        tabla("VPORT", [registro("VPORT", "AcDbViewportTableRecord", [
            (2, "*Active"), (70, 0), (10, 0), (20, 0), (11, 1), (21, 1),
            (12, 210 * E), (22, 148.5 * E), (13, 0), (23, 0), (14, 10), (24, 10),
            (15, 10), (25, 10), (16, 0), (26, 0), (36, 1), (17, 0), (27, 0), (37, 0),
            (40, 297 * E), (41, 420 / 297), (42, 50), (43, 0), (44, 0), (50, 0),
            (51, 0), (71, 0), (72, 1000), (73, 1), (74, 3), (75, 0), (76, 0),
            (77, 0), (78, 0), (281, 0), (65, 1), (110, 0), (120, 0), (130, 0),
            (111, 1), (121, 0), (131, 0), (112, 0), (122, 1), (132, 0), (79, 0),
            (146, 0)])])

        tipos = [registro("LTYPE", "AcDbLinetypeTableRecord", [
            (2, n), (70, 0), (3, ""), (72, 65), (73, 0), (40, 0)])
            for n in ("ByBlock", "ByLayer", "Continuous")]
        for n, desc, pat in TIPOS:
            g = [(2, n), (70, 0), (3, desc), (72, 65), (73, len(pat)),
                 (40, sum(abs(v) for v in pat))]
            for v in pat:
                g += [(49, v), (74, 0)]
            tipos.append(registro("LTYPE", "AcDbLinetypeTableRecord", g))
        tabla("LTYPE", tipos)

        self.h_placeholder = self._nuevo()
        capas = [registro("LAYER", "AcDbLayerTableRecord", [
            (2, "0"), (70, 0), (62, 7), (6, "Continuous"), (370, -3),
            (390, self.h_placeholder)])]
        for nom, col, tipo, gros in CAPAS:
            capas.append(registro("LAYER", "AcDbLayerTableRecord", [
                (2, nom), (70, 0), (62, col), (6, tipo), (370, gros),
                (390, self.h_placeholder)]))
        tabla("LAYER", capas)

        h_estilo = self._nuevo()
        tabla("STYLE", [
            registro("STYLE", "AcDbTextStyleTableRecord", [
                (2, "Standard"), (70, 0), (40, 0), (41, 1), (50, 0), (71, 0),
                (42, 2.5), (3, "simplex.shx"), (4, "")]),
            registro("STYLE", "AcDbTextStyleTableRecord", [
                (2, "IRAM"), (70, 0), (40, 0), (41, 1), (50, 0), (71, 0),
                (42, 3.5), (3, "simplex.shx"), (4, "")], h_estilo)])
        tabla("VIEW", [])
        tabla("UCS", [])
        tabla("APPID", [registro("APPID", "AcDbRegAppTableRecord",
                                 [(2, "ACAD"), (70, 0)])])

        def dimestilo(nombre, handle=None):
            return registro("DIMSTYLE", "AcDbDimStyleTableRecord", [
                (2, nombre), (70, 0), (40, E), (41, 3.5), (42, 1), (43, 7), (44, 2),
                (140, 3.5), (141, 0), (147, 1), (144, 1), (73, 0), (74, 0), (77, 1),
                (78, 8), (271, 0), (272, 0), (278, 44), (340, h_estilo)],
                handle, 105)
        tabla("DIMSTYLE", [dimestilo("Standard"), dimestilo("IRAM")],
              [(100, "AcDbDimStyleTable"), (71, 0)])

        brecs = [
            registro("BLOCK_RECORD", "AcDbBlockTableRecord",
                     [(2, "*Model_Space"), (340, self.lay_modelo)], self.brec_modelo),
            registro("BLOCK_RECORD", "AcDbBlockTableRecord",
                     [(2, "*Paper_Space"), (340, self.lay_papel)], self.brec_papel)]
        for nom, brec, _ in self.bloques:
            brecs.append(registro("BLOCK_RECORD", "AcDbBlockTableRecord",
                                  [(2, nom), (340, 0)], brec))
        tabla("BLOCK_RECORD", brecs)
        return out

    def _bloque(self, nombre, brec, ents, flags, capa="0"):
        s = [(0, "BLOCK"), (5, self._nuevo()), (330, brec), (100, "AcDbEntity"),
             (8, capa), (100, "AcDbBlockBegin"), (2, nombre), (70, flags),
             (10, 0), (20, 0), (30, 0), (3, nombre), (1, "")]
        for e in ents:
            s += e
        s += [(0, "ENDBLK"), (5, self._nuevo()), (330, brec), (100, "AcDbEntity"),
              (8, capa), (100, "AcDbBlockEnd")]
        return s

    def _layout(self, handle, dic, nombre, orden, brec):
        return [
            (0, "LAYOUT"), (5, handle), (102, "{ACAD_REACTORS"), (330, dic), (102, "}"),
            (330, dic), (100, "AcDbPlotSettings"), (1, ""), (2, "none_device"),
            (4, "ISO_A3_(420.00_x_297.00_MM)"), (6, ""), (40, 0), (41, 0), (42, 0),
            (43, 0), (44, 420), (45, 297), (46, 0), (47, 0), (48, 0), (49, 0),
            (140, 0), (141, 0), (142, 1), (143, self.E), (70, 688), (72, 1), (73, 0),
            (74, 5), (7, ""), (75, 0), (147, 1 / self.E), (148, 0), (149, 0),
            (100, "AcDbLayout"), (1, nombre), (70, 1), (71, orden),
            (10, 0), (20, 0), (11, 420), (21, 297), (12, 0), (22, 0), (32, 0),
            (14, 0), (24, 0), (34, 0), (15, 420 * self.E), (25, 297 * self.E), (35, 0),
            (146, 0), (13, 0), (23, 0), (33, 0), (16, 1), (26, 0), (36, 0),
            (17, 0), (27, 1), (37, 0), (76, 0), (330, brec)]

    def guardar(self, ruta):
        tablas = self._tablas()
        raiz, d_grupo, d_estilo, d_lay = (self._nuevo() for _ in range(4))
        bloques = (self._bloque("*Model_Space", self.brec_modelo, [], 0)
                   + self._bloque("*Paper_Space", self.brec_papel, [], 0))
        for nom, brec, ents in self.bloques:
            bloques += self._bloque(nom, brec, ents, 1)
        entidades = [g for e in self.mod for g in e]
        objetos = [
            (0, "DICTIONARY"), (5, raiz), (330, 0), (100, "AcDbDictionary"), (281, 1),
            (3, "ACAD_GROUP"), (350, d_grupo), (3, "ACAD_LAYOUT"), (350, d_lay),
            (3, "ACAD_PLOTSTYLENAME"), (350, d_estilo),
            (0, "DICTIONARY"), (5, d_grupo), (330, raiz), (100, "AcDbDictionary"), (281, 1),
            (0, "DICTIONARY"), (5, d_lay), (330, raiz), (100, "AcDbDictionary"), (281, 1),
            (3, "Layout1"), (350, self.lay_papel), (3, "Model"), (350, self.lay_modelo),
            (0, "ACDBDICTIONARYWDFLT"), (5, d_estilo), (330, raiz), (100, "AcDbDictionary"),
            (281, 1), (3, "Normal"), (350, self.h_placeholder),
            (100, "AcDbDictionaryWithDefault"), (340, self.h_placeholder),
            (0, "ACDBPLACEHOLDER"), (5, self.h_placeholder), (330, d_estilo),
        ] + self._layout(self.lay_modelo, d_lay, "Model", 0, self.brec_modelo) \
          + self._layout(self.lay_papel, d_lay, "Layout1", 1, self.brec_papel)
        E = self.E
        ex = self.ext
        encabezado = [
            (9, "$ACADVER"), (1, "AC1015"), (9, "$ACADMAINTVER"), (70, 6),
            (9, "$DWGCODEPAGE"), (3, "ANSI_1252"),
            (9, "$INSBASE"), (10, 0), (20, 0), (30, 0),
            (9, "$EXTMIN"), (10, ex[0]), (20, ex[1]), (30, 0),
            (9, "$EXTMAX"), (10, ex[2]), (20, ex[3]), (30, 0),
            (9, "$LIMMIN"), (10, 0), (20, 0), (9, "$LIMMAX"), (10, 420 * E), (20, 297 * E),
            (9, "$PLIMMIN"), (10, 0), (20, 0), (9, "$PLIMMAX"), (10, 420), (20, 297),
            (9, "$PLIMCHECK"), (70, 0),
            (9, "$LTSCALE"), (40, E), (9, "$CELTSCALE"), (40, 1),
            (9, "$TEXTSTYLE"), (7, "IRAM"), (9, "$CLAYER"), (8, "Contornos"),
            (9, "$DIMSTYLE"), (2, "IRAM"), (9, "$DIMSCALE"), (40, E),
            (9, "$DIMASZ"), (40, 3.5), (9, "$DIMEXO"), (40, 1), (9, "$DIMEXE"), (40, 2),
            (9, "$DIMGAP"), (40, 1), (9, "$DIMTXT"), (40, 3.5), (9, "$DIMTAD"), (70, 1),
            (9, "$DIMTIH"), (70, 0), (9, "$DIMTOH"), (70, 0), (9, "$DIMDEC"), (70, 0),
            (9, "$DIMDSEP"), (70, 44), (9, "$DIMLUNIT"), (70, 2),
            (9, "$LUNITS"), (70, 2), (9, "$LUPREC"), (70, 2), (9, "$MEASUREMENT"), (70, 1),
            (9, "$INSUNITS"), (70, 4), (9, "$PSVPSCALE"), (40, 0),
            (9, "$CELWEIGHT"), (370, -1), (9, "$LWDISPLAY"), (290, 1),
            (9, "$HANDSEED"), (5, f"{self._h + 16:X}"),
        ]
        secciones = [("HEADER", encabezado), ("CLASSES", []), ("TABLES", tablas),
                     ("BLOCKS", bloques), ("ENTITIES", entidades), ("OBJECTS", objetos)]
        lineas = []
        for nombre, grupos in secciones:
            lineas += ["  0", "SECTION", "  2", nombre]
            for cod, val in grupos:
                lineas.append(f"{cod:>3}")
                if isinstance(val, float):
                    lineas.append(_n(val))
                else:
                    lineas.append(str(val))
            lineas += ["  0", "ENDSEC"]
        lineas += ["  0", "EOF"]
        with open(ruta, "w", encoding="cp1252", errors="replace", newline="\n") as f:
            f.write("\n".join(lineas) + "\n")
