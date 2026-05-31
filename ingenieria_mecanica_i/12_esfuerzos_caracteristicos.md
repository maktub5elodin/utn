# Esfuerzos Característicos

## 1. Introducción — El rol del ingeniero ante una estructura

Cuando un ingeniero diseña una viga, un eje, una columna o cualquier elemento estructural, su pregunta central es siempre la misma:

> **¿Soporta? ¿Cumple con el objetivo para el que fue diseñado?**

Para responder esa pregunta, el ingeniero necesita un lenguaje matemático que describa **qué le pasa al material por dentro** cuando se aplican fuerzas por fuera. Ese lenguaje son los **esfuerzos característicos**.

Los esfuerzos característicos son las **fuerzas internas** que aparecen en una sección transversal de un sólido cuando se le aplican cargas externas. Identificarlos y cuantificarlos permite **dimensionar** correctamente la estructura — es decir, elegir geometría y material para que el sólido cumpla su función sin fallar.

Las dos variables que el ingeniero maneja son siempre:

```
  VARIABLE 1: FUERZAS          VARIABLE 2: SECCIÓN
  (qué cargas actúan)          (qué área y forma tiene el elemento)
         │                              │
         └──────────────┬───────────────┘
                        ▼
              TENSIONES INTERNAS
              (¿el material aguanta?)
                        │
                        ▼
              DECISIÓN DE DISEÑO
```

> **Analogía contable:** Así como el balance separa activo del pasivo para describir el estado financiero de una empresa, los esfuerzos característicos separan y clasifican las distintas "cargas internas" que actúan sobre una sección para describir el **estado mecánico** del sólido. El ingeniero cierra ese balance: si los esfuerzos superan la capacidad del material, la "empresa" quiebra.

---

## 2. El sólido de alma llena

### ¿Qué es?

Un **sólido de alma llena** es un cuerpo cuya sección transversal es **maciza** — no tiene huecos, cavidades ni perforaciones internas.

```
  ALMA LLENA (maciza)      ALMA ESBELTA (hueca o aligerada)

  ████████████             ████████████
  ████████████             █          █
  ████████████             █          █
  ████████████             ████████████

  (barra circular sólida,  (tubo, perfil I, perfil U,
   barra rectangular)       perfil L, viga cajón)
```

### ¿Por qué se parte de este caso?

El sólido de alma llena es el punto de partida pedagógico porque:
- Su sección es geométricamente simple → el baricentro es fácil de ubicar
- La distribución de tensiones es continua y sin discontinuidades
- No aparecen fenómenos locales como pandeo de alma o concentración en esquinas

Una vez dominado el alma llena, el análisis se extiende a perfiles abiertos y cerrados (alma esbelta).

---

## 3. Material homogéneo e isótropo

Para construir un modelo matemático manejable del comportamiento del sólido, se asumen dos propiedades ideales del material:

### 3.1 Homogéneo

Un material es **homogéneo** si sus propiedades mecánicas son **iguales en todos los puntos** del cuerpo, sin importar dónde se tome la muestra.

```
  HOMOGÉNEO                    NO HOMOGÉNEO
  (mismas propiedades          (propiedades variables
   en todos los puntos)         de punto a punto)

  · · · · · · · · ·            · ○ · △ · ◇ · · ·
  · · · · · · · · ·            · · △ · · · ○ · ·
  · · · · · · · · ·            · ◇ · · △ · · · ○
  (puntos equivalentes)        (puntos distintos)
```

**Ejemplos:** el acero estructural laminado es una buena aproximación al material homogéneo. El hormigón armado, el aglomerado de madera o los materiales compuestos (CFRP) no lo son.

### 3.2 Isótropo

Un material es **isótropo** si sus propiedades son **iguales en todas las direcciones** — no importa desde qué ángulo se lo cargue, responde igual.

```
  ISÓTROPO                     ANISÓTROPO
  (respuesta igual              (respuesta varía
   en toda dirección)            según la dirección)

       ↑ igual                       ↑ fuerte
    ← · →  igual                  ← · →  débil
       ↓ igual                       ↓ fuerte
```

**Ejemplo anisótropo:** la madera es mucho más resistente a lo largo de la fibra que perpendicularmente. El acero estructural es prácticamente isótropo.

> **Por qué se asumen estas propiedades:** Simplifican el modelo matemático hasta volverlo tratable. Con material homogéneo e isótropo, las ecuaciones que relacionan esfuerzos con deformaciones (ley de Hooke generalizada) se reducen a dos constantes: el módulo de elasticidad E y el coeficiente de Poisson ν. Sin estas hipótesis, el modelo requeriría 21 constantes independientes.

---

## 4. Sistema de fuerzas: activo y reactivo

### 4.1 ¿Qué es un sistema de fuerzas?

Un **sistema de fuerzas** es el conjunto completo de todas las fuerzas que actúan sobre el sólido. Se divide en dos grupos con roles distintos:

```
  ┌─────────────────────────────────────────────────────────┐
  │  SISTEMA DE FUERZAS                                     │
  │                                                         │
  │  Fuerzas ACTIVAS         Fuerzas REACTIVAS              │
  │  (las que "cargan"       (las que los apoyos ejercen    │
  │   el sólido)              para mantenerlo en equilibrio)│
  │                                                         │
  │  Ejemplos:               Ejemplos:                      │
  │  · Peso propio           · Reacción en apoyo simple     │
  │  · Carga de uso          · Reacción en empotramiento    │
  │  · Viento, sismo         · Reacción de empuje           │
  └─────────────────────────────────────────────────────────┘
```

```
         P (activa — hacia abajo)
         ↓
  ───────┼───────────────────────
         │         VIGA
  ───────┴───────────────────────
      RA ↑                   ↑ RB
    (reactiva)            (reactiva)
```

### 4.2 Componente activo y componente reactivo

El mismo vocabulario se aplica también a nivel de una sección: cada fuerza interna puede clasificarse por su **dirección respecto a la sección**:

- **Componente normal** (perpendicular a la sección): genera tracción o compresión
- **Componente tangencial** (paralela a la sección): genera corte o cizallamiento

> **Analogía contable:** Las fuerzas activas son los débitos (lo que entra como carga al sistema); las fuerzas reactivas son los créditos (lo que los apoyos aportan para compensar). La suma siempre debe cerrar en cero — igual que el asiento de partida doble.

---

## 5. Sistema de fuerzas en equilibrio

Un sólido está en **equilibrio estático** cuando no se mueve ni acelera. Esto exige que:

```
  ΣF = 0    (la resultante vectorial de todas las fuerzas es nula)
  ΣM = 0    (la resultante de todos los momentos respecto a cualquier
              punto también es nula)
```

Estas dos condiciones son la base de todo el análisis estructural. El equilibrio se alcanza gracias a la combinación de fuerzas activas (que cargan) y fuerzas reactivas (que equilibran).

> **Importante:** El equilibrio permite calcular las reacciones en los apoyos a partir de las cargas conocidas. Una vez conocidas las reacciones, se puede analizar cualquier sección del sólido aplicando nuevamente el equilibrio a la parte cortada.

---

## 6. El plano de simetría

El **plano de simetría** de un sólido divide al cuerpo en dos mitades que son el reflejo especular exacto una de la otra.

```
            Plano de simetría
                  │
  ────────────────┼────────────────
  ███████████████ │ ███████████████   ← sección simétrica
  ███████████████ │ ███████████████
  ────────────────┼────────────────
                  │
```

El plano de simetría es relevante porque:
1. El baricentro de la sección siempre cae sobre él (o sobre su intersección si hay varios)
2. Si las cargas también son simétricas, el problema se reduce a un análisis 2D
3. En flexión, si la carga actúa en el plano de simetría, no hay torsión

Cuando las fuerzas **no** actúan en el plano de simetría, aparecen efectos de torsión que complican el análisis.

---

## 7. La sección — el concepto central

### 7.1 ¿Qué es una sección?

La **sección** es el corte transversal (perpendicular al eje longitudinal del sólido) que el ingeniero realiza imaginariamente para "abrir" el sólido y ver qué fuerzas internas circulan por su interior.

```
    SÓLIDO COMPLETO                VISTA DE LA SECCIÓN
                                   (superficie de corte)
   ╔═══════════════╗
   ║               ║
   ║  ─ ─ ─ ─ ─ ─ ║  ──►    ┌─────────────┐
   ║   (plano      ║         │             │
   ║    de corte)  ║         │      G      │  ← baricentro
   ║               ║         │             │
   ╚═══════════════╝         └─────────────┘
```

### 7.2 Por qué el concepto de sección es tan central

Toda la mecánica estructural gira en torno a la sección:

- Los esfuerzos característicos (N, Q, M, T) son fuerzas y momentos que actúan **sobre** una sección
- Las tensiones (σ, τ) son intensidades de esas fuerzas calculadas **en** puntos de la sección
- El baricentro es la propiedad geométrica más importante **de** la sección
- El momento de inercia es otra propiedad geométrica **de** la sección
- El eje neutro pasa por la sección en un punto determinado por sus propiedades

El profesor mencionó la sección insistentemente porque es la unidad de análisis fundamental: todo lo que ocurre en el interior de la barra se analiza sección a sección.

---

## 8. Baricentro de la sección vs. Centro de gravedad

Esta distinción es sutil pero importante. El profesor la mencionó explícitamente.

### 8.1 Centro de gravedad (o de masa)

El **centro de gravedad** (CG) es el punto donde se concentra, a efectos de cálculo, **toda la masa** del sólido tridimensional. Es una propiedad del **cuerpo completo** en el espacio 3D. Depende de la distribución de masa a lo largo del volumen.

### 8.2 Baricentro de la sección (centroide)

El **baricentro de la sección** (también llamado centroide o centro geométrico) es el **centro geométrico** de la figura plana que forma la sección transversal. Es una propiedad de una **figura 2D** — del área, no del volumen.

```
  CUERPO 3D                          SECCIÓN TRANSVERSAL (2D)

      Z                                    y
      │                                   │
      │      CG (cuerpo entero)            │
      │       ·                           │    ·──── G (baricentro)
      ├───────────────── Y            ────┼────────────────── z
     /                                   │  (área de corte)
    X                                    │

  Es una propiedad del volumen.       Es una propiedad del área.
```

### 8.3 Tabla comparativa

| Concepto | Dimensión | Se calcula sobre | Depende de |
|----------|-----------|------------------|------------|
| Centro de gravedad (CG) | 3D | Todo el volumen | Distribución de masa en el espacio |
| Baricentro de la sección (G) | 2D | El área del corte | Distribución del área en el plano |

Para un material **homogéneo**, el baricentro de cada sección coincide en proyección con el centro de gravedad del sólido. Pero son propiedades conceptualmente distintas aunque numericamente coincidan.

### 8.4 La línea de baricentros — el eje de la barra

El profesor mencionó que hay **una línea con infinitos baricentros**. Esta es una idea geométrica fundamental:

Si se realizan infinitos cortes transversales a lo largo de una barra, cada sección tiene su propio baricentro. Al unir todos esos puntos, se forma una **línea continua** en el interior del sólido — el **eje baricéntrico** de la barra.

```
  Infinitas secciones a lo largo de la barra:

       G₁       G₂       G₃       G₄       G₅
        ·────────·────────·────────·────────·    ← línea de baricentros
  ┌─────┼────────┼────────┼────────┼────────┼────┐
  │     │        │        │        │        │   │
  │     │        │        │        │        │   │
  └─────┼────────┼────────┼────────┼────────┼────┘
        ·────────·────────·────────·────────·

               EJE BARICÉNTRICO
        (una línea con infinitos baricentros,
         uno por cada sección posible)
```

Esta línea es el **eje de referencia** de todo el análisis de esfuerzos:
- Para una barra **prismática** (sección constante) de material homogéneo, el eje es recto
- En estructuras curvadas o de sección variable, el eje baricéntrico es curvo
- Los esfuerzos de flexión se calculan referenciados a este eje

---

## 9. La norma a la sección y la resultante

Cuando se realiza un corte transversal, se necesita un sistema de referencia local. La **norma** (vector normal) a la sección es el vector **perpendicular a la superficie de corte** — apunta en la dirección del eje longitudinal de la barra.

```
       Norma (n̂) — vector perpendicular a la sección
            ↑
            │
  ──────────┼──────────────────────  eje longitudinal
            │
          SECCIÓN
          (plano de corte)
```

La **resultante** de todas las fuerzas internas en esa sección es la fuerza total equivalente que actúa sobre la superficie de corte. Se puede siempre descomponer en:

- **Componente según n̂** (perpendicular a la sección) → fuerza normal N
- **Componente perpendicular a n̂** (paralela a la sección) → fuerza cortante Q

Y el **momento resultante** en la sección se descompone en:

- **Componente alrededor del eje de la barra** → momento torsor T
- **Componente perpendicular al eje de la barra** → momento flector M

---

## 10. Momento de una fuerza — producto vectorial

El **momento de una fuerza** respecto a un punto es la medida del efecto rotacional que esa fuerza produce alrededor de ese punto. Matemáticamente, es el **producto vectorial** entre el vector posición `r` (del punto de referencia al punto de aplicación de la fuerza) y el vector fuerza `F`:

```
  M = r × F
```

El resultado es un **vector** perpendicular al plano formado por `r` y `F`. Su módulo es:

```
  |M| = |r| · |F| · sen(θ)
```

donde `θ` es el ángulo entre `r` y `F`.

```
              F
              ↑
              │
              │  θ
  ────────────·──────────►
  O           r

  M = r × F   →   vector saliendo del plano (⊙) si la rotación
                   es antihoraria, entrando al plano (⊗) si es horaria
```

> **Intuición de la palanca:** La misma fuerza F produce mayor momento cuando se aplica lejos del punto de giro (r grande) que cuando se aplica cerca (r pequeño). Es el principio de la palanca de Arquímedes.

> **Analogía contable:** El momento es análogo al efecto del apalancamiento financiero. La misma "fuerza" (capital) produce efectos muy distintos según la "distancia" (apalancamiento): a mayor palanca, mayor efecto rotacional — para bien o para mal.

---

## 11. Los esfuerzos característicos fundamentales

Al hacer un corte en cualquier sección de un sólido sometido a cargas externas, aparecen en el caso general **cuatro esfuerzos característicos** (seis en el caso 3D completo, pero el introductorio trabaja con cuatro):

### 11.1 Fuerza normal — N

La **fuerza normal** (N) es la componente de la resultante **perpendicular a la sección** (a lo largo del eje de la barra). Actúa uniformemente sobre toda la sección (hipótesis de Navier para barras prismáticas).

```
  TRACCIÓN (+N)                 COMPRESIÓN (−N)

  ←══════════════►              ►══════════════←

  (el material se estira,       (el material se acorta,
   las fibras se separan)        las fibras se comprimen)
```

- `+N` → tracción: el sólido "quiere" alargarse
- `−N` → compresión: el sólido "quiere" acortarse

### 11.2 Fuerza cortante — Q (esfuerzo de corte)

La **fuerza cortante** (Q) es la componente de la resultante **paralela a la sección** (perpendicular al eje). Tiende a "cortar" o "cizallar" el material a lo largo del plano de corte.

```
         Q →
  ─────────────────────────────
  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─    ← sección: las dos mitades tienden
  ─────────────────────────────     a deslizarse una respecto a la otra
         Q →
```

En un sistema de referencia 2D (viga en plano), hay una componente Q en cada dirección transversal. En el caso introductorio plano se trabaja con una sola.

### 11.3 Momento flector — M (o Mf)

El **momento flector** es el momento que tiende a **doblar** o curvar el sólido. Actúa en el plano de la carga y produce curvatura del eje baricéntrico.

```
  Flexión positiva (convención habitual: suela en tracción):

          ↓ P
  ════════╪════════
  ▓▓▓▓▓▓▓█▓▓▓▓▓▓▓  ← fibras superiores: COMPRESIÓN
          │
          │          (la viga se curva hacia abajo)
  ────────┴────────
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ← fibras inferiores: TRACCIÓN
```

### 11.4 Momento torsor — T (torsión)

El **momento torsor** (T) es el momento que tiende a **torcer** el sólido alrededor de su eje longitudinal. Aparece cuando la resultante de cargas tiene un par giratorio respecto al eje de la barra.

```
  Torsión:

  ←────── eje longitudinal ──────►

    ↙↗  (sección A gira)                  ↗↙  (sección B gira en sentido opuesto)
  ══════                                       ══════
  (las secciones vecinas giran relativamente unas respecto a otras)
```

La torsión aparece frecuentemente combinada con la flexión (flexo-torsión) en elementos como ejes de transmisión, vigas curvas y dinteles de balcones.

### 11.5 Tabla resumen de los esfuerzos fundamentales

| Símbolo | Nombre | Dirección respecto a la sección | Efecto sobre el sólido |
|---------|--------|---------------------------------|------------------------|
| N | Fuerza normal (axial) | Perpendicular — a lo largo del eje | Tracción / compresión axial |
| Q | Fuerza cortante | Paralela — en el plano de la sección | Cizallamiento / corte |
| M | Momento flector | Rotación en el plano de carga | Curvatura — flexión |
| T | Momento torsor | Rotación alrededor del eje de la barra | Torsión |

> **Marco de referencia del ingeniero:** N y Q son los dos esfuerzos "básicos" del marco de referencia local de la sección. M y T son los momentos en ese mismo marco. Conocidos estos cuatro valores en cada sección, el estado interno del sólido queda completamente caracterizado (en el caso 2D introductorio).

---

## 12. Momento flector como par de pares

El profesor describió el momento flector como un **"par de pares"**. Esta imagen tiene una interpretación física precisa.

Un **par** (en estática) es un sistema de dos fuerzas paralelas, iguales en módulo, opuestas en sentido, separadas por una distancia `d`. Un par no tiene resultante neta de fuerza — solo produce un momento.

El momento flector en una sección surge porque internamente hay un sistema de fuerzas que forman exactamente un par:

```
  Vista de la sección en flexión:

  ┌─────────────────────────────┐
  │  ←── Compresión (bloque C)  │  ← zona comprimida (arriba del eje neutro)
  │─────────────────────────────│  ← EJE NEUTRO (tensión = 0)
  │  ──► Tracción    (bloque T) │  ← zona traccionada (abajo del eje neutro)
  └─────────────────────────────┘

             ←── C ──┐
                     │  distancia d
             ──► T ──┘

  M = C · d = T · d     (el par de fuerzas internas genera el momento)
```

La zona comprimida forma un "bloque" de compresión C; la zona traccionada forma un "bloque" de tracción T. Ambos son iguales en módulo (equilibrio de fuerzas axiales), opuestos en sentido, y separados por la distancia entre sus centroides. Ese par es el momento flector.

La expresión "par de pares" refleja que el momento flector es el resultado de la interacción entre dos conjuntos de fuerzas internas distribuidas (las tensiones normales de la zona de compresión y las de la zona de tracción) que, integradas sobre la sección, producen un par resultante.

---

## 13. El eje neutro

### ¿Qué es?

El **eje neutro** es la línea dentro de la sección donde la **tensión normal es exactamente cero** — ni tracción ni compresión. Es la frontera que separa la zona comprimida de la zona traccionada en flexión.

```
  Distribución de tensión normal (σ) a lo largo de la altura de la sección:

         COMPRESIÓN (σ < 0)
  ─────────────────────────────
  ◄── ◄── ◄── ◄── ◄── ◄── ◄──│
  ◄── ◄── ◄── ◄──             │
  ◄── ◄──                     │
  ────────────────── │ ────────── ← EJE NEUTRO (σ = 0)
              ──►              │
        ──► ──► ──►           │
  ──► ──► ──► ──► ──► ──► ──► │
  ─────────────────────────────
         TRACCIÓN (σ > 0)

  (La tensión varía linealmente con la distancia al eje neutro)
```

### Propiedades del eje neutro (bajo hipótesis de Navier)

En la teoría clásica de vigas (material lineal, elástico, homogéneo, isótropo, sección plana que permanece plana):

1. El eje neutro **pasa por el baricentro** de la sección
2. La distribución de tensiones normales es **lineal** respecto a la distancia al eje neutro
3. En el eje neutro, la tensión normal es **siempre cero**
4. La máxima tensión (positiva o negativa) ocurre en la **fibra más alejada** del eje neutro

> El profesor lo llamó **eje neutro teórico** porque estas propiedades derivan de hipótesis ideales. En la práctica, materiales no lineales, secciones fisuradas o cargas fuera del plano de simetría pueden desplazarlo o distorsionarlo.

---

## 14. Tensiones normales y tangenciales

Hay una distinción clave entre **esfuerzo** y **tensión** que se debe comprender bien:

| Término | Símbolo | Definición | Naturaleza |
|---------|---------|------------|------------|
| Esfuerzo | N, Q, M, T | Fuerza o momento interno **total** en la sección | Fuerza [N] o momento [N·m] |
| Tensión | σ, τ | Intensidad de la fuerza interna **por unidad de área** | Presión [Pa = N/m²] |

```
  Esfuerzo → Tensión:

  Fuerza normal N (total)
  ─────────────────────── = σ (tensión normal en cada punto)
  Área de la sección A


  Fuerza cortante Q (total)
  ──────────────────────────  ≈  τ (tensión tangencial media)
  Área de la sección A
```

### 14.1 Tensión normal (σ — sigma)

La **tensión normal** actúa **perpendicularmente** a la superficie de la sección. Surge del esfuerzo normal N y del momento flector M.

- σ > 0 → tracción (el material "quiere" separarse)
- σ < 0 → compresión (el material "quiere" aplastarse)

### 14.2 Tensión tangencial (τ — tau)

La **tensión tangencial** (o de cizalla) actúa **paralelamente** a la superficie de la sección. Surge del esfuerzo cortante Q y del momento torsor T.

```
  Vista de una sección:

       ┌──────────────────────┐
       │  σ ←→   (normal)    │  ← tensiones perpendiculares al plano
       │  τ ↕    (tangencial) │  ← tensiones en el plano de la sección
       └──────────────────────┘
```

> **Analogía contable:** El esfuerzo es como el saldo total de una cuenta; la tensión es como el rendimiento por unidad de capital (tasa). Dos vigas pueden tener el mismo esfuerzo N pero tensiones σ muy diferentes si tienen secciones distintas. El material "siente" la tensión, no el esfuerzo.

---

## 15. Momento de inercia de la sección

El **momento de inercia** de una sección (también llamado segundo momento de área) es una medida de **cómo está distribuida el área geométrica** respecto a un eje. Es una propiedad puramente geométrica de la sección — no tiene nada que ver con la inercia dinámica (masa × aceleración).

```
  Definición conceptual:

  I = Σ (área_i × distancia_i²)

  Es decir: cada trocito de área contribuye con su valor multiplicado
  por el cuadrado de su distancia al eje de referencia.
```

```
  Ejemplo visual para una sección rectangular:

       eje neutro (z)
  ─────────────────────────────
  │  │  │  │  │  │  │  │  │  │  ← franja a distancia y₁ del eje
  │  │  │  │  │  │  │  │  │  │
  ─────────────────────────────  ← EJE NEUTRO
  │  │  │  │  │  │  │  │  │  │
  │  │  │  │  │  │  │  │  │  │  ← franja a distancia y₂ del eje
  ─────────────────────────────

  Iz = Σ (A_i × y_i²)
  Las franjas más alejadas del eje contribuyen MÁS al momento de inercia.
```

### ¿Por qué importa el momento de inercia?

El momento de inercia vincula el **momento flector** M con la **tensión normal** σ en cada punto de la sección:

```
  σ = M · y / I
```

donde:
- `M` = momento flector en la sección [N·m]
- `y` = distancia del punto al eje neutro [m]
- `I` = momento de inercia de la sección respecto al eje neutro [m⁴]

Esto revela dos cosas fundamentales para el diseño:

1. **A mayor I → menor σ** para el mismo M: la sección "resiste más" si su área está lejos del eje
2. **A mayor y → mayor σ**: el punto más alejado del eje neutro es el más solicitado

> **Implicación de diseño:** Aquí está la razón de la forma de la viga I. Concentrar material en las alas (lejos del eje neutro) maximiza el momento de inercia sin aumentar el peso. Es el principio de la distribución eficiente del área.

```
  Comparación de dos secciones con igual área:

  SECCIÓN CUADRADA      SECCIÓN I (misma área)
  ┌────────┐            ████████████  ← ala superior
  │        │            ────────────
  │        │                 ██      ← alma
  │        │            ────────────
  └────────┘            ████████████  ← ala inferior

  Iz similar            Iz MUCHO MAYOR
  (área distribuida     (área concentrada lejos del eje)
   cerca del eje)
```

---

## 16. Gráficos de esfuerzos: fuerzas concentradas vs. distribuidas

### 16.1 Fuerzas concentradas

Una **fuerza concentrada** actúa en un único punto (o en un área muy pequeña en la práctica). Produce **cambios bruscos** ("saltos") en los diagramas de esfuerzos.

```
  P (fuerza concentrada)
  ↓
  ────┬──────────────────────
```

### 16.2 Fuerzas distribuidas

Una **fuerza distribuida** está repartida a lo largo de una longitud. Se expresa como intensidad por unidad de longitud: `q` [N/m].

```
  q (carga uniforme por metro)
  ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
  ─────────────────────────────────
```

### 16.3 Diagrama de momentos flectores

El **diagrama de momentos flectores** (DMF) representa cómo varía M a lo largo del eje de la barra. Es la herramienta visual clave para detectar dónde la estructura está más solicitada.

```
  CASO A: Viga simplemente apoyada — carga concentrada central

         P
         ↓
  A──────┼──────B
  ↑             ↑
  RA=P/2        RB=P/2

  DMF:
  0                              0
   \                            /
    \                          /
     \          /\            /
      \        /  \          /
       ───────    ───────────
       (triángulos — tramos lineales, máximo bajo la carga)


  CASO B: Viga simplemente apoyada — carga distribuida uniforme

  q ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
  A──────────────────────────B
  ↑                          ↑
  RA=qL/2                    RB=qL/2

  DMF:
  0                              0
   \                            /
    ╰──────────────────────────╯
       (parábola — curva suave, máximo en el centro)
```

**Regla práctica de forma del diagrama:**

| Tipo de carga | Forma del diagrama de Q | Forma del diagrama de M |
|--------------|------------------------|------------------------|
| Sin carga en el tramo | Constante (horizontal) | Lineal (inclinado) |
| Carga concentrada | Escalón (salto) | Cambio de pendiente (vértice) |
| Carga distribuida uniforme | Lineal (inclinado) | Parabólico (curvo) |

---

## 17. Otros esfuerzos característicos y situaciones combinadas

El profesor mencionó que existen **otros esfuerzos característicos** más allá de N, Q, M y T. En el caso 3D general, una sección puede tener hasta **seis** esfuerzos:

```
  En el caso 3D completo (referencial local x, y, z):

  Fuerzas:      N (axial)
                Qy (cortante en y)
                Qz (cortante en z)

  Momentos:     T  (torsor — alrededor del eje x)
                My (flector alrededor de y)
                Mz (flector alrededor de z)
```

En el análisis introductorio 2D (viga en el plano x-z) se trabaja con N, Q y M. La torsión T aparece cuando se pasa a estructuras espaciales.

### Flexo-torsión

Cuando un elemento está sometido simultáneamente a **flexión** y **torsión** (caso muy frecuente en ejes de máquinas, vigas de balcones, pórticos espaciales), el análisis debe combinar los efectos de M y T para obtener la tensión resultante en cada punto de la sección.

---

## 18. El modelo completo: de las cargas al dimensionamiento

El profesor describió que el rol del ingeniero es darle un **modelo matemático al comportamiento del sólido**. Aunque en esta instancia todo fue conceptual, la cadena completa de razonamiento es:

```
  ┌─────────────────────────────────────────────────────────────────┐
  │  1. CARGAS EXTERNAS                                             │
  │     Identificar fuerzas activas (tipo, magnitud, posición)      │
  └─────────────────────────────────────┬───────────────────────────┘
                                        │
                                        ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  2. EQUILIBRIO GLOBAL                                           │
  │     ΣF = 0 y ΣM = 0  →  calcular reacciones en los apoyos      │
  └─────────────────────────────────────┬───────────────────────────┘
                                        │
                                        ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  3. CORTE EN SECCIÓN DE INTERÉS                                 │
  │     Aplicar equilibrio a la parte cortada                       │
  │     → obtener N, Q, M (y T) en esa sección                     │
  └─────────────────────────────────────┬───────────────────────────┘
                                        │
                                        ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  4. TENSIONES EN CADA PUNTO DE LA SECCIÓN                       │
  │     σ = f (N, M, I, y)      ← tensión normal                   │
  │     τ = f (Q, T, A, forma)  ← tensión tangencial               │
  └─────────────────────────────────────┬───────────────────────────┘
                                        │
                                        ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  5. COMPARACIÓN CON TENSIÓN ADMISIBLE DEL MATERIAL              │
  │     σ_máx ≤ σ_adm  ?   τ_máx ≤ τ_adm  ?                        │
  │                                                                 │
  │     SI → la estructura CUMPLE (dimensionamiento correcto)       │
  │     NO → hay que cambiar la SECCIÓN o el MATERIAL               │
  └─────────────────────────────────────────────────────────────────┘
```

Este esquema muestra por qué el ingeniero trabaja siempre con **dos variables**: la fuerza (pasos 1-3) y la sección (pasos 4-5). La sección determina I, A, y, y la forma de distribución de tensiones.

---

## 19. Errores conceptuales frecuentes

| Error | Corrección |
|-------|-----------|
| Confundir baricentro de la sección con centro de gravedad | El baricentro (G) es propiedad 2D del área; el CG es propiedad 3D del cuerpo. Coinciden en proyección para material homogéneo. |
| Confundir esfuerzo (N, Q, M) con tensión (σ, τ) | El esfuerzo es la fuerza interna total en la sección [N] o [N·m]; la tensión es esa fuerza por unidad de área [Pa]. El material "siente" la tensión. |
| Creer que el eje neutro siempre divide la sección a la mitad | Solo es así para secciones simétricas con material homogéneo en flexión pura. En secciones asimétricas o bimateriales, el eje neutro se desplaza. |
| Pensar que una carga distribuida y su resultante concentrada son equivalentes en todos los aspectos | Producen la misma resultante y los mismos diagramas de esfuerzos globales, pero distribuciones locales de tensión distintas cerca del punto de aplicación. |
| Ignorar el momento torsor T cuando las cargas no pasan por el centro de torsión | T aparece siempre que la carga no pasa por el centro de corte de la sección (que coincide con el baricentro solo en secciones doble simétricas). |
| Creer que el momento de inercia depende del material | I es una propiedad puramente geométrica de la forma de la sección. El material aparece en la fórmula de tensión multiplicando I (a través de E en deformaciones), no en I mismo. |
| Confundir momento de inercia con momento de una fuerza | Son conceptos distintos con el mismo nombre parcial. El momento de inercia (I) es geométrico [m⁴]; el momento de una fuerza (M) es estático [N·m]. |

---

## 20. Tabla de símbolos y unidades

| Símbolo | Nombre | Unidad SI | Observaciones |
|---------|--------|-----------|---------------|
| N | Fuerza normal (axial) | N (newton) | + tracción, − compresión |
| Q | Fuerza cortante | N (newton) | Perpendicular al eje |
| M | Momento flector | N·m | Produce curvatura |
| T | Momento torsor | N·m | Produce giro alrededor del eje |
| σ | Tensión normal | Pa = N/m² | Perpendicular a la sección |
| τ | Tensión tangencial | Pa = N/m² | Paralela a la sección |
| I | Momento de inercia de la sección | m⁴ | Propiedad geométrica pura |
| A | Área de la sección | m² | Propiedad geométrica pura |
| y | Distancia al eje neutro | m | Variable en la fórmula σ = My/I |
| G | Baricentro de la sección | — | Punto geométrico 2D |
| n̂ | Normal a la sección | — | Vector unitario perpendicular al corte |

---

## 21. Mapa conceptual

```
                         ESFUERZOS CARACTERÍSTICOS
                                    │
            ┌───────────────────────┼────────────────────────┐
            │                       │                        │
     SÓLIDO BASE              SISTEMA DE FUERZAS       MODELO
     · Alma llena             · Activas (cargas)       MATEMÁTICO
     · Homogéneo              · Reactivas (apoyos)          │
     · Isótropo                       │                      │
                              EQUILIBRIO                     │
                              ΣF=0, ΣM=0                     │
                                    │                        │
                    ┌───────────────┴──────────────┐         │
                    │                              │         │
                 SECCIÓN                   LÍNEA DE          │
                 (corte 2D)                BARICENTROS        │
                    │                              │         │
            ┌───────┴───────┐                      │         │
            │               │                      │         │
       BARICENTRO       PROPIEDADES           EJE NEUTRO ────┘
       de la sección    GEOMÉTRICAS           (σ = 0)
            │           · Área A
            │           · Inercia I
            │                │
   ┌────────┴────────┐        │
   │                 │        │
ESFUERZOS        ESFUERZOS   │
DIRECTOS         DE MOMENTO  │
   │                 │        │
   ├── N (normal)    ├── M (flector)
   └── Q (cortante)  └── T (torsor)
            │                │
            ▼                ▼
       TENSIONES NORMALES (σ)
       TENSIONES TANGENCIALES (τ)
            │
            ▼
      σ_máx ≤ σ_adm ?
            │
     ┌──────┴──────┐
    SÍ             NO
     │              │
  CUMPLE       REDIMENSIONAR
  (diseño       (cambiar sección
   correcto)     o material)
```

---

*Fuentes: apuntes de clase de Ingeniería Mecánica I — UTN FRBA, 2026 (primer cuatrimestre). Temas expuestos por el docente: sólido de alma llena, material homogéneo e isótropo, sistema de fuerzas activo/reactivo, plano de simetría, equilibrio, baricentro de la sección vs. centro de gravedad, línea de baricentros, norma a la sección, resultante, momento como producto vectorial, esfuerzos N/Q/M/T, momento flector como par de pares, eje neutro teórico, tensiones normales y tangenciales, momento de inercia, diagramas de momentos flectores, cargas concentradas vs. distribuidas, y dimensionamiento estructural.*
