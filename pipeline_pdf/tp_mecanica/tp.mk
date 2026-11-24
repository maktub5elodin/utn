# Perfil «TP Final de Ingeniería Mecánica I»: formato de la cátedra (Times New
# Roman 12, justificado, interlineado 1,15, A4), carátula oficial, notas al pie,
# láminas apaisadas y controles. Un solo .md genera dos entregas (versiones),
# cada una en PDF (principal) y en Word (editable, compatible con Google Docs).
#
# Makefile del documento:
#
#   DOC               := 01_informe                 # el .md, sin extensión
#   SOURCE_DATE_EPOCH := <fecha>                    # builds reproducibles (obligatoria)
#   VALORES_SCRIPT    := valores.py                 # escribe el JSON de valores
#   VALORES_DEPS      := ...                        # de qué depende ese JSON
#   LAMINAS_DIR       := ../06_modelo_2/planos      # PDF de las láminas
#   LAMINAS           := 01_conjunto 02_cabezal     # sin extensión
#   include ../../../pipeline_pdf/tp_mecanica/tp.mk
#
#   make        -> las dos versiones, PDF y Word, con todos los controles
#   make e2     -> PDF de la versión e2 (nombre de salida desde pdf.yaml)
#   make e3     -> PDF de la versión e3
#   make docx   -> Word de las dos versiones
#
# Los datos van en el bloque `tp:` del pdf.yaml (carátula, versiones, límites,
# vocabulario controlado). Requiere LibreOffice (carátula a PDF, paginado del
# índice de Word) y python-docx.

TP    := $(patsubst %/,%,$(dir $(lastword $(MAKEFILE_LIST))))
BUILD := build
AUX   := .build/aux

ifeq ($(VERSION),)
# ── Nivel superior: una sub-make por versión ────────────────────────────

.DEFAULT_GOAL := todo
.PHONY: todo e2 e3 docx clean

todo:
	@$(MAKE) --no-print-directory VERSION=e2 pdf docx
	@$(MAKE) --no-print-directory VERSION=e3 pdf docx
	@python3 $(TP)/controles_tp.py resumen $(AUX)

e2 e3:
	@$(MAKE) --no-print-directory VERSION=$@ pdf

docx:
	@$(MAKE) --no-print-directory VERSION=e2 docx
	@$(MAKE) --no-print-directory VERSION=e3 docx

clean:
	rm -rf $(BUILD) .build

else
# ── Una versión ─────────────────────────────────────────────────────────

SALIDA := $(shell python3 $(TP)/docx_tp.py --nombre pdf.yaml $(VERSION))
ifeq ($(SALIDA),)
$(error No se pudo armar el nombre de salida desde pdf.yaml (¿falta tp.versiones.$(VERSION)?))
endif
export TP_VERSION := $(VERSION)
export TP_SALIDA  := $(SALIDA)

VALORES     := $(AUX)/valores.json
CARATULA    := $(AUX)/caratula_$(VERSION)
LAMINAS_PNG := $(LAMINAS:%=$(AUX)/laminas/%.png)
LO          := soffice --headless -env:UserInstallation=file://$(abspath $(AUX))/lo

PDF_DEFAULTS  := $(TP)/pdf.yaml
DOCX_DEFAULTS := $(TP)/docx.yaml
DOCX_POST      = python3 $(TP)/docx_tp.py armar $@ pdf.yaml $(VERSION) $(CARATULA).docx
DOCX_DEPS     := $(TP)/docx_tp.py $(CARATULA).docx $(LAMINAS_PNG)
PERFIL_DEPS   := $(TP)/tp-mecanica.lua $(TP)/preambulo.tex $(VALORES) $(CARATULA).pdf \
                 $(LAMINAS:%=$(LAMINAS_DIR)/%.pdf) $(if $(RECORTES),$(AUX)/recortes/.hecho)

include $(TP)/../comun.mk

.DEFAULT_GOAL := pdf
.PHONY: pdf

# Controles del PDF y del Word terminados (formato, fuentes, justificado, pie)
pdf: $(BUILD)/$(SALIDA).pdf
	@python3 $(TP)/controles_tp.py pdf $< pdf.yaml $(VERSION)

docx:
	@python3 $(TP)/controles_tp.py docx $(BUILD)/$(SALIDA).docx pdf.yaml $(VERSION)

$(VALORES): $(VALORES_SCRIPT) $(VALORES_DEPS)
	python3 $(VALORES_SCRIPT) $@

# Carátula oficial completada (python-docx); en E3, el Resumen lleva el abstract
$(CARATULA).docx: pdf.yaml $(DOC).md $(TP)/docx_tp.py $(VALORES)
	python3 $(TP)/docx_tp.py caratula pdf.yaml $(VERSION) $(DOC).md $@

$(CARATULA).pdf: $(CARATULA).docx
	$(LO) --convert-to pdf --outdir $(AUX) $< > /dev/null 2>&1
	@test -s $@ || { echo "ERROR: LibreOffice no pudo convertir $<"; exit 1; }
	@test "$$(pdfinfo $@ | sed -n 's/^Pages: *//p')" = 1 || \
	  { echo "ERROR: la carátula ocupa más de una página (¿abstract muy largo para el campo Resumen?)"; rm -f $@; exit 1; }

# Figuras con mucho margen blanco (RECORTES, opcional): copia recortada en
# $(AUX)/recortes/, sin tocar el original; el .md apunta a la copia.
ifneq ($(RECORTES),)
$(AUX)/recortes/.hecho: $(RECORTES)
	mkdir -p $(AUX)/recortes
	python3 -c "import sys; from pathlib import Path; from PIL import Image, ImageOps; \
	[(lambda im: im.crop((lambda b: (max(b[0]-24,0), max(b[1]-24,0), min(b[2]+24,im.width), min(b[3]+24,im.height)))(ImageOps.invert(im).getbbox())).save('$(AUX)/recortes/' + Path(f).name, optimize=True))(Image.open(f).convert('RGB')) for f in sys.argv[1:]]" $(RECORTES)
	touch $@
endif

# Láminas para Word: PNG en escala de grises, 200 ppp sobre A3 (≈ 280 ppp en A4)
$(AUX)/laminas/%.png: $(LAMINAS_DIR)/%.pdf
	mkdir -p $(dir $@)
	pdftoppm -r 200 -gray -png -singlefile $< $(basename $@)

endif
