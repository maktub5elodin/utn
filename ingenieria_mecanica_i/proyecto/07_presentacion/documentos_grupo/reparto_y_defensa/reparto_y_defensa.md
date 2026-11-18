# Reparto de la exposición y preparación de la defensa

Exposición del **jueves 19/11/2026**: 15 minutos, 6 expositores, con proyector y **la máquina en vivo**. El texto completo de cada orador está en las notas de cada lámina de la presentación. Este documento es el resumen para ensayar y para preparar las preguntas del jurado.

<!-- solo-md -->

> **Mantenimiento:** la presentación sale de `07_presentacion/generar_presentacion.py`; los tiempos y oradores los controla `verificar_presentacion.py`. Este `.md` se compila a PDF para el grupo con `make` en `documentos_grupo/` (lo que está entre marcadores `solo-md` no llega al PDF).

<!-- /solo-md -->

## 1. Quién dice qué

| Lám. | Tema | Quién | Tiempo | Hasta | Qué tiene que quedar claro |
|---|-------|------|----|----|-----------------|
| 1 | Portada | Camila | 0:15 | 0:15 | Quiénes somos; trajimos la máquina funcionando |
| 2 | El problema | Camila | 0:45 | 1:00 | A mano, la tira depende de la habilidad. La pregunta del trabajo |
| 3 | Objetivo | Camila | 0:35 | 1:35 | Objetivo principal y los cinco secundarios |
| 4 | Antecedentes | Camila | 0:40 | 2:15 | El ancho irregular es el problema conocido; nuestra respuesta es más simple. Pasa a Sergio |
| 5 | Modelo 1 | Sergio | 0:50 | 3:05 | Qué era y los dos motivos del descarte. Iteración normal de diseño |
| 6 | Principio del 2.0 | Sergio | 1:10 | 4:15 | La tira tira de la botella; la guía fija el paso; nada depende de la fricción |
| 7 | Cabezal | Martín | 0:55 | 5:10 | $w$ = espesor del calce; ranura de 0,85 mm; chapita de metal (en el prototipo falta) |
| 8 | Cuentas clave | Martín | 1:05 | 6:15 | $F = T\cdot r/R$: manivela directa, 13 N; la tira aguanta 124 N. **El tiro de 40 N es un supuesto** |
| 9 | Modelo 3D | Martín | 0:40 | 6:55 | Qué se comprobó en el modelo antes de imprimir |
| 10 | Impresión | Matías | 0:45 | 7:40 | 14 piezas en PLA (~4 h, ~150 g), por qué PLA, hubo reimpresiones |
| 11 | Materiales y seguridad | Angelo | 0:35 | 8:15 | Bulonera (60 mm vs. 45 mm), maderera, reglas de seguridad |
| 12 | Taller | Angelo | 1:00 | 9:15 | Plantilla y herramientas; armado, la prensa |
| 13 | **Demostración en vivo** | Lautaro y Angelo | **2:30** | 11:45 | Ver la sección 3 |
| 14 | Video | — | 0:00 | — | Puede ir de fondo durante la demo (ver la sección 4) |
| 15 | Qué respondió el prototipo | Lautaro | 1:05 | 12:50 | Las cuatro respuestas, honestas |
| 16 | Mejoras | Matías | 0:45 | 13:35 | Manivela, anclaje de la tira, bajada, chapita |
| 17 | Conclusiones | Sergio | 0:35 | 14:10 | El principio funciona; el ancho lo fija la geometría; hay mejoras concretas |
| 18 | Bibliografía | — | — | — | De consulta, no se expone |

**Total asignado: 14:10.** Quedan 50 s para los cambios de orador o una demo más larga.

| Integrante | Láminas | Tiempo |
|-----------|---------|------|
| Camila | 1 a 4 | 2:15 |
| Sergio | 5, 6 y 17 | 2:35 |
| Martín | 7 a 9 | 2:40 |
| Matías | 10 y 16 | 1:30 |
| Lautaro | 13 y 15 | 1:05 + demo |
| Angelo | 11 a 13 | 1:35 + demo |

## 2. Antes de entrar

- ☐ Máquina armada y base sujeta con la prensa a la mesa del aula (**llevar la prensa**).
- ☐ **Dos o tres botellas preparadas**: sin base, con la tapa perforada a 9 mm y la lengüeta de unos 25 cm ya cortada. Una ya montada y enganchada en el carrete antes de empezar.
- ☐ Hoja nueva en el cabezal, apretada por sus dos tornillos. Hojas de repuesto, guantes, pinza.
- ☐ Destornillador y llaves para M3, M5 y M8 (llave Allen de 4 mm para el tornillo del mango), por si hay que reajustar.
- ☐ Un tramo de tira ya cortada para mostrar en la mano.
- ☐ La presentación en el proyector y el PDF en un pendrive. El video abierto en una pestaña (enlace principal y, por las dudas, el de YouTube).
- ☐ Revisar la manivela: **hexágono hacia arriba**, con la tuerca M8 dentro y apretada; la manivela no tiene que tener juego hacia arriba.

## 3. Si algo falla en la demostración

- **Se traba:** parar, girar un poco hacia atrás para aflojar la tira, revisar que la tira siga en el ojal y que el borde siga apoyado en la guía, y seguir. No forzar.
- **La tira se corta:** decirlo con naturalidad, porque es un hallazgo que se cuenta en la lámina 15: "esto es justamente lo que vamos a contar ahora". Si la botella llegó al **hombro**, es lo esperado: ahí termina la parte cilíndrica. Si queda tiempo, volver a enganchar la punta.
- **No arranca en un minuto, o se rompe algo:** pasar a la lámina 14 (video) y seguir con el tiempo que quede.

## 4. Video

La lámina 14 tiene el enlace al video, que se abre con un clic: el principal es <https://euler-services.com/cortadora_pet/modelo_2/> y, si no carga, la copia en YouTube, <https://youtu.be/zanwZWNFGkI>. Puede quedar de fondo mientras se hace la demostración; si la demostración falla, la reemplaza.

<!-- solo-md -->

> **Mantenimiento:** los enlaces están en `VIDEO_URL` y `VIDEO_URL_ALT`, arriba en `generar_presentacion.py`; si cambian, y se vuelve a generar la presentación.

<!-- /solo-md -->

## 5. Preguntas probables

### 5.1 Del modelo 1 al 2.0 (Sergio)

**¿Por qué descartaron el modelo 1?**\
Por dos motivos que aparecieron al modelarlo para construirlo. El rodillo movía la botella por fricción: la fuerza que puede transmitir es $F_t \le \mu_s \cdot N$, cae si la botella se deforma, y esa misma fuerza era la que tenía que vencer el corte. Además, el cuello sostenía toda la botella, tomaba el empuje del rodillo y giraba sobre un rodamiento, con 269 mm de botella en voladizo. No llegamos a construirlo.

**¿Qué conservaron del modelo 1?**\
La cuchilla fija, el corte desde el borde abierto hacia el cuello, la geometría de la botella y el método de trabajo: un modelo en 3D que se comprueba antes de fabricar.

**¿Por qué la botella vertical?**\
Porque el peso ayuda a que la botella baje, y porque la tira sale de canto y se enrolla plana en un carrete de eje vertical, sin retorcerse. Es la misma disposición de PETALOT.

**¿Cómo baja la botella si no hay husillo?**\
El corte es una hélice: en cada vuelta, el borde nuevo queda $w$ más arriba y la botella tiene que bajar $w$ para volver a apoyar en la guía. La bajan el peso de la botella y una componente chica del tiro de la tira, que sale inclinada siguiendo la hélice. Lo que la frena es el rozamiento de la tapa sobre la varilla y de la pared en la ranura.

### 5.2 Diseño y cuentas (Martín)

**¿Cómo se asegura el ancho?**\
El ancho es la altura del filo sobre la guía, y la fija el calce, que es una pieza rígida. No depende del diámetro de la botella ni de cómo se gire la manivela. La ranura de 0,85 mm entre labios evita que la pared se incline, y el diseño apoya el borde en una chapita de metal para no gastar el plástico. En el prototipo todavía falta (ver «¿Y la chapita?»).

**¿Qué pasa con otras botellas?**\
El cabezal no depende del diámetro. Para tiras más anchas o más angostas se cambia el calce: hay de 7, 8, 9 y 10 mm, como en la tabla de PETALOT y Precious Plastic. Lo pensamos para botellas lisas; con nervaduras, el ancho saldría irregular.

**¿Por qué no pusieron engranajes?**\
Porque no hacen falta. La fuerza en la mano es $F = T\cdot r/R$ (tiro por radio del rollo, dividido por el brazo de la manivela). Con la manivela directa da unos 13 N, por debajo del criterio de 20 N que nos pusimos. Un tren como el de una bobinadora de filamento multiplica la velocidad y pediría unos 85 N. Si el tiro real resultara mayor, primero se alarga el brazo, que no agrega piezas, y recién después se piensa en una reducción.

**¿Cuánto vale el tiro? ¿Lo midieron?**\
No, todavía no. El tiro es la fuerza con que hay que tirar de la tira para que la hoja corte. Usamos 40 N como supuesto de diseño, y la máquina admite hasta unos 60 N sin pasar los 20 N en la mano. Se mide con una balanza de equipaje colgada de la tira; la hoja de la prueba ya está preparada.

**¿La tira resiste?**\
Su sección es de 9 × 0,25 mm. Con una resistencia baja para PET (55 MPa), rompe en unos 124 N: tres veces el tiro de diseño.

**¿Por qué la manivela de 80 mm?**\
Es el brazo con el que la fuerza queda cómoda y la mano no choca con la botella: entre el mango y la botella quedan 46 mm.

**¿Qué comprobaron en el modelo?**\
Que no haya choques al principio ni al final del corte, que la manivela dé la vuelta entera, que se pueda armar en orden (26 pasos), que cada pieza se imprima sin soportes y que entre en la cama de la impresora. Después de la prueba del prototipo agregamos un control nuevo: una luz mínima de 3 mm entre lo que gira y la tira.

**¿Por qué FreeCAD y no SolidWorks?**\
Es un CAD paramétrico libre, equivalente a SolidWorks. Exportamos el modelo en STEP, que se abre en SolidWorks, y los planos en DXF para AutoCAD.

### 5.3 Construcción (Matías, Camila, Angelo)

**¿Por qué PLA?** (Matías)\
Es barato, fácil de imprimir y permite corregir rápido: si una medida no va, se reimprime solo esa pieza. El prototipo tiene que probar que el principio funciona, no la resistencia de una máquina final. La pieza más cargada, la torre, trabaja muy por debajo de lo que resiste el PLA entre capas.

**¿Cuánto tardó la impresión?** (Matías)\
El juego completo, unas 4 horas y menos de 150 g de PLA. Hubo reimpresiones y ajustes durante la construcción.

**¿Por qué la base es de madera?** (Camila)\
Es MDF de 18 mm, lo que en la maderera llaman "fibrofácil". Es más barato y rígido que imprimirla, y en la maderera lo cortan a medida. Ya la proponía el proyecto base.

**¿Qué compraron?** (Camila)\
Rodamientos 608ZZ, tornillería métrica y una hoja de trincheta. Todo figura en la lista de compras. La varilla lisa de 8 mm no la compramos: la reciclamos de un juguete de gato. Los tornillos de 60 mm los conseguimos en una bulonera, porque la ferretería llegaba hasta 45 mm.

**¿Cómo cuidaron la seguridad?** (Camila)\
La trincheta guardada cuando no se usa, guantes para cortar, el taladro desenchufado para cambiar la mecha. En la máquina, la hoja queda dentro del cabezal y solo asoma en la ranura.

**¿Para qué la prensa?** (Angelo)\
Sujeta la base a la mesa. Fue clave durante el armado, porque deja las dos manos libres, y al usarla, porque una mano gira la manivela y la otra no tiene que sostener nada.

**¿Cómo perforaron la base?** (Angelo)\
Con una plantilla impresa en escala 1:1 que se pega sobre el MDF: se marca con punzón y se agujerea con mechas de 2,5 mm (guías), 4 mm (taco) y 9 mm (tapa de la botella).

**La manivela, ¿no se suelta?** (Angelo)\
En el primer armado se salía: la habíamos montado dada vuelta, y así la tuerca M8 no quedaba dentro de su hexágono. La pieza no tiene marcada la cara de arriba. Montada con el hexágono hacia arriba, la tuerca entra en él y aprieta la manivela contra el carrete. Lo que sigue pendiente es el tornillo del mango: usamos uno de 75 mm en vez del de 70 mm del diseño, y su punta roza la tira en cada vuelta. Por eso la manivela es la primera mejora.

### 5.4 Resultados y mejoras (Lautaro, Matías)

**¿Por qué la primera botella salió en dos tiras?** (Lautaro)\
El corte se interrumpió una vez, y fue en el **hombro** de la botella, donde la pared deja de ser cilíndrica. Era un límite previsto en el diseño: la máquina corta la parte cilíndrica y el resto se termina a mano.

**¿La botella baja sola?** (Lautaro)\
Sí, en toda la parte cilíndrica, y sin lastre: no lo imprimimos. Lo único que cuesta es el arranque; ahí la acompañamos con la mano hasta que el borde se asienta en la guía, y después sigue sola. El modelo pedía unos 115 g de lastre para el final del corte, pero era una cuenta del lado seguro: no sumaba la componente del tiro a lo largo del eje, y los rozamientos eran supuestos altos.

**¿Por qué cuesta arrancar?** (Lautaro)\
Al principio, la lengüeta cortada a mano todavía no sigue la hélice y el borde no está bien asentado en la guía. Hasta que la tira toma tensión y el borde apoya parejo, la botella no tiene de dónde bajar.

**¿Qué tan uniforme es la tira?** (Lautaro)\
A simple vista es pareja, pero no perfecta. El lunes 16/11 medimos con calibre el ancho mínimo y máximo. El criterio que nos pusimos es 9 ± 0,5 mm. Sin la chapita esperamos algo cerca de 9,5 mm.

**¿Cómo se ancla la punta de la tira?** (Matías)\
El carrete tenía una ranura donde entraba la punta, pero la tira deslizaba. Por ahora la fijamos con un tornillo para madera al núcleo del carrete. La mejora es un anclaje real: un tornillo M3 con tuerca cautiva que cruce la ranura y apriete la punta.

**¿Y la chapita?** (Matías)\
No la pusimos. Sin ella, el borde apoya en el plástico, medio milímetro más abajo: la tira sale hasta 0,5 mm más ancha y la guía se gasta con el uso. Es la mejora más fácil: cortar la galga y colocarla, sin reimprimir nada.

**¿Qué cambiarían en la manivela?** (Matías)\
Que no quede nada colgando debajo del brazo: la cabeza del tornillo embutida arriba, en el mango, y la tuerca embutida en el brazo. Así la punta queda a unos 7 mm de la tira. Mientras tanto, cambiando el tornillo por uno de 70 mm ya deja de rozar. De paso, una marca de "arriba" en la pieza.

**¿Lubricar la varilla ayudaría a que baje?** (Sergio o Martín)\
Según la referencia, no: el polietileno sobre acero tiene el mismo coeficiente seco que con grasa, y la grasa junta virutas. Alcanza con la varilla limpia.

### 5.5 De reserva (solo si preguntan)

**¿Notaron algo más en el armado?** (Angelo)\
Al apretar la manivela, el rodamiento de arriba se hundió unos milímetros en la torre. La torre no tiene escalón ni separador entre los dos rodamientos: el apriete pasa por los aros interiores y empuja el de arriba hacia adentro. Se resuelve con un separador, un tubo de 12 mm entre los aros interiores, como el espaciador de la maza de una bicicleta.

**Preguntas sobre los planos:** ver la *Guía para leer los planos*.

<!-- solo-md -->

---

*Fuentes: concepto, README y resultados del modelo 2.0; instructivo de armado; lista de compras; planos (4 láminas); hallazgos del prototipo; hechos de construcción y prueba informados por el grupo el 15/11/2026.*

*Rutas: `06_modelo_2/00_concepto.md`, `README.md`, `resultados.json`, `hallazgos_prototipo.md`; `06_modelo_2/instructivo/instructivo_armado.md`; `06_modelo_2/compras/lista_compras.md`; `06_modelo_2/planos/`; `06_modelo_2/prueba_1/` (hoja de la prueba del tiro). Inconsistencias y supuestos en `../contradicciones_y_supuestos/contradicciones_y_supuestos.md`.*

<!-- /solo-md -->
