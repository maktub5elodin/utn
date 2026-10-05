# Compila el PDF del TP Mecánica Rotacional 2 a partir del .md (única fuente de
# contenido). Misma estructura que ayga/excercise/Makefile.
#
#   make        -> build/<doc>.tex -> build/<doc>.pdf
#   make clean  -> borra build/ (no toca el .md)
#
# Todavía no hay figuras: los diagramas ASCII del .md salen en el PDF como
# recuadro "Figura pendiente" (filtros/solo-md.lua). Cuando se agreguen, va acá
# la regla figuras/*.pdf + figuras/*.png, como en AyGA.
#
# Usa el pandoc y xelatex del sistema. Detiene la compilación si queda alguna
# referencia sin resolver o algún carácter que la fuente no tiene.

DOC     := Mecanica_Rotacional_2_Resolucion
BUILD   := build
FILTROS := $(wildcard filtros/*.lua)
XELATEX := xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD)

# Builds reproducibles: fecha fija (5/oct/2026 00:00 -03, la del documento) en
# vez de la hora de compilación, para que el PDF versionado salga idéntico byte
# a byte si el contenido no cambió (sin cambios falsos en git).
export SOURCE_DATE_EPOCH := 1791169200
export FORCE_SOURCE_DATE := 1

.PHONY: all clean

# Si un paso falla, se borra su salida: nunca queda un PDF "a medias" que
# make considere actualizado.
.DELETE_ON_ERROR:

all: $(BUILD)/$(DOC).pdf

$(BUILD):
	mkdir -p $@

$(BUILD)/$(DOC).tex: $(DOC).md pdf.yaml $(FILTROS) | $(BUILD)
	pandoc --defaults=pdf.yaml $(DOC).md -o $@

# Pasadas de xelatex hasta que LaTeX deja de pedir "Rerun" (máx. 4), y siempre
# al menos 2: la primera escribe .aux/.toc, la segunda arma el índice.
# "Rerun" cubre los dos avisos: "Rerun to get..." (referencias) y "Rerun
# LaTeX" (anchos de longtable).
$(BUILD)/$(DOC).pdf: $(BUILD)/$(DOC).tex
	@for i in 1 2 3 4; do \
		echo "xelatex, pasada $$i"; \
		$(XELATEX) $< > /dev/null || { grep -A5 '^!' $(BUILD)/$(DOC).log; exit 1; }; \
		if [ $$i -ge 2 ] && ! grep -qE 'Rerun to get|Rerun LaTeX' $(BUILD)/$(DOC).log; then break; fi; \
	done
	@if grep -qE 'undefined|Rerun to get|Rerun LaTeX' $(BUILD)/$(DOC).log; then \
		grep -E 'undefined|Rerun to get|Rerun LaTeX' $(BUILD)/$(DOC).log; \
		echo "ERROR: referencias sin resolver (ver arriba)"; exit 1; fi
	@if grep -q 'Missing character' $(BUILD)/$(DOC).log; then \
		grep 'Missing character' $(BUILD)/$(DOC).log | sort -u; \
		echo "ERROR: caracteres sin glifo en la fuente (ver arriba)"; exit 1; fi
	@echo "--- Advertencias de LaTeX:"
	@grep -E 'Warning|Overfull|Underfull' $(BUILD)/$(DOC).log || echo "(ninguna)"
	@echo "OK: $@"

clean:
	rm -rf $(BUILD)
