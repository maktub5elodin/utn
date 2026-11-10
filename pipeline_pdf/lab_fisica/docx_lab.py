#!/usr/bin/env python3
r"""Informe de laboratorio de Física en Word: lab.mk lo corre después de pandoc.

El .docx es la versión editable para trabajar con el grupo; tiene que verse lo
más parecido posible al PDF (que es la versión principal). Sin reference.docx
(binario): todo se arma acá, solo con la biblioteca estándar + PyYAML.

  - carátula de la U.D.B. Física con la misma estructura de tablas que el
    formulario oficial (carátula .docx), en su propia sección con los márgenes
    originales, y el logo UTN vectorial pasado a PNG (logo_utn_png.tex);
  - encabezado («Trabajo Práctico N°… — título | Física I — curso — grupo») y
    pie con número de página, desde la página 2;
  - estilos del TP5: Arial, títulos azul marino/azul, tablas con encabezado
    azul, pies grises, recuadro de resultado.

Uso:
  python3 docx_lab.py archivo.docx pdf.yaml logo.png   ajusta el .docx
  python3 docx_lab.py --nombre pdf.yaml                imprime el nombre de salida
                                                       (ej. A1193-TP5-G5)
"""
import re
import shutil
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

import yaml

AZUL, MARINO, GRIS, BORDE = "2E75B6", "1F3864", "676767", "AAAAAA"
R_NS = 'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
W_NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'


# ── Datos ────────────────────────────────────────────────────────────────

def datos(ruta_yaml):
    with open(ruta_yaml, encoding="utf-8") as f:
        d = (yaml.safe_load(f).get("metadata") or {}).get("laboratorio")
    if not d:
        sys.exit(f"docx_lab.py: falta el bloque metadata.laboratorio en {ruta_yaml}")
    d = {k: (str(v) if isinstance(v, (int, float)) else v) for k, v in d.items()}
    d.setdefault("materia", "Física I")
    d["grupo_txt"] = f"Grupo N°{d['grupo']}" if d.get("grupo") else "Individual"
    return d


def nombre_salida(d):
    """A1193-TP5-G5; si es individual, A1193-TP3-Apellido; `archivo:` lo pisa."""
    if d.get("archivo"):
        return str(d["archivo"])
    sufijo = f"G{d['grupo']}" if d.get("grupo") else d["integrantes"][0]["apellido"]
    return f"{d['curso']}-TP{d['tp']}-{sufijo}"


# ── Carátula (misma estructura que el formulario oficial) ────────────────

def formato(sz=32, negrita=True, subrayado=False):
    rpr = '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
    rpr += "<w:b/>" if negrita else ""
    rpr += f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>'
    rpr += '<w:u w:val="single"/>' if subrayado else ""
    return f'<w:rPr>{rpr}<w:lang w:val="es-AR"/></w:rPr>'


def parrafo(texto="", sz=32, negrita=True, centro=False, subrayado=False, extra=""):
    # La marca de párrafo lleva el mismo formato: un renglón vacío mide 16 pt,
    # igual que los separadores del formulario.
    jc = '<w:jc w:val="center"/>' if centro else ""
    rpr = formato(sz, negrita, subrayado)
    t = f'<w:r>{rpr}<w:t xml:space="preserve">{escape(texto)}</w:t></w:r>' if texto else ""
    return (f'<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/>'
            f'<w:ind w:left="0" w:right="0" w:firstLine="0"/>{jc}{rpr}</w:pPr>{extra}{t}</w:p>')


def celda(ancho, contenido, span=1, fondo=None, valign=None, bordes=None):
    pr = f'<w:tcW w:w="{ancho}" w:type="dxa"/>'
    pr += f'<w:gridSpan w:val="{span}"/>' if span > 1 else ""
    pr += f"<w:tcBorders>{bordes}</w:tcBorders>" if bordes else ""
    pr += f'<w:shd w:val="clear" w:color="auto" w:fill="{fondo}"/>' if fondo else ""
    pr += f'<w:vAlign w:val="{valign}"/>' if valign else ""
    return f"<w:tc><w:tcPr>{pr}</w:tcPr>{contenido}</w:tc>"


def tabla(ancho, columnas, filas, sangria=0):
    """filas: lista de (alto_twips o None, [celdas])."""
    bordes = "".join(f'<w:{b} w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
                     for b in ("top", "left", "bottom", "right", "insideH", "insideV"))
    pr = (f'<w:tblW w:w="{ancho}" w:type="dxa"/><w:jc w:val="left"/>'
          f'<w:tblInd w:w="{sangria}" w:type="dxa"/><w:tblBorders>{bordes}</w:tblBorders>'
          '<w:tblLayout w:type="fixed"/><w:tblCellMar><w:top w:w="0" w:type="dxa"/>'
          '<w:left w:w="108" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/>'
          '<w:right w:w="108" w:type="dxa"/></w:tblCellMar><w:tblLook w:val="0000"/>')
    grilla = "".join(f'<w:gridCol w:w="{c}"/>' for c in columnas)
    cuerpo = ""
    for alto, celdas in filas:
        trpr = f'<w:trPr><w:trHeight w:val="{alto}" w:hRule="atLeast"/></w:trPr>' if alto else ""
        cuerpo += f"<w:tr>{trpr}{''.join(celdas)}</w:tr>"
    return f"<w:tbl><w:tblPr>{pr}</w:tblPr><w:tblGrid>{grilla}</w:tblGrid>{cuerpo}</w:tbl>"


def logo_en_linea():
    # Logo en línea (no anclado): se mantiene en su lugar en Word, LibreOffice y
    # Google Docs. Proporciones del símbolo oficial (5 : 5,8963), 1,90 cm de alto.
    cy = 684000
    cx = round(cy * 5 / 5.8963)
    return (
        '<w:r><w:drawing><wp:inline xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
        f'distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{cx}" cy="{cy}"/>'
        '<wp:effectExtent l="0" t="0" r="0" b="0"/><wp:docPr id="9001" name="Logo UTN"/>'
        '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
        '<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        '<pic:nvPicPr><pic:cNvPr id="9001" name="logo_utn.png"/><pic:cNvPicPr/></pic:nvPicPr>'
        f'<pic:blipFill><a:blip {R_NS} r:embed="rIdLogoUTN"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
        f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
        '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic>'
        '</wp:inline></w:drawing></w:r>')


def tamano_linea(texto, sz=32, entran=60):
    """Achica la letra de una franja que no entra en un renglón (como el PDF):
    a 16 pt entran unos 60 caracteres de Times negrita en 15,6 cm."""
    return sz if len(texto) <= entran else max(20, int(sz * entran / len(texto)))


def caratula(d):
    ANCHO = 9060
    sep = parrafo()  # renglón vacío de 16 pt entre tablas, como el formulario
    x = []
    # Logo + recuadro gris: el logo va en una celda sin bordes (solo el borde
    # derecho, que es el izquierdo del recuadro), pegado al recuadro
    sin_borde = ('<w:top w:val="nil"/><w:left w:val="nil"/><w:bottom w:val="nil"/>'
                 '<w:right w:val="single" w:sz="4" w:space="0" w:color="000000"/>')
    logo = ('<w:p><w:pPr><w:spacing w:before="0" w:after="0"/><w:jc w:val="right"/></w:pPr>'
            f'{logo_en_linea()}</w:p>')
    gris = parrafo("LABORATORIO DE FÍSICA", centro=True) + parrafo()
    x.append(tabla(ANCHO, [2448, 6612], [(None, [
        celda(2448, logo, bordes=sin_borde),
        celda(6612, gris, fondo="E6E6E6")])]))
    x.append(sep)
    curso = re.sub(r"^([A-Za-z])(\d)", r"\1-\2", str(d["curso"]))
    x.append(tabla(6612, [3305, 3306], [(None, [
        celda(3305, parrafo(f"GRUPO N°{d.get('grupo') or '—'}")),
        celda(3306, parrafo(f"CURSO:{curso}"))])], sangria=2448))
    for texto in (f"PROFESOR: {d['profesor']}", f"JTP: {d['jtp']}",
                  "ATP: " + " ; ".join(d.get("atp") or []),
                  f"ASISTE LOS DÍAS: {d['dias']}", f"EN EL TURNO: {d['turno']}",
                  f"TRABAJO PRÁCTICO N°:{d['tp']}", f"TÍTULO: {d['titulo']}"):
        x.append(sep)
        x.append(tabla(ANCHO, [ANCHO], [(None, [celda(ANCHO, parrafo(texto, sz=tamano_linea(texto)))])]))
    # Integrantes presentes: dos columnas, mínimo 3 filas
    integ = [f"{i['nombre']} {i['apellido']}" for i in d["integrantes"]]
    nf = max(3, -(-len(integ) // 2))
    integ += [""] * (2 * nf - len(integ))
    filas = [(None, [celda(9059, parrafo("INTEGRANTES PRESENTES EL DÍA QUE SE REALIZÓ"), span=2)])]
    for f in range(nf):
        filas.append((None, [celda(4536, parrafo(integ[2 * f], negrita=False, centro=True)),
                             celda(4523, parrafo(integ[2 * f + 1], negrita=False, centro=True))]))
    x.append(sep)
    x.append(tabla(ANCHO, [4536, 4523], filas))
    # Fechas y firmas
    ch = dict(sz=22)
    filas = [(725, [celda(3025, parrafo("", **ch)),
                    celda(3006, parrafo("FECHAS", centro=True, **ch), valign="center"),
                    celda(3029, parrafo("FIRMA Y ACLARACIÓN DEL DOCENTE", centro=True, **ch), valign="center")])]
    for etiqueta, alto, fecha in (("REALIZADO EL", 331, d["fecha"]), ("CORREGIDO", 342, ""), ("APROBADO", 365, "")):
        filas.append((alto, [celda(3025, parrafo(etiqueta, **ch), valign="center"),
                             celda(3006, parrafo(str(fecha), negrita=False, centro=True, **ch), valign="center"),
                             celda(3029, parrafo("", **ch), valign="center")]))
    x.append(sep)
    x.append(tabla(ANCHO, [3025, 3006, 3029], filas))
    # Indicaciones para las correcciones (se achica si hay más filas de integrantes)
    alto = max(1000, 2490 - (nf - 3) * 390)  # 4,39 cm, igual que en el PDF
    x.append(sep)
    x.append(tabla(ANCHO, [ANCHO], [(alto, [celda(ANCHO, parrafo("INDICACIONES PARA LAS CORRECCIONES:", sz=22, subrayado=True))])]))
    # Fin de la sección de la carátula: márgenes del formulario, sin encabezado ni pie
    x.append('<w:p><w:pPr><w:spacing w:before="0" w:after="0"/><w:sectPr>'
             '<w:pgSz w:w="11906" w:h="16838"/>'
             '<w:pgMar w:top="1134" w:right="1418" w:bottom="1134" w:left="1418" '
             'w:header="0" w:footer="709" w:gutter="0"/></w:sectPr></w:pPr></w:p>')
    return "".join(x)


# ── Encabezado y pie ─────────────────────────────────────────────────────

def encabezado(d):
    izq = f"Trabajo Práctico N°{d['tp']} — {d['titulo']}"
    der = f"{d['materia']} — {d['curso']} — {d['grupo_txt']}"
    def r(t, color, negrita=False):
        b = "<w:b/>" if negrita else ""
        return (f'<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>{b}'
                f'<w:color w:val="{color}"/><w:sz w:val="16"/></w:rPr>'
                f'<w:t xml:space="preserve">{escape(t)}</w:t></w:r>')
    return (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:hdr {W_NS} {R_NS}>'
            f'<w:p><w:pPr><w:pBdr><w:bottom w:val="single" w:sz="6" w:space="4" w:color="{AZUL}"/></w:pBdr>'
            '<w:spacing w:before="0" w:after="0"/></w:pPr>'
            f'{r(izq, AZUL, True)}{r("   |   ", GRIS)}{r(der, GRIS)}</w:p></w:hdr>')


def pie():
    rpr = '<w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="18"/></w:rPr>'
    return (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:ftr {W_NS} {R_NS}>'
            f'<w:p><w:pPr><w:pBdr><w:top w:val="single" w:sz="6" w:space="4" w:color="{AZUL}"/></w:pBdr>'
            '<w:spacing w:before="0" w:after="0"/><w:jc w:val="right"/></w:pPr>'
            f'<w:r>{rpr}<w:fldChar w:fldCharType="begin"/></w:r>'
            f'<w:r>{rpr}<w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
            f'<w:r>{rpr}<w:fldChar w:fldCharType="separate"/></w:r>'
            f'<w:r>{rpr}<w:t>1</w:t></w:r>'
            f'<w:r>{rpr}<w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>')


SECCION_CUERPO = (
    '<w:sectPr><w:headerReference w:type="default" r:id="rIdLabEnc"/>'
    '<w:footerReference w:type="default" r:id="rIdLabPie"/>'
    '<w:pgSz w:w="11906" w:h="16838"/>'
    '<w:pgMar w:top="1304" w:right="1134" w:bottom="1304" w:left="1134" '
    'w:header="567" w:footer="567" w:gutter="0"/><w:pgNumType w:start="1"/></w:sectPr>')


ORDEN_RPR = ["rStyle", "rFonts", "b", "bCs", "i", "iCs", "caps", "smallCaps", "strike", "dstrike",
             "outline", "shadow", "emboss", "imprint", "noProof", "snapToGrid", "vanish", "webHidden",
             "color", "spacing", "w", "kern", "position", "sz", "szCs", "highlight", "u", "effect",
             "bdr", "shd", "fitText", "vertAlign", "rtl", "cs", "em", "lang", "eastAsianLayout",
             "specVanish", "oMath"]


def mezclar_rpr(interior, agregar):
    """Suma propiedades de corrida respetando el orden que exige Word."""
    piezas = {m.group(1): m.group(0) for m in re.finditer(r"<w:(\w+)\b[^>]*?(?:/>|>.*?</w:\1>)", interior, flags=re.S)}
    piezas.update(agregar)
    clave = lambda k: ORDEN_RPR.index(k) if k in ORDEN_RPR else len(ORDEN_RPR)
    return "".join(piezas[k] for k in sorted(piezas, key=clave))


def tabla_directa(tbl):
    """Formato del estilo «Table» escrito celda por celda: bordes grises,
    encabezado azul con texto blanco en negrita, texto de 9,5 pt centrado
    verticalmente. Así lo conservan Word, LibreOffice y Google Docs."""
    bordes = "".join(f'<w:{b} w:val="single" w:sz="4" w:space="0" w:color="{BORDE}"/>'
                     for b in ("top", "left", "bottom", "right", "insideH", "insideV"))
    tbl = tbl.replace('<w:jc w:val="center"/>',
                      f'<w:jc w:val="center"/><w:tblBorders>{bordes}</w:tblBorders>'
                      '<w:tblCellMar><w:top w:w="50" w:type="dxa"/><w:left w:w="100" w:type="dxa"/>'
                      '<w:bottom w:w="50" w:type="dxa"/><w:right w:w="100" w:type="dxa"/></w:tblCellMar>', 1)

    def fila(m):
        tr = m.group(0)
        cab = "<w:tblHeader" in tr
        shd = f'<w:shd w:val="clear" w:color="auto" w:fill="{AZUL}"/>' if cab else ""
        tr = re.sub(r"<w:tcPr\s*/>|<w:tcPr>(.*?)</w:tcPr>",
                    lambda c: f"<w:tcPr>{c.group(1) or ''}{shd}<w:vAlign w:val=\"center\"/></w:tcPr>", tr, flags=re.S)
        agregar = {"sz": '<w:sz w:val="19"/>', "szCs": '<w:szCs w:val="19"/>'}
        if cab:
            agregar.update({"b": "<w:b/>", "color": '<w:color w:val="FFFFFF"/>'})
        tr = re.sub(r"<w:r>(?:<w:rPr>(.*?)</w:rPr>)?",
                    lambda r: f"<w:r><w:rPr>{mezclar_rpr(r.group(1) or '', agregar)}</w:rPr>", tr, flags=re.S)
        if cab:  # fórmulas del encabezado en blanco
            tr = re.sub(r"(<m:r>(?:<m:rPr>.*?</m:rPr>)?)(?:<w:rPr>.*?</w:rPr>)?(<m:t\b)",
                        r'\1<w:rPr><w:b/><w:color w:val="FFFFFF"/></w:rPr>\2', tr, flags=re.S)
        return tr

    return re.sub(r"<w:tr\b.*?</w:tr>", fila, tbl, flags=re.S)


def documento(xml, d):
    xml = re.sub(r"<w:sectPr\b.*?</w:sectPr>", "", xml, flags=re.S)
    xml = xml.replace("</w:body>", SECCION_CUERPO + "</w:body>")
    # Tablas del cuerpo centradas, y su texto también salvo alineación explícita
    # de la columna (las tablas de la carátula se agregan después)
    xml = re.sub(r'(<w:tblW\b[^>]*/>)', r'\1<w:jc w:val="center"/>', xml)
    xml = re.sub(r"<w:tbl>.*?</w:tbl>", lambda m: tabla_directa(re.sub(
        r'(<w:pStyle w:val="Compact" ?/>)(?!<w:jc)', r'\1<w:jc w:val="center"/>', m[0])), xml, flags=re.S)
    return re.sub(r"(<w:body>)", lambda m: m[1] + caratula(d), xml, count=1)


# ── Estilos ──────────────────────────────────────────────────────────────

def estilo_parrafo(sid, nombre, ppr="", rpr="", base="Normal", siguiente=None):
    sig = f'<w:next w:val="{siguiente}"/>' if siguiente else ""
    return (f'<w:style w:type="paragraph" w:customStyle="1" w:styleId="{sid}"><w:name w:val="{nombre}"/>'
            f'<w:basedOn w:val="{base}"/>{sig}<w:qFormat/><w:pPr>{ppr}</w:pPr><w:rPr>{rpr}</w:rPr></w:style>')


def titulo(sid, nombre, sz, color, antes, despues, nivel):
    return (f'<w:style w:type="paragraph" w:styleId="{sid}"><w:name w:val="{nombre}"/>'
            '<w:basedOn w:val="Normal"/><w:next w:val="BodyText"/><w:uiPriority w:val="9"/><w:qFormat/>'
            f'<w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="{antes}" w:after="{despues}"/>'
            f'<w:outlineLvl w:val="{nivel}"/></w:pPr>'
            f'<w:rPr><w:b/><w:bCs/><w:color w:val="{color}"/><w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/></w:rPr></w:style>')


CUERPO_PPR = '<w:spacing w:before="0" w:after="100" w:line="264" w:lineRule="auto"/><w:jc w:val="both"/>'
CENTRO = '<w:jc w:val="center"/>'


def estilos_lab():
    bordes = "".join(f'<w:{b} w:val="single" w:sz="4" w:space="0" w:color="{BORDE}"/>'
                     for b in ("top", "left", "bottom", "right", "insideH", "insideV"))
    caja = "".join(f'<w:{b} w:val="single" w:sz="6" w:space="4" w:color="{AZUL}"/>'
                   for b in ("top", "left", "bottom", "right"))
    return {
        "BodyText": estilo_parrafo("BodyText", "Body Text", CUERPO_PPR),
        "FirstParagraph": estilo_parrafo("FirstParagraph", "First Paragraph", "", base="BodyText", siguiente="BodyText"),
        "Compact": estilo_parrafo("Compact", "Compact", '<w:spacing w:before="20" w:after="20"/>'),
        "Heading1": titulo("Heading1", "heading 1", 32, MARINO, 320, 120, 0),
        "Heading2": titulo("Heading2", "heading 2", 26, AZUL, 240, 80, 1),
        "Heading3": titulo("Heading3", "heading 3", 22, AZUL, 200, 40, 2),
        "TituloTP": estilo_parrafo("TituloTP", "Titulo TP", '<w:spacing w:before="200" w:after="80"/>' + CENTRO,
                                   f'<w:b/><w:color w:val="{MARINO}"/><w:sz w:val="44"/><w:szCs w:val="44"/>'),
        "SubtituloTP": estilo_parrafo("SubtituloTP", "Subtitulo TP", '<w:spacing w:before="0" w:after="200"/>' + CENTRO,
                                      f'<w:b/><w:color w:val="{AZUL}"/><w:sz w:val="32"/><w:szCs w:val="32"/>'),
        "DatosTP": estilo_parrafo("DatosTP", "Datos TP", '<w:spacing w:before="0" w:after="20"/>' + CENTRO,
                                  f'<w:color w:val="{GRIS}"/><w:sz w:val="21"/><w:szCs w:val="21"/>'),
        "IntegrantesTP": estilo_parrafo("IntegrantesTP", "Integrantes TP",
                                        '<w:keepNext/><w:spacing w:before="200" w:after="60"/>' + CENTRO,
                                        f'<w:b/><w:color w:val="{MARINO}"/><w:sz w:val="24"/><w:szCs w:val="24"/>'),
        "Piedetabla": estilo_parrafo("Piedetabla", "Pie de tabla", '<w:spacing w:before="40" w:after="160"/>' + CENTRO,
                                     f'<w:color w:val="{GRIS}"/><w:sz w:val="17"/><w:szCs w:val="17"/>'),
        "ImageCaption": estilo_parrafo("ImageCaption", "Image Caption", '<w:spacing w:before="40" w:after="160"/>' + CENTRO,
                                       f'<w:color w:val="{GRIS}"/><w:sz w:val="17"/><w:szCs w:val="17"/>'),
        "Resultado": estilo_parrafo("Resultado", "Resultado",
                                    f'<w:pBdr>{caja}</w:pBdr><w:spacing w:before="160" w:after="160"/>'
                                    '<w:ind w:left="100" w:right="100"/>' + CENTRO),
        "Table": ('<w:style w:type="table" w:default="1" w:styleId="Table"><w:name w:val="Table"/>'
                  '<w:basedOn w:val="TableNormal"/><w:pPr>' + CENTRO + '</w:pPr>'
                  '<w:rPr><w:sz w:val="19"/><w:szCs w:val="19"/></w:rPr>'
                  f'<w:tblPr><w:tblBorders>{bordes}</w:tblBorders><w:tblCellMar>'
                  '<w:top w:w="50" w:type="dxa"/><w:left w:w="100" w:type="dxa"/>'
                  '<w:bottom w:w="50" w:type="dxa"/><w:right w:w="100" w:type="dxa"/></w:tblCellMar></w:tblPr>'
                  '<w:tcPr><w:vAlign w:val="center"/></w:tcPr>'
                  '<w:tblStylePr w:type="firstRow"><w:rPr><w:b/><w:color w:val="FFFFFF"/></w:rPr>'
                  f'<w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="{AZUL}"/></w:tcPr></w:tblStylePr></w:style>'),
    }


def estilos(xml):
    # Fuente y tamaño base: Arial 10 pt (en Linux, LibreOffice usa Liberation Sans, misma métrica)
    xml = re.sub(r"<w:rPrDefault>.*?</w:rPrDefault>",
                 '<w:rPrDefault><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:eastAsia="Arial" w:cs="Arial"/>'
                 '<w:sz w:val="20"/><w:szCs w:val="20"/><w:lang w:val="es-AR" w:eastAsia="en-US" w:bidi="ar-SA"/>'
                 '</w:rPr></w:rPrDefault>', xml, count=1, flags=re.S)
    for sid, definicion in estilos_lab().items():
        xml, n = re.subn(rf'<w:style\b[^>]*w:styleId="{sid}".*?</w:style>', lambda m: definicion, xml, flags=re.S)
        if not n:
            xml = xml.replace("</w:styles>", definicion + "</w:styles>")
    return xml


# ── Paquete .docx ────────────────────────────────────────────────────────

def relaciones(xml):
    extra = (
        '<Relationship Id="rIdLabEnc" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header_lab.xml"/>'
        '<Relationship Id="rIdLabPie" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer_lab.xml"/>'
        '<Relationship Id="rIdLogoUTN" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/logo_utn.png"/>')
    return xml.replace("</Relationships>", extra + "</Relationships>")


def tipos(xml):
    if 'Extension="png"' not in xml:
        xml = xml.replace("<Override", '<Default Extension="png" ContentType="image/png"/><Override', 1)
    extra = (
        '<Override PartName="/word/header_lab.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>'
        '<Override PartName="/word/footer_lab.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>')
    return xml.replace("</Types>", extra + "</Types>")


def main(ruta, ruta_yaml, logo):
    d = datos(ruta_yaml)
    ruta = Path(ruta)
    tmp = ruta.with_suffix(".tmp")
    cambios = {"word/document.xml": lambda x: documento(x, d), "word/styles.xml": estilos,
               "word/_rels/document.xml.rels": relaciones, "[Content_Types].xml": tipos}
    with zipfile.ZipFile(ruta) as ent, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as sal:
        for item in ent.infolist():
            datos_item = ent.read(item.filename)
            if item.filename in cambios:
                datos_item = cambios[item.filename](datos_item.decode("utf-8")).encode("utf-8")
            sal.writestr(item, datos_item)
        sal.writestr("word/header_lab.xml", encabezado(d))
        sal.writestr("word/footer_lab.xml", pie())
        sal.write(logo, "word/media/logo_utn.png")
    shutil.move(tmp, ruta)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--nombre":
        print(nombre_salida(datos(sys.argv[2])))
    elif len(sys.argv) == 4:
        main(*sys.argv[1:])
    else:
        sys.exit(__doc__)
