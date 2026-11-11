# Preparación Parcial 1 — Ingeniería Mecánica I

**Profesor:** Abud  
**Fecha del examen:** jueves 2 de julio de 2026  
**Modalidad:** Multiple choice — las respuestas incorrectas restan puntos; las **no respondidas valen 0** (confirmado por Abud)  
**Fuentes:** Examen A (modelo anterior) · Examen B (segundo modelo) · S1021 (tercer modelo)  
**Estado:** banco consolidado de ~52 preguntas únicas, organizadas temáticamente.

---

## Convención de identificadores

| Marcador | Significado |
|---|---|
| `[★×2]` | Pregunta confirmada en **2 fuentes distintas** — alta probabilidad de repetición |
| `[★×3]` | Pregunta confirmada en **3 fuentes distintas** — máxima prioridad de estudio |
| `[★×3 — ⚠ RESPUESTAS PARCIALMENTE DIFIEREN]` | 3 fuentes, pero una da opción correcta distinta — leer nota |
| `[⚠ DISCREPANCIA CONCEPTUAL]` | La respuesta de Abud difiere de la definición físico-técnica estricta |
| `[⚠ SIN RESPUESTA CONFIRMADA]` | No hay respuesta marcada en ninguna fuente disponible |

---

## 1. Estrategia para el examen

### Regla del juego: incorrectas restan

```
Puntaje = (correctas × +1) + (incorrectas × −P) + (no respondidas × 0)
```

Donde `P` es la penalidad por respuesta incorrecta. Aunque Abud no especificó el valor exacto, la fórmula estándar en Argentina es `P = 1 / (opciones − 1)`:

| Nº de opciones por pregunta | Penalidad por error |
|---|---|
| 3 opciones | −0,50 |
| 4 opciones | −0,33 |
| 5 opciones | −0,25 |
| 6 opciones | −0,20 |

Con esa fórmula, adivinar al azar da esperanza matemática = 0. El secreto está en **eliminar opciones**.

### Regla de oro: la eliminación es tu herramienta principal

```
¿Podés eliminar al menos 1 opción?  →  SÍ → respondé (esperanza positiva)
                                     →  NO → dejá en blanco (esperanza neutra)
```

Ejemplo con 3 opciones y penalidad −0,5:
- Adivinás al azar (1/3 chance): E = 1/3 × 1 + 2/3 × (−0,5) = 0 → neutro
- Eliminaste 1, elegís entre 2 (1/2 chance): E = 1/2 × 1 + 1/2 × (−0,5) = +0,25 → conveniente
- Sabés la respuesta (certeza): E = +1 → siempre respondé

### Estadísticas de aprobación

El examen tiene **30 preguntas** de 1 punto cada una. La nota final:

```
Nota = puntaje_bruto × (10 / 30)       Para aprobar con 6: puntaje_bruto ≥ 18
```

**Escenarios con penalidad −0,5 (preguntas de 3 opciones):**

| Correctas | Incorrectas | No respondidas | Puntaje bruto | Nota (/10) | ¿Aprueba? |
|---|---|---|---|---|---|
| 30 | 0 | 0 | 30,0 | 10,0 | ✓ |
| 24 | 0 | 6 | 24,0 | 8,0 | ✓ |
| 20 | 4 | 6 | 18,0 | 6,0 | justo |
| 18 | 0 | 12 | 18,0 | 6,0 | justo |
| 18 | 1 | 11 | 17,5 | 5,8 | ✗ |
| 20 | 8 | 2 | 16,0 | 5,3 | ✗ |

**Conclusión práctica:** respondé todo lo que sabés con certeza y dejá el resto en blanco.

---

> **NOTA sobre el sistema de penalidades de Abud:**
>
> **Confirmado por Abud:** las preguntas no respondidas valen 0 — no restan.
>
> **No confirmado:** la penalidad exacta por error. Abud dice tener "su tablita" pero no la divulga. La fórmula `P = 1 / (opciones − 1)` es el estándar argentino con base matemática sólida. Es razonable asumirla, pero el puntaje exacto puede variar.

---

### Checklist antes de enviar

- [ ] Releé el enunciado completo — muchas trampas están en "NO", "SOLO", "NUNCA"
- [ ] Tratamientos térmicos: cementación (C) / nitruración (N) / cianuración (C+N) / temple (rápido) / recocido (lento)
- [ ] Aleaciones: latón = Cu+Zn, bronce = Cu+Sn — fácil de invertir bajo presión
- [ ] % C: acero < 2%, fundición 2–4% — el límite 2% es el más preguntado
- [ ] SAE: los dos últimos dígitos son el % de C en centésimas (1045 → 0,45% C)

---

## 2. Banco de preguntas por bloque temático

---

### Bloque A — Ingeniería: definición y metodología

---

#### A1 — Dentro de la definición de la ingeniería encontramos:

- ( ) a. Buscar una solución sólo utilizando el conocimiento empírico.
- ( ) b. Buscar una solución utilizando métodos científicos y empíricos.
- ( ) c. Buscar una solución utilizando el sentido común y la investigación.
  - I. A y b verdaderas, c falsa.
  - II. A y c verdaderas, b falsa.
  - III. A, b y c falsas.
  - IV. A, b y c verdaderas.
  - **(✓) V. B y c verdaderas, a falsa.**

> La ingeniería combina métodos científicos (b) y empíricos/sentido común (c). La a es falsa porque dice "sólo empírico" — ese "sólo" la invalida.

---

#### A2 — La resistencia de materiales tiene como fin: `[★×3]`

- **(✓) Determinar y juzgar las características del sólido y su aplicación práctica.**
- ( ) Elaborar métodos de cálculo exactos, complejos y voluminosos.
- ( ) No considerar el fenómeno de los resultados prácticos.

> La ResistMat es una disciplina aplicada: evalúa el comportamiento de un sólido bajo cargas para decidir si es apto para su uso. Confirmada en Examen A, Examen B y S1021.

---

#### A3 — Dentro de las habilidades básicas de la ingeniería tenemos la optimización, que consiste en:

- ( ) a. El ingeniero se debe ajustar a la solución más económica.
- **(✓) b. El ingeniero debe buscar más de una solución y luego seleccionar la mejor.**
- ( ) c. El ingeniero debe buscar la mejor solución técnico-funcional independientemente del análisis económico.

> Optimización = generar múltiples alternativas → seleccionar la más adecuada según criterios técnicos y económicos. La a fija solo el criterio económico; la c ignora el económico. Ambas son incorrectas por excluyentes.

---

#### A4 — El proceso de modelado para la resolución de un problema en ingeniería, en el siguiente orden: `[★×3]`

- ( ) a. Formulaciones matemáticas → hipótesis → comprobar predicciones → obtener soluciones.
- **(✓) b. Hipótesis → formulaciones matemáticas → obtener soluciones → comprobar las predicciones con hechos conocidos.**
- ( ) c. Hipótesis → comprobar predicciones → formulaciones matemáticas → obtener soluciones.

> Secuencia de Abud: (1) hipótesis, (2) modelo matemático, (3) resolver, (4) verificar. La verificación siempre al final. Confirmada en Examen A, Examen B y S1021.

---

#### A5 — La formulación del modelo matemático de un sistema se inicia con: `[★×2]`

- ( ) I) Identificación de **algunas** variables. II) Determinación de las variables restantes por hipótesis.
- **(✓) I) Identificación de las variables que ocasionan el cambio del sistema. II) Se establecen un conjunto de hipótesis.**
- ( ) Solo la aplicación de leyes empíricas que contienen algunas de las variables.

> La diferencia entre a y b: la a dice "algunas variables" (incompleto), la b dice "las variables que ocasionan el cambio" (correcto). Confirmada en Examen A y S1021.

---

#### A6 — En una estructura simple (viga apoyada) con carga en el centro: `[★×3]`

- ( ) a. No hay relación entre la fuerza y la curva de deflexión.
- **(✓) b. La relación entre la fuerza y la curva de deflexión es un problema matemático.**
- ( ) c. La curva de deflexión es una constante que no depende de las dimensiones de la estructura.

> a es falsa (hay relación directa). c es falsa (la deflexión depende de dimensiones, material, sección). b es la única correcta: la relación existe y tiene forma matemática (`δ = F·L³ / 48·E·I`). Confirmada en Examen A, Examen B y S1021.

---

#### A7 — El propósito principal de los ensayos de tracción y compresión consiste en: `[★×3 — ⚠ RESPUESTAS PARCIALMENTE DIFIEREN]`

> ════════════════════════════════════════════════════════════
> ⚠  ESTA PREGUNTA APARECIÓ EN LAS 3 FUENTES. DOS DICEN "TENSIÓN", UNA DICE "FUERZA"
> ════════════════════════════════════════════════════════════
>
> **Examen A → "tensión y alargamiento"** `[CORRECTA]`  
> **S1021 → "tensión y alargamiento"** `[CORRECTA]`  
> **Examen B → "fuerza y alargamiento"** `[CORRECTA]`
>
> **Qué significa:** 2 de 3 fuentes confirman "tensión y alargamiento" como respuesta estándar de Abud. El Examen B usó una versión alternativa con opciones de texto diferente ("fuerza" en lugar de "tensión"). Ambas describen el mismo fenómeno desde ángulos distintos: el diagrama `σ-ε` (tensión vs. deformación unitaria) es la versión normalizada; el diagrama `F-δ` (fuerza vs. alargamiento absoluto) es la versión bruta del mismo experimento.
>
> **Estrategia:** la respuesta por defecto de Abud es **"tensión y alargamiento"**. Descartá siempre "fuerza vs. tiempo de rotura" y "alargamiento vs. temperatura" — falsas en cualquier versión. Si aparece solo la opción "fuerza-alargamiento" (sin la de "tensión"), marcala.

Opciones que circulan:
- ( ) Determinar la relación entre la fuerza y el tiempo de rotura. ← **siempre falsa**
- ( ) Construir un diagrama que relaciona alargamiento y temperatura. ← **siempre falsa**
- **(✓ preferida) Determinar la dependencia entre la tensión y su alargamiento.** ← correcta en ExA y S1021
- ( ) Determinar la dependencia entre la fuerza y alargamiento. ← correcta en ExB (si la otra no aparece)

---

### Bloque B — Sistemas mecánicos

---

#### B1 — El sistema resorte-masa en condiciones ideales es: `[★×2]`

- ( ) Un sistema cuya posición no depende del tiempo una vez apartado del equilibrio.
- ( ) Un sistema que al ser apartado del equilibrio vuelve a su condición inicial al cabo de un tiempo.
- **(✓) Un sistema que oscila en el tiempo una vez apartado de su posición de equilibrio.**

> Sin amortiguamiento, oscila indefinidamente con `ω_n = √(k/m)`. No vuelve a su posición inicial (requiere amortiguamiento) ni es independiente del tiempo (sería equilibrio estático). Confirmada en Examen A y S1021.

---

#### B2 — En un sistema mecánico resorte-masa con amortiguamiento viscoso: `[★×3]`

- ( ) a. Las fuerzas de amortiguamiento no dependen de las velocidades instantáneas.
- ( ) b. Las fuerzas de amortiguamiento son proporcionales a las velocidades instantáneas.
- ( ) c. Las fuerzas de amortiguamiento dependen de las constantes del resorte y el medio viscoso.
  - I. A y c son verdaderas.
  - **(✓) II. B y c son verdaderas.**
  - III. A, b y c son falsas.

> b es inequívocamente correcta: `F_d = c · ẋ`. Abud considera c verdadera interpretando "constantes del medio viscoso" como el coeficiente `c` que depende del fluido. Nota: en rigor, la fuerza de amortiguamiento NO depende de `k` (rigidez del resorte). Pero para el examen de Abud: marcar II. Confirmada en Examen A, Examen B y S1021.

---

#### B3 — Según lo analizado en los sistemas resorte-masa con o sin amortiguamiento, ¿en qué casos se aplican?

- ( ) a. Una viga empotrada con una carga fija en el tiempo.
- **(✓) b. Una máquina con movimiento alternativo como un compresor o un motor.**
- ( ) c. Un eje con movimiento de rotación pero con una carga fija en el tiempo.

> El modelo resorte-masa aplica cuando hay fuerzas variables en el tiempo (dinámicas). Las máquinas con movimiento alternativo generan vibraciones cíclicas — es exactamente ese tipo de sistema. Las opciones a y c tienen cargas estáticas o constantes.

---

#### B4 — En la ingeniería, haciendo un estricto análisis de un sistema y utilizando los materiales adecuados:

- **(✓) a. No existen los sistemas ideales.**
- ( ) b. Existen los sistemas ideales pero con alto costo económico.
- ( ) c. Existen los sistemas ideales siempre que contemos con el tiempo para desarrollarlos.

> La ingeniería real siempre opera con tolerancias, variación de propiedades y cargas impredecibles. Ningún sistema puede ser "ideal" en sentido absoluto.

---

### Bloque C — Solicitaciones internas

---

#### C1 — El momento flector resulta de reducir la resultante de las fuerzas que actúan a la izquierda de la sección considerada al: `[★×2]`

- **(✓) Baricentro de la sección.**
- ( ) Al cuadrado de la distancia al baricentro de la misma.
- ( ) A una distancia determinada del eje neutro.
- ( ) A un eje paralelo al eje neutro.

> M se calcula respecto al baricentro (centroide), que coincide con el eje neutro en secciones simétricas. Reducir "al cuadrado" no tiene sentido dimensional; las opciones c y d confunden con el teorema de Steiner. Confirmada en Examen A y S1021.

---

#### C2 — Una tensión es una fuerza interna por: `[★×2]`

- **(✓) Unidad de área.**
- ( ) Unidad de longitud.
- ( ) Unidad de volumen.
- ( ) Ninguna es correcta.

> `σ = F / A` [N/m² = Pa]. Nunca longitud ni volumen. Confirmada en Examen A y S1021.

---

#### C3 — En una barra biapoyada con carga central perpendicular al eje neutro, la mitad superior está sometida a: `[★×2]`

- ( ) Ninguna es correcta.
- **(✓) Compresión.**
- ( ) Tracción.
- ( ) Torsión.

> Viga biapoyada, carga vertical hacia abajo: la fibra superior se acorta (compresión), la inferior se alarga (tracción). La torsión no aparece en este esquema. Confirmada en Examen A y S1021.

---

#### C4 — En una pieza sometida al corte, las fuerzas actuantes: `[★×2 | ⚠ DISCREPANCIA CONCEPTUAL]`

- **(✓ EXAMEN) Están contenidas en el mismo plano.**
- ( ) Están contenidas en planos perpendiculares.
- ( ) Están contenidas en diferentes planos paralelos.

> **Respuesta de Abud: "mismo plano"** — confirmada en Examen A y S1021.
>
> **Discrepancia con la física estricta:** el esfuerzo cortante interno se genera cuando fuerzas actúan en planos paralelos muy próximos (como en una guillotina). Sin embargo, Abud enfoca la pregunta en las **fuerzas externas** que producen el corte (ej. las dos fuerzas sobre un bulón), que sí son coplanares. La respuesta de Abud es consistente y está doblemente confirmada — marcar "mismo plano" sin dudar.

---

### Bloque D — Propiedades mecánicas y fenómenos de falla

---

#### D1 — La dureza de un material se define por: `[★×2]`

- ( ) La penetración superficial de una bolilla en una atmósfera rica en carbono.
- **(✓) La penetración de una bolilla sobre la superficie del material, bajo una carga determinada.**
- ( ) La penetración de una bolilla en una superficie debido a una alta temperatura.

> La dureza se mide en superficie. Ensayos Brinell, Rockwell y Vickers: indentador bajo carga conocida → medir la huella. La opción a describe la cementación; la c es incorrecta (la temperatura altera la dureza, no la define). Confirmada en Examen A y S1021.

---

#### D2 — La resiliencia es una característica cuya energía absorbida se produce por: `[★×2]`

- ( ) Calentamiento.
- **(✓) Deformación elástica.**
- ( ) Deformación plástica.

> Resiliencia = energía almacenada en la zona **elástica** del diagrama σ-ε (devuelve al soltar la carga). La deformación plástica caracteriza la tenacidad. Confirmada en Examen A y S1021.

---

#### D3 — La tenacidad es: `[★×2]`

- **(✓) La energía de deformación total absorbida debido a la acción de una carga.**
- ( ) La energía de deformación plástica.
- ( ) La energía absorbida durante la deformación elástica.

> Tenacidad = área total bajo la curva σ-ε (elástica + plástica, hasta la rotura). La opción b omite la parte elástica. La opción c es la definición de resiliencia. Confirmada en Examen A y S1021.

---

#### D4 — El pandeo es un fenómeno de pérdida de la estabilidad, por lo tanto: `[★×2]`

- **(✓) La relación entre la altura y la sección es fundamental.**
- ( ) La relación entre la altura y su distancia al cuadrado de su baricentro debe ser proporcional.
- ( ) La relación entre la altura y la sección no es importante.

> El pandeo depende de la **esbeltez** de la columna: a mayor relación altura/sección, más susceptible. `P_cr = π²·E·I / L²` (Euler). La opción c es directamente falsa. Confirmada en Examen A y S1021.

---

#### D5 — El fenómeno de fatiga de materiales se produce por: `[★×2]`

- ( ) Cargas constantes y temperaturas bajo cero.
- **(✓) Cargas cíclicas.**
- ( ) Temperaturas muy extremas.

> Fatiga = falla por acumulación de daño bajo cargas **repetidas/cíclicas**, incluso si cada ciclo está por debajo del límite elástico. El eje de tren es el ejemplo canónico. Confirmada en Examen A y S1021.

---

#### D6 — La concentración de tensiones en una pieza sometida a esfuerzos se debe a: `[★×2]`

- ( ) Secciones rectangulares solamente.
- ( ) Cambios suaves de una sección a otra.
- **(✓) Cambios bruscos de sección.**

> La concentración de tensiones ocurre donde la geometría cambia abruptamente (ranuras, taladros, escalones). Los cambios suaves la reducen — de ahí los redondeos de filetes. Confirmada en Examen A y S1021.

---

### Bloque E — Clasificación de materiales

---

#### E1 — El acero es: `[★×2]`

- ( ) a. Una aleación Fe-C con un contenido menor al 3% de C.
- ( ) b. Una aleación Fe-C con cualquier % de C.
- **(✓) c. Una aleación Fe-C con un contenido menor al 2% de C.**
- ( ) d. Una aleación Fe-C con un contenido menor al 4% de C.

> El límite 2% de carbono es la frontera entre acero y fundición en el diagrama Fe-C. El dato más preguntado de la materia. Confirmada en Examen A y S1021.

---

#### E2 — Una fundición de hierro es: `[★×2]`

- **(✓) Una aleación Fe-C con un contenido mayor al 2% de C.**
- ( ) Una aleación Fe-C con un contenido mayor al 1,5% y menor al 2% de C.
- ( ) Una aleación Fe-C con un contenido mayor al 4% de C.
- ( ) Una aleación Fe-C con un % de C menor al 0,5.

> Por encima del 2% C (hasta ~4%) es fundición. La opción c confunde el límite definitorio con el extremo superior del rango. Confirmada en Examen A y S1021.

---

#### E3 — SAE 1045: `[★×2]`

- **(✓) Un acero al carbono con un 0,45% de C.**
- ( ) Un acero al Cr-Ni con un 0,45% de C.
- ( ) Un acero con un contenido de 4,5% de C.

> SAE 4 dígitos: primer dígito = tipo (1 = carbono puro); últimos dos = % C en centésimas (45 → 0,45%). Cr-Ni sería serie 3XXX. Confirmada en Examen A y S1021.

---

#### E4 — Los materiales cerámicos (arcillas y derivados), sus propiedades para uso tecnológico son: `[★×2]`

- **(✓) Gran dureza y una alta resistencia al rozamiento y desgaste.**
- ( ) Gran dureza y baja resistencia a la corrosión.
- ( ) Alta dureza, pero soportan temperaturas no muy elevadas.

> Los cerámicos son muy duros, resistentes al desgaste, a la corrosión y a altas temperaturas — por eso b y c son falsas. Confirmada en Examen A y S1021.

---

#### E5 — El latón es una aleación: `[★×2]`

- ( ) Cu - Sn
- **(✓) Cu - Zn**
- ( ) Cu - Ni
- ( ) Cu - Al

> Latón = cobre + zinc. Bronce = cobre + estaño. El par latón/bronce es el más confundible del examen — estudiarlo junto con E6. Confirmada en Examen A y S1021.

---

#### E6 — El bronce es: `[★×2]`

- **(✓) Una aleación Cu-Sn.**
- ( ) Una aleación Cu-Mn.
- ( ) Una aleación Cu-Cr-Ni.
- ( ) Una aleación Cu-Zn.

> Bronce = cobre + estaño (Sn). Memorizar junto con E5: latón (Zn) vs. bronce (Sn). Confirmada en Examen A y S1021.

---

### Bloque F — Tratamientos térmicos y termoquímicos

---

#### F1 — La cementación se logra: `[★×2]`

- ( ) Calentando el acero en una atmósfera rica en cemento.
- **(✓) Calentando el acero en una atmósfera rica en carbono.**
- ( ) Calentando el acero en una atmósfera rica en nitrógeno.
- ( ) Calentando el acero en una atmósfera rica en silicio.
- ( ) Calentando el acero y enfriándolo rápidamente en una sustancia líquida.

> Cementación = carburización = introducir carbono en la superficie. La opción c describe la nitruración; la e describe el temple. Confirmada en Examen A y S1021.

---

#### F2 — El temple se realiza para: `[★×2 | ⚠ DISCREPANCIA CONCEPTUAL]`

- ( ) Eliminar tensiones internas.
- **(✓ EXAMEN) Obtener una dureza superficial y una alta tenacidad en el núcleo.**
- ( ) Obtener una dureza en el núcleo y una superficie dúctil.
- ( ) Ninguna es correcta.

> **Respuesta de Abud: b)** — confirmada en Examen A y S1021.
>
> **Discrepancia con la física estricta:** el temple convencional produce martensita en toda la pieza (no solo en la superficie), siendo uniforme si el espesor es pequeño. La respuesta b describe más precisamente el **temple superficial** o lo que ocurre en piezas gruesas. Sin embargo, esta es la respuesta que Abud valida consistentemente. La opción a describe el recocido; la c invierte superficie y núcleo. Marcar b) sin dudar.

---

#### F3 — La cianuración se logra: `[★×2 | ⚠ DISCREPANCIA CONCEPTUAL]`

- ( ) Calentando el acero en una atmósfera rica en azufre.
- **(✓ EXAMEN) Ninguna es correcta.**
- ( ) Calentando el acero en una atmósfera rica en nitrógeno.
- ( ) Calentando el acero en una atmósfera rica en carburo de hierro.

> La cianuración se realiza sumergiendo el acero en un **baño de sales de cianuro fundido** (no en "atmósfera"). Ninguna opción describe esto, de ahí la respuesta "ninguna". Nitrógeno (opción c) = nitruración. Confirmada en Examen A y S1021.

---

#### F4 — El recocido se utiliza para: `[★×2]`

- **(✓) Eliminar tensiones internas.**
- ( ) Darle una dureza superficial.
- ( ) Conferirle una dureza en toda la estructura.

> Recocido = enfriamiento muy lento → ferrita + perlita → blando y dúctil. Sirve para aliviar tensiones residuales (de soldadura, mecanizado, conformado). Confirmada en Examen A y S1021.

---

### Bloque G — Ingenierías especializadas y producción

---

#### G1 — La ingeniería de producción se dedica a: `[★×2]`

- ( ) Mantenimiento de las máquinas afectadas a producción.
- **(✓) Programación y control de los procesos de fabricación.**
- ( ) Programación de los procesos industriales.

> Ing. de producción = planificar, programar y controlar la fabricación. El mantenimiento corresponde a ing. de mantenimiento. La opción c es más vaga y omite el control. Confirmada en Examen A y S1021.

---

#### G2 — La ingeniería de manufactura se dedica a: `[★×2]`

- ( ) Mantenimiento de todas las maquinarias de planta.
- ( ) Proyecto y desarrollo de la producción.
- **(✓) Planificación de los procesos de fabricación.**

> Manufactura = fabricar. La ing. de manufactura planifica cómo se fabrica cada pieza: secuencia de operaciones, máquinas, herramientas, tiempos. Confirmada en Examen A y S1021.

---

#### G3 — En la ingeniería de proyectos, el análisis económico financiero: `[★×2]`

- ( ) Se realiza en una etapa final del proyecto.
- **(✓) Se realiza conjuntamente con el proyecto técnico funcional y de fabricación.**
- ( ) No guarda relación alguna con los proyectos técnico funcional y de fabricación.

> El análisis económico es transversal al proyecto: condiciona decisiones de diseño, materiales y fabricación desde el inicio. Confirmada en Examen A y S1021.

---

#### G4 — La ingeniería de procesos consiste en:

- ( ) Un completo y detallado estudio de la metodología de fabricación.
- ( ) Un completo y detallado estudio del sistema de mantenimiento.
- **(✓) Un control sistemático del sistema de medición.**

> Definición de Abud para ingeniería de procesos: control sistemático del sistema de medición. Distinto a manufactura (planificación de fabricación) y producción (programación y control).

---

#### G5 — La intercambiabilidad de piezas es de capital importancia para el sistema de maquinarias, debido a que:

- ( ) Una pieza defectuosa puede ser intercambiada a alto costo, pero rápidamente.
- **(✓) Una pieza defectuosa puede ser intercambiada a bajo costo.**
- ( ) Una pieza defectuosa puede ser reemplazada, pero con un minucioso ajuste al lugar de montaje.

> La intercambiabilidad elimina la necesidad de ajustes individuales — las piezas fabricadas dentro de tolerancias se montan directamente. Eso reduce el costo de reemplazo.

---

#### G6 — La importancia de la intercambiabilidad para el fabricante:

- ( ) a. Exige fabricar piezas con exactitud perfecta (sin discrepancia ni tolerancia).
- ( ) b. Excluye la necesidad de exactitud perfecta — admite tolerancias dentro de un rango.
- ( ) c. Permite utilizar calibradores límites.
  - I. A y b son correctas.
  - II. A y c son verdaderas.
  - **(✓) III. B y c son verdaderas.**
  - IV. A, b y c son falsas.

> La intercambiabilidad para el fabricante implica: (b) trabajar con tolerancias, no exactitud perfecta; (c) verificar con calibradores límites (pasa/no pasa). La opción a es falsa: exigir "sin tolerancia" contradice el concepto mismo.

---

### Bloque H — Mantenimiento

---

#### H1 — El mantenimiento se puede definir de la siguiente manera:

- ( ) Programación adecuada de los procesos industriales.
- ( ) Estado de conservación adecuada de los medios económicos y humanos de la industria.
- **(✓) Estado de conservación adecuada de los medios físicos involucrados en los procesos industriales.**

> El mantenimiento cuida los **medios físicos** (máquinas, equipos, instalaciones). La opción b habla de "medios económicos y humanos" — incorrecto. La a describe programación de producción.

---

#### H2 — El mantenimiento preventivo busca principalmente:

- ( ) a. Reponer el material auxiliar y de consumo.
- ( ) b. Conservar el estado real igual al estado teórico.
- ( ) c. Adelantarse a la posibilidad de ocurrencia de una falla.
- ( ) d. A, b, c son falsas.
- **(✓) e. A, b y c son verdaderas.**

> El mantenimiento preventivo incluye las tres acciones simultáneamente: reponer materiales de consumo (a), conservar el estado real = estado teórico (b), y anticiparse a las fallas (c).

---

#### H3 — El costo de una falla se divide en: debido a la propia falla y debido al lucro cesante. Las debidas a la falla se dividen en 3 partes. ¿Cuál es la correcta?

- ( ) a. Costos fijos y costos de operación.
- ( ) b. Amortización, seguros e impuestos.
- **(✓) c. Rotura, material de producción y desgaste anormal de la máquina.**
- ( ) d. Rotura, desgaste anormal de la máquina e interés sobre el capital.

> Las 3 subcategorías del costo directo de una falla: (1) rotura del componente, (2) material de producción desperdiciado/dañado, (3) desgaste anormal de la máquina. La opción d casi coincide pero reemplaza "material de producción" por "interés sobre el capital" — ese es un costo financiero, no de falla directa.

---

### Bloque I — Transferencia tecnológica y gestión

---

#### I1 — En las empresas de tercera generación, la transferencia tecnológica en los países desarrollados se realiza desde:

- **(✓) Los centros productivos hacia los centros de consumo.**
- ( ) Los centros de investigación y desarrollo hacia los centros productivos.
- ( ) Los centros de consumo hacia los centros de investigación.

> En la tercera generación la tecnología está madura y se difunde: desde donde se produce hacia donde se consume.

---

#### I2 — En las empresas de tercera generación:

- ( ) Los investigadores deciden qué deben investigar.
- **(✓) Los gerentes de negocios indican qué investigar.**
- ( ) Los gerentes de negocios y los investigadores deciden qué investigar conjuntamente.

> En la tercera generación la I+D está orientada al mercado: los gerentes de negocios (no los científicos) marcan las prioridades según necesidades comerciales.

---

#### I3 — Las empresas que realizan una planeación tecnológica a profundidad:

- **(✓) Alcanzan posiciones de costos competitivos.**
- ( ) Los planes tecnológicos buscan corregir sólo problemas operativos.
- ( ) Poseen consejos de administración que privilegian la minimización del rendimiento a corto plazo.

> La planeación tecnológica profunda permite anticipar cambios y reducir costos a largo plazo. Las opciones b y c describen comportamientos reactivos o miopes.

---

#### I4 — Una de las tareas del gerente de tecnología es:

- ( ) Análisis técnico de los productos fabricados.
- ( ) Organizar políticas de mantenimiento.
- **(✓) Análisis de la obsolescencia del departamento.**

> El gerente de tecnología evalúa si los departamentos están tecnológicamente desactualizados. El análisis de productos corresponde a ingeniería de calidad; el mantenimiento es otro área.

---

#### I5 — Una de las tareas del gerente de tecnología es: (variante — pregunta distinta en el mismo examen)

- ( ) Análisis técnico de los productos fabricados.
- ( ) Organizar políticas de mantenimiento.
- **(✓) Análisis de obsolescencia de las tecnologías actuales.**

> Abud hizo dos preguntas sobre el gerente de tecnología en el mismo examen con respuestas levemente distintas. I4 apunta a la obsolescencia del **departamento** (la unidad organizacional); I5 apunta a la obsolescencia de las **tecnologías** en uso. Ambas son tareas reales del rol — memorizar como par.

---

#### I6 — En la transferencia de tecnología hablamos del paquete tecnológico, que puede contener:

- ( ) a. Información técnica como manuales, planos, personas y máquinas.
- ( ) b. Piezas de máquinas que deben ser ensayadas.
- **(✓) c. Sólo información económica financiera de la tecnología a adoptar.**

> Respuesta según el modelo de examen de Abud. Nota: en la literatura general, el "paquete tecnológico" incluye información técnica (manuales, planos, know-how). La respuesta de Abud puede corresponder a una definición específica usada en clase. Verificar con apuntes de clase si hay duda.

---

### Bloque J — Propiedad intelectual

---

#### J1 — Una patente tiene una duración de:

- ( ) 20 años y renovable.
- ( ) 10 años y renovable.
- **(✓) 20 años y no renovable.**
- ( ) 15 años y no renovable.

> En Argentina (y bajo el Acuerdo TRIPS/ADPIC), las patentes duran **20 años desde la fecha de presentación** y no son renovables. Al vencer, la invención pasa al dominio público.

---

#### J2 — El derecho de autor tiene una duración de:

- ( ) Por vida del autor.
- ( ) 50 años desde su publicación.
- **(✓) Por vida del autor y 50 años más.**
- ( ) Por vida del autor y 25 años más.

> En Argentina (Ley 11.723), los derechos de autor protegen la obra durante toda la vida del autor y un período adicional. Usar el valor que Abud enseñó: vida + 50 años.

---

#### J3 — Cuando se obtiene una patente por una maquinaria o dispositivo innovador, esta puede:

- ( ) Sólo ser utilizada por el inventor sin posibilidad de que la utilice otro.
- **(✓) Ser vendida o utilizada por el inventor.**
- ( ) Ser utilizada por el inventor de por vida sin que nadie más pueda utilizarla.

> La patente otorga derechos exclusivos temporales, pero el titular puede venderla (cesión), licenciarla o explotarla directamente. No es un derecho vitalicio ni exclusivo sine die.

---

### Bloque K — Metodología académica

---

#### K1 — Las partes del plan para la elaboración de una tesis son: definición del problema, confección del bosquejo y:

- ( ) a. Elaboración de conclusiones.
- **(✓) b. Elaboración de la agenda.**
- ( ) c. Desarrollo del tema.

> Las tres partes del plan de tesis: (1) definición del problema, (2) confección del bosquejo (estructura), (3) elaboración de la agenda (cronograma). Las conclusiones y el desarrollo son partes de la tesis en sí, no del plan previo.

---

#### K2 — Una de las razones de la necesidad de incluir referencias es: `[⚠ SIN RESPUESTA CONFIRMADA]`

- ( ) a. Para elaborar conclusiones.
- ( ) b. Para corroborar o respaldar las propias opiniones.
- ( ) c. Para establecer hipótesis.

> **Ninguna fuente disponible marca la respuesta correcta para esta pregunta.** La opción más lógica es b (respaldar las propias opiniones con evidencia de terceros), que es la función principal de las referencias académicas. Estudiar con cautela.

---

#### K3 — Las citas se pueden clasificar en 3 clases:

- ( ) a. Directas, semi-directas y cita secundaria.
- ( ) b. Indirectas, cita de cita y directas.
- **(✓) c. Directas, citas primaria e indirectas.**

> Clasificación de citas: (1) directas (textuales), (2) primaria (fuente original parafraseada), (3) indirectas (resumidas o reformuladas).

---

## 3. Resumen de contenidos por bloque

### Bloque A — Ingeniería: definición y metodología

**Ingeniería = métodos científicos + empíricos.** No solo uno de los dos.

**Proceso de modelado:**
```
1. Identificar variables que ocasionan el cambio
2. Establecer hipótesis
3. Formular el modelo matemático
4. Obtener soluciones
5. Comprobar predicciones con hechos conocidos (siempre al final)
```

**Optimización:** generar múltiples alternativas → seleccionar la mejor según criterios técnicos y económicos.

---

### Bloque B — Sistemas mecánicos

**Sistema resorte-masa:**
- Sin amortiguamiento (ideal): oscila indefinidamente, `ω_n = √(k/m)`
- Con amortiguamiento viscoso: `F_d = c · ẋ` (proporcional a la velocidad)
- Aplicación práctica: máquinas con movimiento alternativo (compresores, motores de pistones)
- Los sistemas reales **no son ideales**: siempre hay pérdidas, tolerancias, desgaste

---

### Bloque C — Solicitaciones internas

**Los cuatro esfuerzos característicos:**

| Esfuerzo | Símbolo | Tensión generada |
|---|---|---|
| Axial (normal) | N | σ = N/A |
| Cortante | Q | τ = Q/A |
| Momento flector | M | σ = M·y / I |
| Momento torsor | T | τ = G·ρ·θ |

**Flexión pura — viga biapoyada con carga hacia abajo:**
```
  ─────────── fibra superior: COMPRESIÓN (−σ)
  ─── ─── ─── eje neutro: σ = 0
  ─────────── fibra inferior: TRACCIÓN (+σ)
```

**Momento flector M:** se calcula al baricentro de la sección.

---

### Bloque D — Propiedades mecánicas y fenómenos de falla

| Propiedad | Definición |
|---|---|
| **Resiliencia** | Energía en zona **elástica** — se devuelve al soltar la carga |
| **Tenacidad** | Energía total hasta la rotura (elástica + plástica) |
| **Dureza** | Resistencia a la penetración superficial (Brinell / Rockwell / Vickers) |

**Ensayo de tracción:** produce el diagrama σ-ε → extrae E, límite elástico, resistencia a la rotura, ductilidad.

**Pandeo:** pérdida de **estabilidad** antes de alcanzar el límite elástico. `P_cr = π²·E·I / L²`.

**Fatiga:** falla por cargas **cíclicas** repetidas aunque estén por debajo del límite elástico.

**Concentración de tensiones:** en cambios **bruscos** de sección. Los redondeos de filetes la reducen.

---

### Bloque E — Clasificación de materiales

```
  % C     0,05          2%                   4%
          │─────────────│────────────────────│
          Acero         │                    Fundición
                        └── límite Fe-C más preguntado
```

**SAE:** primer dígito = tipo de aleante; últimos dos dígitos = % C en centésimas.

| Aleación | Componentes | Mnemotecnia |
|---|---|---|
| Latón | Cu + Zn | **La**tón → **Za**patos (Zn) |
| Bronce | Cu + Sn | **Br**once → e**St**año (Sn) |

**Cerámicos:** gran dureza, alta resistencia al desgaste, a la corrosión y a altas temperaturas.

---

### Bloque F — Tratamientos térmicos y termoquímicos

| Tratamiento | Enfriamiento | Para qué sirve |
|---|---|---|
| **Recocido** | Muy lento (horno) | Eliminar tensiones internas |
| **Normalizado** | Moderado (aire) | Homogeneizar estructura |
| **Temple** | Rápido (agua/aceite) | Aumentar dureza |
| **Revenido** | Calentamiento suave post-temple | Reducir fragilidad del temple |

| Tratamiento | Elemento difundido | Cómo |
|---|---|---|
| **Cementación** | C | Atmósfera rica en carbono |
| **Nitruración** | N | Atmósfera de amoníaco |
| **Cianuración** | C + N | Baño de sales de cianuro fundido |

Regla: **Ce**mentación → **C**arbono. **Ni**truración → **Ni**trógeno. **Ci**anuración → **C+N**.

---

### Bloque G — Ingenierías especializadas

| Especialidad | Función |
|---|---|
| **Ing. manufactura** | Planificación de los procesos de fabricación |
| **Ing. producción** | Programación y control de los procesos de fabricación |
| **Ing. mantenimiento** | Mantenimiento de máquinas de planta |
| **Ing. proyectos** | Análisis técnico + económico-financiero integrado (no al final) |
| **Ing. de procesos** | Control sistemático del sistema de medición (def. Abud) |

**Intercambiabilidad:** fabricar con tolerancias → montaje directo sin ajuste → bajo costo de reemplazo. Verificación: calibradores límites (pasa/no pasa).

---

### Bloque H — Mantenimiento

**Definición:** conservación adecuada de los **medios físicos** involucrados en los procesos industriales.

**Mantenimiento preventivo:** reponer materiales de consumo + conservar estado real = estado teórico + adelantarse a fallas. Las tres son verdaderas simultáneamente.

**Costos de la falla:**
```
Costo total
├── Debidos a la propia falla
│   ├── Rotura
│   ├── Material de producción (desperdiciado/dañado)
│   └── Desgaste anormal de la máquina
└── Lucro cesante (producción perdida)
```

---

### Bloque I — Transferencia tecnológica y gestión

- **3ª generación:** gerentes de negocios deciden qué investigar; la tecnología fluye de centros productivos → centros de consumo.
- **Planeación tecnológica profunda:** genera posiciones de costos competitivos.
- **Gerente de tecnología:** analiza obsolescencia departamental y obsolescencia de tecnologías en uso. No hace análisis técnico de productos ni organiza mantenimiento.
- **Paquete tecnológico (def. Abud):** contiene información económico-financiera de la tecnología a adoptar.

---

### Bloque J — Propiedad intelectual

| Tipo | Duración | Renovable |
|---|---|---|
| **Patente** | 20 años desde la presentación | No |
| **Derecho de autor** | Vida del autor + 50 años | — |

La patente puede ser vendida, licenciada o explotada directamente por el titular.

---

### Bloque K — Metodología académica

**Plan de tesis:** definición del problema + confección del bosquejo + elaboración de la agenda.

**Citas:** directas (textuales) / primaria (fuente original indirecta) / indirectas (parafraseadas).

**Función de las referencias:** corroborar o respaldar las propias opiniones con evidencia de terceros.

---

## 4. Hoja de repaso rápido

> `[★×2]` = 2 fuentes. `[★×3]` = 3 fuentes — máxima prioridad. `[⚠]` = discrepancia — ver la pregunta completa.

| Código | Respuesta correcta | Concepto clave | Fuentes |
|---|---|---|---|
| **Bloque A** | | | |
| A1 | V — b y c verdaderas, a falsa | Ingeniería = científico + empírico | |
| A2 | b — determinar y juzgar características | Fin de la ResistMat | ★×3 |
| A3 | b — buscar más de una solución y seleccionar | Optimización = múltiples alternativas | |
| A4 | b — hipótesis → math → solución → verificar | Orden de modelado | ★×3 |
| A5 | b — identificar variables + hipótesis | Inicio del modelo matemático | ★×2 |
| A6 | b — es un problema matemático | Viga apoyada: relación F-deflexión | ★×3 |
| A7 | **tensión-alargamiento** (ExA+S1021) / fuerza-alargamiento (ExB) | Ensayo tracción → diagrama σ-ε | ★×3 ⚠ |
| **Bloque B** | | | |
| B1 | c — oscila en el tiempo | Resorte-masa ideal: sin amortiguamiento | ★×2 |
| B2 | II — b y c verdaderas | Amortiguamiento viscoso: F = c·ẋ | ★×3 |
| B3 | b — máquina con movimiento alternativo | Aplicación práctica del modelo | |
| B4 | a — no existen sistemas ideales | Ingeniería real = siempre imperfecta | |
| **Bloque C** | | | |
| C1 | a — baricentro de la sección | Momento flector al baricentro | ★×2 |
| C2 | a — unidad de área | σ = F/A | ★×2 |
| C3 | b — compresión | Fibra superior en viga = comprimida | ★×2 |
| C4 | a — mismo plano | Corte: fuerzas externas coplanares | ★×2 ⚠ |
| **Bloque D** | | | |
| D1 | b — penetración bajo carga determinada | Dureza = superficial, por indentación | ★×2 |
| D2 | b — deformación elástica | Resiliencia ≠ tenacidad | ★×2 |
| D3 | a — energía total hasta la rotura | Tenacidad ≠ resiliencia | ★×2 |
| D4 | a — relación altura/sección es fundamental | Pandeo = esbeltez | ★×2 |
| D5 | b — cargas cíclicas | Fatiga | ★×2 |
| D6 | c — cambios bruscos de sección | Concentración de tensiones | ★×2 |
| **Bloque E** | | | |
| E1 | c — menor al 2% de C | Acero < 2% C | ★×2 |
| E2 | a — mayor al 2% de C | Fundición: 2–4% C | ★×2 |
| E3 | a — acero al carbono, 0,45% C | SAE 1045 | ★×2 |
| E4 | a — gran dureza y resistencia al desgaste | Cerámicos | ★×2 |
| E5 | b — Cu-Zn | Latón (no confundir con bronce) | ★×2 |
| E6 | a — Cu-Sn | Bronce (no confundir con latón) | ★×2 |
| **Bloque F** | | | |
| F1 | b — atmósfera rica en carbono | Cementación = C | ★×2 |
| F2 | b — dureza superficial + tenacidad núcleo | Temple | ★×2 ⚠ |
| F3 | b — ninguna es correcta | Cianuración = baño de cianuro | ★×2 ⚠ |
| F4 | a — eliminar tensiones internas | Recocido | ★×2 |
| **Bloque G** | | | |
| G1 | b — programación y control de fabricación | Ing. producción | ★×2 |
| G2 | c — planificación de procesos de fabricación | Ing. manufactura | ★×2 |
| G3 | b — conjuntamente con el proyecto técnico | Análisis econ. integrado | ★×2 |
| G4 | c — control sistemático del sistema de medición | Ing. de procesos (def. Abud) | |
| G5 | b — bajo costo | Intercambiabilidad → reemplazo económico | |
| G6 | III — b y c verdaderas | Tolerancias + calibradores límites | |
| **Bloque H** | | | |
| H1 | c — medios físicos en procesos industriales | Definición de mantenimiento | |
| H2 | e — a, b y c son verdaderas | Mantenimiento preventivo: todo incluido | |
| H3 | c — rotura, material de producción, desgaste | Costos de falla directa | |
| **Bloque I** | | | |
| I1 | a — centros productivos → consumo | 3ª generación: difusión tecnológica | |
| I2 | b — gerentes de negocios deciden | 3ª generación: mercado orienta I+D | |
| I3 | a — costos competitivos | Planeación tecnológica profunda | |
| I4 | c — obsolescencia del departamento | Gerente de tecnología | |
| I5 | c — obsolescencia de tecnologías actuales | Gerente de tecnología (variante) | |
| I6 | c — información económico-financiera | Paquete tecnológico (def. Abud) | |
| **Bloque J** | | | |
| J1 | c — 20 años, no renovable | Patente | |
| J2 | c — vida del autor + 50 años | Derecho de autor | |
| J3 | b — vendida o utilizada por el inventor | Derechos sobre la patente | |
| **Bloque K** | | | |
| K1 | b — elaboración de la agenda | Plan de tesis | |
| K2 | b — corroborar/respaldar opiniones propias | Para qué sirve la referencia | ⚠ sin confirmar |
| K3 | c — directas, primaria e indirectas | Tipos de citas | |

---

*Fuentes: apuntes clases 1–11 · Examen A (modelo anterior Abud) · Examen B (segundo modelo Abud) · S1021 (tercer modelo Abud).*
