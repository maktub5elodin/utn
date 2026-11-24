#!/usr/bin/env python3
"""Controles del PDF y del Word terminados (perfil tp_mecanica).

Los controles de contenido (secciones, largos, vocabulario, notas ↔
bibliografía, valores) los hace tp-mecanica.lua al compilar; acá se controla
el formato de los archivos ya armados. Termina con error si algo no pasa.

  python3 controles_tp.py pdf  build/X.pdf  pdf.yaml e3
      A4; fuentes embebidas, solo Times New Roman (texto) y TeX Gyre Termes
      Math (fórmulas); pie en todas las páginas; renglones del cuerpo y de las
      notas justificados (borde derecho alineado, salvo el último de cada párrafo)

  python3 controles_tp.py docx build/X.docx pdf.yaml e3
      Times New Roman 12 e interlineado 1,15 por defecto; párrafos del cuerpo
      y de las notas justificados; A4; carátula sin marcadores rojos; pie;
      láminas apaisadas; misma cantidad de notas que el .md; índice con
      números de página que coinciden con el paginado de LibreOffice

  python3 controles_tp.py resumen .build/aux
      tabla con el resultado de todos los controles
"""
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

import yaml

# Intermedios de tp.mk, relativos a la carpeta del documento (desde donde corre make).
AUX = Path(".build", "aux")

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
A4 = (595.28, 841.89)
MARGEN = 70.87                      # 2,5 cm en puntos
FUENTES_OK = re.compile(r"^([A-Z]{6}\+)?(TimesNewRoman|TeXGyreTermesMath)")


def tp(ruta_yaml):
    with open(ruta_yaml, encoding="utf-8") as f:
        return yaml.safe_load(f)["metadata"]["tp"]


def sh(*cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout


def guardar(aux, nombre, res):
    Path(aux).mkdir(parents=True, exist_ok=True)
    Path(aux, nombre).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")


def informar(titulo, res):
    malos = [k for k, v in res.items() if isinstance(v, dict) and not v.get("ok", True)]
    for k, v in res.items():
        if isinstance(v, dict):
            marca = "OK " if v.get("ok", True) else "MAL"
            print(f"  [{marca}] {k}: {v.get('detalle', '')}")
    if malos:
        print(f"ERROR: {titulo}: no pasan {', '.join(malos)}")
        sys.exit(1)
    print(f"OK: {titulo}")


# ── PDF ──────────────────────────────────────────────────────────────────

def control_pdf(ruta, ruta_yaml, version):
    datos = tp(ruta_yaml)
    info = sh("pdfinfo", "-f", "1", "-l", "999", ruta)
    paginas = int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))
    tamanos = re.findall(r"^Page\s+(\d+) size:\s+([\d.]+) x ([\d.]+)", info, re.M)
    rotadas = {int(n) for n, r in re.findall(r"^Page\s+(\d+) rot:\s+(\d+)", info, re.M) if int(r) % 180}
    no_a4 = [n for n, w, h in tamanos
             if not (abs(float(w) - A4[0]) < 1 and abs(float(h) - A4[1]) < 1)]
    res = {"paginas": paginas}
    res["A4"] = {"ok": not no_a4, "detalle": f"{paginas} páginas A4 ({len(rotadas)} apaisadas)"
                 + (f"; no A4: {no_a4}" if no_a4 else "")}

    fuentes = []
    for linea in sh("pdffonts", ruta).splitlines()[2:]:
        partes = linea.split()
        if partes:
            emb = re.search(r"\s(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+", linea)
            fuentes.append((partes[0], emb.group(1) if emb else "?"))
    malas = sorted({f for f, e in fuentes if e != "yes" or not FUENTES_OK.match(f)})
    nombres = sorted({re.sub(r"^[A-Z]{6}\+", "", f) for f, _ in fuentes})
    res["fuentes"] = {"ok": not malas, "detalle": ", ".join(nombres) + (f"; no permitidas o sin embeber: {malas}" if malas else "")}

    pie = datos["pie"]
    textos = sh("pdftotext", "-layout", ruta, "-").split("\f")[:paginas]
    sin_pie = [k + 1 for k, t in enumerate(textos) if pie not in re.sub(r"[ \t]+", " ", t)]
    res["pie"] = {"ok": not sin_pie, "detalle": f"«{pie}» en {paginas - len(sin_pie)}/{paginas} páginas"
                  + (f"; falta en {sin_pie}" if sin_pie else "")}

    res["justificado"] = justificado(ruta, paginas, rotadas)
    guardar(AUX, f"formato_{Path(ruta).stem}.pdf.json", res)
    informar(f"formato del PDF {Path(ruta).name}", res)


def justificado(ruta, paginas, rotadas):
    """Renglones de cuerpo (12 pt) y de notas (10 pt) que no son el último de su
    bloque: el borde derecho tiene que llegar al margen derecho. Se omiten la
    carátula, el índice, las láminas, las tablas y los epígrafes (11 pt)."""
    xml = sh("pdftotext", "-bbox-layout", ruta, "-")
    xml = re.sub(r"<!DOCTYPE[^>]*>", "", xml)
    xml = re.sub(r'\sxmlns="[^"]+"', "", xml, count=1)
    raiz = ET.fromstring(xml)
    derecho = A4[0] - MARGEN
    ancho = derecho - MARGEN

    def alto_de(ln):
        altos = sorted(float(w.get("yMax")) - float(w.get("yMin")) for w in ln.iter("word"))
        return round(altos[len(altos) // 2], 1) if altos else 0

    # Altura de palabra del cuerpo (12 pt): la más frecuente del documento.
    # Notas: 10 pt; epígrafes y tablas (11 pt) quedan afuera.
    conteo = {}
    for ln in raiz.iter("line"):
        conteo[alto_de(ln)] = conteo.get(alto_de(ln), 0) + 1
    h12 = max(conteo, key=conteo.get)
    h10 = h12 * 10 / 12
    def centro(e):
        return (float(e.get("yMin")) + float(e.get("yMax"))) / 2

    revisados, malos = 0, []
    for k, pag in enumerate(raiz.iter("page"), start=1):
        if k <= 2 or k in rotadas:
            continue
        # Rótulos de lista (viñetas, «1.»): pdftotext los deja en otro bloque
        rotulos = [w for w in pag.iter("word") if re.fullmatch(r"[•◦–∗]|\d+\.", w.text or "")]

        def empieza_item(sig):
            x0, c = float(sig.get("xMin")), centro(sig)
            return any(abs(centro(w) - c) < 2 and float(w.get("xMax")) <= x0 + 1 for w in rotulos)

        for bloque in pag.iter("block"):
            lineas = list(bloque.iter("line"))
            for i, ln in enumerate(lineas[:-1]):
                x0, x1 = float(ln.get("xMin")), float(ln.get("xMax"))
                alto = alto_de(ln)
                if abs(alto - h12) < 0.3:
                    puntos = 12
                elif abs(alto - h10) < 0.3:
                    puntos = 10
                else:
                    continue
                if x0 > MARGEN + 40 or (x1 - x0) < 0.5 * ancho:
                    continue
                # Solo si el renglón siguiente continúa el mismo párrafo: misma
                # sangría y sin el espacio entre párrafos (si no, este renglón es
                # el último de su párrafo o de su ítem, y no va justificado)
                sig = lineas[i + 1]
                paso = max(float(w.get("yMax")) for w in sig.iter("word")) - \
                    max(float(w.get("yMax")) for w in ln.iter("word"))
                primera = next(iter(sig.iter("word"))).text or ""
                if abs(float(sig.get("xMin")) - x0) > 1.5 or paso > 1.6 * puntos or empieza_item(sig):
                    continue
                if re.fullmatch(r"[•◦–∗]|\d+\.", primera):   # empieza otro ítem de la lista
                    continue
                if puntos == 10 and re.fullmatch(r"\d+", primera):   # empieza otra nota
                    continue
                revisados += 1
                if x1 < derecho - 2.5:
                    texto = " ".join(w.text or "" for w in ln.iter("word"))
                    malos.append(f"p. {k}: «{texto[:50]}…» termina a {derecho - x1:.1f} pt del margen")
    return {"ok": not malos, "detalle": f"{revisados} renglones revisados, {len(malos)} sin justificar"
            + ("; " + " | ".join(malos[:5]) if malos else "")}


# ── Word ─────────────────────────────────────────────────────────────────

def _xml(z, nombre):
    return ET.fromstring(z.read(nombre)) if nombre in z.namelist() else None


def _texto(e):
    return "".join(t.text or "" for t in e.iter(W + "t"))


def control_docx(ruta, ruta_yaml, version):
    datos = tp(ruta_yaml)
    res = {}
    z = zipfile.ZipFile(ruta)
    doc, estilos, notas = _xml(z, "word/document.xml"), _xml(z, "word/styles.xml"), _xml(z, "word/footnotes.xml")
    body = doc.find(W + "body")

    # Valores por defecto y estilo del cuerpo
    rpr = estilos.find(f"{W}docDefaults/{W}rPrDefault/{W}rPr")
    fuente = rpr.find(W + "rFonts").get(W + "ascii")
    tam = rpr.find(W + "sz").get(W + "val")
    cuerpo = estilos.find(f"{W}style[@{W}styleId='BodyText']/{W}pPr")
    esp = cuerpo.find(W + "spacing")
    linea = (esp.get(W + "line"), esp.get(W + "lineRule"))
    jc = cuerpo.find(W + "jc").get(W + "val")
    res["fuente"] = {"ok": fuente == "Times New Roman" and tam == "24",
                     "detalle": f"por defecto {fuente} {int(tam) / 2:g} pt"}
    usadas = {f.get(W + "ascii") for f in doc.iter(W + "rFonts") if f.get(W + "ascii")}
    otras = usadas - {"Times New Roman", "Cambria Math"}
    temas = [f for f in doc.iter(W + "rFonts") if f.get(W + "asciiTheme")]
    res["fuentes_usadas"] = {"ok": not otras and not temas,
                             "detalle": ", ".join(sorted(usadas)) + (f"; otras: {otras}" if otras else "")}
    res["interlineado"] = {"ok": linea == ("276", "auto"), "detalle": f"cuerpo: line={linea[0]} ({int(linea[0]) / 240:.2f}), {linea[1]}"}

    # Párrafos del cuerpo: justificados con pPr directo (después de la carátula)
    hijos = list(body)
    fin_car = next(i for i, e in enumerate(hijos) if e.find(f".//{W}pPr/{W}sectPr") is not None)
    excluir = re.compile(r"^(Heading\d|TituloTP|Indicetitulo|ImageCaption|TableCaption|CaptionedFigure|Figure|Lamina|Piedelamina|TOC\d)$")
    revisados, malos = 0, []
    for e in hijos[fin_car + 1:]:
        if e.tag != W + "p":
            continue
        ps = e.find(f"{W}pPr/{W}pStyle")
        sid = ps.get(W + "val") if ps is not None else ""
        if excluir.match(sid) or not _texto(e).strip() or e.find(f".//{W}drawing") is not None:
            continue
        revisados += 1
        j = e.find(f"{W}pPr/{W}jc")
        s = e.find(f"{W}pPr/{W}spacing")
        if j is None or j.get(W + "val") != "both" or s is None or s.get(W + "line") not in ("276",):
            malos.append(f"{sid or 'sin estilo'}: «{_texto(e)[:40]}»")
    notas_rev, notas_mal = 0, []
    n_notas = 0
    if notas is not None:
        for fn in notas.iter(W + "footnote"):
            if int(fn.get(W + "id")) <= 0 or fn.get(W + "type"):
                continue
            n_notas += 1
            for p in fn.iter(W + "p"):
                notas_rev += 1
                j = p.find(f"{W}pPr/{W}jc")
                if j is None or j.get(W + "val") != "both":
                    notas_mal.append(_texto(p)[:40])
    res["justificado"] = {"ok": not malos and not notas_mal and jc == "both",
                          "detalle": f"{revisados} párrafos del cuerpo y {notas_rev} de notas; estilo del cuerpo: {jc}"
                          + (f"; sin justificar: {(malos + notas_mal)[:4]}" if malos or notas_mal else "")}

    # Notas: tantas como en el .md
    lua = AUX / f"controles_{Path(ruta).stem}.docx.json"
    esperadas = json.loads(lua.read_text(encoding="utf-8"))["notas"] if lua.exists() else None
    res["notas"] = {"ok": esperadas is None or esperadas == n_notas,
                    "detalle": f"{n_notas} notas al pie reales" + (f" (en el .md: {esperadas})" if esperadas is not None else "")}

    # Secciones: A4 vertical o apaisada; láminas
    sects = list(body.iter(W + "sectPr"))
    tam_mal, apaisadas = [], 0
    for s in sects:
        pg = s.find(W + "pgSz")
        wh = (int(pg.get(W + "w")), int(pg.get(W + "h")))
        if wh == (16838, 11906):
            apaisadas += 1
        elif wh != (11906, 16838):
            tam_mal.append(wh)
    res["A4"] = {"ok": not tam_mal and apaisadas == int(datos["controles"]["laminas"]),
                 "detalle": f"{len(sects)} secciones A4, {apaisadas} apaisadas (láminas)" + (f"; otras: {tam_mal}" if tam_mal else "")}

    # Carátula completa
    car = "".join(ET.tostring(e, encoding="unicode") for e in hijos[:fin_car + 1])
    rojo = re.search(r'color[^>]*val="[Ff][Ff]0000"', car)
    marcas = [m for m in ("XX", "Reemplazar") if m in car]
    textos_car = "".join(_texto(e) for e in hijos[:fin_car + 1])
    v = datos["versiones"][version]
    linea_car = f"ENTREGA N°{v['entrega']} - REVISIÓN N°{v['revision']}"
    falta = [x for x in (datos["titulo"], datos["profesor"], datos["atp"], linea_car) if x not in textos_car]
    falta += [a["legajo"] for a in datos["alumnos"] if a["legajo"] not in textos_car]
    res["caratula"] = {"ok": not rojo and not marcas and not falta,
                       "detalle": f"oficial completada ({linea_car})"
                       + ("; con resumen" if v.get("resumen") else "; resumen vacío")
                       + (f"; faltan: {falta}" if falta else "") + ("; quedan marcadores" if rojo or marcas else "")}

    # Pie
    pies = [ET.fromstring(z.read(n)) for n in z.namelist() if re.match(r"word/footer\d+\.xml", n)]
    con_pie = sum(datos["pie"] in _texto(p) for p in pies)
    con_campo = sum(" PAGE " in "".join(t.text or "" for t in p.iter(W + "instrText")) for p in pies)
    res["pie"] = {"ok": con_pie >= 2 and con_campo >= 1, "detalle": f"{con_pie} pies con el texto, {con_campo} con número de página"}

    # Índice: entradas y números de página según LibreOffice
    sdt = body.find(W + "sdt")
    entradas = []
    if sdt is not None:
        for p in sdt.iter(W + "p"):
            ts = [t.text or "" for t in p.iter(W + "t")]
            if len(ts) >= 2:
                entradas.append((ts[0].strip(), ts[-1].strip()))
    vista = AUX / (Path(ruta).stem + ".pdf")
    desajustes = []
    if vista.exists():
        paginas = sh("pdftotext", "-layout", str(vista), "-").split("\f")
        for texto, num in entradas:
            pag = paginas[int(num) - 1] if num.isdigit() and int(num) <= len(paginas) else ""
            if not any(re.sub(r"\s+", " ", l).strip().startswith(texto[:45]) for l in pag.splitlines()):
                desajustes.append(f"{texto} → {num}")
    res["indice"] = {"ok": bool(entradas) and all(n.isdigit() for _, n in entradas) and not desajustes,
                     "detalle": f"{len(entradas)} entradas con página" + (f"; no coinciden: {desajustes}" if desajustes else "")}

    guardar(AUX, f"formato_{Path(ruta).stem}.docx.json", res)
    informar(f"formato del Word {Path(ruta).name}", res)


# ── Resumen ──────────────────────────────────────────────────────────────

def resumen(aux):
    aux = Path(aux)
    print("\nResumen de controles")
    for f in sorted(aux.glob("controles_*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        largos = ", ".join(f"{k}: {v['palabras']} palabras / {v['parrafos']} párr."
                           for k, v in d.items() if isinstance(v, dict) and "palabras" in v)
        print(f"  {f.stem.replace('controles_', '')}: {len(d.get('problemas', []))} problemas; "
              f"{d.get('valores_verificados')} valores, {d.get('notas')} notas, {d.get('bibliografia')} en "
              f"Bibliografía, {d.get('links')} links, {d.get('laminas')} láminas, {d.get('figuras')} figuras, "
              f"{d.get('tablas')} tablas; {largos}")
    for f in sorted(aux.glob("formato_*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        malos = [k for k, v in d.items() if isinstance(v, dict) and not v.get("ok", True)]
        print(f"  {f.stem.replace('formato_', '')}: " + ("OK" if not malos else "NO PASA: " + ", ".join(malos)))


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) == 4 and a[0] == "pdf":
        control_pdf(*a[1:])
    elif len(a) == 4 and a[0] == "docx":
        control_docx(*a[1:])
    elif len(a) == 2 and a[0] == "resumen":
        resumen(a[1])
    else:
        sys.exit(__doc__)
