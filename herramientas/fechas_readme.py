#!/usr/bin/env python3
"""Fecha de la última edición real de cada materia, para la tabla del README.

Uso (desde la raíz del repo):
    python3 herramientas/fechas_readme.py              # todas las materias de la tabla
    python3 herramientas/fechas_readme.py fisica_i     # solo esas carpetas
    python3 herramientas/fechas_readme.py -v [...]     # con los archivos de esa fecha

Qué cuenta como edición real: el contenido propio de la carpeta (.md, .tex,
scripts, datos), no lo que genera `make` ni el mantenimiento. Por archivo:

- Se ignoran los generados y la infraestructura: build/, .build/, figuras/*.png,
  __pycache__/, Makefile y CLAUDE.md.
- Con cambios sin commitear (o nuevo): su mtime.
- Commiteado: el menor entre su mtime y la fecha del último commit que lo tocó
  sin ser de mantenimiento (mensaje que empieza con «mantenimiento:»).
  · Commit tardío de algo editado antes: gana el mtime (fecha real del trabajo).
  · Archivo reescrito igual por un `make` o tocado por un arreglo de
    mantenimiento: gana la fecha del commit real anterior.

La fecha de la materia es la más reciente de sus archivos. Con -v lista los
archivos editados ese día, para escribir la columna «Último trabajo».
"""
import datetime as dt
import os
import re
import subprocess
import sys

MESES = "ene feb mar abr may jun jul ago sep oct nov dic".split()
IGNORAR_DIR = {"build", ".build", "__pycache__"}
IGNORAR_ARCH = {"Makefile", "CLAUDE.md"}


def git(*args):
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def archivos(carpeta):
    lista = git("ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", carpeta)
    for f in filter(None, lista.split("\0")):
        partes = f.split("/")
        if IGNORAR_DIR & set(partes[:-1]) or partes[-1] in IGNORAR_ARCH:
            continue
        if "figuras" in partes[:-1] and f.endswith(".png"):
            continue
        if os.path.isfile(f):
            yield f


def fecha(f, sucios):
    mtime = dt.date.fromtimestamp(os.path.getmtime(f))
    if f in sucios:
        return mtime
    commit = git("log", "-1", "--format=%cs", "--invert-grep", "-E",
                 "--grep=^mantenimiento:", "--", f).strip()
    return min(mtime, dt.date.fromisoformat(commit)) if commit else mtime


def texto(d):
    return f"{d.day:02d}/{MESES[d.month - 1]}/{d.year}"


def materias_del_readme():
    with open("README.md", encoding="utf-8") as f:
        return re.findall(r"^\| \[`([^`]+)/`\]", f.read(), re.M)


def main():
    os.chdir(git("rev-parse", "--show-toplevel").strip())
    sucios = set(git("diff", "--name-only", "HEAD").split()) | \
        set(git("ls-files", "--others", "--exclude-standard").split())
    args = sys.argv[1:]
    detalle = "-v" in args
    pedidas = [a for a in args if a != "-v"] or materias_del_readme()
    for carpeta in pedidas:
        carpeta = carpeta.rstrip("/")
        fechas = {f: fecha(f, sucios) for f in archivos(carpeta)}
        if not fechas:
            print(f"{carpeta:28s} (sin archivos de contenido)")
            continue
        ultima = max(fechas.values())
        print(f"{carpeta:28s} {texto(ultima)}")
        if detalle:
            for f in sorted(f for f, d in fechas.items() if d == ultima):
                print(f"    {f}")


if __name__ == "__main__":
    main()
