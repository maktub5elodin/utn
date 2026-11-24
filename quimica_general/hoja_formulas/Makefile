# Hoja de fórmulas de Química General: LaTeX directo (no pasa por pandoc ni por
# pipeline_pdf/, porque necesita control fino del espacio: una carilla, 3 columnas).
#
#   make        -> build/hoja_formulas.pdf
#   make clean  -> borra build/ y .build/

DOC := hoja_formulas

# Fecha del documento para builds reproducibles: 26/oct/2026 00:00 -03.
SOURCE_DATE_EPOCH := 1792983600
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

# Además de compilar, verifica que la hoja siga entrando en una sola carilla.
$(BUILD)/$(DOC).pdf: $(DOC).tex | $(BUILD) $(INTER)
	@$(XELATEX) $< > /dev/null || { grep -A5 '^!' $(INTER)/$(DOC).log; exit 1; }
	@if grep -q 'Missing character' $(INTER)/$(DOC).log; then \
		grep 'Missing character' $(INTER)/$(DOC).log | sort -u; \
		echo "ERROR: caracteres sin glifo en la fuente"; exit 1; fi
	@if ! grep -q 'Output written on .*(1 page' $(INTER)/$(DOC).log; then \
		grep 'Output written' $(INTER)/$(DOC).log; \
		echo "ERROR: la hoja pasó de una carilla"; exit 1; fi
	@echo "--- Advertencias de LaTeX:"
	@grep -E 'Warning|Overfull|Underfull' $(INTER)/$(DOC).log || echo "(ninguna)"
	@mv $(INTER)/$(DOC).pdf $@
	@echo "OK: $@"

clean:
	rm -rf $(BUILD) $(INTER)
