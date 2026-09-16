# Guía de construcción — Diagrama Chapin Ejercicio 13 (`parcial_1.dxf`)

> Guía de **medidas y coordenadas en milímetros** para dibujar en LibreCAD, a mano, el diagrama estructurado (Chapin/Nassi-Shneiderman) del Problema 13, dentro del área de trabajo que ya existe en `parcial_1.dxf`. Esto **no reemplaza** el `.dxf` — es la hoja de ruta para completarlo vos mismo.
>
> Alcance: **solo el diagrama estructurado**. La parte escrita (los 3 párrafos de justificación tipo "las variables que uso son contadoras...", equivalentes a las notas (4)(5)(6) de Francisco) va aparte, en una hoja rayada — no está contemplada acá.

## 0. De dónde sale esta versión

Se reconstruyó a partir de tres fuentes, en este orden de prioridad:

1. **Fotos reales del pizarrón** (`ejercicio_13_1.jpeg`, `ejercicio_13_2.jpeg`) — la resolución del Ing. Alaniz tal cual la dibujó, con los círculos de incisos (1a,1b,1c,2a,2b,3) marcados a mano en `ejercicio_13_2.jpeg`.
2. **Resolución de Francisco Sticotti** (`ejercicio_13_0.jpeg`) — mismo esqueleto, letra e higiene de diagrama superiores, con las 3 correcciones ya incorporadas (contador único en TM/300, ramas F que también informan, "Error de tipeo" para cargo inválido).
3. `candidatos_parcial_chapin.md` y `diagramacion_estructurada.html` — que documentan por qué esa es la versión a reproducir.

La técnica de trazado que uso abajo (la cascada de cargos dibujada como **columnas paralelas una al lado de la otra**, no anidadas cada vez más angostas hacia adentro) es la que **realmente usan ambos** en las fotos — no una simplificación mía. Es la clave que hace que todo entre cómodo en la hoja.

## 1. Área de trabajo disponible (ya existe en el .dxf, no la toques)

Confirmado leyendo `parcial_1.dxf`:

| Elemento | Coordenadas (mm) | Capa |
|---|---|---|
| Marco exterior de hoja (A4) | (0,0) – (210,297) | `MARCO` |
| Marco interior | (25,10) – (200,287) | `MARCO` |
| Rótulo (franja superior) | (25,267) – (200,287) | `ROTULO_2B` / `ROTULO_2H` |

El rótulo ya tiene tus datos (Paredes Sergio, Leg. 260.861-3), "Ej. 13", fecha y materia. **No lo toques.**

Eso deja libre, por debajo del rótulo, el área donde va el diagrama:

- **X: 25 a 200** (175 mm de ancho)
- **Y: 10 a 267** (257 mm de alto)

Todo lo que sigue va en una **capa nueva `GEOMETRIA`** (ya existe en el archivo, vacía — está pensada para esto). Cambiá a esa capa antes de dibujar.

## 2. El algoritmo a reproducir (versión recomendada)

Igual a la que ya está en `candidatos_parcial_chapin.md` (líneas 120-163) y en `diagramacion_estructurada.html` — pizarrón del profesor + las 3 correcciones de Francisco:

```
CONTGI<-0, CONTAI<-0, CONTGA<-0, CONTAA<-0, CONTATM<-0
Leer ApyN
Mientras (ApyN <> "ZZZZ ZZZZZ")
  Leer cargo, sexo, edad, cond
  Si cargo=="IM/100"        Si cargo=="A/200"         Si cargo=="TM/300"        (ninguna)
    V: CONTGI++               V: CONTGA++                V: Si 20<=edad<=30        F: Informar "Error de
       Si sexo=="M"              Si 25<=edad<=30              V: CONTATM++             tipeo: el cargo no
         V: Si 25<=edad<=30        V: CONTAA++                F: (nada)                corresponde a ninguna
              V: Si cond==1        F: (nada)                                           referencia"
                   V: CONTAI++
                   F: (nada)
              F: (nada)
         F: (nada)
  Leer ApyN
Informar "Se presentaron:", CONTGI, "postulantes para IM/100, de los cuales", CONTAI, "cumplen las condiciones"
Si CONTAI>=3   V: Informar "Se cubren los cargos solicitados de IM/100"     F: Informar "No se cubren..."
Informar "Se presentaron:", CONTGA, "postulantes para el cargo A/200"
Si CONTAA>=2   V: Informar "Se cubren los cargos solicitados de A/200"     F: Informar "No se cubren..."
Informar "Los aspirantes en condiciones para TM/300 son:", CONTATM
```

(La tabla de arriba ya "aplana" la cascada de cargos en 4 columnas — así es como se dibuja, ver §4.)

## 3. Método: unidades del grillado

| Constante | Valor | Uso |
|---|---|---|
| `ROW_H` | 12 mm | alto de una fila simple (una condición, una acción, una lectura) |
| `ROW_H_2L` | 18 mm | alto de una fila con texto largo que ocupa 2 renglones (los `Informar` finales con varias variables) |
| `INDENT` | 3 mm | cuánto se corre el borde izquierdo al entrar un nivel más adentro en una selección anidada |
| `F_FINO` | 5 mm | ancho de una columna "F" que solo dice "(nada)" — se dibuja como una rayita diagonal, **sin escribir texto**, igual que en las fotos de Francisco y del pizarrón |

**Altura de texto según profundidad** (para que todo entre legible):

| Nivel | Dónde | Altura de texto sugerida |
|---|---|---|
| 0 | Inicialización, lecturas, `Mientras`, `Informar` finales | 3.5 mm |
| 1 | Encabezados de la cascada de cargos (`Si cargo==...`) | 3 mm |
| 2 | `CONTGI++`, `CONTGA++`, encabezados `Si sexo`/`Si edad` | 2.8 mm |
| 3 | `Si edad` (rama IM/100), `Si cond==1` | 2.4 mm |
| 4 | `CONTAI++`, `CONTAA++`, `CONTATM++`, "(nada)" | 2.2 mm |
| — | Mensaje "Error de tipeo..." | 2.5 mm (ancho generoso, ver §4.4) |

Todo el diagrama mide **222 mm de alto** con estas medidas, contra 257 mm disponibles — hay margen de sobra (~35 mm) para ajustar cualquier fila un poco si al dibujar te queda justo.

## 4. Tabla de coordenadas

Sistema: **X crece hacia la derecha, Y crece hacia arriba** (como ya está el .dxf). Todas las coordenadas son absolutas, en mm, para usar directo en LibreCAD (`Línea`, `Rectángulo`, `Texto múltiple`).

### 4.1 Rectángulo exterior y secuencia de nivel superior

Ancho fijo para todo lo de nivel 0: **X: 30 a 195** (dejás 5 mm de aire contra el marco interior a cada lado).

| Bloque | Y superior | Y inferior | Contenido |
|---|---|---|---|
| Rectángulo exterior | 260 | 38 | — (dibujalo primero, es el contorno de todo el algoritmo) |
| Título (fuera del rectángulo, en el hueco bajo el rótulo) | 267 | 260 | Texto centrado ~(112,263): `DIAGRAMA CHAPIN — EJERCICIO 13` |
| **B1** Inicialización | 260 | 248 | `CONTGI←0, CONTAI←0, CONTGA←0, CONTAA←0, CONTATM←0` |
| **B2** Lectura previa | 248 | 236 | `Leer ApyN` |
| **B3** Mientras (bloque completo) | 236 | 128 | ver §4.2 |
| **B4** Informar final 1 (2 líneas) | 128 | 110 | `Informar "Se presentaron:", CONTGI, "postulantes para IM/100, de los cuales", CONTAI, "cumplen las condiciones"` |
| **B5** Si CONTAI≥3 | 110 | 86 | ver desglose abajo |
| **B6** Informar final 2 | 86 | 74 | `Informar "Se presentaron:", CONTGA, "postulantes para el cargo A/200"` |
| **B7** Si CONTAA≥2 | 74 | 50 | ver desglose abajo |
| **B8** Informar final 3 | 50 | 38 | `Informar "Los aspirantes en condiciones para TM/300 son:", CONTATM` |

**B5** (X30-195, Y110-86): encabezado en 110→98 con texto `CONTAI>=3` centrado; debajo, fila 98→86 partida en X≈113: **V** (30-113) `Informar "Se cubren los cargos solicitados de IM/100"`, **F** (113-195) `Informar "No se cubren los cargos solicitados de IM/100"`.

**B7** (X30-195, Y74-50): mismo esquema — encabezado 74→62 `CONTAA>=2`; fila 62→50 partida en X≈113: **V** `Informar "Se cubren los cargos solicitados de A/200"`, **F** `Informar "No se cubren los cargos solicitados de A/200"`.

### 4.2 Interior del `Mientras` (bloque B3, Y236→128)

- **Encabezado del bucle**: fila 236→224, ancho completo X30-195. Texto: `Mientras (ApyN <> "ZZZZ ZZZZZ")`.
- **Cuerpo del bucle**: indentado, arranca en **X=36** (dejás 6 mm de margen a la izquierda contra el borde del rectángulo — ahí va la flecha de alcance del bucle, ver §5).
  - Fila 224→212 (X36-195): `Leer cargo, sexo, edad, cond`
  - Fila 212→200 (X36-195): **banda de la cascada de cargos** — acá van los 3 chequeos de `cargo` como una selección en cascada dibujada en columnas paralelas (§4.3), no anidada hacia adentro.
  - Zona de contenido: Y200→140, dividida en 4 columnas paralelas (§4.3)
  - Fila 140→128 (X36-195): `Leer ApyN`

### 4.3 La cascada de cargos — 4 columnas paralelas

Esta es la parte que copia literal la técnica de las fotos: en vez de anidar el `Sino` cada vez más angosto hacia la derecha (que te deja sin espacio abajo), las 3 condiciones de cargo se dibujan **una al lado de la otra**, todas arrancando a la misma altura. Girá 90° la cabeza al mirar `ejercicio_13_0.jpeg` si hace falta para verlo — es exactamente este patrón.

Divisiones verticales de **X36 a X195** en la banda Y212→140 (dibujalas primero, de punta a punta, antes de rellenar el contenido de cada columna):

| Línea vertical en X= | Desde Y | Hasta Y |
|---|---|---|
| 82 | 212 | 140 |
| 118 | 212 | 140 |
| 154 | 212 | 140 |

Esto te da 4 columnas: **IM/100** (36-82, 46mm), **A/200** (82-118, 36mm), **TM/300** (118-154, 36mm), **Error** (154-195, 41mm).

**Banda de encabezado (Y212→200)**, dentro de cada columna:

| Columna | Texto | Marca V/F |
|---|---|---|
| IM/100 (36-82) | `Si cargo=="IM/100"` | `V` abajo-izquierda (sigue en esta columna); `F` abajo-derecha, junto a X=82 (si falso, pasa a la próxima) |
| A/200 (82-118) | `Si cargo=="A/200"` | igual esquema, `F` junto a X=118 |
| TM/300 (118-154) | `Si cargo=="TM/300"` | igual esquema, `F` junto a X=154 |
| Error (154-195) | *(sin texto — es el F final de la cascada, cae directo al mensaje de error)* | — |

**Contenido de cada columna (Y200 hacia abajo):**

**Columna IM/100 (X36-82)** — la más profunda, 3 niveles anidados:

| Elemento | X1 | Y1 | X2 | Y2 | Contenido |
|---|---|---|---|---|---|
| Acción | 36 | 200 | 82 | 188 | `CONTGI++` |
| Encabezado sexo | 36 | 188 | 82 | 176 | `Si sexo=="M"` |
| — división V/F sexo | vertical en X=77, de Y176 a Y140 | | | | |
| Encabezado edad | 39 | 176 | 77 | 164 | `Si 25<=edad<=30` |
| sexo-F (rayita, sin texto) | 77 | 176 | 82 | 140 | `/` |
| — división V/F edad | vertical en X=72, de Y164 a Y140 | | | | |
| Encabezado cond | 42 | 164 | 72 | 152 | `Si cond==1` |
| edad-F (rayita) | 72 | 164 | 77 | 140 | `/` |
| — división V/F cond | vertical en X=67, de Y152 a Y140 | | | | |
| cond-V | 42 | 152 | 67 | 140 | `CONTAI++` |
| cond-F (rayita) | 67 | 152 | 72 | 140 | `/` |

**Columna A/200 (X82-118)** — 1 nivel anidado, termina en Y164 (queda un espacio en blanco entre 164 y 140, es normal — la fila comparte el mismo piso que la columna IM/100 pero acá el contenido es más corto):

| Elemento | X1 | Y1 | X2 | Y2 | Contenido |
|---|---|---|---|---|---|
| Acción | 82 | 200 | 118 | 188 | `CONTGA++` |
| Encabezado edad | 82 | 188 | 118 | 176 | `Si 25<=edad<=30` |
| — división V/F | vertical en X=113, de Y176 a Y164 | | | | |
| edad-V | 82 | 176 | 113 | 164 | `CONTAA++` |
| edad-F (rayita) | 113 | 176 | 118 | 164 | `/` |

**Columna TM/300 (X118-154)** — 1 nivel anidado, sin acción previa (por eso el contador es único, corrección de Francisco), termina en Y176:

| Elemento | X1 | Y1 | X2 | Y2 | Contenido |
|---|---|---|---|---|---|
| Encabezado edad | 118 | 200 | 154 | 188 | `Si 20<=edad<=30` |
| — división V/F | vertical en X=149, de Y188 a Y176 | | | | |
| edad-V | 118 | 188 | 149 | 176 | `CONTATM++` |
| edad-F (rayita) | 149 | 188 | 154 | 176 | `/` |

**Columna Error (X154-195)** — sin encabezado propio (cae acá directo cuando ninguna de las 3 referencias matchea):

| Elemento | X1 | Y1 | X2 | Y2 | Contenido |
|---|---|---|---|---|---|
| Mensaje | 154 | 200 | 195 | 176 | `Informar "Error de tipeo: el cargo ingresado no corresponde a ninguna referencia"` — MTEXT con ese ancho (41mm), LibreCAD ajusta el salto de línea solo (te va a quedar en 3-4 renglones) |

### 4.4 Por qué esto entra cómodo

Con este esquema el punto más angosto de todo el diagrama es `cond-V` (25mm) — sobra para escribir `CONTAI++` con letra de 2.2mm sin apretar. Compará con lo que pasaría si anidaras la cascada de cargos hacia adentro en vez de en paralelo: el ancho se te iba angostando a la mitad en cada nivel y llegabas al mensaje de error con ~14mm disponibles — por eso ni el pizarrón ni Francisco lo dibujan así.

## 5. Toques de fidelidad al estilo del profesor (opcionales pero recomendados)

Según las notas de `candidatos_parcial_chapin.md` (sección "estilo del profesor") y visibles en las fotos:

1. **Flecha de alcance del bucle**: una línea vertical fina en **X=33**, de **Y=224 a Y=128** (en el margen de 6mm que dejaste a la izquierda del cuerpo del `Mientras`). Marca visualmente hasta dónde llega el `Mientras` — es un agregado propio del profesor, no notación estricta de Chapin, pero es lo que reconoce de un vistazo.
2. **Círculos de inciso**, como los marcó el profesor a mano en `ejercicio_13_2.jpeg`: círculos chicos (~4mm de diámetro) en el margen izquierdo, **X≈27** (en el hueco de 5mm entre el marco interior y tu rectángulo):

   | Círculo | Y aproximado | Junto a |
   |---|---|---|
   | `1b` | 122 | mitad superior de B4 (CONTGI) |
   | `1c` | 114 | mitad inferior de B4 (CONTAI) |
   | `1a` | 98 | encabezado de B5 |
   | `2a` | 80 | B6 |
   | `2b` | 62 | encabezado de B7 |
   | `3` | 44 | B8 |

3. **Convención de nombres**: minúsculas no aplican acá (no hay variables auxiliares tipo `tmin`) — todo son contadores, así que todo va en **mayúsculas** (`CONTGI`, `CONTAI`, etc.), consistente con cómo los usa el profesor.
4. **Asignación**: usá `<-` (o la flecha `←` si tu fuente la tiene) en la inicialización, no `=`.

## 6. Orden de dibujo sugerido en LibreCAD

1. Cambiá a la capa `GEOMETRIA`.
2. Rectángulo exterior (30,260)-(195,38).
3. Las 7 líneas horizontales de ancho completo que separan B1...B8 (Y=248,236,224,128,110,98,86,74,62,50 — todas de X30 a X195, salvo 224 que ya es el techo del cuerpo del bucle).
4. Dentro del `Mientras`: la línea de Y=212 y Y=200 (ancho X36-195), después las 3 verticales de la cascada (X=82,118,154, de Y212 a Y140).
5. Subdivisiones internas de cada columna (sexo/edad/cond en IM/100; edad en A/200 y TM/300) — de afuera hacia adentro.
6. Divisores V/F de B5 y B7 (verticales en X≈113).
7. Todos los textos (`MTEXT`), de arriba hacia abajo — así controlás que cada uno entre en su celda antes de seguir.
8. Los toques opcionales de §5 al final.

Guardá seguido — LibreCAD no autoguarda.

---

**Fuentes:** `candidatos_parcial_chapin.md`, `diagramacion_estructurada.html`, fotos del pizarrón (`ejercicio_13_1.jpeg`, `ejercicio_13_2.jpeg`) y resolución de Francisco Sticotti (`ejercicio_13_0.jpeg`), enunciado (`consignas.jpeg`), y la geometría existente de `parcial_1.dxf` (marco y rótulo). Cátedra: Fundamentos de Informática, Ing. Aldo J. Alaniz, Dto. Ingeniería Mecánica, UTN FRBA.
