#!/usr/bin/env python3
r"""TP Final de Ingeniería Mecánica I en Word: carátula oficial y armado final.

El .docx es la versión editable para compartir con el grupo (y subir a Google
Docs); el PDF es el principal. tp.mk lo usa en tres pasos:

  python3 docx_tp.py --nombre pdf.yaml e3
      imprime el nombre de salida de la versión (tp.versiones.e3.archivo)

  python3 docx_tp.py caratula pdf.yaml e3 informe.md salida.docx
      completa la carátula OFICIAL de la cátedra (tp.caratula) con python-docx:
      reemplaza los marcadores rojos (grupo, curso, entrega, revisión, título),
      agrega profesor, ATP y alumnos, pasa la hoja a A4 y, si la versión lo
      pide (resumen: true), copia el abstract del .md en el campo «Resumen».
      La misma carátula, pasada a PDF con LibreOffice, es la página 1 del PDF.

  python3 docx_tp.py armar documento.docx pdf.yaml e3 caratula.docx
      ajusta el .docx de pandoc:
        - estilos: Times New Roman 12, justificado, interlineado 1,15, A4;
          alineación e interlineado escritos también en cada párrafo, y el
          formato de las tablas celda por celda (Google Docs ignora parte de
          los estilos);
        - la carátula completada, como primera sección, con sus márgenes, su
          logo, sus estilos (renombrados, para que no entren al índice) y su pie;
        - pie «Ing. Mecánica - Grupo … - Curso … - Año …» + número de página;
        - secciones apaisadas para las láminas (marcadas por tp-mecanica.lua);
        - índice como campo TOC real con las entradas y los números de página
          ya cargados (paginado con LibreOffice), para que no aparezca vacío.
"""
import copy
import io
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml
from lxml import etree
from docx import Document
from docx.opc.constants import CONTENT_TYPE as CT
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import parse_xml
from docx.oxml.ns import qn
from docx.parts.hdrftr import FooterPart
from docx.shared import Twips

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = f'xmlns:w="{W_NS}" xmlns:r="{R_NS}"'
TNR = "Times New Roman"
A4 = (11906, 16838)
ANCHO_TEXTO = 11906 - 2 * 1418          # 2,5 cm por lado
MARCA_VERTICAL = "00B2B2B2"              # sectPr que pone tp-mecanica.lua
MARCA_APAISADA = "00A1A1A1"


# ── Datos ────────────────────────────────────────────────────────────────

def datos(ruta_yaml, version):
    with open(ruta_yaml, encoding="utf-8") as f:
        tp = (yaml.safe_load(f).get("metadata") or {}).get("tp")
    if not tp:
        sys.exit(f"docx_tp.py: falta el bloque metadata.tp en {ruta_yaml}")
    v = (tp.get("versiones") or {}).get(version)
    if not v:
        sys.exit(f"docx_tp.py: falta tp.versiones.{version} en {ruta_yaml}")
    tp["v"] = v
    tp["base"] = Path(ruta_yaml).resolve().parent
    return tp


# ── Abstract del .md (para el campo «Resumen» de la carátula) ───────────

def _texto(inlines):
    out = []
    for x in inlines:
        t, c = x["t"], x.get("c")
        if t == "Str":
            out.append(c)
        elif t in ("Space", "SoftBreak", "LineBreak"):
            out.append(" ")
        elif t in ("Emph", "Strong", "Underline", "Strikeout", "Superscript", "Subscript", "SmallCaps"):
            out.append(_texto(c))
        elif t in ("Span", "Link"):
            out.append(_texto(c[1]))
        elif t == "Quoted":
            out.append("«" + _texto(c[1]) + "»")
        elif t == "Math":
            out.append(c[1])
        elif t == "Code":
            out.append(c[1])
        elif t == "Cite":
            out.append(_texto(c[1]))
    return "".join(out)


def abstract(md):
    ast = json.loads(subprocess.run(["pandoc", "-f", "markdown", "-t", "json", md],
                                    check=True, capture_output=True, text=True).stdout)

    def plano(blocks):
        for b in blocks:
            if b["t"] == "Div":
                yield from plano(b["c"][1])
            else:
                yield b

    parrafos, dentro = [], False
    for b in plano(ast["blocks"]):
        if b["t"] == "Header":
            dentro = _texto(b["c"][2]).strip().lower() == "abstract"
        elif dentro and b["t"] == "Para":
            parrafos.append(re.sub(r"\s+", " ", _texto(b["c"])).strip())
    if not parrafos:
        sys.exit("docx_tp.py: no se encontró la sección «Abstract» en " + md)
    return parrafos


# ── Carátula oficial completada ──────────────────────────────────────────

def _txt(elem):
    """Texto de un párrafo (los w:t; itertext() de python-docx lo repite)."""
    return "".join(t.text or "" for t in elem.iter(qn("w:t")))


def _rojo(run):
    c = run._r.find(qn("w:rPr") + "/" + qn("w:color"))
    return c is not None and c.get(qn("w:val"), "").lower() == "ff0000"


def _sin_color(run):
    rpr = run._r.find(qn("w:rPr"))
    if rpr is not None:
        for c in rpr.findall(qn("w:color")):
            rpr.remove(c)


def _parrafo_tnr(texto, sz, ind_izq=0, colgante=0, ind_der=0, jc="left", negrita=False, despues=0):
    rpr = (f'<w:rPr><w:rFonts w:ascii="{TNR}" w:hAnsi="{TNR}" w:cs="{TNR}" w:eastAsia="{TNR}"/>'
           f'{"<w:b/>" if negrita else ""}<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/></w:rPr>')
    t = texto.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    run = f'<w:r>{rpr}<w:t xml:space="preserve">{t}</w:t></w:r>' if texto else ""
    return parse_xml(
        f'<w:p {NS}><w:pPr><w:spacing w:before="0" w:after="{despues}" w:line="240" w:lineRule="auto"/>'
        f'<w:ind w:left="{ind_izq}" w:right="{ind_der}" w:hanging="{colgante}"/><w:jc w:val="{jc}"/>{rpr}</w:pPr>'
        f'{run}</w:p>')


def caratula(ruta_yaml, version, md, salida):
    tp = datos(ruta_yaml, version)
    v = tp["v"]
    doc = Document(tp["base"] / tp["caratula"])
    curso = str(tp["curso"])
    grupo = str(tp["grupo"])

    # Línea GRUPO XX - CURSO S109X - ENTREGA N°X - REVISIÓN N°X: los marcadores
    # rojos, en orden; el tabulador antes de «- REVISIÓN» se quita.
    reemplazos = [grupo, curso[-1] + " ", str(v["entrega"]), str(v["revision"])]
    hechos = {"linea": False, "titulo": False, "profesor": False, "atp": False}
    for p in doc.paragraphs:
        texto = p.text
        if texto.startswith("GRUPO "):
            rojos = [r for r in p.runs if _rojo(r)]
            if len(rojos) != len(reemplazos):
                sys.exit("docx_tp.py: la línea GRUPO/CURSO/ENTREGA de la carátula cambió de formato")
            for r, nuevo in zip(rojos, reemplazos):
                r.text = nuevo
                _sin_color(r)
            for tab in p._p.iter(qn("w:tab")):
                if tab.getparent().tag == qn("w:r"):
                    tab.getparent().remove(tab)
            hechos["linea"] = True
        elif "(Reemplazar por el título)" in texto:
            for r in p.runs:
                if "(Reemplazar" in r.text:
                    r.text = tp["titulo"]
                _sin_color(r)
            # En A4 (más angosta que Carta) el título no entra en un renglón con
            # la sangría izquierda del formulario: se quita esa sangría
            ind = p._p.find(qn("w:pPr") + "/" + qn("w:ind"))
            if ind is not None:
                ind.set(qn("w:left"), "0")
            hechos["titulo"] = True
        elif texto.strip() in ("Profesor:", "ATP:"):
            clave = "profesor" if texto.strip() == "Profesor:" else "atp"
            p.runs[-1].text = texto.strip() + " "
            # nombre en redonda (el renglón tiene estilo de título, en negrita)
            r = _parrafo_tnr(tp[clave], 24).find(qn("w:r"))
            r.find(qn("w:rPr")).insert(1, parse_xml(f'<w:b {NS} w:val="0"/>'))
            r.find(qn("w:rPr")).insert(2, parse_xml(f'<w:bCs {NS} w:val="0"/>'))
            p._p.append(r)
            hechos[clave] = True
    faltan = [k for k, ok in hechos.items() if not ok]
    if faltan:
        sys.exit("docx_tp.py: no se encontraron en la carátula: " + ", ".join(faltan))

    # Alumnos: reemplazan los renglones vacíos entre «Alumnos:» y «Resumen:»
    ps = doc.paragraphs
    i_al = next(i for i, p in enumerate(ps) if p.text.strip() == "Alumnos:")
    i_re = next(i for i, p in enumerate(ps) if p.text.strip() == "Resumen:")
    for p in ps[i_al + 1:i_re]:
        if p.text.strip():
            sys.exit("docx_tp.py: texto inesperado entre «Alumnos:» y «Resumen:»")
        p._p.getparent().remove(p._p)
    ancla = ps[i_al]._p
    nuevos = [_parrafo_tnr(f"•  {a['nombre']} — Legajo: {a['legajo']}", 24,
                           ind_izq=1733, colgante=360) for a in tp["alumnos"]]
    nuevos.append(_parrafo_tnr("", 12))
    for n in reversed(nuevos):
        ancla.addnext(n)

    # Resumen: el abstract (solo si la versión lo pide); si no, queda el rótulo solo
    ps = doc.paragraphs
    i_re = next(i for i, p in enumerate(ps) if p.text.strip() == "Resumen:")
    vacio = ps[i_re + 1]._p if i_re + 1 < len(ps) else None
    if v.get("resumen"):
        ancla = ps[i_re]._p
        for k, t in enumerate(reversed(abstract(md))):
            ancla.addnext(_parrafo_tnr(t, int(tp.get("resumen_sz", 20)), ind_izq=1373, ind_der=346,
                                       jc="both", despues=60))
        if vacio is not None and not _txt(vacio).strip():
            vacio.getparent().remove(vacio)

    # Pie de la carátula (pie de primera página del formulario)
    # El campo de número de página pegado a «2026» se quita (la carátula del
    # informe anterior no mostraba número) y la sangría izquierda también: en A4
    # el texto no entraba en un renglón.
    sec = doc.sections[0]
    for p in sec.first_page_footer.paragraphs:
        rojos = [r for r in p.runs if _rojo(r)]
        for r, nuevo in zip(rojos, [grupo, curso[-1]]):
            r.text = nuevo
            _sin_color(r)
        for instr in list(p._p.iter(qn("w:instrText"))):
            if instr.text and instr.text.strip() == "PAGE":
                corrida = instr.getparent()
                corrida.getparent().remove(corrida)
        ind = p._p.find(qn("w:pPr") + "/" + qn("w:ind"))
        if ind is not None:
            ind.set(qn("w:left"), "0")
            ind.set(qn("w:firstLine"), "0")

    # En el formulario, todo lo rojo es marcador: ya completado, también se quita
    # el rojo de las marcas de párrafo (si no, lo que se escriba ahí sale rojo)
    for parte in (doc.element, sec.first_page_footer._element):
        for c in list(parte.iter(qn("w:color"))):
            if c.get(qn("w:val"), "").lower() == "ff0000":
                c.getparent().remove(c)

    # A4, como todo el documento
    sec.page_width, sec.page_height = Twips(A4[0]), Twips(A4[1])

    # Nada en rojo ni marcadores sin completar
    xml = doc.element.xml + "".join(p.part.element.xml for p in [sec.first_page_footer])
    if re.search(r'w:color w:val="[Ff][Ff]0000"', xml) or "XX" in xml or "Reemplazar" in xml:
        sys.exit("docx_tp.py: quedaron marcadores rojos sin completar en la carátula")
    doc.core_properties.title = tp["titulo"]
    Path(salida).parent.mkdir(parents=True, exist_ok=True)
    doc.save(salida)


# ── Estilos ──────────────────────────────────────────────────────────────

def _rpr(sz=24, negrita=False, cursiva=False, color=None):
    s = f'<w:rFonts w:ascii="{TNR}" w:hAnsi="{TNR}" w:eastAsia="{TNR}" w:cs="{TNR}"/>'
    s += "<w:b/><w:bCs/>" if negrita else ""
    s += "<w:i/><w:iCs/>" if cursiva else ""
    s += f'<w:color w:val="{color}"/>' if color else ""
    return s + f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>'


CUERPO = '<w:spacing w:before="0" w:after="120" w:line="276" w:lineRule="auto"/><w:jc w:val="both"/>'
NOTA = '<w:spacing w:before="0" w:after="40" w:line="240" w:lineRule="auto"/><w:jc w:val="both"/>'
CENTRO = '<w:spacing w:before="60" w:after="160" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/>'
BIBLIO = ('<w:spacing w:before="0" w:after="80" w:line="276" w:lineRule="auto"/>'
          '<w:ind w:left="720" w:hanging="720"/><w:jc w:val="both"/>')
LISTA = '<w:spacing w:before="0" w:after="60" w:line="276" w:lineRule="auto"/><w:jc w:val="both"/>'

# estilo -> (pPr, rPr). Los de cuerpo llevan además el pPr escrito en cada párrafo.
ESTILOS = {
    "Normal": ("", _rpr()),
    "BodyText": (CUERPO, ""),
    "FirstParagraph": (CUERPO, ""),
    "Compact": ('<w:spacing w:before="20" w:after="20" w:line="240" w:lineRule="auto"/>', ""),
    "Heading1": ('<w:keepNext/><w:keepLines/><w:spacing w:before="360" w:after="120" w:line="276" w:lineRule="auto"/>'
                 '<w:jc w:val="left"/><w:outlineLvl w:val="0"/>', _rpr(28, negrita=True)),
    "Heading2": ('<w:keepNext/><w:keepLines/><w:spacing w:before="240" w:after="80" w:line="276" w:lineRule="auto"/>'
                 '<w:jc w:val="left"/><w:outlineLvl w:val="1"/>', _rpr(24, negrita=True)),
    "Heading3": ('<w:keepNext/><w:keepLines/><w:spacing w:before="200" w:after="40" w:line="276" w:lineRule="auto"/>'
                 '<w:jc w:val="left"/><w:outlineLvl w:val="2"/>', _rpr(24, negrita=True, cursiva=True)),
    "TituloTP": ('<w:spacing w:before="0" w:after="240"/><w:jc w:val="center"/>', _rpr(32, negrita=True)),
    "Indicetitulo": ('<w:spacing w:before="120" w:after="120"/><w:jc w:val="left"/>', _rpr(28, negrita=True)),
    "TOC1": ('<w:spacing w:before="60" w:after="0" w:line="276" w:lineRule="auto"/>', _rpr()),
    "TOC2": ('<w:spacing w:before="0" w:after="0" w:line="276" w:lineRule="auto"/><w:ind w:left="240"/>', _rpr()),
    "FootnoteText": (NOTA, _rpr(20)),
    "FootnoteReference": ("", '<w:vertAlign w:val="superscript"/>'),
    "ImageCaption": (CENTRO, _rpr(22)),
    "TableCaption": ('<w:keepNext/>' + CENTRO, _rpr(22)),
    "CaptionedFigure": ('<w:keepNext/><w:spacing w:before="120" w:after="0"/><w:jc w:val="center"/>', ""),
    "Figure": ('<w:keepNext/><w:spacing w:before="120" w:after="0"/><w:jc w:val="center"/>', ""),
    "Lamina": ('<w:spacing w:before="0" w:after="0"/><w:jc w:val="center"/>', ""),
    "Piedelamina": ('<w:spacing w:before="60" w:after="0"/><w:jc w:val="center"/>', _rpr(22)),
    "Bibliografia": (BIBLIO, ""),
    "Hyperlink": ("", '<w:color w:val="0563C1"/><w:u w:val="single"/>'),
}
NOMBRES = {"Normal": "Normal", "BodyText": "Body Text", "FirstParagraph": "First Paragraph",
           "Compact": "Compact", "Heading1": "heading 1", "Heading2": "heading 2", "Heading3": "heading 3",
           "TituloTP": "Titulo TP", "Indicetitulo": "Indice titulo", "TOC1": "toc 1", "TOC2": "toc 2",
           "FootnoteText": "footnote text", "FootnoteReference": "footnote reference",
           "ImageCaption": "Image Caption", "TableCaption": "Table Caption",
           "CaptionedFigure": "Captioned Figure", "Figure": "Figure", "Lamina": "Lamina",
           "Piedelamina": "Pie de lamina", "Bibliografia": "Bibliografia", "Hyperlink": "Hyperlink"}
# pPr que se escribe en cada párrafo de estos estilos (Google Docs)
DIRECTO = {"BodyText": CUERPO, "FirstParagraph": CUERPO, "Bibliografia": BIBLIO, "": CUERPO,
           "Compact": LISTA, "ImageCaption": CENTRO, "TableCaption": CENTRO}


def estilos(doc):
    st = doc.styles.element
    defaults = st.find(qn("w:docDefaults"))
    if defaults is not None:
        st.remove(defaults)
    st.insert(0, parse_xml(
        f'<w:docDefaults {NS}><w:rPrDefault><w:rPr>{_rpr()}<w:lang w:val="es-AR" w:eastAsia="en-US" w:bidi="ar-SA"/>'
        '</w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/>'
        '</w:pPr></w:pPrDefault></w:docDefaults>'))
    for sid, (ppr, rpr) in ESTILOS.items():
        tipo = "character" if sid in ("FootnoteReference", "Hyperlink") else "paragraph"
        viejo = st.find(f'{qn("w:style")}[@{qn("w:styleId")}="{sid}"]')
        base = "" if sid == "Normal" or tipo == "character" else '<w:basedOn w:val="Normal"/>'
        if sid in ("FirstParagraph",):
            base = '<w:basedOn w:val="BodyText"/>'
        sig = '<w:next w:val="BodyText"/>' if sid.startswith("Heading") else ""
        nuevo = parse_xml(
            f'<w:style {NS} w:type="{tipo}" w:styleId="{sid}"{" w:default=\"1\"" if sid == "Normal" else ""}>'
            f'<w:name w:val="{NOMBRES[sid]}"/>{base}{sig}<w:qFormat/>'
            + (f"<w:pPr>{ppr}</w:pPr>" if tipo == "paragraph" else "")
            + f"<w:rPr>{rpr}</w:rPr></w:style>")
        if viejo is not None:
            viejo.addprevious(nuevo)
            st.remove(viejo)
        else:
            st.append(nuevo)
    # Fuentes de tema (Calibri/Cambria) fuera de cualquier otro estilo de pandoc
    for rf in st.iter(qn("w:rFonts")):
        for a in ("asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme"):
            rf.attrib.pop(qn("w:" + a), None)
        for a in ("ascii", "hAnsi", "eastAsia", "cs"):
            rf.set(qn("w:" + a), TNR)
    for c in st.iter(qn("w:color")):
        if c.getparent().getparent().get(qn("w:styleId")) not in ("Hyperlink",):
            c.set(qn("w:val"), "000000")
            for a in ("themeColor", "themeShade", "themeTint"):
                c.attrib.pop(qn("w:" + a), None)


def _poner_ppr(p, ppr_xml):
    """Escribe en el párrafo las propiedades dadas (alineación, interlineado,
    sangría), conservando su estilo y su sectPr."""
    ppr = p.find(qn("w:pPr"))
    if ppr is None:
        ppr = parse_xml(f"<w:pPr {NS}/>")
        p.insert(0, ppr)
    nuevos = parse_xml(f"<w:pPr {NS}>{ppr_xml}</w:pPr>")
    for hijo in list(nuevos):
        for viejo in ppr.findall(hijo.tag):
            ppr.remove(viejo)
    # Orden del esquema: pStyle, keepNext, keepLines, ..., spacing, ind, jc, ..., rPr, sectPr
    orden = ["pStyle", "keepNext", "keepLines", "pageBreakBefore", "widowControl", "numPr", "pBdr",
             "shd", "tabs", "spacing", "ind", "jc", "outlineLvl", "rPr", "sectPr"]
    todos = list(ppr) + list(nuevos)
    for x in list(ppr):
        ppr.remove(x)
    clave = lambda e: orden.index(e.tag.split("}")[1]) if e.tag.split("}")[1] in orden else 10
    for x in sorted(todos, key=clave):
        ppr.append(x)


def parrafos_directos(doc, notas_xml):
    body = doc.element.body
    for p in body.iter(qn("w:p")):
        if p.getparent().tag == qn("w:tc") or any(a.tag == qn("w:tc") for a in p.iterancestors()):
            continue
        ps = p.find(qn("w:pPr") + "/" + qn("w:pStyle"))
        sid = ps.get(qn("w:val")) if ps is not None else ""
        if sid in DIRECTO and (sid or _txt(p).strip()):
            if sid == "" and p.find(".//" + qn("w:drawing")) is not None:
                continue
            _poner_ppr(p, DIRECTO[sid])
    if notas_xml is not None:
        for p in notas_xml.iter(qn("w:p")):
            _poner_ppr(p, NOTA)


def tablas(doc):
    bordes = "".join(f'<w:{b} w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
                     for b in ("top", "left", "bottom", "right", "insideH", "insideV"))
    for tbl in doc.element.body.iter(qn("w:tbl")):
        tblpr = tbl.find(qn("w:tblPr"))
        for tag in ("w:tblBorders", "w:jc", "w:tblCellMar", "w:tblStyle"):
            for x in tblpr.findall(qn(tag)):
                tblpr.remove(x)
        tblpr.append(parse_xml(f'<w:jc {NS} w:val="center"/>'))
        tblpr.append(parse_xml(f"<w:tblBorders {NS}>{bordes}</w:tblBorders>"))
        tblpr.append(parse_xml(f'<w:tblCellMar {NS}><w:top w:w="40" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
                               '<w:bottom w:w="40" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar>'))
        for k, tr in enumerate(tbl.findall(qn("w:tr"))):
            cab = tr.find(qn("w:trPr") + "/" + qn("w:tblHeader")) is not None
            for tc in tr.findall(qn("w:tc")):
                tcpr = tc.find(qn("w:tcPr"))
                if tcpr is None:
                    tcpr = parse_xml(f"<w:tcPr {NS}/>")
                    tc.insert(0, tcpr)
                for x in tcpr.findall(qn("w:vAlign")):
                    tcpr.remove(x)
                tcpr.append(parse_xml(f'<w:vAlign {NS} w:val="center"/>'))
                for p in tc.iter(qn("w:p")):
                    _poner_ppr(p, '<w:spacing w:before="20" w:after="20" w:line="240" w:lineRule="auto"/>')
                    for r in p.iter(qn("w:r")):
                        rpr = r.find(qn("w:rPr"))
                        if rpr is None:
                            rpr = parse_xml(f"<w:rPr {NS}/>")
                            r.insert(0, rpr)
                        for tag in ("w:rFonts", "w:sz", "w:szCs"):
                            for x in rpr.findall(qn(tag)):
                                rpr.remove(x)
                        rpr.insert(0, parse_xml(f'<w:rFonts {NS} w:ascii="{TNR}" w:hAnsi="{TNR}" w:cs="{TNR}"/>'))
                        rpr.append(parse_xml(f'<w:sz {NS} w:val="22"/>'))
                        rpr.append(parse_xml(f'<w:szCs {NS} w:val="22"/>'))
                        if cab and rpr.find(qn("w:b")) is None:
                            rpr.insert(1, parse_xml(f"<w:b {NS}/>"))


# ── Secciones, pie y carátula ────────────────────────────────────────────

def pie(tp):
    texto = tp["pie"].replace("&", "&amp;")
    rpr = f'<w:rPr><w:rFonts w:ascii="{TNR}" w:hAnsi="{TNR}" w:cs="{TNR}"/><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr>'
    rpri = rpr.replace("<w:sz ", "<w:i/><w:sz ")
    return (f'<w:ftr {NS}><w:p><w:pPr><w:tabs><w:tab w:val="right" w:pos="{ANCHO_TEXTO}"/></w:tabs>'
            f'<w:spacing w:before="0" w:after="0"/></w:pPr>'
            f'<w:r>{rpri}<w:t xml:space="preserve">{texto}</w:t></w:r><w:r>{rpr}<w:tab/></w:r>'
            f'<w:r>{rpr}<w:fldChar w:fldCharType="begin"/></w:r>'
            f'<w:r>{rpr}<w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
            f'<w:r>{rpr}<w:fldChar w:fldCharType="separate"/></w:r>'
            f'<w:r>{rpr}<w:t>2</w:t></w:r><w:r>{rpr}<w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>')


def pie_apaisado(tp):
    return pie(tp).replace(f'w:pos="{ANCHO_TEXTO}"', 'w:pos="15704"')


def nueva_parte_pie(doc, xml):
    paquete = doc.part.package
    nombre = paquete.next_partname("/word/footer%d.xml")
    parte = FooterPart(nombre, CT.WML_FOOTER, parse_xml(xml), paquete)
    return doc.part.relate_to(parte, RT.FOOTER)


def sect_vertical(rid):
    return parse_xml(
        f'<w:sectPr {NS}><w:footerReference w:type="default" r:id="{rid}"/>'
        f'<w:pgSz w:w="{A4[0]}" w:h="{A4[1]}"/>'
        '<w:pgMar w:top="1418" w:right="1418" w:bottom="1418" w:left="1418" w:header="709" w:footer="567" w:gutter="0"/>'
        "</w:sectPr>")


def sect_apaisada(rid):
    return parse_xml(
        f'<w:sectPr {NS}><w:footerReference w:type="default" r:id="{rid}"/>'
        f'<w:pgSz w:w="{A4[1]}" w:h="{A4[0]}" w:orient="landscape"/>'
        '<w:pgMar w:top="567" w:right="567" w:bottom="680" w:left="567" w:header="284" w:footer="284" w:gutter="0"/>'
        "</w:sectPr>")


def _limpiar_ids(elem):
    for e in elem.iter():
        for a in list(e.attrib):
            if "}" in a and (a.split("}")[1] in ("paraId", "textId") or a.split("}")[1].startswith("rsid")):
                del e.attrib[a]


def insertar_caratula(doc, ruta_car):
    car = Document(ruta_car)
    body = doc.element.body
    # Estilos de la carátula (Title y Heading1 del formulario), renombrados
    renombre = {"Title": "CaratulaTitle", "Heading1": "CaratulaHeading1"}
    st_car = car.styles.element
    for viejo, nuevo in renombre.items():
        e = copy.deepcopy(st_car.find(f'{qn("w:style")}[@{qn("w:styleId")}="{viejo}"]'))
        e.set(qn("w:styleId"), nuevo)
        e.find(qn("w:name")).set(qn("w:val"), "Carátula " + viejo.lower())
        for x in e.findall(qn("w:next")):
            e.remove(x)
        doc.styles.element.append(e)
    # Logo: misma imagen, relación nueva
    mapa = {}
    for rid, parte in car.part.related_parts.items():
        if parte.partname.endswith((".jpg", ".jpeg", ".png")):
            nuevo, _ = doc.part.get_or_add_image(io.BytesIO(parte.blob))
            mapa[rid] = nuevo
    # Pie de primera página de la carátula, completado
    sec = car.sections[0]
    rid_pie = nueva_parte_pie(doc, sec.first_page_footer._element.xml)
    rid_vacio = nueva_parte_pie(doc, f'<w:ftr {NS}><w:p/></w:ftr>')
    # Párrafos de la carátula, en orden, antes de todo
    bloques = [copy.deepcopy(e) for e in car.element.body if e.tag != qn("w:sectPr")]
    primero = body[0]
    for e in bloques:
        _limpiar_ids(e)
        for ps in e.iter(qn("w:pStyle")):
            ps.set(qn("w:val"), renombre.get(ps.get(qn("w:val")), ps.get(qn("w:val"))))
        for blip in e.iter("{http://schemas.openxmlformats.org/drawingml/2006/main}blip"):
            blip.set(qn("r:embed"), mapa[blip.get(qn("r:embed"))])
        primero.addprevious(e)
    # Sección de la carátula: márgenes del formulario, A4, pie de primera página
    pm = car.sections[0]._sectPr.find(qn("w:pgMar"))
    margenes = " ".join(f'w:{a}="{pm.get(qn("w:" + a))}"' for a in ("top", "right", "bottom", "left", "header", "footer"))
    sect = parse_xml(
        f'<w:sectPr {NS}><w:footerReference w:type="default" r:id="{rid_vacio}"/>'
        f'<w:footerReference w:type="first" r:id="{rid_pie}"/>'
        f'<w:pgSz w:w="{A4[0]}" w:h="{A4[1]}"/><w:pgMar {margenes} w:gutter="0"/>'
        '<w:pgNumType w:start="1"/><w:titlePg/></w:sectPr>')
    ultimo = bloques[-1]
    ppr = ultimo.find(qn("w:pPr"))
    if ppr is None:
        ppr = parse_xml(f"<w:pPr {NS}/>")
        ultimo.insert(0, ppr)
    ppr.append(sect)


def secciones(doc, tp):
    rid = nueva_parte_pie(doc, pie(tp))
    rid_ap = nueva_parte_pie(doc, pie_apaisado(tp))
    body = doc.element.body
    for s in list(body.iter(qn("w:sectPr"))):
        marca = s.get(qn("w:rsidR"))
        if marca == MARCA_VERTICAL:
            s.addprevious(sect_vertical(rid)); s.getparent().remove(s)
        elif marca == MARCA_APAISADA:
            s.addprevious(sect_apaisada(rid_ap)); s.getparent().remove(s)
    final = body.find(qn("w:sectPr"))
    if final is not None:
        body.remove(final)
    body.append(sect_vertical(rid))


# ── Índice ───────────────────────────────────────────────────────────────

def encabezados(doc):
    """(nivel, texto, marcador) de cada Heading1/Heading2, en orden."""
    out = []
    for p in doc.element.body.iter(qn("w:p")):
        ps = p.find(qn("w:pPr") + "/" + qn("w:pStyle"))
        sid = ps.get(qn("w:val")) if ps is not None else ""
        if sid in ("Heading1", "Heading2"):
            bm = p.find(qn("w:bookmarkStart"))
            if bm is None:
                nombre = f"_Toc{len(out) + 1:04d}"
                bm = parse_xml(f'<w:bookmarkStart {NS} w:id="{9000 + len(out)}" w:name="{nombre}"/>')
                p.insert(1, bm)
                p.append(parse_xml(f'<w:bookmarkEnd {NS} w:id="{9000 + len(out)}"/>'))
            texto = "".join(t.text or "" for t in p.iter(qn("w:t"))).strip()
            out.append((1 if sid == "Heading1" else 2, texto, bm.get(qn("w:name"))))
    return out


def indice_xml(entradas, paginas):
    esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;")
    filas = []
    for k, (nivel, texto, marca) in enumerate(entradas):
        ini = ""
        if k == 0:
            ini = ('<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
                   '<w:r><w:instrText xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText></w:r>'
                   '<w:r><w:fldChar w:fldCharType="separate"/></w:r>')
        fin = '<w:r><w:fldChar w:fldCharType="end"/></w:r>' if k == len(entradas) - 1 else ""
        filas.append(
            f'<w:p><w:pPr><w:pStyle w:val="TOC{nivel}"/>'
            f'<w:tabs><w:tab w:val="right" w:leader="dot" w:pos="{ANCHO_TEXTO}"/></w:tabs></w:pPr>{ini}'
            f'<w:hyperlink w:anchor="{marca}" w:history="1"><w:r><w:t xml:space="preserve">{esc(texto)}</w:t></w:r>'
            f'<w:r><w:tab/></w:r><w:r><w:t>{paginas.get(k, "")}</w:t></w:r></w:hyperlink>{fin}</w:p>')
    return parse_xml(
        f'<w:sdt {NS}><w:sdtPr><w:docPartObj><w:docPartGallery w:val="Table of Contents"/><w:docPartUnique/>'
        f'</w:docPartObj></w:sdtPr><w:sdtContent>{"".join(filas)}</w:sdtContent></w:sdt>')


def a_pdf(docx, carpeta):
    perfil = Path(carpeta, "lo").resolve()
    subprocess.run(["soffice", "--headless", f"-env:UserInstallation=file://{perfil}",
                    "--convert-to", "pdf", "--outdir", str(carpeta), str(docx)],
                   check=True, capture_output=True)
    return Path(carpeta, Path(docx).stem + ".pdf")


def paginar(docx, entradas, aux):
    """Página de cada encabezado, según LibreOffice (las páginas del documento
    empiezan en 1 en la carátula, igual que en Word)."""
    pdf = a_pdf(docx, aux)
    txt = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], check=True,
                         capture_output=True, text=True).stdout
    paginas = txt.split("\f")
    norm = lambda s: re.sub(r"\s+", " ", s).strip()
    resultado, desde = {}, 2       # páginas 1 (carátula) y 2 (índice) no cuentan
    for k, (_, texto, _) in enumerate(entradas):
        clave = norm(texto)[:45]
        for n in range(desde, len(paginas)):
            if any(norm(linea).startswith(clave) for linea in paginas[n].splitlines()):
                resultado[k] = str(n + 1)
                desde = n
                break
    return resultado


def armar(ruta, ruta_yaml, version, ruta_car):
    tp = datos(ruta_yaml, version)
    doc = Document(ruta)
    estilos(doc)
    # Notas al pie: python-docx no las modela; se editan como XML y se reescriben
    parte_notas = next((r.target_part for r in doc.part.rels.values() if r.reltype == RT.FOOTNOTES), None)
    notas = parse_xml(parte_notas.blob) if parte_notas is not None else None
    parrafos_directos(doc, notas)
    if notas is not None:
        parte_notas._blob = etree.tostring(notas, xml_declaration=True, encoding="UTF-8", standalone=True)
    tablas(doc)
    insertar_caratula(doc, ruta_car)
    secciones(doc, tp)

    # Índice: primero con las entradas, después con las páginas
    marca = next(p for p in doc.element.body.iter(qn("w:p")) if _txt(p) == "[[INDICE]]")
    entradas = encabezados(doc)
    sdt = indice_xml(entradas, {k: "0" for k in range(len(entradas))})
    marca.addprevious(sdt)
    marca.getparent().remove(marca)
    doc.core_properties.title = tp["titulo"]
    doc.core_properties.author = tp["pie"]
    doc.save(ruta)
    aux = Path(ruta).parent / "aux"
    with tempfile.TemporaryDirectory(dir=aux) as tmp:
        paginas = paginar(ruta, entradas, tmp)
    faltan = [entradas[k][1] for k in range(len(entradas)) if k not in paginas]
    if faltan:
        sys.exit("docx_tp.py: no se encontró la página de: " + "; ".join(faltan))
    doc = Document(ruta)
    sdt = doc.element.body.find(qn("w:sdt"))
    sdt.addprevious(indice_xml(entradas, paginas))
    sdt.getparent().remove(sdt)
    doc.save(ruta)
    # Vista de control: el .docx terminado, en PDF (LibreOffice), en build/aux/
    a_pdf(ruta, aux)


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) == 3 and a[0] == "--nombre":
        print(datos(a[1], a[2])["v"]["archivo"])
    elif len(a) == 5 and a[0] == "caratula":
        caratula(*a[1:])
    elif len(a) == 5 and a[0] == "armar":
        armar(*a[1:])
    else:
        sys.exit(__doc__)
