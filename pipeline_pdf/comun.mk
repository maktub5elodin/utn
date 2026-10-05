# Reglas comunes para compilar un .md a PDF (pandoc + xelatex).
#
# Cada documento tiene un Makefile corto que define sus variables y después
# incluye este archivo:
#
#   DOC               := nombre_del_md_sin_extension
#   SOURCE_DATE_EPOCH := <fecha del documento, en segundos>   (obligatoria)
#   FIG_SCRIPT        := figuras_xxx.py                       (opcional)
#   FIG_NAMES         := fig1_a fig2_b                         (opcional)
#   include ../../pipeline_pdf/comun.mk
#
# y su pdf.yaml con título, subtítulo y fecha. La configuración común de pandoc
# está en base.yaml, junto a este archivo.
#
#   make          -> figuras (si hay) -> build/<doc>.tex -> build/<doc>.pdf
#   make figuras  -> solo regenera las figuras
#   make clean    -> borra build/ (no toca figuras/ ni el .md)
#
# Usa el python3, pandoc y xelatex del sistema. Detiene la compilación si queda
# alguna referencia sin resolver o algún carácter que la fuente no tiene.

PIPELINE := $(patsubst %/,%,$(dir $(lastword $(MAKEFILE_LIST))))
BUILD    := build
FILTROS  := $(wildcard $(PIPELINE)/filtros/*.lua)
XELATEX  := xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD)

ifndef DOC
$(error Falta definir DOC en el Makefile del documento)
endif

# Builds reproducibles: fecha fija en vez de la hora de compilación, para que el
# PDF y los PNG versionados salgan idénticos byte a byte si el contenido no
# cambió (sin cambios falsos en git). La usan xelatex (también el que llama
# matplotlib para las figuras).
ifndef SOURCE_DATE_EPOCH
$(error Falta definir SOURCE_DATE_EPOCH (fecha del documento) en el Makefile)
endif
export SOURCE_DATE_EPOCH
export FORCE_SOURCE_DATE := 1

FIGS := $(foreach n,$(FIG_NAMES),figuras/$(n).pdf figuras/$(n).png)

.PHONY: all figuras clean

# Si un paso falla, se borra su salida: nunca queda un PDF "a medias" que
# make considere actualizado.
.DELETE_ON_ERROR:

all: $(BUILD)/$(DOC).pdf

figuras: $(FIGS)

ifneq ($(FIGS),)
$(FIGS) &: $(FIG_SCRIPT)
	python3 $(FIG_SCRIPT)
endif

$(BUILD):
	mkdir -p $@

$(BUILD)/$(DOC).tex: $(DOC).md pdf.yaml $(PIPELINE)/base.yaml $(FILTROS) $(FIGS) | $(BUILD)
	pandoc --defaults=$(PIPELINE)/base.yaml --defaults=pdf.yaml $(DOC).md -o $@

# Pasadas de xelatex hasta que LaTeX deja de pedir "Rerun" (máx. 4), y siempre
# al menos 2: la primera escribe .aux/.toc, la segunda arma el índice. Se buscan
# los dos avisos: "Rerun to get..." (referencias) y "Rerun LaTeX" (anchos de
# longtable).
$(BUILD)/$(DOC).pdf: $(BUILD)/$(DOC).tex $(FIGS)
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
