# Diagrama Chapin Ejercicio 13 (`parcial_1.dxf`) — documentación as-built

> Este archivo documenta **cómo quedó realmente armado** el diagrama estructurado (Chapin/Nassi-Shneiderman) del Problema 13 dentro de `parcial_1.dxf`, que es la **versión final** entregada. No es una guía de construcción a futuro (esa fue su versión anterior) — es la referencia de coordenadas y contenido tal como está, por si hay que corregir algo puntual, revisar una celda, o entender la técnica usada para reproducirla en otro ejercicio.
>
> Alcance: solo el diagrama estructurado (capas `2H`/`2B`/`0`, dentro del marco). La parte escrita de justificación (los 3 párrafos tipo "las variables que uso son contadoras...") va aparte, en hoja rayada — no está en este `.dxf`.

## 0. De dónde sale esta versión

Se partió de tres fuentes, en este orden de prioridad:

1. **Fotos reales del pizarrón** (`ejercicio_13_1.jpeg`, `ejercicio_13_2.jpeg`) — la resolución del Ing. Alaniz, con los círculos de incisos (1a,1b,1c,2a,2b,3) marcados a mano en `ejercicio_13_2.jpeg`.
2. **Resolución de Francisco Sticotti** (`ejercicio_13_0.jpeg`) — mismo esqueleto, con las 3 correcciones ya incorporadas (contador único en TM/300, ramas F que también informan, "Error de tipeo" para cargo inválido).
3. `candidatos_parcial_chapin.md` y `diagramacion_estructurada.html` — que documentan por qué esa es la versión a reproducir.

**La técnica finalmente usada para dibujar la cascada de cargos no fue la de "columnas paralelas" que planeaba la primera versión de esta guía.** Al armarlo en LibreCAD terminó saliendo el símbolo de selección Chapin clásico — un **trapecio con vértice** (el rectángulo se angosta hacia un punto, con la condición arriba y las ramas Verdadero/Falso saliendo de las esquinas inferiores) — y esos trapecios se anidan igual que en las fotos, pero mediante esta forma en vez de columnas rectas con divisores verticales. Ver §4.3.

## 1. Área de trabajo y capas (confirmado leyendo el `.dxf` final)

| Elemento | Coordenadas (mm) | Capa |
|---|---|---|
| Marco exterior de hoja (A4) | (0,0) – (210,297) | `MARCO` |
| Marco interior | (25,10) – (200,287) | `MARCO` |
| Rótulo (franja superior) | (25,267) – (200,287) | `ROTULO_2B` / `ROTULO_2H` |
| Diagrama (contorno general) | (30,38) – (195,260) | `2H` |

El rótulo tiene los datos: **Paredes Sergio, Leg. 260.861-3**, materia "Fundamentos de Informatica", "S1554", "Ej. 13", fecha "17-09-26".

**Capas realmente usadas para el diagrama** (distinto de lo que planeaba la versión anterior de esta guía, que preveía una única capa `GEOMETRIA` para todo):

| Capa | Contenido real |
|---|---|
| `2H` | Toda la geometría estructural: rectángulos de bloque, los trapecios de decisión (líneas diagonales + verticales), divisores. Nombre por convención de dureza de lápiz (2H = trazo fino de construcción), igual criterio que `ROTULO_2H`. |
| `2B` | Todo el texto (`MTEXT`) — instrucciones, condiciones, `True`/`False`. Mismo criterio que `ROTULO_2B` (2B = trazo grueso, para lo que se lee). |
| `0` | Líneas finas auxiliares: reglas de margen a la izquierda del cuerpo del bucle y pequeñas marcas ("banderines") junto a las etiquetas `True`/`False` de cada decisión. |
| `GEOMETRIA` | Casi sin uso: quedaron solo 4 segmentos horizontales cortos, de conexión entre celdas vecinas de la cascada (ver §4.3). La capa vacía que preveía la guía original para "todo el diagrama" no terminó siendo el contenedor principal. |

No se dibujó ningún texto de título por encima de B1 (la línea "DIAGRAMA CHAPIN — EJERCICIO 13" que planeaba la versión anterior de esta guía **no está** en el `.dxf` final) — el diagrama arranca directo en el bloque de inicialización, a Y=260.

## 2. El algoritmo tal como quedó escrito en el diagrama

Texto literal extraído del `.dxf` (los saltos de línea `\P` son los que usa LibreCAD dentro de un mismo `MTEXT`):

```
CONTGI->0;    CONTGA->0;    CONTATM->0;
CONTAI->0;    CONTAA->0;
Leer ApyN
While (ApyN <> "ZZZZ ZZZZZ")
  Leer cargo, sexo, edad, cond
  cargo == "IM/100"      cargo == "A/200"       cargo == "TM/300"      (False final)
    True: CONTGI++          True: CONTGA++          True: 20 < edad < 30   → Informar "Error de Tipeo"
      sexo == "M"              25 < edad < 30           True: CONTATM++
        True: 25<edad<30          True: CONTAA++          False: (nada)
          True: cond == 1          False: (nada)
            True: CONTAI++
            False: (nada)
          False: (nada)
        False: (nada)
  Leer ApyN
Informar "Se presentaron " CONTGI " postulantes para el cargo IM/100, de los cuales " CONTAI " cumplen las condiciones solicitadas."
CONTAI > 3   True: Informar "Sí se cubren los cargos solicitados de IM/100."   False: Informar "No se cubren los cargos solicitados de IM/100."
Informar "Se presentaron " CONTGA " postulantes para el cargo A/200."
CONTAA > 2   True: Informar "Sí se cubren los cargos solicitados de A/200."   False: Informar "No se cubren los cargos solicitados de A/200."
Informar "Se presentaron " CONTATM " postulantes que cumplen las condiciones para el cargo TM/300."
```

Diferencias respecto a la versión de pizarrón/`candidatos_parcial_chapin.md` que quedaron fijadas al pasarlo a CAD (elección propia, consistente en todo el archivo):

- **Asignación**: `->` en vez de `<-` (ej. `CONTGI->0;`), con punto y coma al final.
- **Comparación**: `==` (estilo lenguaje de programación) en vez de `=`.
- **Bucle**: `While (...)` en inglés, no `Mientras (...)`.
- **Ramas**: etiquetadas `True` / `False`, no `V` / `F`.
- Los mensajes finales dicen **"Se presentaron"** (no "Se presentaron:") y las respuestas de cobertura dicen **"Sí se cubren..." / "No se cubren..."** (con tilde en "Sí").

## 3. Tamaños de letra realmente usados

No se siguió una tabla fija por nivel de anidamiento como preveía la versión anterior de esta guía — la altura de cada `MTEXT` se ajustó a mano según el ancho disponible en esa celda puntual (los trapecios angostan de forma no uniforme). A modo de referencia, así quedó agrupado:

| Elemento | Altura de texto |
|---|---|
| `While(...)`, `Leer ApyN`, `Leer cargo, sexo, edad, cond` (nivel 0 del cuerpo) | 7 mm |
| Inicialización (`CONTxx->0;`) | 4 mm |
| Decisión `cargo=="IM/100"`, sus `True`/`False`, `CONTGI++`, `CONTGA++`, `CONTAA++`, decisión `sexo=="M"` | 5 mm |
| Decisión `cargo=="A/200"` y su `True`/`False` de esa fila | 4 mm |
| Decisiones anidadas de edad/cond (IM/100 y A/200) y sus `True`/`False` | 3–4 mm |
| Decisión `cargo=="TM/300"`, su anidada `20<edad<30`, y el mensaje de error | 2 mm (la zona más angosta de todo el diagrama) |
| `CONTAI++`, `CONTATM++` | 2.2–2.5 mm |
| Bloques finales (`CONTAI>3`, `CONTAA>2`, mensajes `Sí`/`No`, los 3 `Informar` de cierre) | 3 mm |

Altura total del diagrama: **222 mm** (Y=38 a Y=260), dentro de los 257 mm disponibles bajo el rótulo.

## 4. Coordenadas tal como están en el `.dxf`

Sistema: **X crece hacia la derecha, Y crece hacia arriba**. Coordenadas absolutas en mm.

### 4.1 Bloques de nivel superior

Ancho de nivel 0: **X: 30 a 195**.

| Bloque | Y superior | Y inferior | Contenido |
|---|---|---|---|
| **B1** Inicialización | 260 | 248 | 3 celdas lado a lado (ver abajo) |
| **B2** Lectura previa | 248 | 236 | `Leer ApyN` en (31,242), h=7 |
| **B3** Mientras (bloque completo) | 236 | 128 | ver §4.2 |
| **B4** Informar final 1 | 128 | 110 | `Informar "Se presentaron " CONTGI " postulantes para el cargo IM/100, de\Plos cuales " CONTAI " cumplen las condiciones solicitadas."` en (31,119), h=3 |
| **B5** Decisión `CONTAI > 3` | 110 | 86 | trapecio de decisión, ver desglose abajo |
| **B6** Informar final 2 | 86 | 74 | `Informar "Se presentaron " CONTGA " postulantes para el cargo A/200."` en (31,79), h=3 |
| **B7** Decisión `CONTAA > 2` | 74 | 50 | trapecio de decisión, ver desglose abajo |
| **B8** Informar final 3 | 50 | 38 | `Informar "Se presentaron " CONTATM " postulantes que cumplen las\Pcondiciones para el cargo TM/300."` en (31,44), h=3 |

**B1** (X30-195, Y260-248) — tres celdas de inicialización lado a lado, separadas por líneas verticales en X=31, X=66 y X=101 (estas verticales continúan hacia abajo hasta Y=236, atravesando también B2):

| Celda | X | Contenido |
|---|---|---|
| 1 | 31 | `CONTGI->0;` / `CONTAI->0;` (2 líneas, un solo `MTEXT`, h=4) |
| 2 | 66 | `CONTGA->0;` / `CONTAA->0;` (2 líneas, un solo `MTEXT`, h=4) |
| 3 | 101 | `CONTATM->0;` (h=4, en Y=257 en vez de 254 — centrado más arriba por ser una sola línea) |

**B5** (X30-195, Y110-86): trapecio de decisión — rectángulo (30,98)-(195,110) con vértice en (112.5,98); condición `CONTAI > 3` en (112.5,109) h=3; `True` en (31,103), `False` en (194,103), ambos h=3. Debajo, fila (30,86)-(195,98) partida en X=112.5: **True** → `Informar "Sí se cubren los\Pcargos solicitados de IM/100."` en (31,92); **False** → `Informar "No se cubren los\Pcargos solicitados de IM/100."` en (194,92), ambos h=3.

**B7** (X30-195, Y74-50): mismo esquema — trapecio (30,62)-(195,74), vértice (112.5,62); condición `CONTAA > 2` en (112.5,73); `True` (31,67), `False` (194,67). Debajo, fila (30,50)-(195,62) partida en X=112.5: **True** → `Informar "Sí se cubren los\Pcargos solicitados de A/200."` (31,56); **False** → `Informar "No se cubren los\Pcargos solicitados de A/200."` (194,56).

### 4.2 Interior del `Mientras` (bloque B3, Y236→128)

- **Encabezado del bucle**: fila (30,224)-(195,236). Texto `While (ApyN <> "ZZZZ ZZZZZ")` en (31,230), h=7.
- **Cuerpo del bucle**, indentado a X=36-37:
  - Fila (36,212)-(195,224): `Leer cargo, sexo, edad, cond` en (37,218), h=7.
  - Fila (36,140)-(195,212): **cascada de decisiones de cargo**, ver §4.3.
  - Fila (36,128)-(195,140): `Leer ApyN` en (37,134), h=7.
- Sobre el margen izquierdo del cuerpo (X≈31-37) hay una regla vertical fina en capa `0` que corre a lo largo de cada tramo del cuerpo, con pequeñas marcas ("banderines") de ~3mm junto a cada etiqueta `True`/`False` — es el equivalente real a lo que la versión anterior de esta guía planeaba como una única "flecha de alcance del bucle" en X=33: en la práctica quedó repartida en varios segmentos cortos en vez de una sola línea continua.

### 4.3 La cascada de cargos — trapecios anidados (símbolo de selección Chapin)

Cada decisión se dibuja como un **rectángulo que se angosta hasta un punto** (el vértice), con la condición escrita arriba, `True` en la esquina inferior izquierda y `False` en la inferior derecha. Debajo del vértice, una línea vertical separa la rama Verdadero (izquierda) de la Falso (derecha), y cada rama sigue bajando con ese mismo ancho hasta que se resuelve (una acción, otra decisión anidada, o queda vacía = "(nada)").

La cascada de los 3 cargos avanza **hacia la derecha por la rama Falso**: si `cargo != "IM/100"`, la zona Falso de esa decisión contiene directamente la siguiente decisión (`cargo == "A/200"`), y así con `TM/300`; si ninguna matchea, la Falso final cae en el mensaje de error. Dentro de la rama Verdadero de `IM/100` es donde se anida en profundidad (sexo → edad → cond), igual que en las fotos.

**Fila 1 (Y212→200)** — decisión `cargo == "IM/100"`: rectángulo (36,200)-(195,212), vértice (115.5,200). Condición en (115.5,211) h=5. `True` en (37,206), `False` en (194,206), h=5.

- **Zona Verdadero** (X36-115.5): sigue en la Fila 2A.
- **Zona Falso** (X115.5-195): sigue en la Fila 2B con la decisión `A/200`.

**Fila 2A (Y200→188), rama IM/100 verdadera** — `CONTGI++` en (37,194), h=5. Rectángulo (36,188)-(115.5,200).

**Fila 2B (Y200→188), rama IM/100 falsa** — decisión `cargo == "A/200"`: rectángulo (115.5,188)-(195,200), vértice (155.25,188). Condición en (155.25,199) h=4. `True` en (116.5,192), `False` en (194,192), h=4.

- **Zona Verdadero** (X115.5-155.25): sigue en Fila 3B.
- **Zona Falso** (X155.25-195): sigue en Fila 3C con la decisión `TM/300`.

**Fila 3A (Y188→176)** — decisión `sexo == "M"` (rama Verdadero de IM/100 continuada): rectángulo (36,176)-(115.5,188), vértice (105.5625,176). Condición en (110.75,187) h=4. `True` en (37,182) h=5, `False` en (114.5,181) h=5. La rama Falso de `sexo` no sigue a ninguna fila más (queda "(nada)").

**Fila 3B (Y188→176)** — `CONTGA++` (rama A/200 verdadera) en (116.5,182), h=5. Esta celda comparte el mismo rectángulo ancho (115.5,176)-(195,188) con la Fila 3C de al lado; están separadas por una línea vertical en X=155.25 dibujada aparte (no por dos rectángulos distintos).

**Fila 3C (Y188→176)** — decisión `cargo == "TM/300"` (rama A/200 falsa): dentro del mismo rectángulo (115.5,176)-(195,188), vértice en (180.09375,176). Condición en (175.125,187) h=2. `True` en (156,177) h=5, `False` en (194,177) h=5.

- **Zona Verdadero** (X155.25-180.094): sigue en Fila 4B.
- **Zona Falso** (X180.094-195): mensaje de error, sin más filas (ver abajo).

**Fila 4A (Y176→164)** — decisión `25 < edad < 30` (rama sexo=="M" verdadera, IM/100): rectángulo (36,164)-(105.5625,176), vértice (96.8671875,164). Condición en (100.5625,175) h=3. `True` en (37,170) h=5, `False` en (104.5625,168) h=5.

**Fila 4B (Y176→164)** — decisión `25 < edad < 30` (rama A/200 verdadera, anidada bajo `CONTGA++`): rectángulo con vértice (151,164), dentro del ancho 115.5-155.25. Condición en (152,175) h=2. `True` en (116.5,165) h=4, `False` en (154.25,165) h=2.

**Fila 4C (Y176→140)** — decisión `20 < edad < 30` (rama TM/300 verdadera): vértice (176,164), dentro del ancho 155.25-180.094. Condición en (167.671875,175) h=2. `True` en (156,165) h=3, `False` en (179,165) h=2.

**Zona Error** (X180.094-195, Y176 hacia abajo): mensaje `Informar\P"Error\Pde\PTipeo"` en (181,175), h=2 — sin decisión propia, es la caída final de la cascada.

**Fila 5A (Y164→152)** — decisión `cond == 1` (rama edad verdadera, IM/100): rectángulo (36,152)-(96.8671875,164), vértice (89.2587890625,152). Condición en (92.8671875,163) h=3. `True` en (37,158) h=5, `False` en (95.8671875,156) h=5.

**Fila 5B (Y164→140)** — `CONTAA++` (rama edad verdadera, A/200; no tiene más anidamiento, la celda ocupa todo el resto de la profundidad) en (116.5,158), h=5.

**Fila 5C (Y164→140)** — `CONTATM++` (rama edad verdadera, TM/300; tampoco anida más) en (156,163), h=2.5.

**Fila 6 (Y152→140)** — `CONTAI++` (rama cond verdadera, el punto más profundo de toda la cascada) en (37,146), h=2.2 aprox. Todas las demás ramas Falso de esta zona (sexo-F, edad-F de IM/100, cond-F) quedan vacías — "(nada)", sin texto, tal como en las fotos.

Las cuatro líneas horizontales cortas en capa `GEOMETRIA` — (95.625,176)-(115.5,176), (88.171875,164)-(105.5625,164), (81.650390625,152)-(96.8671875,152) y (175.125,176)-(195,176) — son los conectores que cierran visualmente el borde de cada celda "(nada)" contra la celda vecina.

### 4.4 Por qué terminó siendo así

El trapecio con vértice es la forma estándar de la selección Chapin/Nassi-Shneiderman (la misma que usan el profesor y Francisco en las fotos si se las mira con atención) — no una simplificación. Al construirlo en LibreCAD con líneas y no con el bloque predefinido de un software de diagramación, salió natural resolverlo como "rectángulo + 2 diagonales + 1 vertical" en cascada, que es exactamente este patrón. El punto más angosto de todo el diagrama termina siendo la franja `TM/300`/Error (h=2mm), consistente con que ahí conviven 2 niveles de anidamiento (cargo→edad) en el tramo más a la derecha, con menos ancho disponible que en la rama IM/100.

## 5. Toques de fidelidad al estilo del profesor — qué quedó y qué no

Repasando contra lo que preveía la versión anterior de esta guía (basada en `candidatos_parcial_chapin.md` y las fotos):

- **Círculos de inciso** (1a,1b,1c,2a,2b,3) marcados a mano por el profesor en `ejercicio_13_2.jpeg`: **no se dibujaron** en el `.dxf` final (no hay ninguna entidad `CIRCLE` en todo el archivo). Si se quieren agregar, van en el margen izquierdo, X≈27, junto a cada bloque (B4, B5, B6, B7, B8).
- **Flecha de alcance del bucle** en una única línea X=33: no quedó así — en su lugar hay varios tramos de regla + banderines cortos en capa `0`, descriptos en §4.2.
- **Convención de mayúsculas** para contadores (`CONTGI`, `CONTAI`, etc.): sí se respetó, consistente en todo el archivo.
- **Asignación** con flecha: se usó `->` (no `<-` ni `←`), con punto y coma final — una decisión propia al tipear en CAD, no la notación exacta de Chapin, pero consistente en todas las inicializaciones.
- **Comparación**: se usó `==` en vez de `=` — mismo criterio, elección propia consistente.

## Fuentes

`candidatos_parcial_chapin.md`, `diagramacion_estructurada.html`, fotos del pizarrón (`ejercicio_13_1.jpeg`, `ejercicio_13_2.jpeg`), resolución de Francisco Sticotti (`ejercicio_13_0.jpeg`), enunciado (`consignas.jpeg`), y la geometría real del `parcial_1.dxf` final (marco, rótulo y diagrama — coordenadas y textos extraídos directamente del archivo). Cátedra: Fundamentos de Informática, Ing. Aldo J. Alaniz, Dto. Ingeniería Mecánica, UTN FRBA.
