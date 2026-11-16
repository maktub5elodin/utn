#!/usr/bin/env python3
"""Genera Presentacion_Cortadora_PET_S1091_Grupo_1.pptx (modelo 2.0) y su PDF, sin dependencias de PPTX.

Escribe el OOXML directamente con zipfile: formas y tablas quedan nativas y editables en PowerPoint.
El contenido de cada lámina está en las funciones lamina_*; los números salen de ../08_modelo_2/resultados.json.
Las figuras se arman en figuras/ a partir de los renders, planos e imágenes del modelo 2.0; los dos renders
propios de la presentación los hace renderizar_figuras.py (FreeCAD). La v1 (modelo 1) quedó en v1_modelo_1/.
Uso: python3 generar_presentacion.py [--sin-pdf]   (escribe el .pptx y, con LibreOffice, el .pdf)
"""
import json
import math
import re
import subprocess
import sys
import tempfile
import uuid
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageChops

AQUI = Path(__file__).resolve().parent
MODELO_2 = AQUI.parent / "08_modelo_2"
MODELO_1 = AQUI.parent / "06_modelo_3d"
FIGURAS = AQUI / "figuras"
SALIDA = AQUI / "Presentacion_Cortadora_PET_S1091_Grupo_1.pptx"
FECHA_ZIP = (2026, 11, 15, 12, 0, 0)

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


def corridas(texto, sz, c, b=False, i=False, fuente=None, link=None):
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
        if link:
            f += f'<a:hlinkClick r:id="{link}"/>'
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
            + corridas(p["t"], tam, col, p.get("b", False), p.get("i", False), p.get("fuente"), p.get("link"))
            + "</a:p>")


class Lamina:
    def __init__(self, layout, orador, segundos, bloque, notas):
        self.layout, self.orador, self.segundos, self.bloque, self.notas = layout, orador, segundos, bloque, notas
        self.formas, self.rels = [], []
        self.n = 1

    def _id(self):
        self.n += 1
        return self.n

    def rel(self, tipo, destino, externo=False):
        self.rels.append((tipo, destino, externo))
        return f"rId{len(self.rels) + 1}"  # rId1 es el layout

    def hipervinculo(self, url):
        return self.rel(f"{REL}/hyperlink", url, externo=True)

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
             transparencia=None, guion=None):
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
            f'<a:prstGeom prst="{geom}">{av}</a:prstGeom>{relleno(fondo, transparencia)}{linea(borde, borde_pt, guion)}</p:spPr>'
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

    def tabla(self, x, y, anchos, altos, filas, sz=14, resaltar_fila=None):
        grid = "".join(f'<a:gridCol w="{e(a)}"/>' for a in anchos)
        cuerpo = ""
        for i, fila in enumerate(filas):
            celdas = ""
            for j, celda in enumerate(fila):
                encabezado, lateral = i == 0, j == 0
                resaltada = (i == resaltar_fila) if resaltar_fila is not None else (j == len(fila) - 1 and not encabezado)
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


# ---------- Datos que todavía pueden cambiar ----------
# Ancho de la tira medido por el grupo (mínimo, máximo) en mm. Con None, la lámina dice que se está midiendo.
MEDICION_ANCHO = None
# Enlace al video de respaldo (.mp4 publicado por el grupo). Con None, la lámina muestra un recuadro pendiente.
VIDEO_URL = None

# Números del modelo 2.0 que sostienen decisiones (08_modelo_2/README.md, sección 4, y 00_concepto.md, 4.1)
MODELO = json.loads((MODELO_2 / "resultados.json").read_text(encoding="utf-8"))
RENDER = json.loads((AQUI / "build" / "render.json").read_text(encoding="utf-8")) if (AQUI / "build" / "render.json").exists() else {}


# ---------- Figuras ----------
def recorte_blanco(im, margen=0):
    """Recorta el blanco alrededor de la imagen y deja un margen parejo."""
    rgb = im.convert("RGB")
    caja = ImageChops.difference(rgb, Image.new("RGB", rgb.size, "white")).getbbox()
    x0, y0, x1, y1 = caja
    return im.crop((max(0, x0 - margen), max(0, y0 - margen), min(im.width, x1 + margen), min(im.height, y1 + margen)))


def pdf_a_png(pdf, dpi):
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / "hoja"
        subprocess.run(["pdftoppm", "-r", str(dpi), "-png", "-singlefile", str(pdf), str(base)], check=True)
        return Image.open(f"{base}.png").convert("RGB")


def preparar_figuras():
    """Genera figuras/*.png a partir de los renders, figuras y planos del modelo 2.0 (y del modelo 1)."""
    FIGURAS.mkdir(exist_ok=True)
    # FreeCAD guarda la hora dentro del PNG: se reescriben para que el mismo render dé el mismo archivo
    for ruta in FIGURAS.glob("render_*.png"):
        Image.open(ruta).save(ruta, optimize=True)
    m2 = MODELO_2
    salida = {}
    salida["portada"] = recorte_blanco(Image.open(m2 / "figuras" / "conjunto.png"), 30)
    salida["modelo_1"] = Image.open(MODELO_1 / "figuras" / "conjunto_inicio.png").convert("RGB").crop((340, 175, 1730, 965))
    salida["cabezal"] = Image.open(m2 / "figuras" / "detalle_cabezal.png").convert("RGB").crop((180, 120, 1460, 900))
    # Detalle A de la lámina 02: sin la columna de rótulos (llevan la numeración del plano); se rotula en la lámina
    hoja = pdf_a_png(m2 / "planos" / "02_cabezal.pdf", 200)
    k = hoja.width / 1820
    salida["detalle_a"] = hoja.crop(tuple(int(v * k) for v in DETALLE_A))
    salida["explotada"] = recorte_blanco(Image.open(FIGURAS / "render_explotada.png"), 20)
    salida["carrete_manivela"] = Image.open(FIGURAS / "render_carrete_manivela.png").convert("RGB").crop(RECORTE_CARRETE)
    # Mosaico de las piezas impresas, en el orden de la ficha (sin el vaso de lastre, que no se imprimió)
    mini = m2 / "ficha" / "miniaturas"
    mosaico = Image.new("RGB", (4 * 400, 4 * 300), "white")
    for i, n in enumerate(PIEZAS_IMPRESAS):
        im = Image.open(mini / f"{n}.png").convert("RGBA")
        mosaico.paste(im, ((i % 4) * 400, (i // 4) * 300), im)
    salida["piezas_impresas"] = recorte_blanco(mosaico, 10)
    plantilla = pdf_a_png(m2 / "instructivo" / "build" / "plantilla_base_A3.pdf", 150)
    salida["plantilla"] = plantilla.crop((205, 70, 2275, 1285))
    for n in ("paso_12", "paso_22"):
        salida[n] = recorte_blanco(Image.open(m2 / "instructivo" / "pasos" / f"{n}.png"), 10)
    rutas = {}
    for nombre, im in salida.items():
        ruta = FIGURAS / f"{nombre}.png"
        im.save(ruta, optimize=True)
        rutas[nombre] = (ruta, im.width / im.height)
    return rutas


DETALLE_A = (1010, 555, 1619, 1030)        # en píxeles de la lámina a 1820 de ancho
# Altura de cada rótulo del detalle A, como fracción del alto del recorte (la línea de referencia llega al borde)
ROTULOS_A = [("Labio exterior", .116), ("Pisador", .191), ("Hoja", .278), ("Calce", .519),
             ("Chapita", .720), ("Placa del cabezal", .808), ("Taco de MDF", .920)]
RECORTE_CARRETE = (0, 170, 1600, 1000)
TUERCA_MANGO = (620 / 1600, (530 - 170) / 830)   # posición de la tuerca del mango en el recorte
PIEZAS_IMPRESAS = ["Cabezal", "LabioExterior", "Calce_7mm", "Calce_8mm", "Calce_9mm", "Calce_10mm", "Pisador",
                   "Zocalo", "Ojal", "Torre", "CarreteInferior", "CarreteSuperior", "Manivela", "Mango"]


def encajar(fig, nombre, x, y, w, h):
    """Posición de la imagen dentro de la caja (x, y, w, h), centrada y sin deformar."""
    asp = fig[nombre][1]
    if w / h > asp:
        ancho, alto = h * asp, h
    else:
        ancho, alto = w, w / asp
    return x + (w - ancho) / 2, y + (h - alto) / 2, ancho, alto


# ---------- Láminas ----------
# Seis integrantes; cada uno expone lo que hizo. Las notas llevan orador, tiempo y minuto de inicio y fin.


def lamina_portada(fig):
    s = Lamina(0, "Camila", 15, "Apertura",
               "Buenas. Somos el Grupo 1 del curso S1091. Les presentamos nuestro trabajo final: una cortadora manual que convierte una botella PET en una tira continua. "
               "La trajimos funcionando.")
    s.titulo("Cortadora manual de botellas PET", "ctrTitle")
    s.subtitulo("Tiras continuas por corte helicoidal controlado")
    x, y, w, h = encajar(fig, "portada", 7.0, .9, 5.75, 5.3)
    s.imagen(fig["portada"][0], x, y, w, h, "Modelo 2.0 de la cortadora: base de MDF, botella vertical sobre una varilla, cabezal de corte, ojal y carrete con manivela", radio=2500)
    s.caja(x, y + h + .06, w, .3, "Modelo 2.0 en FreeCAD", sz=11, c="bg2", nombre="Crédito de la imagen")
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
    s = Lamina(1, "Camila", 45, "Apertura",
               "El problema. Cortar una botella en tira a mano tiene tres dificultades: la botella es flexible y se desalinea frente al filo, "
               "el ancho de la tira sale irregular, como muestra este esquema, que es ilustrativo, y hay que sostener la botella y el filo al mismo tiempo. "
               "Todo depende de la habilidad de quien corta. De ahí sale nuestra pregunta: cómo obtener una tira continua y uniforme sin depender de esa habilidad.")
    s.titulo("Cortar una botella a mano depende del operador")
    items = ["Desalineación", "Ancho irregular", "Exposición al filo"]
    for k, t in enumerate(items):
        y = 1.55 + k * 1.14
        s.anillo(.6, y + .1, .62, k + 1, "accent4")
        s.caja(1.42, y, 4.75, .82, {"t": t, "b": True, "c": "tx2"}, sz=24, anchor="ctr", nombre=t)
    s.caja(6.65, 1.55, 6.08, .36, {"t": "A mano", "b": True, "c": "accent4"}, sz=18, nombre="Rótulo a mano")
    s.trazo(tira(6.65, 2.05, 6.08, .62, .07), c="accent4", pt=1, fondo="accent4", transparencia=70, nombre="Esquema tira irregular", alt="Esquema de una tira de ancho irregular")
    s.caja(6.65, 3.05, 6.08, .36, {"t": "Con mecanismo", "b": True, "c": "accent1"}, sz=18, nombre="Rótulo con mecanismo")
    s.trazo([[(6.65, 3.52), (12.73, 3.52), (12.73, 4.14), (6.65, 4.14), (6.65, 3.52)]], c="accent1", pt=1, fondo="accent1", transparencia=70, nombre="Esquema tira uniforme", alt="Esquema de una tira de ancho uniforme")
    s.tarjeta(.6, 4.95, 12.13, 1.45, {"t": "¿Cómo obtener una tira continua y uniforme sin depender de la habilidad manual?", "b": True, "c": "bg1", "algn": "ctr", "fuente": "+mj-lt"},
              fondo="tx2", sz=25, anchor="ctr", nombre="Pregunta del trabajo", margen=.3)
    return s


def lamina_objetivos():
    s = Lamina(1, "Camila", 35, "Apertura",
               "Nuestro objetivo principal: desarrollar un dispositivo manual que transforme la botella en tira mediante un corte helicoidal controlado. "
               "Desarrollar implica diseñar, calcular y fabricar. Para lograrlo nos propusimos sostener la botella sin cargar el cuello, fijar el ancho por geometría, "
               "accionarla con una manivela directa, adaptarla con calces y llegar a un prototipo que funcione.")
    s.titulo("Objetivo: una tira continua con una sola entrada manual")
    s.tarjeta(.6, 1.55, 5.0, 4.85, [
        {"t": "Objetivo principal", "b": True, "sz": 16, "c": "bg2", "despues": 10},
        {"t": "Desarrollar un dispositivo manual que transforme botellas PET en tiras continuas por corte helicoidal controlado", "c": "bg1"},
    ], fondo="tx2", sz=25, margen=.3, anchor="ctr", nombre="Objetivo principal")
    items = ["Cuello sin carga", "Ancho fijado por geometría", "Manivela directa", "Adaptación con calces", "Prototipo funcional"]
    for k, t in enumerate(items):
        y = 1.55 + k * .99
        s.anillo(6.0, y + .06, .66, k + 1, sz=18)
        s.caja(6.95, y, 5.78, .8, {"t": t, "c": "tx2", "b": True}, sz=24, anchor="ctr", nombre=t)
    return s


def lamina_antecedentes():
    s = Lamina(1, "Camila", 40, "Apertura",
               "Partimos de dos trabajos. Tylman y Dzierżek usan cuchilla fija y bobinado motorizado, y señalan que el ancho irregular arruina el material final. "
               "Meraj y colaboradores sincronizan corte y avance con un husillo controlado por Arduino. "
               "Nosotros llegamos a algo más simple: la guía fija el paso y la propia tira arrastra la botella. Sergio cuenta cómo llegamos ahí.")
    s.titulo("Antecedentes: el ancho de la tira es lo crítico")
    s.tabla(.6, 1.55, [2.0, 3.35, 3.35, 3.43], [.6, .72, .72, .78, 1.0], [
        ["", "Tylman y Dzierżek (2020)^{1}", "Meraj et al. (2024)^{2}", "Este proyecto"],
        ["Accionamiento", "Bobinado motorizado", "Automatizado con Arduino", "Manual, manivela directa al carrete"],
        ["Corte", "Cuchilla fija", "Dos rodamientos afilados", "Hoja de trincheta fija sobre un calce"],
        ["Avance", "Bobinado de la tira, engranajes 1:10", "Husillo roscado (lead screw)", "La guía fija el paso; la tira arrastra la botella"],
        ["Qué aporta", "La irregularidad del ancho genera defectos en el material", "El husillo sincroniza corte y avance sobre una botella", "Ancho fijado por geometría, sin mecanismo de avance"],
    ], sz=16)
    s.nota_pie([
        "^{1} Tylman, I., & Dzierżek, K. (2020). Filament for a 3D printer from PET bottles — Simple machine. International Journal of Mechanical Engineering and Robotics Research, 9(10), 1386–1392. https://doi.org/10.18178/ijmerr.9.10.1386-1392",
        "^{2} Meraj, M., Ku, P. X., Choo, H. L., & Aung, P. P. (2024). Design and development of an automated PET plastic bottle 3D printer filament making machine. Journal of Physics: Conference Series, 2923(1), 012005. https://doi.org/10.1088/1742-6596/2923/1/012005",
    ], y=5.8, h=1.2)
    return s


def lamina_modelo_1(fig):
    s = Lamina(1, "Sergio", 50, "Del modelo 1 al 2.0",
               "Nuestro primer diseño, el de la segunda entrega, hacía girar la botella con un rodillo por fricción y la hacía avanzar con un husillo y engranajes. "
               "Al modelarlo para construirlo vimos dos problemas. El rodillo podía resbalar: la fuerza que transmite depende del rozamiento, y cae si la botella se deforma. "
               "Y el cuello cargaba con todo: sostenía la botella, tomaba el empuje y giraba, con casi 27 centímetros de botella en voladizo. "
               "Así que lo descartamos antes de construirlo. Fue parte normal del diseño.")
    s.titulo("Modelo 1: lo descartamos antes de construirlo")
    x, y, w, h = encajar(fig, "modelo_1", .6, 1.5, 7.3, 4.95)
    s.imagen(fig["modelo_1"][0], x, y, w, h, "Render del modelo 1: botella horizontal sujeta del cuello, rodillo, engranajes, husillo, tuerca fija y cuchilla fija", radio=2500, borde="bg2")
    s.caja(x, y + h + .04, w, .28, "Modelo 1 en FreeCAD (Entrega 2)", sz=11, c="accent6", nombre="Crédito de la imagen")
    items = [("Rodillo por fricción", "Podía resbalar: F_{t} ≤ μ_{s}·N"),
             ("Cuello", "Sostenía, empujaba y giraba, con 269 mm en voladizo")]
    for k, (t, d) in enumerate(items):
        yy = 1.55 + k * 1.75
        s.anillo(8.3, yy + .12, .62, k + 1, "accent4")
        s.caja(9.1, yy, 3.63, 1.55, [{"t": t, "b": True, "sz": 22, "c": "tx2", "despues": 4}, d], sz=18, nombre=t)
    s.tarjeta(8.3, 5.15, 4.43, 1.25, {"t": "Iteración de diseño: del modelo al cambio de principio", "b": True, "c": "tx2"}, sz=18, anchor="ctr", nombre="Mensaje")
    return s


def flecha_arco(s, cx, cy, r, a0, a1, c, nombre):
    """Arco de a0 a a1 (grados, sentido horario en pantalla) con punta al final."""
    n = 24
    pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * k / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * k / n))) for k in range(n + 1)]
    s.trazo([pts[:-1]], c=c, pt=2.5, nombre=nombre)
    s.recta(*pts[-3], *pts[-1], c=c, pt=2.5, nombre=nombre + " punta")


def lamina_principio():
    s = Lamina(1, "Sergio", 70, "Del modelo 1 al 2.0",
               "El modelo 2.0 cambia el principio: la tira tira de la botella. La botella va parada, con el pico arriba, sobre una varilla vertical. "
               "El borde cortado apoya en la guía del cabezal y la pared pasa por una ranura donde está la hoja fija. "
               "La tira pasa por un ojal y se enrolla en un carrete. Al girar la manivela, la tira se enrolla, tira de la pared, la botella gira y la hoja corta. "
               "El corte es una hélice: en cada vuelta la botella baja el ancho de la tira y vuelve a apoyar en la guía. El paso lo fija la guía, no un mecanismo. "
               "Y no hay nada que dependa de la fricción: si el corte pide más fuerza, se tira más fuerte.")
    s.titulo("Modelo 2.0: la tira tira de la botella")
    k = .021                                   # pulgadas por mm del modelo
    bx, by = 1.75, 3.95                        # eje de la botella
    rb = 44 * k
    xc, yc = bx + 180 * k, by - 22.8 * k        # eje del carrete
    yt = by - rb                               # la tira sale tangente
    gris, naranja, verde = "accent6", "accent2", "accent1"
    s.caja(bx - rb, by - rb, 2 * rb, 2 * rb, fondo="bg2", borde=verde, borde_pt=2, geom="ellipse", nombre="Esquema botella")
    s.caja(bx - .07, by - .07, .14, .14, fondo=gris, geom="ellipse", nombre="Esquema varilla")
    s.caja(bx - .25, yt - .42, .95, .5, fondo=naranja, borde=None, geom="rect", nombre="Esquema cabezal", transparencia=25)
    s.recta(bx, yt, xc, yt, c=verde, pt=5, punta=False, nombre="Esquema tira")
    s.caja(bx + 70 * k - .08, yt - .2, .16, .4, fondo=naranja, geom="rect", nombre="Esquema ojal")
    for r, f in ((36.4, "bg2"), (21.2, verde), (16, naranja)):
        s.caja(xc - r * k, yc - r * k, 2 * r * k, 2 * r * k, fondo=f, borde=naranja if f == "bg2" else None, borde_pt=1.5, geom="ellipse", nombre="Esquema carrete")
    s.recta(xc, yc, xc + 80 * k, yc, c=naranja, pt=9, punta=False, nombre="Esquema manivela")
    s.caja(xc + 80 * k - 11 * k, yc - 11 * k, 22 * k, 22 * k, fondo=naranja, geom="ellipse", nombre="Esquema mango")
    # Visto desde arriba, botella y carrete giran en sentido horario (README del modelo 2.0, sección 2)
    flecha_arco(s, bx, by, rb + .2, 115, 235, "accent3", "Esquema giro botella")
    flecha_arco(s, xc, yc, 80 * k + .38, -45, 45, "accent3", "Esquema giro manivela")
    s.recta(bx + 1.6, yt - .32, bx + 2.5, yt - .32, c="accent3", pt=2.5, nombre="Esquema tiro")
    rot = [("Botella", bx - .25, by + rb + .3), ("Hoja", bx - .3, yt - .95), ("Tiro", bx + 1.75, yt - .78),
           ("Ojal", bx + 70 * k - .3, yt + .3), ("Carrete", xc - .5, yc + 38 * k + .12), ("Manivela", xc + .55, yc + .3)]
    for t, x, y in rot:
        s.caja(x, y, 1.2, .36, {"t": t, "b": True, "c": "tx2"}, sz=15, nombre=f"Esquema rótulo {t}")
    s.caja(.6, 6.1, 6.9, .3, "Vista desde arriba, sin escala", sz=12, c="accent6", nombre="Crédito del esquema")
    pasos = ["Manivela: enrolla la tira", "El tiro gira la botella contra la hoja", "Baja w por vuelta: la guía fija el paso"]
    for i, t in enumerate(pasos):
        y = 1.6 + i * 1.12
        s.anillo(8.0, y + .1, .62, i + 1, sz=18)
        s.caja(8.8, y, 3.93, .95, {"t": t, "c": "tx2", "b": True}, sz=19, anchor="ctr", nombre=f"Paso {i + 1}")
    s.tarjeta(8.0, 5.15, 4.73, 1.25, {"t": "Nada depende de la fricción", "b": True, "c": "bg1", "algn": "ctr"}, fondo="tx2", sz=22, anchor="ctr", nombre="Mensaje")
    return s


def lamina_cabezal(fig):
    s = Lamina(1, "Martín", 55, "Diseño y cuentas",
               "El requisito más importante es que el ancho sea constante, porque es lo que los antecedentes marcan como problema. "
               "En el cabezal, el ancho es la altura del filo sobre la guía, y esa altura la fija el calce que va debajo de la hoja. No depende del diámetro de la botella ni de la mano. "
               "La pared pasa por una ranura de 0,85 milímetros entre dos labios, así no se inclina, y el borde apoya sobre una chapita de metal para que no gaste el plástico; en el prototipo todavía falta ponerla. "
               "Para otro ancho se cambia el calce: hay de 7, 8, 9 y 10 milímetros.")
    s.titulo("El ancho de la tira lo fija el cabezal")
    x, y, w, h = encajar(fig, "cabezal", .6, 1.5, 5.6, 3.5)
    s.imagen(fig["cabezal"][0], x, y, w, h, "Render del cabezal de corte: placa sobre el taco de MDF, labios, chapita, calce, hoja, pisador y la tira saliendo hacia el ojal", radio=2500, borde="bg2")
    s.tarjeta(.6, 5.2, 5.6, 1.25, {"t": "**w** = altura del filo sobre la guía = espesor del **calce** (7, 8, 9 o 10 mm)", "c": "tx2"}, sz=18, anchor="ctr", nombre="Ecuación del ancho")
    ancho_a = 4.05
    asp = fig["detalle_a"][1]
    xa, ya, ha = 6.55, 1.5, ancho_a / asp
    s.imagen(fig["detalle_a"][0], xa, ya, ancho_a, ha, "Corte por la ranura del cabezal: pared de la botella entre los labios, hoja a la altura w sobre la chapita, calce, pisador, placa y taco de MDF")
    for t, f in ROTULOS_A:
        s.caja(xa + ancho_a + .04, ya + f * ha - .11, 2.1, .22, {"t": t, "c": "tx1"}, sz=11, anchor="ctr", nombre=f"Rótulo plano {t}")
    s.caja(6.55, ya + ha + .02, ancho_a, .26, {"t": "Corte por la ranura (lámina 2, detalle A)", "c": "accent6"}, sz=11, nombre="Rótulo plano detalle")
    s.caja(6.55, 5.35, 6.18, 1.1, "Ranura de 0,85 mm: la pared no se inclina. Falta la chapita del borde.",
           sz=17, c="tx2", nombre="Ranura y chapita")
    return s


def lamina_cuentas():
    fun = MODELO["funcionamiento"]
    coma = lambda v: f"{v}".replace(".", ",")
    s = Lamina(1, "Martín", 65, "Diseño y cuentas",
               "La cuenta que más decisiones tomó es la fuerza en la mano: el tiro de la tira por el radio del rollo, dividido por el brazo de la manivela. "
               "Comparamos tres transmisiones. El tren de engranajes de una bobinadora de filamento multiplica la velocidad y pide unos 85 newtons. "
               "Una reducción 1 a 3 baja la fuerza pero triplica las vueltas. La manivela directa al carrete pide unos 13 newtons, por debajo del criterio de 20, y no lleva engranajes. "
               "La tira aguanta unos 124 newtons, tres veces el tiro. Una aclaración: el tiro de 40 newtons es un supuesto, todavía no lo medimos. "
               "Y el modelo nos avisó que, hacia el final, la botella pesa tan poco que podría no bajar sola: previó un lastre de unos 115 gramos.")
    s.titulo("Cuentas clave: manivela directa, sin engranajes")
    s.tabla(.6, 1.55, [3.9, 2.3, 2.3], [.62, .7, .7, .7], [
        ["Transmisión", "Fuerza en la mano", "Vueltas por botella"],
        ["Tren de una bobinadora (×6,6)", "~85 N", "~7"],
        ["Directa 1:1 (elegida)", f"{coma(fun['fuerza_mano_N'])} N", str(fun["vueltas_manivela"])],
        ["Reducción 1:3", "~4 N", "~130"],
    ], sz=17, resaltar_fila=2)
    s.tarjeta(.6, 4.5, 8.5, 1.3, [{"t": "F = T · r / R", "b": True, "sz": 28, "fuente": "+mj-lt", "c": "tx2"},
                                 {"t": "T: tiro · r: radio del rollo · R: brazo (80 mm)", "sz": 16}],
              anchor="ctr", nombre="Ecuación de la fuerza", algn="ctr")
    datos = [(f"{fun['rotura_tira_N']} N", "rompe la tira: 3 veces el tiro"), (f"~{fun['lastre_total_g']} g", "de lastre previsto al final del corte")]
    for k, (v, d) in enumerate(datos):
        y = 1.55 + k * 2.15
        s.tarjeta(9.45, y, 3.28, 1.95, [{"t": v, "b": True, "sz": 30, "c": "accent1", "fuente": "+mj-lt", "algn": "ctr"}, {"t": d, "sz": 16, "algn": "ctr"}],
                  anchor="ctr", margen=.12, nombre=d)
    s.nota_pie(["Tiro de diseño T = 40 N: supuesto, todavía sin medir. Criterio: hasta 20 N en la mano. Rollo lleno: r = 26,4 mm. Valores del modelo 2.0 y del documento conceptual, sección 4."], y=5.95, h=.5)
    return s


def lamina_modelo_3d(fig):
    s = Lamina(1, "Martín", 40, "Diseño y cuentas",
               "Todo lo armamos primero en FreeCAD, un CAD paramétrico libre, equivalente a SolidWorks. Antes de imprimir comprobamos que ninguna pieza choque, "
               "al principio y al final del corte, que la manivela dé la vuelta completa sin tocar nada, que se pueda armar en orden, en 26 pasos, "
               "y que cada pieza se imprima sin soportes. De ahí salieron los planos y el instructivo de armado.")
    s.titulo("Todo se armó primero en el modelo 3D")
    x, y, w, h = encajar(fig, "explotada", .6, 1.5, 6.6, 4.95)
    s.imagen(fig["explotada"][0], x, y, w, h, "Vista explotada del modelo 2.0: zócalo, cabezal con sus capas, ojal, torre con rodamientos, carrete y manivela con el mango")
    s.caja(x, y + h + .02, w, .28, "Vista explotada (FreeCAD)", sz=11, c="accent6", nombre="Crédito de la imagen")
    s.tarjeta(7.55, 1.55, 5.18, .95, {"t": "FreeCAD: CAD paramétrico libre, equivalente a SolidWorks", "b": True, "c": "tx2"}, sz=17, anchor="ctr", nombre="Programa")
    items = ["Sin choques al inicio ni al final", "La manivela da la vuelta completa", "26 pasos de armado en orden", "Piezas sin soportes de impresión"]
    for k, t in enumerate(items):
        yy = 2.8 + k * .92
        s.anillo(7.55, yy + .08, .56, "✓", sz=16)
        s.caja(8.3, yy, 4.43, .72, {"t": t, "c": "tx2", "b": True}, sz=18, anchor="ctr", nombre=t)
    return s


def lamina_impresion(fig):
    s = Lamina(1, "Matías", 45, "Construcción",
               "Las piezas las imprimí en PLA, en una Bambu Lab P1S. Son 14 piezas: el cabezal, los calces, el zócalo, el ojal, la torre, el carrete y la manivela. "
               "Elegimos PLA porque es barato, fácil de imprimir y permite corregir rápido: el prototipo prueba el principio, no la resistencia final. "
               "El juego completo lleva unas 6 horas y menos de 200 gramos. Hubo reimpresiones y ajustes en el camino.")
    s.titulo("Piezas impresas en PLA")
    x, y, w, h = encajar(fig, "piezas_impresas", .6, 1.5, 6.6, 4.95)
    s.imagen(fig["piezas_impresas"][0], x, y, w, h, "Las 14 piezas impresas tal como van en la cama de la impresora")
    datos = [("14 piezas", "Bambu Lab P1S, sin soportes"), ("~6 h · ~190 g", "juego completo, estimado")]
    for k, (v, d) in enumerate(datos):
        yy = 1.55 + k * 1.45
        s.tarjeta(7.55, yy, 5.18, 1.25, [{"t": v, "b": True, "sz": 26, "c": "accent1", "fuente": "+mj-lt"}, {"t": d, "sz": 16}], anchor="ctr", nombre=v)
    s.tarjeta(7.55, 4.45, 5.18, 1.0, {"t": "**PLA:** barato, fácil de imprimir y rápido de corregir", "c": "tx2"}, sz=17, anchor="ctr", nombre="Por qué PLA")
    s.caja(7.55, 5.6, 5.18, .8, "Hubo reimpresiones y ajustes durante la construcción", sz=16, c="accent6", anchor="ctr", nombre="Reimpresiones")
    return s


def lamina_abastecimiento():
    s = Lamina(1, "Camila", 35, "Construcción",
               "Matías y yo nos ocupamos de los materiales. La ferretería tenía tornillos de hasta 45 milímetros y necesitábamos de 60, así que fuimos a una bulonera. "
               "En la maderera nos cortaron la base y el taco de MDF a medida. Y en el taller cuidamos dos reglas: la trincheta siempre guardada "
               "y el taladro desenchufado para cambiar la mecha.")
    s.titulo("Materiales, compras y seguridad")
    s.tarjeta(.6, 1.55, 5.9, 2.15, [{"t": "Bulonera", "b": True, "sz": 22, "c": "tx2", "despues": 4},
                                   "Tornillos de 60 mm (ferretería: hasta 45 mm)"], sz=18, nombre="Bulonera")
    s.tarjeta(.6, 3.95, 5.9, 2.15, [{"t": "Maderera", "b": True, "sz": 22, "c": "tx2", "despues": 4},
                                   "Base y taco de MDF cortados a medida"], sz=18, nombre="Maderera")
    s.tarjeta(6.85, 1.55, 5.88, 4.55, [{"t": "Seguridad en el taller", "b": True, "sz": 22, "c": "bg1", "despues": 10},
                                      {"t": "Trincheta siempre guardada", "viñeta": True, "c": "bg1", "despues": 8},
                                      {"t": "Taladro desenchufado para cambiar la mecha", "viñeta": True, "c": "bg1", "despues": 8},
                                      {"t": "Guantes para cortar", "viñeta": True, "c": "bg1"}],
              fondo="tx2", sz=19, margen=.3, nombre="Seguridad")
    return s


def lamina_taller(fig):
    s = Lamina(1, "Lautaro y Angelo", 60, "Construcción",
               "LAUTARO: Para perforar la base usamos una plantilla impresa en escala 1 a 1: se pega sobre el MDF, se marca con punzón y se agujerea. "
               "Las herramientas fueron el taladro, mechas de 9, 4 y 2,5 milímetros, destornillador y llaves. "
               "ANGELO: En el armado, la prensa fue clave: sujeta la base a la mesa y nos permitió trabajar con las dos manos. Los rodamientos entran a presión en la torre "
               "y la hoja va apretada entre el calce y el pisador. Hubo rediseños y reimpresiones mientras armábamos.")
    s.titulo("Construcción en el taller")
    cajas = [("plantilla", "Plantilla 1:1 para perforar"), ("paso_12", "Rodamientos a presión"), ("paso_22", "Hoja sobre el calce")]
    for i, (n, t) in enumerate(cajas):
        x0 = .6 + i * 4.11
        x, y, w, h = encajar(fig, n, x0, 1.5, 3.91, 2.6)
        s.imagen(fig[n][0], x, y, w, h, t, borde="bg2")
        s.caja(x0, 4.15, 3.91, .4, {"t": t, "c": "accent6", "algn": "ctr"}, sz=14, nombre=f"Rótulo {t}")
    s.tarjeta(.6, 4.8, 5.9, 1.6, [{"t": "Herramientas", "b": True, "c": "tx2", "sz": 19, "despues": 4}, "Taladro, mechas de 9, 4 y 2,5 mm, destornillador, llaves"],
              sz=16, nombre="Herramientas")
    s.tarjeta(6.83, 4.8, 5.9, 1.6, [{"t": "La prensa fue clave", "b": True, "c": "tx2", "sz": 19, "despues": 4}, "Sujeta la base: las dos manos quedan libres"],
              sz=16, nombre="Prensa")
    return s


def lamina_demo():
    s = Lamina(2, "Angelo (opera) y Lautaro", 150, "Demostración",
               "GUION DE LA DEMO. Antes de empezar: botella sin base, tapa perforada, lengüeta de 25 cm ya enganchada en el carrete, base sujeta con la prensa. "
               "ANGELO: Ahora lo ven funcionando. Giro la manivela en sentido horario, a ritmo parejo. Miren tres cosas. "
               "Uno: la botella gira sola, porque la tira la arrastra. Dos: la tira sale por el ojal y se enrolla en el carrete. Tres: yo solo marco la velocidad; la fuerza la pide el corte. "
               "Al arrancar la acompaño con la mano hasta que el borde se asienta en la guía; después sigue sola. "
               "LAUTARO: mientras Angelo gira, muestra un tramo de tira cortada al público. "
               "Si se traba: parar, girar un poco hacia atrás, revisar ojal y borde, y seguir. Si no arranca en un minuto, pasar a la lámina siguiente, con el video.")
    s.titulo("Demostración en vivo")
    items = ["La botella gira: la tira la arrastra", "La tira pasa por el ojal y se enrolla", "La mano solo marca la velocidad"]
    for k, t in enumerate(items):
        y = 2.0 + k * 1.2
        s.caja(.7, y + .1, .7, .7, {"t": str(k + 1), "b": True, "c": "tx2", "algn": "ctr"}, sz=18, anchor="ctr", fondo="bg1", borde="accent2", borde_pt=3, geom="ellipse", nombre=f"Anillo {k + 1}")
        s.caja(1.7, y, 10.9, 1.0, {"t": t, "b": True, "sz": 26, "c": "bg1"}, anchor="ctr", nombre=t)
    s.caja(.7, 5.85, 11.9, .6, {"t": "Respaldo: video en la lámina siguiente", "c": "bg2"}, sz=16, anchor="ctr", nombre="Respaldo")
    return s


def lamina_video():
    s = Lamina(1, "Respaldo", 0, "Demostración",
               "Solo si la demostración en vivo falla: abrir el enlace y reproducir el video. Si la demo salió bien, pasar de largo.")
    s.titulo("Respaldo: video del funcionamiento")
    if VIDEO_URL:
        rid = s.hipervinculo(VIDEO_URL)
        s.tarjeta(.6, 2.2, 12.13, 2.4, [{"t": "Ver el video", "b": True, "sz": 30, "c": "tx2", "algn": "ctr", "despues": 8},
                                       {"t": VIDEO_URL, "sz": 16, "algn": "ctr", "link": rid}], anchor="ctr", nombre="Video")
    else:
        s.caja(.6, 1.6, 12.13, 4.6, [{"t": "VIDEO PENDIENTE", "b": True, "sz": 30, "c": "accent4", "algn": "ctr", "despues": 8},
                                     {"t": "Acá va el enlace al video (.mp4) del funcionamiento", "sz": 18, "algn": "ctr", "c": "accent6"}],
               anchor="ctr", borde="accent4", borde_pt=2, guion="dash", nombre="Video pendiente")
    return s


def lamina_respuestas():
    if MEDICION_ANCHO:
        uniforme = f"Sí: ancho entre {MEDICION_ANCHO[0]} y {MEDICION_ANCHO[1]} mm".replace(".", ",")
    else:
        uniforme = "A simple vista sí, no perfecta: midiendo mín. y máx."
    s = Lamina(1, "Lautaro", 65, "Resultados y cierre",
               "Antes de construir nos habíamos hecho cuatro preguntas. ¿Retiene? La botella, sí: la varilla y la tapa la sostienen sin cargar el cuello. "
               "La punta de la tira, al principio no: la ranura del carrete no la retenía y hoy la fija un tornillo, como solución provisoria. "
               "¿Desliza? No hay rodillo, así que no: la tira arrastra la botella. "
               "¿Es uniforme? A simple vista sí, pero no es perfecta; esta semana medimos el ancho mínimo y máximo. "
               "¿Es continua? Casi: la primera botella completa salió en dos tiras. Arrancar cuesta, y hacia el final la botella deja de bajar, como había anticipado el modelo.")
    s.titulo("Qué respondió el prototipo")
    cuadros = [("¿Retiene?", "Botella, sí. Punta de la tira: tornillo provisorio", "accent2"),
               ("¿Desliza?", "No: la tira arrastra la botella", "accent1"),
               ("¿Es uniforme?", uniforme, "accent1" if MEDICION_ANCHO else "accent2"),
               ("¿Es continua?", "Casi: una botella dio dos tiras", "accent2")]
    for k, (t, d, c) in enumerate(cuadros):
        x, y = .6 + (k % 2) * 6.17, 1.55 + (k // 2) * 2.5
        s.tarjeta(x, y, 5.96, 2.3, [{"t": t, "b": True, "sz": 28, "c": "tx2", "fuente": "+mj-lt", "despues": 6}, {"t": d, "c": c, "b": True}], sz=19, margen=.22, anchor="ctr", nombre=t)
    return s


def lamina_mejoras(fig):
    s = Lamina(1, "Matías", 45, "Resultados y cierre",
               "Las pruebas dejaron cuatro mejoras concretas. La tuerca del mango, debajo de la manivela, roza la tira en cada vuelta: hay que alejarla, rediseñando y reimprimiendo la manivela. "
               "La punta de la tira necesita un anclaje real en el carrete, una pinza o una ranura con traba, en lugar del tornillo provisorio. "
               "Para que la botella baje hasta el final, probar el vaso de lastre que ya está diseñado y que todavía no imprimimos. "
               "Y poner la chapita de metal: sin ella, el borde apoya en el plástico y la tira sale medio milímetro más ancha.")
    s.titulo("Mejoras identificadas")
    x, y, w, h = encajar(fig, "carrete_manivela", .6, 1.5, 6.6, 4.95)
    s.imagen(fig["carrete_manivela"][0], x, y, w, h, "Render del carrete con la manivela pasando sobre la tira: la tuerca del mango queda justo encima de la tira", borde="bg2")
    tx, ty = x + TUERCA_MANGO[0] * w, y + TUERCA_MANGO[1] * h
    s.caja(tx - .3, ty - .3, .6, .6, borde="accent4", borde_pt=3, geom="ellipse", nombre="Marca tuerca")
    s.caja(x, y + h + .02, w, .28, f"Tuerca del mango sobre la tira (modelo: {RENDER.get('luz_tuerca_mango_tira_mm', 0.7)} mm de luz)".replace(".", ","),
           sz=11, c="accent6", nombre="Crédito de la imagen")
    items = [("Manivela", "Alejar de la tira la tuerca del mango"), ("Anclaje de la tira", "Pinza o ranura con traba en el carrete"), ("Bajada", "Probar el lastre ya diseñado"),
             ("Chapita", "Colocarla: que el borde apoye en metal")]
    for k, (t, d) in enumerate(items):
        yy = 1.55 + k * 1.22
        s.anillo(7.55, yy + .12, .62, k + 1, "accent2", sz=18)
        s.caja(8.35, yy, 4.38, 1.12, [{"t": t, "b": True, "sz": 22, "c": "tx2", "despues": 4}, d], sz=18, nombre=t)
    return s


def lamina_conclusiones():
    s = Lamina(2, "Sergio", 35, "Resultados y cierre",
               "Cierro con tres ideas. El principio funciona: la tira arrastra la botella y la hoja la corta, que es lo que pedía la consigna, que la máquina funcione. "
               "El ancho lo fija la geometría del cabezal, no la habilidad de quien gira. Y el prototipo nos dejó mejoras concretas para la próxima versión. Muchas gracias. ¿Preguntas?")
    s.titulo("Conclusiones")
    items = [("El principio funciona", "La tira arrastra y la hoja corta"),
             ("El ancho lo fija la geometría", "No la habilidad de quien gira"),
             ("Mejoras concretas", "Manivela, anclaje, bajada y chapita")]
    for k, (t, d) in enumerate(items):
        y = 1.85 + k * 1.25
        s.caja(.7, y + .1, .7, .7, {"t": str(k + 1), "b": True, "c": "tx2", "algn": "ctr"}, sz=18, anchor="ctr", fondo="bg1", borde="accent2", borde_pt=3, geom="ellipse", nombre=f"Anillo {k + 1}")
        s.caja(1.7, y, 5.9, 1.0, [{"t": t, "b": True, "sz": 23, "c": "bg1"}, {"t": d, "sz": 17, "c": "bg2"}], anchor="ctr", nombre=t)
    s.caja(8.0, 1.85, 4.73, 3.55, [{"t": "FOTO PENDIENTE", "b": True, "sz": 22, "c": "accent2", "algn": "ctr", "despues": 6},
                                  {"t": "El grupo con la máquina", "sz": 16, "c": "bg2", "algn": "ctr"}],
           anchor="ctr", borde="accent2", borde_pt=2, guion="dash", nombre="Foto pendiente")
    s.caja(.7, 5.8, 11.9, .7, {"t": "Muchas gracias. ¿Preguntas?", "b": True, "c": "accent2", "fuente": "+mj-lt"}, sz=30, anchor="ctr", nombre="Cierre")
    return s


def lamina_bibliografia():
    s = Lamina(1, "Consulta", 0, "Consulta", "Lámina de consulta: no se expone. Queda disponible por si piden alguna referencia durante las preguntas.")
    s.titulo("Bibliografía")
    refs = [
        "Appropedia. (s. f.). 3D printed improved PET bottle stripper. https://www.appropedia.org/3D_printed_improved_PET_bottle_stripper",
        "Engineering ToolBox. (s. f.). Friction and friction coefficients. https://www.engineeringtoolbox.com/friction-coefficients-d_778.html",
        "Function 3D. (s. f.). PETALOT: PET bottle to 3D printer filament [Repositorio]. https://github.com/function3d/petalot",
        "Low-tech Lab. (s. f.). Découpeuse de bouteille plastique. https://wiki.lowtechlab.org/wiki/Découpeuse_de_bouteille_plastique/en",
        "Meraj, M., Ku, P. X., Choo, H. L., & Aung, P. P. (2024). Design and development of an automated PET plastic bottle 3D printer filament making machine. Journal of Physics: Conference Series, 2923(1), 012005. https://doi.org/10.1088/1742-6596/2923/1/012005",
        "OpenStax. (2016). University Physics Volume 1: 6.2 Friction; 12.3 Stress, strain, and elastic modulus. https://openstax.org/books/university-physics-volume-1",
        "Precious Plastic. (s. f.). PET filament from bottles. https://community.preciousplastic.com/library/pet-filament-from-bottles",
        "Tylman, I., & Dzierżek, K. (2020). Filament for a 3D printer from PET bottles — Simple machine. International Journal of Mechanical Engineering and Robotics Research, 9(10), 1386–1392. https://doi.org/10.18178/ijmerr.9.10.1386-1392",
    ]
    s.caja(.6, 1.45, 12.13, 4.6, [{"t": r, "despues": 4} for r in refs], sz=14, nombre="Referencias")
    s.caja(.6, 6.1, 11.0, .4, "Renders, planos y cálculos: elaboración propia con FreeCAD.", sz=12, c="accent6", anchor="ctr", nombre="Crédito de las imágenes")
    return s


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
    cuerpo = "".join(f'<Relationship Id="{r[0]}" Type="{r[1]}" Target="{escape(r[2], {chr(34): "&quot;"})}"'
                     + (' TargetMode="External"' if len(r) > 3 and r[3] else "") + "/>" for r in lista)
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

    for n, lam in enumerate(laminas, 1):
        if lam.layout == 1:
            lam.numero(n)
        partes[f"ppt/slides/slide{n}.xml"] = (
            XML + f'<p:sld {NS}><p:cSld><p:spTree>{GRUPO}{"".join(lam.formas)}</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>')
        lista = [("rId1", f"{REL}/slideLayout", f"../slideLayouts/slideLayout{lam.layout + 1}.xml")]
        lista += [(f"rId{i + 2}", t, d, ext) for i, (t, d, ext) in enumerate(lam.rels)]
        lista.append((f"rId{len(lista) + 1}", f"{REL}/notesSlide", f"../notesSlides/notesSlide{n}.xml"))
        partes[f"ppt/slides/_rels/slide{n}.xml.rels"] = rels(lista)
        partes[f"ppt/notesSlides/notesSlide{n}.xml"] = notas_xml(lam.notas)
        partes[f"ppt/notesSlides/_rels/notesSlide{n}.xml.rels"] = rels([
            ("rId1", f"{REL}/notesMaster", "../notesMasters/notesMaster1.xml"), ("rId2", f"{REL}/slide", f"../slides/slide{n}.xml")])
        tipos[f"/ppt/slides/slide{n}.xml"] = "application/vnd.openxmlformats-officedocument.presentationml.slide+xml"
        tipos[f"/ppt/notesSlides/notesSlide{n}.xml"] = "application/vnd.openxmlformats-officedocument.presentationml.notesSlide+xml"

    for ruta in MEDIOS:
        partes[f"ppt/media/{ruta.name}"] = ruta.read_bytes()

    # Secciones: una por bloque del relato (los oradores van en las notas)
    secciones, orden = {}, []
    for n, lam in enumerate(laminas):
        if lam.bloque not in secciones:
            secciones[lam.bloque] = []
            orden.append(lam.bloque)
        secciones[lam.bloque].append(256 + n)
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
        '<dc:title>Cortadora manual de botellas PET, modelo 2.0</dc:title><dc:subject>TP Final Ingeniería Mecánica I</dc:subject><dc:creator>Grupo 1, curso S1091</dc:creator>'
        '<dcterms:created xsi:type="dcterms:W3CDTF">2026-11-15T12:00:00Z</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">2026-11-15T12:00:00Z</dcterms:modified></cp:coreProperties>')
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




def a_pdf():
    """PDF de respaldo con LibreOffice, en un perfil temporal para no chocar con una sesión abierta."""
    with tempfile.TemporaryDirectory() as perfil:
        subprocess.run(["soffice", f"-env:UserInstallation=file://{perfil}", "--headless", "--convert-to", "pdf",
                        "--outdir", str(AQUI), str(SALIDA)], check=True, capture_output=True)
    return SALIDA.with_suffix(".pdf")


def main():
    fig = preparar_figuras()
    laminas = [lamina_portada(fig), lamina_problema(), lamina_objetivos(), lamina_antecedentes(),
               lamina_modelo_1(fig), lamina_principio(),
               lamina_cabezal(fig), lamina_cuentas(), lamina_modelo_3d(fig),
               lamina_impresion(fig), lamina_abastecimiento(), lamina_taller(fig),
               lamina_demo(), lamina_video(),
               lamina_respuestas(), lamina_mejoras(fig), lamina_conclusiones(), lamina_bibliografia()]
    transcurrido = 0
    for lam in laminas:
        if lam.segundos:
            ini, transcurrido = transcurrido, transcurrido + lam.segundos
            lam.notas = (f"{lam.orador.upper()} · {lam.segundos // 60}:{lam.segundos % 60:02d} min "
                         f"(del {ini // 60}:{ini % 60:02d} al {transcurrido // 60}:{transcurrido % 60:02d}). {lam.notas}")
    empaquetar(laminas)
    print(f"{SALIDA.name}: {len(laminas)} láminas, {transcurrido // 60}:{transcurrido % 60:02d} min asignados")
    if "--sin-pdf" not in sys.argv:
        print(f"{a_pdf().name}: listo")


if __name__ == "__main__":
    main()
