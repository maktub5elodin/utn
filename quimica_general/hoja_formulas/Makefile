# Hoja de fórmulas de Química General: LaTeX directo (no pasa por pandoc ni por
# pipeline_pdf/, porque necesita control fino del espacio: una carilla, 3 columnas).
#
#   make        -> build/hoja_formulas.pdf
#   make clean  -> borra build/

DOC := hoja_formulas

# Fecha del documento para builds reproducibles: 26/oct/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1792983600
export SOURCE_DATE_EPOCH
export FORCE_SOURCE_DATE := 1

BUILD   := build
XELATEX := xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD)

.PHONY: all clean
.DELETE_ON_ERROR:

all: $(BUILD)/$(DOC).pdf

$(BUILD):
	mkdir -p $@

# Además de compilar, verifica que la hoja siga entrando en una sola carilla.
$(BUILD)/$(DOC).pdf: $(DOC).tex | $(BUILD)
	@$(XELATEX) $< > /dev/null || { grep -A5 '^!' $(BUILD)/$(DOC).log; exit 1; }
	@if grep -q 'Missing character' $(BUILD)/$(DOC).log; then \
		grep 'Missing character' $(BUILD)/$(DOC).log | sort -u; \
		echo "ERROR: caracteres sin glifo en la fuente"; exit 1; fi
	@if ! grep -q 'Output written on .*(1 page' $(BUILD)/$(DOC).log; then \
		grep 'Output written' $(BUILD)/$(DOC).log; \
		echo "ERROR: la hoja pasó de una carilla"; exit 1; fi
	@echo "--- Advertencias de LaTeX:"
	@grep -E 'Warning|Overfull|Underfull' $(BUILD)/$(DOC).log || echo "(ninguna)"
	@echo "OK: $@"

clean:
	rm -rf $(BUILD)
