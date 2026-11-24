# Mezcla de cuatro disoluciones (ejercicio del 2.º parcial): LaTeX directo, igual que hoja_formulas/.
#
#   make        -> build/mezcla_disoluciones.pdf
#   make clean  -> borra build/ y .build/

DOC := mezcla_disoluciones

# Fecha del documento para builds reproducibles: 02/nov/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1793588400
export SOURCE_DATE_EPOCH
export FORCE_SOURCE_DATE := 1

# build/: solo el PDF (versionado). .build/: intermedios (.aux, .log), ignorados.
BUILD   := build
INTER   := .build
XELATEX := xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(INTER)

.PHONY: all clean
.DELETE_ON_ERROR:

all: $(BUILD)/$(DOC).pdf

$(BUILD) $(INTER):
	mkdir -p $@

$(BUILD)/$(DOC).pdf: $(DOC).tex | $(BUILD) $(INTER)
	@$(XELATEX) $< > /dev/null || { grep -A5 '^!' $(INTER)/$(DOC).log; exit 1; }
	@if grep -q 'Missing character' $(INTER)/$(DOC).log; then \
		grep 'Missing character' $(INTER)/$(DOC).log | sort -u; \
		echo "ERROR: caracteres sin glifo en la fuente"; exit 1; fi
	@grep 'Output written' $(INTER)/$(DOC).log
	@echo "--- Advertencias de LaTeX:"
	@grep -E 'Warning|Overfull|Underfull' $(INTER)/$(DOC).log || echo "(ninguna)"
	@mv $(INTER)/$(DOC).pdf $@
	@echo "OK: $@"

clean:
	rm -rf $(BUILD) $(INTER)
