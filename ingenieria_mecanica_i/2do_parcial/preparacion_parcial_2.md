# Preparación Parcial 2 — Ingeniería Mecánica I

**Profesor:** Abud  
**Fecha del examen:** a confirmar  
**Modalidad:** multiple choice — las incorrectas restan; las no respondidas valen 0 (mismo régimen que el 1er parcial)  
**Temario anunciado por Abud:** máquinas y herramientas (transformación de la materia prima, Unidad VII) · marcas, patentes y derecho de autor · mecánica rotacional (todo) · ingeniería de control automático · teoría del engrane · elementos de máquinas (árboles y ejes, entre otros)  
**Estado:** banco de **102 preguntas reales únicas** — 62 dentro del temario anunciado (bloques RO, MH, SV, CA, EM, PI), 7 "comodines" de parciales recientes (VA) y 33 de 2° parciales viejos fuera del temario (VJ).  
**Preguntas sugeridas (inventadas, no son de examen):** van en archivo aparte → [preguntas_sugeridas_parcial_2.md](preguntas_sugeridas_parcial_2.md)

---

## Convención de identificadores

**Fuentes** (detalle y ubicación al final del documento):

| Sigla | Fuente | Trae respuestas |
|---|---|---|
| `CV21` | 2° parcial del campus virtual, cursada 2021 (comisiones S1021/S1022), 30 preguntas | **Sí — clave oficial** ("La respuesta correcta es…") |
| `COMP` | Compilado "PREGUNTAS PARCIAL ABUD": un 2° parcial numerado 1–30 (≈2018–2019) + listas sueltas | Sí — resaltadas por alumnos |
| `P13` | Fotos del 2° parcial, Tema 1, diciembre 2013, 30 preguntas | No (se cruzan con `COMP`) |
| `FIN14` | Final "Tema 14", 32 preguntas | Sí — marcadas por alumnos |
| `F23` | Formulario "Preguntas de repaso — 2° Parcial" (2023), 42 preguntas "sacadas de parciales viejos" | No (la clave se ve recién al enviarlo) |
| `R23` | Resumen manuscrito del 2° parcial (2023) | No tiene preguntas; confirma temario y datos |
| `AP` | Apuntes y diapositivas de cátedra (`material_catedra/`) | — |

**Marcadores de confianza:**

| Marcador | Significado |
|---|---|
| `[OFICIAL]` | La respuesta sale de la clave del campus (`CV21`). Máxima confianza. |
| `[ALUMNOS]` | Respuesta marcada por alumnos (`COMP` o `FIN14`), sin clave oficial; verificada contra el apunte de cátedra. |
| `[DEDUCIDA]` | Ninguna fuente trae la respuesta: se dedujo del apunte de cátedra (la nota cita el texto). |
| `[★×N]` | La pregunta aparece en N fuentes distintas — a más estrellas, más probabilidad de repetición. |
| `[⚠ …]` | Fuentes en conflicto, respuesta en duda o respuesta de cátedra que no coincide con la teoría estricta — leer la nota. |

**Códigos:** `RO` rotacional · `MH` máquinas-herramienta (arranque de viruta) · `SV` procesos sin arranque de viruta · `CA` control automático · `EM` elementos de máquinas · `PI` propiedad intelectual · `VA` comodines recientes · `VJ` 2° parciales viejos.

> En el campus las opciones aparecen mezcladas y sin letra: **memorizá el texto de la respuesta, no la letra**. Las letras de este documento son las de la versión en papel cuando existe.

---

## 1. La ficha de Abud

### Qué tomó en cada modelo conocido

| Tema | 2013 (`P13`) | ≈2018–19 (`COMP` numerado) | 2021 (`CV21`) |
|---|---|---|---|
| Mecánica rotacional | 5 | — | **13** |
| Máquinas-herramienta y procesos de fabricación | — | — | **13** (10 con viruta + 3 sin viruta) |
| Control automático (+ analogía eléctrica) | — | **10** | 2 |
| Marcas, patentes y derecho de autor | — | 4 | — |
| Modelos (termostato, modelo analógico) | 3 | 1 | — |
| Toma de decisiones, problemas, creatividad, sombreros | 8 | 2 | 1 |
| Optimización | 4 | — | — |
| Máquinas en base racional / empírica | 3 | 3 | — |
| Proyecto de máquina, gestión y transferencia de tecnología | 2 | 6 | — |
| Unidades elementales de transformación (UET) | 5 | 3 | — |
| Informes escritos | — | 1 | 1 |
| **Total** | 30 | 30 | 30 |

**Lectura:** el temario cambia de un año a otro, pero **dentro de cada tema las preguntas se repiten textuales** (de las cinco de rotacional de 2013, cuatro están idénticas en 2021 y la quinta aparece en su versión espejo). El temario que anunció este año es la unión del modelo 2021 (rotacional + procesos) con el de ≈2018–19 (control + patentes), más engranajes y elementos de máquinas.

### Cobertura del banco frente al temario anunciado

| Tema anunciado | Preguntas reales | Dónde |
|---|---|---|
| Mecánica rotacional | 14 (13 con clave oficial) | Bloque RO |
| Máquinas y herramientas | 26 (13 con clave oficial) | Bloques MH y SV |
| Control automático | 13 (2 con clave oficial) | Bloque CA |
| Marcas, patentes, derecho de autor | 4 | Bloque PI |
| Elementos de máquinas | 5 — todas de roscas | Bloque EM |
| Teoría del engrane · árboles y ejes | **0** — no apareció ninguna en las fuentes | Solo [sugeridas](preguntas_sugeridas_parcial_2.md) |

### Patrones observados

1. **"¿Quién se mueve?"** Para cada máquina-herramienta pregunta el movimiento relativo entre pieza y herramienta, y lo hace con **dos redacciones** (la del campus y la del final viejo). La tabla de la [sección 3](#3-resumen-de-contenidos-por-bloque) resuelve unas quince preguntas.
2. **Pares espejo en rotacional.** La misma situación preguntada al revés: cambia `ω` → ¿qué pasa con `I`? (nada, RO3) / cambia `I` → ¿qué pasa con `ω`? (disminuye, RO4). Lo mismo con el cilindro que rueda (RO11 vs. RO12) y con la potencia (RO5 vs. RO6).
3. **La opción más completa suele ser la correcta.** En `CV21`, en 10 de 30 preguntas ganó la que más cosas incluía ("en altura, longitudinal y transversalmente"; "momento de inercia, velocidad angular y aceleración angular"; "compactación media y con agujereado"…).
4. **"Solo…" casi siempre es falsa.** En `CV21` hubo 10 opciones con "solo": 9 falsas. La única verdadera: *"Solo en el avance del torpedo"* (MH14).
5. **"Ninguna es correcta" es relleno.** En `CV21` apareció 6 veces y nunca fue la respuesta. (En el 1er parcial sí lo fue una vez: cianuración.)
6. **Respuestas de cátedra que no se razonan, se memorizan:** fresado cilíndrico → "a) y b) son correctas" (MH3); informe escrito → "introducción, antecedentes, metodología y planos" (VA2); derecho de autor → "vida del autor y 50 años más" (PI3).

### Puntaje

Rige lo mismo que en el 1er parcial (ver [estrategia del 1er parcial](../1er_parcial/preparacion_parcial_1.md#1-estrategia-para-el-examen)): responder lo que se sabe, dejar en blanco lo que no se puede acotar.

Dato nuevo, del encabezado del final Tema 14 (32 preguntas): *"para aprobar este examen debe tener como mínimo el 65 % (21) correctamente respondidas y como máximo 5 mal contestadas. La pregunta que no sabe no la conteste."* No está confirmado que el parcial use ese mismo criterio, pero es la única pista escrita de la "tablita" de Abud: **además de sumar correctas, hay un tope de errores**. Con más de 5 mal, el final se desaprueba aunque sobren correctas.

### Checklist antes de entregar

- [ ] ¿La pregunta habla de **energía cinética** del cilindro (→ `I` del centro de masa y `v` del centro de masa) o de **eje instantáneo** (→ `I` respecto del punto de contacto)?
- [ ] ¿Cambia `ω` y preguntan por `I`, o cambia `I` y preguntan por `ω`?
- [ ] Limadora y amortajadora: se mueve la **herramienta**. Cepilladora: se mueve la **pieza**.
- [ ] Torno: gira la **pieza**. Fresadora, alesadora, taladro: gira la **herramienta**. Rectificadora: giran **las dos**.
- [ ] Servomecanismo = **posición** de un elemento mecánico. Regulador = referencia **fija** por períodos largos.
- [ ] Whitworth = **55°** e hilos por **pulgada**. Métrica = **60°** y paso en **mm**.
- [ ] Patente = 20 años **no renovable**. Marca = 10 años **renovable** (usada en los últimos 5). Derecho de autor = vida + 50.

---

## 2. Banco de preguntas reales

---

### Bloque RO — Mecánica rotacional

> Fue el 43 % del parcial 2021. Las 14 preguntas se responden con seis fórmulas del apunte de Abud: `K = ½·I·ω²` · `L = I·ω` · `T_ext = dL/dt` · `P = T·ω = I·ω·α` · `dW = T·dθ` · `ωp = T / (L·sen θ)`.

---

#### RO1 — Se tiene una máquina con un eje girando a cierto número de RPM. En un momento dado se realiza un cambio de marcha en la máquina, cambiando las RPM. Si el momento de inercia no ha variado, su energía cinética rotacional… `[OFICIAL · ★×3]`

- ( ) a. No varía.
- ( ) b. Varía linealmente con la velocidad angular.
- **(✓) c. Varía con el cuadrado de la velocidad angular.**
- ( ) d. Varía con la raíz cuadrada de la velocidad angular.
- ( ) e. Varía con el cubo de la velocidad angular.

> `K = ½·I·ω²`. Con `I` constante, la energía depende de `ω²`. Fuentes: `CV21` (clave), `COMP`, `P13`.

---

#### RO2 — En una máquina que tiene una potencia "P" con un eje que gira a una cierta velocidad angular, se realiza un cambio en una parte de sus piezas con movimiento de rotación, que provoca el aumento del momento rotacional del eje. Si la potencia no varía, la velocidad angular resultante… `[OFICIAL · ★×3]`

- ( ) a. Aumenta.
- ( ) b. Se mantiene constante.
- **(✓) c. Disminuye.**
- ( ) d. Varía con el cuadrado del momento rotacional.

> `P = T·ω`. Si `P` es constante y el momento de rotación `T` aumenta, `ω` tiene que bajar. Fuentes: `CV21` (clave), `COMP`, `P13`.

---

#### RO3 — Un eje apoyado sobre dos rodamientos experimenta, en un momento dado, el aumento de su velocidad angular debido a una fuerza exterior. ¿Cómo afecta este cambio al momento de inercia del conjunto eje y rodamientos? `[ALUMNOS · ★×2]`

- ( ) a. Solo aumenta el momento de inercia del eje.
- ( ) b. Aumenta el momento de inercia del conjunto.
- **(✓) c. El momento de inercia del conjunto se mantiene constante.**
- ( ) d. El momento de inercia del conjunto aumenta con el cuadrado de la velocidad angular.

> `I = Σ m·r²`: según el apunte, el momento de inercia "es función del eje con respecto al que se está moviendo" y "de cómo está distribuida toda la masa". No depende de `ω`. **Par espejo de RO4.** Fuentes: `COMP`, `P13`.

---

#### RO4 — Un eje apoyado sobre dos rodamientos experimenta, en un momento dado, el aumento de su momento de inercia, sin mediar ninguna fuerza exterior. ¿Cómo afecta este cambio a la velocidad angular del eje y rodamientos? `[OFICIAL · ★×2]`

- ( ) No existe relación entre el momento de inercia y la velocidad angular en los sistemas rotacionales.
- ( ) Se mantiene constante.
- **(✓) Disminuye.**
- ( ) Aumenta.

> Sin momento exterior, `L = I·ω` se conserva: `I₁·ω₁ = I₂·ω₂`. Si `I` sube, `ω` baja. **Par espejo de RO3:** allá cambia `ω` y preguntan por `I` (no cambia); acá cambia `I` y preguntan por `ω` (disminuye). Fuentes: `CV21` (clave), `COMP`.

---

#### RO5 — La potencia de un mecanismo que gira en torno a un eje: `[OFICIAL · ★×3]`

- **(✓) a. Es función del momento de inercia, velocidad angular y aceleración angular.**
- ( ) b. Solo es función de la velocidad angular, sin depender de su momento de inercia y aceleración angular.
- ( ) c. Es función de su momento de inercia y velocidad angular, sin depender de su aceleración angular.
- ( ) d. Es función del momento de inercia y la aceleración angular, sin depender de la velocidad angular.

> El apunte llega a `P = I·ω·α` igualando `P = T·ω` con la derivada de `½·I·ω²`. Las tres magnitudes. Fuentes: `CV21` (clave), `COMP` (dos veces), `P13`.

---

#### RO6 — La potencia de un eje montado sobre dos rodamientos es: `[OFICIAL · ★×2]`

- **(✓) Dependiente de la variación de su velocidad angular.**
- ( ) No es dependiente de la variación de su velocidad angular.
- ( ) Aumenta con la disminución de la velocidad angular.
- ( ) Disminuye con el aumento del momento de inercia.

> Misma fórmula que RO5 leída de otro modo: `P = I·ω·α` y `α = dω/dt`, la variación de la velocidad angular. Fuentes: `CV21` (clave), `COMP`.

---

#### RO7 — Se tiene un mecanismo que tiene un determinado trabajo de rotación; si su momento de inercia no varía y repentinamente se produce un aumento de su aceleración angular: `[OFICIAL · ★×2]`

- **(✓) El trabajo de rotación aumenta.**
- ( ) El trabajo de rotación disminuye.
- ( ) El trabajo de rotación es independiente de la aceleración angular.
- ( ) El trabajo de rotación se mantiene constante.

> `dW = T·dθ` y `T = I·α`: con `I` fijo, más `α` es más momento y por lo tanto más trabajo. Fuentes: `CV21` (clave), `COMP`.

---

#### RO8 — Dos ejes apoyados respectivamente en dos rodamientos cada uno están acoplados a través de un engranaje y girando cada uno a sendas velocidades angulares. La cantidad de movimiento angular de cada eje… `[OFICIAL · ★×3 · ⚠ EL COMPILADO RESALTA OTRA]`

- **(✓) a. Es función del producto del momento de inercia y la velocidad angular.**
- ( ) b. Es solo función de la velocidad angular.
- ( ) c. Es función del cuadrado de la velocidad angular y el momento de inercia.
- ( ) d. Es función del cuadrado de la velocidad angular y el cuadrado del momento de inercia.
- ( ) e. La cantidad de movimiento angular no es función ni de la velocidad angular ni del momento de inercia.

> `L = I·ω`. El compilado `COMP` tiene resaltada la b ("solo función de la velocidad angular"): **es un error de quien lo armó**. La clave del campus dice a, y coincide con el apunte. La c es la trampa: describe la energía cinética, no la cantidad de movimiento. Fuentes: `CV21` (clave), `P13`, `COMP`.

---

#### RO9 — Se tiene un mecanismo en donde el momento de rotación de todas las fuerzas exteriores es cero. ¿Qué sucede con su cantidad de movimiento angular? `[OFICIAL · ★×2]`

- **(✓) Se mantiene constante.**
- ( ) No hay relación entre el momento de rotación y la cantidad de movimiento rotacional.
- ( ) Es cero.

> `T_ext = dL/dt`. Si `T_ext = 0`, entonces `dL/dt = 0` y `L` es constante (conservación). "Es cero" es la trampa: lo que vale cero es la variación, no `L`. Fuentes: `CV21` (clave), `COMP`.

---

#### RO10 — Se tiene una polea de radio R, por la cual se levanta una masa m con una velocidad angular ω: `[OFICIAL]`

- **(✓) La cantidad de movimiento angular del sistema es función del momento de inercia, ω, la masa, la velocidad V y R.**
- ( ) La cantidad de movimiento angular del sistema solo es función de ω, v y el radio de la polea R.
- ( ) La cantidad de movimiento angular del sistema polea-masa es independiente de la velocidad de ascenso.
- ( ) La cantidad de movimiento angular del sistema es función de ω, el cuadrado de la velocidad de ascenso, R, el momento de inercia de la polea y la masa m.

> Se suman dos aportes: la polea que gira (`I·ω`) y la masa que sube (`m·v·R`). `L = I·ω + m·v·R`. La última opción falla por "el cuadrado de la velocidad". Fuente: `CV21` (clave).

---

#### RO11 — La energía cinética de un cilindro rodando sobre un plano inclinado con rozamiento es función de: `[OFICIAL]`

- **(✓) De su momento de inercia respecto de su centro de masa y su velocidad de traslación del centro de masa.**
- ( ) Solo de su momento de inercia respecto de su centro de masa.
- ( ) Ninguna es correcta.
- ( ) Sólo de la velocidad de traslación.

> Rodadura = rotación + traslación: `K = ½·I_CM·ω² + ½·M·v_CM²`. **Par espejo de RO12.** Fuente: `CV21` (clave).

---

#### RO12 — En un cilindro que está rodando sobre una superficie con rozamiento, la velocidad de rotación alrededor de su eje instantáneo es función de: `[OFICIAL]`

- ( ) El momento de inercia del cilindro respecto de un eje perpendicular a la dirección de desplazamiento y que pase simultáneamente por su centro de masa y el punto de contacto.
- ( ) El momento de inercia del cilindro respecto de su centro de masa.
- ( ) Ninguna es correcta.
- **(✓) El momento de inercia del cilindro respecto del punto de contacto.**

> El eje instantáneo de rotación pasa por el punto de contacto `P`: `K = ½·I_P·ω²`, con `I_P = I_CM + M·R²`. Si la pregunta dice **"eje instantáneo"**, la respuesta es **"punto de contacto"**; si dice **"energía cinética"** (RO11), es centro de masa. En el intento del campus esta pregunta figura como mal respondida: es de las que confunden. Fuente: `CV21` (clave).

---

#### RO13 — En un mecanismo que está girando con una velocidad angular de precesión ωp, el momento de las fuerzas exteriores τ: `[OFICIAL]`

- **(✓) Se encuentra en un plano perpendicular al formado por ωp y L.**
- ( ) τ se encuentra en el mismo plano formado por ωp y L.
- ( ) τ, ωp y L están en diferentes planos.
- ( ) Ninguna es correcta.

> `τ = ωp × L` (producto vectorial): el resultado es perpendicular al plano de los dos factores. Fuente: `CV21` (clave).

---

#### RO14 — Se tiene un mecanismo donde una de las piezas tiene un movimiento de precesión. Si la cantidad de movimiento angular L de esta aumenta y no hay cambio del sistema de fuerzas exteriores: `[OFICIAL]`

- **(✓) La velocidad angular de precesión disminuye.**
- ( ) La velocidad angular de precesión no varía.
- ( ) Ninguna es correcta.
- ( ) La velocidad angular de precesión aumenta.
- ( ) La velocidad angular de precesión aumenta con el cuadrado de L.

> `ωp = T / (L·sen θ) = r·m·g / L`. El apunte lo dice textual: la velocidad de precesión "es independiente de θ y es inversamente proporcional a L, o sea que si L aumenta ωp disminuye y viceversa". Fuente: `CV21` (clave).

---

### Bloque MH — Máquinas-herramienta (procesos con arranque de viruta)

> Casi todas preguntan lo mismo: **quién gira, quién avanza y en qué dirección**. Hay dos redacciones por máquina: la del campus 2021 y la del final viejo. Conviene estudiarlas de a pares.

---

#### MH1 — En el proceso de arranque de viruta por torneado se pueden obtener piezas cilíndricas. La herramienta tiene un avance respecto de la pieza en forma: `[OFICIAL · ★×2]`

- ( ) Longitudinal y circular.
- ( ) Solo longitudinal.
- ( ) Solo transversal.
- **(✓) Longitudinal y transversal.**

> En el torno la pieza gira (movimiento de corte) y la herramienta, sujeta al carro, "efectúa un movimiento longitudinal y transversal, que constituyen el avance y la penetración". Lo circular es de la pieza, no de la herramienta. Fuentes: `CV21` (clave), `F23`.

---

#### MH2 — Entre las máquinas herramientas está el torno. Diga cómo es el movimiento relativo entre la pieza y la herramienta: `[ALUMNOS]`

- ( ) a. La herramienta gira y la pieza se mueve en sentido longitudinal y transversal.
- **(✓) b. La pieza gira y la herramienta se mueve en sentido longitudinal y transversal.**
- ( ) c. La herramienta gira y la pieza se mueve en sentido vertical, perpendicular al plano de la herramienta.
- ( ) d. La pieza y la herramienta giran simultáneamente.

> Misma idea que MH1 en la redacción del final. La a describe una fresadora; la c, un taladro; la d, una rectificadora. Fuente: `FIN14`.

---

#### MH3 — En el fresado cilíndrico la herramienta (fresa) tiene un movimiento: `[OFICIAL · ★×2 · ⚠ MEMORIZAR]`

- ( ) a. Giratorio en un plano paralelo a la pieza.
- ( ) b. Giratorio en un plano perpendicular a la pieza.
- ( ) c. Giratorio en un plano inclinado a la pieza.
- ( ) d. Alternativo en un plano perpendicular a la pieza.
- **(✓) e. a) y b) son correctas.**

> Es la clave del campus. El apunte solo dice que en el fresado cilíndrico "el eje de la fresa se halla dispuesto paralelamente a la superficie de trabajo"; de ahí no sale de forma evidente que valgan a y b a la vez. **No conviene razonarla: fresado cilíndrico → "a) y b) son correctas".** Fuentes: `CV21` (clave), `F23`.

---

#### MH4 — En el fresado frontal el eje de giro de la fresa se encuentra: `[OFICIAL · ★×2]`

- **(✓) Perpendicular al plano de avance de la pieza.**
- ( ) Paralelo al plano de avance de la pieza.
- ( ) En un ángulo menor al especificado por la herramienta utilizada, respecto del plano de avance de la pieza.
- ( ) En un ángulo menor de 45°, respecto del plano de avance de la pieza.

> Apunte: "En el fresado frontal el eje de la fresa es normal a la superficie de trabajo". Cilíndrico = eje paralelo; frontal = eje perpendicular. Fuentes: `CV21` (clave), `F23`.

---

#### MH5 — En una fresadora horizontal la herramienta y la pieza tienen los siguientes movimientos: `[ALUMNOS]`

- **(✓) a. La herramienta gira y la pieza se mueve en un plano horizontal en sentido longitudinal y transversal.**
- ( ) b. La pieza gira y la herramienta se mueve en un plano horizontal en sentido longitudinal y transversal.
- ( ) c. La herramienta y la pieza giran conjuntamente en diferentes planos.

> Apunte: "La fresa realiza el movimiento circular de corte. Los movimientos de avance y de aproximación son realizados por la pieza". La b es el torno. Fuente: `FIN14`.

---

#### MH6 — El alesado se utiliza para obtener agujeros cilíndricos. El movimiento relativo entre la pieza y la herramienta se forma con: `[OFICIAL · ★×2]`

- ( ) a. La pieza girando y la herramienta fija.
- **(✓) b. La pieza fija y la herramienta girando.**
- ( ) c. La pieza girando y la herramienta desplazándose en forma longitudinal.
- ( ) d. La pieza y la herramienta girando.

> Apunte: "La herramienta va montada sobre un mandril especial giratorio, mientras la pieza es fijada sobre la bancada de la máquina". "Fija" quiere decir que **no gira**: va sujeta a la mesa, que es la que le da el avance (ver MH7). Fuentes: `CV21` (clave), `F23`.

---

#### MH7 — En una alesadora el movimiento de la herramienta y la pieza son: `[ALUMNOS]`

- ( ) a. La herramienta está fija y la pieza gira.
- **(✓) b. La herramienta gira y la pieza se mueve en un plano horizontal.**
- ( ) c. La herramienta y la pieza giran en diferentes planos.

> Coincide con el apunte: "la herramienta arranca la viruta según una trayectoria circular; pero el movimiento de avance (rectilíneo y constante) lo tiene la pieza". No contradice a MH6: en las dos la herramienta gira y la pieza no. Fuente: `FIN14`.

---

#### MH8 — En un proceso de rectificado cilíndrico, la herramienta abrasiva y la pieza tienen un movimiento relativo entre ambas. Esto puede darse, según las características de las máquinas de este tipo, de la siguiente forma: `[OFICIAL · ★×2]`

- ( ) Con movimiento de rotación de la herramienta y la pieza fija.
- ( ) Con movimiento de rotación y desplazamiento longitudinal de la herramienta y la pieza fija.
- **(✓) Con movimiento de rotación en forma longitudinal de la herramienta y la pieza.**
- ( ) Con movimiento de rotación y longitudinal de la pieza y la herramienta fija.

> En la rectificadora cilíndrica **giran las dos** (la muela por su cabezal, la pieza por el cabezal portapiezas) y la mesa agrega el movimiento longitudinal. Las tres opciones falsas dejan algo "fijo". Fuentes: `CV21` (clave), `F23`.

---

#### MH9 — En un proceso de rectificado cilíndrico los movimientos son los siguientes: `[ALUMNOS · ★×2]`

- ( ) a. Rotación de la herramienta con la pieza fija.
- ( ) b. Rotación de la pieza con la herramienta fija.
- **(✓) c. Rotación de la pieza y la herramienta combinado con un movimiento longitudinal.**
- ( ) d. Movimiento longitudinal de la pieza y la herramienta, sin movimiento de rotación.

> Redacción del final de la misma pregunta MH8. Fuentes: `FIN14`, `F23`.

---

#### MH10 — En el brochado interior, los filos (de la herramienta) de arranque de la viruta se disponen de la siguiente forma: `[OFICIAL · ★×2]`

- **(✓) Con las dimensiones crecientes en el sentido de avance.**
- ( ) Con las dimensiones alternadas entre crecientes y decrecientes.
- ( ) Con las dimensiones constantes en el sentido de avance.
- ( ) Con las dimensiones decrecientes en el sentido de avance.

> Apunte: "Los dientes son cada vez un poco más altos"; "el movimiento de avance queda cumplido por la herramienta en función de los filos, cada vez más grandes de la brocha". Cada diente saca un poco más que el anterior. Fuentes: `CV21` (clave), `F23`.

---

#### MH11 — En un proceso de brochado se obtienen piezas: `[ALUMNOS · ★×2]`

- ( ) a. En forma lenta y de baja calidad superficial.
- ( ) b. En forma rápida y de baja calidad superficial.
- **(✓) c. En forma rápida y de alta calidad superficial.**

> Apunte: "Mediante el brochado se consiguen, con poco tiempo de mecanizado, piezas de dimensiones exactas y de elevada calidad superficial". Fuentes: `FIN14`, `F23`.

---

#### MH12 — En el cepillado, el movimiento relativo entre la pieza se produce: `[OFICIAL · ★×2]`

- ( ) Por el movimiento longitudinal simultáneo de la mesa porta pieza y el bastidor porta herramienta.
- ( ) Por el movimiento longitudinal del bastidor porta herramienta, mientras que la mesa porta pieza permanece fija.
- ( ) Por el movimiento longitudinal de la mesa porta pieza y el movimiento rotacional del bastidor porta herramienta.
- **(✓) Por el movimiento de la mesa en forma longitudinal y el movimiento transversal de la herramienta sobre un bastidor o columna fija.**

> En la cepilladora el corte lo hace **la pieza**: la mesa va y viene (longitudinal) y el carro portaherramienta se corre de costado sobre el travesaño (transversal, intermitente). El bastidor no se mueve ni gira. Fuentes: `CV21` (clave), `F23`.

---

#### MH13 — En una cepilladora el movimiento de la pieza respecto de la herramienta es: `[ALUMNOS · ★×2]`

- **(✓) a. En un plano perpendicular a la herramienta en forma longitudinal y transversal.**
- ( ) b. En un plano paralelo a la herramienta.
- ( ) c. No hay movimiento relativo entre la pieza y la herramienta.

> Redacción del final de MH12: mismos dos movimientos (longitudinal y transversal). La c es absurda: sin movimiento relativo no hay corte. Fuentes: `FIN14`, `F23`.

---

#### MH14 — En una máquina limadora, el arranque de viruta se produce por medio de una carrera horizontal de la herramienta: `[OFICIAL · ★×2]`

- **(✓) Solo en el avance del torpedo.**
- ( ) Solo en el retroceso del torpedo.
- ( ) En el avance y retroceso del torpedo.

> Apunte: "La viruta es arrancada durante la carrera de trabajo. Por medio de la carrera en vacío (retroceso) la herramienta vuelve hacia atrás sin arranque de viruta". Es la única pregunta del parcial 2021 donde la opción con "solo" es la verdadera. Fuentes: `CV21` (clave), `F23`.

---

#### MH15 — En una limadora el movimiento del torpedo, que imprime el movimiento al porta herramienta, es producido por: `[OFICIAL · ★×2]`

- ( ) Un engranaje (volante) sin biela.
- ( ) Un engranaje (volante) con una cremallera.
- ( ) Un engranaje (volante) con una biela fija en su centro.
- **(✓) Un engranaje (volante) con una biela excéntrica.**

> El giro del volante se convierte en vaivén del torpedo con una biela tomada fuera del centro (excéntrica). El apunte lo llama "biela oscilante de corredera". Con la biela "fija en su centro" no habría carrera. Fuentes: `CV21` (clave), `F23`.

---

#### MH16 — En una limadora el movimiento de la herramienta se lo da el torpedo; este tiene un movimiento: `[★×2 · ⚠ RESPUESTA EN DUDA]`

- **(✓ recomendada) a. Longitudinal en sentido de avance y retroceso.**
- ( ) b. Longitudinal y en un solo sentido. ← la que marcó el alumno en `FIN14`
- ( ) c. Circular.

> **Conflicto.** El final resuelto `FIN14` tiene marcada la b. Pero el apunte de cátedra describe el movimiento del torpedo como "movimiento de ida y vuelta del carro de la limadora", con "carrera de trabajo" y "carrera de vacío (retroceso)", y la clave oficial de MH14 presupone que el retroceso existe. Lo que ocurre en un solo sentido es el **corte**, no el movimiento del torpedo. Recomendación: **a**. Es la pregunta 5 del formulario `F23`: al enviarlo se ve la clave y se puede salir de la duda. Fuentes: `FIN14`, `F23`.

---

#### MH17 — En una limadora, la herramienta está montada sobre: `[DEDUCIDA]`

- **(✓) a. Carro.**
- ( ) b. Husillo.
- ( ) c. Caja de engranaje Norton.

> Apunte: "El carro de la limadora va dispuesto en una guía y produce el movimiento principal; en su cabezal lleva el carro portaherramienta". El husillo es del torno y de la fresadora (lo que gira); la caja Norton es la caja de avances del torno. Fuente: `F23` (sin clave).

---

#### MH18 — En una máquina amortajadora, el movimiento relativo de la herramienta respecto de la pieza se realiza: `[OFICIAL · ★×2]`

- ( ) En forma circular en un plano perpendicular al plano de la mesa porta pieza.
- **(✓) En forma vertical alternativamente.**
- ( ) En forma horizontal.
- ( ) En forma vertical y horizontal simultáneamente.

> Apunte: "Este caso es igual al de la limadora, pero la herramienta realiza un movimiento de corte vertical". Horizontal alternativo = limadora; vertical alternativo = amortajadora. Fuentes: `CV21` (clave), `F23`.

---

#### MH19 — El proceso de amortajado, la herramienta: `[ALUMNOS · ★×2]`

- **(✓) a. Tiene un movimiento vertical alternativo.**
- ( ) b. Tiene un movimiento rotatorio.
- ( ) c. Tiene un movimiento horizontal paralelo a la mesa donde se fija la pieza.

> Redacción del final de MH18. La c describe la limadora. Fuentes: `FIN14`, `F23`.

---

### Bloque SV — Procesos sin arranque de viruta (moldeo, deformación, pulvimetalurgia)

---

#### SV1 — En un proceso de moldeo para obtener piezas por fundición de un metal, se utiliza tierra en determinadas condiciones de humedad. ¿Cuál es el factor que debe considerarse para evitar imperfecciones internas en la pieza durante la colada? `[OFICIAL · ★×2]`

- ( ) Un llenado del molde con tierra, sin compactación y con agujereado para salida de gases.
- ( ) Un llenado del molde con tierra, con una compactación media y sin agujereado para salida de gases.
- ( ) Un llenado del molde con tierra, con compactación extrema.
- **(✓) Un llenado del molde con tierra, con una compactación media y con agujereado para salida de gases.**
- ( ) Un llenado del molde con tierra, sin compactación.

> Dos condiciones a la vez: la tierra tiene que copiar el modelo (compactación) sin perder la permeabilidad "que posibilita evacuar los gases del molde". Los gases atrapados dejan poros dentro de la pieza. Fuentes: `CV21` (clave), `F23`.

---

#### SV2 — En una pieza obtenida por fundición, esta es producto de un proceso de armado de un molde. Diga cuál de las características o resultados siguientes NO se corresponde con la pieza terminada: `[ALUMNOS · ★×2]`

- ( ) a. Fragilidad.
- **(✓) b. No se necesita ninguna acción posterior.**
- ( ) c. El molde de tierra arcillosa no puede volver a utilizarse.

> La pregunta pide la **falsa**. La pieza fundida es frágil (a, verdadera) y el molde de arena es "molde perdido": se rompe para sacar la pieza (c, verdadera). Lo que no es cierto es que salga lista: después vienen el desbarbado, la limpieza y, muchas veces, mecanizado o tratamiento térmico. En el final las opciones se combinaban además en "I) a y b · II) a y c · III) b y c"; el alumno marcó la b sola. Fuentes: `FIN14`, `F23`.

---

#### SV3 — En el laminado de un metal, la deformación se produce por la acción de dos rodillos con una determinada separación. La deformación producida en la barra es: `[OFICIAL · ★×2]`

- ( ) Solo en la altura de la misma.
- **(✓) En altura, longitudinal y transversalmente.**
- ( ) En altura y transversalmente.
- ( ) En altura y longitudinalmente.

> Apunte, textual: "se producen tres tipos de deformaciones: por aplastamiento o de la altura de la barra; transversal o ensanchamiento; longitudinal o alargamiento". Fuentes: `CV21` (clave), `F23`.

---

#### SV4 — El sinterizado es el proceso mediante el cual se obtienen piezas por medio de: `[OFICIAL]`

- ( ) Partir de un polvo de metal, se lo lleva al estado cercano a la fusión dentro de un horno y luego se lo enfría rápidamente en una atmósfera controlada.
- **(✓) Partir de un polvo de metal, se lo comprime a una presión determinada dentro de un molde y luego se lo introduce en un horno.**
- ( ) La inyección de metal líquido en un molde.
- ( ) El calentado de un metal en un horno hasta temperaturas cercanas a la fusión y luego se lo moldea a través de golpes para darle la forma buscada.

> El orden es **primero comprimir, después hornear**: polvos → mezclado → compactado → sinterizado. La primera opción se saltea el compactado y agrega un enfriamiento rápido que no existe; la tercera es inyección; la cuarta, forja. Fuente: `CV21` (clave).

---

#### SV5 — El proceso de sinterizado está basado en la metalurgia de polvos; estos deben tener ciertas características, entre las cuales se encuentran capacidad de compresión, capacidad de fundirse y: `[DEDUCIDA]`

- ( ) a) Forma y tamaño de la partícula del polvo.
- ( ) b) Capacidad para fluir libremente.
- ( ) c) Capacidad de solidificar rápidamente.
- ( ) d) Capacidad de solidificar lentamente.
  - ( ) 1) "a" y "d".
  - **(✓) 2) "a" y "b".**
  - ( ) 3) "c" y "d".

> El apunte enumera lo que hay que considerar del polvo: "forma de la partícula · tamaño de la partícula · su capacidad para fluir libremente · capacidad de compresión · su capacidad de sinterizado (fundirse o unirse)". El enunciado ya nombra las dos últimas; faltan forma y tamaño (a) y fluir libremente (b). De solidificación no dice nada. Fuente: `F23` (sin clave).

---

#### SV6 — El proceso de estampa en frío se utiliza para la obtención de piezas de formas variadas. Esta produce piezas de: `[DEDUCIDA]`

- ( ) a. Baja dureza.
- **(✓) b. Alta dureza.**
- ( ) c. Dúctil.
- ( ) d. Frágil.

> Apunte, textual: "Esta deformación en frío genera en el material el fenómeno de acritud. Se obtiene una pieza con una alta dureza". Fuente: `F23` (sin clave).

---

#### SV7 — El proceso de repujado se utiliza para la obtención de piezas: `[DEDUCIDA · ⚠ CONFIANZA MEDIA]`

- ( ) a. Poco profundas y de gran espesor.
- ( ) b. Profundas y de gran espesor.
- **(✓) c. Profundas y de bajo espesor.**

> El apunte solo dice que con el "recalcado o repujado en torno" se consiguen "piezas de gran altura y volumen" (ollas, sartenes, faroles, trofeos). Gran altura = profundas; y se parte de chapa, así que el espesor es bajo. No hay fuente que confirme la opción: conviene verificarla con el formulario `F23` (pregunta 13). Fuente: `F23` (sin clave).

---

### Bloque CA — Ingeniería de control automático

> Todo sale del apunte "Ingeniería del control automático" (ciclo 2018). Vocabulario mínimo: `r` entrada de referencia · `c` variable controlada · `e` señal actuadora (o de error) · `G(p)` elementos de control · `H(p)` elementos de realimentación. Relaciones: `e = r − c` (comparador) y `c = G(p)·e`.

---

#### CA1 — En la ingeniería del control automático, si analizamos un lazo, diga cuál de las siguientes corresponde a un comparador: `[ALUMNOS · ★×2]`

- ( ) a. El comparador multiplica la señal de referencia con la señal realimentada.
- **(✓) b. El comparador resta de la señal de referencia la señal realimentada.**
- ( ) c. El comparador resta de la señal de referencia con la señal actuante.

> Apunte, textual: "El comparador resta de la señal de referencia 'r' la señal realimentada 'c' que produce la señal actuante 'e'". `e = r − c`. En la c, la señal actuante aparece como lo que se resta, cuando en realidad es el resultado. Fuentes: `COMP`, `F23`.

---

#### CA2 — En la ingeniería del control automático la función de transferencia G(p) representa: `[ALUMNOS · ★×2]`

- **(✓) a. La operación de los elementos de control.**
- ( ) b. La operación de la señal realimentada.
- ( ) c. La operación de una señal actuadora.

> Apunte, textual: "C = G(p)·e, donde G(p) representa la operación de los elementos de control". Fuentes: `COMP`, `F23`.

---

#### CA3 — Suponga que tiene un resorte con un extremo fijo a una pared y en el otro extremo una fuerza lo comprime. Si representa el sistema en un diagrama de bloques, diga cuál es el valor de la función de transferencia (siendo k la constante del resorte): `[ALUMNOS · ★×2]`

- ( ) a. G(p) = k
- ( ) b. G(p) = 2k
- **(✓) c. G(p) = 1/k**

> `Fs = k·x`. En el bloque la **entrada es la fuerza y la salida es el desplazamiento**: `x = (1/k)·Fs`. Por eso la constante queda dividiendo. Fuentes: `COMP`, `F23`.

---

#### CA4 — Se tiene una masa M que está apoyada sobre un resorte y un amortiguador viscoso (cilindro con un émbolo) y una fuerza que actúa sobre este sistema. En la representación de un diagrama de bloques la función de transferencia G(p) es: `[ALUMNOS · ★×2]`

- ( ) a. Directamente proporcional a la suma de las acciones de cada uno de los integrantes del sistema.
- **(✓) b. Inversamente proporcional a la suma de las acciones de cada uno de los integrantes del sistema.**
- ( ) c. El cuadrado de la sumatoria de las acciones de los integrantes del sistema.
- ( ) d. La raíz cuadrada de la sumatoria de las acciones del sistema.

> El apunte llega a `f = (M·p² + C·p + K)·x'`, o sea `G(p) = 1 / (M·p² + C·p + K)`: uno sobre la suma de los tres aportes (masa, amortiguador, resorte). Mismo criterio que CA3: fuerza de entrada, desplazamiento de salida. Fuentes: `COMP`, `F23`.

---

#### CA5 — Componentes mecánicos rotativos: en un resorte de torsión la cupla tiene la siguiente expresión matemática: Ts (cupla) = Ks (coeficiente de torsión) × θ (desplazamiento angular). Si se realizara la modelización en un diagrama de bloques, la función de transferencia G(p) sería: `[ALUMNOS]`

- **(✓) a. Inversamente proporcional a Ks.**
- ( ) b. Directamente proporcional a Ks.
- ( ) c. Igual al cuadrado de Ks.

> Versión rotativa de CA3: entra la cupla, sale el ángulo, `θ = (1/Ks)·Ts`. Fuente: `COMP`.

---

#### CA6 — Traslaciones lineales: en dispositivos donde se tienen dos cremalleras, una inferior y otra superior, entre ambas se ubican dos ruedas dentadas que son movidas simultáneamente por una barra recta. Este dispositivo se puede utilizar como un comparador para un sistema de control automático. Si las posiciones de referencia son Xr para la cremallera superior, Xc para la inferior y Xe para la barra recta, la expresión matemática es: `[ALUMNOS]`

- ( ) a. Xe = (Xr + Xc)/2
- **(✓) b. Xe = (Xr − Xc)/2**
- ( ) c. Xe = (Xr + Xc)·2

> Un comparador **resta**. Apunte: "la ecuación de xe es: xe = (xr − xc)/2. Debe observarse que si se invierte el sentido positivo de xc obtendríamos un dispositivo sumador" — eso es la opción a. Fuente: `COMP`.

---

#### CA7 — Dispositivos integradores: en estos dispositivos, utilizados en la ingeniería de control automático como un comparador: `[ALUMNOS · ★×2]`

- **(✓) a. La salida de este aumenta constantemente con el tiempo.**
- ( ) b. La salida de este disminuye constantemente con el tiempo.
- ( ) c. La salida de este se mantiene constante.

> Apunte, textual: "Con la utilización del integrador, la salida de éste aumenta constantemente con el tiempo, aunque la entrada sea muy pequeña, de modo tal que el sistema termina por reconocer el error". Fuentes: `COMP`, `F23`.

---

#### CA8 — Un servomecanismo es un tipo particular de sistema de control realimentado en el que… `[OFICIAL · ★×3]`

- ( ) La entrada de referencia se mantiene fija.
- ( ) La variable controlada se mantiene fija durante períodos de tiempo largos.
- ( ) Ninguna es correcta.
- **(✓) La variable controlada es la posición de un elemento mecánico.**

> Definición del apunte; ejemplo: "la posición angular de un eje (regulación de entrada de aire de un quemador)". **Par con CA9:** el distractor de cada una es la respuesta de la otra. Fuentes: `CV21` (clave), `COMP`, `F23`.

---

#### CA9 — Un regulador es un sistema de control automático realimentado en el que la entrada de referencia… `[OFICIAL · ★×3]`

- ( ) La variable controlada no se mantiene constante por períodos de tiempo relativamente largos.
- **(✓) Se mantiene fija o constante durante períodos de tiempo relativamente largos.**
- ( ) Ninguna es correcta.
- ( ) La variable controlada es la posición de un elemento mecánico.

> Definición del apunte: la referencia, "aunque sea ajustable", queda fija mucho tiempo. Ejemplo: controles de temperatura. Fuentes: `CV21` (clave), `COMP`, `F23`.

---

#### CA10 — En un sistema realimentado, la señal actuadora y la variable controlada se relacionan por: `[DEDUCIDA]`

- ( ) a. Suma.
- **(✓) b. Producto.**
- ( ) c. Suma y producto.

> Apunte: "la relación entre la señal actuadora 'e' […] y la variable controlada 'c' se expresa por la siguiente ecuación: C = G(p)·e […]. El rectángulo representa una multiplicación". La suma (el círculo) es del comparador y relaciona otras señales: referencia, realimentación y señal actuadora. Fuente: `F23` (sin clave).

---

#### CA11 — En la modelización, cuando asimilamos un sistema mecánico a un circuito eléctrico, diga cuál de las siguientes afirmaciones es correcta: `[ALUMNOS]`

- **(✓) a. Un resorte es el equivalente a una inductancia.**
- ( ) b. Un amortiguador se representa como una capacitancia.
- ( ) c. Una masa como una resistencia eléctrica.
- ( ) d. Todas son falsas.
- ( ) e. Todas son correctas.

> Analogía que da Abud en clase (según la carpeta de otro año): **resorte = inductancia · amortiguador = resistencia · masa = capacitancia**. Las opciones b y c tienen cruzados el amortiguador y la masa. Fuente: `COMP`.

---

#### CA12 — En el caso de un recipiente con un fluido, se coloca un termostato para controlar su temperatura. ¿Cómo clasificaría este dispositivo? `[ALUMNOS · ★×4]`

- ( ) a. Como un modelo físico.
- **(✓) b. Como un modelo analógico.**
- ( ) c. Como un modelo matemático.
- ( ) d. Todas son falsas.

> Pertenece al tema "Modelos", pero es de las preguntas más repetidas entre todas las fuentes, y el termostato es además el ejemplo con que arranca el apunte de control. Se entiende con CA13. Fuentes: `COMP` (dos veces), `P13`, `FIN14`.

---

#### CA13 — Un modelo analógico es aquel donde: `[ALUMNOS · ★×2]`

- ( ) a. Sus características se definen a través de un plano con cotas.
- **(✓) b. La variable controlada es de distinta naturaleza que la variable medida.**
- ( ) c. La variable controlada es de igual naturaleza que la variable medida.
- ( ) d. Todas son falsas.

> Por eso el termostato de CA12 es analógico: controla una temperatura midiendo otra cosa (una dilatación, una posición). La a describe un modelo icónico o gráfico. Fuentes: `COMP`, `P13`.

---

### Bloque EM — Elementos de máquinas

> Lo único que apareció de este tema en las fuentes son las cinco preguntas de roscas del formulario 2023, que no trae clave. Las respuestas salen del apunte de la Unidad IX y coinciden con el resumen manuscrito `R23` ("Whitworth 55° · métrica 60° · paso: distancia entre dos crestas sucesivas"). De árboles, ejes, cojinetes, chavetas y engranajes no hay ninguna pregunta real: ver [sugeridas](preguntas_sugeridas_parcial_2.md).

---

#### EM1 — En una rosca, el paso es: `[DEDUCIDA]`

- ( ) a. Altura del filete.
- **(✓) b. Distancia entre filetes.**
- ( ) c. Radio de los filetes.

> Apunte: "Paso de la rosca: distancia que hay entre dos crestas sucesivas". Fuente: `F23` (sin clave), `R23`.

---

#### EM2 — ¿Qué es el paso de la rosca o hélice? `[DEDUCIDA]`

- **(✓) a. Distancia entre filete y filete.**
- ( ) b. Profundidad del filete.
- ( ) c. Diámetro total del tornillo.
- ( ) d. Distancia entre dientes.

> La misma pregunta que EM1 con otras opciones. "Dientes" tienen los engranajes, no las roscas. Fuente: `F23` (sin clave).

---

#### EM3 — En una rosca Whitworth, los hilos representan: `[DEDUCIDA]`

- ( ) a. Cantidad de filetes por mm.
- **(✓) b. Cantidad de filetes por pulgada.**
- ( ) c. Cantidad de pasos por pulgada.
- ( ) d. Todas son falsas.

> Apunte: el paso "en el sistema métrico se expresa en mm y en el sistema inglés por el número de hilos que hay en una pulgada". Whitworth es la rosca inglesa. Fuente: `F23` (sin clave).

---

#### EM4 — En una rosca métrica el ángulo del cono de la hélice es: `[DEDUCIDA]`

- ( ) a. 55°
- **(✓) b. 60°**
- ( ) c. 65°
- ( ) d. 50°

> El perfil de la rosca métrica ISO es un triángulo de 60°. Fuente: `F23` (sin clave), `R23`.

---

#### EM5 — En una rosca Whitworth el ángulo del cono de la hélice es: `[DEDUCIDA]`

- **(✓) a. 55°**
- ( ) b. 60°
- ( ) c. 65°
- ( ) d. 50°

> Whitworth = 55°. Va de a pares con EM4: **métrica 60° / Whitworth 55°**. Fuente: `F23` (sin clave), `R23`.

---

### Bloque PI — Marcas, patentes y derecho de autor

> Tres de estas cuatro ya estaban en el banco del 1er parcial (J1, J2, J3). Se repiten acá completas porque el tema está anunciado para este parcial; la de marcas es nueva.

---

#### PI1 — La duración de una marca una vez registrada: `[ALUMNOS]`

- ( ) a. Debe renovarse cada 15 años.
- ( ) b. Debe renovarse cada 10 años, con la condición de haber sido usada en los últimos 2 años.
- ( ) c. Debe renovarse cada 5 años.
- **(✓) d. Debe renovarse cada 10 años, con la condición de haber sido utilizada en los últimos 5 años.**

> Coincide con la ley argentina de marcas (22.362): el registro dura 10 años y se renueva indefinidamente si la marca fue usada dentro de los 5 años previos al vencimiento. La b es la trampa: mismos 10 años, pero con 2 de uso. Fuente: `COMP`.

---

#### PI2 — Una patente tiene una duración de: `[ALUMNOS · ★×3]`

- ( ) a. 20 años y renovable.
- ( ) b. 10 años y renovable.
- **(✓) c. 20 años y no renovable.**
- ( ) d. 15 años y no renovable.

> 20 años desde la presentación de la solicitud, improrrogables; después la invención pasa al dominio público. Fuentes: `COMP` (dos veces), `FIN14`, y los apuntes manuscritos de finales viejos ("Patentes: 20 años improrrogables").

---

#### PI3 — El derecho de autor tiene una duración de: `[ALUMNOS · ★×3 · ⚠ NO COINCIDE CON LA LEY VIGENTE]`

- ( ) a. De por vida del autor.
- ( ) b. 50 años desde su publicación.
- **(✓ EXAMEN) c. De por vida del autor y 50 años más.**
- ( ) d. De por vida del autor y 25 años más.

> **Respuesta de Abud: vida + 50**, igual en las tres fuentes. La ley argentina vigente (11.723, con la reforma de 1997) da vida del autor + 70 años; los 50 son el mínimo del Convenio de Berna. Con estas cuatro opciones no hay conflicto: marcar la c. Si alguna vez apareciera "70 años" entre las opciones, ahí sí habría que dudar. Fuentes: `COMP` (dos veces), `FIN14`.

---

#### PI4 — Cuando se obtiene una patente por una maquinaria o un dispositivo innovador, esta puede: `[ALUMNOS · ★×3]`

- ( ) a. Solo ser utilizada por el inventor, sin posibilidad de que la use otro.
- **(✓) b. Ser vendida o utilizada por el inventor.**
- ( ) c. Ser solo utilizada por el inventor de por vida, sin que nadie pueda utilizar el invento mientras viva este.

> Los derechos de la patente son transferibles: se venden, se licencian, se heredan. Las dos falsas tienen "solo". Fuentes: `COMP` (dos veces), Examen A del 1er parcial.

---

### Bloque VA — Comodines: fuera del temario anunciado, pero presentes en parciales recientes

> Las dos primeras salieron en el 2° parcial 2021 (clave oficial) aunque no son de ninguno de los temas anunciados. Las otras cinco están en el formulario de repaso 2023 y en el modelo ≈2018–19. Son pocas y cortas: conviene saberlas.

---

#### VA1 — El proceso creativo consta de las siguientes etapas: `[OFICIAL · ★×2]`

- ( ) Necesidad, concentración, recolección de datos y verificación.
- ( ) Necesidad, recolección de datos y análisis, concentración y verificación.
- **(✓) Necesidad, recolección de datos y análisis, concentración, relajamiento y verificación.**
- ( ) Necesidad, concentración, relajamiento y verificación.

> Cinco etapas, en ese orden. Es la más larga de las cuatro y la única que tiene a la vez "recolección de datos" y "relajamiento". Fuentes: `CV21` (clave), `F23`.

---

#### VA2 — En un informe escrito las partes que lo componen son: `[OFICIAL · ★×2 · ⚠ MEMORIZAR]`

- ( ) Introducción, planos, metodología y conclusiones.
- ( ) Introducción, antecedentes, planos y conclusiones.
- **(✓) Introducción, antecedentes, metodología y planos.**
- ( ) Introducción, cálculos, planos y conclusiones.

> Contra la intuición, **la correcta es la única que no tiene "conclusiones"**. Es la clave del campus. Fuentes: `CV21` (clave), `F23`.

---

#### VA3 — Las partes del plan en una elaboración eficiente de informes son: definición del problema, confección del bosquejo y… `[ALUMNOS · ★×4]`

- ( ) a. Elaboración de conclusiones.
- **(✓) b. Elaboración de agenda.**
- ( ) c. Desarrollo del tema.

> Misma pregunta que K1 del 1er parcial (ahí decía "elaboración de una tesis"). Fuentes: `COMP` (dos veces), `F23`, Examen A del 1er parcial, apuntes manuscritos de finales viejos.

---

#### VA4 — El proyecto de fabricación de una máquina debe ser realizado: `[ALUMNOS · ★×2]`

- ( ) a. En forma totalmente independiente de los proyectos técnico-funcional y económico-financiero.
- ( ) b. En una etapa previa al proyecto técnico-funcional.
- **(✓) c. Conjuntamente con el proyecto técnico-funcional y el proyecto económico-financiero.**
- ( ) d. Todas son falsas.

> Los tres proyectos (técnico-funcional, de fabricación y económico-financiero) se hacen juntos y se condicionan entre sí. Misma idea que G3 del 1er parcial. Fuentes: `COMP`, `F23`.

---

#### VA5 — En el proyecto de una máquina, el proyecto técnico-funcional: `[ALUMNOS · ★×4]`

- ( ) a. No depende del proyecto de fabricación.
- ( ) b. Solo depende del proyecto de fabricación.
- **(✓) c. Depende del proyecto de fabricación y el proyecto económico-financiero.**
- ( ) d. Depende del proyecto de fabricación y el proyecto analítico.
- ( ) e. Todas son falsas.

> La otra cara de VA4. El "proyecto analítico" de la d no existe en la clasificación de Abud. Fuentes: `COMP` (dos veces), `P13`, `F23`.

---

#### VA6 — Las empresas que realizan una planeación tecnológica a profundidad: `[ALUMNOS · ★×4]`

- **(✓) a. Alcanzan posiciones de costos competitivas.**
- ( ) b. Sus planes tecnológicos buscan corregir solo problemas operativos.
- ( ) c. Poseen consejos de administración que privilegian la minimización del riesgo y buscan un rendimiento a corto plazo.

> Igual que I3 del 1er parcial. Fuentes: `COMP` (dos veces), `F23`, Examen A del 1er parcial.

---

#### VA7 — Una de las tareas del gerente de tecnología es: `[ALUMNOS · ★×4]`

- ( ) a. Análisis técnico de los productos fabricados.
- ( ) b. Organizar políticas de mantenimiento.
- **(✓) c. Análisis de la obsolescencia de las tecnologías actuales.**
- ( ) d. Análisis de los desarrollos del departamento de investigación.

> Igual que I4/I5 del 1er parcial; existe la variante "análisis de la obsolescencia del departamento", también correcta. La palabra clave es **obsolescencia**. Fuentes: `COMP` (tres veces), `F23`, Examen A del 1er parcial.

---

### Bloque VJ — 2° parciales viejos (2013 y ≈2018–19): temas fuera del temario anunciado

> **Prioridad baja para este parcial, útil para el final** (que mezcla preguntas de los dos parciales). Las respuestas son las resaltadas por alumnos en `COMP`; las fotos `P13` aportan las opciones completas. Donde la fuente solo trae la respuesta, se indica.

**Toma de decisiones y resolución de problemas**

---

#### VJ1 — En un proceso de toma de decisiones: `[ALUMNOS · ★×2]`

- ( ) a. Los factores técnicos no forman parte del proceso.
- **(✓) b. Los factores de recursos forman parte del proceso.**
- ( ) c. Los factores humanos se consideran fuera del proceso de toma de decisiones.
- ( ) d. Todas las afirmaciones son falsas.
- ( ) e. Todas las afirmaciones son verdaderas.

> Técnicos, humanos y de recursos: los tres forman parte. La a y la c niegan uno. Fuentes: `P13`, `COMP`.

---

#### VJ2 — Dentro de los defectos que suelen ocurrir en la priorización de problemas en el proceso de toma de decisiones, podemos encontrar: `[ALUMNOS · ★×3]`

- ( ) a. Tendencia a atender sólo lo urgente relegando lo importante.
- ( ) b. Aprovechamiento de oportunidades a expensas de una excesiva preocupación por superar problemas negativos.
- **(✓) c. Las dos son verdaderas.**
- ( ) d. Las dos son falsas.

> Fuentes: `P13`, `COMP` (dos veces).

---

#### VJ3 — En un proceso de resolución de problemas, si la meta está clara pero el estado inicial no, debe aplicarse el procedimiento: `[★×2 · ⚠ RESPUESTA EN DUDA]`

- ( ) a. Subir la cuesta (hill climbing).
- **(✓ según `COMP`) b. Análisis medios-fin.**
- ( ) c. Trabajar en sentido inverso.

> `COMP` resalta la b. En la teoría general de heurísticos, el caso "meta clara, estado inicial no" es el de **trabajar en sentido inverso** (c), y medios-fin se usa cuando ambos estados están claros. Sin apunte de cátedra que lo defina, queda en duda: es candidata a dejar en blanco. Fuentes: `P13`, `COMP`.

---

#### VJ4 — En un proceso de resolución de problemas donde cada nuevo estado provocará un estímulo en función del cual se deberá analizar el estado siguiente, se debe aplicar el procedimiento: `[ALUMNOS]`

- **(✓) b. Subir la cuesta.**

> La fuente solo trae la respuesta; las opciones serían las mismas tres de VJ3. Fuente: `COMP`.

---

#### VJ5 — En el análisis de un problema, las variables de entrada y de salida: `[ALUMNOS · ★×3]`

- **(✓) a. Son parámetros que pueden fluctuar entre ciertos valores.**
- ( ) b. Son restricciones ficticias.
- ( ) c. Las dos son verdaderas.
- ( ) d. Las dos son falsas.

> Fuentes: `P13`, `COMP`, apuntes manuscritos de finales viejos ("son aquellos parámetros que pueden fluctuar entre ciertos valores en la solución del problema: el tamaño, colores, etc.").

---

#### VJ6 — En el análisis de un problema las restricciones ficticias: `[ALUMNOS]`

- **(✓) b. Nos pueden limitar alguna posibilidad de solución.**

> Solo respuesta en la fuente. Fuente: `COMP`.

---

#### VJ7 — En el análisis de un problema las restricciones son características que debemos considerar para la resolución correcta y aceptable del problema. ¿Cuál de las siguientes corresponde a una? `[ALUMNOS]`

- **(✓) b. Leyes de impacto ambiental.**

> Solo respuesta en la fuente. Fuente: `COMP`.

---

#### VJ8 — En el análisis de un problema donde debemos diseñar y calcular una cámara frigorífica, diga cuáles de las siguientes combinaciones responden a las variables de entrada que deben conocerse: `[ALUMNOS]`

- **(✓) d. Cantidad de producto, consumo de energía de la maquinaria que produce frío, temperatura final que debe alcanzar dentro de la cámara.**

> Solo respuesta en la fuente. Fuente: `COMP`.

---

#### VJ9 — En la resolución de problemas, dentro de los métodos heurísticos, el conocimiento procedimental es: `[ALUMNOS]`

- **(✓) c. El conocimiento de acciones para resolver un problema particular.**

> Solo respuesta en la fuente. Fuente: `COMP`.

---

#### VJ10 — Dentro de las actitudes que debe tener el ingeniero para ser creativo, encontramos: `[★×4 · ⚠ FUENTES EN CONFLICTO]`

- **(✓ recomendada) a. Buscar formas de ver el problema, evitando suposiciones preconcebidas.**
- ( ) b. Reconocer que no existen soluciones no ingenieriles.
- ( ) c. Las dos son verdaderas.
- ( ) d. Las dos son falsas.

> `COMP` la trae dos veces con respuestas distintas (a en el parcial numerado, c en la lista) y `FIN14` la dejó sin marcar. Los apuntes manuscritos de finales viejos dan como actitudes verdaderas "evitar hacer suposiciones" y "**existen** soluciones no ingenieriles": entonces la b, que dice que **no** existen, es falsa, y la respuesta es **a**. Fuentes: `P13`, `COMP` (dos veces), `FIN14`.

---

**Modelos y optimización**

---

#### VJ11 — Un modelo icónico puede ser utilizado en el siguiente caso: `[ALUMNOS]`

- **(✓) b. Para representar una imagen de la solución del problema.**

> Solo respuesta en la fuente. Va de a pares con VJ12: imagen de la solución → icónico. Fuente: `COMP`.

---

#### VJ12 — Un modelo analógico puede ser utilizado en el siguiente caso: `[ALUMNOS · ★×2]`

- ( ) a. Para darnos una imagen física de la solución de un problema.
- **(✓) b. Para representar la velocidad de corriente de un sistema hidrodinámico.**
- ( ) c. Las dos verdaderas.
- ( ) d. Las dos son falsas.

> La a es el modelo icónico de VJ11. Fuentes: `P13`, `COMP`.

---

#### VJ13 — En una optimización tenemos: `[ALUMNOS · ★×2]`

- ( ) a. Una variable dependiente denominada criterio en la que influye la variable manipulada.
- ( ) b. Un valor para el cual la variable dependiente es máxima y que recibe el nombre de valor óptimo.
- **(✓) c. Las dos verdaderas.**
- ( ) d. Las dos son falsas.

> Criterio = variable dependiente; variable manipulada = independiente; valor óptimo = el que hace máximo el criterio. Fuentes: `P13`, `COMP`.

---

#### VJ14 — En ingeniería se utiliza el método iterativo para el diseño y consta de: `[ALUMNOS · ★×2]`

- ( ) a. Sólo una búsqueda global donde el ingeniero supone que se encuentra el valor óptimo.
- ( ) b. Sólo una búsqueda local donde el ingeniero supone que se encuentra el valor óptimo.
- **(✓) c. Una búsqueda global y una búsqueda local.**
- ( ) d. Todas son falsas.

> Fuentes: `P13`, `COMP`.

---

#### VJ15 — En el caso de un motor de combustión interna, la optimización (variable dependiente) del rendimiento es función de (variable independiente o variable manipulada): `[ALUMNOS · ★×3]`

- ( ) a. Velocidad.
- **(✓) b. Régimen de inyección de combustible.**
- ( ) c. Las dos son falsas.

> Rendimiento del motor = variable dependiente; inyección de combustible = variable independiente. Fuentes: `P13`, `COMP`, apuntes manuscritos de finales viejos.

---

#### VJ16 — Si estamos haciendo un cálculo para la climatización de una sala de teatro, ¿cuál sería el criterio (variable dependiente)? `[ALUMNOS · ★×2]`

- ( ) a. La temperatura.
- ( ) b. La presión.
- **(✓) c. El confort de las personas.**
- ( ) d. Todas son falsas.

> La temperatura es lo que se manipula; lo que se quiere maximizar es el confort. Fuentes: `P13`, `COMP`.

---

**Máquinas en base racional y en base empírica · proyecto de máquina**

---

#### VJ17 — De las siguientes afirmaciones: I) Una máquina en base empírica es aquella en que sus dimensiones están basadas en características elástico-resistenciales. II) Una máquina termocinética (por ejemplo, un intercambiador de calor) tiene sus dimensiones basadas en el empirismo. `[ALUMNOS · ★×2]`

- ( ) a. I es verdadera y II es falsa.
- **(✓) b. I y II son verdaderas.**
- ( ) c. I es falsa y II es verdadera.
- ( ) d. I y II son falsas.

> Fuentes: `P13`, `COMP` (ahí con la redacción "a y b son correctas").

---

#### VJ18 — De las siguientes afirmaciones: a) Una máquina en base racional es aquella en la cual sus dimensiones están basadas en características fluidodinámicas. b) Una bomba centrífuga es una máquina en base racional. `[ALUMNOS]`

- **(✓) c. a y b son correctas.**
- ( ) d. a y b son falsas.

> Regla para VJ17–VJ20: **racional = fluidodinámica** (bombas, turbomáquinas) · **empírica = elástico-resistencial y termocinética** (reductores, intercambiadores de calor). Fuente: `COMP`.

---

#### VJ19 — Las máquinas en base racional, reales, son: `[ALUMNOS · ★×2]`

- ( ) a. Iguales en peso a las ideales.
- ( ) b. Mayores en peso y menores en tamaño que las ideales.
- **(✓) c. Mayores en peso y en tamaño que las ideales.**
- ( ) d. Todas son falsas.

> `COMP` trae también la variante "Las máquinas en base empírica reales son:", con la misma respuesta. La máquina real siempre es más pesada y más grande que la ideal. Fuentes: `P13`, `COMP` (dos veces).

---

#### VJ20 — Un intercambiador de calor está diseñado en función de la siguiente expresión: Q = K·S·τm, donde S es la superficie de intercambio de calor, Q la cantidad de calor, K el coeficiente de transmisión total de calor obtenido experimentalmente y τm el salto medio de temperaturas. Según lo expuesto, este tipo de máquinas es: `[ALUMNOS · ★×3]`

- ( ) a. Una máquina en base racional.
- **(✓) b. Una máquina en base empírica.**
- ( ) c. Una máquina alternativa.
- ( ) d. a, b y c son falsas.

> La pista está en el enunciado: `K` se obtiene **experimentalmente** → empírica. `COMP` trae la variante con "un evaporador" en lugar de intercambiador; misma respuesta. Fuentes: `P13`, `COMP` (dos veces).

---

#### VJ21 — El proyecto de una máquina requiere de la conjunción de los siguientes proyectos: `[ALUMNOS · ★×2]`

- ( ) a. Proyecto de fabricación, proyecto ponderal y proyecto económico-financiero.
- ( ) b. Proyecto técnico-funcional, proyecto económico-financiero y proyecto estético.
- **(✓) c. Proyecto económico-financiero, proyecto técnico-funcional y proyecto de fabricación.**
- ( ) d. Todas son falsas.

> Los mismos tres proyectos de VA4 y VA5. "Ponderal" y "estético" son inventados. Fuentes: `P13`, `COMP`.

---

**Unidades elementales de transformación (UET)**

> Regla para todo el grupo: **vinculación física = rígida**, prefijada, línea de producción, bajo costo por pieza. **Vinculación lógica = flexible**, limitada solo por la imaginación del procesista.

---

#### VJ22 — En una vinculación física de unidades elementales de transformación: `[ALUMNOS · ★×2]`

- ( ) a. Es posible modificar la vinculación para obtener diferentes procesos.
- **(✓) b. Las vinculaciones están prefijadas por mecanismos especiales que responden a un diseño y no es posible modificar absolutamente nada.**
- ( ) c. El orden de las vinculaciones no altera el proceso, es indistinto un orden u otro.
- ( ) d. a, b y c son falsas.

> Fuentes: `P13`, `COMP`.

---

#### VJ23 — En una vinculación lógica de unidades elementales de transformación: `[ALUMNOS]`

- **(✓) a. Los métodos de vinculación sólo están limitados por la imaginación creativa del procesista.**
- ( ) b. Las UET están unidas rígidamente entre sí.
- ( ) c. a y b son falsas.

> La b describe la vinculación física. Fuente: `COMP`.

---

#### VJ24 — En una disposición serie de UET: `[ALUMNOS]`

- ( ) a. La continuidad del flujo se encuentra asegurada si la capacidad de las UET son distintas.
- **(✓) b. La continuidad del flujo se encuentra asegurada si la capacidad de las UET son iguales.**
- ( ) c. La continuidad del flujo se encuentra asegurada si la capacidad de las UET se van sumando progresivamente.

> En serie, la más lenta frena a todas: tienen que tener la misma capacidad. Par con VJ25. Fuente: `COMP`.

---

#### VJ25 — En una disposición paralela de UET: `[ALUMNOS · ★×2]`

- **(✓) a. Las UET pueden tener o no la misma capacidad de producción.**
- ( ) b. Las UET deben tener la misma capacidad de producción.
- ( ) c. Las UET no deben tener la misma capacidad de producción.

> En paralelo cada una produce por su cuenta: da igual. Serie → iguales (VJ24); paralelo → indistinto. Fuentes: `P13`, `COMP`.

---

#### VJ26 — Una línea de producción es: `[ALUMNOS]`

- ( ) a. Una vinculación lógica UET.
- **(✓) b. Una vinculación física UET.**
- ( ) c. Una combinación de vinculaciones lógicas y físicas.

> Par con VJ27: línea de **producción** → física; línea de **montaje** → combinación. Fuente: `COMP`.

---

#### VJ27 — Una línea de montaje es posible ser conformada por: `[ALUMNOS · ★×2]`

- **(✓) a. Una combinación de vinculación física y lógica.**
- ( ) b. No existe posibilidad de una combinación mixta.
- ( ) c. a y b son falsas.

> Fuentes: `P13`, `COMP`.

---

#### VJ28 — Una de las ventajas de la vinculación física de las UET es: `[ALUMNOS · ★×2]`

- ( ) a. Posibilidad de fabricar distintos productos.
- ( ) b. Utilización de maquinarias de propósitos específicos.
- **(✓) c. Bajo costo por pieza producida.**

> La a sería una ventaja de la vinculación lógica. Fuentes: `P13`, `COMP`.

---

#### VJ29 — En el proyecto de una planta industrial, ¿en base a qué análisis se define el tipo de vinculación de las UET? `[ALUMNOS · ★×2]`

- ( ) a. Producto a fabricar.
- ( ) b. La superficie disponible.
- **(✓) c. Estudio de mercado del producto a fabricar.**
- ( ) d. Análisis de costos del producto a fabricar.
- ( ) e. Análisis de la cantidad de personal involucrado.
- ( ) f. Todas son falsas.

> Fuentes: `P13`, `COMP`.

---

**Seis sombreros para pensar · tesis**

> Blanco = datos · rojo = sentimientos · negro = riesgos y juicio negativo · amarillo = optimismo y beneficios · verde = ideas nuevas · azul = control del proceso.

---

#### VJ30 — En el caso de estar tratando la funcionalidad de una turbina para un avión, la afirmación "qué pasaría si un pájaro entrara en la turbina y afectara su funcionamiento" es de pensamiento de: `[ALUMNOS · ★×2]`

- **(✓) Sombrero negro.**
- ( ) Blanco · verde · amarillo · rojo · azul.

> Señala un riesgo. Fuentes: `P13`, `COMP`.

---

#### VJ31 — En el caso de estar tratándose de una gran cantidad de agua que se encuentra en una montaña, alguien propone aprovecharla llevándola a una ciudad que se ubica en la base, a través de una tubería. Sería un pensamiento de: `[ALUMNOS · ★×2]`

- **(✓) Sombrero amarillo.**
- ( ) Verde · negro · azul · blanco · rojo.

> Ve el beneficio, el aprovechamiento. Fuentes: `P13`, `COMP`.

---

#### VJ32 — En el caso de estar tratándose un tema para una toma de decisiones, una afirmación del tipo "siento que este producto va a fracasar" es de sombrero: `[ALUMNOS · ★×2]`

- **(✓) Rojo.**
- ( ) Amarillo · verde · azul · blanco · negro.

> "Siento que…": es una emoción, no un análisis de riesgo. Por eso es rojo y no negro. Fuentes: `P13`, `COMP`.

---

#### VJ33 — En una redacción eficiente de informes, para la elaboración de una tesis, la elección del tema debe: `[⚠ RESPUESTA EN DUDA]`

- ( ) a. Ser realizado en función de los requerimientos de la tesis, sin tener en cuenta el interés en el mismo.
- ( ) b. Estar en función del tiempo disponible para trabajar en el mismo.
- ( ) c. No estar en función del tiempo disponible para su realización.
  - ( ) I. a y b son verdaderas y c es falsa.
  - ( ) II. a y c son verdaderas y b es falsa.
  - ( ) III. a, b y c son verdaderas.
  - ( ) IV. a y c son falsas y b verdadera.
  - **(✓ según `FIN14`) V. Todas son falsas.**

> El alumno marcó V. Por lógica la b parece verdadera (el tema tiene que ser abordable en el tiempo disponible), lo que llevaría a IV. Sin otra fuente: candidata a dejar en blanco. Fuente: `FIN14`.

---

## 3. Resumen de contenidos por bloque

### Bloque RO — Mecánica rotacional

| Concepto | Fórmula del apunte | Resuelve |
|---|---|---|
| Momento de inercia | `I = Σ m·r²` — depende del eje y de cómo está distribuida la masa; **no** de `ω` | RO3 |
| Ejes paralelos | `I = I_CM + M·h²` | RO12 |
| Energía cinética de rotación | `K = ½·I·ω²` | RO1 |
| Cantidad de movimiento angular | `L = I·ω` (partícula: `L = r × p`) | RO8, RO10 |
| Ley fundamental | `T_ext = dL/dt` | RO9 |
| Conservación (`T_ext = 0`) | `L = cte` → `I₁·ω₁ = I₂·ω₂` | RO4, RO9 |
| Trabajo de rotación | `dW = T·dθ` → `W = T·(θ₂ − θ₁)` | RO7 |
| Potencia | `P = T·ω = I·ω·α` (análoga a `P = F·v`) | RO2, RO5, RO6 |
| Rodadura | `K = ½·I_CM·ω² + ½·M·v_CM² = ½·I_P·ω²` (`P` = punto de contacto) | RO11, RO12 |
| Precesión | `T = ωp × L` · `ωp = T / (L·sen θ) = r·m·g / L` | RO13, RO14 |

En la rodadura, el punto de contacto tiene velocidad 0, el centro `v_CM` y el punto superior `2·v_CM`.

### Bloques MH y SV — Máquinas-herramienta y procesos

**Con arranque de viruta — quién se mueve:**

| Máquina | Movimiento de corte | Avance | Frase de examen |
|---|---|---|---|
| **Torno** | La **pieza** gira | Herramienta: longitudinal y transversal | "La pieza gira y la herramienta se mueve en sentido longitudinal y transversal" |
| **Fresadora** | La **fresa** gira | Pieza: plano horizontal, longitudinal y transversal | Cilíndrico: eje paralelo a la superficie → "a) y b)". Frontal: eje perpendicular al plano de avance |
| **Alesadora** | La **herramienta** gira | Pieza (no gira): se desplaza en un plano horizontal | "La pieza fija y la herramienta girando" |
| **Rectificadora cilíndrica** | **Muela y pieza** giran | Longitudinal | "Rotación de la pieza y la herramienta combinado con un movimiento longitudinal" |
| **Brochadora** | La **brocha**, rectilíneo | Lo dan los filos, de dimensiones crecientes | "En forma rápida y de alta calidad superficial" |
| **Cepilladora** | La **pieza** (mesa), longitudinal de ida y vuelta | Herramienta: transversal, sobre bastidor o columna fija | "Movimiento de la mesa en forma longitudinal y movimiento transversal de la herramienta" |
| **Limadora** | La **herramienta** (torpedo), horizontal de ida y vuelta | Pieza | Viruta "solo en el avance del torpedo" · volante con biela excéntrica · herramienta sobre el carro |
| **Amortajadora** | La **herramienta**, vertical de ida y vuelta | Pieza | "En forma vertical alternativamente" |

Cepillado, limado y amortajado: herramienta de un solo filo que corta solo en la carrera de trabajo. Se diferencian en **quién** hace el corte (pieza / herramienta / herramienta) y **en qué dirección** (horizontal / horizontal / vertical).

**Sin arranque de viruta — el dato que preguntan:**

| Proceso | Qué es | Dato de examen |
|---|---|---|
| Fundición en arena | Molde perdido de tierra con arcilla | Compactación media + agujereado para gases · la pieza necesita acciones posteriores |
| Laminado | Deformación plástica entre dos cilindros | Tres deformaciones: altura, transversal y longitudinal |
| Estampado en frío | Deformación entre dos estampas, a presión | Acritud → alta dureza |
| Repujado | Conformado de chapa sobre torno | Piezas profundas y de bajo espesor |
| Sinterizado | Polvo → comprimir en molde → horno | Polvo: forma y tamaño de partícula, fluir libremente, compresión, capacidad de sinterizado |

### Bloque CA — Control automático

```
        comparador             elementos de acción directa
 r ──(+)──►( Σ )───── e ─────►[  G(p)  ]───────┬─────► c
            ▲ (−)                               │
            │ b      elementos de realimentación│
            └──────────────[  H(p)  ]◄──────────┘

 e = r − b       c = G(p)·e       b = H(p)·c
 Con realimentación unitaria b = c, y queda e = r − c.
 El círculo es una adición; el rectángulo, una multiplicación.
```

| Término | Definición del apunte |
|---|---|
| Entrada de referencia `r` | El valor deseado (en el termostato, la posición del dial) |
| Variable controlada `c` | El valor verdadero (la temperatura real) |
| Señal actuadora `e` | La señal de error que acciona los elementos de control |
| Lazo cerrado | La variable controlada se realimenta y se compara con la referencia |
| Lazo abierto | No hay comparador; cada ajuste fija una posición de los elementos de control |
| Servomecanismo | La variable controlada es la **posición** de un elemento mecánico |
| Regulador | La entrada de referencia se mantiene **fija** durante períodos largos |
| Integrador | Su salida aumenta constantemente con el tiempo, aunque la entrada sea muy pequeña |

| Componente | Ecuación (`p = d/dt`) | Función de transferencia |
|---|---|---|
| Resorte | `Fs = k·x` | `1/k` |
| Amortiguador viscoso | `Fd = c·p·x` | `1/(c·p)` |
| Masa + resorte + amortiguador | `f = (M·p² + C·p + K)·x'` | `1/(M·p² + C·p + K)` |
| Resorte de torsión | `Ts = Ks·θ` | `1/Ks` |
| Disco en medio viscoso sobre eje de torsión | `T = (Ks + Cv·p + I·p²)·θ` | `1/(Ks + Cv·p + I·p²)` |
| Comparador de cremalleras | `xe = (xr − xc)/2` | — |
| Comparador diferencial de engranajes | `θe = (θr − θc)/2` | — |

En todos los bloques entra la fuerza (o la cupla) y sale el desplazamiento (o el ángulo): por eso la constante del componente siempre queda **dividiendo**.

Analogía mecánico-eléctrica de Abud: resorte = inductancia · amortiguador = resistencia · masa = capacitancia.

### Bloques EM y PI

| Rosca | Ángulo | Cómo se expresa el paso |
|---|---|---|
| Métrica | 60° | En milímetros |
| Whitworth (inglesa) | 55° | En hilos (filetes) por pulgada |

Paso = distancia entre dos crestas (filetes) sucesivas.

| Derecho | Duración (respuesta de examen) | Renovable |
|---|---|---|
| Patente | 20 años | No |
| Marca | 10 años | Sí, si se usó en los últimos 5 años |
| Derecho de autor | Vida del autor + 50 años | — |

---

## 4. Hoja de repaso rápido

| Código | Respuesta | Clave para recordarla | Confianza |
|---|---|---|---|
| **Bloque RO** | | | |
| RO1 | Varía con el cuadrado de la velocidad angular | `K = ½·I·ω²` | Oficial ★×3 |
| RO2 | Disminuye | `P = T·ω` constante | Oficial ★×3 |
| RO3 | El momento de inercia se mantiene constante | `I` no depende de `ω` | Alumnos ★×2 |
| RO4 | Disminuye | `I₁·ω₁ = I₂·ω₂` | Oficial ★×2 |
| RO5 | Función de momento de inercia, velocidad y aceleración angular | `P = I·ω·α` | Oficial ★×3 |
| RO6 | Dependiente de la variación de su velocidad angular | `α = dω/dt` | Oficial ★×2 |
| RO7 | El trabajo de rotación aumenta | `dW = I·α·dθ` | Oficial ★×2 |
| RO8 | Producto del momento de inercia y la velocidad angular | `L = I·ω` | Oficial ★×3 |
| RO9 | Se mantiene constante | `T_ext = 0` → `L = cte` | Oficial ★×2 |
| RO10 | Función de `I`, `ω`, la masa, la velocidad `V` y `R` | `L = I·ω + m·v·R` | Oficial |
| RO11 | `I` respecto del centro de masa y velocidad del centro de masa | Energía cinética → CM | Oficial |
| RO12 | `I` respecto del punto de contacto | Eje instantáneo → contacto | Oficial |
| RO13 | Plano perpendicular al formado por `ωp` y `L` | `T = ωp × L` | Oficial |
| RO14 | La velocidad de precesión disminuye | `ωp = T / (L·sen θ)` | Oficial |
| **Bloque MH** | | | |
| MH1 | Longitudinal y transversal | Avance de la herramienta del torno | Oficial ★×2 |
| MH2 | La pieza gira y la herramienta se mueve long. y transv. | Torno | Alumnos |
| MH3 | a) y b) son correctas | Fresado cilíndrico — memorizar | Oficial ★×2 |
| MH4 | Perpendicular al plano de avance de la pieza | Fresado frontal | Oficial ★×2 |
| MH5 | La herramienta gira y la pieza se mueve en un plano horizontal, long. y transv. | Fresadora horizontal | Alumnos |
| MH6 | La pieza fija y la herramienta girando | Alesado | Oficial ★×2 |
| MH7 | La herramienta gira y la pieza se mueve en un plano horizontal | Alesadora | Alumnos |
| MH8 | Rotación en forma longitudinal de la herramienta y la pieza | Rectificado: giran las dos | Oficial ★×2 |
| MH9 | Rotación de la pieza y la herramienta + movimiento longitudinal | Rectificado (final) | Alumnos ★×2 |
| MH10 | Dimensiones crecientes en el sentido de avance | Filos de la brocha | Oficial ★×2 |
| MH11 | Rápida y de alta calidad superficial | Brochado | Alumnos ★×2 |
| MH12 | Mesa longitudinal + herramienta transversal sobre bastidor fijo | Cepillado | Oficial ★×2 |
| MH13 | Plano perpendicular a la herramienta, longitudinal y transversal | Cepilladora (final) | Alumnos ★×2 |
| MH14 | Solo en el avance del torpedo | Limadora: viruta | Oficial ★×2 |
| MH15 | Volante con una biela excéntrica | Limadora: mecanismo | Oficial ★×2 |
| MH16 | Longitudinal en sentido de avance y retroceso | Limadora: torpedo | ⚠ en duda |
| MH17 | Carro | Limadora: dónde va la herramienta | Deducida |
| MH18 | En forma vertical alternativamente | Amortajadora | Oficial ★×2 |
| MH19 | Movimiento vertical alternativo | Amortajado (final) | Alumnos ★×2 |
| **Bloque SV** | | | |
| SV1 | Compactación media y con agujereado para salida de gases | Moldeo en tierra | Oficial ★×2 |
| SV2 | "No se necesita ninguna acción posterior" (es la falsa) | Pieza fundida | Alumnos ★×2 |
| SV3 | En altura, longitudinal y transversalmente | Laminado | Oficial ★×2 |
| SV4 | Polvo → comprimir en molde → horno | Sinterizado | Oficial |
| SV5 | "a" y "b": forma y tamaño de partícula + fluir libremente | Polvos | Deducida |
| SV6 | Alta dureza | Estampa en frío (acritud) | Deducida |
| SV7 | Profundas y de bajo espesor | Repujado | Deducida ⚠ |
| **Bloque CA** | | | |
| CA1 | Resta de la señal de referencia la señal realimentada | `e = r − c` | Alumnos ★×2 |
| CA2 | La operación de los elementos de control | `G(p)` | Alumnos ★×2 |
| CA3 | `G(p) = 1/k` | Resorte | Alumnos ★×2 |
| CA4 | Inversamente proporcional a la suma de las acciones | `1/(M·p² + C·p + K)` | Alumnos ★×2 |
| CA5 | Inversamente proporcional a `Ks` | Resorte de torsión | Alumnos |
| CA6 | `Xe = (Xr − Xc)/2` | Comparador de cremalleras | Alumnos |
| CA7 | La salida aumenta constantemente con el tiempo | Integrador | Alumnos ★×2 |
| CA8 | La variable controlada es la posición de un elemento mecánico | Servomecanismo | Oficial ★×3 |
| CA9 | Se mantiene fija o constante durante períodos largos | Regulador | Oficial ★×3 |
| CA10 | Producto | `c = G(p)·e` | Deducida |
| CA11 | Un resorte equivale a una inductancia | Analogía eléctrica | Alumnos |
| CA12 | Modelo analógico | Termostato | Alumnos ★×4 |
| CA13 | Variable controlada de distinta naturaleza que la medida | Modelo analógico | Alumnos ★×2 |
| **Bloque EM** | | | |
| EM1 · EM2 | Distancia entre filetes | Paso de la rosca | Deducida |
| EM3 | Cantidad de filetes por pulgada | Hilos Whitworth | Deducida |
| EM4 | 60° | Rosca métrica | Deducida |
| EM5 | 55° | Rosca Whitworth | Deducida |
| **Bloque PI** | | | |
| PI1 | Cada 10 años, si se usó en los últimos 5 | Marca | Alumnos |
| PI2 | 20 años y no renovable | Patente | Alumnos ★×3 |
| PI3 | Vida del autor y 50 años más | Derecho de autor | Alumnos ★×3 ⚠ |
| PI4 | Ser vendida o utilizada por el inventor | Patente | Alumnos ★×3 |
| **Bloque VA** | | | |
| VA1 | Necesidad, recolección de datos y análisis, concentración, relajamiento y verificación | Proceso creativo | Oficial ★×2 |
| VA2 | Introducción, antecedentes, metodología y planos | Informe escrito (sin "conclusiones") | Oficial ★×2 |
| VA3 | Elaboración de agenda | Plan del informe | Alumnos ★×4 |
| VA4 | Conjuntamente con los proyectos técnico-funcional y económico-financiero | Proyecto de fabricación | Alumnos ★×2 |
| VA5 | Depende del proyecto de fabricación y del económico-financiero | Proyecto técnico-funcional | Alumnos ★×4 |
| VA6 | Alcanzan posiciones de costos competitivas | Planeación tecnológica | Alumnos ★×4 |
| VA7 | Análisis de la obsolescencia de las tecnologías actuales | Gerente de tecnología | Alumnos ★×4 |
| **Bloque VJ** | | | |
| VJ1 | Los factores de recursos forman parte del proceso | Toma de decisiones | Alumnos ★×2 |
| VJ2 | Las dos son verdaderas | Defectos al priorizar | Alumnos ★×3 |
| VJ3 | Análisis medios-fin (según `COMP`) | Meta clara, inicio no | ⚠ en duda |
| VJ4 | Subir la cuesta | Cada estado da un estímulo | Alumnos |
| VJ5 | Parámetros que pueden fluctuar entre ciertos valores | Variables de entrada y salida | Alumnos ★×3 |
| VJ6 | Nos pueden limitar alguna posibilidad de solución | Restricciones ficticias | Alumnos |
| VJ7 | Leyes de impacto ambiental | Ejemplo de restricción | Alumnos |
| VJ8 | Cantidad de producto, consumo de energía, temperatura final | Cámara frigorífica | Alumnos |
| VJ9 | Conocimiento de acciones para resolver un problema particular | Conocimiento procedimental | Alumnos |
| VJ10 | Buscar formas de ver el problema evitando suposiciones | Actitud creativa | ⚠ conflicto |
| VJ11 | Representar una imagen de la solución del problema | Modelo icónico | Alumnos |
| VJ12 | Velocidad de corriente de un sistema hidrodinámico | Modelo analógico | Alumnos ★×2 |
| VJ13 | Las dos verdaderas | Optimización | Alumnos ★×2 |
| VJ14 | Una búsqueda global y una búsqueda local | Método iterativo | Alumnos ★×2 |
| VJ15 | Régimen de inyección de combustible | Variable manipulada del motor | Alumnos ★×3 |
| VJ16 | El confort de las personas | Criterio en la climatización | Alumnos ★×2 |
| VJ17 | I y II son verdaderas | Base empírica | Alumnos ★×2 |
| VJ18 | a y b son correctas | Base racional = fluidodinámica | Alumnos |
| VJ19 | Mayores en peso y en tamaño que las ideales | Máquinas reales | Alumnos ★×2 |
| VJ20 | Una máquina en base empírica | Intercambiador de calor | Alumnos ★×3 |
| VJ21 | Económico-financiero, técnico-funcional y de fabricación | Proyecto de máquina | Alumnos ★×2 |
| VJ22 | Prefijadas; no se puede modificar nada | Vinculación física | Alumnos ★×2 |
| VJ23 | Solo limitada por la imaginación del procesista | Vinculación lógica | Alumnos |
| VJ24 | Continuidad asegurada si las capacidades son iguales | UET en serie | Alumnos |
| VJ25 | Pueden tener o no la misma capacidad | UET en paralelo | Alumnos ★×2 |
| VJ26 | Vinculación física | Línea de producción | Alumnos |
| VJ27 | Combinación de vinculación física y lógica | Línea de montaje | Alumnos ★×2 |
| VJ28 | Bajo costo por pieza producida | Ventaja de la vinculación física | Alumnos ★×2 |
| VJ29 | Estudio de mercado del producto a fabricar | Tipo de vinculación en una planta | Alumnos ★×2 |
| VJ30 | Negro | Pájaro en la turbina | Alumnos ★×2 |
| VJ31 | Amarillo | Agua de la montaña | Alumnos ★×2 |
| VJ32 | Rojo | "Siento que va a fracasar" | Alumnos ★×2 |
| VJ33 | Todas son falsas (según `FIN14`) | Elección del tema de tesis | ⚠ en duda |

---

## 5. Dudas abiertas

### Cómo cerrarlas: el formulario de 2023

El formulario [Preguntas de repaso — 2° Parcial — Mecánica I](https://docs.google.com/forms/d/e/1FAIpQLSd-NUSryvv3NtzLeNiHmS9I6IOdvkXt74uPvIf25cF28GB66g/viewform) muestra la clave al enviarlo. Sirve para practicar y, de paso, para confirmar las once respuestas de este banco que no tienen respaldo de una fuente con clave:

| Pregunta del formulario | Código acá | Respuesta puesta en este banco |
|---|---|---|
| 1 y 16 | EM1 · EM2 | Distancia entre filetes |
| 2 | MH17 | Carro |
| 3 | CA10 | Producto |
| 4 | EM3 | Cantidad de filetes por pulgada |
| 5 | MH16 | Longitudinal en sentido de avance y retroceso (**en duda**) |
| 11 | SV6 | Alta dureza |
| 12 | SV5 | "a" y "b" |
| 13 | SV7 | Profundas y de bajo espesor |
| 14 | EM4 | 60° |
| 15 | EM5 | 55° |

La clave del formulario la armó un alumno, no la cátedra: si contradice algo marcado `[OFICIAL]`, vale lo oficial.

### Discrepancias con el banco del 1er parcial (para el final)

Al cruzar las fuentes nuevas aparecieron respuestas distintas a las del [banco del 1er parcial](../1er_parcial/preparacion_parcial_1.md). No se tocó ese documento; quedan anotadas para cuando se prepare el final.

| Pregunta (código del 1er parcial) | Banco del 1er parcial | Lo que dicen las fuentes nuevas |
|---|---|---|
| G4 — La ingeniería de procesos consiste en | c. Control sistemático del sistema de medición (Examen A) | **a. Estudio completo y detallado de la metodología de fabricación** — así en `FIN14` y en `COMP`. Dos fuentes contra una. |
| I1 — Tercera generación: la transferencia de tecnología se realiza desde | a. Centros productivos → centros de consumo (Examen A) | b. Centros de investigación y desarrollo → centros productivos (`COMP`, parcial numerado) |
| I6 — Paquete tecnológico | c. Solo información económico-financiera (Examen A y lista de `COMP`) | a. Información técnica: manuales, planos, personas y máquinas (`COMP`, parcial numerado). El propio compilado se contradice. |
| B1 — Resorte-masa en condiciones ideales | Oscila en el tiempo (★×2) | `COMP` resalta "vuelve a su condición inicial luego de un tiempo". Probable error del compilado. |

---

## Fuentes

**Provistas (ya estaban en la carpeta de la materia):**

- `2do_parcial/fuentes/fotos_2do_parcial_2013_tema1/` — `P13`. Siete fotos (seis páginas; la 3 está dos veces) del 2° parcial Tema 1. Son las mismas que circulan en UTNianos desde diciembre de 2013.
- `2do_parcial/fuentes/PREGUNTAS PARCIAL ABUD.pdf` — `COMP`. En el 1er parcial se lo citó como "Examen B". Leyenda de colores (página 3): verde = 1er parcial, rojo = mecánica rotacional, violeta = 2° parcial; el resaltado gris viene del documento original. Las páginas están desordenadas: el parcial numerado 1–30 se lee en el orden 7 → 6 → 5 → 4 → 2.
- `final/fuentes/FinMec1Abud_resuelto.pdf` — `FIN14`.
- `material_catedra/` — `AP`: "Mecánica Rotacional" e "Ingeniería del control automático" (apuntes teóricos, ciclo 2018), Unidad VI (moldeo), Unidad VII (máquinas-herramienta: apunte y diapositivas), Unidad IX (elementos usados en ingeniería), Unidad X (árboles, ejes, engranajes) y Unidad XI (gráficos, curvas, manuales).

**Descargadas de la web** (`2do_parcial/fuentes/descargas_web/`):

- `2° Parcial - S1021.pdf` — `CV21`. Hilo de UTNianos [1° y 2° Parcial de Abud-Gallo (S1021 y S1022)](https://www.utnianos.com.ar/foro/tema-1%C2%B0y-2%C2%B0-parcial-de-abud-gallo-s1021y-s1022). Es la revisión de un intento en el campus: 26 correctas y 4 incorrectas, con la respuesta correcta de las 30.
- `formulario_repaso_2do_parcial_2023.txt` — `F23`. Transcripción de las 42 preguntas del formulario enlazado en el hilo [Práctica para 2° parcial mecánica I — Abud](https://www.utnianos.com.ar/foro/tema-aporte-practica-para-2%C2%B0-parcial-mec%C3%A1nica-i-abud). El formulario de rotacional de ese mismo hilo ya no existe.
- `Resumen 2do Parcial ABUD.pdf` — `R23`. Hilo [Resúmenes Ingeniería Mecánica 1 Abud](https://www.utnianos.com.ar/foro/tema-resumenes-ingenieria-mecanica-1-abud).
- `carpeta_completa_im1_otro_anio.pdf` — Carpeta manuscrita completa de una cursada con Abud (43 páginas). La segunda mitad del año va de la página 13 a la 43: rotacional, mecanismos, modelización, control automático, proyecto de máquinas. Sale del Drive "Mecánica 1" enlazado en el hilo [La biblioteca de Joey](https://www.utnianos.com.ar/foro/tema-recursos-parciales-carpetas-resumenes-la-biblioteca-de-joey).
- `TOMA DE DECISIONES.pdf` — Diapositivas de los seis sombreros. Hilo [Ing Mecánica 1 — Abud — Seis sombreros para pensar](https://www.utnianos.com.ar/foro/tema-ing-mec%C3%A1nica-1-abud-seis-sombreros-para-pensar).

**Otras descargas, guardadas por instancia:** `final/fuentes/descargas_web/` (respuestas manuscritas de finales viejos, del hilo [2do. Parcial y finales de Ingeniería Mecánica 1 Abud](https://www.utnianos.com.ar/foro/tema-2do-parcial-y-finales-de-ingenieria-mecanica-1-abud), y un cuestionario a desarrollar de otra cátedra) y `1er_parcial/fuentes/descargas_web/` (apunte manuscrito del 1er cuatrimestre y una grilla de respuestas sin enunciados).

**Qué se revisó y no aportó preguntas:** los 38 hilos de "Ingeniería Mecánica I" del foro de Mecánica de UTNianos. Los anteriores a 2012 son de finales a desarrollar o de otras cátedras y regionales. No apareció ninguna pregunta de engranajes, árboles, ejes ni cojinetes.

