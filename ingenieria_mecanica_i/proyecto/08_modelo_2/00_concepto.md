# Modelo 2.0 de la cortadora: documento conceptual

> **Borrador para decidir. Todavía no hay modelo 3D.** La prioridad es que el prototipo **funcione y se pueda imprimir y armar**; la Entrega 2 es una referencia, no un requisito. El modelo 1 (`06_modelo_3d/`) queda como está. Las cuentas son estimaciones de orden de magnitud: los valores definitivos salen del modelo (etapa 3) y de las pruebas de la sección 9.

## 1. Por qué un modelo 2.0

Al pensar el modelo 1 para construirlo, aparecieron dos problemas:

1. **El rodillo puede resbalar.** Mueve la botella por fricción contra el costado. Si la botella se deforma, la fuerza normal cae, y con ella la fuerza que se puede transmitir (`Ft ≤ μs·N`, Entrega 2, 5.2). Además, esa fuerza es la que tiene que vencer el corte.
2. **La sujeción por el pico es difícil.** El cuello sostiene toda la botella, absorbe el empuje del rodillo y tiene que girar sobre un rodamiento. Además, el modelo 1 mostró 269 mm de botella en voladizo al inicio (hallazgo 2.5).

Lo que hay que entregar es un **prototipo funcional**: piezas impresas en PLA por Maty en una Bambu Lab P1S, armadas y andando.

## 2. Principio de funcionamiento

**La tira tira de la botella.** El mismo tiro que hace girar la botella es el que corta.

```
          tapa perforada (desliza y gira sobre la varilla)
               _|_
              | | |   <- pico, arriba
             /  |  \
            |   |   |
            |   |   |  botella sin la base,
            |   |   |  el borde cortado abajo
  varilla ->|   |   |
            |   |   |                               manivela
            |___|___|                              ____|
    ========[ cabezal ]===( ojal )=========> (carrete, eje vertical)
            borde apoyado en la guía,               [ torre ]
            cuchilla a altura w
  ==================== base de MDF ======================================
```

1. **Preparación, a mano:** se corta la base de la botella y se arranca una tira de unos 10 cm con tijera, como en todas las cortadoras de referencia.
2. **Sostén desde adentro:** la botella va **con el pico arriba y el borde cortado abajo**, y la **varilla vertical** la atraviesa de abajo hacia arriba: entra por donde estaba la base y sale por el pico. Arriba la centra su propia tapa, perforada, que gira y desliza sobre la varilla. El pico ya no sostiene ni transmite nada: solo centra.
3. **Corte:** el borde abierto se apoya en la **guía del cabezal**, y la pared pasa por una ranura angosta. La cuchilla cruza la ranura a una altura `w` sobre la guía, que es el ancho de la tira.
4. **Tiro:** la tira pasa por un **ojal fijo** y se engancha en un **carrete de eje vertical**, con la manivela arriba, como un molinillo (sección 4.2). Al girarla, la tira se enrolla, tira de la pared, la botella gira y la cuchilla corta.
5. **Avance:** el corte es una hélice de paso `w`. En cada vuelta, el nuevo borde baja y vuelve a apoyarse en la guía. **El paso lo fija la guía, no un mecanismo.**

### Por qué resuelve los dos problemas

- **No hay nada que resbale.** El movimiento no pasa por un contacto con fricción: la manivela tira de la tira, y la tira es la misma pieza que se corta. Si el corte pide más fuerza, se tira más fuerte. Lo único que puede fallar es que la tira se rompa, y eso está acotado en la sección 4.
- **El cuello ya no trabaja.** La tapa perforada solo centra; los esfuerzos del corte los toma el cabezal, justo al lado de la cuchilla.

### ¿La botella avanza sola? Sí, si algo la empuja apenas hacia la guía

La sospecha es correcta en lo principal: **no hace falta husillo ni carro**, porque la guía fija el paso. Pero la botella tiene que acompañar el avance, bajando `w` por vuelta, y para eso algo tiene que empujarla hacia la guía. Bastaría una fuerza muy chica:

- **El rozamiento casi no frena la bajada.** Tanto en la tapa como en la ranura, la superficie se desliza casi toda en el sentido del giro. La hélice sube solo `tan α = w/(π·D) = 9/(π·88) ≈ 0,033` por cada unidad de giro, es decir `α ≈ 1,9°`. El rozamiento se opone al deslizamiento, así que su componente a lo largo del eje es del orden del 3 % del rozamiento total.
- **Hay tres fuentes de ese empuje:**
  - **El peso,** con el eje vertical: es la disposición de PETALOT (Function 3D), donde la botella va sobre una barra vertical.
  - **El propio tiro de la tira,** si sale alineada con la hélice: tiene una componente `T·sen α ≈ 0,03·T` hacia la guía.
  - **Una pesa liviana sobre la tapa,** como respaldo. En la cortadora de Low-tech Lab, el usuario apoya "una leve presión" sobre el cuello.

**Conclusión:** el principio cierra, pero el autoavance es la hipótesis más importante del modelo 2.0. Se verifica con números en el modelo y con la prueba 2. Por eso se elige el **eje vertical**: el peso ayuda gratis, y la pesa es un plan B que no cambia el diseño.

## 3. Requisito: ancho de tira constante

Tylman y Dzierżek (2020), citados en la Entrega 2, atribuyen los defectos de su filamento a un ancho de tira irregular, en una máquina con cuchilla fija y bobinado. El modelo 2.0 también es cuchilla fija y bobinado, así que **el ancho constante es un requisito de diseño**. El ancho real depende de tres cosas, y cada una tiene una medida concreta:

| Qué puede variar el ancho | Medida de diseño |
|---|---|
| **La distancia entre el borde y el filo** | **Referencia local.** El ancho es la altura del filo sobre el piso de la guía, fijada por un calce rígido. El borde se apoya en ese piso **justo debajo del filo**, a no más de 5 mm medido a lo largo del giro. Así, ni el diámetro de la botella ni su ovalización cambian `w`: solo importa la geometría del cabezal |
| **La pared se inclina o se escapa en la zona de corte** | **Pared confinada.** Pasa por una ranura entre dos labios, uno de cada lado, con una holgura de pocas décimas sobre el espesor (de 0,25 a 0,35 mm), antes y después del filo. Así no puede inclinarse ni trepar. La entrada es abocinada para que no se trabe. La cuchilla queda apretada en dos puntos y paralela al piso de la guía |
| **El borde se levanta de la guía** | **Borde siempre apoyado.** Empujan hacia abajo el peso de la botella y, si hace falta, una pesa sobre la tapa (sección 2). Esa carga tiene que superar con margen la componente axial del rozamiento; se calcula en el modelo |
| **Cambia la dirección o la tensión del tiro** | **Dirección fija.** La tira pasa por un ojal fijo entre el cabezal y el carrete, alineado con la salida de la ranura y con la inclinación de la hélice. Sin ojal, la dirección cambiaría al crecer el rollo y según cómo se mueva la mano, y una componente lateral levantaría el borde |
| **El borde gasta la guía** | **Guía con superficie metálica.** Appropedia reporta que la botella va comiendo las cortadoras impresas: el piso donde apoya el borde lleva una chapita metálica. El desgaste de los labios se revisa en la prueba 4 |

**Sobre la tensión:** la tensión de la tira no la fija la manivela, sino la resistencia del corte; la mano solo define la velocidad. Lo que influye en el ancho es la **dirección** del tiro, que la fija el ojal, y que el giro sea **parejo, sin tirones**. Por eso la manivela es directa y con un brazo cómodo (sección 4): una manivela dura invita a dar tirones.

**Cómo se comprueba:** midiendo el ancho con calibre cada 50 cm de tira (prueba 3). El criterio propuesto es `w ± 0,5 mm` en toda la botella, a revisar con el grupo según para qué se use la tira.

## 4. Números de referencia y relación de transmisión

Con la botella de 1,5 L del modelo 1: Ø88 mm y unos 180 mm de tramo cilíndrico. **Ambos datos están a confirmar midiendo las botellas reales.**

**El ancho de la tira depende del espesor de la pared.** Es la tabla que publican Function 3D (PETALOT) y Precious Plastic para hacer filamento:

| Espesor de pared (mm) | Ancho de tira `w` (mm) | Vueltas de botella | Largo de tira (m) | Radio final del rollo (mm) |
|---|---|---|---|---|
| 0,20 | 10 | 18 | 5,0 | 23 |
| 0,25 | 9 | 20 | 5,5 | 26 |
| 0,30 | 8 | 22,5 | 6,2 | 29 |
| 0,35 | 7 | 25,7 | 7,1 | 32 |

El ancho se regula **con calces bajo la cuchilla**, como en PETALOT. El radio del rollo parte de un núcleo de 15 mm y crece con el área `largo · espesor`.

### 4.1 Relación de transmisión elegida: carrete directo, 1:1

La fuerza en la mano es `F = T · r / (i · R)`, donde `T` es el tiro, `r` el radio del rollo, `R` el brazo de la manivela e `i` la reducción entre la manivela y el carrete; `i < 1` significa que multiplica la velocidad.

Se calcula con el caso más exigente del cuadro, el rollo lleno de 26 mm de la pared de 0,25 mm, y con un tiro de diseño `T = 40 N`. Ese tiro es un **supuesto**: no se encontró un valor medido, y se mide en la prueba 1. Criterio: no más de **20 N** en la mano, para girar parejo y sin cansarse en ~45 vueltas.

| Opción | `i` | Fuerza en la mano, brazo de 80 mm | Vueltas de manivela por botella | Lectura |
|---|---|---|---|---|
| Tren de la bobinadora | 1/6,6 | ~85 N | ~7 | Multiplica la velocidad: imposible de girar parejo |
| **Carrete directo** | **1** | **~13 N** | **~43** | **Cumple con margen y no tiene engranajes que imprimir** |
| Reducción 1:3 | 3 | ~4 N | ~130 | Más liviana, pero triplica las vueltas y suma dos engranajes y un eje |

**Se elige el carrete directo.** Cumple el criterio con margen: admite hasta `T = 20 · 80 / 26 ≈ 62 N` antes de pasar los 20 N. Si la prueba 1 da más, el primer recurso es **alargar el brazo** a 120 mm, que admite unos 92 N; recién después, una reducción. Un brazo más largo no agrega piezas que se rompan, y por eso va antes que un engranaje.

**La tira resiste:** su sección es de `9 × 0,25 = 2,25 mm²`. Con 55 MPa, una resistencia baja de PET sin orientar, rompe en ~120 N, tres veces el tiro de diseño. La pared de una botella está orientada y resiste más.


### 4.2 Orientación del carrete: eje vertical

Con la botella vertical, la tira sale de la cuchilla **de canto**: su ancho de 9 mm queda vertical. Para enrollarla plana, como una cinta, el eje del carrete tiene que ser paralelo a ese ancho, es decir **vertical**. Con el eje horizontal, la tira tendría que girar 90° sobre sí misma entre el ojal y el carrete.

| Criterio | Eje vertical, manivela arriba (tipo molinillo) | Eje horizontal |
|---|---|---|
| Recorrido de la tira | Sin giro: va en un plano horizontal, a la altura de la guía, desde la cuchilla hasta el carrete | Gira 90°. Los bordes de la tira recorren más camino que el centro: el estiramiento del borde es `ε ≈ (w·θ)² / (8·L²)`. Para no pasar de 0,5 %, el tramo libre `L` tiene que medir al menos **71 mm** |
| Riesgo para el ancho (sección 3) | La tira llega derecha; el ojal solo corrige el corrimiento lateral al crecer el rollo | Al crecer el rollo, el punto de salida sube 11 mm: el tiro cambia de inclinación. Si el ojal no lo absorbe del todo, aparece una componente vertical que puede levantar el borde de la guía |
| Ergonomía | La mano gira en un plano horizontal, a ~6 cm de la mesa, como un molinillo de café. Con ~13 N es cómodo. La otra mano sujeta la base | La mano gira en un plano vertical, como un malacate: es el gesto más conocido. Pero el eje tiene que estar a más de 80 mm de brazo, más el mango, más la mano, sobre la mesa: **más de 130 mm de alto** |
| Estabilidad | Torre baja, de 36 mm: el tiro actúa cerca de la base | Torre o soporte de más de 130 mm: el tiro y la mano actúan altos y hacen palanca sobre la base |
| Fijación a la base | Una sola torre atornillada, con los dos rodamientos en la misma pieza: quedan alineados por construcción | Dos soportes, o uno alto en forma de "U", que hay que alinear entre sí |
| Distancia cuchilla-carrete | Solo la necesaria para que la mano no choque con la botella: ~180 mm entre ejes | Al menos 71 mm por el giro de la tira, más el espacio de la manivela al costado |

**Se elige el eje vertical.** La tira no se retuerce, que es lo que más importa para el ancho constante. Además, la torre es baja y es una sola pieza. Lo que se resigna es el gesto de malacate: girar en un plano horizontal es menos habitual, pero con la fuerza calculada es cómodo. En los dos casos hay que sujetar la base con la otra mano o con una prensa.

## 5. Qué se reutiliza y qué es nuevo

| De dónde | Qué se toma | Qué se descarta y por qué |
|---|---|---|
| **Modelo 1** | Método completo: `parametros.py` como única fuente de verdad, origen de cada dato, verificación de choques y `make`. Geometría de la botella (`botella_solida`). Cuchilla fija y corte desde el borde abierto hacia el cuello. Lección del hallazgo 2.1: la manivela, lejos de la botella | Rodillo, husillo, carro, guías, engranajes y mordaza del cuello: los reemplaza el principio de tiro |
| **Bobinadora de Maty** | Manivela con eje cuadrado cónico, a presión. Idea de las bridas que sujetan un carrete. Pies que encastran en la base | Tren de engranajes: multiplica ×6,6 (sección 4). Lector y eje de rosca doble: ver abajo. No se copian piezas: se diseñan de nuevo, por la licencia y porque "se rompe fácil" |
| **Cortadoras de referencia** | Ranura con cuchilla a altura fija sobre una guía (Low-tech Lab, cortadoras de mano de MakerWorld y Printables). Eje vertical (PETALOT). Ancho regulable con calces. Tabla de espesor y ancho. Guía con superficie metálica (Appropedia) | Cuchillas de rulemanes afilados: requieren amoladora |
| **Nuevo** | Cabezal de corte con ranura, guía y portacuchilla; varilla y tapa perforada; ojal; carrete angosto de eje vertical con manivela; torre del carrete; base | — |

### ¿Y el eje de rosca doble con el lector?

En la bobinadora, el lector reparte un hilo redondo de 1,75 mm a lo ancho de un carrete de 60 mm o más: avanza ~1,8 mm por vuelta de carrete. Una tira plana de 9 mm conviene enrollarla **como un rollo de cinta**: cada vuelta encima de la anterior, en un carrete apenas más ancho que la tira, de 12 a 14 mm. Así no hace falta repartirla.

Si el grupo quiere enrollarla en un carrete comercial de filamento vacío, sí haría falta el lector. Pero tendría que avanzar unos 9 mm por vuelta de carrete, y el de la bobinadora avanza 1,8 mm, así que no serviría tal cual. Además, un lector que se mueve cambiaría la dirección del tiro, que el requisito de la sección 3 pide fija. **Se elige el carrete angosto sin lector**, con el ojal fijo a la entrada.

## 6. Cambios respecto de la Entrega 2

Tabla para la exposición: qué había, qué queda y por qué.

| Elemento de la E2 | Qué había | Qué queda | Por qué |
|---|---|---|---|
| Rodillo por fricción (objetivo 3; 5.2) | Rodillo contra una franja del cuerpo, que hacía girar la botella | **Se elimina.** Gira por el tiro de la tira | Podía resbalar, más con la botella deformada, y su adherencia limitaba la fuerza de corte |
| Engranajes reductores (objetivo 3; 5.3) | Par de engranajes entre el eje del rodillo y el husillo | **Se eliminan.** Manivela directa al carrete, relación 1:1 | Con el carrete directo la fuerza en la mano ya es ~13 N (sección 4). Si hiciera falta más, se alarga el brazo antes de sumar engranajes |
| Husillo y tuerca fija (objetivo 3; 5.3) | Convertían giro en avance, coordinado con el rodillo | **Se eliminan.** El avance lo da la guía del borde | El paso queda fijado junto a la cuchilla, sin depender de que dos movimientos estén sincronizados |
| Carro y dos guías (objetivo 2; 5.1) | Llevaban botella, sujeción y transmisión frente a la cuchilla | **Se eliminan.** La botella baja sobre la varilla | Sin husillo no hay nada que desplazar |
| Sujeción exterior del cuello (objetivo 1; 5.4) | El cuello sostenía y retenía la botella | **Cambia:** varilla interior y tapa perforada, que solo centran | El cuello deja de tomar esfuerzos; el apoyo pasa al cabezal, que responde a la pregunta de E2 sobre apoyos complementarios |
| Ancho por relación de engranajes (5.3) | `a = L·Db/(i·Dr)`: el ancho dependía de engranajes y diámetros | **Cambia:** el ancho es la altura del filo sobre la guía, con calces | No depende del diámetro de la botella; es el requisito de la sección 3 |
| Regulación con piezas intercambiables (objetivo 4) | Sujeciones y engranajes intercambiables | **Cambia:** calces de 7 a 10 mm; varilla común a toda botella con tapa de 28 mm | Más simple, y sin desarmar la transmisión |
| Manivela (objetivo 3) | Unida al eje del rodillo | **Queda,** unida al eje del carrete | Sigue siendo la única entrada de movimiento |
| Cuchilla fija (objetivo 2; 5.1) | Unida a la base | **Queda,** en el cabezal | — |
| Corte desde el borde abierto hacia el cuello (5.1) | Previa remoción de la base | **Queda** | — |
| Prototipo en PLA (objetivo 5; 5.5) | Para evaluar sujeción, transmisión y corte | **Queda,** impreso por Maty | — |

## 7. Piezas

### 7.1 Impresas en PLA

Todas tienen que entrar en la cama de 256 × 256 mm de la P1S. Se diseñan para imprimir sin soportes o con muy pocos, con holguras en ejes y encastres, y unidas con tornillos y tuercas: nada pegado ni "mágico". **La ficha vigente, generada desde el modelo, es [ficha_impresion.md](ficha_impresion.md)**; esta tabla fue la primera idea.

| Pieza | Función | Primera idea de impresión |
|---|---|---|
| Cabezal de corte | Ranura con labios, piso de guía con chapita, apoyo de la cuchilla y de los calces, salida de la tira | Con el piso de la guía hacia arriba y la base sobre la cama |
| Calces de ancho (7, 8, 9 y 10 mm) | Fijan la altura del filo | Planos |
| Pisador de la cuchilla | Aprieta la hoja con dos tornillos M3 | Plano |
| Zócalo de la varilla | Rosca la varilla con una tuerca M8 cautiva y la mantiene vertical | Plano, con la tuerca hacia la cama |
| Ojal | Fija la dirección del tiro | De pie |
| Torre del carrete | Aloja los dos rodamientos, uno sobre otro | De pie |
| Carrete, en dos partes | Núcleo de Ø30 con ranura para enganchar la tira; disco inferior con tuerca M8 cautiva; disco superior atornillado | Cada parte plana sobre la cama |
| Manivela | Brazo de 80 mm, con tuerca M8 cautiva en el cubo | Plana |
| Mango | Tubo que gira sobre un tornillo M5 | De pie |
| Vaso de lastre (opcional) | Se apoya en la tapa; se llena de tuercas o arena si la botella no baja sola | De pie |

### 7.2 Comerciales

**La lista vigente, generada desde el modelo, es [lista_compras.md](lista_compras.md).** Esta tabla fue la primera estimación: el modelo cambió varias piezas, como la varilla, que pasó a ser lisa, el tornillo M8 × 60, la chapita, que es una galga de 0,5 mm, el taco de MDF bajo el cabezal y el sargento.

| Pieza | Cantidad | Para qué |
|---|---|---|
| Varilla lisa Ø8 mm, 400 mm (eje lineal de impresora 3D) | 1 | Eje vertical de la botella. Lisa y no roscada: la tapa baja y gira sin engancharse en los filetes |
| Tornillo M8 × 70, cabeza hexagonal, rosca completa | 1 | Eje del carrete |
| Tuercas M8 | 3 | Una cautiva en el zócalo, una en el carrete y una en la manivela |
| Arandela M8 | 2 | Entre los rodamientos y lo que gira sobre ellos |
| Rodamiento 608ZZ (8 × 22 × 7) | 2 | Torre del carrete; es el rodamiento estándar de la impresión 3D |
| Hoja de trincheta de 18 mm | 1 y repuestos | Cuchilla: se cambia un segmento cuando pierde filo |
| Chapa fina de unos 0,5 mm | 1 recorte | Superficie del piso de la guía |
| Tornillos M3 × 25 y tuercas M3 | 2 + 2 | Pisador de la cuchilla, con tuercas cautivas |
| Tornillos M3 × 16 y tuercas M3 | 3 + 3 | Unión de las dos partes del carrete |
| Tornillo M5 × 50 y tuerca autoblocante M5 | 1 + 1 | Eje del mango |
| Tornillos para madera de 3,5 × 16 | ~14 | Fijar las piezas a la base |
| Tabla de MDF de 15 a 18 mm, unos 300 × 200 mm | 1 | Base: más barata y rígida que imprimirla. El proyecto base ya proponía MDF |
| Tapa de la misma botella, perforada a 9 mm | 1 por botella | Centra la botella arriba |
| Balanza de equipaje o dinamómetro | 1, prestado | Medir el tiro en las pruebas (anexo A) |

## 8. Riesgos

| Riesgo | Qué pasaría | Mitigación prevista |
|---|---|---|
| La botella no baja sola | El corte se vuelve un anillo en lugar de una hélice, o la tira se angosta | Eje vertical; pesa sobre la tapa; tira alineada con la hélice |
| El tiro real supera los 62 N | La manivela pasa de 20 N | Medirlo primero. Si es alto: hoja nueva; brazo de 120 mm; recién después, reducción |
| El borde gasta la guía | La referencia se desplaza y cambia el ancho | Chapita metálica en la guía y en los labios |
| La pared se traba en la ranura | El corte se frena o la tira se deforma | Entrada abocinada; holgura a definir con una pieza de prueba |
| Hombro de la botella | Al llegar al hombro, el ancho cambia | Cortar solo la parte cilíndrica y terminar a mano |
| Botellas con nervaduras | Ancho irregular | Elegir botellas lisas; sería un límite de uso declarado |
| La cuchilla corta al usuario | Accidente | Hoja dentro del cabezal; solo asoma en la ranura |
| La pieza rompe como en la bobinadora | Prototipo fuera de servicio | Ver qué rompió en la de Maty; espesores y orientación de capa según la carga |

## 9. Pruebas, en orden

1. **Tiro, sin imprimir nada** (anexo A): hoja, calces y botella sobre una tabla, tirando de la tira con una balanza de equipaje. Da el `T` real y confirma el carrete directo y el brazo de 80 mm.
2. **Autoavance.** Con el cabezal y la varilla: ¿baja sola la botella? Si no, ¿cuánto peso hace falta?
3. **Uniformidad del ancho.** Medir con calibre cada 50 cm de tira; criterio `w ± 0,5 mm`.
4. **Prototipo completo.** Botellas enteras, tiempo por botella, y desgaste de la guía después de varias botellas.

## 10. Supuestos con los que se modela

Hasta que lleguen las respuestas de Maty y del grupo, el modelo usa estos supuestos, marcados `[SUP]` en `parametros.py`:

| Pregunta | Supuesto |
|---|---|
| Base | MDF, con las piezas atornilladas |
| Boquilla de Maty | 0,4 mm |
| Botella | 1,5 L, lisa: Ø88 mm, pared de 0,25 mm, ancho de tira de 9 mm |
| Tolerancia del ancho | `w ± 0,5 mm` |
| Qué pieza rompió en la bobinadora | Sin dato: espesores mínimos generosos y capas orientadas según la carga |

## Anexo A. Prueba 1 sin imprimir nada: medir el tiro

**Objetivo:** saber cuánta fuerza hace falta para tirar de la tira mientras la cuchilla corta. El cálculo de la sección 4 supone 40 N, y este dato lo reemplaza. Lleva media hora.

### Qué hace falta

- Una botella de 1,5 L lisa, limpia y seca, **con su tapa**.
- Una trincheta con hoja nueva de 18 mm.
- Un taco o tabla de madera de unos 20 × 10 cm, y otro taco chico de unos 3 cm de alto.
- Algo plano para levantar la hoja a la altura del ancho de la tira: arandelas, palitos de helado o cartón apilados, hasta unos 9 mm.
- Dos tornillos con arandela, o una prensa chica (sargento), para apretar la hoja.
- Una balanza de equipaje, de las que tienen gancho. Mejor si marca el máximo.
- Regla o calibre, tijera, marcador, guantes y alguien que ayude.

### Armado

```
   vista de costado

         hoja de trincheta (filo hacia la botella)
        ____________________
   ====|____________________|====   <- taco de arriba, apretando la hoja
       |  calces: unos 9 mm |
   ____|____________________|_______________
   |            tabla de madera              |
```

1. **Cortá la base de la botella** con la trincheta, a la altura donde empieza la parte lisa. Trabajá despacio y con guantes. El borde tiene que quedar lo más parejo posible.
2. **Armá la cuchilla.** Sobre la tabla, apilá los calces hasta unos 9 mm. Apoyá la hoja encima, con el filo hacia afuera de la tabla, sobresaliendo unos 2 cm. Apretala con el taco de arriba y los tornillos, o con la prensa. **La hoja no se tiene que mover.**
3. **Medí la altura real** desde la mesa hasta el filo, con regla o calibre: ese es el ancho `w` que vas a cortar. Anotalo.
4. **Arrancá la tira.** Con la tijera, cortá en la botella una lengüeta de ese mismo ancho y unos 10 cm de largo, desde el borde hacia arriba, siguiendo una línea un poco inclinada.
5. **Atá la punta** de la tira a un lápiz, y colgá el gancho de la balanza del lápiz.

### Medición

1. Apoyá la botella parada sobre la mesa, con el pico arriba y el borde cortado sobre la mesa, al lado del filo. Metela de modo que **la hoja entre en el corte**: la pared queda pasando entre la mesa y la hoja.
2. Quien ayuda apoya **una mano suave sobre la tapa**, solo para que la botella no se caiga y pueda girar.
3. **Tirá de la balanza despacio y parejo**, en línea recta, a la altura de la mesa y tangente a la botella: la tira tiene que salir derecha, sin subir ni bajar. La botella va a girar sola.
4. Mirá la balanza mientras tirás:
   - **Tiro medio:** el valor que más se repite mientras el corte avanza parejo.
   - **Tiro máximo:** el pico más alto, por ejemplo al arrancar o si se traba.
5. Cortá unos 50 cm, frená y anotá. **Repetí tres veces** en la misma botella.
6. Al final, medí con regla o calibre el **ancho de la tira** en cinco puntos, y el **espesor de pared** en un pedazo. Si el calibre no llega a medir tan fino, doblá un pedazo de tira en cuatro, medí las cuatro capas juntas y dividí por cuatro.

**Para pasar a newtons:** la balanza marca kilos; multiplicá por 9,8. Por ejemplo, 3 kg son unos 29 N.

### Qué anotar

| Dato | Medición 1 | Medición 2 | Medición 3 |
|---|---|---|---|
| Marca y tipo de botella, diámetro | | | |
| Espesor de pared (mm) | | | |
| Altura del filo, `w` (mm) | | | |
| Ancho de la tira en 5 puntos (mm) | | | |
| Tiro medio (kg) | | | |
| Tiro máximo (kg) | | | |
| ¿La botella bajó sola, o hubo que empujarla? | | | |
| Observaciones: se trabó, se rompió la tira, se movió la hoja… | | | |

### Cómo se usa el resultado

- **Tiro medio de hasta 6 kg (unos 60 N):** sirve el carrete directo con brazo de 80 mm.
- **Entre 6 y 9 kg:** brazo de 120 mm.
- **Más de 9 kg:** revisar el filo y el ángulo de la hoja antes de pensar en engranajes.

La última fila de la tabla adelanta la prueba 2: si la botella bajó sola con la mano apoyada encima, el autoavance va bien encaminado.

**Seguridad:** guantes todo el tiempo, la hoja siempre apretada y nadie con la mano delante del filo. Al terminar, retirá la hoja.

---
*Fuentes: `03_entrega_2/Entrega_2_Reentrega_0_S1091_Grupo_1.pdf` (objetivos y secciones 3, 5.1 a 5.5); Tylman, I., & Dzierżek, K. (2020), citados en esa entrega; `06_modelo_3d/hallazgos.md` y `parametros.py`; `07_referencias/bobinadora_maty/` (README, STL y PDF de armado); Function 3D, [PETALOT](https://github.com/function3d/petalot) y la tabla de espesor y ancho de su FAQ; Precious Plastic, [PET filament from bottles](https://community.preciousplastic.com/library/pet-filament-from-bottles); Low-tech Lab, [Découpeuse de bouteille plastique](https://wiki.lowtechlab.org/wiki/Découpeuse_de_bouteille_plastique/en) (CC BY-SA); Appropedia, [3D printed improved PET bottle stripper](https://www.appropedia.org/3D_printed_improved_PET_bottle_stripper) (CC BY-SA 3.0); cortadoras de mano en MakerWorld ([1256835](https://makerworld.com/es/models/1256835-handheld-plastic-bottle-cutter), [98441](https://makerworld.com/en/models/98441), [98443](https://makerworld.com/en/models/98443-pet-bottom-cutter)) y Printables ([499352](https://www.printables.com/model/499352-plastic-bottle-ribbon-cutter), [279374](https://www.printables.com/model/279374-simple-pet-bottle-cutter)), conocidas solo por los resúmenes del buscador, porque esos sitios bloquean la lectura automática. El modelo 1256835 no se pudo leer: no se tomó nada concreto de él.*
