# Contradicciones, hallazgos del prototipo y supuestos de la presentación

Estado al **15/11/2026**, para la exposición del 19/11. Reúne en un solo lugar qué decía cada documento cuando no coincidían, qué encontramos al armar y probar el prototipo, qué mejoras quedan para decidir y qué datos de la presentación son supuestos.

**Criterio:** lo que pasó en el prototipo prevalece sobre todo. Después, lo que salió del modelo 3D (ficha de impresión, lista de compras, planos, instructivo), y por último el documento de concepto, que fue la primera idea.

<!-- solo-md -->

> **Mantenimiento:** el seguimiento detallado de los hallazgos, con los cambios en el código, está en `06_modelo_2/hallazgos_prototipo.md`; las secciones 2 a 4 de este documento lo resumen para el grupo. La v1 de este archivo, para el modelo 1, quedó en `07_presentacion/v1_modelo_1/`. Se compila con `make` en `documentos_grupo/`.

<!-- /solo-md -->

## 1. Contradicciones entre documentos

| # | Tema | Qué decía cada documento | Cómo quedó | Pendiente |
|--|-----|------------|--------|--------|
| 1 | Tornillo del mango | Concepto: M5 × 50. Lista de compras y planos: M5 × 70. Prototipo: M5 × 75 cabeza Allen | El del prototipo, en el modelo y en todos los documentos | Pasar a M5 × 70 (hallazgo H2) |
| 2 | Eje del carrete | Concepto: M8 × 70 con 3 tuercas. Lista de compras: M8 × 60 con 2 tuercas (el zócalo pasó a prisionero M3) | Lista de compras; el concepto fue la primera estimación | — |
| 3 | Orientación de la manivela | Diseño, plano 03 e instructivo: hexágono de la tuerca M8 hacia **abajo**. Prototipo: funciona con el hexágono hacia **arriba** | Hexágono **hacia arriba**. Modelo, plano 03 e instructivo corregidos | Marca de cara en la pieza (mejora F) |
| 4 | Fijación de la placa del cabezal | README del modelo: al taco. Plano 02: "tornillos a la base" | Al taco; plano corregido | — |
| 5 | Cota de 42 mm, lámina 1 | La línea del globo 5 tapaba el "4" de la cota 42 | Globo movido; plano corregido | — |
| 6 | Bajada de la botella | Instructivo: "baja sola". Modelo: al final hace falta un lastre de ~115 g. Prototipo: baja sin lastre en toda la parte cilíndrica; cuesta arrancar y el corte termina en el hombro | Lo del prototipo. Instructivo corregido | **Actualizar las láminas 15 y 16:** todavía hablan de falta de peso y del lastre |
| 7 | Anclaje de la tira | Instructivo: la punta entra en la ranura del carrete y queda tomada con una vuelta. Prototipo: deslizaba | Tornillo para madera, provisorio; ya figura en el instructivo | Anclaje real (mejora E) |
| 8 | Cantidad de piezas impresas | Ficha: 15 piezas, ~194 g, ~6,1 h, con el vaso de lastre. Prototipo: el lastre no se imprimió | Lámina 10: 14 piezas, ~4 h, ~150 g (dato del grupo, 17/11) | Si se imprime el lastre, actualizar |
| 9 | Video de respaldo | El primer video decía "versión preliminar" en pantalla | Rehecho sin ese rótulo, con el prototipo tal como está (25 s); publicado y enlazado en la lámina 14 (dominio propio y YouTube) | — |

## 2. Hallazgos del prototipo (15/11)

| # | Qué pasó | Tipo | Estado |
|--|------------|------|------------|
| H1 | La manivela se montó dada vuelta: apoyaba sobre la tuerca M8 sin alojarla, y manivela y mango se salían | Armado (la pieza no indica su cara) | **Corregido:** hexágono hacia arriba. Falta la marca de cara (F) |
| H2 | El tornillo y la tuerca del mango rozan la tira en cada vuelta | Diseño | **Abierto.** Con el M5 × 75, la punta baja 1,8 mm por debajo del borde de la tira |
| H3 | El rodamiento 608ZZ de arriba se hundió unos milímetros en la torre | Diseño (hipótesis) | **Abierto** (mejora D) |
| H4 | La punta de la tira deslizaba en la ranura del carrete | Diseño | Provisorio: tornillo para madera (mejora E) |
| H5 | La botella cuesta arrancar; el corte termina en el **hombro**, donde la pared deja de ser cilíndrica | Límite de uso | **Confirmado.** La primera botella dio dos tiras. Instructivo corregido |
| H6 | La tuerca autoblocante M5 se reutilizó al dar vuelta la manivela | Armado | **Abierto:** el nylon pierde agarre; comprar una nueva |
| H7 | La chapita no se colocó: el borde de la botella apoya en el PLA | Armado | **Abierto** (mejora H). El modelo, los planos y el instructivo la mantienen |

**Sobre H2.** Debajo del brazo de la manivela cuelgan la tuerca autoblocante M5 y la punta del tornillo del mango. Con la manivela como quedó, la tuerca pasa a 4,7 mm de la tira, pero el tornillo de 75 mm asoma 6,5 mm debajo de la tuerca y su punta entra en la tira. Desde el 15/11, el modelo exige al menos **3 mm de luz** entre lo que gira y la tira. Con un **M5 × 70** y una autoblocante nueva, la luz da 3,2 mm y deja de rozar, sin reimprimir nada. Otra opción es cortar 5 mm de la punta del M5 × 75.

**Sobre H3.** Los dos rodamientos van en un mismo alojamiento de la torre, con 12 mm libres entre ellos y nada que los separe. Al apretar la manivela, la cabeza del tornillo M8 empuja hacia arriba el aro interior del rodamiento de abajo, y la arandela empuja hacia abajo el aro interior del de arriba. Lo único que se opone es el ajuste a presión en el PLA, y el de arriba cede.

**Sobre H5.** El modelo pedía lastre porque su cuenta era del lado seguro: no sumaba la componente del tiro a lo largo del eje de la botella (unos 1,3 N con un tiro de 40 N), y los rozamientos eran supuestos altos. Por ahora queda descartado que falte peso. El arranque cuesta porque la lengüeta cortada a mano todavía no sigue la hélice.

**Sobre H7.** La cara de la chapita era la referencia del ancho. Sin ella, el borde baja hasta el fondo del rebaje, 0,5 mm más abajo: con el calce de 9 mm la tira sale de unos 9,5 mm, justo en el límite de 9 ± 0,5. Además, el borde gasta el PLA justo donde se define el ancho. La medición del lunes 16/11 lo confirma.

## 3. Mejoras propuestas: para decidir el lunes 16/11

Ninguna está aplicada. La presentación y el video muestran el prototipo tal como está.

| # | Mejora | Resuelve | Hay que reimprimir | Hay que comprar |
|--|-----------|-----|---------|---------|
| C | Nada colgando debajo del brazo de la manivela | H2 | Manivela y mango | Tornillo M5 × 60 Allen y autoblocante M5 |
| D | Separador entre los dos rodamientos | H3 | Una pieza nueva chica | — |
| E | Anclaje real de la punta de la tira | H4 | Disco inferior del carrete | Tornillo M3 y tuerca |
| F | Marca de cara en la manivela | H1 | Manivela (junto con C) | — |
| G | Medidas de la varilla real | Lastre, tapa, zócalo | El lastre, si se imprime | — |
| H | Colocar la chapita | H7 | — | Galga de 0,5 mm (o un segmento de trincheta) |

- **C. Manivela sin nada debajo del brazo.** La cabeza Allen del tornillo queda embutida arriba, en la punta del mango, y se ajusta con la llave de 4 mm desde arriba. La autoblocante va embutida en un hexágono de la cara de abajo del brazo. Con el mango de 55 mm corresponde un M5 × 60, y la punta queda a unos 7 mm de la tira (el mínimo es 3 mm). Para reutilizar el M5 × 75, el mango tendría que medir unos 70 mm.
- **D. Separador.** Un tubo de 12 mm de largo, Ø8,4 interior y unos Ø11 exterior, que va entre los dos rodamientos y apoya solo en los aros interiores. El apriete se cierra contra el tubo y la torre no recibe carga, igual que el espaciador de la maza de una bicicleta. Se imprime en minutos, no obliga a reimprimir la torre y se coloca al armar la torre, entre el primer rodamiento y el segundo.
- **E. Anclaje.** Un tornillo M3 con tuerca cautiva que cruza la ranura del carrete y aprieta la punta de la tira contra la pared. Alternativa más simple: un agujero guía para el tornillo para madera actual.
- **F. Marca de cara.** El texto "ARRIBA" en bajorrelieve de 0,6 mm sobre la cara que va hacia arriba. Se imprime sin soportes.
- **G. Varilla.** La del prototipo no se compró: es reciclada de un juguete, así que su diámetro no está garantizado. Si la varilla medida no es de Ø8, hay que ajustar en el modelo el agujero del zócalo, el tubo del vaso de lastre y el agujero de la tapa.
- **H. Chapita.** Cortar la galga a 18 × 12,7 mm, o usar un segmento de trincheta, y colocarla como en el paso 8 del instructivo, sacando antes el calce y el labio exterior. No se reimprime nada.

## 4. Mediciones pendientes

La última columna queda libre para anotar el resultado a mano.

| # | Qué medir | Cómo | Resultado |
|--|----------|----------|--------|
| M1 | Ancho de la tira, mínimo y máximo | Calibre, en varios puntos de la tira; lunes 16/11. Criterio: 9 ± 0,5 mm | |
| M2 | Tiro necesario para cortar | Balanza de equipaje colgada de la tira, con la hoja de la prueba. Hoy se usa el supuesto de 40 N | |
| M3 | Altura de la botella donde se corta la tira | **Hecha:** en el hombro (15/11) | Hombro |
| M4 | Diámetro de la varilla | Calibre; lunes 16/11 | |

## 5. Supuestos y datos de la presentación

| Dato | Valor | De dónde sale | Estado |
|-------|--------|----------|------|
| Duración | 15 min; 14:10 asignados | Informada por el grupo | Confirmado |
| Demostración en vivo | 2:30, lámina 13 | Propuesta aprobada el 15/11 | Ensayar |
| Ritmo de lectura | 115 palabras por minuto | Supuesto | Ensayar con reloj |
| Reparto | Por área de trabajo de cada integrante | Propuesta aprobada el 15/11 | Confirmado |
| Integrantes | Burelli, Fernandez, Franco Solignac, Kainer, Ledesma Blanco, Paredes | Carátula de la Entrega 2 ("Fernandez" sin tilde, como ahí) | Confirmado |
| Docentes | Prof. Abud, ATP Cáceres Guido | Carátula de la Entrega 2 | Confirmado |
| Tiro de diseño | 40 N | Supuesto del concepto | **Medir (M2)** |
| Fuerza en la mano | 13,2 N; 42 vueltas | Cálculo del modelo | Depende del tiro |
| Transmisiones comparadas | Como una bobinadora: ~85 N y ~7 vueltas. Reducción 1:3: ~4 N y ~130 vueltas | Concepto, con un tiro de 40 N | Depende del tiro |
| Rotura de la tira | 124 N | Cálculo del modelo (55 MPa, valor bajo para PET) | Referencia |
| Lastre | ~115 g | Cálculo del modelo, del lado seguro | No se imprimió; no hizo falta (H5) |
| Impresión | 14 piezas, ~4 h, ~150 g | Dato del grupo (17/11); la ficha estimaba ~6 h y ~190 g sin el vaso de lastre | Confirmado |
| Objetivos secundarios | Cuello sin carga, ancho fijado por la geometría, manivela directa, adaptación con calces, prototipo funcional | Adaptados de la Entrega 2 al modelo 2.0 | Aprobados el 15/11 |
| Bibliografía | PETALOT, Low-tech Lab, Appropedia, Precious Plastic y Engineering Toolbox (salen ISO 261, KHK y Thomson, que eran del modelo 1) | Concepto y README del modelo 2.0 | Las citas web no se volvieron a contrastar |
| Fotos | Solo una, en el cierre (lámina 17); hoy dice **FOTO PENDIENTE** | Pedido del grupo | **La saca el grupo** |

<!-- solo-md -->

## Imágenes de la presentación (mantenimiento)

| Lámina | Imagen | Origen |
|---|---|---|
| 1 | `figuras/portada.png` | `06_modelo_2/figuras/conjunto.png`, recortada |
| 5 | `figuras/modelo_1.png` | `05_modelo_1/figuras/conjunto_inicio.png`, sin título ni leyenda |
| 6 | Esquema vectorial del principio | **Nueva**, dibujada en la lámina (simplificada de la lámina 4 de los planos) |
| 7 | `figuras/cabezal.png` y `figuras/detalle_a.png` | `06_modelo_2/figuras/detalle_cabezal.png`, y el detalle A de `planos/02_cabezal.pdf` sin la columna de rótulos (llevaba la numeración de los planos); los rótulos van en la lámina |
| 9 | `figuras/explotada.png` | **Nueva:** vista explotada, `renderizar_figuras.py` |
| 10 | `figuras/piezas_impresas.png` | **Nueva:** mosaico de las 14 miniaturas de la ficha |
| 12 | `figuras/plantilla.png`, `paso_12.png`, `paso_22.png` | Plantilla A3 y vistas del instructivo |
| 16 | `figuras/carrete_manivela.png` | **Nueva:** render con la manivela sobre la tira, `renderizar_figuras.py`; la marca roja es una forma de la lámina |
| 17 | Recuadro **FOTO PENDIENTE** | Lo reemplaza la foto del grupo |

Pendientes en `generar_presentacion.py`: `MEDICION_ANCHO` (M1) y la foto final. `VIDEO_URL` y `VIDEO_URL_ALT` ya tienen los enlaces (contradicción 9).

<!-- /solo-md -->

<!-- solo-md -->

---

*Fuentes: concepto, README y resultados del modelo 2.0; hallazgos del prototipo; ficha de impresión; lista de compras; instructivo de armado; planos; consignas de las Entregas 1 y 2; carátula de la Entrega 2; hechos de construcción y prueba informados por el grupo el 15/11/2026.*

*Rutas: `06_modelo_2/00_concepto.md`, `README.md`, `resultados.json`, `hallazgos_prototipo.md`, `piezas.py`, `parametros.py`, `ficha/ficha_impresion.md`, `compras/lista_compras.md`, `instructivo/instructivo_armado.md` y `planos/`; `00_consignas/`; `08_entregas_2_3/entregado/Entrega_2_Reentrega_0_S1091_Grupo_1.pdf`.*

<!-- /solo-md -->
