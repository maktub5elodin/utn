# PDF de la resolución de los parciales del 2do parcial de Física I, curso Z1054 (Prof. R. Vella).
# Reglas comunes en pipeline_pdf/comun.mk: make | make figuras | make clean

DOC        := Parciales_Vella_Z1054
FIG_SCRIPT := figuras_parciales_vella.py
FIG_NAMES  := h1_tronco h2_dos_liquidos \
              p1_choque_2d p2_resorte_vertical p3_caneria p4_cilindro_resorte p5_cilindro_F \
              r1_choque_resorte r2_energias_mas r3_bloque_agua r4_cilindro_F r5_polea_resorte \
              q4_barra_cuerda a2_pendulo_resorte a3_resortes_serie a4_cilindro_tambor

# Fecha del documento para builds reproducibles: 22/nov/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1795316400

include ../../../pipeline_pdf/comun.mk

# Las figuras también dependen del estilo común de 2do_parcial/.
$(FIGS): ../figuras_comun.py
