# Hallazgos del prototipo del modelo 2.0

Armado y primera prueba del prototipo impreso, informados por el grupo el 15/11/2026. Cada hallazgo queda registrado para resolverlo en el modelo, en el instructivo o en los planos. Los cambios se aplican en `parametros.py`, `piezas.py` y `verificar.py`, y desde ahí se regeneran la ficha, los planos y el instructivo con `make`.

**Criterio vigente (15/11):** el modelo representa el prototipo **tal como está armado**, con sus defectos. Las mejoras que piden reimprimir o comprar piezas quedan preparadas en «Próximos pasos» hasta que el grupo las apruebe.

## Resumen

| # | Hallazgo | Tipo | Causa | Estado |
|---|---|---|---|---|
| H1 | Manivela montada dada vuelta, sin retención axial | Armado; el diseño indicaba la cara opuesta a la que funciona | Confirmada | Corregido en el prototipo, el modelo, el plano 03 y el instructivo; falta la marca de cara (F) |
| H2 | El tornillo y la tuerca del mango rozan la tira | Diseño | Confirmada en el modelo | Abierto; `verificar.py` lo controla y lo registra como aviso |
| H3 | El 608ZZ de arriba se hunde en la torre | Diseño | Hipótesis | Abierto |
| H4 | La punta de la tira desliza en la ranura del núcleo | Diseño | Confirmada | Solución provisoria (tornillo para madera), ya en el instructivo |
| H5 | La botella cuesta arrancar y deja de bajar en el hombro | Límite de uso | Confirmada para la detención; hipótesis para el arranque | Instructivo corregido |
| H6 | Tuerca autoblocante M5 reutilizada | Armado | Confirmada | Abierto |
| H7 | La chapita no se colocó: el borde apoya en PLA | Armado | Confirmada | Abierto; el modelo la mantiene |

## H1. Manivela montada dada vuelta

- **Qué pasó:** la manivela quedó apoyada sobre la tuerca M8, sin la tuerca dentro de su hexágono. Transmitía el giro, pero no tenía retención axial: manivela y mango se salían seguido.
- **Causa (confirmada):** la manivela se montó con la cara equivocada hacia abajo. Al reensamblarla con la otra cara hacia abajo, el 15/11, quedó fija.
- **Orientación que funciona (confirmada por el grupo):** hexágono **hacia arriba**. Es la misma pieza impresa, con la cara que apoyó en la cama hacia arriba. La tuerca M8 entra en el hexágono desde arriba y, al enroscarla, aprieta la manivela contra el disco superior. El brazo queda en la parte alta del cubo (cubo de 12 mm, brazo de 8 mm) y sube 4 mm respecto del diseño original.
- **Tipo:** error de armado. La pieza no tiene ninguna marca de cara, y el diseño y el instructivo indicaban la orientación opuesta a la que funciona.
- **Aplicado (15/11):** modelo con el hexágono arriba (`parametros.py`: `Z_BRAZO`, `Z_BRAZO_SUP`; `piezas.py`: manivela, tuerca M8, mango y tornillo). La pieza se imprime igual: `piezas.VOLTEADAS` la apoya en la cama con el hexágono abajo. Paso 18 con la orientación explícita y la figura `pasos/manivela_caras.png` (desde arriba y desde abajo). Nota del plano 03: "se arma con esa cara arriba".
- **Pendiente:** marca de cara en la pieza (F, en «Próximos pasos»).

## H2. El tornillo y la tuerca del mango rozan la tira

- **Qué pasa:** debajo del brazo de la manivela, la tuerca autoblocante M5 y la punta del tornillo rozan la tira en cada vuelta.
- **Causa (confirmada en el modelo):**
  - Con la manivela como en el diseño original, la tuerca quedaba a 0,7 mm de la tira y la punta del M5 × 70 ya entraba en ella (0,9 mm³ a 164°). El control de giro de `verificar.py` iba de a 10° y no lo detectó.
  - El tornillo del prototipo es **M5 × 75 con cabeza Allen** (ISO 4762: cabeza Ø8,5 × 5 mm, llave Allen de 4 mm, que mide 4,6 mm entre vértices). Asoma 6,5 mm debajo de la tuerca. Aun con la manivela como quedó (H1), la punta baja hasta z = 49,1 mm, 1,8 mm por debajo del borde de la tira (z = 50,9 mm). La tuerca, en cambio, queda a 4,7 mm.
  - El hundimiento del rodamiento (H3) baja todo el conjunto unos milímetros más.
- **Tipo:** error de diseño.
- **Aplicado (15/11):**
  - `verificar.py` mide, de a 2° y con la botella al inicio y al final, la luz entre lo que gira (manivela, mango, tornillo y tuerca M5) y la tira. El mínimo es `LUZ_GIRO_TIRA = 3 mm` (`parametros.py`) y el resultado queda en `resultados.json` (`luz_giro_tira`).
  - El modelo lleva el M5 × 75 Allen del prototipo (`TORNILLO_MANGO_L = 75`, `[PROTO]`), igual que la ficha, la lista de compras, el instructivo y los planos. Como la luz no se cumple, `verificar.py` lo registra en `avisos` (par conocido `TornilloMango`–`Tira` en `CONOCIDOS`), sin detener `make`. Al resolver H2, el par sale de `CONOCIDOS` y el control vuelve a ser obligatorio.
  - El instructivo, en el paso 20, avisa que la punta roza la tira.
- **Solución sin reimprimir:** M5 × 70 Allen y una autoblocante nueva (H6). Con eso, la luz en el modelo da 3,2 mm y el control pasa. Otra opción es cortar 5 mm de la punta del M5 × 75.
- **Solución de fondo:** C, en «Próximos pasos».

## H3. Rodamiento superior hundido en la torre

- **Qué pasa:** al reensamblar, el 608ZZ de arriba se hundió unos milímetros en la torre y dejó de quedar al ras.
- **Causa (hipótesis):** los dos rodamientos van en un mismo alojamiento de Ø22,15 mm, entre z = 10 y z = 36 mm, con 12 mm libres entre ellos y nada que los separe. Al apretar la manivela, el tornillo M8 queda tirante. Su cabeza empuja hacia arriba el aro interior del rodamiento de abajo y la arandela empuja hacia abajo el aro interior del de arriba: los dos rodamientos se aprietan uno contra otro. Lo único que se opone es el ajuste a presión en el PLA, y el de arriba cede.

```
         arandela  (empuja hacia abajo)
  ┃ ┌────▼────┐ ┃   ← 608ZZ de arriba: baja
  ┃ │         │ ┃
  ┃ │  12 mm  │ ┃   ← hueco: nada separa los aros interiores
  ┃ │  libres │ ┃
  ┃ └────▲────┘ ┃   ← 608ZZ de abajo
         cabeza M8 (empuja hacia arriba)
```

- **Tipo:** error de diseño.
- **Mejora propuesta:** D, en «Próximos pasos».

## H4. Anclaje de la punta de la tira

- **Qué pasó:** la ranura de 1,2 × 8 mm del núcleo del carrete no retenía la punta: la tira deslizaba.
- **Causa (confirmada):** la ranura solo guía la punta; no la traba. Una vuelta de tira encima no alcanza para tomarla.
- **Tipo:** error de diseño.
- **Solución provisoria, vigente:** un tornillo para madera chico fija la punta al interior del carrete. Ya figura en el «Primer uso», 2.4, del instructivo.
- **Mejora:** E, en «Próximos pasos» (el grupo todavía no la evaluó).

## H5. Bajada de la botella

- **Qué pasa:** sin lastre, la botella baja, pero cuesta arrancar: hay que acompañarla con la mano hasta que el borde se asienta en la guía. Después sigue sola, hasta que deja de bajar y la tira se corta. La primera botella completa dio **dos tiras continuas**.
- **Causa del arranque (hipótesis):** la lengüeta cortada a mano todavía no sigue la hélice.
- **Causa de la detención (confirmada por el grupo):** la tira se cortó en el **hombro** de la botella, donde la pared deja de ser cilíndrica. El concepto ya lo preveía (`00_concepto.md`, sección 8: cortar solo la parte cilíndrica y terminar a mano). Por ahora queda descartado que falte peso.
- **Diferencia con el modelo:** la botella baja sin lastre durante todo el tramo cilíndrico, aunque el modelo pedía ~115 g. La cuenta no incluye la componente axial del tiro (`T·sen α ≈ 0,03·T`, ~1,3 N con `T = 40 N`), y los rozamientos de la tapa y de los labios son supuestos del lado seguro.
- **Tipo:** límite de uso, ni de diseño ni de armado: la cortadora corta la parte cilíndrica.
- **Aplicado (15/11):** el «Primer uso», 3, del instructivo ya no dice "baja sola". Separa el arranque (acompañar la botella con la mano hasta que el borde se asienta en la chapita) del final (en el hombro termina el corte; el resto se corta a mano).
- **Pendiente:** sumar la componente axial del tiro a la cuenta de bajada del modelo.

## H6. Tuerca autoblocante M5 reutilizada

- **Qué pasó:** para dar vuelta la manivela (H1) hubo que sacar la autoblocante del mango y volver a ponerla.
- **Causa (confirmada):** el inserto de nylon pierde agarre cada vez que se desenrosca.
- **Tipo:** error de armado (consecuencia de H1).
- **Mejora:** comprar una nueva junto con el M5 × 70 (H2), en la bulonera.

## H7. Chapita sin colocar

- **Qué pasó:** la galga de 0,5 mm no se compró ni se colocó. El rebaje de la placa quedó vacío y el borde de la botella apoya en el PLA.
- **Efecto en el ancho (estimado en el modelo):** la cara de la chapita era la referencia del ancho (`Z_GUIA` = 41,9 mm). Cerca del filo, el borde es lo más bajo de la hélice (la pendiente es de unos 0,3 mm en los 9 mm de rebaje aguas arriba), así que baja hasta el fondo del rebaje, a 41,4 mm. La tira sale hasta **0,5 mm más ancha**: con el calce de 9 mm, unos 9,5 mm, justo en el límite del criterio de 9 ± 0,5 mm. Lo confirma M1.
- **Efecto en el desgaste:** el borde roza el PLA justo donde se define el ancho, que es lo que la chapita evitaba (`00_concepto.md`, sección 8). Con el uso, el rebaje se gasta y la tira sale cada vez más ancha.
- **Tipo:** error de armado. El diseño no cambia.
- **Criterio:** a diferencia de H1, el modelo, los planos (pieza 7), el instructivo (paso 8) y la lista de compras mantienen la chapita: es una pieza que falta poner, no un diseño que cambió. `verificar.py` sigue controlando el borde sobre metal.
- **Mejora:** H, en «Próximos pasos».

## Próximos pasos (preparados, sin aplicar)

Dependen de que el grupo decida, el lunes 16/11, si se reimprimen piezas. El video de respaldo y la presentación del 19/11 muestran el prototipo tal como está.

| # | Mejora | Resuelve | Reimprime | Compra |
|---|---|---|---|---|
| C | Nada colgando debajo del brazo | H2 | Manivela y mango | Según la variante |
| D | Separador entre los 608ZZ | H3 | Pieza nueva chica | — |
| E | Anclaje real de la punta de la tira | H4 | Disco inferior del carrete | Tornillo M3 y tuerca |
| F | Marca de cara en la manivela | H1 | Manivela (junto con C) | — |
| G | Medidas de la varilla real | Lastre, tapa, zócalo | Lastre, si se imprime | — |
| H | Colocar la chapita | H7 | — | Galga de 0,5 mm (o un segmento de trincheta) |

**C. Mango sin nada debajo del brazo.** La cabeza Allen permite embutir el tornillo arriba, en el mango:

- Caja de Ø9 × 5,5 mm en la punta de arriba del mango, para la cabeza Allen (Ø8,5 × 5). La llave de 4 mm entra por arriba.
- Autoblocante M5 embutida en un hexágono de 5 mm de profundidad en la cara de abajo del brazo, que queda de 8 mm.
- El tornillo se elige para que la punta asome apenas debajo de la tuerca, lo justo para pasar el inserto de nylon (~2 mm). Con el mango de 55 mm corresponde un M5 × 60. Para reutilizar el M5 × 75, el mango tendría que tener unos 70 mm.
- Luz esperada con la manivela como en H1: la punta queda a unos 7 mm de la tira, contra los 3 mm mínimos.
- Cambios: `piezas.py` (mango, manivela, tornillo, tuerca), `parametros.py` (`TORNILLO_MANGO_L`, `MANGO_L`), pasos 19 y 20 del instructivo, lista de compras. Al aplicarlo, sacar el par `TornilloMango`–`Tira` de `CONOCIDOS` en `verificar.py`.

**D. Separador entre los rodamientos.** Es un tubo de 12,0 mm de largo, Ø8,4 mm interior y ~Ø11 mm exterior, que va en el hueco entre los dos 608ZZ y apoya solo en los aros interiores. El apriete de la manivela se cierra contra el tubo (cabeza M8 → aro interior de abajo → tubo → aro interior de arriba → arandela) y la torre no recibe carga axial. Es lo mismo que el espaciador de una maza de bicicleta. Se imprime en minutos y no obliga a reimprimir la torre. Se coloca en el paso 12, entre el primer rodamiento y el segundo, y sería la pieza n.° 16 de la ficha. La alternativa, un escalón en el alojamiento, obliga a reimprimir la torre y carga las bolas del rodamiento.

**E. Anclaje de la tira.** Tornillo M3 con tuerca cautiva que cruza la ranura del núcleo y aprieta la punta contra la pared, como el prisionero que traba la varilla en el zócalo. Alternativa: agujero guía para el tornillo para madera actual, que se gasta con cada botella.

**F. Marca de cara.** Texto "ARRIBA" bajorrelieve de 0,6 mm en la cara de la cama del brazo, que con H1 queda arriba. Se imprime sin soportes.

**G. Varilla.** La del prototipo no se compró: es reciclada de un juguete, así que su diámetro no está garantizado. Si la varilla medida no es de Ø8, el diámetro pasa a `VARILLA_D` en `parametros.py`. Ojo: hoy `VARILLA_D` también define los agujeros por donde pasa el tornillo M8 en el carrete y en la manivela, así que antes hay que separarlo en dos parámetros. Dependen de la varilla: el agujero del zócalo (`HOLG_VARILLA`), el tubo del vaso de lastre (`VARILLA_D + 0,8`) y el agujero de la tapa (`TAPA_AGUJERO = 9`).

**H. Chapita.** Cortar la galga a 18 × 12,7 mm (o usar un segmento de trincheta, que también es de 0,5 mm) y colocarla como en el paso 8 del instructivo: hay que sacar el calce y el labio exterior. No se reimprime nada. Después, medir de nuevo el ancho (M1).

## Mediciones pendientes

| # | Qué | Cómo | Dónde va |
|---|---|---|---|
| M1 | Ancho de la tira, mínimo y máximo | Calibre, varios puntos; lunes 16/11. Sin chapita se esperan unos 9,5 mm (H7) | `MEDICION_ANCHO` de `05_presentacion/generar_presentacion.py` |
| M2 | Tiro necesario para cortar | Hoja de `prueba_1/`; hoy sigue el supuesto de 40 N | `parametros.py` y cuentas del README |
| M3 | Altura de la botella donde la tira se corta | Hecha: en el hombro (15/11) | Causa de H5 |
| M4 | Diámetro de la varilla | Calibre; lunes 16/11 | G |
| M5 | Tornillo del mango: largo, cabeza y cuánto asoma debajo de la tuerca | Calibre; lunes 16/11 | Confirma H2 (el modelo dice 6,5 mm) |
| M6 | Cuánto se hundió el 608ZZ de arriba | Calibre de profundidad, desde la cara de la torre | H3 y luz de H2 |

---
*Fuentes: `05_presentacion/documentos_grupo/contradicciones_y_supuestos/contradicciones_y_supuestos.md` (secciones 1 y 2); `00_concepto.md`, sección 8; `README.md`, secciones 2 y 4; `instructivo/instructivo_armado.md` (pasos 12, 18 y 20, «Primer uso»); `resultados.json` (`luz_giro_tira`, `avisos`); medidas de cabeza Allen M5 según ISO 4762; hechos de armado y prueba informados por el grupo el 15/nov/2026 (H7 y el origen de la varilla, después).*
