# Perfil «informe de laboratorio de Física»: carátula de la U.D.B. Física +
# estética de los informes TP5/TP6, en PDF (principal) y en Word (editable,
# para compartir con el grupo).
#
# Makefile de cada informe (ver plantilla/):
#
#   DOC               := informe            # el .md, sin extensión
#   SOURCE_DATE_EPOCH := <fecha del TP>     # builds reproducibles (obligatoria)
#   FIG_SCRIPT / FIG_NAMES                  # opcionales, como en comun.mk
#   include ../../../pipeline_pdf/lab_fisica/lab.mk
#
#   make        -> build/A1193-TP5-G5.pdf   (nombre armado desde pdf.yaml)
#   make docx   -> build/A1193-TP5-G5.docx
#
# Los datos del informe van en el bloque `laboratorio:` del pdf.yaml.

LAB := $(patsubst %/,%,$(dir $(lastword $(MAKEFILE_LIST))))

# Nombre de salida: <curso>-TP<n>-G<grupo> (o `archivo:` en pdf.yaml)
SALIDA := $(shell python3 $(LAB)/docx_lab.py --nombre pdf.yaml)
ifeq ($(SALIDA),)
$(error No se pudo armar el nombre de salida desde pdf.yaml (¿falta metadata.laboratorio?))
endif

PDF_DEFAULTS  := $(LAB)/pdf.yaml
DOCX_DEFAULTS := $(LAB)/docx.yaml
# Logo UTN para Word: PNG compartido, generado una sola vez (regla en comun.mk).
LOGO_PNG      := $(LAB)/../logos/build/logo_utn.png
DOCX_POST      = python3 $(LAB)/docx_lab.py $@ pdf.yaml $(LOGO_PNG)
DOCX_DEPS     := $(LAB)/docx_lab.py $(LOGO_PNG)
PERFIL_DEPS   := $(LAB)/lab-fisica.lua $(LAB)/preambulo.tex $(LAB)/../logos/logo_utn.tex

include $(LAB)/../comun.mk

