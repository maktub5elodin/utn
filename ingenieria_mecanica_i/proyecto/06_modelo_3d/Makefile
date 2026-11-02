# Cortadora PET: modelo, verificación, STEP, planos, figuras y video.
#   make             verifica; genera STEP, planos (DXF y PDF), figuras y el .FCStd
#   make video       además, video MP4 (unos minutos)
# Solo se rehace lo que cambió: un cambio en parametros.py regenera todo menos el video.
FREECAD := $(HOME)/Aplicaciones/FreeCAD.AppImage
SYSPY   := /usr/bin/python3
TANDAS  := 3
CUADROS := 1080
GUI     := CARPETA_MODELO=$(CURDIR) QT_QPA_PLATFORM=offscreen
MODELO  := parametros.py piezas.py
LAMINAS := 01_conjunto 02_despiece 03_esquema_cinematico 04_hallazgo_manivela
DXF     := $(LAMINAS:%=planos/%.dxf)
PDF     := $(LAMINAS:%=planos/%.pdf)
STEP    := salida/cortadora_pet.step
export SOURCE_DATE_EPOCH := 1793577600
export FORCE_SOURCE_DATE := 1

all: build/.verificado $(STEP) $(DXF) $(PDF) build/.auditado build/.figuras

build/.verificado: $(MODELO) verificar.py
	mkdir -p build
	$(FREECAD) freecadcmd verificar.py > /dev/null 2>&1; grep -q '"fallas": \[\]' resultados.json
	touch $@

# Termina con error si al reabrirlo no coinciden sólidos, volumen o nombres.
$(STEP): $(MODELO) exportar_step.py build/.verificado
	$(GUI) $(FREECAD) exportar_step.py > /dev/null 2>&1
	touch $@

# FreeCAD proyecta y anota; ezdxf, en el Python del sistema, escribe los DXF.
# Falla si dos textos se superponen o si ezdxf encuentra errores.
$(DXF) &: $(MODELO) planos.py dibujo.py dxf.py build/.verificado
	$(FREECAD) freecadcmd planos.py > /dev/null 2>&1
	$(SYSPY) dxf.py

$(PDF) &: $(DXF) a_pdf.sh
	./a_pdf.sh

# Auditoría independiente y comparación entre LibreCAD y ezdxf.
build/.auditado: $(PDF) control_dxf.py
	$(SYSPY) control_dxf.py
	touch $@

build/.figuras: $(MODELO) renderizar.py build/.verificado
	$(GUI) RENDER=figuras $(FREECAD) renderizar.py > /dev/null 2>&1
	rm -f modelo/*.FCBak
	touch $@

# Varias instancias a la vez a veces se caen al guardar la imagen (driver gráfico):
# cada ronda retoma los cuadros que faltan, y sin los 1080 no se arma el video.
video: build/.verificado renderizar.py
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

.PHONY: all video
