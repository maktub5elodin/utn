# PDF de la ficha de impresión, para Maty. El .md lo escribe ../exportar_stl.py
# y las miniaturas ../vista.py: se arma con `make ficha_pdf` (o `make`) desde
# la carpeta del modelo, que regenera todo lo anterior si hace falta.
# Reglas comunes en pipeline_pdf/comun.mk.

DOC := ficha_impresion

# Fecha del documento para builds reproducibles: 7/nov/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1794020400

include ../../../../pipeline_pdf/comun.mk

# Las miniaturas no pasan por png-a-pdf (no están en figuras/): se incluyen como PNG.
$(BUILD)/$(DOC).tex: $(wildcard miniaturas/*.png)
