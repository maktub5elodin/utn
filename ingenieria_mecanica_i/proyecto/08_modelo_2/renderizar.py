# -*- coding: utf-8 -*-
"""
Cuadros del video corto del modelo 2.0, con el método del modelo 1: la escena
se arma una vez, cada cuadro solo cambia lo que se mueve, se renderiza al
doble y se reduce, y los rótulos se dibujan encima con PIL. Sin pantalla:
    CARPETA_MODELO=$PWD QT_QPA_PLATFORM=offscreen RENDER=video TANDA=0/3 ~/Aplicaciones/FreeCAD.AppImage renderizar.py
    RENDER=prueba SEGUNDOS=1,6,14 ...   cuadros sueltos en build/prueba_*.png
Lo lanza el Makefile (make video).

Cinemática: manda el avance de la botella. Con n vueltas de botella:
  corte s = w·n          (la botella baja exactamente w por vuelta)
  tira    L = π·D·n
  rollo   r = √(r_núcleo² + L·espesor/π)
  manivela N = (r − r_núcleo)/espesor   (integral de dL / 2πr)
"""
import math, os, sys, traceback

CARPETA = os.environ.get("CARPETA_MODELO", os.getcwd())
sys.path.insert(0, CARPETA)

import FreeCAD as App
import FreeCADGui as Gui
from PIL import Image, ImageDraw, ImageFont
from pivy import coin

import parametros as P
import piezas as Z

V = App.Vector
ANCHO, ALTO = 1600, 900
SS = 2                      # supermuestreo: se renderiza al doble y se reduce
FPS = 30
DURACION = 25.0
T_INI, T_FIN = 2.5, 23.5    # el corte ocurre entre estos segundos; antes y después, quieto
LENTO = (11.5, 16.5)        # primer plano del cabezal, en cámara lenta
RAMPA = 1.5
R_LENTA = 0.25              # vueltas de botella por segundo en cámara lenta
MARCAS_BOTELLA = 3          # franjas pintadas para que se vea el giro
MARCAS_CARRETE = 3
COLOR_MARCA = (0.78, 0.04, 0.32)


# ------------------------------------------------------------------ cinemática
def _forma(t):
    """Velocidad relativa de la botella: 1 fuera del primer plano, R_LENTA/R dentro."""
    a, b = LENTO[0] - RAMPA, LENTO[1] + RAMPA
    if t < T_INI or t > T_FIN:
        return 0.0
    if a <= t < LENTO[0]:
        return 1.0 - (t - a) / RAMPA
    if LENTO[0] <= t < LENTO[1]:
        return 0.0
    if LENTO[1] <= t < b:
        return (t - LENTO[1]) / RAMPA
    return 1.0


def _integrar(r_rapida, t_hasta, dt=1e-3):
    """Vueltas de botella acumuladas: rápida·forma + lenta·(1 − forma), con arranque y frenado suaves."""
    n, t = 0.0, T_INI
    while t < min(t_hasta, T_FIN):
        f = _forma(t)
        arr = min(1.0, (t - T_INI) / 1.0, (T_FIN - t) / 1.0)      # 1 s para arrancar y para frenar
        n += (r_rapida * f + R_LENTA * (1 - f)) * max(0.0, arr) * dt
        t += dt
    return n


# La velocidad rápida se ajusta para que el corte termine justo en T_FIN
_A = _integrar(0.0, T_FIN)
_B = _integrar(1.0, T_FIN) - _A
R_RAPIDA = (P.VUELTAS_BOTELLA - _A) / _B
_TABLA = []


def vueltas_botella(t):
    if not _TABLA:
        n, k = 0.0, 0
        while k <= int(DURACION * FPS):
            _TABLA.append(_integrar(R_RAPIDA, k / FPS))
            k += 1
    i = min(int(round(t * FPS)), len(_TABLA) - 1)
    return _TABLA[i]


def estado(n_b):
    s = P.W * n_b
    largo = math.pi * P.D_B * n_b
    r = math.sqrt(P.R_NUCLEO ** 2 + largo * P.PARED / math.pi)
    return {"s": s, "n_botella": n_b, "largo": largo, "r_rollo": r,
            "n_manivela": (r - P.R_NUCLEO) / P.PARED}


def control_estroboscopico():
    """Falla si, en algún cuadro, algo que gira avanza casi un número entero de marcas."""
    peor = []
    for k in range(1, int(DURACION * FPS) + 1):
        e0, e1 = estado(vueltas_botella((k - 1) / FPS)), estado(vueltas_botella(k / FPS))
        for nombre, d in (("marcas de la botella", (e1["n_botella"] - e0["n_botella"]) * MARCAS_BOTELLA),
                          ("marcas del carrete", (e1["n_manivela"] - e0["n_manivela"]) * MARCAS_CARRETE),
                          ("manivela", e1["n_manivela"] - e0["n_manivela"])):
            if d > 0.5 and abs(d - round(d)) < 0.15:
                peor.append((nombre, k, round(d, 3)))
    if peor:
        raise ValueError(f"efecto estroboscópico: {peor[:3]}")
    e_max = max((estado(vueltas_botella(k / FPS))["n_manivela"] - estado(vueltas_botella((k - 1) / FPS))["n_manivela"])
                for k in range(1, int(DURACION * FPS) + 1))
    return e_max * MARCAS_CARRETE


# --------------------------------------------------------------------- escena
def franja(r0, r1, ang, ancho_grados, z0, z1):
    return Z.sector(r0, r1, ang, ang + ancho_grados, z0, z1)


def marcas_botella(e):
    zt = P.z_superior_botella(e["s"])
    z0, z1 = P.Z_GUIA + P.W + 2, zt - P.X_HOMBRO_FIN
    if z1 <= z0 + 2:
        return None
    giro = -360.0 * e["n_botella"]
    partes = [franja(P.R_B, P.R_B + 0.5, giro + 360 / MARCAS_BOTELLA * k, 4.0, z0, z1)
              for k in range(MARCAS_BOTELLA)]
    out = partes[0]
    for p in partes[1:]:
        out = out.fuse(p)
    return out


def marcas_carrete():
    z = P.Z_CORE1 + P.DISCO_ESP
    partes = []
    for k in range(MARCAS_CARRETE):
        m = franja(P.CUBO_R + 2, P.R_DISCO - 2, 120 * k + 40, 8.0, z, z + 0.6)
        m.translate(V(P.X_CARRETE, P.Y_CARRETE, 0))
        partes.append(m)
    out = partes[0]
    for p in partes[1:]:
        out = out.fuse(p)
    return out


GIRA_CON_MANIVELA = ["Manivela", "Mango", "TornilloMango", "TuercaMango", "TuercaManivela",
                     "CarreteSuperior", "CarreteInferior", "TuercaCarrete", "EjeCarrete", "MarcasCarrete"]


class Escena:
    def __init__(self):
        self.doc = App.newDocument("Video_v2")
        self.obj = {}
        pz = Z.conjunto(0.0)
        for n, d in pz.items():
            o = self.doc.addObject("Part::Feature", n)
            o.Shape = d["forma"]
            c = Z.COLORES["mdf"] if n in ("Base", "Taco") else Z.COLORES.get(d["tipo"], (0.7, 0.7, 0.7))
            if n == "Tira":
                c = Z.COLORES["tira"]
            o.ViewObject.ShapeColor = c
            if n in ("Botella", "Tapa"):
                o.ViewObject.Transparency = 55
            if n == "Lastre":
                o.ViewObject.Transparency = 35
            self.obj[n] = o
        for n, forma in (("MarcasCarrete", marcas_carrete()), ("MarcasBotella", marcas_botella(estado(0.0)))):
            o = self.doc.addObject("Part::Feature", n)
            o.Shape = forma
            o.ViewObject.ShapeColor = COLOR_MARCA
            self.obj[n] = o
        self.doc.recompute()
        self.vista = Gui.getDocument(self.doc.Name).activeView()
        self.vista.setAnimationEnabled(False)
        self.vista.setCameraType("Perspective")
        self.cam = self.vista.getCameraNode()

    def posar(self, n_b):
        e = estado(n_b)
        self.obj["Botella"].Shape = Z.botella(e["s"])
        self.obj["Tapa"].Shape = Z.tapa(e["s"])
        self.obj["Lastre"].Shape = Z.lastre(e["s"])
        self.obj["Tira"].Shape = Z.tira(e["s"])
        mb = marcas_botella(e)
        self.obj["MarcasBotella"].Visibility = mb is not None
        if mb is not None:
            self.obj["MarcasBotella"].Shape = mb
        rot = App.Rotation(V(0, 0, 1), -360.0 * e["n_manivela"])   # horario visto desde arriba
        c = V(P.X_CARRETE, P.Y_CARRETE, 0)
        for n in GIRA_CON_MANIVELA:
            self.obj[n].Placement = App.Placement(c - rot.multVec(c), rot)
        self.doc.recompute()
        return e

    def camara(self, pos, obj, angulo):
        self.cam.position.setValue(coin.SbVec3f(*pos))
        self.cam.pointAt(coin.SbVec3f(*obj), coin.SbVec3f(0, 0, 1))
        self.cam.heightAngle.setValue(math.radians(angulo))
        self.cam.nearDistance.setValue(20)
        self.cam.farDistance.setValue(5000)

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


# ------------------------------------------------------------------ cámaras
GENERAL = ((-430.0, 780.0, 600.0), (70.0, 20.0, 175.0), 32.0)
CABEZAL = ((70.0, 170.0, 210.0), (5.0, 46.0, 45.0), 28.0)   # desde arriba: la hoja asoma entre la pared y el pisador
PLANOS = [  # (segundo, cámara)
    (0.0, GENERAL), (9.8, GENERAL), (11.5, CABEZAL), (16.5, CABEZAL), (18.3, GENERAL), (DURACION, GENERAL),
]


def suave(t):
    return t * t * (3 - 2 * t)


def plano(seg):
    for (ta, a), (tb, b) in zip(PLANOS, PLANOS[1:]):
        if seg <= tb:
            u = suave((seg - ta) / (tb - ta)) if tb > ta else 1.0
            pos = [a[0][i] + (b[0][i] - a[0][i]) * u for i in range(3)]
            obj = [a[1][i] + (b[1][i] - a[1][i]) * u for i in range(3)]
            return pos, obj, a[2] + (b[2] - a[2]) * u
    return PLANOS[-1][1]


# ----------------------------------------------------------------- rótulos
TINTA = (32, 36, 44)
SUAVE_C = (98, 104, 116)
_F = {"n": "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
      "b": "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"}


def fuente(e, px):
    ruta = _F[e]
    if not os.path.exists(ruta):
        ruta = "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if e == "b" else "")
    return ImageFont.truetype(ruta, px)


def rotulo(d, proy, texto, p3, x, y, alfa=255):
    f = fuente("b", 26)
    w = d.textlength(texto, font=f)
    if p3 is not None:
        px, py = proy(p3)
        d.line((x + w / 2, y + 20, px, py), fill=TINTA + (alfa,), width=2)
        d.ellipse((px - 5, py - 5, px + 5, py + 5), fill=TINTA + (alfa,))
    d.rounded_rectangle((x - 12, y - 4, x + w + 12, y + 38), 8, fill=(255, 255, 255, round(240 * alfa / 255)),
                        outline=(204, 208, 214, alfa), width=2)
    d.text((x, y), texto, font=f, fill=TINTA + (alfa,))


def etiqueta_version(d):
    t = "Modelo 2.0 - versión preliminar"
    f = fuente("n", 22)
    w = d.textlength(t, font=f)
    d.rounded_rectangle((24, 22, 24 + w + 32, 62), 10, fill=(255, 255, 255, 225))
    d.text((40, 30), t, font=f, fill=SUAVE_C)


def titulo(d, alfa):
    t = "Modelo 2.0 - versión preliminar"
    f = fuente("b", 50)
    w = d.textlength(t, font=f)
    d.rounded_rectangle(((ANCHO - w) / 2 - 30, 40, (ANCHO + w) / 2 + 30, 124), 14,
                        fill=(255, 255, 255, round(235 * alfa / 255)))
    d.text(((ANCHO - w) / 2, 52), t, font=f, fill=TINTA + (alfa,))


def visible(seg, a, b, fundido=0.4):
    """Opacidad de un rótulo que se muestra entre a y b, con fundido."""
    if seg < a or seg > b:
        return 0
    return round(255 * min(1.0, (seg - a) / fundido, (b - seg) / fundido))


def componer(img, dibujar):
    capa = Image.new("RGBA", img.size, (0, 0, 0, 0))
    dibujar(ImageDraw.Draw(capa))
    return Image.alpha_composite(img.convert("RGBA"), capa).convert("RGB")


def cuadro(esc, seg, ruta):
    e = esc.posar(vueltas_botella(seg))
    pos, obj, ang = plano(seg)
    if os.environ.get("CAM"):                 # solo para probar cámaras
        v = [float(x) for x in os.environ["CAM"].split(",")]
        pos, obj, ang = v[:3], v[3:6], v[6]
    esc.camara(pos, obj, ang)
    img = esc.foto(ruta)
    proy = esc.proyector()
    zt = P.z_superior_botella(e["s"])

    def dibujar(d):
        a = visible(seg, 0.0, 3.2)
        if a:
            titulo(d, a)
        if seg > 3.0:
            etiqueta_version(d)
        a = visible(seg, 4.0, 9.6)
        if a:
            rotulo(d, proy, "La tira tira de la botella", (P.X_OJAL + 40, P.R_B, P.Z_GUIA + P.W / 2), 300, 720, a)
        a = visible(seg, 5.5, 9.6)
        if a:
            rotulo(d, proy, "Carrete", (P.X_CARRETE, P.Y_CARRETE, P.Z_CORE1 + 2), 300, 380, a)
        a = visible(seg, 12.0, 16.4)
        if a:
            rotulo(d, proy, "Cuchilla fija", (9.0, 44.0, P.Z_GUIA + P.W + 0.5), 980, 150, a)
        a = visible(seg, 19.0, DURACION + 1)
        if a:
            rotulo(d, proy, "La tira tira de la botella", (P.X_OJAL + 40, P.R_B, P.Z_GUIA + P.W / 2), 300, 720, a)
            rotulo(d, proy, "Carrete", (P.X_CARRETE, P.Y_CARRETE, P.Z_CORE1 + 2), 300, 380, a)
    img = componer(img, dibujar)
    img.save(ruta + ".tmp.png")
    os.replace(ruta + ".tmp.png", ruta)       # un cuadro a medias nunca queda con su nombre


def main():
    control_estroboscopico()
    esc = Escena()
    modo = os.environ.get("RENDER", "video")
    if modo == "prueba":
        for s in os.environ.get("SEGUNDOS", "1,6,14,22").split(","):
            cuadro(esc, float(s), os.path.join(CARPETA, "build", f"prueba_{float(s):05.1f}.png"))
        return
    k, n = (int(v) for v in os.environ.get("TANDA", "0/1").split("/"))
    carpeta = os.path.join(CARPETA, "build", "cuadros")
    os.makedirs(carpeta, exist_ok=True)
    total = int(DURACION * FPS)
    for i in range(k, total, n):
        ruta = os.path.join(carpeta, f"{i:04d}.png")
        if not os.path.exists(ruta):          # reanuda si una tanda se cayó
            cuadro(esc, i / FPS, ruta)


try:
    main()
except Exception:
    with open(os.path.join(CARPETA, "build", "render_error.txt"), "a") as f:
        f.write(traceback.format_exc())
finally:
    sys.stdout.flush()
    os._exit(0)
