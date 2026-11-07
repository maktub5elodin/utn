# -*- coding: utf-8 -*-
"""
Piezas del modelo 2.0, armadas en su lugar. El único estado que cambia es s,
lo que ya se cortó de la botella (0 a RECORRIDO): la botella se acorta y baja,
el rollo crece. El resto queda quieto, salvo lo que gira.

Cada pieza es un dict:
  forma      sólido armado
  tipo       "impresa", "comercial" o "botella" (botella, tapa, tira)
  cantidad   unidades iguales en el armado
  impresion  Placement que lleva la pieza armada a la cama (Z = 0)
  nota       para la ficha de impresión o la lista de compras
"""
import math

import FreeCAD as App
import Part

import parametros as P

V = App.Vector
Z_UP = V(0, 0, 1)

COLORES = {
    "impresa": (0.95, 0.50, 0.12),
    "comercial": (0.72, 0.74, 0.78),
    "mdf": (0.78, 0.66, 0.48),
    "botella": (0.55, 0.85, 0.72),
    "tira": (0.20, 0.62, 0.45),
}


# ------------------------------------------------------------------ primitivas
def caja(x, y, z):
    return Part.makeBox(x[1] - x[0], y[1] - y[0], z[1] - z[0], V(x[0], y[0], z[0]))


def cil(r, z0, z1, x=0.0, y=0.0):
    """Cilindro de eje vertical."""
    return Part.makeCylinder(r, z1 - z0, V(x, y, z0), Z_UP)


def sector(r0, r1, th0, th1, z0, z1):
    """Sector de corona alrededor del eje de la botella; ángulos en grados."""
    ext = Part.makeCylinder(r1, z1 - z0, V(0, 0, z0), Z_UP, th1 - th0)
    ext.rotate(V(0, 0, 0), Z_UP, th0)
    if r0 <= 0:
        return ext
    return ext.cut(cil(r0, z0 - 1, z1 + 1))


def hexagono(entre_caras, z0, z1, x=0.0, y=0.0, giro=0.0):
    """Prisma hexagonal vertical (alojamiento de tuerca)."""
    r = entre_caras / math.sqrt(3)
    pts = [V(x + r * math.cos(math.radians(giro + 60 * k)),
             y + r * math.sin(math.radians(giro + 60 * k)), z0) for k in range(7)]
    return Part.Face(Part.makePolygon(pts)).extrude(V(0, 0, z1 - z0))


def agujero(d_nominal, z0, z1, x=0.0, y=0.0):
    return cil((d_nominal + P.HOLG_AGUJERO) / 2, z0, z1, x, y)


def revolucion(puntos_rz):
    """Sólido de revolución alrededor del eje Z a partir de (r, z)."""
    pts = [V(r, 0, z) for r, z in puntos_rz] + [V(puntos_rz[0][0], 0, puntos_rz[0][1])]
    return Part.Face(Part.makePolygon(pts)).revolve(V(0, 0, 0), Z_UP, 360)


def a_la_cama(forma):
    """Placement que apoya la forma armada sobre la cama, sin girarla."""
    b = forma.BoundBox
    return App.Placement(V(-b.XMin, -b.YMin, -b.ZMin), App.Rotation())


def tornillo_madera(x, y, z_apoyo):
    """Agujero pasante con caja para la cabeza; queda PISO_BAJO_TORNILLO de material."""
    pas = agujero(P.MADERA_D, -1, z_apoyo + 1, x, y)
    caja_cab = cil(P.MADERA_CABEZA_D / 2 + 0.3, P.PISO_BAJO_TORNILLO, z_apoyo + 1, x, y)
    return pas.fuse(caja_cab)


# ----------------------------------------------------------------- base y eje
def mdf():
    x0, y0 = P.MDF_ORIGEN
    return caja((x0, x0 + P.MDF[0]), (y0, y0 + P.MDF[1]), (-P.MDF[2], 0))


def zocalo():
    cuerpo = cil(P.ZOCALO_R, 0, P.ZOCALO_ALTO)
    for a in P.OREJAS_ZOCALO:
        x, y = P.OREJA_R * math.cos(math.radians(a)), P.OREJA_R * math.sin(math.radians(a))
        oreja = cil(7.0, 0, 8.0, x, y).fuse(cil(7.0, 0, 8.0, x / 2, y / 2))
        cuerpo = cuerpo.fuse(oreja)
    for a in P.OREJAS_ZOCALO:
        x, y = P.OREJA_R * math.cos(math.radians(a)), P.OREJA_R * math.sin(math.radians(a))
        cuerpo = cuerpo.cut(agujero(P.MADERA_D, -1, 9, x, y))
    cuerpo = cuerpo.cut(agujero(P.VARILLA_D, -1, P.ZOCALO_ALTO + 1))
    cuerpo = cuerpo.cut(hexagono(P.M8_EC + P.HOLG_TUERCA, -1, P.M8_ALTO + 0.5))
    return cuerpo.removeSplitter()


def varilla():
    return cil(P.VARILLA_D / 2, 1.0, 1.0 + P.VARILLA_L)


def tuerca_m8(z0, x=0.0, y=0.0):
    return hexagono(P.M8_EC, z0, z0 + P.M8_ALTO, x, y).cut(cil(P.VARILLA_D / 2, z0 - 1, z0 + 9, x, y))


def arandela_m8(z0, x=0.0, y=0.0):
    di, de, e = P.ARANDELA_M8
    return cil(de / 2, z0, z0 + e, x, y).cut(cil(di / 2, z0 - 1, z0 + e + 1, x, y))


# ------------------------------------------------------------------- cabezal
def cabezal():
    zg = P.Z_GUIA
    cuerpo = caja(P.CAB_X, P.CAB_Y, (0, zg))
    # labio interior: dentro de la botella, más bajo que la hoja
    r_int = P.R_B - P.PARED - P.HOLG_RANURA
    cuerpo = cuerpo.fuse(sector(P.LABIO_INT_R0, r_int, *P.TH_LABIOS, zg, zg + P.ALTO_LABIO_INT))
    # labio exterior: aguas arriba del filo (X < 0)
    r_ext = P.R_B + P.HOLG_RANURA
    th_filo = 90.0 + math.degrees(math.asin(0.6 / r_ext))      # termina 0,6 mm antes del filo
    cuerpo = cuerpo.fuse(sector(r_ext, r_ext + P.LABIO_ESP, th_filo, P.TH_LABIO_EXT_FIN,
                                zg, zg + P.ALTO_LABIO_EXT))
    # ranura de la chapita: queda a ras del piso, debajo de los labios
    x0 = P.CHAPITA_X[0] - 1
    cuerpo = cuerpo.cut(caja((x0, P.CHAPITA_X[1]), P.CHAPITA_Y, (zg - P.CHAPITA_ESP, zg)))
    # tornillos de la hoja: agujero vertical y tuerca que entra de costado (+Y)
    for x, y in P.TORNILLOS_HOJA:
        cuerpo = cuerpo.cut(agujero(3.0, zg - 16, zg + 1, x, y))
        ec = P.M3_EC + P.HOLG_TUERCA
        r_vert = ec / math.sqrt(3)                 # la tuerca entra con un vértice adelante
        zt = zg - P.PROF_TUERCA_HOJA - 3.0
        cuerpo = cuerpo.cut(caja((x - ec / 2, x + ec / 2), (y - r_vert, P.CAB_Y[1] + 1),
                                 (zt, zt + 3.0)))
    # fijación a la base
    for x, y in P.TORNILLOS_CABEZAL:
        cuerpo = cuerpo.cut(tornillo_madera(x, y, zg))
    return cuerpo.removeSplitter()


def calce(w):
    pl = caja(P.CALCE_X, P.CALCE_Y, (P.Z_GUIA, P.Z_GUIA + w))
    for x, y in P.TORNILLOS_HOJA:
        pl = pl.cut(agujero(3.0, P.Z_GUIA - 1, P.Z_GUIA + w + 1, x, y))
    return pl


def z_hoja(w=P.W):
    return P.Z_GUIA + w


def hoja(w=P.W):
    """Trincheta: el filo largo, en X = 0, mira aguas arriba (-X)."""
    z = z_hoja(w)
    return caja((0.0, P.HOJA[0]), (P.HOJA_Y0, P.HOJA_Y0 + P.LARGO_HOJA), (z, z + P.HOJA[1]))


def pisador(w=P.W):
    z = z_hoja(w) + P.HOJA[1]
    pl = caja(P.CALCE_X, P.CALCE_Y, (z, z + P.PISADOR_ESP))
    for x, y in P.TORNILLOS_HOJA:
        pl = pl.cut(agujero(3.0, z - 1, z + P.PISADOR_ESP + 1, x, y))
    return pl


def tornillos_hoja(w=P.W):
    z_cab = z_hoja(w) + P.HOJA[1] + P.PISADOR_ESP
    out = []
    for x, y in P.TORNILLOS_HOJA:
        out.append(cil(1.5, z_cab - P.TORNILLO_HOJA_L, z_cab, x, y).fuse(
            cil(P.M3_CABEZA_D / 2, z_cab, z_cab + P.M3_CABEZA_ALTO, x, y)))
    return Part.makeCompound(out)


def tuercas_hoja():
    zt = P.Z_GUIA - P.PROF_TUERCA_HOJA - 3.0 + 0.3
    return Part.makeCompound([hexagono(P.M3_EC, zt, zt + P.M3_ALTO, x, y, giro=30).cut(
        cil(1.5, zt - 1, zt + 4, x, y)) for x, y in P.TORNILLOS_HOJA])


def chapita():
    return caja(P.CHAPITA_X, P.CHAPITA_Y, (P.Z_GUIA - P.CHAPITA_ESP, P.Z_GUIA))


# ----------------------------------------------------------------------- ojal
def ojal():
    x0, x1 = P.X_OJAL - P.OJAL_LARGO / 2, P.X_OJAL + P.OJAL_LARGO / 2
    yc = P.R_B - P.PARED / 2
    h = P.OJAL_HUECO / 2
    alto = P.Z_GUIA + P.W_MAX + 2.0
    brida = caja((x0 - 14, x1 + 14), (yc - 9, yc + 9), (0, 5.0))
    torre = caja((x0, x1), (yc - h - P.OJAL_PARED, yc + h + P.OJAL_PARED), (0, alto))
    cuerpo = brida.fuse(torre)
    cuerpo = cuerpo.cut(caja((x0 - 1, x1 + 1), (yc - h, yc + h), (P.Z_GUIA - 0.5, alto + 1)))
    for x in (x0 - 7, x1 + 7):
        cuerpo = cuerpo.cut(agujero(P.MADERA_D, -1, 6, x, yc))
    return cuerpo.removeSplitter()


# --------------------------------------------------------- carrete y su torre
def torre():
    xc, yc = P.X_CARRETE, P.Y_CARRETE
    rb, eb = P.TORRE_BRIDA
    cuerpo = cil(P.TORRE_R, 0, P.TORRE_ALTO, xc, yc).fuse(cil(rb, 0, eb, xc, yc))
    cuerpo = cuerpo.cut(cil(P.TORRE_CAVIDAD[0], -1, P.TORRE_CAVIDAD[1], xc, yc))
    cuerpo = cuerpo.cut(cil(P.D_608_ALOJ / 2, P.TORRE_CAVIDAD[1], P.TORRE_ALTO + 1, xc, yc))
    for k in range(3):
        a = math.radians(90 + 120 * k)
        x, y = xc + P.TORRE_TORNILLOS_R * math.cos(a), yc + P.TORRE_TORNILLOS_R * math.sin(a)
        cuerpo = cuerpo.cut(agujero(P.MADERA_D, -1, eb + 1, x, y))
    return cuerpo.removeSplitter()


def rodamientos():
    xc, yc = P.X_CARRETE, P.Y_CARRETE
    z_inf = P.TORRE_CAVIDAD[1]
    out = []
    for z0 in (z_inf, P.TORRE_ALTO - P.ANCHO_608):
        out.append(cil(P.D_608 / 2, z0, z0 + P.ANCHO_608, xc, yc).cut(
            cil(4.0, z0 - 1, z0 + P.ANCHO_608 + 1, xc, yc)))
    return Part.makeCompound(out)


def eje_carrete():
    """Tornillo M8 × 60 con su arandela, cabeza abajo, en la cavidad de la torre."""
    xc, yc = P.X_CARRETE, P.Y_CARRETE
    z_ar = P.TORRE_CAVIDAD[1] - P.ARANDELA_M8[2]
    z_cab = z_ar - P.M8_CABEZA_ALTO
    cab = hexagono(P.M8_CABEZA_EC, z_cab, z_ar, xc, yc)
    cuerpo = cil(4.0, z_ar, z_ar + P.EJE_CARRETE_L, xc, yc)
    return cab.fuse(cuerpo).fuse(arandela_m8(z_ar, xc, yc))


def arandela_superior():
    return arandela_m8(P.TORRE_ALTO, P.X_CARRETE, P.Y_CARRETE)


def carrete_inferior():
    """Disco inferior con el núcleo y la ranura para enganchar la tira."""
    xc, yc = P.X_CARRETE, P.Y_CARRETE
    z0 = P.Z_CORE0 - P.DISCO_ESP
    cuerpo = cil(P.R_DISCO, z0, P.Z_CORE0, xc, yc).fuse(cil(P.R_NUCLEO, P.Z_CORE0, P.Z_CORE1, xc, yc))
    cuerpo = cuerpo.cut(agujero(P.VARILLA_D, z0 - 1, P.Z_CORE1 + 1, xc, yc))
    cuerpo = cuerpo.cut(hexagono(P.M8_EC + P.HOLG_TUERCA, z0 - 1, z0 + P.M8_ALTO + 0.5, xc, yc))
    ranura = caja((xc - 0.6, xc + 0.6), (yc - P.R_NUCLEO - 1, yc - 8.0), (P.Z_CORE0, P.Z_CORE1 + 1))
    return cuerpo.cut(ranura).removeSplitter()


def carrete_superior():
    """Disco superior suelto: lo aprieta el cubo de la manivela."""
    xc, yc = P.X_CARRETE, P.Y_CARRETE
    d = cil(P.R_DISCO, P.Z_CORE1, P.Z_CORE1 + P.DISCO_ESP, xc, yc)
    return d.cut(agujero(P.VARILLA_D, P.Z_CORE1 - 1, P.Z_CORE1 + P.DISCO_ESP + 1, xc, yc))


def tuerca_carrete():
    return tuerca_m8(P.Z_CORE0 - P.DISCO_ESP + 0.3, P.X_CARRETE, P.Y_CARRETE)


def tuerca_manivela():
    return tuerca_m8(P.Z_MANIVELA + 0.3, P.X_CARRETE, P.Y_CARRETE)


def manivela():
    xc, yc = P.X_CARRETE, P.Y_CARRETE
    z0 = P.Z_MANIVELA
    cubo = cil(P.CUBO_R, z0, z0 + P.CUBO_ALTO, xc, yc)
    brazo = caja((xc, xc + P.R_MANIVELA), (yc - P.MANIVELA_ANCHO / 2, yc + P.MANIVELA_ANCHO / 2),
                 (z0, z0 + P.MANIVELA_ESP))
    punta = cil(P.MANIVELA_ANCHO / 2 + 2, z0, z0 + P.MANIVELA_ESP, xc + P.R_MANIVELA, yc)
    cuerpo = cubo.fuse(brazo).fuse(punta)
    cuerpo = cuerpo.cut(agujero(P.VARILLA_D, z0 - 1, z0 + P.CUBO_ALTO + 1, xc, yc))
    cuerpo = cuerpo.cut(hexagono(P.M8_EC + P.HOLG_TUERCA, z0 - 1, z0 + P.M8_ALTO + 0.5, xc, yc))
    cuerpo = cuerpo.cut(agujero(5.0, z0 - 1, z0 + P.MANIVELA_ESP + 1, xc + P.R_MANIVELA, yc))
    return cuerpo.removeSplitter()


def mango():
    x, y = P.X_CARRETE + P.R_MANIVELA, P.Y_CARRETE
    z0 = P.Z_MANIVELA + P.MANIVELA_ESP + 0.5
    return cil(P.MANGO_R, z0, z0 + P.MANGO_L, x, y).cut(agujero(5.0, z0 - 1, z0 + P.MANGO_L + 1, x, y))


def tornillo_mango():
    x, y = P.X_CARRETE + P.R_MANIVELA, P.Y_CARRETE
    z_top = P.Z_MANIVELA + P.MANIVELA_ESP + 0.5 + P.MANGO_L
    cab = cil(P.M5_CABEZA_D / 2, z_top, z_top + P.M5_CABEZA_ALTO, x, y)
    return cab.fuse(cil(2.5, z_top - P.TORNILLO_MANGO_L, z_top, x, y))


def tuerca_mango():
    x, y = P.X_CARRETE + P.R_MANIVELA, P.Y_CARRETE
    z_t = P.Z_MANIVELA - P.M5_TUERCA_ALTO
    return hexagono(P.M5_TUERCA_EC, z_t, P.Z_MANIVELA, x, y).cut(cil(2.5, z_t - 1, P.Z_MANIVELA + 1, x, y))


# -------------------------------------------------------------------- botella
def botella(s):
    """Cáscara de la botella después de cortar s mm: el borde sigue en la guía."""
    largo = P.ALTO_BOTELLA - s
    zt = P.z_superior_botella(s)
    xs = sorted(set([0.0, P.X_CUELLO_FIN] + [P.X_CUELLO_FIN + (P.X_HOMBRO_FIN - P.X_CUELLO_FIN) * k / 16
                                             for k in range(17)] + [largo]))
    xs = [x for x in xs if x <= largo]
    ext = [(P.radio_botella(x), zt - x) for x in xs]
    inte = []
    for x in reversed(xs):
        r = P.R_CUELLO_INT if x <= P.X_CUELLO_FIN else P.radio_botella(x) - P.PARED
        inte.append((r, zt - x))
    # en el fin del cuello el interior salta de la boca al hombro
    pts = ext + inte
    return revolucion(pts)


def tapa(s):
    zt = P.z_superior_botella(s)
    cuerpo = cil(15.0, zt - 12.0, zt + 2.0).cut(cil(P.R_CUELLO + 0.1, zt - 13.0, zt))
    return cuerpo.cut(cil(4.5, zt - 1, zt + 3))


def lastre(s):
    z0 = P.z_superior_botella(s) + 2.0
    vaso = cil(P.LASTRE_R, z0, z0 + P.LASTRE_ALTO).cut(
        cil(P.LASTRE_R - P.LASTRE_PARED, z0 + P.LASTRE_PARED, z0 + P.LASTRE_ALTO + 1))
    tubo = cil(P.VARILLA_D / 2 + 0.6 + P.LASTRE_PARED, z0, z0 + P.LASTRE_ALTO)
    return vaso.fuse(tubo).cut(agujero(P.VARILLA_D + 0.8, z0 - 1, z0 + P.LASTRE_ALTO + 1)).removeSplitter()


def tira(s):
    """Tramo libre, de la hoja al rollo (recto), y el rollo según s."""
    y0, y1 = P.R_B - P.PARED, P.R_B
    zc = (P.Z_GUIA, P.Z_GUIA + P.W)
    largo_hecho = math.pi * P.D_B * s / P.W
    r = math.sqrt(P.R_NUCLEO ** 2 + largo_hecho * P.PARED / math.pi)
    tramo = caja((0.0, P.X_CARRETE), (y0, y1), zc)
    partes = [tramo]
    if r > P.R_NUCLEO + 0.05:
        partes.append(cil(r, *zc, P.X_CARRETE, P.Y_CARRETE).cut(
            cil(P.R_NUCLEO, zc[0] - 1, zc[1] + 1, P.X_CARRETE, P.Y_CARRETE)))
    forma = partes[0]
    for p in partes[1:]:
        forma = forma.fuse(p)
    # el tramo recto termina donde toca el núcleo o el rollo
    return forma.cut(cil(min(r, P.R_NUCLEO) - 0.01, zc[0] - 1, zc[1] + 1, P.X_CARRETE, P.Y_CARRETE))


# -------------------------------------------------------------------- conjunto
def conjunto(s=0.0, con_lastre=True):
    """Todas las piezas armadas para el estado s."""
    pz = {}

    def add(nombre, forma, tipo, cantidad=1, nota="", impresion=None):
        pz[nombre] = {"forma": forma, "tipo": tipo, "cantidad": cantidad, "nota": nota,
                      "impresion": impresion if impresion is not None else a_la_cama(forma)}

    add("Base", mdf(), "comercial", nota="Tabla de MDF de 15 a 18 mm, 310 × 200 mm")
    add("Zocalo", zocalo(), "impresa", nota="Tuerca M8 cautiva hacia la cama")
    add("Varilla", varilla(), "comercial", nota="Varilla roscada M8 × 380")
    add("TuercaZocalo", tuerca_m8(0.3), "comercial", nota="Tuerca M8 cautiva")
    add("ContratuercaZocalo", arandela_m8(P.ZOCALO_ALTO).fuse(tuerca_m8(P.ZOCALO_ALTO + P.ARANDELA_M8[2])),
        "comercial", nota="Arandela y tuerca M8 que traban la varilla")
    add("Cabezal", cabezal(), "impresa", nota="Piso de la guía arriba; sin soportes")
    add("Chapita", chapita(), "comercial", nota="Fleje de ~0,5 mm, 36 × 2,8 mm")
    add("Calce", calce(P.W), "impresa", nota="Uno por ancho: 7, 8, 9 y 10 mm")
    add("Hoja", hoja(), "comercial", nota="Trincheta de 18 mm")
    add("Pisador", pisador(), "impresa")
    add("TornillosHoja", tornillos_hoja(), "comercial", 2, "M3 × 25")
    add("TuercasHoja", tuercas_hoja(), "comercial", 2, "Tuerca M3, entra de costado")
    add("Ojal", ojal(), "impresa")
    add("Torre", torre(), "impresa", nota="Dos 608ZZ a presión desde arriba")
    add("Rodamientos", rodamientos(), "comercial", 2, "608ZZ")
    add("EjeCarrete", eje_carrete(), "comercial", nota="Tornillo M8 × 60 rosca completa, con arandela")
    add("ArandelaCarrete", arandela_superior(), "comercial", nota="Arandela M8")
    add("CarreteInferior", carrete_inferior(), "impresa", nota="Tuerca M8 cautiva hacia la cama")
    add("CarreteSuperior", carrete_superior(), "impresa")
    add("TuercaCarrete", tuerca_carrete(), "comercial", nota="Tuerca M8 cautiva en el carrete")
    add("Manivela", manivela(), "impresa", nota="Tuerca M8 cautiva hacia la cama")
    add("TuercaManivela", tuerca_manivela(), "comercial", nota="Tuerca M8 cautiva en la manivela")
    add("Mango", mango(), "impresa")
    add("TornilloMango", tornillo_mango(), "comercial", nota="M5 × 70")
    add("TuercaMango", tuerca_mango(), "comercial", nota="Tuerca autoblocante M5")
    add("Botella", botella(s), "botella")
    add("Tapa", tapa(s), "botella", nota="La tapa de la botella, perforada a 9 mm")
    if con_lastre:
        add("Lastre", lastre(s), "impresa", nota="Opcional: se llena de tuercas o arena")
    add("Tira", tira(s), "botella")
    return pz


def calces_todos():
    """Los cuatro calces, para exportar: el armado solo lleva el de W."""
    return {f"Calce_{int(w)}mm": calce(w) for w in P.CALCES}
