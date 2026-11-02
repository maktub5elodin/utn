# -*- coding: utf-8 -*-
"""
Figuras y cuadros del video. Necesita la interfaz de FreeCAD (sin pantalla):
    QT_QPA_PLATFORM=offscreen RENDER=figuras ~/Aplicaciones/FreeCAD.AppImage renderizar.py
    QT_QPA_PLATFORM=offscreen RENDER=video TANDA=0/8 ~/Aplicaciones/FreeCAD.AppImage renderizar.py
Lo lanza el Makefile. También guarda el modelo en modelo/cortadora_pet.FCStd.
"""
import json, math, os, sys, traceback

CARPETA = os.environ.get("CARPETA_MODELO", os.getcwd())
sys.path.insert(0, CARPETA)

import FreeCAD as App
import FreeCADGui as Gui
import Mesh
import Part
from PIL import Image, ImageDraw, ImageFont
from pivy import coin

import parametros as P
import piezas as Z

V = App.Vector
ANCHO, ALTO = 1920, 1080
SS = 2                      # supermuestreo: se renderiza al doble y se reduce
FPS = 30
SEG_INTRO, SEG_CORTE, SEG_FINAL = 3.0, 30.0, 3.0

COLORES = {
    "fijo": (0.30, 0.33, 0.38),
    "carro": (0.13, 0.42, 0.72),
    "gira": (0.95, 0.50, 0.12),
    "elastomero": (0.10, 0.10, 0.11),
    "filo": (0.82, 0.84, 0.87),
}
COLOR_PET = (0.55, 0.85, 0.72)
COLOR_MARCA = (0.98, 0.78, 0.15)


# ----------------------------------------------------------- mallas que cambian
def malla_grilla(filas):
    """Triángulos de una grilla de puntos: filas[i][j] = (x, y, z)."""
    tri = []
    for a, b in zip(filas, filas[1:]):
        for j in range(len(a) - 1):
            tri.append([a[j], b[j], b[j + 1]])
            tri.append([a[j], b[j + 1], a[j + 1]])
    return Mesh.Mesh(tri)


def punto_local(x, r, th):
    return (x, r * math.cos(th), P.H_EJE + r * math.sin(th))


def malla_botella_fija():
    """Cuello, hombro y franja: lo que nunca se corta."""
    xs = [0.0, 3.0, 3.01, 8.0, 8.01, 13.0, 13.01, 18.0, 18.01, P.X_CUELLO_FIN]
    rs = [14.0, 14.0, 15.2, 15.2, 14.0, 14.0, 15.2, 15.2, 16.8, 16.8]
    n = 40
    for k in range(1, n + 1):
        x = P.X_CUELLO_FIN + (P.X_HOMBRO_FIN - P.X_CUELLO_FIN) * k / n
        xs.append(x)
        rs.append(P.radio_botella(x))
    xs.append(P.X_FRANJA_FIN)
    rs.append(P.R_B)
    columnas = 96
    filas = []
    for x, r in zip(xs, rs):
        filas.append([punto_local(x, r, 2 * math.pi * j / columnas)
                      for j in range(columnas + 1)])
    return malla_grilla(filas)


def malla_marcas():
    """Marcas sobre la franja, para que se vea girar la botella."""
    tri = []
    for k in range(6):
        c = 2 * math.pi * k / 6
        filas = []
        for x in (P.X_FRANJA_FIN - 7, P.X_FRANJA_FIN - 1):
            filas.append([punto_local(x, P.R_B + 0.25, c + t * 0.09) for t in (-1, 0, 1)])
        tri.append(malla_grilla(filas))
    m = tri[0]
    for o in tri[1:]:
        m.addMesh(o)
    return m


def malla_cuerpo(est):
    """Lo que queda del cuerpo: cada generatriz llega hasta el borde helicoidal.
    Coordenadas de la botella. La columna 0 cae justo en la cuchilla, donde la
    hélice salta un paso a."""
    x_corte = P.X_BORDE - est["s"]
    th_k = math.pi - math.radians(est["botella"])
    columnas, filas_n = 120, 28
    filas = []
    for i in range(filas_n + 1):
        w = i / filas_n
        fila = []
        for j in range(columnas + 1):
            f = j / columnas
            x_e = min(P.X_BORDE, x_corte + P.PASO_A * f)
            fila.append(punto_local(P.X_FRANJA_FIN + (x_e - P.X_FRANJA_FIN) * w,
                                    P.R_B, th_k + 2 * math.pi * f))
        filas.append(fila)
    return malla_grilla(filas)


def malla_helice_futura(est):
    """Línea fina sobre la pared todavía sin cortar: por dónde va a pasar la
    cuchilla. Hace visible el paso a."""
    x_corte = P.X_BORDE - est["s"]
    th_k = math.pi - math.radians(est["botella"])
    fila_a, fila_b = [], []
    pasos = int(max(0.0, x_corte - P.X_FRANJA_FIN) / P.PASO_A * 48)
    if pasos < 2:
        return None
    for k in range(pasos + 1):
        dx = k / 48 * P.PASO_A
        th = th_k - k / 48 * 2 * math.pi
        fila_a.append(punto_local(x_corte - dx - 0.25, P.R_B + 0.08, th))
        fila_b.append(punto_local(x_corte - dx + 0.25, P.R_B + 0.08, th))
    return malla_grilla([fila_a, fila_b])


def malla_tira(est, vueltas):
    """La tira: sale de la cuchilla hacia abajo y afuera, y cuelga. El recorrido
    es ilustrativo: E2 solo pide una salida libre y alejada de lo que se mueve."""
    largo = P.LARGO_TIRA * vueltas / P.VUELTAS_MANIVELA_TOTAL
    largo = max(1.0, min(largo, 460.0))
    a = P.PASO_A
    xk = P.X_CUCHILLA
    # Tramos: arco de radio 60, arco de radio 25, recta hacia abajo.
    y0, z0 = -P.R_B - 0.4, P.H_EJE
    r1, r2 = 60.0, 25.0
    l1, l2 = r1 * math.pi / 2, r2 * math.pi / 2

    def centro(l):
        if l <= l1:
            t = l / r1
            return y0 - r1 + r1 * math.cos(t), z0 - r1 * math.sin(t)
        if l <= l1 + l2:
            t = (l - l1) / r2
            yc, zc = y0 - r1, z0 - r1 - r2
            return yc - r2 * math.sin(t), zc + r2 * math.cos(t)
        return y0 - r1 - r2, z0 - r1 - r2 - (l - l1 - l2)

    filas = []
    n = max(2, int(largo / 5))
    fase = P.LARGO_TIRA * vueltas / P.VUELTAS_MANIVELA_TOTAL / 18
    for k in range(n + 1):
        l = largo * k / n
        y, z = centro(l)
        e = max(0.0, (l - l1 - l2) / 200)
        y -= 7 * min(e, 1) * (1 + math.sin(l / 26 - fase))
        dx = 5 * min(e, 1) * math.sin(l / 38 - fase * 0.7)
        filas.append([(xk + dx, y, z), (xk + dx + a, y, z)])
    return malla_grilla(filas)


def malla_husillo():
    """Rosca real de 4 entradas y sentido derecho: el radio depende de la fase
    (x/L - θ/2π), y una línea de cresta avanza con θ. Se mueve con Placement."""
    columnas = 72
    dx = 0.33
    r_c, r_f = P.D_HUSILLO / 2, P.D_HUSILLO / 2 - 1.1
    y, z = P.Y_H, P.Z_H

    def radio(x, th):
        u = (x / P.L_HUSILLO - th / (2 * math.pi)) * P.ENTRADAS % 1.0
        if u < 0.14 or u > 0.86:
            return r_f
        if 0.36 < u < 0.64:
            return r_c
        return r_f + (r_c - r_f) * ((u - 0.14) / 0.22 if u < 0.5 else (0.86 - u) / 0.22)

    n = int((P.X_HUSILLO_FIN - P.X_HUSILLO_INI) / dx)
    filas = []
    for i in range(n + 1):
        x = P.X_HUSILLO_INI + i * dx
        fila = []
        for j in range(columnas + 1):
            th = 2 * math.pi * j / columnas
            r = radio(x, th)
            fila.append((x, y + r * math.cos(th), z + r * math.sin(th)))
        filas.append(fila)
    return malla_grilla(filas)


# --------------------------------------------------------------- armar documento
class Escena:
    def __init__(self):
        self.doc = App.newDocument("Cortadora_PET")
        self.piezas = {}
        for nombre, (forma, grupo, centro, clave) in Z.formas().items():
            o = self.doc.addObject("Part::Feature", nombre)
            o.Shape = forma
            o.ViewObject.ShapeColor = COLORES[grupo]
            o.ViewObject.DisplayMode = "Shaded" if grupo != "fijo" else "Flat Lines"
            if hasattr(o.ViewObject, "LineWidth"):
                o.ViewObject.LineWidth = 1.0
            if nombre.startswith("Placa"):   # dejan ver los engranajes
                o.ViewObject.Transparency = 72
            self.piezas[nombre] = (o, grupo, centro, clave)
        self.mallas = {}
        self._malla("BotellaFija", malla_botella_fija(), COLOR_PET, 55, (0.0, P.H_EJE), "botella")
        self._malla("Marcas", malla_marcas(), COLOR_MARCA, 0, (0.0, P.H_EJE), "botella")
        self._malla("Husillo", malla_husillo(), COLORES["gira"], 0, (P.Y_H, P.Z_H), "husillo")
        self._malla("Cuerpo", Mesh.Mesh(), COLOR_PET, 55, (0.0, P.H_EJE), "botella")
        self._malla("Helice", Mesh.Mesh(), (0.05, 0.28, 0.20), 62, (0.0, P.H_EJE), "botella")
        self._malla("Tira", Mesh.Mesh(), (0.35, 0.78, 0.60), 15, None, None, fija=True)
        self.doc.recompute()
        self.vista = Gui.getDocument(self.doc.Name).activeView()
        self.vista.setAnimationEnabled(False)
        self.vista.setCameraType("Perspective")
        self.cam = self.vista.getCameraNode()

    def _malla(self, nombre, malla, color, transp, centro, clave, fija=False):
        o = self.doc.addObject("Mesh::Feature", nombre)
        o.Mesh = malla
        o.ViewObject.ShapeColor = color
        o.ViewObject.Transparency = transp
        if hasattr(o.ViewObject, "Lighting"):
            o.ViewObject.Lighting = "Two side"
        self.mallas[nombre] = (o, centro, clave, fija)

    def posar(self, vueltas):
        est = P.estado(vueltas)
        for o, grupo, centro, clave in self.piezas.values():
            o.Placement = Z.colocar(None, grupo, centro, clave, est)
        self.mallas["Cuerpo"][0].Mesh = malla_cuerpo(est)
        h = malla_helice_futura(est)
        self.mallas["Helice"][0].Mesh = h if h is not None else Mesh.Mesh()
        self.mallas["Tira"][0].Mesh = malla_tira(est, vueltas)
        for o, centro, clave, fija in self.mallas.values():
            if fija:
                continue
            o.Placement = Z.colocar(None, "gira", centro, clave, est)
        return est

    def camara(self, pos, obj, angulo=32.0):
        self.cam.position.setValue(coin.SbVec3f(*pos))
        self.cam.pointAt(coin.SbVec3f(*obj), coin.SbVec3f(0, 0, 1))
        if hasattr(self.cam, "heightAngle"):
            self.cam.heightAngle.setValue(math.radians(angulo))
        self.cam.nearDistance.setValue(30)
        self.cam.farDistance.setValue(6000)

    def proyector(self):
        vv = self.cam.getViewVolume(ANCHO / ALTO)

        def f(p):
            s = vv.projectToScreen(coin.SbVec3f(*p))
            return s[0] * ANCHO, (1 - s[1]) * ALTO
        return f

    def foto(self, ruta):
        crudo = ruta + ".crudo.png"
        self.vista.saveImage(crudo, ANCHO * SS, ALTO * SS, "#F4F5F7")
        img = Image.open(crudo).convert("RGB").resize((ANCHO, ALTO), Image.LANCZOS)
        os.remove(crudo)
        return img


# ------------------------------------------------------------ textos sobre la imagen
TINTA = (32, 36, 44)
SUAVE = (98, 104, 116)
_F = {"n": "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
      "b": "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"}


def fuente(e, px):
    ruta = _F[e]
    if not os.path.exists(ruta):
        ruta = "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if e == "b" else "")
    return ImageFont.truetype(ruta, px)


def rgb255(c):
    return tuple(round(v * 255) for v in c)


def leyenda(d):
    x, y = 40, ALTO - 46
    d.rounded_rectangle((24, y - 12, 760, y + 34), 10, fill=(255, 255, 255, 225))
    for nombre, c in (("fijo a la base", COLORES["fijo"]),
                      ("se traslada con el carro", COLORES["carro"]),
                      ("se traslada y gira", COLORES["gira"])):
        d.rounded_rectangle((x, y, x + 22, y + 22), 5, fill=rgb255(c))
        d.text((x + 30, y - 3), nombre, font=fuente("n", 22), fill=TINTA)
        x += 62 + d.textlength(nombre, font=fuente("n", 22))


def panel(d, vueltas):
    est = P.estado(vueltas)
    vb = est["botella"] / 360
    tira = P.LARGO_TIRA * vueltas / P.VUELTAS_MANIVELA_TOTAL / 1000
    filas = [("Manivela", f"{vueltas:5.1f} vueltas"),
             ("Botella", f"{vb:5.1f} vueltas"),
             ("Avance del carro", f"{est['s']:5.1f} mm"),
             ("Tira cortada", f"{tira:5.2f} m")]
    x0, y0, w, alto = 40, 36, 420, 40 + 40 * len(filas) + 58
    d.rounded_rectangle((x0, y0, x0 + w, y0 + alto), 14, fill=(255, 255, 255, 235),
                        outline=(214, 218, 224), width=2)
    y = y0 + 20
    for k, v in filas:
        d.text((x0 + 22, y), k, font=fuente("n", 24), fill=SUAVE)
        t = v
        d.text((x0 + w - 22 - d.textlength(t, font=fuente("b", 25)), y - 1), t,
               font=fuente("b", 25), fill=TINTA)
        y += 40
    d.line((x0 + 22, y + 4, x0 + w - 22, y + 4), fill=(214, 218, 224), width=2)
    d.text((x0 + 22, y + 14), f"a = L·Db / (i·Dr) = {P.PASO_A:.1f} mm/vuelta",
           font=fuente("b", 24), fill=rgb255(COLORES["gira"]))


def rotulos(d, proy, est, lista):
    """lista: (texto, punto 3D en reposo, se mueve con el carro, x, y de la caja)."""
    f = fuente("b", 25)
    for texto, p, movil, x, y in lista:
        q = (p[0] + (est["s"] if movil else 0), p[1], p[2])
        px, py = proy(q)
        w = d.textlength(texto, font=f)
        d.line((x + w / 2, y + 20, px, py), fill=TINTA, width=2)
        d.ellipse((px - 5, py - 5, px + 5, py + 5), fill=TINTA)
        d.rounded_rectangle((x - 12, y - 4, x + w + 12, y + 38), 8, fill=(255, 255, 255, 240),
                            outline=(204, 208, 214), width=2)
        d.text((x, y), texto, font=f, fill=TINTA)


def titulo(d, texto, sub):
    w = d.textlength(texto, font=fuente("b", 46))
    d.text(((ANCHO - w) / 2, 34), texto, font=fuente("b", 46), fill=TINTA)
    w = d.textlength(sub, font=fuente("n", 26))
    d.text(((ANCHO - w) / 2, 98), sub, font=fuente("n", 26), fill=SUAVE)


def pie(d):
    t = "Modelo de estudio: medidas de referencia, no definitivas"
    w = d.textlength(t, font=fuente("n", 22))
    d.rounded_rectangle((ANCHO - w - 56, ALTO - 58, ANCHO - 24, ALTO - 12), 10,
                        fill=(255, 255, 255, 225))
    d.text((ANCHO - w - 40, ALTO - 46), t, font=fuente("n", 22), fill=SUAVE)


def componer(img, dibujar):
    capa = Image.new("RGBA", img.size, (0, 0, 0, 0))
    dibujar(ImageDraw.Draw(capa))
    return Image.alpha_composite(img.convert("RGBA"), capa).convert("RGB")


# ------------------------------------------------------------------ cámara del video
OBJ_C = (180.0, 0.0, 100.0)
PLANOS = [  # (segundo del corte, posición, objetivo, ángulo, cuánto sigue al carro)
    (0.0, (-330, 900, 480), OBJ_C, 24, 0),
    (5.0, (-260, 800, 380), (150, 20, 110), 26, 0),
    (9.0, (-230, 620, 300), (30, 60, 105), 26, 1),      # transmisión
    (16.0, (-200, 620, 280), (30, 60, 105), 26, 1),
    (20.0, (380, -560, 330), (300, -40, 150), 24, 0),   # cuchilla
    (25.0, (470, -520, 300), (330, -40, 140), 24, 0),
    (30.0, (820, 760, 520), (230, 0, 100), 25, 0),
]


def suave(t):
    return t * t * (3 - 2 * t)


def plano(seg, s):
    for a, b in zip(PLANOS, PLANOS[1:]):
        if seg <= b[0]:
            t = suave((seg - a[0]) / (b[0] - a[0]))
            sigue = (a[4] + (b[4] - a[4]) * t) * s
            pos = [a[1][i] + (b[1][i] - a[1][i]) * t for i in range(3)]
            obj = [a[2][i] + (b[2][i] - a[2][i]) * t for i in range(3)]
            pos[0] += sigue
            obj[0] += sigue
            return pos, obj, a[3] + (b[3] - a[3]) * t
    return PLANOS[-1][1], PLANOS[-1][2], PLANOS[-1][3]


def rotulos_video(seg):
    """Cada plano nombra lo que muestra, con las palabras de E2."""
    if 9.0 <= seg <= 16.0:
        return [("Manivela", (P.X_MANIVELA, P.Y_R + 20, P.Z_R), True, 1540, 300),
                ("Rodillo", (100, P.Y_R + 14, P.Z_R + 14), True, 560, 330),
                ("Engranajes z1 = 20 / z2 = 40", (47, P.Y_R + 42, P.Z_H), True, 1300, 800),
                ("Husillo", (150, P.Y_H + 3, P.Z_H), True, 300, 800)]
    if 20.5 <= seg <= 25.0:
        return [("Cuchilla fija", (P.X_CUCHILLA, -P.R_B - 3, P.H_EJE), False, 700, 190),
                ("Tira", (P.X_CUCHILLA + 3, -P.R_B - 62, P.H_EJE - 62), False, 1250, 800)]
    return []


def cuadro_video(esc, i, ruta):
    seg = i / FPS
    if seg < SEG_INTRO:
        vueltas, s_corte = 0.0, 0.0
    elif seg < SEG_INTRO + SEG_CORTE:
        s_corte = seg - SEG_INTRO
        vueltas = P.VUELTAS_MANIVELA_TOTAL * s_corte / SEG_CORTE
    else:
        vueltas, s_corte = P.VUELTAS_MANIVELA_TOTAL, SEG_CORTE
    est = esc.posar(vueltas)
    pos, obj, ang = plano(s_corte, est["s"])
    esc.camara(pos, obj, ang)
    img = esc.foto(ruta)
    proy = esc.proyector()

    def dibujar(d):
        leyenda(d)
        pie(d)
        if seg < SEG_INTRO:
            titulo(d, "Cortadora manual de botellas PET",
                   "Una sola entrada: la manivela hace girar la botella y hace avanzar el carro")
        elif seg < SEG_INTRO + SEG_CORTE:
            panel(d, vueltas)
            rotulos(d, proy, est, rotulos_video(s_corte))
        else:
            panel(d, vueltas)
            titulo(d, "Corte terminado",
                   f"{P.VUELTAS_MANIVELA_TOTAL:.0f} vueltas de manivela, {P.LARGO_TIRA / 1000:.1f} m de tira; "
                   "queda la franja del rodillo")
    img = componer(img, dibujar)
    img.save(ruta + ".tmp.png")
    os.replace(ruta + ".tmp.png", ruta)      # un cuadro a medias nunca queda con su nombre


# ----------------------------------------------------------------------- figuras
def figuras(esc):
    salida = os.path.join(CARPETA, "figuras")
    os.makedirs(salida, exist_ok=True)

    def toma(nombre, vueltas, pos, obj, ang, dibujar=None):
        est = esc.posar(vueltas)
        esc.camara(pos, obj, ang)
        ruta = os.path.join(salida, nombre)
        img = esc.foto(ruta)
        proy = esc.proyector()
        img = componer(img, lambda d: (leyenda(d), pie(d),
                                       dibujar(d, proy, est) if dibujar else None))
        img.save(ruta)

    def rot_inicio(d, proy, est):
        titulo(d, "Conjunto al inicio del corte", "Carro atrás, cuchilla en el borde abierto")
        rotulos(d, proy, est, [
            ("Manivela", (P.X_MANIVELA - 40, P.Y_R, P.Z_R + P.R_MANIVELA), True, 1560, 300),
            ("Sujeción del cuello", (14, 0, P.H_EJE + 40), True, 1240, 190),
            ("Rodillo", (100, P.Y_R + 14, P.Z_R - 20), True, 830, 700),
            ("Engranajes", (47, P.Y_R, P.Z_H + 10), True, 1560, 660),
            ("Husillo", (180, P.Y_H + 3, P.Z_H), True, 590, 780),
            ("Tuerca fija", (P.X_TUERCA[0] + 10, P.Y_H + 15, 40), False, 370, 590),
            ("Cuchilla fija", (P.X_CUCHILLA, -P.R_B, P.H_EJE + 6), False, 500, 210)])

    def rot_fin(d, proy, est):
        titulo(d, "Conjunto al final del corte",
               f"El carro avanzó {P.RECORRIDO:.0f} mm; queda la franja del rodillo sin cortar")

    toma("conjunto_inicio.png", 0.0, (-330, 900, 480), OBJ_C, 28, rot_inicio)
    toma("conjunto_mitad.png", P.VUELTAS_MANIVELA_TOTAL * 0.5, (-300, 880, 470), (240, 0, 100), 32,
         lambda d, proy, est: (titulo(d, "A mitad del corte", ""), panel(d, P.VUELTAS_MANIVELA_TOTAL * 0.5)))
    toma("conjunto_final.png", P.VUELTAS_MANIVELA_TOTAL, (820, 760, 520), (230, 0, 100), 32, rot_fin)
    toma("detalle_transmision.png", 12.0, (-40, 400, 200), (55, 60, 105), 24,
         lambda d, proy, est: rotulos(d, proy, est, [
             ("Rodillo", (100, P.Y_R + 14, P.Z_R + 16), True, 1420, 180),
             ("z1 = 20", (47, P.Y_R + 22, P.Z_R), True, 1520, 420),
             ("z2 = 40", (47, P.Y_R + 42, P.Z_H), True, 1450, 760),
             ("Husillo T8 de 4 entradas", (100, P.Y_H + 4, P.Z_H), True, 60, 880)]))
    toma("detalle_cuchilla.png", 16.0, (430, -520, 300), (320, -40, 140), 22,
         lambda d, proy, est: (rotulos(d, proy, est, [
             ("Cuchilla fija", (P.X_CUCHILLA, -P.R_B - 3, P.H_EJE), False, 560, 190),
             ("Tira", (P.X_CUCHILLA + 3, -P.R_B - 62, P.H_EJE - 62), False, 1450, 700)]),))

    # El hallazgo principal: la manivela sobre el cuerpo, como la imagen IA
    x_tras = P.X_RODILLO[1] + 12
    fantasma = esc.doc.addObject("Part::Feature", "ManivelaCuerpo")
    fantasma.Shape = Z.manivela(x_tras, +1)
    fantasma.ViewObject.ShapeColor = COLORES["gira"]
    cho = Part.Shape()
    cho.importBrep(os.path.join(CARPETA, "build", "choque_manivela.brep"))
    rojo = esc.doc.addObject("Part::Feature", "Choque")
    rojo.Shape = cho
    rojo.ViewObject.ShapeColor = (0.86, 0.10, 0.12)
    rojo.ViewObject.Transparency = 0
    barr = esc.doc.addObject("Part::Feature", "Barrido")
    barr.Shape = Z.barrido_manivela(x_tras, +1)
    barr.ViewObject.ShapeColor = (0.95, 0.50, 0.12)
    barr.ViewObject.Transparency = 85
    original = esc.piezas["Manivela"][0]
    original.ViewObject.Visibility = False
    r = json.load(open(os.path.join(CARPETA, "resultados.json"), encoding="utf-8"))
    hueco = r["manivela"]["hueco_eje_a_botella_mm"]

    def rot_choque(d, proy, est):
        titulo(d, "Manivela del lado del cuerpo: al girar, atraviesa la botella",
               f"Del eje del rodillo a la pared hay {hueco:.0f} mm; con radio {P.R_MANIVELA:.0f} mm, "
               "en rojo lo que la manivela barre dentro de la botella")
    toma("hallazgo_choque_manivela.png", 0.0, (620, 860, 460), (130, 20, 120), 26, rot_choque)
    esc.doc.removeObject("ManivelaCuerpo")
    esc.doc.removeObject("Choque")
    esc.doc.removeObject("Barrido")
    original.ViewObject.Visibility = True

    # Modelo para abrir y recorrer en FreeCAD
    esc.posar(0.0)
    os.makedirs(os.path.join(CARPETA, "modelo"), exist_ok=True)
    esc.doc.saveAs(os.path.join(CARPETA, "modelo", "cortadora_pet.FCStd"))


# --------------------------------------------------------------------------- main
def main():
    modo = os.environ.get("RENDER", "figuras")
    esc = Escena()
    if modo == "figuras":
        figuras(esc)
    else:
        k, n = (int(v) for v in os.environ.get("TANDA", "0/1").split("/"))
        carpeta = os.path.join(CARPETA, "build", "cuadros")
        os.makedirs(carpeta, exist_ok=True)
        total = int((SEG_INTRO + SEG_CORTE + SEG_FINAL) * FPS)
        solo = os.environ.get("CUADROS")
        lista = [int(v) for v in solo.split(",")] if solo else range(k, total, n)
        for i in lista:
            ruta = os.path.join(carpeta, f"{i:04d}.png")
            if not os.path.exists(ruta):     # reanuda si una tanda se cayó
                cuadro_video(esc, i, ruta)


try:
    main()
except Exception:
    with open(os.path.join(CARPETA, "build_error.txt"), "a") as f:
        f.write(traceback.format_exc())
    traceback.print_exc()
finally:
    sys.stdout.flush()
    os._exit(0)
