# Mezcla de cuatro disoluciones (ejercicio del 2.º parcial): LaTeX directo, igual que hoja_formulas/.
#
#   make        -> build/mezcla_disoluciones.pdf
#   make clean  -> borra build/

DOC := mezcla_disoluciones

# Fecha del documento para builds reproducibles: 02/nov/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1793588400
export SOURCE_DATE_EPOCH
export FORCE_SOURCE_DATE := 1

BUILD   := build
XELATEX := xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD)

.PHONY: all clean
.DELETE_ON_ERROR:

all: $(BUILD)/$(DOC).pdf

$(BUILD):
	mkdir -p $@

$(BUILD)/$(DOC).pdf: $(DOC).tex | $(BUILD)
	@$(XELATEX) $< > /dev/null || { grep -A5 '^!' $(BUILD)/$(DOC).log; exit 1; }
	@if grep -q 'Missing character' $(BUILD)/$(DOC).log; then \
		grep 'Missing character' $(BUILD)/$(DOC).log | sort -u; \
		echo "ERROR: caracteres sin glifo en la fuente"; exit 1; fi
	@grep 'Output written' $(BUILD)/$(DOC).log
	@echo "--- Advertencias de LaTeX:"
	@grep -E 'Warning|Overfull|Underfull' $(BUILD)/$(DOC).log || echo "(ninguna)"
	@echo "OK: $@"

clean:
	rm -rf $(BUILD)
