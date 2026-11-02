# -*- coding: utf-8 -*-
"""
Registro de una lámina: guarda qué dibujar en un JSON, sin depender de ezdxf.
planos.py corre en el Python de FreeCAD (TechDraw) y ezdxf está en el del sistema,
así que dxf.py lee este JSON del otro lado.

Las medidas van en mm reales; alturas de letra y desplazamientos, en mm de papel.
"""
import json, math

ANCHO_LETRA = 0.72      # ancho medio de un carácter respecto de la altura


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
        self.ops = []
        self.rect = []         # rectángulos de texto, para buscar superposiciones

    def linea(self, capa, a, b):
        self.ops.append(["l", capa, list(a), list(b)])

    def circulo(self, capa, c, r):
        self.ops.append(["c", capa, list(c), r])

    def arco(self, capa, c, r, a0, a1):
        """Antihorario, de a0 a a1, en grados."""
        self.ops.append(["a", capa, list(c), r, a0 % 360, a1 % 360])

    def polilinea(self, capa, pts, cerrada=False):
        self.ops.append(["p", capa, [list(p) for p in pts], cerrada])

    def solido(self, capa, a, b, c):
        """Triángulo relleno."""
        self.ops.append(["s", capa, list(a), list(b), list(c)])

    def _registrar(self, x, y, H, s, alin, rot):
        w = ancho_texto(s, H)
        dx = {"i": 0.0, "c": -w / 2, "d": -w}[alin]
        r = math.radians(rot)
        esq = [(x + u * math.cos(r) - v * math.sin(r), y + u * math.sin(r) + v * math.cos(r))
               for u, v in ((dx, 0), (dx + w, 0), (dx + w, H), (dx, H))]
        xs, ys = [p[0] for p in esq], [p[1] for p in esq]
        self.rect.append((min(xs), min(ys), max(xs), max(ys), s))

    def texto(self, capa, x, y, h, s, alin="i", rot=0.0):
        """x, y en el modelo; h en mm de papel; alin: i(zquierda), c(entro), d(erecha)."""
        H = h * self.E
        self.ops.append(["t", capa, x, y, H, s, alin, rot])
        self._registrar(x, y, H, s, alin, rot)

    def cota(self, a, b, d, s=None, direc=None):
        """Cota lineal entre a y b, con la línea a d mm de papel de la recta que
        los une. direc: 'h', 'v' o None (paralela a ab). s: texto; None = medida."""
        E = self.E
        if direc == "h":
            ang = 0.0
        elif direc == "v":
            ang = 90.0
        else:
            ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
        # El número se lee de abajo o desde la derecha (ISO 129-1, IRAM 4513)
        if ang > 90.001 or ang <= -89.999:
            ang -= 180 if ang > 0 else -180
            a, b = b, a
        r = math.radians(ang)
        ux, uy = math.cos(r), math.sin(r)
        nx, ny = -uy, ux
        base = (a[0] + nx * d * E, a[1] + ny * d * E)
        ta = (a[0] - base[0]) * ux + (a[1] - base[1]) * uy
        tb = (b[0] - base[0]) * ux + (b[1] - base[1]) * uy
        med = abs(tb - ta)
        entero = abs(med - round(med)) < 0.005
        rotulo = s if s is not None else formato(med)
        self.ops.append(["d", list(a), list(b), list(base), ang,
                         "<>" if s is None and entero else rotulo])
        # Dónde va a quedar el número, para el control de superposiciones
        p1 = (base[0] + ux * ta, base[1] + uy * ta)
        p2 = (base[0] + ux * tb, base[1] + uy * tb)
        H = 3.5 * E
        w = ancho_texto(rotulo, H)
        c = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        if med < 7 * E + w + 2 * E:       # espacio reducido: número afuera
            lejos = w / 2 + 7 * E + E
            sen = 1 if tb > ta else -1
            c = (p2[0] + ux * sen * lejos, p2[1] + uy * sen * lejos)
        self._registrar(c[0] + nx * E, c[1] + ny * E, H, rotulo, "c", ang)

    def guardar(self, ruta, ancho, alto):
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump({"escala": self.E, "ancho": ancho, "alto": alto, "ops": self.ops},
                      f, ensure_ascii=False)
