# Modelo 3D de la cortadora: qué encontró

Modelo de FreeCAD del mecanismo que describe la Entrega 2 (E2), simulado en todo el recorrido. **Es material de estudio para que el grupo decida.** No cambia la Entrega 2 ni la presentación.

![](figuras/conjunto_inicio.png)

## 1. Qué se puede confiar y qué no

- **Sale de E2:** la disposición (tuerca y cuchilla fijas a la base; soporte del cuello, rodillo, engranajes y husillo sobre el carro), el corte desde el borde abierto hacia el cuello y la ecuación `a = L·Db/(i·Dr)`.
- **Son supuestos:** casi todas las medidas. E2 no las define todavía. En [parametros.py](parametros.py) cada valor indica su origen: `[E2]`, `[DXF]`, `[REF]` (valor de referencia de la lámina 10) o `[SUP]` (supuesto de este modelo).
- **Qué se verificó:** geometría y cinemática. Se comprobó que las piezas no choquen en 13 posiciones del recorrido, y que los dientes reales engranen con 20/40. Como control, los mismos dientes con una relación equivocada sí se pisan.
- **Qué no se verificó:** fuerzas, fricción, deformación de la botella ni calidad del corte. Eso solo lo responde el prototipo. El paso medido en la simulación (7,04 mm) coincide con la ecuación porque la simulación usa las mismas relaciones: confirma que el modelo es coherente, no que la máquina real dé ese paso.
- **El recorrido de la tira es ilustrativo.** E2 solo pide una salida libre.

## 2. Hallazgos

### 2.1 La manivela no puede ir del lado del cuerpo de la botella

E2 une la manivela al eje del rodillo, pero no dice de qué lado. El eje del rodillo queda a `Dr/2` = **25 mm** de la pared. Con un mango de radio 12 mm, del lado del cuerpo la manivela no podría tener más de **13 mm** de radio. Con 70 mm de radio, la manivela barre **unos 283 000 mm³ dentro de la botella**.

La imagen IA parece mostrarla de ese lado. Se ve bien porque es una foto de una sola posición: al girar, chocaría.

![](figuras/hallazgo_choque_manivela.png)

En el modelo, el eje se prolonga más allá del soporte del cuello y la manivela queda detrás. Así no hay choque, pero el eje llega a 149 mm de largo. **A decidir:** esta solución, un reenvío, u otra posición de entrada.

### 2.2 Los rodamientos del eje no entran junto al rodillo

Un rodamiento para eje Ø30 mide cerca de Ø55 (se tomó el 6006, medida a confirmar con catálogo). Su radio de 27,5 mm no entra en los 25 mm disponibles sobre el cuerpo. Por eso el rodillo queda **en voladizo, a 24 mm** del último apoyo, y la placa de ese apoyo pasa a solo **1,5 mm** del hombro de la botella.

**A confirmar:** si el Ø30 del DXF es realmente este eje. Un eje más fino alivia este punto y el siguiente.

### 2.3 El eje Ø30 condiciona los engranajes

Un piñón de 20 dientes tiene el fondo del diente en `m·(z − 2,5)`. Con módulo 1,5 mide 26,25 mm, menos que el eje. Recién con **módulo 2** (fondo de 35 mm) queda material: 2,5 mm de pared. Eso fija 60 mm entre ejes y un engranaje conducido de Ø84.

### 2.4 Los sentidos de giro ya quedan determinados

E2 pide comprobarlos. Con el carro avanzando hacia el borde abierto y la tuerca fija:

| Elemento | Resultado |
|---|---|
| Rosca del husillo | Derecha, la más común |
| Manivela, vista desde el borde abierto | Sentido horario |
| Botella y husillo | Giran en el mismo sentido (dos inversiones) |
| Pared en la cuchilla, con la cuchilla del lado opuesto al rodillo | Baja: el filo mira hacia arriba y la tira sale hacia abajo |

Con una rosca izquierda, habría que girar la manivela al revés, y la cuchilla tendría que invertirse.

![](figuras/detalle_cuchilla.png)

### 2.5 La máquina es bastante más larga que su base

| Medida | Valor |
|---|---|
| Base | 380 mm |
| Husillo | 264 mm |
| Largo total, del mango al extremo del husillo al final del corte | **570 mm** |
| Husillo que sobresale de la base al final | 158 mm |

Es el "espacio libre para el recorrido" que pide E2, ya con un número. La botella, en cambio, no avanza más allá de la cuchilla: se va consumiendo a medida que el carro avanza.

Al inicio, la botella queda sostenida solo del cuello, con **269 mm en voladizo**, y el rodillo la empuja de costado. Refuerza la pregunta de E2 sobre los apoyos complementarios.

### 2.6 Una idea para adaptar otras botellas: pivotar la caja sobre el husillo

E2 pide que la regulación del rodillo sea compatible con la distancia entre ejes. Si las dos placas que sostienen ambos ejes pivotan **alrededor del husillo**, el rodillo se acerca o se aleja de la botella y los engranajes no se separan.

| Db (mm) | Ángulo de la caja respecto de la línea husillo-botella | `a` (mm/vuelta) |
|---|---:|---:|
| 65 | 17,5° | 5,2 |
| 75 | 24,6° | 6,0 |
| 88 | 32,3° | 7,04 |
| 100 | 38,7° | 8,0 |
| 110 | 43,7° | 8,8 |

Alcanza con unos **26° de giro** para ese rango de diámetros, que también es supuesto. Dos límites:

- El paso `a` sigue cambiando con `Db`: para mantener el ancho hacen falta los engranajes intercambiables de E2.
- Es una propuesta mía: solo calculé el alcance. No simulé choques para otros diámetros, ni la fijación de la caja.

## 3. Cómo se usa

```
make          # verifica; genera STEP, planos auditados, figuras y modelo/cortadora_pet.FCStd
make video    # además, salida/cortadora_pet.mp4
```

Se cambia una medida en `parametros.py` y se vuelve a correr. Si el cambio genera un choque, `make` termina con error y `resultados.json` indica qué piezas se tocan y en qué posición del carro. Las piezas son formas fijas generadas por Python: para modificarlas se edita el código, no el `.FCStd`.

| Archivo | Qué es |
|---|---|
| `parametros.py` | Medidas con su origen y cinemática |
| `piezas.py` | Sólidos de cada pieza |
| `verificar.py` | Choques, engrane, paso y sentidos, sin ventana |
| `renderizar.py` | Figuras y video |
| `exportar_step.py` | `salida/cortadora_pet.step` para SolidWorks: 22 sólidos con nombre y color, en la posición inicial. Lo reabre y compara sólidos y volumen. La tira queda afuera |
| `planos.py`, `dibujo.py` | Proyectan el modelo y arman las cuatro láminas A3. Falla si dos textos se superponen |
| `dxf.py` | Escribe `planos/*.dxf` (R2000) con `ezdxf`, en el Python del sistema |
| `a_pdf.sh` | DXF a PDF con LibreCAD, en negro |
| `control_dxf.py` | Audita cada DXF con `ezdxf`, lo dibuja con un segundo lector y compara. `make` falla si hay errores |
| `resultados.json` | Números de la última verificación |

## 4. Normas de los planos

Los planos siguen las normas IRAM como norma de aplicación, a nivel de cursada: líneas, márgenes, escala, letra, método E y representación convencional de engranajes y roscas. El rótulo es un bloque simple de cursada. El relevamiento de normas ISO e IRAM, con sus fuentes y lo que quedó sin confirmar, está en [normas_detalle.md](normas_detalle.md), para cuando el proyecto lo necesite.

---
*Fuentes: `03_entrega_2/Entrega_2_Reentrega_0_S1091_Grupo_1.pdf` (secciones 5.1 a 5.5), `04_material_grafico/Proy Mecanica.dxf`, `04_material_grafico/imagen_ia_conjunto_rodillo_marcado.jpeg`, `05_presentacion/contradicciones_y_supuestos.md`, `sistemas_de_representacion/01_materiales_y_normas_iram.md` y `sistemas_de_representacion/CLASE 3.pdf`. Método de trabajo tomado de `~/FreeCAD/macros/`.*
