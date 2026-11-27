# PDF con las resoluciones de los parciales modelo del 1er parcial de AyGA
# (campus virtual), agrupadas por parcial. Reglas comunes en pipeline_pdf/comun.mk.
#
# figuras.py: figuras 3D de los ejercicios de geometría (cada una verificada con assert).
# temas.py: lee las marcas <!-- temas: ... --> del .md y genera el gráfico de
# frecuencia de temas (las marcas las va a usar también el documento por tema).
# Los enunciados están en ../fuentes/ (locales, no se versionan).

DOC        := Parciales_1er_Parcial
FIG_SCRIPT := figuras.py
FIG_NAMES  := fig_p1t1_e1 fig_p1t1_e2 fig_p2_e1 fig_p2_e2 \
              fig_p3_e1 fig_p3_e2 fig_p4_e1 fig_p4_e2 fig_p4_e5 fig_p5_e1 fig_p5_e2 \
              fig_p6_e1 fig_p6_e2 fig_p6_e5 fig_p7_e1 fig_p7_e2 fig_sarrus

# Fecha del documento para builds reproducibles: 24/nov/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1795489200

include ../../../pipeline_pdf/comun.mk

# Frecuencia de temas: depende de las marcas del .md, no de figuras.py.
FREC := figuras/fig_frecuencia_temas.pdf figuras/fig_frecuencia_temas.png

$(FREC) &: temas.py $(DOC).md
	python3 temas.py

$(TEX): $(FREC)
figuras: $(FREC)

# Filtro propio (marcadores del outline con fórmulas en Unicode).
$(TEX): marcadores.lua
