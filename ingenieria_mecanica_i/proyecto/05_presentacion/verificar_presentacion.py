#!/usr/bin/env python3
"""Control de calidad de la presentación: palabras, fuentes, márgenes, superposiciones, ajuste de texto y tiempos.

Uso: python3 verificar_presentacion.py [archivo.pptx]. Sale con código 1 si encuentra algún problema.
Exenciones acordadas: notas al pie, créditos y rótulos del plano (mínimo 10 pt, fuera del conteo de palabras);
tablas, bibliografía y números de los anillos fuera del conteo de palabras.
"""
import re
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

from lxml import etree
from PIL import ImageFont

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
EMU, W, H = 914400, 13.333, 7.5
BORDE, TOPE_PALABRAS, MIN_PT, MIN_EXENTO = .5, 40, 14, 10
PALABRAS_MINUTO = 115
FUENTES = "/usr/share/fonts/truetype/crosextra/"
EXENTOS = ("Notas al pie", "Crédito", "Rótulo plano")
TITULO_SZ = {"ctrTitle": 44, "title": 34}


def fuente(sz, b, serif):
    nombre = ("Caladea" if serif else "Carlito") + ("-Bold" if b else "-Regular") + ".ttf"
    return ImageFont.truetype(FUENTES + nombre, int(sz * 10))


def alto_texto(sp, ancho):
    """Alto estimado en pulgadas, con métricas de Carlito/Caladea (compatibles con Calibri/Cambria)."""
    total = 0.0
    for p in sp.iter(A + "p"):
        corridas = [(r.findtext(A + "t") or "", r.find(A + "rPr")) for r in p.findall(A + "r")]
        if not corridas:
            continue
        tam, x, lineas = 14.0, 0.0, 1
        for texto, rpr in corridas:
            sz = int(rpr.get("sz", 1400)) / 100
            b = rpr.get("b") == "1"
            latin = rpr.find(A + "latin")
            f = fuente(sz, b, latin is not None and latin.get("typeface") == "+mj-lt")
            tam = max(tam, sz) if lineas or x else sz
            for pal in re.findall(r"\S+\s*", texto):
                largo = f.getlength(pal) / 10 / 72
                if x + f.getlength(pal.rstrip()) / 10 / 72 > ancho and x > 0:
                    lineas, x = lineas + 1, 0.0
                x += largo
        ppr = p.find(A + "pPr")
        esp = 0.0
        if ppr is not None:
            for t in ("spcBef", "spcAft"):
                nodo = ppr.find(f"{A}{t}/{A}spcPts")
                esp += int(nodo.get("val")) / 100 if nodo is not None else 0
        total += (lineas * tam * 1.2 + esp) / 72
    return total


def rect(sp):
    xf = sp.find(f".//{A}xfrm")
    if xf is None:
        xf = sp.find(f"{P}xfrm")
    if xf is None or xf.find(A + "off") is None:
        return None
    o, x = xf.find(A + "off"), xf.find(A + "ext")
    return tuple(int(v) / EMU for v in (o.get("x"), o.get("y"), x.get("cx"), x.get("cy")))


def contiene(a, b, tol=.02):
    return a[0] - tol <= b[0] and a[1] - tol <= b[1] and a[0] + a[2] + tol >= b[0] + b[2] and a[1] + a[3] + tol >= b[1] + b[3]


def main(ruta):
    z = zipfile.ZipFile(ruta)
    problemas = []
    n_lam = len([n for n in z.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)])
    tiempos = defaultdict(lambda: [0, 0])
    print("lám  palabras  (con exentos)")
    for n in range(1, n_lam + 1):
        raiz = etree.fromstring(z.read(f"ppt/slides/slide{n}.xml"))
        arbol = raiz.find(f"{P}cSld/{P}spTree")
        titulo = ""
        palabras = todas = 0
        cajas = []
        for sp in arbol:
            cnv = sp.find(f".//{P}cNvPr")
            if cnv is None or cnv.get("id") == "1":
                continue
            nombre = cnv.get("name")
            ph = sp.find(f".//{P}ph")
            r = rect(sp)
            es_tabla = sp.find(f".//{A}tbl") is not None
            exento = nombre.startswith(EXENTOS)
            # Texto y palabras (párrafo a párrafo, uniendo subíndices a su símbolo)
            for p in sp.iter(A + "p"):
                t = "".join(x.text or "" for x in p.iter(A + "t"))
                c = len([w for w in t.split() if re.search(r"\w", w)])
                todas += c
                if not exento and not es_tabla and not nombre.startswith("Anillo") and not (ph is not None and ph.get("type") == "sldNum"):
                    palabras += c
            if ph is not None and ph.get("type") in TITULO_SZ:
                titulo = "".join(x.text or "" for x in sp.iter(A + "t"))
            # Tamaños
            minimo = MIN_EXENTO if exento else MIN_PT
            for rpr in sp.iter(A + "rPr"):
                if rpr.get("sz") and int(rpr.get("sz")) / 100 < minimo:
                    problemas.append(f"L{n} {nombre}: {int(rpr.get('sz')) / 100} pt < {minimo}")
            if r is None:
                continue
            # Márgenes
            if r[0] < BORDE - .001 or r[1] < BORDE - .001 or r[0] + r[2] > W - BORDE + .001 or r[1] + r[3] > H - BORDE + .001:
                problemas.append(f"L{n} {nombre}: a menos de {BORDE}\" del borde {tuple(round(v, 2) for v in r)}")
            # Ajuste de texto
            if sp.tag == P + "sp" and sp.find(f".//{A}t") is not None:
                bp = sp.find(f"{P}txBody/{A}bodyPr")
                m = int(bp.get("lIns", 0)) / EMU if bp is not None else 0
                req = alto_texto(sp, r[2] - 2 * m) + 2 * m
                if req > r[3] + .02:
                    problemas.append(f"L{n} {nombre}: texto {req:.2f}\" en caja de {r[3]:.2f}\"")
            if sp.tag != P + "cxnSp":
                cajas.append((nombre, r, sp.find(f".//{A}t") is not None))
        # Título
        if titulo:
            ancho = 5.9 if n == 1 else 12.13
            sz = TITULO_SZ["ctrTitle"] if n == 1 else TITULO_SZ["title"]
            if fuente(sz, True, True).getlength(titulo) / 10 / 72 > ancho * (2 if n == 1 else 1):
                problemas.append(f"L{n} título no entra en una línea: {titulo}")
        # Superposiciones (se admite contenido dentro de su tarjeta; el esquema y el plano se dibujan en capas)
        for i, (na, ra, ta) in enumerate(cajas):
            for nb, rb, tb in cajas[i + 1:]:
                if na.startswith(("Esquema", "Plano")) and nb.startswith(("Esquema", "Plano")):
                    continue
                solapa = ra[0] + ra[2] > rb[0] + .02 and rb[0] + rb[2] > ra[0] + .02 and ra[1] + ra[3] > rb[1] + .02 and rb[1] + rb[3] > ra[1] + .02
                if not solapa or (contiene(ra, rb) and not ta) or (contiene(rb, ra) and not tb):
                    continue
                problemas.append(f"L{n} superposición: {na} / {nb}")
        # Gráfico
        rels = z.read(f"ppt/slides/_rels/slide{n}.xml.rels").decode()
        if "charts/chart1.xml" in rels:
            graf = z.read("ppt/charts/chart1.xml").decode()
            for sz in re.findall(r'sz="(\d+)"', graf):
                if int(sz) / 100 < MIN_PT:
                    problemas.append(f"L{n} gráfico: {int(sz) / 100} pt")
            ser = re.findall(r"<c:tx>.*?<c:v>(.*?)</c:v>", graf) + re.findall(r"<c:strCache><c:ptCount val=\"3\"/>(.*?)</c:strCache>", graf)[:1] + re.findall(r"<a:t>(.*?)</a:t>", graf)
            c = sum(len([w for w in re.sub("<[^>]+>", " ", s).split() if re.search(r"\w", w)]) for s in ser)
            palabras += c
        marca = ""
        if n != n_lam and palabras > TOPE_PALABRAS:
            problemas.append(f"L{n}: {palabras} palabras")
            marca = "  <-- excede"
        print(f"{n:>3}  {palabras:>8}  {todas:>12}{marca}")
        # Notas
        notas = etree.fromstring(z.read(f"ppt/notesSlides/notesSlide{n}.xml"))
        texto = " ".join(x.text or "" for x in notas.iter(A + "t") if x.text and len(x.text) > 3)
        m = re.match(r"(.+?) · (\d+):(\d+) min", texto)
        if m:
            cuerpo = texto.split("). ", 1)[1]
            tiempos[m.group(1)][0] += int(m.group(2)) * 60 + int(m.group(3))
            tiempos[m.group(1)][1] += len(cuerpo.split())
    print("\nbloque             asignado  palabras  a %d pal/min" % PALABRAS_MINUTO)
    total = 0
    for k, (seg, pal) in tiempos.items():
        total += seg
        hablado = pal / PALABRAS_MINUTO * 60
        print(f"{k:<18} {seg // 60}:{seg % 60:02d}     {pal:>6}      {int(hablado) // 60}:{int(hablado) % 60:02d}")
        if hablado > seg * 1.15:
            problemas.append(f"Notas del {k}: exceden el tiempo asignado")
    print(f"Total asignado: {total // 60}:{total % 60:02d}")
    # Secciones contiguas y en orden
    pres = z.read("ppt/presentation.xml").decode()
    orden = re.findall(r'<p:sldId id="(\d+)"', pres)
    secc = re.findall(r'<p14:sldId id="(\d+)"', pres)
    if orden != secc:
        problemas.append("Las secciones p14 no siguen el orden de las láminas")
    print(f"\n{len(problemas)} problema(s)")
    for x in problemas:
        print(" -", x)
    return 1 if problemas else 0


if __name__ == "__main__":
    base = Path(__file__).resolve().parent / "Presentacion_Cortadora_PET_S1091_Grupo_1.pptx"
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else base))
