# Clase 8 — Pérdida de estabilidad y pandeo

**Fecha:** 28 de mayo de 2026  
**Profesor:** Abud  
**Continuación de:** Clase 7 (21/05) — torsión pura, τ = G·ρ·θ

---

## 1. De qué se trata: estabilidad vs. resistencia

Hasta ahora el análisis estuvo centrado en la **resistencia**: ¿el material soporta la tensión que le aplico? (σ ≤ σ_adm).

Hoy aparece un fenómeno diferente: la **pérdida de estabilidad**. Una estructura puede fallar sin que el material alcance su límite de resistencia — simplemente porque el sistema pasa de un estado de equilibrio estable a uno inestable.

### Intuición: equilibrio estable vs. inestable

```
  ESTABLE                   INESTABLE
  (vuelve si se perturba)   (se aleja si se perturba)

       _                         /\
      / \                       /  \
     /   \                     /    \
  ──●──────   → perturbo →   ──────●──
    (bolita en el fondo        (bolita en la cima
     del valle: vuelve)         de la colina: se cae)
```

Una columna comprimida que está parada derecha está en equilibrio — pero puede ser estable o inestable dependiendo de cuánta carga lleva. Cuando la carga supera un valor crítico, el equilibrio pasa de estable a inestable: la columna se dobla lateralmente de golpe.

---

## 2. La ecuación de la curva elástica: E·I·y'' = M

La base de este análisis es la relación entre el momento flector M y la forma que adopta el eje de la barra al deformarse.

La deformación lateral de una barra se describe por la función `y(z)`:
- `z` = posición a lo largo del eje de la barra
- `y(z)` = desplazamiento lateral (flecha) en cada punto z

La **curvatura** de esa función es su segunda derivada `y''` (y doble prima). Matemáticamente: y'' mide cómo cambia la pendiente de y(z), es decir, cuánto se está curvando la barra en ese punto.

La relación fundamental de la teoría de vigas (Euler-Bernoulli):

```
  E · I · y'' = M
```

Donde:
- `E` = módulo de elasticidad longitudinal [MPa] — rigidez del material
- `I` = momento de inercia de la sección respecto al **eje mínimo** [mm⁴]
- `y''` = segunda derivada de la deflexión lateral [1/mm] — curvatura
- `M` = momento flector en esa sección [N·mm]

### ¿Por qué el eje mínimo?

La columna va a pandear en la dirección donde le cuesta **menos** resistir. Como P_cr depende de I (lo veremos en breve), la columna colapsa primero alrededor del eje con menor I — el eje mínimo. Por eso se toma ese I para el análisis: es el caso más desfavorable y el que gobierna el diseño.

---

## 3. Ley de Hooke — repaso y conexión

Abud repasó la Ley de Hooke antes de plantear la ecuación diferencial:

> **Fuerza necesaria para estirar o comprimir un resorte es directamente proporcional a la distancia que se deforma, siempre y cuando no se supere su límite elástico.**

```
  F = k · x
  (fuerza = constante del resorte × deformación)
```

La relación `E·I·y'' = M` es la versión de Hooke aplicada a una viga: el momento M es la "fuerza" que curva la barra, y y'' es la "deformación" (curvatura) resultante. La constante de proporcionalidad es `E·I`, que mide la rigidez a la flexión de la barra.

---

## 4. La columna bajo carga axial compresiva

El caso de pandeo: una barra recta cargada con una fuerza axial compresiva P en sus extremos.

```
          P
          ↓
     ─────┬─────
          │
          │  ← columna recta (estado inicial)
          │
     ─────┴─────
          ↑
          P
```

Si la columna se desplaza lateralmente una pequeña cantidad `y` en algún punto, el momento flector que genera esa carga es:

```
  M = − P · y
```

El signo negativo indica que P tiende a aumentar la curvatura (si y aumenta, M aumenta en sentido que sigue curvando la barra — es un efecto desestabilizador).

Sustituyendo en `E·I·y'' = M`:

```
  E·I·y'' = −P·y
  E·I·y'' + P·y = 0
```

Dividiendo por E·I:

```
  y'' + (P / E·I) · y = 0
```

---

## 5. Resolución de la ecuación diferencial

### Sustitución de variable

Se define la constante:

```
  k² = P / (E·I)
```

La ecuación queda:

```
  y'' + k²·y = 0
```

Esta es una ecuación diferencial ordinaria de segundo orden, lineal, con coeficientes constantes. Su solución general es:

```
  y(z) = c₁ · sen(k·z) + c₂ · cos(k·z)
```

Donde `c₁` y `c₂` son constantes a determinar.

### Condiciones de borde

Para encontrar c₁ y c₂ se aplican las **condiciones de borde**: las restricciones físicas en los extremos de la columna. Para una columna simplemente apoyada en ambos extremos (articulada-articulada):

```
  y(0) = 0   (el extremo inferior no se desplaza)
  y(L) = 0   (el extremo superior no se desplaza)
```

**Aplicando y(0) = 0:**

```
  0 = c₁ · sen(0) + c₂ · cos(0) = 0 + c₂   →   c₂ = 0
```

La solución se reduce a: `y(z) = c₁ · sen(k·z)`

**Aplicando y(L) = 0:**

```
  0 = c₁ · sen(k·L)
```

Hay dos posibilidades:
- `c₁ = 0` → y(z) = 0 para todo z: la columna permanece recta. Solución trivial — no informa nada.
- `sen(k·L) = 0` → solución no trivial: la columna sí se deflecta.

Para que `sen(k·L) = 0`:

```
  k·L = n·π     con n = 1, 2, 3, ...
```

---

## 6. La primera carga crítica (Euler)

El menor valor de carga que produce inestabilidad corresponde a `n = 1`:

```
  k·L = π   →   k² = π² / L²

  Como k² = P / (E·I):

       π² · E · I
  P_cr = ──────────     ← Primera carga crítica de Euler
              L²
```

Esta es la **fórmula de Euler para el pandeo**. Es la carga mínima a la que la columna deja de ser estable.

```
  A mayor E (material más rígido)   →  P_cr mayor (más resistente al pandeo)
  A mayor I (sección más robusta)   →  P_cr mayor
  A mayor L (columna más larga)     →  P_cr menor (más susceptible al pandeo)
                                        (L entra al cuadrado en el denominador)
```

Las cargas `n = 2, 3, ...` corresponden a modos de pandeo superiores (la columna formaría 2, 3... ondas), pero en la práctica siempre se alcanza primero el modo `n = 1`.

---

## 7. El pandeo NO es deformación progresiva — es colapso

Este punto fue enfatizado por Abud.

### La diferencia con la falla por resistencia

En falla por resistencia (rotura):
```
  Aumento de carga → aumento gradual de σ → llega al límite → falla
  Es progresivo y observable.
```

En pandeo (pérdida de estabilidad):
```
  Carga por debajo de P_cr → columna recta, sin deflexión lateral
       │
       │  (nada visible ocurre durante todo este rango)
       │
  Carga = P_cr → la columna se deflecta lateralmente de golpe
       │
       │  (colapso: el sistema se vuelve inestable de manera abrupta)
       ▼
  La deflexión crece sin control → colapso estructural
```

Por eso Abud dice: **no es deformación, es colapso**. El sistema no "avisa" — pasa de estable a inestable de forma súbita cuando se alcanza P_cr. No hay zona de transición gradual.

```
  DEBAJO DE P_cr         EN P_cr              ARRIBA DE P_cr
  ─────────────          ──────────           ──────────────
        │                     │                    │
        │  ← estable          │  bifurcación →     │  inestable
        │  (permanece          │  (cualquier        │  (colapsa)
        │   recto)             │   perturbación
                               │   lo vuelca)
```

---

## 8. Mapa del análisis completo

```
  Columna comprimida por P
          │
          ▼
  Suponer pequeña deflexión lateral y(z)
          │
          ▼
  Momento en la sección: M = −P·y
          │
          ▼
  Ecuación de la curva elástica: E·I·y'' + P·y = 0
          │
          ▼
  Sustituir k² = P/(E·I) → y'' + k²·y = 0
          │
          ▼
  Solución: y = c₁·sen(kz) + c₂·cos(kz)
          │
          ▼
  Condiciones de borde → c₂ = 0, sen(kL) = 0 → kL = nπ
          │
          ▼
  n = 1: P_cr = π²·E·I / L²   ← primera carga crítica
          │
          ▼
  Si P < P_cr → estable     Si P ≥ P_cr → colapso (pandeo)
```

---

## Resumen de la clase

| Concepto | Definición / fórmula |
|---|---|
| Pérdida de estabilidad | Paso de equilibrio estable a inestable — sin que el material falle por resistencia |
| E·I·y'' = M | Ecuación de la curva elástica (relación curvatura-momento) |
| Eje mínimo | El I más pequeño — el que gobierna el pandeo (dirección más débil) |
| M = −P·y | Momento que genera la carga axial P sobre una columna deflectada |
| E·I·y'' + P·y = 0 | Ecuación diferencial del pandeo |
| k² = P/(E·I) | Constante de la ecuación diferencial |
| y = c₁·sen(kz) + c₂·cos(kz) | Solución general |
| Condiciones de borde | Restricciones físicas en los extremos → determinan c₁ y c₂ |
| kL = nπ | Condición de no trivialidad para la solución |
| P_cr = π²·E·I / L² | Primera carga crítica de Euler (n = 1) |
| Pandeo | NO es deformación progresiva — es colapso abrupto al alcanzar P_cr |

---
*Fuente: apuntes de clase — Prof. Abud, 28/05/2026*
