# Hoja de fórmulas de Física I: LaTeX directo (no pasa por pandoc ni por
# pipeline_pdf/, porque necesita control fino del espacio: 3 columnas). Es hoja de
# estudio: a diferencia de la de Química, no se exige una sola carilla.
#
#   make        -> build/hoja_formulas.pdf
#   make figuras -> figuras/mcu_*.png (solo para hoja_formulas.md)
#   make clean  -> borra build/

DOC := hoja_formulas

# Fecha del documento para builds reproducibles: 31/oct/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1793415600
export SOURCE_DATE_EPOCH
export FORCE_SOURCE_DATE := 1

BUILD   := build
XELATEX := xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD)

.PHONY: all clean figuras
.DELETE_ON_ERROR:

all: $(BUILD)/$(DOC).pdf

$(BUILD):
	mkdir -p $@

$(BUILD)/$(DOC).pdf: $(DOC).tex | $(BUILD)
	@$(XELATEX) $< > /dev/null || { grep -A5 '^!' $(BUILD)/$(DOC).log; exit 1; }
	@if grep -q 'Missing character' $(BUILD)/$(DOC).log; then \
		grep 'Missing character' $(BUILD)/$(DOC).log | sort -u; \
		echo "ERROR: caracteres sin glifo en la fuente"; exit 1; fi
	@echo "--- Advertencias de LaTeX:"
	@grep -E 'Warning|Overfull|Underfull' $(BUILD)/$(DOC).log || echo "(ninguna)"
	@echo "OK: $@"

# Figuras del .md (no entran al PDF).
figuras:
	python3 figuras_mcu.py

clean:
	rm -rf $(BUILD)
