# Cortadora PET, modelo 2.0: verificación del modelo.
#   make     verifica choques, armado en orden, impresión y funcionamiento;
#            después, figuras de vista previa y modelo/cortadora_v2.FCStd
# Termina con error si resultados.json registra alguna falla.
FREECAD := $(HOME)/Aplicaciones/FreeCAD.AppImage
SYSPY   := /usr/bin/python3
export SOURCE_DATE_EPOCH := 1794009600
export FORCE_SOURCE_DATE := 1
MODELO  := parametros.py piezas.py

all: build/.verificado build/.figuras

build/.verificado: $(MODELO) verificar.py
	mkdir -p build
	$(FREECAD) freecadcmd verificar.py > /dev/null 2>&1; grep -q '"fallas": \[\]' resultados.json
	touch $@

build/.figuras: $(MODELO) vista.py build/.verificado
	CARPETA_MODELO=$(CURDIR) QT_QPA_PLATFORM=offscreen $(FREECAD) vista.py > /dev/null 2>&1
	# FreeCAD guarda la hora en el PNG: se quita, para que la misma imagen dé el mismo archivo
	$(SYSPY) -c "import sys; from PIL import Image; [Image.open(f).save(f, optimize=True) for f in sys.argv[1:]]" figuras/*.png
	touch $@

.PHONY: all
