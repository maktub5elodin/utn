# Repaso 2do Parcial de Química General: LaTeX directo, igual que hoja_formulas/.
#
#   make        -> build/repaso_2do_parcial.pdf y build/ejercicios_nuevos.pdf,
#                y build/ejercicios_nuevos_2.pdf
#   make clean  -> borra build/ y .build/

DOCS := repaso_2do_parcial ejercicios_nuevos ejercicios_nuevos_2

# Fecha del documento para builds reproducibles: 29/oct/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1793242800
export SOURCE_DATE_EPOCH
export FORCE_SOURCE_DATE := 1

# build/: solo el PDF (versionado). .build/: intermedios (.aux, .log), ignorados.
BUILD   := build
INTER   := .build
XELATEX := xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(INTER)

.PHONY: all clean
.DELETE_ON_ERROR:

all: $(DOCS:%=$(BUILD)/%.pdf)

$(BUILD) $(INTER):
	mkdir -p $@

$(BUILD)/%.pdf: %.tex | $(BUILD) $(INTER)
	@$(XELATEX) $< > /dev/null || { grep -A5 '^!' $(INTER)/$*.log; exit 1; }
	@if grep -q 'Missing character' $(INTER)/$*.log; then \
		grep 'Missing character' $(INTER)/$*.log | sort -u; \
		echo "ERROR: caracteres sin glifo en la fuente"; exit 1; fi
	@grep 'Output written' $(INTER)/$*.log
	@echo "--- Advertencias de LaTeX:"
	@grep -E 'Warning|Overfull|Underfull' $(INTER)/$*.log || echo "(ninguna)"
	@mv $(INTER)/$*.pdf $@
	@echo "OK: $@"

clean:
	rm -rf $(BUILD) $(INTER)
