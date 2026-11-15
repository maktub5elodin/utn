#!/bin/sh
# DXF → PDF A3 con LibreCAD, en negro (IRAM), más un PNG de control en build/planos/.
# Saca la fecha de creación del PDF: el mismo DXF da el mismo PDF.
set -e
raiz="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$raiz/build/planos"
for dxf in 01_conjunto:0.4 02_cabezal:1 03_carrete:1 04_esquema:1; do
  r=${dxf%%:*}; s=${dxf##*:}
  n=$(basename "$r")
  cd "$raiz/planos/$(dirname "$r")"
  rm -f "$n.pdf"
  QT_QPA_PLATFORM=offscreen librecad dxf2pdf -p 420x297 -f 0,0,0,0 -s "$s" -c -m "$n.dxf" </dev/null >/dev/null 2>&1
  test -s "$n.pdf"
  sed -i -E 's#/CreationDate \(D:[^)]*\)#/CreationDate (D:20261119000000)#; s#/ModDate \(D:[^)]*\)#/ModDate (D:20261119000000)#' "$n.pdf"
  pdftoppm -r 110 -png -singlefile "$n.pdf" "$raiz/build/planos/$n"
done
