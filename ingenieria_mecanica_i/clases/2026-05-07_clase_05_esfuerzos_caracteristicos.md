# Clase 5 — Esfuerzos característicos

**Fecha:** 7 de mayo de 2026  
**Profesor:** Abud  
**Unidad:** UT I / UT II — La Ingeniería y la Tecnología / Proceso de Diseño  
**Referencia:** Ver también `campus_virtual/12_esfuerzos_caracteristicos.md` para desarrollo completo con diagramas y errores frecuentes.

---

## 1. La pregunta que organiza todo

Abud abrió la clase con la pregunta que da sentido a todo el tema:

> **¿Qué pasa interiormente en un sólido cuando se le aplican fuerzas externas?**

Para responderla, necesitamos tres cosas: un **marco de referencia**, **abstracciones** e **hipótesis** que permitan modelar matemáticamente el comportamiento del sólido. Sin ese andamiaje conceptual previo, no se puede plantear ninguna ecuación.

---

## 2. El sólido base: alma llena

El punto de partida del análisis es el **sólido de alma llena**: un cuerpo cuya sección transversal es completamente maciza, sin huecos.

> **Abud fue explícito: los huecos no entran.** El análisis de secciones huecas (tubos, perfiles I, U, L) es una extensión posterior; ahora trabajamos solo con sección maciza.

```
  ALMA LLENA (válida para este análisis)
  ████████████
  ████████████
  ████████████

  ALMA ESBELTA (queda fuera por ahora)
  ████████████
  █          █
  ████████████
```

---

## 3. Hipótesis sobre el material: homogéneo e isótropo

Para que el modelo matemático sea tratable, se asumen dos propiedades ideales del material:

### Homogéneo
Las propiedades mecánicas son **iguales en todos los puntos** del cuerpo. No importa dónde se tome la muestra: el material "se comporta igual".

> Ejemplo real que lo aproxima: acero estructural laminado.  
> Contraejemplo: hormigón armado, madera, materiales compuestos.

### Isótropo
Las propiedades son **iguales en todas las direcciones**. La resistencia no varía según desde qué ángulo se cargue el material.

> Contraejemplo: la madera es mucho más resistente a lo largo de la fibra que perpendicularmente — es **anisótropa**.

**¿Por qué se asumen estas hipótesis?** Porque simplifican el modelo matemático hasta hacerlo manejable. Con material homogéneo e isótropo, la relación entre esfuerzos y deformaciones queda definida por solo dos constantes: el módulo de elasticidad `E` y el coeficiente de Poisson `ν`. Sin estas hipótesis, harían falta 21 constantes independientes.

---

## 4. El sistema de fuerzas

El sólido y el sistema de fuerzas que actúan sobre él **admiten un plano de simetría** — condición que simplifica el análisis a dos dimensiones.

### Fuerzas activas y reactivas

Abud usó la siguiente notación en pizarrón:

```
  P_i  →  fuerzas ACTIVAS  (las cargas que se aplican al sólido)
  R₁, R₂  →  fuerzas REACTIVAS  (las reacciones de los apoyos)
```

- `P_i` representa **todas** las fuerzas activas que actúan sobre el sólido (cada `P_i` es una fuerza individual del sistema de cargas).
- `R₁` y `R₂` son las fuerzas **reactivas** que los apoyos ejercen para mantener el sólido en equilibrio.

```
         P₁       P₂       P₃
          ↓        ↓        ↓
  ════════╪════════╪════════╪════════
                  VIGA
  ════════╪════════╪════════╪════════
          ↑                 ↑
          R₁                R₂
```

### Condición de equilibrio

El sólido con **todo** su sistema de fuerzas (activas + reactivas) está en **equilibrio**:

```
  ΣP_i + ΣR_j = 0     (suma vectorial de todas las fuerzas = 0)
  ΣM = 0              (suma de todos los momentos = 0)
```

Las fuerzas reactivas son exactamente las que permiten que se cumpla esta condición.

---

## 5. Baricentro de la sección — G

Abud introdujo el **baricentro de la sección** (G) y aclaró con énfasis que:

> **G NO es el centro de gravedad ni el centro de masa.**

| Concepto | Dimensión | Propiedad de | Lo que mide |
|---|---|---|---|
| Centro de gravedad (CG) | 3D | El cuerpo completo (volumen) | Distribución de masa en el espacio |
| Baricentro de la sección (G) | 2D | La sección transversal (área) | Centro geométrico del área de corte |

Para un material homogéneo, G y CG coinciden en proyección — pero son conceptos distintos. El baricentro es una propiedad **geométrica** del área, no una propiedad de la masa.

### La línea SS — eje baricéntrico

Si se realizan infinitos cortes transversales a lo largo de la barra, cada sección tiene su propio baricentro G. Abud llamó a la línea que une todos esos baricentros **línea SS**:

```
         G₁   G₂   G₃   G₄   G₅
  S ─────·────·────·────·────·───── S
  ┌──────┼────┼────┼────┼────┼──────┐
  │      │    │    │    │    │      │
  └──────┼────┼────┼────┼────┼──────┘

         LÍNEA SS = eje baricéntrico
  (una línea con infinitos baricentros, uno por cada sección posible)
```

Esta línea es el **eje de referencia** de todo el análisis. Los esfuerzos de flexión se calculan respecto a ella.

---

## 6. La norma a la sección y la resultante

Cuando se hace un corte imaginario en el sólido, la **norma** es el vector perpendicular a la superficie de corte (apunta en la dirección del eje longitudinal). Las fuerzas internas en esa sección se expresan como su **resultante**, que siempre se puede descomponer en dos partes:

```
  Resultante de fuerzas internas:
  ├─ Componente NORMAL (perpendicular a la sección)  →  N
  └─ Componente TANGENCIAL (paralela a la sección)   →  Q

  Resultante de momentos internos:
  ├─ Componente alrededor del eje de la barra        →  T (torsor)
  └─ Componente perpendicular al eje                 →  M (flector)
```

**Condición clave:** la resultante de fuerzas a la izquierda del corte debe anularse con la resultante de fuerzas a la derecha del corte. El equilibrio del sólido cortado es lo que permite determinar los esfuerzos internos.

```
   IZQUIERDA DEL CORTE        │ DERECHA DEL CORTE
                              │
   (P_i activas + R₁) → res. │ ← res. (P_i activas + R₂)
                              │
              se anulan entre sí (equilibrio)
```

---

## 7. Los tres esfuerzos básicos del marco de referencia

Abud enumeró los **tres esfuerzos característicos fundamentales** que trabajan en el marco 2D introductorio:

### N — Fuerza normal (esfuerzo axial)
- Dirección: **perpendicular a la sección** (a lo largo del eje de la barra)
- Puede ser:
  - **Tracción** (+N): las fibras del material se estiran y separan
  - **Compresión** (−N): las fibras se comprimen y acercan

```
  TRACCIÓN:     ←══════════════►
  COMPRESIÓN:   ►══════════════←
```

### Q — Fuerza cortante (esfuerzo de corte)
- Dirección: **paralela a la sección** (perpendicular al eje de la barra)
- Tiende a "cizallar" el material: las dos mitades del sólido a ambos lados del corte tienden a deslizarse una respecto a la otra.

### M — Momento flector
- Es un **par de pares**: internamente, el momento flector surge de la interacción entre el bloque de compresión (zona superior) y el bloque de tracción (zona inferior) de la sección. Dos bloques de fuerza iguales, opuestos y separados forman un par; el resultado de ese par es el momento.

```
  ← Compresión ─┐
                 │  distancia d  →  M = fuerza × d
  → Tracción  ──┘
```

> Abud lo definió como **par de pares**: el momento flector es el resultado de dos conjuntos de fuerzas internas distribuidas que, integradas sobre la sección, producen un par resultante.

### El momento de una fuerza

Abud aclaró el concepto en el pizarrón:

> El momento de una fuerza es el **producto vectorial** entre dos vectores — el vector posición `r` y el vector fuerza `F` — y por lo tanto **su resultado es también un vector**.

```
  M = r × F   (producto vectorial)
```

Esto explica por qué el momento flector M es un vector (tiene dirección y sentido), no solo un número.

---

## 8. Fórmula de flexión y flexo-torsión

Cuando actúan simultáneamente flexión (M) y torsión (T), el análisis debe combinar ambos efectos. Abud mencionó la **fórmula de flexo-torsión** como el tipo de expresión que se usa para calcular la tensión resultante en esos casos — el desarrollo completo de la fórmula es materia de cursos más avanzados; en esta clase quedó planteada como concepto.

---

## 9. Fuerzas concentradas vs. distribuidas

Un sistema de fuerzas puede aplicarse de dos maneras sobre el sólido:

| Tipo | Descripción | Diagrama |
|---|---|---|
| **Fuerza concentrada** | Actúa en un único punto | `↓ P` en un punto |
| **Fuerza distribuida** | Repartida a lo largo de una longitud | `↓↓↓↓↓↓ q [N/m]` |

La forma en que la fuerza está distribuida afecta directamente la **forma del diagrama de momentos flectores**:
- Carga concentrada → diagrama de M con **vértice** (cambio brusco de pendiente)
- Carga distribuida uniforme → diagrama de M con forma **parabólica** (curva suave)

Construir el **gráfico de momentos flectores** a lo largo de toda la viga es una herramienta clave: permite ver de un vistazo dónde está la sección más solicitada y cuánto vale M en cada punto.

---

## 10. Dos variables, dimensionamiento

Abud sintetizó la lógica de trabajo del ingeniero:

> Siempre trabaja con **dos variables**: las **fuerzas** y las **secciones**. El objetivo es **dimensionar** — verificar si la estructura cumple con el objetivo para el que fue diseñada.

### Tensión: la unidad que une fuerzas y secciones

```
  Tensión σ = Fuerza / Área = N/m² = Pa
```

La tensión es la **fuerza por unidad de área** — es lo que el material "siente" en cada punto. La misma fuerza produce tensiones muy distintas según el área de la sección.

Abud distinguió dos tipos de tensión:

| Tipo | Símbolo | Dirección | Esfuerzo que la genera |
|---|---|---|---|
| **Tensión normal** | σ (sigma) | Perpendicular a la sección | N (normal) y M (flector) |
| **Tensión tangencial** | τ (tau) | Paralela a la sección | Q (cortante) y T (torsor) |

Abud mencionó también que existen **otros esfuerzos característicos** más allá de los tres básicos — en el caso 3D completo hay hasta seis. En esta instancia introductoria se trabaja con N, Q y M (y T cuando hay torsión).

---

## 11. Momento de inercia

Abud introdujo el **momento de inercia de la sección** (I). Su unidad es `cm⁴` (o `m⁴` en SI).

Es una propiedad **puramente geométrica** de la sección — describe cómo está distribuida el área respecto al eje neutro. No depende del material, solo de la forma y tamaño de la sección.

Su relevancia: aparece en la fórmula que relaciona el momento flector con la tensión normal:

```
  σ = M · y / I
```

A mayor `I` (área bien distribuida lejos del eje), menor tensión `σ` para el mismo momento M. Por eso las vigas en I son más eficientes que las rectangulares: concentran material lejos del eje neutro, maximizando I sin aumentar el peso.

---

## Resumen de la clase

| Concepto | Definición de Abud / idea central |
|---|---|
| Pregunta central | ¿Qué pasa interiormente? → necesitamos marco de referencia + hipótesis |
| Alma llena | Sección maciza; los huecos no entran en este análisis |
| Homogéneo | Propiedades iguales en todos los puntos |
| Isótropo | Propiedades iguales en todas las direcciones |
| P_i / R₁, R₂ | Fuerzas activas / fuerzas reactivas |
| G (baricentro) | Centro geométrico del área de la sección — NO es CG ni centro de masa |
| Línea SS | Eje baricéntrico: la línea de todos los baricentros del sólido |
| N, Q, M | Los tres esfuerzos básicos del marco de referencia |
| Momento (M = r × F) | Producto vectorial → resultado es un vector |
| Momento flector | "Par de pares" — bloque comprimido + bloque traccionado |
| Tensión (σ, τ) | Fuerza por unidad de área; normal (⊥ sección) vs. tangencial (∥ sección) |
| Momento de inercia I | Propiedad geométrica de la sección [cm⁴]; aparece en σ = M·y/I |
| Dimensionamiento | Verificar que σ_máx ≤ σ_admisible del material |

---
*Fuente: apuntes de clase — Prof. Abud, 07/05/2026*
