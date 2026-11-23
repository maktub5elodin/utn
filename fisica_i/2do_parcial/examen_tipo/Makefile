# PDF de la resolución del examen tipo propuesto de Física I.
# Reglas comunes en pipeline_pdf/comun.mk: make | make figuras | make clean

DOC        := Examen_Tipo_Fisica_I
FIG_SCRIPT := figuras_examen_tipo.py
FIG_NAMES  := fig1_p1_via_circular fig1b_p1_dcl_D fig2_p2_resortes_AB fig3_p3_cilindro_polea fig4_p4_esfera

# Fecha del documento para builds reproducibles: 22/nov/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1795316400

include ../../../pipeline_pdf/comun.mk

# Las figuras también dependen del estilo común de 2do_parcial/.
$(FIGS): ../figuras_comun.py
