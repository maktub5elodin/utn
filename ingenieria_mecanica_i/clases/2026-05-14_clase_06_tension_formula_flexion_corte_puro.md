# Clase 6 — Tensión, fórmula de flexión y esfuerzo de corte puro

**Fecha:** 14 de mayo de 2026  
**Profesor:** Abud  
**Continuación de:** Clase 5 (07/05) — esfuerzos característicos N, Q, M, T

---

## 1. Tensión — definición formal

> **Tensión** es la fuerza interna que relaciona los esfuerzos internos por unidad de área.

Dicho de otro modo: el esfuerzo interno (N, Q, M) es la fuerza total que actúa sobre toda una sección. La tensión es cuánto de esa fuerza corresponde a cada centímetro cuadrado de esa sección.

```
  Esfuerzo (total)        Tensión (por unidad de área)
  ──────────────────  →   ─────────────────────────────
  N [N o kN]              σ = N / A   [N/m² = Pa]
  Q [N o kN]              τ = Q / A   [N/m² = Pa]
```

El material no "siente" el esfuerzo total — siente la tensión en cada punto. Por eso dos barras con la misma fuerza axial pueden estar en estados muy distintos si tienen secciones diferentes.

---

## 2. Tensiones normales (σ) y tangenciales (τ)

| Tipo | Símbolo | Dirección | Origen | Unidades |
|---|---|---|---|---|
| **Normal** | σ (sigma) | Perpendicular a la sección | Esfuerzo axial N y momento flector M | Pa = N/m² |
| **Tangencial** | τ (tau) | Paralela a la sección (en el plano del corte) | Esfuerzo cortante Q y momento torsor T | Pa = N/m² |

En la práctica de ingeniería mecánica se trabaja frecuentemente con múltiplos:

```
  1 MPa = 1 N/mm²  (megapascal, muy usado en resistencia de materiales)
  1 GPa = 1.000 MPa
```

El acero estructural, por ejemplo, tiene una resistencia del orden de 250 MPa.

---

## 3. Relación entre el momento flector M y la tensión normal σ

Abud estableció que M y σ son **proporcionales**: a mayor momento flector en una sección, mayor tensión normal en esa sección.

La intuición es directa: si se aplica una fuerza mayor sobre la viga, el momento flector en la sección crítica aumenta, y con él la tensión que el material debe soportar.

Esto anticipa la fórmula de flexión que se desarrolla en la sección siguiente.

---

## 4. Momento de inercia de la sección — I

El **momento de inercia de la sección** (también llamado segundo momento de área) mide cómo está distribuida el área de la sección respecto al eje neutro. Es una propiedad **puramente geométrica** — no depende del material.

### Fórmula

```
        N
I_xx = Σ  ΔA_i · y_i²
       i=1
```

Donde:
- `ΔA_i` = pequeño elemento de área de la sección [mm² o cm²]
- `y_i` = distancia desde ese elemento al eje neutro xx [mm o cm]
- La suma recorre todos los elementos en que se divide la sección

### Unidades

> **Corrección importante de notación:** las unidades de I son **mm⁴ o cm⁴** (no mm² ni cm²).

La razón es directa: se multiplica área [mm²] por distancia al cuadrado [mm²], y el resultado es [mm⁴]:

```
  I = ΔA · y²  →  [mm²] × [mm²] = [mm⁴]
```

### Interpretación

Las franjas de área **más alejadas del eje neutro** contribuyen mucho más a I, porque entran al cuadrado en la fórmula (y_i²). Esto explica por qué la sección en I (viga doble T) es tan eficiente: concentra la mayor parte del área en las alas, lejos del eje neutro, maximizando I con el mínimo material.

```
  SECCIÓN MACIZA        SECCIÓN EN I (misma área total)
  ┌──────────┐          ████████████  ← ala superior (lejos del eje)
  │          │          ────────────
  │          │               ██       ← alma (cerca del eje)
  │          │          ────────────
  └──────────┘          ████████████  ← ala inferior (lejos del eje)

  I pequeño              I mucho mayor
```

---

## 5. Fórmula de flexión: σ = M·c / I

La **fórmula de flexión** (o de Euler-Bernoulli) relaciona el momento flector M con la tensión normal σ en cualquier fibra de la sección:

```
       M · c
  σ = ───────
         I
```

Donde:
- `M` = momento flector en la sección [N·mm]
- `c` = distancia desde el eje neutro hasta la fibra donde se calcula σ [mm]
- `I` = momento de inercia de la sección respecto al eje neutro [mm⁴]
- `σ` = tensión normal resultante [N/mm² = MPa]

### ¿Qué es `c`?

`c` es la distancia desde el eje neutro hasta el punto donde queremos conocer la tensión. Si queremos la tensión máxima (la más peligrosa), usamos `c = y_max` — la distancia hasta la fibra más alejada del eje neutro.

```
          ← c_sup (distancia al ala superior) →  σ_sup (compresión)
          ─────────────────────────────────────────────
EJE NEUTRO ─────────────────── · ──────────────────── σ = 0
          ─────────────────────────────────────────────
          ← c_inf (distancia al ala inferior) →  σ_inf (tracción)
```

### Efecto de I sobre σ

Como I aparece en el denominador:

```
  ↑ I  →  ↓ σ   (para el mismo momento M)
  ↓ I  →  ↑ σ
```

**A mayor momento de inercia, menor tensión** para el mismo esfuerzo externo. Esta es la razón de diseño fundamental para preferir secciones con alto I: permiten soportar los mismos momentos con menor tensión interna, o bien soportar mayores momentos sin superar la tensión admisible.

---

## 6. Tensión admisible

La **tensión admisible** (σ_adm) es el límite máximo de tensión que puede tener el material sin que falle o se deforme permanentemente. Depende del material y del tipo de carga.

La condición de diseño es:

```
  σ_máx  ≤  σ_adm   (la tensión real no debe superar la admisible)
```

Si σ_máx > σ_adm, la estructura no cumple: hay que cambiar la sección (aumentar I), cambiar el material (aumentar σ_adm), o reducir las cargas (disminuir M).

El proceso completo de **dimensionamiento** queda entonces:

```
  Cargas → M en cada sección → σ = M·c/I → comparar con σ_adm
                                                    │
                                        ┌───────────┴───────────┐
                                      CUMPLE               NO CUMPLE
                                   σ ≤ σ_adm             cambiar sección
                                                           o material
```

---

## 7. La resultante — aclaración

Abud aclaró este concepto que aparece frecuentemente en los análisis:

> La **resultante** es simplemente la **suma vectorial de todas las fuerzas** que actúan sobre el sistema (o sobre la parte del sistema que se está analizando).

Es una fuerza — y por lo tanto un **vector**: tiene módulo, dirección y sentido. Reemplaza al sistema de fuerzas original de manera equivalente desde el punto de vista del movimiento del cuerpo.

```
  F₁ + F₂ + F₃  →  R (resultante)

  R produce el mismo efecto traslacional que el conjunto F₁, F₂, F₃
```

Esta aclaración es útil cuando se analiza un tramo del sólido cortado: la resultante de todas las fuerzas a la izquierda del corte se descompone en N, Q, M y T — los esfuerzos característicos de esa sección.

---

## 8. Esfuerzo de corte puro

El **esfuerzo de corte puro** ocurre cuando sobre una sección actúa exclusivamente la fuerza cortante Q, sin fuerza axial (N = 0) ni momento flector (M = 0).

En ese caso, la tensión es puramente tangencial:

```
       Q
  τ = ───
       A
```

Donde `A` es el área de la sección que resiste el corte.

### Ejemplo 1: la tijera

Al cortar con tijera, las dos hojas ejercen fuerzas paralelas y opuestas sobre el material en la zona de corte. En el plano de corte, el material experimenta **puro cizallamiento** — sin tracción ni compresión, solo deslizamiento de una parte sobre la otra.

```
  Hoja superior  →→→→→→
  ─────────────────────────  ← plano de corte (τ puro)
  Hoja inferior  ←←←←←←
```

### Ejemplo 2: el roblón diseñado para corte puro

Un **roblón** (remache) es un elemento de unión que conecta dos chapas o perfiles. Cuando las piezas unidas son traccionadas en sentidos opuestos, el roblón trabaja en **corte puro**: la fuerza se transmite de una chapa a la otra a través del cuerpo del roblón, que es cizallado en su sección transversal.

```
  Chapa A  →→→→  ║ ROBLÓN ║  ←←←←  Chapa B
                  ────────
                  ↑ sección de corte del roblón
                  (τ = Q / A_roblón)
```

Este es uno de los casos más claros de diseño para un esfuerzo específico: el roblón se dimensiona exactamente para resistir la fuerza cortante Q con la tensión tangencial resultante menor que τ_adm del material.

---

## Resumen de la clase

| Concepto | Definición / fórmula |
|---|---|
| Tensión | Esfuerzo interno por unidad de área |
| σ (tensión normal) | Perpendicular a la sección — unidad: Pa = N/m² |
| τ (tensión tangencial) | Paralela a la sección — unidad: Pa = N/m² |
| M proporcional a σ | A mayor momento flector, mayor tensión normal |
| I_xx (momento de inercia) | `Σ ΔA_i · y_i²` — unidad: **mm⁴ o cm⁴** |
| Fórmula de flexión | `σ = M·c / I` |
| Efecto de I | Mayor I → menor σ para el mismo M |
| Tensión admisible | Límite del material: σ_máx ≤ σ_adm |
| Resultante | Suma vectorial de fuerzas → es un vector |
| Corte puro | Solo actúa Q → τ = Q/A; sin N ni M |
| Roblón | Unión diseñada para trabajar en corte puro |

---
*Fuente: apuntes de clase — Prof. Abud, 14/05/2026*
