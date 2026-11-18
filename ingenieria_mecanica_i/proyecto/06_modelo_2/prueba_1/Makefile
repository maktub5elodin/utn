# Hoja de la prueba 1 (medir el tiro), para imprimir. El .md y el dibujo salen
# de generar_prueba1.py, con los umbrales de ../parametros.py.
# Reglas comunes en pipeline_pdf/comun.mk.

DOC        := prueba_1_tiro
FIG_SCRIPT := generar_prueba1.py
FIG_NAMES  := armado

# Fecha del documento para builds reproducibles: 7/nov/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1794020400

include ../../../../pipeline_pdf/comun.mk

# El .md sale del mismo script que el dibujo, y depende de los parámetros del modelo.
$(DOC).md: $(FIG_SCRIPT) ../parametros.py
	python3 $(FIG_SCRIPT)
$(FIGS): ../parametros.py
