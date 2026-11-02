# -*- coding: utf-8 -*-
"""
Constructores de las piezas. Todo se arma en la posición de partida (carro en
s = 0, manivela en 0 vueltas); la cinemática después solo cambia Placements.

Cada pieza pertenece a un grupo según cómo se mueve, y el color de los videos
sale de ese grupo (E2, 5.1):
  fijo   unido a la base
  carro  se traslada con el carro
  gira   se traslada con el carro y además rota
"""
import math

import FreeCAD as App
import Part

import parametros as P

V = App.Vector
EJE_X = V(1, 0, 0)


def cil(r, x0, x1, y=0.0, z=None):
    """Cilindro de eje paralelo a X."""
    z = P.H_EJE if z is None else z
    return Part.makeCylinder(r, x1 - x0, V(x0, y, z), EJE_X)


def caja(x, y, z):
    return Part.makeBox(x[1] - x[0], y[1] - y[0], z[1] - z[0], V(x[0], y[0], z[0]))


def engranaje(z, x0, x1, y, zc, fase_grados, r_agujero, juego=0.08):
    """Dientes involutos con 20° de presión. El diente queda centrado en
    fase_grados; juego: lo que se le quita a cada flanco, en mm."""
    m = P.MODULO
    rp, ra, rf = m * z / 2, m * (z + 2) / 2, m * (z - 2.5) / 2
    rb = rp * math.cos(math.radians(20))
    inv = lambda alfa: math.tan(alfa) - alfa
    ap = math.radians(20)
    r0 = max(rb, rf)
    radios = [r0 + (ra - r0) * k / 5 for k in range(6)]
    fase = math.radians(fase_grados)

    def punto(r, ang):
        return V(x0, y + r * math.cos(ang), zc + r * math.sin(ang))

    pts = []
    for k in range(z):
        c = fase + 2 * math.pi * k / z
        flanco = []
        for r in radios:
            ar = math.acos(min(1.0, rb / r))
            med = math.pi / (2 * z) - juego / rp + inv(ap) - inv(ar)
            flanco.append((r, med))
        pts.append(punto(rf, c - flanco[0][1]))
        pts += [punto(r, c - med) for r, med in flanco]
        pts += [punto(r, c + med) for r, med in reversed(flanco)]
        pts.append(punto(rf, c + flanco[0][1]))
    pts.append(pts[0])
    cara = Part.Face(Part.makePolygon(pts))
    cuerpo = cara.extrude(V(x1 - x0, 0, 0))
    return cuerpo.cut(cil(r_agujero, x0 - 1, x1 + 1, y, zc))


def fases_engrane():
    """Fases para que un diente del conductor entre en un hueco del conducido.
    El conducido está debajo: la línea de centros es -90° desde el conductor."""
    return -90.0, 90.0 + 180.0 / P.Z_2


def botella_solida():
    """Envolvente llena de la botella, para buscar choques."""
    n = 40
    z = P.H_EJE
    perfil = [V(0, 0, z), V(0, P.R_CUELLO, z)]
    for k in range(n + 1):
        x = P.X_CUELLO_FIN + (P.X_HOMBRO_FIN - P.X_CUELLO_FIN) * k / n
        perfil.append(V(x, P.radio_botella(x), z))
    perfil += [V(P.X_BORDE, P.R_B, z), V(P.X_BORDE, 0, z), V(0, 0, z)]
    # Con la geometría ya en su lugar: colocar() pisa el Placement de la forma.
    return Part.Face(Part.makePolygon(perfil)).revolve(V(0, 0, z), EJE_X, 360)


def manivela(x_brazo=None, sentido=-1):
    """Cubo, brazo y mango, con el brazo en x_brazo. sentido: hacia dónde sale
    el mango (-1 = hacia -X, +1 = hacia +X)."""
    x = P.X_MANIVELA if x_brazo is None else x_brazo
    y, z = P.Y_R, P.Z_R
    cubo = cil(20, x - 6, x + 6, y, z)
    brazo = caja((x - 5, x + 5), (y - 9, y + 9), (z, z + P.R_MANIVELA))
    r = P.R_MANGO
    if sentido < 0:
        vastago = cil(r * 0.5, x - 8, x + 5, y, z + P.R_MANIVELA)
        mango = cil(r, x - 8 - P.LARGO_MANGO, x - 8, y, z + P.R_MANIVELA)
    else:
        vastago = cil(r * 0.5, x - 5, x + 8, y, z + P.R_MANIVELA)
        mango = cil(r, x + 8, x + 8 + P.LARGO_MANGO, y, z + P.R_MANIVELA)
    return cubo.fuse([brazo, vastago, mango]).removeSplitter()


def barrido_manivela(x_brazo=None, sentido=-1):
    """Volumen que barre la manivela al dar una vuelta completa."""
    x = P.X_MANIVELA if x_brazo is None else x_brazo
    r = P.R_MANIVELA + P.R_MANGO
    if sentido < 0:
        return cil(r, x - 8 - P.LARGO_MANGO, x + 6, P.Y_R, P.Z_R)
    return cil(r, x - 6, x + 8 + P.LARGO_MANGO, P.Y_R, P.Z_R)


def placa_caja(x):
    """Placa que sostiene los dos ejes a distancia fija. Al ser concéntrica con
    el husillo, también podría pivotar sobre él (ver hallazgos)."""
    y = P.Y_R
    rs, ri = P.R_PLACA_EJE, P.R_PLACA_HUSILLO
    arriba = cil(rs, x[0], x[1], y, P.Z_R)
    abajo = cil(ri, x[0], x[1], y, P.Z_H)
    alma = Part.Face(Part.makePolygon([
        V(x[0], y - rs, P.Z_R), V(x[0], y + rs, P.Z_R),
        V(x[0], y + ri, P.Z_H), V(x[0], y - ri, P.Z_H), V(x[0], y - rs, P.Z_R),
    ])).extrude(V(x[1] - x[0], 0, 0))
    pie = caja(x, (y - ri, y + ri), (P.Z_CARRO[1], P.Z_H))
    forma = arriba.fuse([abajo, alma, pie]).removeSplitter()
    forma = forma.cut(cil(P.D_EJE / 2 + 0.3, x[0] - 1, x[1] + 1, y, P.Z_R))
    return forma.cut(cil(P.D_HUSILLO / 2 + 0.3, x[0] - 1, x[1] + 1, y, P.Z_H))


def soporte_cuello():
    """Porta rodamientos de 70 × 80 sobre un pie, unido al carro (E2, 5.4)."""
    x, a, h = P.X_SOPORTE, P.ANCHO_SOPORTE / 2, P.ALTO_SOPORTE / 2
    cabeza = caja(x, (-a, a), (P.H_EJE - h, P.H_EJE + h))
    pie = caja(x, (-a * 0.7, a * 0.7), (P.Z_CARRO[1], P.H_EJE - h))
    agujero = cil(P.D_ROD_CUELLO[1] / 2, x[0] - 1, x[1] + 1)
    return cabeza.fuse(pie).removeSplitter().cut(agujero)


def portacuchilla():
    """Fijo a la base, afuera del carro: el carro pasa por al lado."""
    xk = P.X_CUCHILLA
    xs = (xk - 14, xk - 2)
    z = P.H_EJE
    poste = caja(xs, (-105, -88), (0, z + 6))
    brazo = caja(xs, (-88, -P.R_B - 6), (z - 6, z + 6))
    perilla = cil(9, xs[0] - 8, xs[0], -96, z)
    return poste.fuse([brazo, perilla]).removeSplitter()


def cuchilla():
    """Hoja comercial [E2, 5.4]. Entra apenas en la pared; el filo mira hacia
    arriba, porque la pared le llega de arriba hacia abajo (ver hallazgos)."""
    xk, z, r = P.X_CUCHILLA, P.H_EJE, P.R_B
    puntos = [V(xk - 2.6, -r - 6, z - 7), V(xk - 2.6, -r + 0.6, z - 1),
              V(xk - 2.6, -r - 6, z + 7), V(xk - 2.6, -r - 6, z - 7)]
    return Part.Face(Part.makePolygon(puntos)).extrude(V(3.0, 0, 0))


def tuerca_y_poste():
    x = P.X_TUERCA
    y, z = P.Y_H, P.Z_H
    poste = caja(x, (y - 15, y + 15), (0, z - 11))
    cuerpo = cil(16, x[0], x[1], y, z)
    forma = poste.fuse(cuerpo).removeSplitter()
    return forma.cut(cil(P.D_HUSILLO / 2, x[0] - 1, x[1] + 1, y, z))


def formas():
    """Todas las piezas sólidas: nombre → (forma, grupo, centro de giro, clave
    del ángulo en parametros.estado)."""
    f1, f2 = fases_engrane()
    r_eje = P.D_EJE / 2
    y, zr, zh = P.Y_R, P.Z_R, P.Z_H
    x_rod = P.X_RODILLO

    base = caja(P.X_BASE, P.Y_BASE, (-P.ESPESOR_BASE, 0))
    guias = [cil(P.D_GUIA / 2, P.X_GUIAS[0], P.X_GUIAS[1], yg, P.Z_GUIA)
             for yg in P.Y_GUIAS]
    apoyos = []
    for yg in P.Y_GUIAS:
        for x0 in (P.X_GUIAS[0] - 5, P.X_GUIAS[1] - 5):
            apoyos.append(caja((x0, x0 + 10), (yg - 12, yg + 12), (0, P.Z_GUIA + 9)))
    guias_todo = guias[0].fuse(guias[1:] + apoyos)

    patines = []
    for yg in P.Y_GUIAS:
        for x0 in (0.0, 44.0):
            p = caja((x0, x0 + 24), (yg - 12, yg + 12), (P.Z_GUIA - 7.5, P.Z_CARRO[0]))
            patines.append(p.cut(cil(P.D_GUIA / 2, x0 - 1, x0 + 25, yg, P.Z_GUIA)))
    carro = caja(P.X_CARRO, P.Y_CARRO, P.Z_CARRO).fuse(patines).removeSplitter()

    nucleo = cil(r_eje + 5, x_rod[0], x_rod[1], y, zr)
    elast = cil(P.D_R / 2, x_rod[0], x_rod[1], y, zr).cut(nucleo)

    mordaza_a = cil(P.D_ROD_CUELLO[0] / 2, *P.X_MORDAZA).cut(
        cil(P.R_CUELLO + 0.05, P.X_MORDAZA[0] - 1, P.X_MORDAZA[1] + 1))
    aro_int = cil(P.D_ROD_CUELLO[0] / 2 + 5, 8, 20).cut(
        cil(P.D_ROD_CUELLO[0] / 2, 7, 21))
    aro_ext = cil(P.D_ROD_CUELLO[1] / 2, 8, 20).cut(
        cil(P.D_ROD_CUELLO[0] / 2 + 5.3, 7, 21))
    collares = cil(9, 25, 28, y, zh).fuse(cil(9, 40, 42, y, zh))

    pz = {
        "Base": (base, "fijo", None, None),
        "Guias": (guias_todo, "fijo", None, None),
        "Tuerca": (tuerca_y_poste(), "fijo", None, None),
        "Portacuchilla": (portacuchilla(), "fijo", None, None),
        "Cuchilla": (cuchilla(), "filo", None, None),
        "Carro": (carro, "carro", None, None),
        "SoporteCuello": (soporte_cuello(), "carro", None, None),
        "RodamientoCuello": (aro_ext, "carro", None, None),
        "Placa1": (placa_caja(P.X_PLACA_1), "carro", None, None),
        "Placa2": (placa_caja(P.X_PLACA_2), "carro", None, None),
        "Mordaza": (mordaza_a.fuse(aro_int).removeSplitter(), "gira",
                    (0.0, P.H_EJE), "botella"),
        "Eje": (cil(r_eje, P.X_EJE[0], P.X_EJE[1], y, zr), "gira", (y, zr), "rodillo"),
        "NucleoRodillo": (nucleo.cut(cil(r_eje, x_rod[0] - 1, x_rod[1] + 1, y, zr)),
                          "gira", (y, zr), "rodillo"),
        "Rodillo": (elast, "elastomero", (y, zr), "rodillo"),
        "Manivela": (manivela(), "gira", (y, zr), "rodillo"),
        "EngranajeZ1": (engranaje(P.Z_1, *P.X_ENGRANAJES, y, zr, f1, r_eje),
                        "gira", (y, zr), "rodillo"),
        "EngranajeZ2": (engranaje(P.Z_2, *P.X_ENGRANAJES, y, zh, f2, P.D_HUSILLO / 2),
                        "gira", (y, zh), "husillo"),
        "Collares": (collares, "gira", (y, zh), "husillo"),
    }
    return pz


def husillo_liso():
    """El husillo como cilindro, para buscar choques; la rosca real es malla."""
    return cil(P.D_HUSILLO / 2, P.X_HUSILLO_INI, P.X_HUSILLO_FIN, P.Y_H, P.Z_H)


def colocar(forma, grupo, centro, clave, est):
    """Devuelve el Placement de una pieza según el estado de la cinemática."""
    s = 0.0 if grupo in ("fijo", "filo") else est["s"]
    if centro is None:
        return App.Placement(V(s, 0, 0), App.Rotation())
    rot = App.Rotation(EJE_X, est[clave])
    c = V(0, centro[0], centro[1])
    return App.Placement(V(s, 0, 0) + c - rot.multVec(c), rot)
