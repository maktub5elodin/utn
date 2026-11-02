# Cortadora PET: modelo, verificación, figuras y video.
#   make             verifica y genera figuras y el modelo .FCStd
#   make video       además, video MP4 (unos minutos)
FREECAD := $(HOME)/Aplicaciones/FreeCAD.AppImage
TANDAS  := 3
CUADROS := 1080
GUI     := CARPETA_MODELO=$(CURDIR) QT_QPA_PLATFORM=offscreen

all: resultados.json figuras

resultados.json: parametros.py piezas.py verificar.py
	$(FREECAD) freecadcmd verificar.py > /dev/null 2>&1; grep -q '"fallas": \[\]' resultados.json

figuras: resultados.json renderizar.py
	$(GUI) RENDER=figuras $(FREECAD) renderizar.py > /dev/null 2>&1

# Varias instancias a la vez a veces se caen al guardar la imagen (driver gráfico):
# cada ronda retoma los cuadros que faltan, y sin los 1080 no se arma el video.
video: resultados.json renderizar.py
	mkdir -p build/cuadros
	for ronda in 1 2 3 4 5 6 7 8 9 10 11 12; do \
	  rm -f build/cuadros/*.crudo.png build/cuadros/*.tmp.png; \
	  [ $$(ls build/cuadros | wc -l) -ge $(CUADROS) ] && break; \
	  for k in $$(seq 0 $$(($(TANDAS)-1))); do \
	    $(GUI) RENDER=video TANDA=$$k/$(TANDAS) $(FREECAD) renderizar.py > /dev/null 2>&1 & \
	  done; wait; \
	done
	rm -f build/cuadros/*.crudo.png build/cuadros/*.tmp.png
	test $$(ls build/cuadros | wc -l) -eq $(CUADROS)
	mkdir -p salida
	ffmpeg -y -loglevel error -framerate 30 -i build/cuadros/%04d.png -c:v libx264 -preset slow \
	  -crf 20 -pix_fmt yuv420p -movflags +faststart salida/cortadora_pet.mp4

.PHONY: all figuras video
