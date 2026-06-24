# Preparación Parcial 1 — Ingeniería Mecánica I

**Profesor:** Abud  
**Fecha del examen:** jueves 2 de julio de 2026  
**Modalidad:** Multiple choice — las respuestas incorrectas restan puntos  
**Estado de este documento:** Respuestas confirmadas contra el modelo oficial. 28/30 coinciden; P14 y P15 tienen discrepancia conceptual documentada (ver cada pregunta).

---

## 1. Estrategia para el examen

### Regla del juego: incorrectas restan

El examen es multiple choice con penalidad. El mecanismo es:

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

Con esa fórmula, adivinar al azar entre **todas** las opciones da esperanza matemática = 0 (no gana ni pierde). El secreto está en **eliminar opciones**.

### Regla de oro: la eliminación es tu herramienta principal

```
¿Podés eliminar al menos 1 opción?  →  SÍ → respondé (esperanza positiva)
                                     →  NO → dejá en blanco (esperanza neutra)
```

Ejemplo con 3 opciones y penalidad −0,5:
- Adivinás al azar (1/3 chance): E = 1/3 × 1 + 2/3 × (−0,5) = 0     → neutro
- Eliminaste 1, elegís entre 2 (1/2 chance): E = 1/2 × 1 + 1/2 × (−0,5) = +0,25 → conveniente
- Sabés la respuesta (certeza): E = +1                                → siempre respondé

### Estadísticas de aprobación

El examen tiene **30 preguntas** de 1 punto cada una. La nota final se convierte a la escala 1–10:

```
Nota = puntaje_bruto × (10 / 30)
```

Para aprobar con 6 (sobre 10):
```
puntaje_bruto ≥ 6 × (30/10) = 18 puntos
```

**Escenarios de aprobación con penalidad −0,5 por error (preguntas de 3 opciones):**

| Correctas | Incorrectas | No respondidas | Puntaje bruto | Nota (/10) | ¿Aprueba? |
|---|---|---|---|---|---|
| 30 | 0 | 0 | 30,0 | 10,0 | ✓ |
| 24 | 0 | 6 | 24,0 | 8,0 | ✓ |
| 20 | 4 | 6 | 18,0 | 6,0 | justo |
| 18 | 0 | 12 | 18,0 | 6,0 | justo |
| 18 | 1 | 11 | 17,5 | 5,8 | ✗ |
| 15 | 6 | 9 | 12,0 | 4,0 | ✗ |
| 20 | 8 | 2 | 16,0 | 5,3 | ✗ |

**Conclusión práctica:** si respondés todas las que sabés con certeza (digamos ~20) y las demás en blanco, llegás cómodo. No vale la pena arriesgar las últimas si no tenés ni 50% de confianza en la opción.

---

> **ADVERTENCIA — incertidumbre sobre el sistema de penalidades de Abud:**
>
> Todo el análisis anterior asume que **no responder = 0 puntos** y que la penalidad depende de la cantidad de opciones. Ambas cosas son convenciones estándar, pero **no están confirmadas para este examen**.
>
> Dos incógnitas reales:
>
> 1. **¿Las preguntas sin responder restan?** En algunos sistemas (especialmente con Abud), dejar en blanco puede equivaler a responder incorrectamente. Si ese fuera el caso, la estrategia de "dejar en blanco si no sé" se invalida completamente — y convendría siempre marcar algo.
>
> 2. **¿Cuál es la penalidad exacta por error?** El sistema propuesto arriba (`P = 1 / (opciones − 1)`) es el más común en Argentina y tiene base matemática sólida (hace que adivinar sea neutral en esperanza). Pero Abud podría usar una penalidad fija (ej. −1 para toda pregunta incorrecta, independientemente de las opciones), o una fracción diferente.
>
> **Recomendación ante la incertidumbre:** antes de empezar el examen, **preguntarle explícitamente a Abud** cuánto resta una incorrecta y si el blanco puntúa 0 o negativo. Es una pregunta completamente legítima y esa información cambia la estrategia óptima de manera significativa.

---

### Checklist antes de enviar

- [ ] Releé el enunciado completo antes de marcar — muchas trampas están en "NO", "SOLO", "NUNCA"
- [ ] Para preguntas de tratamientos térmicos: distinguí cementación (C) / nitruración (N) / cianuración (C+N) / temple (rapidez) / recocido (lentitud)
- [ ] Para preguntas de aleaciones: latón = Cu+Zn, bronce = Cu+Sn — fácil de invertir bajo presión
- [ ] Para preguntas de % C: acero < 2%, fundición 2–4% — el límite 2% es el más preguntado
- [ ] Para SAE: los dos últimos dígitos son el % de C en centésimas (1045 → 0,45% C)

---

## 2. Preguntas del modelo de examen

> **ADVERTENCIA:** Las respuestas marcadas a continuación son una **primera revisión** hecha con criterio teórico. Deben ser confirmadas. Las preguntas con ⚠ tienen alguna ambigüedad o requieren confirmación especial.

---

### P1 — La dureza de un material se define por:

- ( ) La penetración superficial de una bolilla en una atmósfera rica en carbono.
- **(✓) La penetración de una bolilla sobre la superficie del material, bajo una carga determinada.**
- ( ) La penetración de una bolilla en una superficie debido a una alta temperatura.

> La dureza se mide siempre en superficie. Los ensayos Brinell, Rockwell y Vickers consisten en presionar un indentador (bolilla o cono) bajo una carga conocida y medir la huella. La opción a describe la cementación (tratamiento termoquímico, no dureza). La c es incorrecta porque la temperatura no define la dureza sino que la altera.

---

### P2 — En una estructura simple (viga apoyada) con carga en el centro: ⚠

- ( ) La curva de deflexión es una constante que no depende de las dimensiones de la estructura.
- ( ) No hay relación entre la fuerza y la curva de deflexión.
- **(✓) La relación entre la fuerza y la curva de deflexión es un problema matemático.**

> Por eliminación: a es falsa (la deflexión sí depende de dimensiones, material, forma de sección — clase 2). b es falsa (hay relación directa). c es la única correcta, aunque la redacción sea vaga: lo que afirma es que la relación sí existe y tiene forma matemática (δ = F·L³ / 48·E·I para viga biapoyada con carga central). ⚠ Confirmar con Abud si hay una opción más precisa en el examen real.

---

### P3 — Los materiales cerámicos (arcillas y derivados), sus propiedades tecnológicas son:

- **(✓) Gran dureza y una alta resistencia al rozamiento y desgaste.**
- ( ) Gran dureza y baja resistencia a la corrosión.
- ( ) Alta dureza, pero soportan temperaturas no muy elevadas.

> Los cerámicos son muy duros y resistentes al desgaste (por eso se usan en herramientas de corte, frenos, refractarios). También tienen alta resistencia a la corrosión y soportan temperaturas muy elevadas — por eso b y c son falsas.

---

### P4 — Una fundición de Hierro es:

- **(✓) Una aleación Fe-C con un contenido mayor al 2% de C.**
- ( ) Una aleación Fe-C con un contenido mayor al 1,5% y menor al 2% de C.
- ( ) Una aleación Fe-C con un contenido mayor al 4% de C.

> El diagrama Fe-C establece el límite en 2% C: por debajo es acero, por encima es fundición (hasta ~4%). La opción c es incorrecta porque, si bien existen fundiciones con >4% C, el límite definitorio de "fundición" es >2%, no >4%.

---

### P5 — El acero es:

- ( ) a. Una aleación Fe-C con un contenido menor al 3% de C.
- ( ) b. Una aleación Fe-C con cualquier % de C.
- **(✓) c. Una aleación Fe-C con un contenido menor al 2% de C.**
- ( ) d. Una aleación Fe-C con un contenido menor al 4% de C.

> El límite 2% de carbono es la frontera técnica entre acero y fundición en el diagrama Fe-C. Es el dato más preguntado de toda la materia — memorizarlo es obligatorio.

---

### P6 — SAE 1045:

- **(✓) Un acero al carbono con un 0,45% de C.**
- ( ) Un acero al Cr-Ni con un 0,45% de C.
- ( ) Un acero con un contenido de 4,5% de C.

> Sistema SAE de 4 dígitos: primer dígito = tipo de aleación (1 = acero al carbono), segundo dígito = subgrupo o aleante secundario (0 = sin aleante adicional), últimos dos dígitos = % de C en centésimas (45 → 0,45%). Cr-Ni correspondería a la serie 3XXX.

---

### P7 — La resistencia de materiales tiene como fin:

- **(✓) Determinar y juzgar las características del sólido y su aplicación práctica.**
- ( ) Elaborar métodos de cálculo exactos, complejos y voluminosos.
- ( ) No considerar el fenómeno de los resultados prácticos.

> La resistencia de materiales es una disciplina aplicada: busca evaluar el comportamiento de un sólido bajo cargas para decidir si es apto para su uso. Las opciones b y c describen lo opuesto a eso.

---

### P8 — El momento flector resulta de reducir la resultante de las fuerzas que actúan a la izquierda de la sección considerada al:

- **(✓) Baricentro de la sección.**
- ( ) Al cuadrado de la distancia al baricentro de la misma.
- ( ) A una distancia determinada del eje neutro.
- ( ) A un eje paralelo al eje neutro.

> El momento flector M se calcula respecto al baricentro (centroide) de la sección, que coincide con el eje neutro en secciones simétricas. Reducir al cuadrado (b) no tiene sentido dimensional; "a una distancia determinada" (c) es vago; "eje paralelo al eje neutro" (d) confunde con el teorema de Steiner.

---

### P9 — La cementación se logra:

- ( ) Calentando el acero en una atmósfera rica en cemento.
- **(✓) Calentando el acero en una atmósfera rica en carbono.**
- ( ) Calentando el acero en una atmósfera rica en nitrógeno.
- ( ) Calentando el acero en una atmósfera rica en silicio.

> Cementación = carburización = introducir carbono en la superficie del acero calentándolo en atmósfera carbonífera. La opción c describe la nitruración. La a es un distractor con "cemento" (no tiene nada que ver).

---

### P10 — El temple se realiza para: ⚠

- ( ) Eliminar tensiones internas.
- **(✓) Obtener una dureza superficial y una alta tenacidad en el núcleo.**
- ( ) Obtener una dureza en el núcleo y una superficie dúctil.
- ( ) Ninguna es correcta.

> El temple (enfriamiento rápido desde la zona de austenita) produce martensita en la superficie, que es muy dura. En piezas de espesor considerable, el núcleo se enfría más lento y puede retener mayor tenacidad. La a describe el recocido. La c invierte superficie y núcleo. ⚠ Confirmar: si Abud enseñó que el temple produce dureza uniforme en toda la pieza, la respuesta podría ser d (ninguna).

---

### P11 — El latón es una aleación:

- ( ) Cu - Sn
- **(✓) Cu - Zn**
- ( ) Cu - Ni
- ( ) Cu - Al

> Latón = cobre + zinc. Bronce = cobre + estaño. Cuproníquel = Cu + Ni. Este par latón/bronce es el más confundible del examen — estudiar juntos y memorizarlos en pareja.

---

### P12 — En la ingeniería de proyectos, el análisis económico financiero:

- ( ) Se realiza en una etapa final del proyecto.
- **(✓) Se realiza conjuntamente con el proyecto técnico funcional y de fabricación.**
- ( ) No guarda relación alguna con los proyectos técnico funcional y de fabricación.

> El análisis económico es transversal al proyecto: condiciona decisiones de diseño, materiales y fabricación desde el inicio. No se puede hacer al final porque cambiar una decisión de diseño tardía es muy costoso.

---

### P13 — La ingeniería de producción se dedica a:

- ( ) Mantenimiento de las máquinas afectadas a producción.
- **(✓) Programación y control de los procesos de fabricación.**
- ( ) Programación de los procesos industriales.

> Ingeniería de producción = planificar, programar y controlar cómo se fabrican las piezas. El mantenimiento de máquinas corresponde a ingeniería de mantenimiento. La opción c es más vaga que b y omite el control.

---

### P14 — En una pieza sometida al corte, las fuerzas actuantes:

- **(✓ EXAMEN) Están contenidas en el mismo plano.**
- ( ) Están contenidas en planos perpendiculares.
- ( ) ~~Están contenidas en diferentes planos paralelos.~~ ← marcada inicialmente, **incorrecta según el examen**

> **Respuesta del examen: a (mismo plano).**
>
> **Discrepancia conceptual — leer con atención:**
>
> La respuesta del examen es "mismo plano", pero la definición física del corte (cizalla) es debatible. Hay dos interpretaciones posibles:
>
> - **Interpretación de Abud (examen):** En una pieza "sometida al corte" en el sentido de *falla por corte* (como un bulón cortado por dos chapas), las fuerzas externas que producen el corte son coplanares — actúan en el mismo plano. El corte ocurre *en* esa sección compartida.
>
> - **Interpretación física alternativa:** El esfuerzo cortante interno se genera cuando fuerzas actúan en planos paralelos muy próximos (como en una guillotina: hoja superior e inferior en planos distintos pero cercanos). Desde este punto de vista, "planos paralelos" describe mejor el mecanismo.
>
> **Para el examen de Abud: marcar "mismo plano".** La distinción entre ambas interpretaciones es sutil y depende de si la pregunta apunta a las fuerzas *externas* (mismo plano) o al mecanismo *interno* de la falla (planos paralelos). Abud elige la primera lectura.

---

### P15 — Sistema resorte-masa con amortiguamiento viscoso:

- ( ) a. Las fuerzas de amortiguamiento no dependen de la velocidad instantánea.
- ( ) b. Las fuerzas de amortiguamiento son proporcionales a la velocidad instantánea. ← parcialmente correcta, pero no la respuesta
- ( ) c. Las fuerzas de amortiguamiento dependen de las constantes del resorte y del medio.
- ( ) d. a y c son verdaderas.
- **(✓ EXAMEN) e. b y c son verdaderas.**
- ( ) f. a, b y c son falsas.

> **Respuesta del examen: e (b y c verdaderas).**
>
> **Discrepancia conceptual — leer con atención:**
>
> La opción b es inequívocamente correcta: `F_d = c · ẋ` (amortiguamiento viscoso = proporcional a la velocidad). Hasta ahí no hay discusión.
>
> La controversia está en la opción c: *"Las fuerzas de amortiguamiento dependen de las constantes del resorte y del medio."*
>
> - **Interpretación de Abud (examen):** c es verdadera. Abud lee "constantes del medio" como el coeficiente de amortiguamiento `c` (que efectivamente depende de las propiedades del medio viscoso — aceite, agua, aire), y "constantes del resorte" en sentido amplio como "las constantes del sistema mecánico". En ese marco, c agrega información válida: el amortiguamiento sí depende de propiedades del medio.
>
> - **Interpretación estricta:** c es incorrecta porque mezcla "resorte" con "medio". La fuerza de amortiguamiento viscoso es `F_d = c · ẋ` — depende únicamente del coeficiente de amortiguamiento `c` (propiedad del fluido/medio) y de la velocidad `ẋ`. **No depende de `k` (rigidez del resorte)** en absoluto. Incluir "constantes del resorte" en la opción c la hace técnicamente falsa.
>
> **Para el examen de Abud: marcar e (b y c).** Abud valida la c bajo su lectura de "constantes del sistema/medio". En un examen suyo, la lógica que importa es la suya.

---

### P16 — El proceso de modelado para resolución de un problema en ingeniería, en orden correcto:

- ( ) Formulaciones matemáticas → hipótesis → comprobar predicciones → obtener soluciones.
- ( ) Hipótesis → comprobar predicciones → formulaciones matemáticas → obtener soluciones.
- **(✓) Hipótesis → formulaciones matemáticas → obtener soluciones → comprobar las predicciones con hechos conocidos.**

> Secuencia de Abud (clase 1): (1) identificar variables y establecer hipótesis, (2) plantear el modelo matemático, (3) resolver, (4) verificar contra la realidad. La verificación siempre va al final — es el paso que valida si el modelo es útil.

---

### P17 — La resiliencia es una característica cuya energía absorbida se produce por:

- ( ) Calentamiento.
- **(✓) Deformación elástica.**
- ( ) Deformación plástica.

> Resiliencia = energía almacenada en la zona **elástica** del diagrama tensión-deformación (lo que el material puede devolver al soltar la carga). Tenacidad = energía total (elástica + plástica, hasta la rotura). La deformación plástica es la que caracteriza la tenacidad, no la resiliencia.

---

### P18 — El bronce es:

- **(✓) Una aleación Cu-Sn.**
- ( ) Una aleación Cu-Mn.
- ( ) Una aleación Cu-Zn.

> Bronce = cobre + estaño (Sn). Recordar como par con la P11: latón (Zn) vs. bronce (Sn). Cu-Mn no es una aleación estándar de uso común.

---

### P19 — La concentración de tensiones en una pieza sometida a esfuerzos se debe a:

- ( ) Secciones rectangulares solamente.
- ( ) Cambios suaves de una sección a otra.
- **(✓) Cambios bruscos de sección.**

> La concentración de tensiones ocurre donde la geometría cambia abruptamente (ranuras, taladros, filetes sin radio de curvatura, escalones bruscos). Los cambios suaves de sección la reducen — de hecho, los redondeos de filetes existen precisamente para evitarla. Las secciones rectangulares por sí solas no la causan.

---

### P20 — En una barra biapoyada con carga central perpendicular al eje neutro, la mitad superior (desde el eje neutro hacia arriba) está sometida a:

- **(✓) Compresión.**
- ( ) Tracción.
- ( ) Torsión.

> Viga biapoyada con carga vertical hacia abajo en el centro: la fibra superior se acorta (compresión), la fibra inferior se alarga (tracción). El eje neutro es la línea sin deformación. La torsión no aparece en este esquema.

---

### P21 — La tenacidad es:

- **(✓) La energía de deformación total absorbida debido a la acción de una carga.**
- ( ) La energía de deformación plástica.
- ( ) La energía absorbida durante la deformación elástica.

> Tenacidad = área total bajo la curva tensión-deformación (elástica + plástica, hasta la rotura). La opción b omite la parte elástica. La opción c es la definición de resiliencia, no de tenacidad.

---

### P22 — La formulación del modelo matemático de un sistema se inicia con:

- ( ) I) Identificación de **algunas** variables. II) Determinación de las variables restantes por hipótesis.
- **(✓) I) Identificación de las variables que ocasionan el cambio del sistema. II) Se establecen un conjunto de hipótesis.**
- ( ) Solo la aplicación de leyes empíricas que contienen algunas de las variables.

> La clave es la diferencia entre a y b: la a dice "algunas variables" (incompleto), la b dice "las variables que ocasionan el cambio" (correcto — se identifican todas las variables relevantes y luego se establecen hipótesis para simplificar).

---

### P23 — La ingeniería de manufactura se dedica a:

- ( ) Mantenimiento de todas las maquinarias de planta.
- ( ) Proyecto y desarrollo de la producción.
- **(✓) Planificación de los procesos de fabricación.**

> Manufactura = fabricar. La ingeniería de manufactura planifica cómo se fabrica cada pieza: secuencia de operaciones, máquinas, herramientas, tiempos. El mantenimiento es otra especialidad. "Proyecto y desarrollo de la producción" describe más bien la ingeniería de producción.

---

### P24 — Una Tensión es una fuerza interna por:

- **(✓) Unidad de área.**
- ( ) Unidad de longitud.
- ( ) Unidad de volumen.
- ( ) Ninguna es correcta.

> Definición directa: `σ = F / A` [N/m² = Pa]. La presión también es fuerza por unidad de área, pero en resistencia de materiales hablamos de tensión (normal o tangencial). Nunca longitud ni volumen.

---

### P25 — El pandeo es un fenómeno de pérdida de la estabilidad, por lo tanto:

- **(✓) La relación entre la altura y la sección es fundamental.**
- ( ) La relación entre la altura y su distancia al cuadrado de su baricentro debe ser proporcional.
- ( ) La relación entre la altura y la sección no es importante.

> El pandeo depende de la **esbeltez** de la columna: a mayor relación altura/sección, más susceptible al pandeo. La fórmula de Euler relaciona la carga crítica con L², E e I (momento de inercia de la sección). La sección es fundamental — la opción c es directamente falsa.

---

### P26 — El propósito principal de los ensayos de tracción y compresión consiste en:

- ( ) Construir un diagrama que relaciona el alargamiento y la temperatura.
- ( ) Determinar la relación existente entre la fuerza y el tiempo de rotura.
- **(✓) Determinar la dependencia entre la tensión y su alargamiento.**

> El ensayo de tracción produce el **diagrama tensión-deformación (σ-ε)**, que muestra la relación entre tensión aplicada y alargamiento proporcional. De ese diagrama se extraen E, límite elástico, resistencia a la rotura, ductilidad.

---

### P27 — El fenómeno de fatiga de materiales se produce por:

- ( ) Cargas constantes y temperaturas bajo cero.
- **(✓) Cargas cíclicas.**
- ( ) Temperaturas muy extremas.

> Fatiga = falla por acumulación de daño bajo cargas **repetidas/cíclicas**, incluso si cada ciclo está por debajo del límite elástico. El eje de tren es el ejemplo clásico (clase 9): rota indefinidamente, la fibra superior e inferior alternan entre compresión y tracción con cada vuelta.

---

### P28 — La cianuración se logra: ⚠

- ( ) Calentando el acero en una atmósfera rica en azufre.
- **(✓) Ninguna es correcta.**
- ( ) Calentando el acero en una atmósfera rica en nitrógeno.
- ( ) Calentando el acero en una atmósfera rica en carburo de hierro.

> La cianuración (cyaniding) se realiza sumergiendo el acero en un **baño de sales de cianuro fundido** (no en "atmósfera") a alta temperatura. Introduce simultáneamente C y N en la superficie. Ninguna de las otras opciones describe esto: azufre (a) no tiene relación; nitrógeno (c) describe la nitruración; carburo de hierro (d) es incorrecto. ⚠ Confirmar — depende de cómo lo explicó Abud en clase.

---

### P29 — El recocido se utiliza para:

- **(✓) Eliminar tensiones internas.**
- ( ) Darle una dureza superficial.
- ( ) Conferirle una dureza en toda la estructura.

> El recocido (annealing) = enfriamiento muy lento desde la zona de austenita. Produce ferrita + perlita: estructura blanda y dúctil. Su propósito es **aliviar tensiones residuales** (de soldadura, mecanizado, conformado). La dureza superficial corresponde al temple superficial; la dureza en toda la estructura, al temple convencional.

---

### P30 — El sistema resorte-masa en condiciones ideales es:

- ( ) Un sistema cuya posición no depende del tiempo una vez apartado del equilibrio.
- ( ) Un sistema que al ser apartado del equilibrio vuelve a su condición inicial al cabo de un tiempo.
- **(✓) Un sistema que oscila en el tiempo una vez apartado de su posición de equilibrio.**

> En condiciones ideales (sin amortiguamiento), el sistema resorte-masa oscila indefinidamente con frecuencia natural `ω_n = √(k/m)`. No vuelve a su posición inicial (eso requeriría amortiguamiento) ni su posición es independiente del tiempo (eso sería equilibrio estático permanente).

---

## 3. Resumen de temas por bloque

### Bloque A — Ingeniería, modelos y sistemas

**La ingeniería vs. la ciencia pura:**  
La ciencia describe la realidad; la ingeniería la transforma. La ingeniería usa la ciencia como base pero está sujeta a restricciones de costo, normas y fabricabilidad.

**Proceso de modelado matemático (3 pasos):**

```
1. Identificar variables que ocasionan el cambio
        ↓
2. Establecer hipótesis (incluye leyes empíricas aplicables)
        ↓
3. Formular el modelo matemático
        ↓
4. Obtener soluciones
        ↓
5. Comprobar predicciones con hechos conocidos (validación)
```

**Sistema resorte-masa:**
- Parámetros fijos: masa `m`, rigidez `k`, amortiguamiento `c`
- Variables dinámicas: posición `x(t)`, velocidad `ẋ(t)`, aceleración `ẍ(t)`
- Sin amortiguamiento (ideal): oscila indefinidamente con `ω_n = √(k/m)`
- Con amortiguamiento viscoso: `F_d = c · ẋ` (proporcional a la velocidad)

---

### Bloque B — Estructuras simples y solicitaciones

**Viga biapoyada con carga central:**
- La deflexión depende de: forma de sección, módulo E, punto de aplicación, tipo de apoyo
- `δ_max = F·L³ / (48·E·I)` (fórmula de referencia — no es el foco del parcial, sí el concepto)

**Los cuatro esfuerzos característicos:**

| Esfuerzo | Símbolo | Qué produce | Tensión generada |
|---|---|---|---|
| Axial (normal) | N | Tracción o compresión uniforme en la sección | σ = N/A |
| Cortante | Q | Cizalladura — fuerzas en planos paralelos | τ = Q/A |
| Momento flector | M | Flexión — compresión arriba, tracción abajo | σ = M·y / I |
| Momento torsor | T | Torsión — giro de la sección | τ = G·ρ·θ |

**Tensión — definición:**  
`σ = F / A` [Pa = N/m²]. Es una fuerza interna por unidad de área. El material "siente" la tensión en cada punto, no la fuerza total.

**Flexión pura — distribución de tensiones:**
```
  ─────────── fibra superior: COMPRESIÓN (−σ)
  ─── ─── ─── eje neutro: σ = 0
  ─────────── fibra inferior: TRACCIÓN (+σ)
```
Para una viga biapoyada con carga vertical hacia abajo.

**Momento flector M:** se calcula reduciendo la resultante de fuerzas al **baricentro** de la sección. `I` (momento de inercia de sección) mide cómo está distribuida el área respecto al eje neutro — unidades: mm⁴ o cm⁴.

---

### Bloque C — Fenómenos de falla

**Pandeo:**  
Pérdida de **estabilidad** (no de resistencia). Una columna falla por pandeo antes de alcanzar el límite elástico. La relación altura/sección (esbeltez) es el parámetro crítico — columnas más altas y delgadas pandean antes. `P_cr = π²·E·I / L²` (Euler).

**Fatiga:**  
Falla por cargas **cíclicas** repetidas, aunque cada carga esté debajo del límite elástico. Mecanismo: nucleación y propagación de una microfisura hasta rotura súbita. El eje de ferrocarril es el ejemplo canónico.

**Concentración de tensiones:**  
En zonas de cambio **brusco** de sección (ranuras, taladros, escalones), las tensiones locales se amplifican respecto al valor nominal. Los redondeos de filetes existen para suavizar ese cambio y reducir la concentración.

**Ensayos de tracción y compresión:**  
Producen el diagrama `σ-ε` (tensión vs. deformación), del que se extraen:
- Módulo de elasticidad E (pendiente zona elástica)
- Límite elástico (punto donde deja de ser lineal)
- Resistencia a la rotura
- Ductilidad (alargamiento hasta fractura)

---

### Bloque D — Propiedades y clasificación de materiales

**Propiedades mecánicas clave — diferencias cruciales:**

| Propiedad | Definición | Energía involucrada |
|---|---|---|
| **Resiliencia** | Capacidad de absorber energía en zona **elástica** y devolverla | Solo zona elástica |
| **Tenacidad** | Energía total absorbida **hasta la rotura** (zona elástica + plástica) | Total |
| **Dureza** | Resistencia a la **penetración superficial** | — |
| **Ductilidad** | Capacidad de deformarse sin romperse | — |
| **Maleabilidad** | Capacidad de extenderse en láminas | — |
| **Plasticidad** | Deformación permanente al superar el límite elástico | — |

**Metales ferrosos — clasificación por % de carbono:**

```
  % C
  ────────────────────────────────────────────────
  0,05          2%                   4%
  │─────────────│────────────────────│
  Acero         │                    Fundición
  (dúctil,      │                    (dura, frágil,
  soldable)     │                    no soldable)
                └── límite Fe-C más preguntado
```

| Material | % de C | Características |
|---|---|---|
| Hierro forjado | < 0,05% | Casi hierro puro, maleable |
| Acero | 0,05 – 2% | Dúctil, soldable, se oxida |
| Fundición | 2 – 4% | Dura, frágil, no soldable |

**Aceros al carbono por contenido:**
- Bajo carbono (< 0,25% C): estructuras, chapas, soldadura
- Medio carbono (0,25–0,55% C): ejes, engranajes, resortes
- Alto carbono (> 0,55% C): herramientas, rieles, rodamientos

**Clasificación SAE — 4 dígitos:**

```
  SAE  X  X  X  X
       │  │  └──┘
       │  │   └── % de C en centésimas
       │  └─── aleante secundario
       └─── tipo de aleante principal
              1 = carbono puro
              2 = níquel
              3 = cromo-níquel
              4 = molibdeno
              5 = cromo
              6 = cromo-vanadio
```

Ejemplos clave: SAE 1045 = acero al carbono con 0,45% C. SAE 4140 = acero Cr-Mo con 0,40% C.

**Metales no ferrosos — aleaciones importantes:**

| Aleación | Componentes | Mnemotecnia |
|---|---|---|
| Latón | Cu + Zn | **La**tón → **Za**patos (Zn) |
| Bronce | Cu + Sn | **Br**once → e**St**año (Sn) |
| Cuproníquel | Cu + Ni | Cu + Ni (directo) |

---

### Bloque E — Tratamientos térmicos y termoquímicos

**Tratamientos térmicos** (solo calor, sin cambiar composición química):

| Tratamiento | Velocidad de enfriamiento | Microestructura | Propiedades | Para qué sirve |
|---|---|---|---|---|
| **Recocido** | Muy lento (en horno) | Ferrita + perlita | Blando, dúctil | Eliminar tensiones internas |
| **Normalizado** | Moderado (aire) | Perlita fina | Resistencia media | Homogeneizar estructura |
| **Temple** | Rápido (agua/aceite) | Martensita | Muy duro, muy frágil | Aumentar dureza |
| **Revenido** | — (calentamiento suave tras temple) | Martensita revenida | Duro + menos frágil | Reducir fragilidad del temple |

**Tratamientos termoquímicos** (calor + difusión de elementos en la superficie):

| Tratamiento | Elemento difundido | Cómo se logra | Efecto |
|---|---|---|---|
| **Cementación** | Carbono (C) | Atmósfera rica en C | Dureza superficial + núcleo tenaz |
| **Nitruración** | Nitrógeno (N) | Atmósfera de amoníaco (N₂) | Dureza superficial muy alta, sin fragilidad |
| **Cianuración** | C + N simultáneos | Baño de sales de cianuro fundido | Dureza superficial + resistencia al desgaste |

> Regla mnemotécnica: **Ce**mentación → **C**arbono. **Ni**truración → **Ni**trógeno. **Ci**anuración → **C**+N (cianuro tiene C y N).

---

### Bloque F — Ingenierías especializadas

| Especialidad | Función principal |
|---|---|
| **Ingeniería de manufactura** | Planificación de los procesos de fabricación de piezas |
| **Ingeniería de producción** | Programación y control de los procesos de fabricación |
| **Ingeniería de mantenimiento** | Mantenimiento de las máquinas de planta |
| **Ingeniería de proyectos** | Análisis técnico + económico-financiero integrado (no al final) |

---

## 4. Resumen de respuestas (hoja de repaso rápido)

> Confirmadas contra el modelo oficial. ⚠ = respuesta del examen difiere de la interpretación física estricta — ver la pregunta completa para el razonamiento.

| # | Respuesta correcta | Concepto clave |
|---|---|---|
| 1 | b — penetración de bolilla bajo carga | Dureza = superficial, por indentación |
| 2 ⚠ | c — es un problema matemático | Por eliminación |
| 3 | a — gran dureza y resistencia al desgaste | Cerámicos: duros, resistentes |
| 4 | a — mayor al 2% de C | Fundición: 2–4% C |
| 5 | c — menor al 2% de C | Acero: < 2% C |
| 6 | a — acero al carbono, 0,45% C | SAE 1045 |
| 7 | a — determinar características y aplicación | Fin de la ResistMat |
| 8 | a — baricentro de la sección | Momento flector al baricentro |
| 9 | b — atmósfera rica en carbono | Cementación = C |
| 10 ⚠ | b — dureza superficial + tenacidad en núcleo | Temple |
| 11 | b — Cu-Zn | Latón (no confundir con bronce) |
| 12 | b — conjuntamente con el proyecto técnico | Análisis econ. integrado |
| 13 | b — programación y control de fabricación | Ing. producción |
| 14 ⚠ | **a — mismo plano** (examen) / c — planos paralelos (física estricta) | Ver discrepancia en P14 |
| 15 ⚠ | **e — b y c verdaderas** (examen) / b solo (física estricta) | Ver discrepancia en P15 |
| 16 | c — hipótesis → math → solución → verificar | Orden de modelado |
| 17 | b — deformación elástica | Resiliencia ≠ tenacidad |
| 18 | a — Cu-Sn | Bronce (no confundir con latón) |
| 19 | c — cambios bruscos de sección | Concentración de tensiones |
| 20 | a — compresión | Fibra superior = comprimida |
| 21 | a — energía total hasta la rotura | Tenacidad ≠ resiliencia |
| 22 | b — identificar variables + hipótesis | Inicio del modelo |
| 23 | c — planificación de procesos de fabricación | Ing. manufactura |
| 24 | a — unidad de área | σ = F/A |
| 25 | a — relación altura/sección es fundamental | Pandeo = esbeltez |
| 26 | c — dependencia tensión-alargamiento | Diagrama σ-ε |
| 27 | b — cargas cíclicas | Fatiga |
| 28 ⚠ | b — ninguna es correcta | Cianuración = baño de cianuro |
| 29 | a — eliminar tensiones internas | Recocido |
| 30 | c — oscila en el tiempo | Sistema ideal sin amortiguación |

---

*Fuente: apuntes clases 1–11, `abud.docx`, modelo de examen Abud 2026.*
