#!/usr/bin/env python3
"""Genera Presentacion_Cortadora_PET_S1091_Grupo_1.pptx sin dependencias de PPTX.

Escribe el OOXML directamente con zipfile: las formas, la tabla y el gráfico quedan
nativos y editables en PowerPoint. El contenido de cada lámina está en las funciones
lamina_*; los valores de referencia del cálculo, en la sección CALCULO.
Uso: python3 generar_presentacion.py
"""
import io
import math
import re
import uuid
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image

AQUI = Path(__file__).resolve().parent
GRAFICO = AQUI.parent / "04_material_grafico"
FIGURAS = AQUI / "figuras"
SALIDA = AQUI / "Presentacion_Cortadora_PET_S1091_Grupo_1.pptx"
FECHA_ZIP = (2026, 11, 1, 12, 0, 0)

EMU = 914400
W, H = 13.333, 7.5
NS = ('xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
      'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
      'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"')
XML = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

TEMA = {"dk1": "1B2A2F", "lt1": "FFFFFF", "dk2": "0F3D3E", "lt2": "E9F4F1",
        "accent1": "1F8A70", "accent2": "F28C28", "accent3": "2458A6",
        "accent4": "C9302C", "accent5": "6FB536", "accent6": "5B6C70",
        "hlink": "2458A6", "folHlink": "5B6C70"}
FUENTE_TITULO, FUENTE_CUERPO = "Cambria", "Calibri"


def e(v):
    return int(round(v * EMU))


def color(c):
    return f'<a:schemeClr val="{c}"/>'


def relleno(c, transparencia=None):
    if c is None:
        return "<a:noFill/>"
    alfa = f'<a:alpha val="{int((100 - transparencia) * 1000)}"/>' if transparencia else ""
    return f'<a:solidFill><a:schemeClr val="{c}">{alfa}</a:schemeClr></a:solidFill>'


def linea(c=None, pt=1.0, guion=None, punta=False):
    if c is None:
        return "<a:ln><a:noFill/></a:ln>"
    g = f'<a:prstDash val="{guion}"/>' if guion else ""
    p = '<a:tailEnd type="triangle" w="med" len="med"/>' if punta else ""
    return f'<a:ln w="{int(pt * 12700)}">{relleno(c)}{g}<a:round/>{p}</a:ln>'


# ---------- Texto ----------
TOKEN = re.compile(r"(\*\*.+?\*\*|_\{.+?\}|\^\{.+?\})")


def corridas(texto, sz, c, b=False, i=False, fuente=None):
    """Marcado mínimo: **negrita**, _{subíndice}, ^{superíndice}."""
    salida = []
    for parte in TOKEN.split(texto):
        if not parte:
            continue
        negrita, base = b, 0
        if parte.startswith("**"):
            parte, negrita = parte[2:-2], True
        elif parte.startswith("_{"):
            parte, base = parte[2:-1], -25000
        elif parte.startswith("^{"):
            parte, base = parte[2:-1], 30000
        attrs = f'lang="es-AR" sz="{int(sz * 100)}" b="{int(negrita)}" i="{int(i)}"'
        if base:
            attrs += f' baseline="{base}"'
        f = f'<a:latin typeface="{fuente or "+mn-lt"}"/>'
        salida.append(f'<a:r><a:rPr {attrs} dirty="0">{relleno(c)}{f}</a:rPr>'
                      f"<a:t>{escape(parte)}</a:t></a:r>")
    return "".join(salida)


def parrafo(p, sz, c, algn="l"):
    if isinstance(p, str):
        p = {"t": p}
    tam, col = p.get("sz", sz), p.get("c", c)
    attrs = f'algn="{p.get("algn", algn)}"'
    viñeta = "<a:buNone/>"
    if p.get("viñeta"):
        attrs += ' marL="228600" indent="-228600"'
        viñeta = f'<a:buClr>{color("accent1")}</a:buClr><a:buFont typeface="Arial"/><a:buChar char="•"/>'
    else:
        attrs += ' marL="0" indent="0"'
    espacio = (f'<a:spcBef><a:spcPts val="{int(p.get("antes", 0) * 100)}"/></a:spcBef>'
               f'<a:spcAft><a:spcPts val="{int(p.get("despues", 0) * 100)}"/></a:spcAft>')
    return (f"<a:p><a:pPr {attrs}>{espacio}{viñeta}</a:pPr>"
            + corridas(p["t"], tam, col, p.get("b", False), p.get("i", False), p.get("fuente"))
            + "</a:p>")


class Lamina:
    def __init__(self, layout, orador, segundos, notas):
        self.layout, self.seccion, self.segundos, self.notas = layout, orador, segundos, notas
        self.formas, self.rels = [], []
        self.n = 1

    def _id(self):
        self.n += 1
        return self.n

    def rel(self, tipo, destino):
        self.rels.append((tipo, destino))
        return f"rId{len(self.rels) + 1}"  # rId1 es el layout

    def titulo(self, texto, tipo="title"):
        self.formas.append(
            f'<p:sp><p:nvSpPr><p:cNvPr id="{self._id()}" name="Título"/>'
            f'<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr><p:ph type="{tipo}"/></p:nvPr></p:nvSpPr>'
            f'<p:spPr/><p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="es-AR" dirty="0"><a:latin typeface="+mj-lt"/></a:rPr>'
            f"<a:t>{escape(texto)}</a:t></a:r></a:p></p:txBody></p:sp>")

    def subtitulo(self, texto):
        self.formas.append(
            f'<p:sp><p:nvSpPr><p:cNvPr id="{self._id()}" name="Subtítulo"/>'
            f'<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr><p:ph type="subTitle" idx="1"/></p:nvPr></p:nvSpPr>'
            f'<p:spPr/><p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="es-AR" dirty="0"><a:latin typeface="+mn-lt"/></a:rPr>'
            f"<a:t>{escape(texto)}</a:t></a:r></a:p></p:txBody></p:sp>")

    def caja(self, x, y, w, h, parrafos=None, sz=16, c="tx1", anchor="t", fondo=None, borde=None,
             borde_pt=1.0, geom="rect", radio=None, margen=0.0, algn="l", nombre="Texto", alt="",
             transparencia=None):
        parrafos = parrafos if parrafos is not None else []
        if isinstance(parrafos, (str, dict)):
            parrafos = [parrafos]
        av = f'<a:avLst><a:gd name="adj" fmla="val {radio}"/></a:avLst>' if radio is not None else "<a:avLst/>"
        cuerpo = "".join(parrafo(p, sz, c, algn) for p in parrafos) or '<a:p><a:endParaRPr lang="es-AR"/></a:p>'
        m = e(margen)
        txbox = ' txBox="1"' if parrafos and fondo is None and borde is None else ""
        descr = f' descr="{escape(alt, {chr(34): "&quot;"})}"' if alt else ""
        self.formas.append(
            f'<p:sp><p:nvSpPr><p:cNvPr id="{self._id()}" name="{escape(nombre)}"{descr}/><p:cNvSpPr{txbox}/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{e(x)}" y="{e(y)}"/><a:ext cx="{e(w)}" cy="{e(h)}"/></a:xfrm>'
            f'<a:prstGeom prst="{geom}">{av}</a:prstGeom>{relleno(fondo, transparencia)}{linea(borde, borde_pt)}</p:spPr>'
            f'<p:txBody><a:bodyPr wrap="square" lIns="{m}" tIns="{m}" rIns="{m}" bIns="{m}" anchor="{anchor}" rtlCol="0"><a:noAutofit/></a:bodyPr>'
            f"<a:lstStyle/>{cuerpo}</p:txBody></p:sp>")

    def tarjeta(self, x, y, w, h, parrafos=None, fondo="bg2", **kw):
        kw.setdefault("margen", 0.16)
        kw.setdefault("radio", 7000)
        self.caja(x, y, w, h, parrafos, fondo=fondo, geom="roundRect", nombre=kw.pop("nombre", "Tarjeta"), **kw)

    def anillo(self, x, y, d, texto, c="accent1", sz=15):
        """Motivo del deck: anillo numerado, como los que marcó el grupo sobre el conjunto."""
        self.caja(x, y, d, d, {"t": str(texto), "b": True, "c": c, "algn": "ctr"}, sz=sz, anchor="ctr",
                  fondo="bg1", borde=c, borde_pt=2.5, geom="ellipse", nombre=f"Anillo {texto}")

    def recta(self, x1, y1, x2, y2, c="tx2", pt=1.5, punta=True, guion=None, nombre="Conector"):
        fx = ' flipH="1"' if x2 < x1 else ""
        fy = ' flipV="1"' if y2 < y1 else ""
        self.formas.append(
            f'<p:cxnSp><p:nvCxnSpPr><p:cNvPr id="{self._id()}" name="{nombre}"/><p:cNvCxnSpPr/><p:nvPr/></p:nvCxnSpPr>'
            f'<p:spPr><a:xfrm{fx}{fy}><a:off x="{e(min(x1, x2))}" y="{e(min(y1, y2))}"/>'
            f'<a:ext cx="{e(abs(x2 - x1))}" cy="{e(abs(y2 - y1))}"/></a:xfrm>'
            f'<a:prstGeom prst="line"><a:avLst/></a:prstGeom>{linea(c, pt, guion, punta)}</p:spPr></p:cxnSp>')

    def trazo(self, subcaminos, c="tx1", pt=1.0, fondo=None, guion=None, nombre="Trazo", alt="", transparencia=None):
        """Forma libre vectorial: lista de polilíneas [(x, y), ...] en pulgadas."""
        xs = [p[0] for s in subcaminos for p in s]
        ys = [p[1] for s in subcaminos for p in s]
        x0, y0, ancho, alto = min(xs), min(ys), max(max(xs) - min(xs), 0.001), max(max(ys) - min(ys), 0.001)
        caminos = []
        for s in subcaminos:
            cerrar = s[0] == s[-1] and fondo is not None
            puntos = s[:-1] if cerrar else s
            seg = f'<a:moveTo><a:pt x="{e(puntos[0][0] - x0)}" y="{e(puntos[0][1] - y0)}"/></a:moveTo>'
            seg += "".join(f'<a:lnTo><a:pt x="{e(a - x0)}" y="{e(b - y0)}"/></a:lnTo>' for a, b in puntos[1:])
            if cerrar:
                seg += "<a:close/>"
            attr = "" if fondo else ' fill="none"'
            caminos.append(f'<a:path w="{e(ancho)}" h="{e(alto)}"{attr}>{seg}</a:path>')
        descr = f' descr="{escape(alt, {chr(34): "&quot;"})}"' if alt else ""
        self.formas.append(
            f'<p:sp><p:nvSpPr><p:cNvPr id="{self._id()}" name="{escape(nombre)}"{descr}/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{e(x0)}" y="{e(y0)}"/><a:ext cx="{e(ancho)}" cy="{e(alto)}"/></a:xfrm>'
            f'<a:custGeom><a:avLst/><a:gdLst/><a:ahLst/><a:cxnLst/><a:rect l="0" t="0" r="r" b="b"/>'
            f'<a:pathLst>{"".join(caminos)}</a:pathLst></a:custGeom>'
            f'{relleno(fondo, transparencia)}{linea(c, pt, guion)}</p:spPr></p:sp>')

    def imagen(self, ruta, x, y, w, h, alt, radio=None, borde=None, borde_pt=1.0):
        rid = self.rel(f"{REL}/image", f"../media/{ruta.name}")
        MEDIOS.add(ruta)
        geom = (f'<a:prstGeom prst="roundRect"><a:avLst><a:gd name="adj" fmla="val {radio}"/></a:avLst></a:prstGeom>'
                if radio is not None else '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>')
        self.formas.append(
            f'<p:pic><p:nvPicPr><p:cNvPr id="{self._id()}" name="{escape(ruta.stem)}" descr="{escape(alt, {chr(34): "&quot;"})}"/>'
            f'<p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr><p:nvPr/></p:nvPicPr>'
            f'<p:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>'
            f'<p:spPr><a:xfrm><a:off x="{e(x)}" y="{e(y)}"/><a:ext cx="{e(w)}" cy="{e(h)}"/></a:xfrm>{geom}{linea(borde, borde_pt)}</p:spPr></p:pic>')

    def tabla(self, x, y, anchos, altos, filas, sz=14):
        grid = "".join(f'<a:gridCol w="{e(a)}"/>' for a in anchos)
        cuerpo = ""
        for i, fila in enumerate(filas):
            celdas = ""
            for j, celda in enumerate(fila):
                encabezado, lateral = i == 0, j == 0
                resaltada = j == len(fila) - 1 and not encabezado
                c = "bg1" if encabezado else ("tx2" if lateral else "tx1")
                negrita = encabezado or lateral
                fondo = "tx2" if encabezado else ("bg2" if resaltada else None)
                borde = (f'<a:lnL w="0"><a:noFill/></a:lnL><a:lnR w="0"><a:noFill/></a:lnR><a:lnT w="0"><a:noFill/></a:lnT>'
                         f'<a:lnB w="9525">{relleno("accent6", 55)}</a:lnB>')
                celdas += (f'<a:tc><a:txBody><a:bodyPr/><a:lstStyle/>{parrafo({"t": celda, "b": negrita}, sz, c)}</a:txBody>'
                           f'<a:tcPr marL="{e(.11)}" marR="{e(.11)}" marT="{e(.06)}" marB="{e(.06)}" anchor="ctr">{borde}{relleno(fondo)}</a:tcPr></a:tc>')
            cuerpo += f'<a:tr h="{e(altos[i])}">{celdas}</a:tr>'
        self.formas.append(
            f'<p:graphicFrame><p:nvGraphicFramePr><p:cNvPr id="{self._id()}" name="Tabla"/>'
            f'<p:cNvGraphicFramePr><a:graphicFrameLocks noGrp="1"/></p:cNvGraphicFramePr><p:nvPr/></p:nvGraphicFramePr>'
            f'<p:xfrm><a:off x="{e(x)}" y="{e(y)}"/><a:ext cx="{e(sum(anchos))}" cy="{e(sum(altos))}"/></p:xfrm>'
            f'<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/table">'
            f'<a:tbl><a:tblPr firstRow="1"/><a:tblGrid>{grid}</a:tblGrid>{cuerpo}</a:tbl></a:graphicData></a:graphic></p:graphicFrame>')

    def grafico(self, x, y, w, h, alt):
        rid = self.rel(f"{REL}/chart", "../charts/chart1.xml")
        self.formas.append(
            f'<p:graphicFrame><p:nvGraphicFramePr><p:cNvPr id="{self._id()}" name="Gráfico" descr="{escape(alt)}"/>'
            f'<p:cNvGraphicFramePr/><p:nvPr/></p:nvGraphicFramePr>'
            f'<p:xfrm><a:off x="{e(x)}" y="{e(y)}"/><a:ext cx="{e(w)}" cy="{e(h)}"/></p:xfrm>'
            f'<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/chart">'
            f'<c:chart xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart" r:id="{rid}"/>'
            f'</a:graphicData></a:graphic></p:graphicFrame>')

    def numero(self, n):
        self.formas.append(
            f'<p:sp><p:nvSpPr><p:cNvPr id="{self._id()}" name="Número de lámina"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
            f'<p:nvPr><p:ph type="sldNum" sz="quarter" idx="12"/></p:nvPr></p:nvSpPr><p:spPr/><p:txBody><a:bodyPr/><a:lstStyle/>'
            f'<a:p><a:fld id="{CAMPO_NUMERO}" type="slidenum"><a:rPr lang="es-AR"><a:latin typeface="+mn-lt"/></a:rPr><a:t>{n}</a:t></a:fld></a:p></p:txBody></p:sp>')

    def nota_pie(self, parrafos, y=6.32, h=0.62):
        if isinstance(parrafos, str):
            parrafos = [parrafos]
        self.caja(0.6, y, 11.0, h, [{"t": p, "despues": 1} for p in parrafos], sz=10.5, c="accent6",
                  anchor="b", nombre="Notas al pie")


MEDIOS = set()
CAMPO_NUMERO = "{B6F15528-21DE-4FAA-801E-634DDDAF4B2B}"


# ---------- CALCULO: valores de referencia (a confirmar en el dimensionamiento) ----------
D_RODILLO = 50.0            # mm, leído del plano Proy Mecanica.dxf
BOTELLAS = [("Ø65", 65.0), ("Ø88", 88.0), ("Ø110", 110.0)]
L_M8, I_M8 = 1.25, 1.0      # M8 de paso normal, sin reducción
L_T8, I_T8 = 8.0, 2.0       # husillo T8 de 4 entradas, reducción 2:1
TRAMO_CILINDRICO = 180.0    # mm, supuesto para el largo de corte


def avance(L, i, Db, Dr=D_RODILLO):
    """a = L·Db / (i·Dr) — Entrega 2, apartado 5.3."""
    return L * Db / (i * Dr)


# ---------- Plano: DXF a trazos vectoriales ----------
def leer_dxf(ruta):
    filas = ruta.read_text(encoding="cp1252", errors="replace").split("\n")
    pares = [(filas[i].strip(), filas[i + 1].rstrip()) for i in range(0, len(filas) - 1, 2)]
    ini = pares.index(("2", "ENTITIES"))
    fin = next(k for k, p in enumerate(pares) if p == ("0", "ENDSEC") and k > ini)
    entidades, actual = [], None
    for a, b in pares[ini + 1:fin]:
        if a == "0":
            actual = {"t": b}
            entidades.append(actual)
        elif a not in actual:
            actual[a] = b
    return entidades


def polilineas_dxf(entidades, capas):
    salida = []
    for en in entidades:
        if en.get("8") not in capas:
            continue
        if en["t"] == "LINE":
            salida.append([(float(en["10"]), float(en["20"])), (float(en["11"]), float(en["21"]))])
        elif en["t"] in ("CIRCLE", "ARC"):
            cx, cy, r = float(en["10"]), float(en["20"]), float(en["40"])
            a0, a1 = (0.0, 360.0) if en["t"] == "CIRCLE" else (float(en["50"]), float(en["51"]))
            if a1 <= a0:
                a1 += 360.0
            pasos = max(int((a1 - a0) / 6), 4)
            salida.append([(cx + r * math.cos(math.radians(a0 + (a1 - a0) * k / pasos)),
                            cy + r * math.sin(math.radians(a0 + (a1 - a0) * k / pasos))) for k in range(pasos + 1)])
    return salida


def vista_dxf(lam, entidades, caja, x, y, escala, nombre):
    """Dibuja una vista del DXF (mm) en la lámina (pulgadas), con una forma libre por tipo de línea."""
    x0, y0, x1, y1 = caja
    estilos = [(("Trazos",), "accent3", 0.6, "dash"), (("Ejes",), "accent4", 0.6, "lgDashDot"),
               (("Elementos",), "tx1", 0.9, None), (("Contornos",), "tx1", 1.25, None)]
    for capas, c, pt, guion in estilos:
        trazos = [[(x + (px - x0) * escala, y + (y1 - py) * escala) for px, py in s]
                  for s in polilineas_dxf(entidades, capas)
                  if all(x0 <= px <= x1 and y0 <= py <= y1 for px, py in s)]
        if trazos:
            lam.trazo(trazos, c=c, pt=pt, guion=guion, nombre=f"Plano {nombre} {capas[0]}",
                      alt=f"Vista {nombre} del plano preliminar")


# ---------- Figuras ----------
def preparar_figuras():
    FIGURAS.mkdir(exist_ok=True)
    rodillo = Image.open(GRAFICO / "imagen_ia_conjunto_rodillo_marcado.jpeg").convert("RGB")
    tuerca = Image.open(GRAFICO / "imagen_ia_conjunto_tuerca_marcada.jpeg").convert("RGB")
    # Ambas imágenes son iguales salvo el anillo: se compone una versión limpia sin marcas.
    limpia = tuerca.copy()
    zona = (475, 345, 635, 505)
    limpia.paste(rodillo.crop(zona), zona[:2])
    salida = {"conjunto": limpia.crop((0, 46, 895, 566)),
              "detalle_rodillo": rodillo.crop((205, 62, 525, 302)),
              "detalle_tuerca": tuerca.crop((440, 346, 730, 516))}
    rutas = {}
    for nombre, im in salida.items():
        ruta = FIGURAS / f"{nombre}.png"
        im.save(ruta, optimize=True)
        rutas[nombre] = (ruta, im.width / im.height)
    return rutas


# ---------- Láminas ----------
# Seis bloques continuos de 2:30 (total 15:00). La asignación de integrantes se define en el grupo.


def lamina_portada(fig):
    s = Lamina(0, "Bloque 1", 30,
               "Buenas. Somos el Grupo 1 del curso S1091 y les presentamos nuestro trabajo final: una cortadora manual que transforma botellas PET en una tira continua. "
               "Entre los seis vamos a recorrer el problema, la solución mecánica, las ecuaciones de diseño y lo que todavía falta validar con el prototipo.")
    s.titulo("Cortadora manual de botellas PET", "ctrTitle")
    s.subtitulo("Tiras continuas por corte helicoidal controlado")
    ruta, asp = fig["conjunto"]
    s.imagen(ruta, 6.95, 1.75, 5.78, 5.78 / asp, "Ilustración del conjunto: botella sujeta por el cuello, rodillo, manivela, engranajes, husillo y cuchilla sobre una base con guías", radio=3500)
    s.caja(6.95, 1.75 + 5.78 / asp + .08, 5.78, .3, "Ilustración conceptual generada con IA", sz=11, c="bg2", nombre="Crédito de la imagen")
    s.caja(.7, 4.55, 5.9, 1.9, [
        {"t": "TP Final · Ingeniería Mecánica I · UTN FRBA · 2026", "b": True, "despues": 6},
        {"t": "Grupo 1 · S1091", "despues": 6},
        {"t": "Burelli · Fernandez · Franco Solignac · Kainer · Ledesma Blanco · Paredes", "despues": 6},
        {"t": "Prof. Abud · ATP Cáceres Guido"},
    ], sz=15, c="bg1", nombre="Datos del trabajo")
    return s


def tira(x, y, largo, alto, onda):
    n = 120
    sup = [(x + largo * k / n, y + onda * math.sin(k * .33) * .8 + onda * .55 * math.sin(k * .71)) for k in range(n + 1)]
    inf = [(x + largo * k / n, y + alto + onda * math.sin(k * .27 + 1.4) + onda * .5 * math.sin(k * .83)) for k in range(n, -1, -1)]
    return [sup + inf + [sup[0]]]


def lamina_problema():
    s = Lamina(1, "Bloque 1", 60,
               "Empiezo por el problema. Convertir botellas PET en tiras continuas es una forma simple de aprovechar el residuo, pero cuando el corte se hace a mano aparecen tres dificultades. "
               "Primero, la desalineación: la botella es cilíndrica y flexible, y tiende a desplazarse o deformarse frente a la herramienta. "
               "Segundo, el ancho irregular: esa falta de control produce una tira variable, como muestro en este esquema, que es solo ilustrativo y no una medición. "
               "Tercero, la exposición al filo, porque hay que sostener el envase y el elemento cortante al mismo tiempo. "
               "Todo depende de la habilidad de quien corta. De ahí sale nuestra pregunta: cómo obtener una tira continua y uniforme sin depender de esa habilidad.")
    s.titulo("Cortar una botella a mano depende del operador")
    items = ["Desalineación", "Ancho irregular", "Exposición al filo"]
    for k, t in enumerate(items):
        y = 1.55 + k * 1.14
        s.anillo(.6, y + .1, .62, k + 1, "accent4")
        s.caja(1.42, y, 4.75, .82, {"t": t, "b": True, "c": "tx2"}, sz=24, anchor="ctr", nombre=t)
    s.caja(6.65, 1.55, 6.08, .36, {"t": "A mano", "b": True, "c": "accent4"}, sz=18, nombre="Rótulo a mano")
    s.trazo(tira(6.65, 2.05, 6.08, .62, .07), c="accent4", pt=1, fondo="accent4", transparencia=70, nombre="Tira irregular", alt="Esquema de una tira de ancho irregular")
    s.caja(6.65, 3.05, 6.08, .36, {"t": "Con mecanismo", "b": True, "c": "accent1"}, sz=18, nombre="Rótulo con mecanismo")
    s.trazo([[(6.65, 3.52), (12.73, 3.52), (12.73, 4.14), (6.65, 4.14), (6.65, 3.52)]], c="accent1", pt=1, fondo="accent1", transparencia=70, nombre="Tira uniforme", alt="Esquema de una tira de ancho uniforme")
    s.tarjeta(.6, 4.95, 12.13, 1.45, {"t": "¿Cómo obtener una tira continua y uniforme sin depender de la habilidad manual?", "b": True, "c": "bg1", "algn": "ctr", "fuente": "+mj-lt"},
              fondo="tx2", sz=25, anchor="ctr", nombre="Pregunta del trabajo", margen=.3)
    return s


def lamina_objetivos():
    s = Lamina(1, "Bloque 1", 60,
               "Para responderla nos propusimos como objetivo principal desarrollar un dispositivo mecánico de accionamiento manual que transforme botellas PET en tiras continuas mediante un corte helicoidal controlado. "
               "Elegimos el verbo desarrollar porque implica diseñar, calcular y fabricar. Planteamos cinco objetivos secundarios: una sujeción exterior del cuello, que permita el giro y retenga la botella; "
               "un guiado longitudinal frente a una cuchilla fija; una transmisión manual que coordine giro y avance; regulaciones y piezas intercambiables para adaptarnos a distintos envases; "
               "y un prototipo experimental para evaluar todo lo anterior. A continuación, veamos qué encontramos en los antecedentes.")
    s.titulo("Objetivo: tira continua con una sola entrada manual")
    s.tarjeta(.6, 1.55, 5.0, 4.85, [
        {"t": "Objetivo principal", "b": True, "sz": 16, "c": "bg2", "despues": 10},
        {"t": "Desarrollar un dispositivo manual que transforme botellas PET en tiras continuas por corte helicoidal controlado", "c": "bg1"},
    ], fondo="tx2", sz=25, margen=.3, anchor="ctr", nombre="Objetivo principal")
    items = ["Sujeción del cuello", "Guiado", "Transmisión manual", "Adaptación a envases", "Prototipo"]
    for k, t in enumerate(items):
        y = 1.55 + k * .99
        s.anillo(6.0, y + .06, .66, k + 1, sz=18)
        s.caja(6.95, y, 5.78, .8, {"t": t, "c": "tx2", "b": True}, sz=24, anchor="ctr", nombre=t)
    return s


def lamina_antecedentes():
    s = Lamina(1, "Bloque 2", 75,
               "Revisamos dos trabajos recientes. Tylman y Dzierżek, en 2020, documentan una máquina de bajo costo, con piezas impresas en 3D, que produce tiras con cuchilla fija y un bobinado motorizado con engranajes de relación 1 a 10. "
               "Ellos mismos señalan que la irregularidad del ancho generó defectos en el material final. Eso nos indica que el problema no es solo cortar, sino controlar el avance. "
               "Meraj y colaboradores, en 2024, proponen una máquina automatizada con dos rodamientos afilados y un husillo roscado controlado por Arduino. "
               "Para nosotros es un antecedente clave, porque muestra que el husillo ya se usó para sincronizar corte y avance sobre una botella. "
               "Nuestra propuesta toma esa idea y la resuelve sin electrónica: con manivela, engranajes y husillo.")
    s.titulo("En los antecedentes, el avance es el punto crítico")
    s.tabla(.6, 1.55, [2.0, 3.45, 3.45, 3.23], [.6, .72, .72, .78, 1.0], [
        ["", "Tylman y Dzierżek (2020)^{1}", "Meraj et al. (2024)^{2}", "Este proyecto"],
        ["Accionamiento", "Bobinado motorizado", "Automatizado con Arduino", "Manual, por manivela"],
        ["Corte", "Cuchilla fija", "Dos rodamientos afilados", "Cuchilla fija comercial"],
        ["Avance", "Bobinado de la tira, engranajes 1:10", "Husillo roscado (lead screw)", "Engranajes y husillo vinculados al giro"],
        ["Qué aporta", "La irregularidad del ancho genera defectos en el material", "El husillo sincroniza corte y avance sobre una botella", "Coordinación mecánica con una única entrada manual"],
    ], sz=16)
    s.nota_pie([
        "^{1} Tylman, I., & Dzierżek, K. (2020). Filament for a 3D printer from PET bottles — Simple machine. International Journal of Mechanical Engineering and Robotics Research, 9(10), 1386–1392. https://doi.org/10.18178/ijmerr.9.10.1386-1392",
        "^{2} Meraj, M., Ku, P. X., Choo, H. L., & Aung, P. P. (2024). Design and development of an automated PET plastic bottle 3D printer filament making machine. Journal of Physics: Conference Series, 2923(1), 012005. https://doi.org/10.1088/1742-6596/2923/1/012005",
    ], y=5.8, h=1.2)
    return s


def lamina_principio(fig):
    s = Lamina(1, "Bloque 2", 75,
               "Esta es la solución. Aclaro que la imagen es una ilustración conceptual generada con inteligencia artificial: sirve para ubicar los componentes, pero no define dimensiones. "
               "El principio combina dos movimientos. El primero es el giro: un rodillo hace girar la botella por fricción. El segundo es el avance: un husillo desplaza longitudinalmente el carro que lleva la botella. "
               "La cuchilla queda fija a la base, así que es la botella la que se mueve frente a ella. La combinación de giro y avance dibuja una hélice sobre la pared del envase, y esa hélice es la tira. "
               "Durante el corte, lo único que hago como operador es girar la manivela. Ahora veamos cómo se usa y cómo se conectan los movimientos.")
    s.titulo("Giro más avance: un corte helicoidal controlado")
    ruta, asp = fig["conjunto"]
    ancho = 7.7
    s.imagen(ruta, .6, 1.55, ancho, ancho / asp, "Ilustración del conjunto con rótulos: sujeción exterior del cuello, rodillo, manivela, engranajes, husillo y tuerca, guías y carro, cuchilla metálica", radio=2500, borde="bg2")
    s.caja(.6, 1.55 + ancho / asp + .06, ancho, .28, "Ilustración conceptual generada con IA; no define dimensiones.", sz=11, c="accent6", nombre="Crédito de la imagen")
    items = [("Giro", "Rodillo por fricción", "accent1"), ("Avance", "Husillo y carro", "accent2"), ("Corte", "Cuchilla fija", "accent3")]
    for k, (t, d, c) in enumerate(items):
        y = 1.55 + k * 1.15
        s.anillo(8.7, y + .1, .66, k + 1, c, sz=18)
        s.caja(9.6, y, 3.13, .95, [{"t": t, "b": True, "sz": 22, "c": "tx2"}, d], sz=18, anchor="ctr", nombre=t)
    s.tarjeta(8.7, 5.1, 4.03, 1.2, {"t": "Durante el corte, el operador solo gira la manivela", "b": True, "c": "tx2"}, sz=19, anchor="ctr", nombre="Mensaje")
    return s


def lamina_proceso():
    s = Lamina(1, "Bloque 3", 60,
               "El uso tiene cinco pasos. Primero quito la base de la botella, porque el corte empieza en ese borde abierto. Después sujeto el cuello con una pieza desmontable de dos mitades, que gira sobre rodamientos. "
               "Tercero, regulo la posición y la presión del rodillo, y ajusto la cuchilla, que queda bloqueada durante la operación. Cuarto, giro la manivela: el corte avanza desde el borde abierto hacia el cuello. "
               "Quinto, me detengo antes de llegar a la franja próxima al hombro, que es donde apoya el rodillo y por eso queda sin cortar, y retiro la tira.")
    s.titulo("Del envase a la tira en cinco pasos")
    ejey, R = 2.72, .66
    x_hombro, x_cuerpo, x_fin = 2.55, 3.75, 10.55
    arriba = [(1.55, ejey - .3), (x_hombro, ejey - .3)]
    arriba += [(x_hombro + (x_cuerpo - x_hombro) * k / 24,
                ejey - .3 - (R - .3) * (1 - math.cos(math.pi * k / 24)) / 2) for k in range(1, 25)]
    arriba += [(x_fin, ejey - R)]
    abajo = [(x, 2 * ejey - y) for x, y in reversed(arriba)]
    s.trazo([arriba + abajo + [arriba[0]]], c="accent1", pt=1.75, fondo="accent1", transparencia=86, nombre="Esquema botella", alt="Esquema de botella horizontal con el cuello a la izquierda y el borde abierto a la derecha")
    s.trazo([[(x_fin, ejey - R), (11.05, ejey - R), (11.3, ejey - R * .55), (11.3, ejey + R * .55), (11.05, ejey + R), (x_fin, ejey + R)]],
            c="accent6", pt=1.25, guion="dash", nombre="Esquema base retirada")
    s.trazo([[(3.85, ejey - R), (4.75, ejey - R), (4.75, ejey + R), (3.85, ejey + R), (3.85, ejey - R)]], c="accent2", pt=1, fondo="accent2", transparencia=55, nombre="Esquema franja del rodillo")
    s.caja(1.72, ejey - .47, .58, .94, fondo="accent3", geom="roundRect", radio=14000, nombre="Esquema sujeción", alt="Sujeción exterior del cuello")
    paso, hel, x = .42, [], x_fin
    while x - paso / 2 > 5.0:
        hel.append([(x, ejey - R), (x - paso / 2, ejey + R)])
        x -= paso
    s.trazo(hel, c="accent4", pt=1.25, nombre="Esquema trayectoria helicoidal", alt="Líneas inclinadas que representan la trayectoria helicoidal del corte")
    def rotulo(tx, ty, tw, texto, lx, ly1, ly2, c="tx2"):
        s.caja(tx, ty, tw, .3, {"t": texto, "b": True, "c": c, "algn": "ctr"}, sz=15, nombre=f"Rótulo {texto}")
        s.recta(lx, ly1, lx, ly2, c=c, pt=1, punta=False)
    rotulo(.8, 1.5, 2.4, "Sujeción del cuello", 2.0, 1.82, ejey - .47, "accent3")
    rotulo(3.3, 1.5, 2.0, "Franja del rodillo", 4.3, 1.82, ejey - R, "tx2")
    rotulo(6.8, 1.5, 2.4, "Zona de corte", 8.0, 1.82, ejey - R, "accent4")
    rotulo(10.2, 1.5, 1.8, "Base retirada", 11.1, 1.82, ejey - R, "accent6")
    s.recta(10.3, ejey + R + .14, 5.1, ejey + R + .14, c="accent4", pt=1.75, nombre="Flecha de sentido")
    s.caja(5.2, ejey + R + .18, 5.1, .3, {"t": "Del borde abierto al cuello", "c": "accent4", "algn": "ctr", "b": True}, sz=15, nombre="Sentido del corte")
    pasos = ["Quitar la base", "Sujetar el cuello", "Regular rodillo y cuchilla", "Girar la manivela", "Retirar la tira"]
    w = 2.3
    for k, t in enumerate(pasos):
        x = .6 + k * (w + .1075)
        s.tarjeta(x, 4.25, w, 2.15, fondo="bg2", nombre=f"Fondo paso {k + 1}")
        s.anillo(x + .16, 4.4, .56, k + 1, sz=16)
        s.caja(x + .16, 5.08, w - .3, 1.2, {"t": t, "c": "tx2", "b": True}, sz=20, nombre=f"Paso {k + 1}")
    return s


def lamina_cadena():
    s = Lamina(1, "Bloque 3", 90,
               "Veamos la cadena cinemática. Hay una única entrada, la manivela, unida al eje del rodillo de modo que no haya giro relativo entre ambos. Desde ese eje salen dos caminos. "
               "Por arriba, el rodillo transmite el movimiento a la botella por fricción; como es un contacto exterior, giran en sentidos opuestos. "
               "Por abajo, un par de engranajes reduce la velocidad y la entrega al husillo, que al girar a través de una tuerca fija convierte el giro en avance del carro. "
               "Los dos caminos terminan en la misma trayectoria helicoidal, y el dato que la define es a, el avance por vuelta de botella: la velocidad del carro dividida por la velocidad de giro de la botella. "
               "La clave es que giro y avance nacen del mismo eje. Entonces quedan vinculados mecánicamente: si giro más rápido o más lento, los dos cambian juntos y la relación se mantiene, siempre que el rodillo no deslice. "
               "Esa es la diferencia con cortar a mano. Pasemos ahora a los dos eslabones críticos.")
    s.titulo("Una manivela, dos caminos cinemáticos")
    def caja(x, y, w, t, sub="", c="bg2", tc="tx2"):
        ps = [{"t": t, "b": True, "sz": 18, "c": tc, "algn": "ctr"}]
        if sub:
            ps.append({"t": sub, "sz": 16, "c": tc if c == "tx2" else "tx1", "algn": "ctr"})
        s.tarjeta(x, y, w, 1.02, ps, fondo=c, anchor="ctr", margen=.05, nombre=t)
    fy, ay, cy = 1.7, 4.0, 2.85
    caja(.6, cy, 1.6, "Manivela", "Entrada", "tx2", "bg1")
    caja(2.5, cy, 1.45, "Eje")
    s.recta(2.2, cy + .51, 2.5, cy + .51)
    s.recta(3.95, cy + .51, 4.4, cy + .51, punta=False)
    s.recta(4.4, fy + .51, 4.4, ay + .51, punta=False)
    s.recta(4.4, fy + .51, 4.75, fy + .51, c="accent1", pt=2.25)
    s.recta(4.4, ay + .51, 4.75, ay + .51, c="accent2", pt=2.25)
    caja(4.75, fy, 1.7, "Rodillo", "n_{r}")
    s.recta(6.45, fy + .51, 8.5, fy + .51, c="accent1", pt=2.25)
    s.caja(6.5, fy + .1, 1.95, .34, {"t": "Fricción", "b": True, "c": "accent1", "algn": "ctr"}, sz=16, nombre="Rótulo fricción")
    caja(8.5, fy, 1.8, "Botella gira", "n_{b}")
    caja(4.75, ay, 1.7, "Engranajes", "i")
    s.recta(6.45, ay + .51, 6.7, ay + .51, c="accent2", pt=2.25)
    caja(6.7, ay, 1.55, "Husillo", "L")
    s.recta(8.25, ay + .51, 8.5, ay + .51, c="accent2", pt=2.25)
    caja(8.5, ay, 1.8, "Carro avanza", "v")
    s.recta(10.3, fy + .51, 10.62, fy + .51, c="accent1", pt=2.25, punta=False)
    s.recta(10.3, ay + .51, 10.62, ay + .51, c="accent2", pt=2.25, punta=False)
    s.recta(10.62, fy + .51, 10.62, cy + .38, c="accent1", pt=2.25, punta=False)
    s.recta(10.62, ay + .51, 10.62, cy + .64, c="accent2", pt=2.25, punta=False)
    s.recta(10.62, cy + .38, 10.95, cy + .38, c="accent1", pt=2.25)
    s.recta(10.62, cy + .64, 10.95, cy + .64, c="accent2", pt=2.25)
    caja(10.95, cy, 1.78, "Hélice", "a = v / n_{b}", "tx2", "bg1")
    s.caja(.6, 5.45, 12.13, .75, {"t": "Giro y avance quedan **vinculados mecánicamente**", "algn": "ctr"}, sz=24, c="tx2", anchor="ctr", nombre="Mensaje")
    return s


def tarjeta_ecuacion(s, x, y, w, h, formula, pie, sz=25):
    s.tarjeta(x, y, w, h, [{"t": formula, "sz": sz, "b": True, "c": "tx2", "algn": "ctr", "fuente": "+mj-lt", "despues": 2},
                           {"t": pie, "sz": 15, "algn": "ctr"}], anchor="ctr", margen=.1, nombre="Ecuación")


def lamina_friccion(fig):
    s = Lamina(1, "Bloque 4", 75,
               "El primer eslabón crítico es el contacto entre rodillo y botella. La fuerza tangencial que puedo transmitir sin deslizamiento tiene un límite: el coeficiente de fricción estática por la fuerza normal. "
               "Es un límite de adherencia, no una fuerza constante. Si aprieto poco, el rodillo desliza y el avance del husillo pierde la relación prevista con el giro de la botella. Si aprieto demasiado, deformo el envase. "
               "Por eso la posición y la presión son regulables, y el intervalo correcto lo vamos a determinar experimentalmente. La segunda ecuación es la condición de rodadura sin deslizamiento: "
               "a igual velocidad del rodillo, una botella de mayor diámetro gira más lento. Eso va a importar enseguida para el paso del corte.")
    s.titulo("Fricción: transmitir el giro sin deslizar ni aplastar")
    ruta, asp = fig["detalle_rodillo"]
    s.imagen(ruta, .6, 1.55, 4.9, 4.9 / asp, "Detalle ilustrado del rodillo sobre la franja de la botella y la manivela, marcados con un anillo rojo", radio=2500, borde="bg2")
    s.caja(.6, 1.55 + 4.9 / asp + .06, 4.9, .28, "Ilustración conceptual generada con IA.", sz=11, c="accent6", nombre="Crédito de la imagen")
    tarjeta_ecuacion(s, 5.9, 1.55, 3.05, 1.3, "F_{t} ≤ μ_{s} · N", "Límite de adherencia^{3}")
    tarjeta_ecuacion(s, 9.13, 1.55, 3.6, 1.3, "n_{b} · D_{b} = n_{r} · D_{r}", "Rodadura sin deslizamiento^{4}")
    s.caja(5.9, 3.15, 6.83, 2.5, [
        {"t": "**Poca presión:** desliza", "viñeta": True, "despues": 10},
        {"t": "**Mucha presión:** aplasta", "viñeta": True, "despues": 10},
        {"t": "**Presión regulable:** intervalo por ensayos", "viñeta": True},
    ], sz=22, nombre="Consecuencias")
    s.nota_pie(["^{3} OpenStax. (2016). 6.2 Friction. En University Physics Volume 1. https://openstax.org/books/university-physics-volume-1/pages/6-2-friction",
                "^{4} OpenStax. (2016). 11.1 Rolling Motion. En University Physics Volume 1. https://openstax.org/books/university-physics-volume-1/pages/11-1-rolling-motion"], y=6.3, h=.7)
    return s


def lamina_husillo(fig):
    s = Lamina(1, "Bloque 4", 75,
               "El segundo eslabón es el avance. Un par de engranajes cilíndricos de dientes rectos conecta el eje del rodillo con el husillo. Como el conducido tiene más dientes, el husillo gira más lento que el rodillo: esa es la relación de reducción i. "
               "La tuerca está fija a la base, entonces el husillo gira y se desplaza a través de ella, y arrastra al carro, al que está retenido axialmente. Engranajes y apoyos acompañan al carro, así se conserva la distancia entre ejes. "
               "La velocidad del carro es L por la velocidad del husillo. Un detalle importante: L es el avance por vuelta, y coincide con el paso de rosca solo si el husillo tiene una entrada. Ahora combinemos estas relaciones.")
    s.titulo("Husillo: del giro reducido al avance longitudinal")
    ruta, asp = fig["detalle_tuerca"]
    s.caja(.6, 1.55, 6.83, 2.2, [
        {"t": "**Tuerca fija** a la base", "viñeta": True, "despues": 10},
        {"t": "El husillo arrastra el carro", "viñeta": True, "despues": 10},
        {"t": "L = paso solo con **una entrada**", "viñeta": True},
    ], sz=22, nombre="Funcionamiento")
    tarjeta_ecuacion(s, .6, 3.95, 4.05, 1.3, "i = z_{2} / z_{1} = n_{r} / n_{h}", "Reducción^{5}")
    tarjeta_ecuacion(s, 4.83, 3.95, 2.6, 1.3, "v = L · n_{h}", "Velocidad^{6}")
    s.imagen(ruta, 7.83, 1.55, 4.9, 4.9 / asp, "Detalle ilustrado del husillo y la tuerca fija, marcados con un anillo verde", radio=2500, borde="bg2")
    s.caja(7.83, 1.55 + 4.9 / asp + .06, 4.9, .28, "Ilustración conceptual generada con IA.", sz=11, c="accent6", nombre="Crédito de la imagen")
    s.nota_pie(["^{5} Kohara Gear Industry Co., Ltd. (s. f.). Internal gears: KHK technical information. https://khkgears.net/pdf/2025/internal-gears.pdf",
                "^{6} Thomson Industries, Inc. (s. f.). Lead vs. pitch: What's the difference? https://www.thomsonlinear.com/en/training/lead-screws/lead_vs_pitch"], y=6.3, h=.7)
    return s


def lamina_ecuacion():
    a_t8 = avance(L_T8, I_T8, 88.0)
    a_m8 = avance(L_M8, I_M8, 88.0)
    largo_m = math.pi * 88.0 * TRAMO_CILINDRICO / a_t8 / 1000
    vueltas_manivela = TRAMO_CILINDRICO / a_t8 * 88.0 / D_RODILLO
    s = Lamina(1, "Bloque 5", 105,
               "Si combino las relaciones anteriores obtengo la ecuación de diseño: a es igual a L por el diámetro de la botella, dividido i por el diámetro del rodillo. "
               "a es el paso de la hélice; todavía tenemos que verificar su correspondencia con el ancho real de la tira. Hicimos una primera pasada con valores de referencia, que no son definitivos. "
               f"Tomé un rodillo de 50 milímetros, leído del plano preliminar, y una botella de 88. Con una varilla roscada M8 común, sin reducción, a da apenas {a_m8:.1f} milímetros, y con reducción daría menos todavía. ".replace("2.2", "2,2")
               + f"Con un husillo de 8 milímetros de avance por vuelta, como los T8 de cuatro entradas, y una reducción de 2 a 1, a da unos {a_t8:.0f} milímetros. "
               f"Si suponemos un tramo de corte de 180 milímetros, serían unos {largo_m:.0f} metros de tira y unas {vueltas_manivela:.0f} vueltas de manivela. "
               "El gráfico deja otra conclusión: a crece con el diámetro de la botella. Por eso, para adaptar el avance a distintos envases, estudiamos pares de engranajes intercambiables.")
    s.titulo("Ecuación de diseño: el paso del corte")
    s.tarjeta(.6, 1.55, 5.1, 1.2, {"t": "a = L · D_{b} / (i · D_{r})", "sz": 32, "b": True, "c": "bg1", "algn": "ctr", "fuente": "+mj-lt"},
              fondo="tx2", anchor="ctr", nombre="Ecuación de diseño")
    s.caja(.6, 2.92, 5.1, .4, {"t": "Botella: D_{b} = 88 mm", "b": True, "c": "tx2"}, sz=20, nombre="Datos del ejemplo")
    datos = [(f"≈{a_t8:.0f} mm", "T8", "accent1"), (f"≈{a_m8:.1f} mm".replace(".", ","), "M8", "accent6")]
    for k, (v, d, c) in enumerate(datos):
        s.caja(.6 + k * 2.6, 3.42, 2.5, 1.3, [{"t": v, "sz": 34, "b": True, "c": c, "fuente": "+mj-lt"}, {"t": d, "sz": 18}], nombre=f"Dato {d}")
    s.tarjeta(.6, 4.95, 5.1, .75, {"t": "Valores de referencia", "b": True, "c": "tx2", "algn": "ctr"}, sz=20, anchor="ctr", nombre="Aclaración")
    s.grafico(6.0, 1.5, 6.73, 4.45, "Gráfico de barras del avance por vuelta de botella según diámetro, para dos combinaciones de husillo y reducción")
    s.nota_pie(["Valores a confirmar: D_{r} = 50 mm leído del plano preliminar; D_{b} a medir; M8 × 1,25 según ISO 261 (1998); L = 8 mm en husillos T8 comerciales de 4 entradas. Ecuación: Entrega 2, apartado 5.3; valores: elaboración propia."], y=6.2, h=.8)
    return s


def lamina_materiales():
    s = Lamina(1, "Bloque 5", 45,
               "Para el dispositivo real proponemos una base de chapa y perfiles de acero, con un carro en placa mecanizada. El husillo, la tuerca, los engranajes y los rodamientos serían preferentemente comerciales, una vez definidos los esfuerzos. "
               "El rodillo lleva núcleo rígido con recubrimiento elastomérico reemplazable, y la cuchilla es comercial. Para el prototipo académico estamos definiendo varias piezas impresas en 3D en PLA, con un relleno de alrededor del 30 % como máximo. Para cerrar, veamos los planos y lo que falta.")
    s.titulo("Materiales del dispositivo real")
    s.tabla(.6, 1.55, [3.0, 9.13], [.58, .68, .68, .68, .68, .68], [
        ["Elemento", "Propuesta"],
        ["Base", "Chapa y perfiles de acero, con puntos de fijación a un banco de trabajo"],
        ["Carro", "Placa mecanizada con alojamientos y ranuras de regulación"],
        ["Ejes y rodillo", "Ejes metálicos; rodillo con núcleo rígido y recubrimiento elastomérico reemplazable"],
        ["Transmisión", "Husillo, tuerca, engranajes y rodamientos, preferentemente comerciales"],
        ["Cuchilla", "Comercial, con portaherramientas desmontable"],
    ], sz=17)
    s.tarjeta(.6, 5.85, 12.13, .6, {"t": "**Prototipo:** piezas impresas en 3D en PLA (en definición)", "c": "tx2", "algn": "ctr"}, sz=20, anchor="ctr", nombre="Prototipo", margen=.05)
    return s


def lamina_plano(dxf):
    s = Lamina(1, "Bloque 6", 45,
               "Estos son los primeros planos del grupo, dibujados en CAD. Muestro el rodillo entre sus dos apoyos con rodamientos, la manivela y el porta rodamientos, partido en dos mitades. "
               "Las medidas que ven son las leídas del dibujo y están sujetas al dimensionamiento. Todavía faltan el conjunto general, la transmisión y las tolerancias, que son parte de lo que nos queda por cerrar.")
    s.titulo("Anteproyecto: conjunto del rodillo y sus apoyos")
    esc = .0215
    vista_dxf(s, dxf, (248, 20, 562, 126), .6, 1.5, esc, "frontal")
    vista_dxf(s, dxf, (128, 20, 212, 126), 7.55, 1.5, esc, "lateral")
    vista_dxf(s, dxf, (483, 123, 557, 197), 1.5, 4.25, esc, "manivela")
    vista_dxf(s, dxf, (573, 128, 647, 212), 4.3, 4.15, esc, "porta rodamientos")
    s.caja(.6, 3.84, 6.6, .26, {"t": "Rodillo entre apoyos, con manivela (vista interrumpida)", "algn": "ctr", "c": "accent6"}, sz=11, nombre="Rótulo plano frontal")
    s.caja(7.3, 3.84, 2.3, .26, {"t": "Vista lateral", "algn": "ctr", "c": "accent6"}, sz=11, nombre="Rótulo plano lateral")
    s.caja(.9, 5.88, 2.7, .26, {"t": "Manivela", "algn": "ctr", "c": "accent6"}, sz=11, nombre="Rótulo plano manivela")
    s.caja(3.65, 6.0, 3.1, .26, {"t": "Porta rodamientos (dos mitades)", "algn": "ctr", "c": "accent6"}, sz=11, nombre="Rótulo plano porta rodamientos")
    datos = [("Ø50 mm", "Rodillo"), ("Ø30 mm", "Eje"), ("Ø70 mm", "Manivela"), ("70 × 80 mm", "Porta rodamientos")]
    for k, (v, d) in enumerate(datos):
        y = 1.55 + k * .98
        s.tarjeta(10.05, y, 2.68, .88, [{"t": v, "b": True, "sz": 22, "c": "accent1", "fuente": "+mj-lt", "algn": "ctr"}, {"t": d, "sz": 15, "algn": "ctr"}], anchor="ctr", margen=.05, nombre=d)
    s.tarjeta(7.3, 5.55, 5.43, .75, {"t": "Plano preliminar", "b": True, "c": "tx2", "algn": "ctr"}, sz=20, anchor="ctr", nombre="Aclaración")
    return s


def lamina_ensayos():
    s = Lamina(1, "Bloque 6", 60,
               "Lo que no se puede resolver en el papel se responde con el prototipo, que tiene que contestar cuatro preguntas. ¿Retiene? Controlamos que el cuello no se desplace durante el recorrido. "
               "¿Desliza? Marcamos rodillo y botella y comparamos las vueltas reales con la relación teórica. ¿Es uniforme? Medimos el ancho a lo largo de la tira y lo comparamos con a calculado. "
               "¿Es continua? Registramos cortes y longitud total. Con esas cuatro respuestas vamos a saber qué partes del diseño se sostienen y cuáles hay que corregir. Los próximos pasos son cerrar dimensiones y rango de envases, completar los planos, construir el prototipo, ensayar y ajustar el diseño.")
    s.titulo("El prototipo debe responder cuatro preguntas")
    cuadros = [("¿Retiene?", "Sujeción del cuello"), ("¿Desliza?", "Rodillo y botella"), ("¿Es uniforme?", "Ancho de la tira"), ("¿Es continua?", "Corte completo")]
    for k, (t, sub) in enumerate(cuadros):
        x, y = .6 + (k % 2) * 4.33, 1.55 + (k // 2) * 2.45
        s.tarjeta(x, y, 4.15, 2.3, [{"t": t, "b": True, "sz": 28, "c": "tx2", "fuente": "+mj-lt", "despues": 6}, {"t": sub, "c": "accent1", "b": True}], sz=20, margen=.22, anchor="ctr", nombre=t)
    s.caja(9.4, 1.55, 3.33, .4, {"t": "Próximos pasos", "b": True, "c": "tx2"}, sz=20, nombre="Próximos pasos")
    pasos = ["Cerrar dimensiones", "Completar planos", "Construir prototipo", "Ensayar y ajustar"]
    s.recta(9.68, 2.45, 9.68, 5.5, c="accent1", pt=2, punta=False, nombre="Línea de pasos")
    for k, t in enumerate(pasos):
        y = 2.2 + k * 1.04
        s.anillo(9.4, y, .56, k + 1, sz=15)
        s.caja(10.12, y - .12, 2.61, .8, t, sz=17, anchor="ctr", nombre=f"Paso {k + 1}")
    return s


def lamina_conclusiones():
    s = Lamina(2, "Bloque 6", 45,
               "Cierro con tres ideas. Este trabajo nos permitió aplicar cinemática, transmisión de movimiento y resistencia mecánica a un problema concreto. Una sola entrada manual alcanza para coordinar giro y avance, porque los vinculamos mecánicamente. El paso de corte se puede seleccionar por diseño, con husillo, reducción y rodillo. "
               "Y lo que falta validar es experimental: la adherencia del rodillo, la estabilidad del envase y la continuidad del corte. Muchas gracias. ¿Tienen alguna pregunta?")
    s.titulo("Conclusiones")
    items = [("Una entrada, dos movimientos", "La manivela coordina giro y avance"),
             ("Paso controlable por diseño", "a = L · D_{b} / (i · D_{r})"),
             ("Falta validar con el prototipo", "Fricción, estabilidad y continuidad")]
    for k, (t, d) in enumerate(items):
        y = 1.95 + k * 1.25
        s.caja(.7, y + .1, .7, .7, {"t": str(k + 1), "b": True, "c": "tx2", "algn": "ctr"}, sz=18, anchor="ctr", fondo="bg1", borde="accent2", borde_pt=3, geom="ellipse", nombre=f"Anillo {k + 1}")
        s.caja(1.7, y, 10.9, 1.0, [{"t": t, "b": True, "sz": 24, "c": "bg1"}, {"t": d, "sz": 19, "c": "bg2"}], anchor="ctr", nombre=t)
    s.caja(.7, 5.8, 11.9, .7, {"t": "Muchas gracias. ¿Preguntas?", "b": True, "c": "accent2", "fuente": "+mj-lt"}, sz=30, anchor="ctr", nombre="Cierre")
    return s


def lamina_bibliografia():
    s = Lamina(1, "Consulta", 0, "Lámina de consulta: no se expone. Queda disponible por si piden alguna referencia durante las preguntas.")
    s.titulo("Bibliografía")
    refs = [
        "International Organization for Standardization. (1998). ISO general purpose metric screw threads — General plan (ISO 261:1998).",
        "Kohara Gear Industry Co., Ltd. (s. f.). Calculation of gear dimensions, sección 4.1: Spur gears. KHK Gears. https://khkgears.net/gear-knowledge/gear-technical-reference/calculation-gear-dimensions/",
        "Kohara Gear Industry Co., Ltd. (s. f.). Internal gears: KHK technical information [Catálogo técnico]. https://khkgears.net/pdf/2025/internal-gears.pdf",
        "Meraj, M., Ku, P. X., Choo, H. L., & Aung, P. P. (2024). Design and development of an automated PET plastic bottle 3D printer filament making machine. Journal of Physics: Conference Series, 2923(1), 012005. https://doi.org/10.1088/1742-6596/2923/1/012005",
        "OpenStax. (2016). University Physics Volume 1: 6.2 Friction; 11.1 Rolling Motion; 12.3 Stress, strain, and elastic modulus. https://openstax.org/books/university-physics-volume-1",
        "Thomson Industries, Inc. (s. f.). Lead vs. pitch: What's the difference? https://www.thomsonlinear.com/en/training/lead-screws/lead_vs_pitch",
        "Tylman, I., & Dzierżek, K. (2020). Filament for a 3D printer from PET bottles — Simple machine. International Journal of Mechanical Engineering and Robotics Research, 9(10), 1386–1392. https://doi.org/10.18178/ijmerr.9.10.1386-1392",
    ]
    s.caja(.6, 1.5, 12.13, 4.3, [{"t": r, "despues": 6} for r in refs], sz=14, nombre="Referencias")
    s.caja(.6, 5.9, 11.0, .6, "Ilustraciones generadas con IA por el grupo (31/oct/2026). Planos preliminares y cálculos con valores de referencia: elaboración propia.", sz=12, c="accent6", anchor="ctr", nombre="Crédito de la imagen")
    return s


# ---------- Gráfico nativo ----------
def libro_xlsx(categorias, series):
    """Libro mínimo embebido para que el gráfico se pueda editar desde PowerPoint."""
    def celda(ref, v):
        if isinstance(v, str):
            return f'<c r="{ref}" t="inlineStr"><is><t>{escape(v)}</t></is></c>'
        return f'<c r="{ref}"><v>{v}</v></c>'
    filas = '<row r="1">' + celda("A1", "Botella") + "".join(celda(f"{chr(66 + j)}1", n) for j, (n, _) in enumerate(series)) + "</row>"
    for i, cat in enumerate(categorias):
        filas += f'<row r="{i + 2}">' + celda(f"A{i + 2}", cat) + "".join(celda(f"{chr(66 + j)}{i + 2}", v[i]) for j, (_, v) in enumerate(series)) + "</row>"
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for nombre, datos in [
            ("[Content_Types].xml", XML + '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/></Types>'),
            ("_rels/.rels", XML + f'<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="{REL}/officeDocument" Target="xl/workbook.xml"/></Relationships>'),
            ("xl/workbook.xml", XML + f'<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="{REL}"><sheets><sheet name="Datos" sheetId="1" r:id="rId1"/></sheets></workbook>'),
            ("xl/_rels/workbook.xml.rels", XML + f'<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="{REL}/worksheet" Target="worksheets/sheet1.xml"/></Relationships>'),
            ("xl/worksheets/sheet1.xml", XML + f'<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>{filas}</sheetData></worksheet>'),
        ]:
            info = zipfile.ZipInfo(nombre, FECHA_ZIP)
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, datos)
    return buf.getvalue()


def grafico_xml():
    categorias = [n for n, _ in BOTELLAS]
    series = [("M8: L = 1,25, i = 1", [round(avance(L_M8, I_M8, d), 2) for _, d in BOTELLAS]),
              ("T8: L = 8, i = 2", [round(avance(L_T8, I_T8, d), 2) for _, d in BOTELLAS])]
    def texto(sz, b=False, c="tx1"):
        return (f'<c:txPr><a:bodyPr/><a:lstStyle/><a:p><a:pPr><a:defRPr sz="{sz * 100}" b="{int(b)}">{relleno(c)}'
                f'<a:latin typeface="+mn-lt"/></a:defRPr></a:pPr><a:endParaRPr lang="es-AR"/></a:p></c:txPr>')
    sers = ""
    cat_pts = "".join(f'<c:pt idx="{i}"><c:v>{escape(n)}</c:v></c:pt>' for i, n in enumerate(categorias))
    for j, (nombre, vals) in enumerate(series):
        col = chr(66 + j)
        c = ["accent6", "accent1"][j]
        pts = "".join(f'<c:pt idx="{i}"><c:v>{v}</c:v></c:pt>' for i, v in enumerate(vals))
        sers += (f'<c:ser><c:idx val="{j}"/><c:order val="{j}"/><c:tx><c:strRef><c:f>Datos!${col}$1</c:f><c:strCache><c:ptCount val="1"/><c:pt idx="0"><c:v>{escape(nombre)}</c:v></c:pt></c:strCache></c:strRef></c:tx>'
                 f'<c:spPr>{relleno(c)}</c:spPr><c:invertIfNegative val="0"/>'
                 f'<c:dLbls><c:numFmt formatCode="0.0" sourceLinked="0"/><c:spPr><a:noFill/><a:ln><a:noFill/></a:ln></c:spPr>{texto(14, True)}<c:dLblPos val="outEnd"/><c:showLegendKey val="0"/><c:showVal val="1"/><c:showCatName val="0"/><c:showSerName val="0"/><c:showPercent val="0"/><c:showBubbleSize val="0"/></c:dLbls>'
                 f'<c:cat><c:strRef><c:f>Datos!$A$2:$A${len(vals) + 1}</c:f><c:strCache><c:ptCount val="{len(vals)}"/>{cat_pts}</c:strCache></c:strRef></c:cat>'
                 f'<c:val><c:numRef><c:f>Datos!${col}$2:${col}${len(vals) + 1}</c:f><c:numCache><c:formatCode>General</c:formatCode><c:ptCount val="{len(vals)}"/>{pts}</c:numCache></c:numRef></c:val></c:ser>')
    titulo = ('<c:title><c:tx><c:rich><a:bodyPr/><a:lstStyle/><a:p><a:pPr><a:defRPr sz="1500" b="1"/></a:pPr>'
              f'<a:r><a:rPr lang="es-AR" sz="1500" b="1">{relleno("tx2")}<a:latin typeface="+mn-lt"/></a:rPr><a:t>a [mm]</a:t></a:r></a:p></c:rich></c:tx><c:overlay val="0"/></c:title>')
    gris = relleno("accent6", 70)
    xml = (XML + '<c:chartSpace xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
           f'xmlns:r="{REL}"><c:roundedCorners val="0"/><c:chart>{titulo}<c:autoTitleDeleted val="0"/><c:plotArea><c:layout/>'
           f'<c:barChart><c:barDir val="col"/><c:grouping val="clustered"/><c:varyColors val="0"/>{sers}<c:gapWidth val="70"/><c:overlap val="-5"/><c:axId val="111111111"/><c:axId val="222222222"/></c:barChart>'
           f'<c:catAx><c:axId val="111111111"/><c:scaling><c:orientation val="minMax"/></c:scaling><c:delete val="0"/><c:axPos val="b"/><c:numFmt formatCode="General" sourceLinked="0"/><c:majorTickMark val="none"/><c:minorTickMark val="none"/><c:tickLblPos val="nextTo"/><c:spPr><a:ln w="9525">{relleno("accent6")}</a:ln></c:spPr>{texto(14)}<c:crossAx val="222222222"/><c:crosses val="autoZero"/><c:auto val="1"/><c:lblAlgn val="ctr"/><c:lblOffset val="100"/><c:noMultiLvlLbl val="0"/></c:catAx>'
           f'<c:valAx><c:axId val="222222222"/><c:scaling><c:orientation val="minMax"/><c:max val="10"/><c:min val="0"/></c:scaling><c:delete val="0"/><c:axPos val="l"/><c:majorGridlines><c:spPr><a:ln w="6350">{gris}</a:ln></c:spPr></c:majorGridlines><c:numFmt formatCode="0" sourceLinked="0"/><c:majorTickMark val="none"/><c:minorTickMark val="none"/><c:tickLblPos val="nextTo"/><c:spPr><a:ln><a:noFill/></a:ln></c:spPr>{texto(14)}<c:crossAx val="111111111"/><c:crosses val="autoZero"/><c:crossBetween val="between"/><c:majorUnit val="2"/></c:valAx>'
           f'</c:plotArea><c:legend><c:legendPos val="b"/><c:overlay val="0"/>{texto(14)}</c:legend><c:plotVisOnly val="1"/><c:dispBlanksAs val="gap"/></c:chart>'
           '<c:externalData r:id="rId1"><c:autoUpdate val="0"/></c:externalData></c:chartSpace>')
    return xml, libro_xlsx(categorias, series)


# ---------- Partes del paquete ----------
def tema_xml():
    colores = "".join(f'<a:{k}><a:srgbClr val="{v}"/></a:{k}>' for k, v in TEMA.items())
    def relleno_tema():
        return '<a:solidFill><a:schemeClr val="phClr"/></a:solidFill>'
    lineas = "".join(f'<a:ln w="{w}"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln>' for w in (6350, 12700, 19050))
    efecto = '<a:effectStyle><a:effectLst/></a:effectStyle>' * 3
    return (XML + f'<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Cortadora PET"><a:themeElements>'
            f'<a:clrScheme name="Cortadora PET">{colores}</a:clrScheme>'
            f'<a:fontScheme name="Cortadora PET"><a:majorFont><a:latin typeface="{FUENTE_TITULO}"/><a:ea typeface=""/><a:cs typeface=""/></a:majorFont>'
            f'<a:minorFont><a:latin typeface="{FUENTE_CUERPO}"/><a:ea typeface=""/><a:cs typeface=""/></a:minorFont></a:fontScheme>'
            f'<a:fmtScheme name="Cortadora PET"><a:fillStyleLst>{relleno_tema() * 3}</a:fillStyleLst><a:lnStyleLst>{lineas}</a:lnStyleLst>'
            f'<a:effectStyleLst>{efecto}</a:effectStyleLst><a:bgFillStyleLst>{relleno_tema() * 3}</a:bgFillStyleLst></a:fmtScheme></a:themeElements></a:theme>')


GRUPO = ('<p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/>'
         '<a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>')


def ph(idn, nombre, tipo, x, y, w, h, texto, idx=None, cuerpo=""):
    i = f' idx="{idx}"' if idx is not None else ""
    return (f'<p:sp><p:nvSpPr><p:cNvPr id="{idn}" name="{nombre}"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr><p:ph type="{tipo}"{i}/></p:nvPr></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{e(x)}" y="{e(y)}"/><a:ext cx="{e(w)}" cy="{e(h)}"/></a:xfrm></p:spPr>'
            f'<p:txBody><a:bodyPr {cuerpo}/><a:lstStyle/><a:p><a:r><a:rPr lang="es-AR"/><a:t>{texto}</a:t></a:r></a:p></p:txBody></p:sp>')


def master_xml(n_layouts):
    ids = "".join(f'<p:sldLayoutId id="{2147483649 + k}" r:id="rId{k + 1}"/>' for k in range(n_layouts))
    nivel = lambda n: (f'<a:lvl{n}pPr marL="{228600 * (n - 1)}" indent="0" algn="l"><a:buNone/><a:defRPr sz="1600">{relleno("tx1")}<a:latin typeface="+mn-lt"/></a:defRPr></a:lvl{n}pPr>')
    return (XML + f'<p:sldMaster {NS}><p:cSld><p:bg><p:bgPr>{relleno("bg1")}<a:effectLst/></p:bgPr></p:bg><p:spTree>{GRUPO}'
            + ph(2, "Título", "title", .6, .5, 12.13, .9, "Título", cuerpo='anchor="ctr"')
            + ph(3, "Cuerpo", "body", .6, 1.55, 12.13, 4.8, "Texto", idx=1)
            + ph_numero(4, 4)
            + '</p:spTree></p:cSld><p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>'
            + f'<p:sldLayoutIdLst>{ids}</p:sldLayoutIdLst>'
            + f'<p:txStyles><p:titleStyle><a:lvl1pPr algn="l"><a:buNone/><a:defRPr sz="3400" b="1">{relleno("tx2")}<a:latin typeface="+mj-lt"/></a:defRPr></a:lvl1pPr></p:titleStyle>'
            + f'<p:bodyStyle>{nivel(1)}{nivel(2)}</p:bodyStyle><p:otherStyle>{nivel(1)}</p:otherStyle></p:txStyles></p:sldMaster>')


def ph_numero(idn, idx):
    return (f'<p:sp><p:nvSpPr><p:cNvPr id="{idn}" name="Número de lámina"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr><p:ph type="sldNum" sz="quarter" idx="{idx}"/></p:nvPr></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{e(11.83)}" y="{e(6.6)}"/><a:ext cx="{e(.9)}" cy="{e(.4)}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr>'
            f'<p:txBody><a:bodyPr lIns="0" tIns="0" rIns="0" bIns="0" anchor="ctr"/><a:lstStyle><a:lvl1pPr algn="r"><a:defRPr sz="1400">{relleno("accent6")}</a:defRPr></a:lvl1pPr></a:lstStyle>'
            f'<a:p><a:fld id="{CAMPO_NUMERO}" type="slidenum"><a:rPr lang="es-AR"><a:latin typeface="+mn-lt"/></a:rPr><a:t>‹#›</a:t></a:fld></a:p></p:txBody></p:sp>')


def layout_xml(nombre, fondo, formas, tipo):
    bg = f'<p:bg><p:bgPr>{relleno(fondo)}<a:effectLst/></p:bgPr></p:bg>' if fondo else ""
    return (XML + f'<p:sldLayout {NS} type="{tipo}" preserve="1"><p:cSld name="{nombre}">{bg}<p:spTree>{GRUPO}{formas}</p:spTree></p:cSld>'
            '<p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sldLayout>')


def ph_estilo(idn, nombre, tipo, x, y, w, h, texto, sz, c, idx=None, anchor="b", b=True):
    i = f' idx="{idx}"' if idx is not None else ""
    return (f'<p:sp><p:nvSpPr><p:cNvPr id="{idn}" name="{nombre}"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr><p:ph type="{tipo}"{i}/></p:nvPr></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{e(x)}" y="{e(y)}"/><a:ext cx="{e(w)}" cy="{e(h)}"/></a:xfrm></p:spPr>'
            f'<p:txBody><a:bodyPr lIns="0" tIns="0" rIns="0" bIns="0" anchor="{anchor}"><a:noAutofit/></a:bodyPr><a:lstStyle><a:lvl1pPr marL="0" indent="0" algn="l"><a:buNone/><a:defRPr sz="{sz * 100}" b="{int(b)}">{relleno(c)}</a:defRPr></a:lvl1pPr></a:lstStyle>'
            f'<a:p><a:r><a:rPr lang="es-AR"/><a:t>{texto}</a:t></a:r></a:p></p:txBody></p:sp>')


def layouts():
    portada = (ph_estilo(2, "Título", "ctrTitle", .7, 1.05, 5.9, 2.2, "Título", 44, "bg1")
               + ph_estilo(3, "Subtítulo", "subTitle", .7, 3.4, 5.9, 1.0, "Subtítulo", 21, "bg2", idx=1, anchor="t", b=False))
    contenido = ph_estilo(2, "Título", "title", .6, .5, 12.13, .9, "Título", 34, "tx2", anchor="ctr") + ph_numero(3, 12)
    cierre = ph_estilo(2, "Título", "title", .7, .55, 11.9, 1.1, "Título", 40, "bg1", anchor="ctr")
    return [layout_xml("Portada", "tx2", portada, "title"), layout_xml("Contenido", None, contenido, "titleOnly"),
            layout_xml("Cierre", "tx2", cierre, "titleOnly")]


def notas_master_xml():
    return (XML + f'<p:notesMaster {NS}><p:cSld><p:bg><p:bgRef idx="1001"><a:schemeClr val="bg1"/></p:bgRef></p:bg><p:spTree>{GRUPO}'
            f'<p:sp><p:nvSpPr><p:cNvPr id="2" name="Imagen de lámina"/><p:cNvSpPr><a:spLocks noGrp="1" noRot="1" noChangeAspect="1"/></p:cNvSpPr><p:nvPr><p:ph type="sldImg" idx="2"/></p:nvPr></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="685800" y="1143000"/><a:ext cx="5486400" cy="3086100"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/><a:ln w="12700"><a:solidFill><a:prstClr val="black"/></a:solidFill></a:ln></p:spPr></p:sp>'
            f'<p:sp><p:nvSpPr><p:cNvPr id="3" name="Notas"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr><p:ph type="body" sz="quarter" idx="3"/></p:nvPr></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="685800" y="4400550"/><a:ext cx="5486400" cy="3600450"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr>'
            f'<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="es-AR"/><a:t>Notas</a:t></a:r></a:p></p:txBody></p:sp>'
            '</p:spTree></p:cSld><p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>'
            '<p:notesStyle><a:lvl1pPr marL="0" algn="l"><a:defRPr sz="1200"><a:solidFill><a:schemeClr val="tx1"/></a:solidFill><a:latin typeface="+mn-lt"/></a:defRPr></a:lvl1pPr></p:notesStyle></p:notesMaster>')


def notas_xml(texto):
    return (XML + f'<p:notes {NS}><p:cSld><p:spTree>{GRUPO}'
            '<p:sp><p:nvSpPr><p:cNvPr id="2" name="Imagen de lámina"/><p:cNvSpPr><a:spLocks noGrp="1" noRot="1" noChangeAspect="1"/></p:cNvSpPr><p:nvPr><p:ph type="sldImg"/></p:nvPr></p:nvSpPr><p:spPr/></p:sp>'
            '<p:sp><p:nvSpPr><p:cNvPr id="3" name="Notas"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr><p:ph type="body" idx="1"/></p:nvPr></p:nvSpPr><p:spPr/>'
            f'<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="es-AR" dirty="0"/><a:t>{escape(texto)}</a:t></a:r></a:p></p:txBody></p:sp>'
            '</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:notes>')


def rels(lista):
    cuerpo = "".join(f'<Relationship Id="{i}" Type="{t}" Target="{d}"/>' for i, t, d in lista)
    return XML + f'<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{cuerpo}</Relationships>'


def empaquetar(laminas):
    partes = {}
    tipos = {"/ppt/presentation.xml": "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml",
             "/ppt/slideMasters/slideMaster1.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml",
             "/ppt/theme/theme1.xml": "application/vnd.openxmlformats-officedocument.theme+xml",
             "/ppt/theme/theme2.xml": "application/vnd.openxmlformats-officedocument.theme+xml",
             "/ppt/notesMasters/notesMaster1.xml": "application/vnd.openxmlformats-officedocument.presentationml.notesMaster+xml",
             "/ppt/presProps.xml": "application/vnd.openxmlformats-officedocument.presentationml.presProps+xml",
             "/ppt/viewProps.xml": "application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml",
             "/ppt/tableStyles.xml": "application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml",
             "/ppt/charts/chart1.xml": "application/vnd.openxmlformats-officedocument.drawingml.chart+xml",
             "/docProps/core.xml": "application/vnd.openxmlformats-package.core-properties+xml",
             "/docProps/app.xml": "application/vnd.openxmlformats-officedocument.extended-properties+xml"}
    lays = layouts()
    for k, x in enumerate(lays, 1):
        partes[f"ppt/slideLayouts/slideLayout{k}.xml"] = x
        partes[f"ppt/slideLayouts/_rels/slideLayout{k}.xml.rels"] = rels([("rId1", f"{REL}/slideMaster", "../slideMasters/slideMaster1.xml")])
        tipos[f"/ppt/slideLayouts/slideLayout{k}.xml"] = "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"
    partes["ppt/slideMasters/slideMaster1.xml"] = master_xml(len(lays))
    partes["ppt/slideMasters/_rels/slideMaster1.xml.rels"] = rels(
        [(f"rId{k}", f"{REL}/slideLayout", f"../slideLayouts/slideLayout{k}.xml") for k in range(1, len(lays) + 1)]
        + [(f"rId{len(lays) + 1}", f"{REL}/theme", "../theme/theme1.xml")])
    partes["ppt/theme/theme1.xml"] = tema_xml()
    partes["ppt/theme/theme2.xml"] = tema_xml()
    partes["ppt/notesMasters/notesMaster1.xml"] = notas_master_xml()
    partes["ppt/notesMasters/_rels/notesMaster1.xml.rels"] = rels([("rId1", f"{REL}/theme", "../theme/theme2.xml")])
    chart, libro = grafico_xml()
    partes["ppt/charts/chart1.xml"] = chart
    partes["ppt/charts/_rels/chart1.xml.rels"] = rels([("rId1", f"{REL}/package", "../embeddings/Datos_grafico1.xlsx")])
    partes["ppt/embeddings/Datos_grafico1.xlsx"] = libro

    for n, lam in enumerate(laminas, 1):
        if lam.layout == 1:
            lam.numero(n)
        partes[f"ppt/slides/slide{n}.xml"] = (
            XML + f'<p:sld {NS}><p:cSld><p:spTree>{GRUPO}{"".join(lam.formas)}</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>')
        lista = [("rId1", f"{REL}/slideLayout", f"../slideLayouts/slideLayout{lam.layout + 1}.xml")]
        lista += [(f"rId{i + 2}", t, d) for i, (t, d) in enumerate(lam.rels)]
        lista.append((f"rId{len(lista) + 1}", f"{REL}/notesSlide", f"../notesSlides/notesSlide{n}.xml"))
        partes[f"ppt/slides/_rels/slide{n}.xml.rels"] = rels(lista)
        partes[f"ppt/notesSlides/notesSlide{n}.xml"] = notas_xml(lam.notas)
        partes[f"ppt/notesSlides/_rels/notesSlide{n}.xml.rels"] = rels([
            ("rId1", f"{REL}/notesMaster", "../notesMasters/notesMaster1.xml"), ("rId2", f"{REL}/slide", f"../slides/slide{n}.xml")])
        tipos[f"/ppt/slides/slide{n}.xml"] = "application/vnd.openxmlformats-officedocument.presentationml.slide+xml"
        tipos[f"/ppt/notesSlides/notesSlide{n}.xml"] = "application/vnd.openxmlformats-officedocument.presentationml.notesSlide+xml"

    for ruta in MEDIOS:
        partes[f"ppt/media/{ruta.name}"] = ruta.read_bytes()

    # Secciones: una por bloque de exposición
    secciones, orden = {}, []
    for n, lam in enumerate(laminas):
        if lam.seccion not in secciones:
            secciones[lam.seccion] = []
            orden.append(lam.seccion)
        secciones[lam.seccion].append(256 + n)
    sec_xml = "".join(
        f'<p14:section name="{escape(nom)}" id="{{{str(uuid.uuid5(uuid.NAMESPACE_DNS, nom)).upper()}}}"><p14:sldIdLst>'
        + "".join(f'<p14:sldId id="{i}"/>' for i in secciones[nom]) + "</p14:sldIdLst></p14:section>" for nom in orden)
    n_lam = len(laminas)
    sld_ids = "".join(f'<p:sldId id="{256 + k}" r:id="rId{k + 10}"/>' for k in range(n_lam))
    partes["ppt/presentation.xml"] = (
        XML + f'<p:presentation {NS} saveSubsetFonts="1"><p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId1"/></p:sldMasterIdLst>'
        f'<p:notesMasterIdLst><p:notesMasterId r:id="rId2"/></p:notesMasterIdLst><p:sldIdLst>{sld_ids}</p:sldIdLst>'
        f'<p:sldSz cx="12192000" cy="6858000"/><p:notesSz cx="6858000" cy="9144000"/>'
        f'<p:defaultTextStyle><a:lvl1pPr><a:defRPr lang="es-AR"><a:latin typeface="+mn-lt"/></a:defRPr></a:lvl1pPr></p:defaultTextStyle>'
        f'<p:extLst><p:ext uri="{{521415D9-36F7-43E2-AB2F-B90AF26B5E84}}"><p14:sectionLst xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main">{sec_xml}</p14:sectionLst></p:ext></p:extLst></p:presentation>')
    partes["ppt/_rels/presentation.xml.rels"] = rels(
        [("rId1", f"{REL}/slideMaster", "slideMasters/slideMaster1.xml"), ("rId2", f"{REL}/notesMaster", "notesMasters/notesMaster1.xml"),
         ("rId3", f"{REL}/presProps", "presProps.xml"), ("rId4", f"{REL}/viewProps", "viewProps.xml"),
         ("rId5", f"{REL}/theme", "theme/theme1.xml"), ("rId6", f"{REL}/tableStyles", "tableStyles.xml")]
        + [(f"rId{k + 10}", f"{REL}/slide", f"slides/slide{k + 1}.xml") for k in range(n_lam)])
    partes["ppt/presProps.xml"] = XML + f"<p:presentationPr {NS}/>"
    partes["ppt/viewProps.xml"] = XML + f"<p:viewPr {NS}/>"
    partes["ppt/tableStyles.xml"] = XML + '<a:tblStyleLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" def="{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}"/>'
    partes["docProps/core.xml"] = (
        XML + '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        '<dc:title>Cortadora manual de botellas PET</dc:title><dc:subject>TP Final Ingeniería Mecánica I</dc:subject><dc:creator>Grupo 1, curso S1091</dc:creator>'
        '<dcterms:created xsi:type="dcterms:W3CDTF">2026-11-01T12:00:00Z</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">2026-11-01T12:00:00Z</dcterms:modified></cp:coreProperties>')
    partes["docProps/app.xml"] = (XML + f'<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"><Application>generar_presentacion.py</Application><Slides>{n_lam}</Slides><Notes>{n_lam}</Notes></Properties>')
    partes["_rels/.rels"] = rels([
        ("rId1", f"{REL}/officeDocument", "ppt/presentation.xml"),
        ("rId2", "http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties", "docProps/core.xml"),
        ("rId3", f"{REL}/extended-properties", "docProps/app.xml")])
    overrides = "".join(f'<Override PartName="{p}" ContentType="{c}"/>' for p, c in sorted(tipos.items()))
    partes["[Content_Types].xml"] = (
        XML + '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/><Default Extension="png" ContentType="image/png"/>'
        f'<Default Extension="xlsx" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"/>{overrides}</Types>')

    with zipfile.ZipFile(SALIDA, "w", zipfile.ZIP_DEFLATED) as z:
        for nombre in ["[Content_Types].xml"] + sorted(k for k in partes if k != "[Content_Types].xml"):
            info = zipfile.ZipInfo(nombre, FECHA_ZIP)
            info.compress_type = zipfile.ZIP_DEFLATED
            datos = partes[nombre]
            z.writestr(info, datos.encode("utf-8") if isinstance(datos, str) else datos)


def main():
    fig = preparar_figuras()
    dxf = leer_dxf(GRAFICO / "Proy Mecanica.dxf")
    laminas = [lamina_portada(fig), lamina_problema(), lamina_objetivos(), lamina_antecedentes(), lamina_principio(fig),
               lamina_proceso(), lamina_cadena(), lamina_friccion(fig), lamina_husillo(fig), lamina_ecuacion(),
               lamina_materiales(), lamina_plano(dxf), lamina_ensayos(), lamina_conclusiones(), lamina_bibliografia()]
    transcurrido = 0
    for lam in laminas:
        if lam.segundos:
            ini, transcurrido = transcurrido, transcurrido + lam.segundos
            lam.notas = (f"{lam.seccion.upper()} · {lam.segundos // 60}:{lam.segundos % 60:02d} min "
                         f"(del {ini // 60}:{ini % 60:02d} al {transcurrido // 60}:{transcurrido % 60:02d}). {lam.notas}")
    empaquetar(laminas)
    print(f"{SALIDA.name}: {len(laminas)} láminas")


if __name__ == "__main__":
    main()
