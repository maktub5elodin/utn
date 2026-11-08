# Cortadora PET, modelo 2.0: verificación del modelo.
#   make     verifica choques, armado en orden, impresión y funcionamiento;
#            después, figuras de vista previa, modelo/cortadora_v2.FCStd,
#            un STL por pieza impresa, y los PDF de la ficha de impresión, la lista de
#            compras, la hoja de la prueba 1 y el instructivo de armado con su plantilla
# Termina con error si resultados.json registra alguna falla.
FREECAD := $(HOME)/Aplicaciones/FreeCAD.AppImage
SYSPY   := /usr/bin/python3
export SOURCE_DATE_EPOCH := 1794009600
export FORCE_SOURCE_DATE := 1
MODELO  := parametros.py piezas.py

all: build/.verificado build/.figuras build/.stl ficha_pdf compras_pdf prueba1_pdf armado_pdf

build/.verificado: $(MODELO) armado.py verificar.py
	mkdir -p build
	$(FREECAD) freecadcmd verificar.py > /dev/null 2>&1; grep -q '"fallas": \[\]' resultados.json
	touch $@

build/.figuras: $(MODELO) vista.py build/.verificado
	CARPETA_MODELO=$(CURDIR) QT_QPA_PLATFORM=offscreen $(FREECAD) vista.py > /dev/null 2>&1
	# FreeCAD guarda la hora en el PNG: se quita, para que la misma imagen dé el mismo archivo
	$(SYSPY) -c "import sys; from PIL import Image; [Image.open(f).save(f, optimize=True) for f in sys.argv[1:]]" figuras/*.png ficha/miniaturas/*.png
	rm -f modelo/*.FCBak
	touch $@

# Cada STL se relee: cerrado, apoyado en la cama y con el volumen de la pieza.
build/.stl: $(MODELO) exportar_stl.py build/.verificado
	$(FREECAD) freecadcmd exportar_stl.py > /dev/null 2>&1; \
	  $(SYSPY) -c "import json,sys; sys.exit(1 if json.load(open('resultados.json'))['stl']['fallas'] else 0)"
	touch $@

# Video corto (make video). Varias instancias a la vez a veces se caen al guardar la
# imagen: cada ronda retoma los cuadros que faltan, y sin todos no se arma el video.
TANDAS  := 3
CUADROS := 750
video: build/.verificado renderizar.py
	mkdir -p build/cuadros
	find build/cuadros -name '*.png' ! -newer renderizar.py -delete
	for ronda in 1 2 3 4 5 6 7 8 9 10; do \
	  rm -f build/cuadros/*.crudo.png build/cuadros/*.tmp.png; \
	  [ $$(ls build/cuadros | wc -l) -ge $(CUADROS) ] && break; \
	  for k in $$(seq 0 $$(($(TANDAS)-1))); do \
	    CARPETA_MODELO=$(CURDIR) QT_QPA_PLATFORM=offscreen RENDER=video TANDA=$$k/$(TANDAS) $(FREECAD) renderizar.py > /dev/null 2>&1 & \
	  done; wait; \
	done
	rm -f build/cuadros/*.crudo.png build/cuadros/*.tmp.png
	test $$(ls build/cuadros | wc -l) -eq $(CUADROS)
	mkdir -p salida
	ffmpeg -y -loglevel error -framerate 30 -i build/cuadros/%04d.png -c:v libx264 -preset slow \
	  -crf 22 -pix_fmt yuv420p -movflags +faststart -map_metadata -1 -fflags +bitexact \
	  -flags:v +bitexact salida/cortadora_v2.mp4

# PDF de la ficha (A4 apaisado), del mismo .md que escribe exportar_stl.py.
ficha_pdf: build/.stl build/.figuras
	$(MAKE) -C ficha

# PDF de la lista de compras (A4 vertical), del .md que escribe exportar_stl.py.
compras_pdf: build/.stl
	$(MAKE) -C compras

# Hoja de la prueba 1 (medir el tiro), con los umbrales de parametros.py.
prueba1_pdf:
	$(MAKE) -C prueba_1

# Instructivo de armado (A4) y plantilla de perforación de la base (A3). Primero las
# vistas de cada paso y las medidas del modelo; después el .md y los PDF.
build/.armado: $(MODELO) armado.py vistas_armado.py build/.verificado
	CARPETA_MODELO=$(CURDIR) QT_QPA_PLATFORM=offscreen $(FREECAD) vistas_armado.py > /dev/null 2>&1
	touch $@

armado_pdf: build/.armado build/.stl build/.figuras
	$(MAKE) -C instructivo

.PHONY: all video ficha_pdf compras_pdf prueba1_pdf armado_pdf
