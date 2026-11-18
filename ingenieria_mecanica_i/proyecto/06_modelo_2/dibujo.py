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

    def cota(self, a, b, d, s=None, direc=None, pos=0.5, afuera=1):
        """Cota lineal entre a y b, con la línea a d mm de papel de la recta que
        los une. direc: 'h', 'v' o None (paralela a ab). s: texto; None = medida.
        pos: dónde va el número a lo largo de la línea (0 = a, 1 = b). Si no entra,
        sale afuera: más allá de b (afuera=1) o de a (afuera=-1)."""
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
        # Dónde va el número: siempre sobre la línea de cota (del lado de la normal,
        # que con el ángulo ya corregido es "arriba" para quien lee), a 1 mm de ella
        p1 = (base[0] + ux * ta, base[1] + uy * ta)
        p2 = (base[0] + ux * tb, base[1] + uy * tb)
        H = 3.5 * E
        w = ancho_texto(rotulo, H)
        c = (p1[0] + (p2[0] - p1[0]) * pos, p1[1] + (p2[1] - p1[1]) * pos)
        if med < w + 2.5 * E:             # el número no entra a lo largo de la cota: afuera
            fin, otro = (p2, p1) if afuera == 1 else (p1, p2)
            lg = math.hypot(fin[0] - otro[0], fin[1] - otro[1]) or 1.0
            ex, ey = (fin[0] - otro[0]) / lg, (fin[1] - otro[1]) / lg
            lejos = w / 2 + 5 * E       # justo después de la flecha (3,5) y 1,5 de aire
            c = (fin[0] + ex * lejos, fin[1] + ey * lejos)
        self._registrar(c[0] + nx * E, c[1] + ny * E, H, rotulo, "c", ang)
        medio = (c[0] + nx * (E + H / 2), c[1] + ny * (E + H / 2))
        self.ops.append(["d", list(a), list(b), list(base), ang,
                         "<>" if s is None and entero else rotulo, list(medio)])

    def guardar(self, ruta, ancho, alto, salida):
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump({"escala": self.E, "ancho": ancho, "alto": alto, "salida": salida,
                       "ops": self.ops},
                      f, ensure_ascii=False)
