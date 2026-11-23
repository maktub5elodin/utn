# PDF de la resolución de la guía de ejercicios extra del 2do parcial de Física I.
# Reglas comunes en pipeline_pdf/comun.mk: make | make figuras | make clean

DOC        := Guia_Extra_2do_Parcial
FIG_SCRIPT := figuras_guia_extra.py
FIG_NAMES  := f1_sumergido f2_dos_cuerpos f3_esfera_atada f4_cubo f5_caneria \
              r1_rampa r2_disco_F r3_ruedas r4_yoyo r5_plano_F r6_esfera_pista r7_disco_mesa \
              r8_pendulo_balistico r9_bala_bloque r10_varilla_pelota \
              mc1_barra mc2_disco_bala mc3_ecuacion_horaria \
              mas1_pendulo_fisico mas2_xt mas4_ecuacion_horaria mas5_resorte_horizontal

# Fecha del documento para builds reproducibles: 22/nov/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1795316400

include ../../../pipeline_pdf/comun.mk

# Las figuras también dependen del estilo común de 2do_parcial/.
$(FIGS): ../figuras_comun.py
