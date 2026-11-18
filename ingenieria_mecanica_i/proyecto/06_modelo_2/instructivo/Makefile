# Instructivo de armado (A4 vertical) y plantilla de perforación de la base (A3).
# El .md y la plantilla salen de generar_instructivo.py, con los números de
# ../parametros.py, ../resultados.json y ../build/armado.json; las vistas de cada
# paso (pasos/*.png) las renderiza ../vistas_armado.py. Desde la carpeta del
# modelo: make armado_pdf. Reglas comunes en pipeline_pdf/comun.mk.

DOC := instructivo_armado

# Fecha del documento para builds reproducibles: 8/nov/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1794106800

include ../../../../pipeline_pdf/comun.mk

DATOS := generar_instructivo.py ../parametros.py ../armado.py ../resultados.json ../build/armado.json

all: build/plantilla_base_A3.pdf

$(DOC).md build/plantilla_base_A3.pdf pasos/plantilla.png &: $(DATOS) | $(BUILD)
	python3 generar_instructivo.py

$(BUILD)/$(DOC).tex: pasos/plantilla.png $(wildcard pasos/paso_*.png) portada.tex preambulo.tex
