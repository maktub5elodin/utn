# Repaso 2do Parcial de Química General: LaTeX directo, igual que hoja_formulas/.
#
#   make        -> build/repaso_2do_parcial.pdf y build/ejercicios_nuevos.pdf,
#                y build/ejercicios_nuevos_2.pdf
#   make clean  -> borra build/

DOCS := repaso_2do_parcial ejercicios_nuevos ejercicios_nuevos_2

# Fecha del documento para builds reproducibles: 29/oct/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1793242800
export SOURCE_DATE_EPOCH
export FORCE_SOURCE_DATE := 1

BUILD   := build
XELATEX := xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD)

.PHONY: all clean
.DELETE_ON_ERROR:

all: $(DOCS:%=$(BUILD)/%.pdf)

$(BUILD):
	mkdir -p $@

$(BUILD)/%.pdf: %.tex | $(BUILD)
	@$(XELATEX) $< > /dev/null || { grep -A5 '^!' $(BUILD)/$*.log; exit 1; }
	@if grep -q 'Missing character' $(BUILD)/$*.log; then \
		grep 'Missing character' $(BUILD)/$*.log | sort -u; \
		echo "ERROR: caracteres sin glifo en la fuente"; exit 1; fi
	@grep 'Output written' $(BUILD)/$*.log
	@echo "--- Advertencias de LaTeX:"
	@grep -E 'Warning|Overfull|Underfull' $(BUILD)/$*.log || echo "(ninguna)"
	@echo "OK: $@"

clean:
	rm -rf $(BUILD)
