# Guía para leer los planos de la cortadora

Son cuatro láminas A3, que salen del mismo modelo 3D que las imágenes de la presentación: si cambia una medida en el modelo, cambian los planos.

<!-- solo-md -->

> **Mantenimiento:** las láminas están en `06_modelo_2/planos/` (PDF para mirar, DXF para AutoCAD): `01_conjunto.pdf`, `02_cabezal.pdf`, `03_carrete.pdf` y `04_esquema.pdf`.

<!-- /solo-md -->

## 1. Lo mínimo para leer cualquier lámina

### El rótulo (abajo a la derecha)

Es la "etiqueta" de la lámina. Dice:

- **Título:** qué muestra la lámina (por ejemplo, "Plano de conjunto").
- **Asignatura y curso:** UTN FRBA, Ingeniería Mecánica I, S1091, Grupo 1.
- **Escala:** cuántas veces más chico o más grande está dibujado.
- **Fecha:** 19/11/2026.
- **Lámina:** "1 de 4", "2 de 4", etc.
- **Símbolo de método:** el dibujito con un cono truncado y dos círculos indica cómo están ubicadas las vistas (ver abajo).

### La escala

- **1:1** — tamaño real: 10 mm en el papel son 10 mm en la pieza.
- **1:2,5** — el dibujo es 2,5 veces más chico que la máquina: 10 mm en el papel son 25 mm de verdad.
- **4:1** — el dibujo es 4 veces más grande: se usa para ver detalles chicos, como la ranura de 0,85 mm.
- **Sin escala** — es un esquema: las proporciones son aproximadas y no se mide sobre el papel.

**Lo importante:** las medidas se leen en las **cotas**, no se miden con regla sobre el papel. Todas las cotas están en **milímetros**, aunque el plano diga una escala.

### Las vistas (método E)

Cada vista es la pieza mirada desde un lado, "aplastada" sobre el papel. Usamos el **método E** (europeo, ISO-E), que es el que se usa en Argentina:

<!-- solo-md -->

```
    +----------------+    +----------------+
    |  Vista frontal |    | Lateral izq.   |   <- la vista desde la IZQUIERDA
    |                |    | (va a la       |      se dibuja a la DERECHA
    +----------------+    |  derecha)      |
    +----------------+    +----------------+
    | Vista superior |   <- la vista desde ARRIBA se dibuja ABAJO
    | (va abajo)     |
    +----------------+
```

<!-- /solo-md -->

<!-- solo-pdf
\begin{center}
\begin{tikzpicture}[font=\small, caja/.style={draw, thick, minimum width=4.2cm, minimum height=2cm, align=center}]
\node[caja] (f) at (0,0) {\textbf{Vista frontal}\\(la principal)};
\node[caja] (l) at (5.2,0) {\textbf{Lateral izquierda}\\mirada desde la \textbf{izquierda},\\dibujada a la \textbf{derecha}};
\node[caja] (s) at (0,-2.8) {\textbf{Vista superior}\\mirada desde \textbf{arriba},\\dibujada \textbf{abajo}};
\draw[dashed, gray] (f.east) -- (l.west);
\draw[dashed, gray] (f.south) -- (s.north);
\end{tikzpicture}
\end{center}
-->

Parece al revés, pero es la regla del método E: cada vista va **del lado opuesto** desde donde se mira. En la lámina 1 están exactamente así.

### Los tipos de línea

| Línea | Qué significa |
|---|---|
| Continua gruesa | Aristas que se ven |
| De trazos (rayitas cortas) | Aristas ocultas: están detrás o adentro, por ejemplo el alojamiento de los rodamientos dentro de la torre |
| Trazo y punto | Ejes de simetría y centros de agujeros: el eje de la botella, el del carrete |
| Continua fina | Cotas, líneas de referencia y rayados |

### Cotas, globos y rayados

- **Cota:** una línea con flechas en las puntas y un número: es la medida en mm. **Ø** delante del número es un diámetro; **R**, un radio.
- **Globo:** un número dentro de un círculo, unido a una pieza con una línea. Ese número se busca en la **lista de piezas** (solo en la lámina 1).
- **Rayado:** líneas inclinadas paralelas dentro de un contorno. Indican que la pieza está **cortada** por un plano imaginario, para ver adentro. Piezas distintas llevan rayado en distinto ángulo, para que se distingan.

## 2. Lámina por lámina

### Lámina 1: plano de conjunto (escala 1:2,5)

**Qué muestra:** la máquina entera armada, con la botella al inicio del corte, en tres vistas: frontal (mirando desde el lado de la cuchilla), lateral izquierda y superior.

**Cómo se lee:**

- Los **globos** (números en círculos) señalan cada pieza; la **lista de piezas**, a la derecha, dice qué es, cuántas hay y de qué material. Se lee de abajo hacia arriba: la 1 (base) está en la última fila.
- Las columnas de la lista son: **N.°** (el del globo), **Denominación** (el nombre), **Cant.** y **Material / Obs.** (PLA si es impresa; si es comercial, la medida).
- Cotas generales: base de **345 × 200 mm** y **18 mm** de espesor; **180 mm** entre el eje de la botella y el del carrete; brazo de la manivela de **80 mm**; **42 mm** de altura de la guía sobre la base.
- La nota de la izquierda aclara que la **prensa (sargento)** no se dibuja, porque no es parte de la máquina, y cuántos tornillos para madera lleva cada pieza.

**Preguntas típicas:**

- *¿Qué es la pieza 7?* Se busca el 7 en la lista: chapita de apoyo, una galga de 0,5 mm cortada a 18 × 12,7 mm.
- *¿Por qué la botella está dibujada entera?* Porque es la posición al inicio del corte: así se ve que nada choca con la botella más alta.
- *¿Qué material es la base?* MDF de 18 mm (pieza 1).

### Lámina 2: cabezal de corte (escala 1:1, detalle 4:1)

**Qué muestra:** las piezas impresas del cabezal, cada una con sus medidas: la **placa del cabezal** (6), el **labio exterior** (8), el **calce** (9) y el **pisador** (11). A la derecha, el **detalle A**, a escala 4:1.

**El detalle A es lo más importante de todos los planos.** Es un corte por la ranura, 3 mm antes del filo. Muestra, de abajo hacia arriba: el taco de MDF, la placa, la chapita metálica, el calce y, encima del calce, la **hoja**. La pared de la botella baja por la ranura entre el labio interior y el labio exterior. La cota **w = 9** es la altura del filo sobre la chapita: **es el ancho de la tira.** La cota **0,85** es el ancho de la ranura: pared de 0,25 mm más 0,3 mm de holgura de cada lado.

**Preguntas típicas:**

- *¿Cómo se cambia el ancho de la tira?* Cambiando el calce: hay de 7, 8, 9 y 10 mm (la nota de la lámina dice sus espesores, 0,1 mm menos que el nombre).
- *¿Para qué la chapita?* Para que el borde de la botella apoye en metal y no gaste el PLA justo donde se define el ancho. En el prototipo todavía no está puesta: es una de las mejoras.
- *¿Qué son los agujeros de la placa?* Los 4 grandes, con caja, son para los tornillos que la fijan al taco; los 2 chicos llevan tuercas M3 cautivas por abajo, para apretar la hoja.

### Lámina 3: carrete, manivela y zócalo (escala 1:1)

**Qué muestra:** las piezas que giran y la que sostiene la varilla: la **torre** (14), el **carrete** (17 y 18), la **manivela** (19) y el **zócalo** (2). Cada una con una vista desde arriba y una de costado.

**Cómo se lee:**

- En la torre, las **líneas de trazos** son el alojamiento de los dos rodamientos 608ZZ, que van a presión (Ø22,1 para un rodamiento de Ø22), y la cavidad de abajo para la cabeza del tornillo M8.
- En el carrete, la **ranura 1,2 × 8** es donde engancha la punta de la tira, y el **hexágono** aloja la tuerca M8 cautiva.
- En la manivela, la cota **80** es el brazo. La nota dice que la tuerca M8 va en el cubo, con el hexágono hacia la cara de la cama, que se arma hacia arriba, y que el mango es un tubo de Ø22 × 55 sobre un tornillo M5 × 75 cabeza Allen.
- En el zócalo, el agujero en **rombo** es para el prisionero M3: tiene esa forma para que se imprima sin soporte.

**Preguntas típicas:**

- *¿Cómo gira el carrete?* Sobre el tornillo M8, que gira dentro de los dos rodamientos de la torre.
- *¿Por qué el agujero en rombo?* Un agujero redondo horizontal tiene un "techo" que la impresora no puede hacer sin soporte; el rombo se sostiene solo.

### Lámina 4: esquema de funcionamiento (sin escala)

**Qué muestra:** el principio de la máquina, visto desde arriba y de frente, con la **cadena de cuentas** y una **tabla de valores**. Es la única lámina que se parece a la presentación.

**Cómo se lee:**

- **Vista desde arriba:** la botella y el carrete giran en sentido horario; la tira sale del cabezal, pasa por el ojal y se enrolla.
- **Vista de frente:** el borde cortado es una hélice; la botella baja $w$ por vuelta y vuelve a apoyar en la guía.
- **Cadena del movimiento:** las fórmulas, desde el paso del corte ($p = w$) hasta la fuerza en la mano, $F = T\cdot r_f / R$, recuadrada.
- **Tabla:** los valores de cada símbolo. El tiro $T = 40$ N dice "supuesto": todavía no se midió.

**Pregunta típica:** *¿De dónde sale la fuerza en la mano?* El momento que hace la tira sobre el carrete (tiro por radio del rollo) lo equilibra la mano con el brazo de la manivela: $F\cdot R = T\cdot r$. Con el rollo lleno da 13,2 N.

<!-- solo-md -->

---

*Fuentes: las cuatro láminas de los planos del modelo 2.0; README del modelo 2.0, sección 7.*

*Rutas: `06_modelo_2/planos/01_conjunto.pdf` a `04_esquema.pdf`; `06_modelo_2/README.md`, sección 7.*

<!-- /solo-md -->
