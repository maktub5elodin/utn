# PDF del parcial de Física I de 2002 con los enunciados reconstruidos.
# Reglas comunes en pipeline_pdf/comun.mk: make | make figuras | make clean

DOC        := Parcial_2002_Reconstruido
FIG_SCRIPT := figuras_parcial_2002.py
FIG_NAMES  := fig1_p1_pista fig2_p2_resortes fig3_p3_polea_plano fig4_p4_polea_resorte

# Fecha del documento para builds reproducibles: 22/nov/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1795316400

include ../../../pipeline_pdf/comun.mk

# Las figuras también dependen del estilo común de 2do_parcial/.
$(FIGS): ../figuras_comun.py
