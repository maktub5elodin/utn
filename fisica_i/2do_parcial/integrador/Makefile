# PDF integrador del 2do parcial de Física I: los ejercicios de los cuatro
# documentos de 2do_parcial/, reordenados por tema y dificultad.
# Reglas comunes en pipeline_pdf/comun.mk: make | make clean
#
# El .md se genera con armar_integrador.py a partir de los .md de origen: las
# correcciones se hacen allá y se regeneran con make.

DOC := Integrador_2do_Parcial
ORIGENES := parciales_vella examen_tipo guia_extra parcial_2002
FUENTES_MD := $(foreach d,$(ORIGENES),$(wildcard ../$(d)/*.md))

# Fecha del documento para builds reproducibles: 22/nov/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1795316400

include ../../../pipeline_pdf/comun.mk

$(DOC).md: armar_integrador.py $(FUENTES_MD)
	python3 armar_integrador.py

# Las figuras son las de los documentos de origen (en PDF vectorial).
.PHONY: figuras-origen
figuras-origen:
	@for d in $(ORIGENES); do $(MAKE) --no-print-directory -C ../$$d figuras; done

$(BUILD)/$(DOC).tex: $(wildcard $(foreach d,$(ORIGENES),../$(d)/figuras/*.pdf)) | figuras-origen
