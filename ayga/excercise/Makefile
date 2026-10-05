# Compila el PDF del TP 7, Ej. 1 b) a partir del .md (única fuente de contenido).
#
#   make         -> figuras (PDF + PNG) -> build/<doc>.tex -> build/<doc>.pdf
#   make figuras -> solo regenera las figuras
#   make clean   -> borra build/ (no toca figuras/ ni el .md)
#
# Usa el python3, pandoc y xelatex del sistema. Detiene la compilación si queda
# alguna referencia o cita sin resolver.

DOC     := tp7_ej1b_parametrizacion_elipse
BUILD   := build
NOMBRES := fig1_elipse_arco fig2_circunferencia_auxiliar fig3_phi_vs_theta fig4_hipotesis
FIGS    := $(foreach n,$(NOMBRES),figuras/$(n).pdf figuras/$(n).png)
FILTROS := $(wildcard filtros/*.lua)
XELATEX := xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD)

# Builds reproducibles: fecha fija (3/oct/2026 00:00 -03, la del documento) en
# vez de la hora de compilación, para que el PDF y los PNG versionados salgan
# idénticos byte a byte si el contenido no cambió (sin cambios falsos en git).
# La usan xelatex (también el que llama matplotlib para las figuras).
export SOURCE_DATE_EPOCH := 1790996400
export FORCE_SOURCE_DATE := 1

.PHONY: all figuras clean

# Si un paso falla, se borra su salida: nunca queda un PDF "a medias" que
# make considere actualizado.
.DELETE_ON_ERROR:

all: $(BUILD)/$(DOC).pdf

figuras: $(FIGS)

$(FIGS) &: figuras_tp7_ej1b.py
	python3 figuras_tp7_ej1b.py

$(BUILD):
	mkdir -p $@

$(BUILD)/$(DOC).tex: $(DOC).md pdf.yaml $(FILTROS) $(FIGS) | $(BUILD)
	pandoc --defaults=pdf.yaml $(DOC).md -o $@

# Pasadas de xelatex hasta que LaTeX deja de pedir "Rerun" (máx. 4): la primera
# escribe .aux/.toc, las siguientes resuelven \ref e índice.
$(BUILD)/$(DOC).pdf: $(BUILD)/$(DOC).tex $(FIGS)
	@for i in 1 2 3 4; do \
		echo "xelatex, pasada $$i"; \
		$(XELATEX) $< > /dev/null || { grep -A5 '^!' $(BUILD)/$(DOC).log; exit 1; }; \
		grep -q 'Rerun to get' $(BUILD)/$(DOC).log || break; \
	done
	@if grep -qE 'undefined|Rerun to get' $(BUILD)/$(DOC).log; then \
		grep -E 'undefined|Rerun to get' $(BUILD)/$(DOC).log; \
		echo "ERROR: referencias sin resolver (ver arriba)"; exit 1; fi
	@echo "--- Advertencias de LaTeX:"
	@grep -E 'Warning|Overfull|Underfull' $(BUILD)/$(DOC).log || echo "(ninguna)"
	@echo "OK: $@"

clean:
	rm -rf $(BUILD)
