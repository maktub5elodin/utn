# Los tres documentos para el grupo, en PDF para imprimir: `make` arma los tres.
# Cada uno tiene su carpeta con su Makefile y su pdf.yaml (pipeline_pdf/comun.mk);
# el preámbulo común está en preambulo.tex.

DOCS := reparto_y_defensa guia_lectura_planos contradicciones_y_supuestos

.PHONY: all clean $(DOCS)

all: $(DOCS)

$(DOCS):
	$(MAKE) -C $@

clean:
	for d in $(DOCS); do $(MAKE) -C $$d clean; done
