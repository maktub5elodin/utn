# Reglas comunes para compilar un .md a PDF (pandoc + xelatex).
#
# Cada documento tiene un Makefile corto que define sus variables y después
# incluye este archivo:
#
#   DOC               := nombre_del_md_sin_extension
#   SOURCE_DATE_EPOCH := <fecha del documento, en segundos>   (obligatoria)
#   FIG_SCRIPT        := figuras_xxx.py                       (opcional)
#   FIG_NAMES         := fig1_a fig2_b                         (opcional)
#   DOCX_ESCALA       := 0.75   (opcional: tamaño de las figuras en Word)
#   include ../../pipeline_pdf/comun.mk
#
# y su pdf.yaml con título, subtítulo y fecha. La configuración común de pandoc
# está en base.yaml, junto a este archivo.
#
#   make          -> figuras (si hay) -> build/<doc>.tex -> build/<doc>.pdf
#   make docx     -> build/<doc>.docx (Word, sin la estética de LaTeX; no se versiona)
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

# Perfiles (ej. lab_fisica/lab.mk) pueden cambiar el nombre de salida y la
# configuración de pandoc antes de incluir este archivo. Por defecto:
# build/<DOC>.pdf con base.yaml, y Word con docx.yaml + docx_estilo.py.
SALIDA        ?= $(DOC)
PDF_DEFAULTS  ?= $(PIPELINE)/base.yaml
DOCX_DEFAULTS ?= $(PIPELINE)/docx.yaml
DOCX_POST     ?= python3 $(PIPELINE)/docx_estilo.py $@ $(DOCX_ESCALA)
DOCX_DEPS     ?= $(PIPELINE)/docx_estilo.py
PERFIL_DEPS   ?=

.PHONY: all docx figuras clean

# Si un paso falla, se borra su salida: nunca queda un PDF "a medias" que
# make considere actualizado.
.DELETE_ON_ERROR:

all: $(BUILD)/$(SALIDA).pdf

docx: $(BUILD)/$(SALIDA).docx

figuras: $(FIGS)

ifneq ($(FIGS),)
$(FIGS) &: $(FIG_SCRIPT)
	python3 $(FIG_SCRIPT)
endif

$(BUILD):
	mkdir -p $@

$(BUILD)/$(SALIDA).tex: $(DOC).md pdf.yaml $(PDF_DEFAULTS) $(FILTROS) $(PERFIL_DEPS) $(FIGS) | $(BUILD)
	pandoc --defaults=$(PDF_DEFAULTS) --defaults=pdf.yaml $(DOC).md -o $@

# Pasadas de xelatex hasta que LaTeX deja de pedir "Rerun" (máx. 4), y siempre
# al menos 2: la primera escribe .aux/.toc, la segunda arma el índice. Se buscan
# los dos avisos: "Rerun to get..." (referencias) y "Rerun LaTeX" (anchos de
# longtable).
$(BUILD)/$(SALIDA).pdf: $(BUILD)/$(SALIDA).tex $(FIGS)
	@for i in 1 2 3 4; do \
		echo "xelatex, pasada $$i"; \
		$(XELATEX) $< > /dev/null || { grep -A5 '^!' $(BUILD)/$(SALIDA).log; exit 1; }; \
		if [ $$i -ge 2 ] && ! grep -qE 'Rerun to get|Rerun LaTeX' $(BUILD)/$(SALIDA).log; then break; fi; \
	done
	@if grep -qE 'undefined|Rerun to get|Rerun LaTeX' $(BUILD)/$(SALIDA).log; then \
		grep -E 'undefined|Rerun to get|Rerun LaTeX' $(BUILD)/$(SALIDA).log; \
		echo "ERROR: referencias sin resolver (ver arriba)"; exit 1; fi
	@if grep -q 'Missing character' $(BUILD)/$(SALIDA).log; then \
		grep 'Missing character' $(BUILD)/$(SALIDA).log | sort -u; \
		echo "ERROR: caracteres sin glifo en la fuente (ver arriba)"; exit 1; fi
	@echo "--- Advertencias de LaTeX:"
	@grep -E 'Warning|Overfull|Underfull' $(BUILD)/$(SALIDA).log || echo "(ninguna)"
	@echo "OK: $@"

# Word: mismo .md y mismos filtros de contenido, configuración en docx.yaml.
# Fórmulas como ecuaciones nativas de Word; figuras en PNG.
$(BUILD)/$(SALIDA).docx: $(DOC).md pdf.yaml $(DOCX_DEFAULTS) $(DOCX_DEPS) $(FILTROS) $(PERFIL_DEPS) $(FIGS) | $(BUILD)
	pandoc --defaults=$(DOCX_DEFAULTS) --defaults=pdf.yaml $(DOC).md -o $@
	$(DOCX_POST)
	@echo "OK: $@"

clean:
	rm -rf $(BUILD)

# Logos compartidos (logos/): cada <logo>.tex (TikZ vectorial) con su
# <logo>_png.tex se pasa a PNG a 1200 ppp una sola vez, en logos/build/, y lo
# reutiliza todo documento que lo pida (ej. LOGO_PNG en lab_fisica/lab.mk).
# No se versiona; `make clean` de un documento no lo borra.
LOGOS := $(PIPELINE)/logos

$(LOGOS)/build/%.png: $(LOGOS)/%.tex $(LOGOS)/%_png.tex
	mkdir -p $(LOGOS)/build
	cd $(LOGOS) && xelatex -interaction=nonstopmode -halt-on-error \
		-output-directory=build $*_png.tex > /dev/null
	pdftoppm -r 1200 -png -singlefile $(LOGOS)/build/$*_png.pdf $(LOGOS)/build/$*
