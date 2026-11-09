# PDF de las resoluciones del 1er Parcial para compartir con el curso, a partir
# del .md (única fuente de contenido). Reglas comunes en pipeline_pdf/comun.mk.
# Solo la figura del ejercicio 2 es propia; las demás son las de ../figuras.

DOC        := Resoluciones_1er_Parcial
FIG_SCRIPT := figuras_resoluciones.py
FIG_NAMES  := fig1_ej2_distancia_minima

# En Word las fórmulas ocupan más: figuras al 75 % para que no queden solas en una página.
DOCX_ESCALA := 0.75

# Fecha del documento para builds reproducibles: 04/nov/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1793761200

include ../../../pipeline_pdf/comun.mk

# Figuras compartidas: si faltan, las genera el Makefile de las correcciones.
FIGS_COMUNES := $(foreach n,fig0_ej1_bolzano_asintota fig2_ej3_tangentes fig3_ej4_continuidad fig4_ej5_dominio_ln,../figuras/$(n).pdf)

$(BUILD)/$(DOC).tex: $(FIGS_COMUNES)

$(FIGS_COMUNES):
	$(MAKE) -C .. figuras
