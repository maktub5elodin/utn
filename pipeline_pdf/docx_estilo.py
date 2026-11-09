#!/usr/bin/env python3
r"""Ajusta el .docx que genera pandoc: make docx lo corre después de pandoc.

Sin reference.docx (binario, no versionable en este repo):
  - página A4 y texto de 11 pt, como el PDF;
  - títulos en negro;
  - estilo "Respuesta" (> [!TIP]): recuadro verde, igual que en el PDF;
  - fórmulas de \boxed y de las respuestas en verde;
  - figuras escaladas, si el documento define DOCX_ESCALA en su Makefile.

Uso: python3 docx_estilo.py archivo.docx [escala de figuras]   (solo biblioteca estándar)
"""
import re
import shutil
import sys
import zipfile
from pathlib import Path

VERDE_RECUADRO = "228B22"
VERDE_TEXTO = "196F3D"
VERDE_FONDO = "E9F7EF"
VERDE_FILETE = "27AE60"

# 16,5 cm de texto: el ancho con el que pandoc escala las figuras.
SECCION = ('<w:pgSz w:w="11906" w:h="16838"/>'
           '<w:pgMar w:top="1418" w:right="1276" w:bottom="1418" w:left="1276" '
           'w:header="708" w:footer="708" w:gutter="0"/>')

ESTILO_RESPUESTA = (
    '<w:style w:type="paragraph" w:customStyle="1" w:styleId="Respuesta">'
    '<w:name w:val="Respuesta"/><w:basedOn w:val="Normal"/><w:qFormat/>'
    '<w:pPr><w:pBdr>'
    f'<w:left w:val="single" w:sz="24" w:space="6" w:color="{VERDE_FILETE}"/>'
    f'</w:pBdr><w:shd w:val="clear" w:color="auto" w:fill="{VERDE_FONDO}"/>'
    '<w:spacing w:before="120" w:after="120"/><w:ind w:left="850" w:right="850"/>'
    '<w:jc w:val="center"/></w:pPr>'
    f'<w:rPr><w:color w:val="{VERDE_TEXTO}"/></w:rPr></w:style>')


def pintar(xml, color):
    """Da color a cada corrida de fórmula (m:r) y a los recuadros de xml."""
    def corrida(m):
        return (f'{m[1]}<w:rPr><w:color w:val="{color}"/></w:rPr>{m[3]}')
    xml = re.sub(r'(<m:r>(?:<m:rPr>(?:(?!</m:rPr>).)*</m:rPr>|<m:rPr ?/>)?)'
                 r'(<w:rPr>(?:(?!</w:rPr>).)*</w:rPr>|<w:rPr ?/>)?(<m:t\b)',
                 corrida, xml, flags=re.S)
    return re.sub(r'<m:borderBox>(?:<m:borderBoxPr ?/>|<m:borderBoxPr>.*?</m:borderBoxPr>)?',
                  '<m:borderBox><m:borderBoxPr><m:ctrlPr><w:rPr>'
                  f'<w:color w:val="{color}"/></w:rPr></m:ctrlPr></m:borderBoxPr>',
                  xml, flags=re.S)


def documento(xml, escala):
    # pgSz y pgMar van después de footnotePr: Word exige ese orden.
    xml = re.sub(r'<w:pgSz\b[^>]*/>|<w:pgMar\b[^>]*/>', '', xml)
    xml = xml.replace('</w:sectPr>', SECCION + '</w:sectPr>')
    if '<w:sectPr' not in xml:
        xml = xml.replace('</w:body>', f'<w:sectPr>{SECCION}</w:sectPr></w:body>')
    if escala != 1:
        xml = re.sub(r'(<(?:wp:extent|a:ext) cx=")(\d+)(" cy=")(\d+)"',
                     lambda m: f'{m[1]}{round(int(m[2]) * escala)}{m[3]}{round(int(m[4]) * escala)}"',
                     xml)
    xml = re.sub(r'<m:borderBox>.*?</m:borderBox>',
                 lambda m: pintar(m[0], VERDE_RECUADRO), xml, flags=re.S)
    return re.sub(r'<w:p(?: [^>]*)?>(?:(?!</w:p>).)*?<w:pStyle w:val="Respuesta"/>.*?</w:p>',
                  lambda m: pintar(m[0], VERDE_TEXTO), xml, flags=re.S)


def estilos(xml):
    # Títulos en negro: pandoc les da el color del tema (sin valor fijo).
    xml = re.sub(r'<w:style\b[^>]*w:styleId="(?:Heading\d|Title|Subtitle)".*?</w:style>',
                 lambda m: re.sub(r'<w:color\b[^>]*/>', '<w:color w:val="000000"/>', m[0]),
                 xml, flags=re.S)
    xml = re.sub(r'(<w:docDefaults>.*?<w:sz w:val=")\d+', r'\g<1>22', xml, count=1, flags=re.S)
    xml, n = re.subn(r'<w:style\b[^>]*w:styleId="Respuesta".*?</w:style>',
                     ESTILO_RESPUESTA, xml, flags=re.S)
    return xml if n else xml.replace('</w:styles>', ESTILO_RESPUESTA + '</w:styles>')


def main(ruta, escala=1.0):
    ruta = Path(ruta)
    tmp = ruta.with_suffix('.tmp')
    cambios = {'word/document.xml': lambda x: documento(x, escala), 'word/styles.xml': estilos}
    with zipfile.ZipFile(ruta) as ent, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as sal:
        for item in ent.infolist():
            datos = ent.read(item.filename)
            if item.filename in cambios:
                datos = cambios[item.filename](datos.decode('utf-8')).encode('utf-8')
            sal.writestr(item, datos)
    shutil.move(tmp, ruta)


if __name__ == '__main__':
    main(sys.argv[1], float(sys.argv[2]) if len(sys.argv) > 2 else 1.0)
