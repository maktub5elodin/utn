# Unidad 2 — Topología de la recta real

---

## ¿Para qué sirve esto?

La topología de la recta no es un fin en sí mismo: es el **lenguaje** que hace posible hablar de límites con precisión.

Cuando en la clase siguiente se defina "el límite de `f(x)` cuando `x → a`", la definición dirá algo como *"para todo entorno de `L` existe un entorno reducido de `a`..."*. Sin saber qué es un entorno, esa frase no tiene sentido.

> **Analogía contable:** la topología es como el plan de cuentas. No es lo que te interesa calcular (el balance, el resultado), pero sin él no podés registrar nada de forma coherente. Primero el marco, después los números.

La unidad cubre cuatro bloques:
1. Valor absoluto y distancia
2. Intervalos
3. Entornos y clasificación de puntos
4. Conjuntos acotados: cotas, supremo e ínfimo

---

## Bloque 1 — Valor absoluto y distancia

### Definición de valor absoluto

El **valor absoluto** de un número real `x` es su distancia al origen:

```
|x| = x     si x ≥ 0
|x| = −x    si x < 0
```

Gráficamente:

```
  |x|
   |
 3 |    ╲         ╱
 2 |      ╲     ╱
 1 |        ╲ ╱
 0 |─────────●──────────── x
            0
```

La gráfica de `y = |x|` es una "V" con vértice en el origen.

### Propiedades esenciales

```
|x| ≥ 0                         siempre no negativo
|x| = 0  ↔  x = 0
|−x| = |x|                      simetría
|x · y| = |x| · |y|             multiplicativo
|x / y| = |x| / |y|   (y ≠ 0)
|x + y| ≤ |x| + |y|             desigualdad triangular
```

La **desigualdad triangular** es la más importante. Dice que "el camino directo nunca es más largo que el camino con desvío". Aparece en casi todas las demostraciones de límites.

Una consecuencia útil (se obtiene aplicando la triangular dos veces):

```
| |x| − |y| | ≤ |x − y|
```

### Distancia entre dos puntos

La **distancia** entre `a` y `b` en la recta real es:

```
d(a, b) = |a − b|
```

Esto es el módulo de la diferencia — sin importar cuál es mayor:

```
d(3, 7) = |3 − 7| = |−4| = 4
d(7, 3) = |7 − 3| = |4|  = 4     ← simétrica, como toda distancia
```

Propiedades de la distancia (son las que definen formalmente un "espacio métrico"):

```
d(a, b) ≥ 0                        no negativa
d(a, b) = 0  ↔  a = b
d(a, b) = d(b, a)                  simétrica
d(a, c) ≤ d(a, b) + d(b, c)       desigualdad triangular
```

### Inecuaciones con valor absoluto

Estas formas aparecen constantemente al trabajar con entornos:

```
|x − a| < δ   ↔   a − δ < x < a + δ   ↔   x ∈ (a−δ, a+δ)
|x − a| ≤ δ   ↔   a − δ ≤ x ≤ a + δ   ↔   x ∈ [a−δ, a+δ]
|x − a| > δ   ↔   x < a − δ  o  x > a + δ
```

Leído en palabras: `|x − a| < δ` significa *"x está a menos de δ de distancia de a"*.

---

## Bloque 2 — Intervalos

Un **intervalo** es un subconjunto de ℝ formado por todos los reales entre dos extremos `a` y `b`. Lo que cambia entre los tipos es si los extremos se incluyen o no.

### Intervalos acotados

```
Notación      Nombre            Definición              Extremos
(a, b)        Abierto           a < x < b               excluidos
[a, b]        Cerrado           a ≤ x ≤ b               incluidos
[a, b)        Semiabierto       a ≤ x < b               a incluido, b no
(a, b]        Semiabierto       a < x ≤ b               b incluido, a no
```

En la recta:

```
 Abierto (a, b):      a ──────────── b
                      ○              ○      ← círculo vacío = excluido

 Cerrado [a, b]:      a ──────────── b
                      ●              ●      ← círculo lleno = incluido

 Semiabierto [a, b):  a ──────────── b
                      ●              ○
```

> **Nota importante:** el intervalo `(a, b)` con `a > b` es el **conjunto vacío** ∅. Por ejemplo, `(5, 3)` no contiene ningún elemento.

### Intervalos no acotados

Cuando uno o ambos extremos son infinitos:

```
(a, +∞)  =  { x ∈ ℝ : x > a }
[a, +∞)  =  { x ∈ ℝ : x ≥ a }
(−∞, b)  =  { x ∈ ℝ : x < b }
(−∞, b]  =  { x ∈ ℝ : x ≤ b }
(−∞, +∞) =  ℝ
```

**Convención:** el infinito `±∞` nunca se escribe con corchete cerrado, porque no es un número real — no puede "incluirse".

### Longitud de un intervalo

Para intervalos acotados `(a, b)`, `[a, b)`, etc., la longitud es siempre `b − a` (independientemente de si los extremos están incluidos o no — un punto no tiene longitud).

---

## Bloque 3 — Entornos y clasificación de puntos

### Entorno de un punto

Dado un punto `x₀ ∈ ℝ` y un número real `δ > 0`, el **entorno de radio `δ` centrado en `x₀`** es el intervalo abierto:

```
V_δ(x₀) = (x₀ − δ, x₀ + δ)
```

Es el conjunto de todos los puntos que están a menos de `δ` de distancia de `x₀`:

```
V_δ(x₀) = { x ∈ ℝ : |x − x₀| < δ }
```

Gráficamente:

```
     ←─── δ ───→←─── δ ───→
     │             │             │
  x₀−δ           x₀           x₀+δ
     ○─────────────●─────────────○
          V_δ(x₀) = intervalo abierto
```

> **Intuición:** un entorno de radio δ centrado en x₀ es una "burbuja" de tamaño δ alrededor de x₀. Cuanto más chico δ, más cerca de x₀ están todos los puntos del entorno.

### Entorno reducido (entorno perforado)

El **entorno reducido** o **perforado** es el entorno sin el punto central:

```
V*_δ(x₀) = V_δ(x₀) − {x₀} = (x₀ − δ, x₀) ∪ (x₀, x₀ + δ)
```

Equivalentemente: `{ x ∈ ℝ : 0 < |x − x₀| < δ }`

La condición `0 < |x − x₀|` excluye exactamente el punto `x₀`.

```
     ○─────────────○ ○─────────────○
  x₀−δ            x₀             x₀+δ
                   ↑
             punto excluido
```

El entorno reducido es el concepto clave para definir el límite: cuando se pregunta qué valor se acerca `f(x)` cuando `x → x₀`, se quiere saber qué pasa en los puntos *cercanos a* `x₀`, pero **no en** `x₀` mismo.

### Clasificación de puntos respecto a un conjunto

Dado un conjunto `A ⊆ ℝ` y un punto `x₀ ∈ ℝ` (que puede o no pertenecer a `A`):

#### Punto interior

`x₀` es **interior** a `A` si existe algún entorno de `x₀` completamente contenido en `A`:

```
∃ δ > 0 : V_δ(x₀) ⊆ A
```

Intuitivamente: se puede "moverse un poco" desde `x₀` en cualquier dirección y seguir dentro de `A`.

```
A = [1, 5]

   ●───────────────────────────────●
   1    2    3    4    5
              ↑
         x₀ = 3 es interior: V_{0.5}(3) = (2.5, 3.5) ⊆ A ✓

   x₀ = 1 NO es interior: cualquier V_δ(1) contiene puntos < 1 ∉ A
```

#### Punto exterior

`x₀` es **exterior** a `A` si existe algún entorno de `x₀` completamente contenido en el complemento de `A` (en `ℝ − A`):

```
∃ δ > 0 : V_δ(x₀) ∩ A = ∅
```

#### Punto frontera

`x₀` es **frontera** de `A` si todo entorno de `x₀` contiene puntos de `A` y también puntos fuera de `A`:

```
∀ δ > 0 : V_δ(x₀) ∩ A ≠ ∅   y   V_δ(x₀) ∩ (ℝ − A) ≠ ∅
```

Los extremos de un intervalo son siempre puntos frontera.

#### Resumen gráfico

```
A = (1, 4)       ← intervalo abierto

   ○─────────────────────────────○
   1     2     3     4     5     6
   ↑     ↑           ↑     ↑
frontera  interior  frontera exterior
```

```
Región:          exterior │ frontera │ interior │ frontera │ exterior
                          1                     4
```

### Conjuntos abiertos y cerrados

- Un conjunto es **abierto** si todos sus puntos son interiores.
- Un conjunto es **cerrado** si contiene todos sus puntos frontera.

```
(a, b) → abierto: los extremos a y b son frontera y no están incluidos
[a, b] → cerrado: los extremos están incluidos
[a, b) → ni abierto ni cerrado
ℝ      → abierto Y cerrado a la vez (caso especial)
∅      → abierto Y cerrado a la vez (caso especial)
```

> **No confundir:** "cerrado" no es lo opuesto de "abierto". Un conjunto puede ser ninguno de los dos (como `[a, b)`), o los dos a la vez (como ℝ o ∅). La analogía con puertas "abiertas/cerradas" es engañosa.

### Punto de acumulación

`x₀` es **punto de acumulación** (o punto límite) de `A` si todo entorno reducido de `x₀` contiene al menos un punto de `A`:

```
∀ δ > 0 : V*_δ(x₀) ∩ A ≠ ∅
```

Puntos clave:
- `x₀` **no necesita pertenecer** a `A`.
- Todo punto interior es de acumulación.
- Los extremos de un intervalo son de acumulación (aunque no pertenezcan).

**Ejemplos:**

```
A = (1, 4)

x₀ = 3   →  de acumulación: todo V*_δ(3) tiene puntos de (1, 4) ✓
x₀ = 1   →  de acumulación: todo V*_δ(1) tiene puntos de (1, 4) ✓  (aunque 1 ∉ A)
x₀ = 7   →  NO de acumulación: V_{0.5}(7) = (6.5, 7.5) no toca (1,4)
```

```
B = {1, 2, 3}   ← conjunto discreto

x₀ = 2   →  NO de acumulación: V_{0.4}(2) = (1.6, 2.4) contiene solo el 2,
             y el entorno reducido excluye el 2  →  V*_{0.4}(2) ∩ B = ∅
```

El **conjunto derivado** `A'` es el conjunto de todos los puntos de acumulación de `A`.

### Punto aislado

`x₀ ∈ A` es **punto aislado** si existe un entorno de `x₀` que no contiene otros puntos de `A`:

```
∃ δ > 0 : V_δ(x₀) ∩ A = {x₀}
```

En un intervalo `(a, b)` no hay puntos aislados — siempre hay más puntos alrededor. Los puntos aislados aparecen en conjuntos discretos como `{1, 2, 3}`.

---

## Bloque 4 — Cotas, supremo e ínfimo

### Conjuntos acotados

Un conjunto `A ⊆ ℝ` está:

- **Acotado superiormente** si existe un número `M` tal que `x ≤ M` para todo `x ∈ A`. A ese `M` se lo llama **cota superior** (o **mayorante**).
- **Acotado inferiormente** si existe un número `m` tal que `x ≥ m` para todo `x ∈ A`. A ese `m` se lo llama **cota inferior** (o **minorante**).
- **Acotado** si está acotado superior e inferiormente.

Las cotas no son únicas: si `M` es cota superior, también lo es `M+1`, `M+100`, etc.

```
A = (1, 4)

 Cotas superiores válidas: 4, 5, 10, 100, ...   (cualquier número ≥ 4)
 Cotas inferiores válidas: 1, 0, −5, ...         (cualquier número ≤ 1)
```

> **Analogía:** en contabilidad, una cota superior es como un presupuesto máximo — el gasto real siempre está por debajo. El supremo es el presupuesto más ajustado posible: el mínimo de todos los topes válidos.

### Supremo e ínfimo

El **supremo** de `A`, notado `sup(A)`, es la **menor** de todas las cotas superiores.

El **ínfimo** de `A`, notado `inf(A)`, es la **mayor** de todas las cotas inferiores.

```
A = (1, 4)

  inf(A) = 1      sup(A) = 4
```

Propiedades que definen el supremo `s = sup(A)`:
1. `s` es cota superior: `x ≤ s` para todo `x ∈ A`.
2. `s` es la menor: para todo `ε > 0`, existe `x ∈ A` con `x > s − ε`.

La propiedad 2 dice que no se puede "bajar un poco" el supremo y que siga siendo cota — siempre hay puntos de `A` que se acercan arbitrariamente al supremo.

### Máximo y mínimo

El **máximo** de `A` es el supremo cuando éste **pertenece** a `A`. El **mínimo** es el ínfimo cuando pertenece a `A`.

```
A = [1, 4]   →  min(A) = 1,  max(A) = 4       (existen, los extremos están incluidos)
B = (1, 4)   →  inf(B) = 1,  sup(B) = 4       (NO existen máx/mín; los extremos ∉ B)
C = [1, +∞)  →  min(C) = 1,  sup(C) no existe (no acotado superiormente)
```

**Regla de oro:** todo conjunto acotado tiene supremo e ínfimo, pero puede no tener máximo ni mínimo.

### El axioma del supremo (completitud de ℝ)

Este es el resultado topológico más profundo de la unidad:

> **Axioma del supremo:** todo subconjunto no vacío de ℝ que esté acotado superiormente tiene supremo en ℝ.

No es un teorema que se demuestra — es una **propiedad que define** a los reales y los distingue de los racionales. En ℚ, el conjunto `{x ∈ ℚ : x² < 2}` está acotado superiormente pero no tiene supremo en ℚ (porque `√2 ∉ ℚ`). En ℝ, el supremo siempre existe.

Esta propiedad se llama **completitud** de ℝ y es el fundamento de por qué los límites, las derivadas y las integrales funcionan: garantiza que las aproximaciones sucesivas *convergen a algo*.

---

## Ejemplos resueltos

### Ejemplo 1 — Clasificación de puntos

Sea `A = [−2, 0) ∪ {3}`.

Clasificar: `x₀ = −1`, `x₀ = 0`, `x₀ = 1`, `x₀ = 3`.

```
Recta real:

  ●─────────────────○        ●
 −2      −1     0   1  2  3
```

**`x₀ = −1`:** Interior. Existe `V_{0.5}(−1) = (−1.5, −0.5) ⊆ [−2, 0)` ✓

**`x₀ = 0`:** Frontera. Todo `V_δ(0)` contiene puntos de `[−2, 0)` (por la izquierda) y puntos de `(0, +∞)` fuera de `A`. No es interior (porque 0 ∉ A). Es de acumulación porque todo entorno reducido tiene puntos de `A`.

**`x₀ = 1`:** Exterior. `V_{0.4}(1) = (0.6, 1.4)` no toca ni `[−2, 0)` ni `{3}`.

**`x₀ = 3`:** Frontera y punto **aislado**. Pertenece a `A`, pero `V_{0.5}(3) = (2.5, 3.5)` no contiene otros puntos de `A` → aislado. Todo entorno de 3 contiene puntos fuera de `A` → frontera. **No** es de acumulación.

### Ejemplo 2 — Supremo e ínfimo

Hallar `sup`, `inf`, `max` y `min` (si existen) de:

**(a)** `A = { x ∈ ℝ : x² < 9 } = (−3, 3)`

```
inf(A) = −3   (no pertenece a A → no hay mínimo)
sup(A) =  3   (no pertenece a A → no hay máximo)
```

**(b)** `B = { 1/n : n ∈ ℕ } = {1, 1/2, 1/3, 1/4, ...}`

```
sup(B) = max(B) = 1     (pertenece a B ✓)
inf(B) = 0              (no pertenece a B → no hay mínimo)
```

El 0 es inf porque todo `1/n > 0`, y para cualquier `ε > 0` existe `n` grande tal que `1/n < ε`.

**(c)** `C = { x ∈ ℝ : x > 5 } = (5, +∞)`

```
inf(C) = 5   (no pertenece a C → no hay mínimo)
sup(C)  no existe (C no está acotado superiormente)
```

### Ejemplo 3 — Inecuación con valor absoluto

Resolver `|2x − 3| < 5` y expresar la solución como intervalo.

```
|2x − 3| < 5
↔   −5 < 2x − 3 < 5      (definición de valor absoluto)
↔   −5 + 3 < 2x < 5 + 3
↔   −2 < 2x < 8
↔   −1 < x < 4
```

Solución: `x ∈ (−1, 4)`.

Verificación: el centro del intervalo es `(−1+4)/2 = 3/2`, que coincide con hacer `2x−3 = 0 → x = 3/2`. El radio es `5/2 = 2.5`. Efectivamente `(3/2 − 5/2, 3/2 + 5/2) = (−1, 4)` ✓

---

## Resumen y tabla de conceptos clave

| Concepto | Definición en palabras | Notación / condición |
|---|---|---|
| Valor absoluto | Distancia al origen | `\|x\| = x` si `x≥0`, `−x` si `x<0` |
| Distancia | Módulo de la diferencia | `d(a,b) = \|a−b\|` |
| Intervalo abierto | Sin extremos | `(a,b)` — `a < x < b` |
| Intervalo cerrado | Con extremos | `[a,b]` — `a ≤ x ≤ b` |
| Entorno | Burbuja de radio δ | `V_δ(x₀) = (x₀−δ, x₀+δ)` |
| Entorno reducido | Entorno sin el centro | `V*_δ(x₀) = V_δ(x₀) − {x₀}` |
| Punto interior | Todo entorno cabe en el conjunto | `∃δ: V_δ(x₀) ⊆ A` |
| Punto frontera | Todo entorno toca dentro y fuera | — |
| Conjunto abierto | Todos los puntos son interiores | — |
| Conjunto cerrado | Contiene todos sus puntos frontera | — |
| Punto de acumulación | Todo entorno reducido toca al conjunto | `∀δ: V*_δ(x₀) ∩ A ≠ ∅` |
| Punto aislado | Algún entorno no toca otros del conjunto | `∃δ: V_δ(x₀) ∩ A = {x₀}` |
| Cota superior | Número que supera todo elemento | `∀x ∈ A: x ≤ M` |
| Supremo | Menor cota superior | `sup(A)` |
| Ínfimo | Mayor cota inferior | `inf(A)` |
| Máximo | Supremo que pertenece al conjunto | `sup(A) ∈ A` |
| Mínimo | Ínfimo que pertenece al conjunto | `inf(A) ∈ A` |

---

## Errores comunes a evitar

1. **Confundir "abierto" con "no cerrado".** Un conjunto puede ser los dos a la vez (∅ y ℝ) o ninguno de los dos (`[a, b)`). La terminología no es la misma que en la vida cotidiana.

2. **Pensar que el supremo siempre pertenece al conjunto.** `sup(0, 1) = 1` pero `1 ∉ (0, 1)`. El supremo es la mejor cota — no tiene por qué ser un elemento del conjunto.

3. **Asumir que todo conjunto acotado tiene máximo.** El conjunto `(0, 1)` está acotado y tiene supremo (= 1), pero no tiene máximo.

4. **Olvidar que el entorno reducido excluye el centro.** `V*_δ(x₀)` cumple `0 < |x − x₀| < δ` — la condición `0 <` (y no `0 ≤`) es lo que excluye a `x₀`. Esto es fundamental para límites.

5. **Confundir punto de acumulación con punto del conjunto.** El límite del intervalo `(1, 4)` — por ejemplo, `x₀ = 1` — es un punto de acumulación aunque no pertenezca al intervalo. En cambio, el `3` aislado de `{3}` pertenece al conjunto pero no es de acumulación.

6. **Aplicar mal la inecuación con valor absoluto.** `|x − a| < δ` se convierte en `a − δ < x < a + δ` (el signo de la desigualdad **no cambia** al quitar el valor absoluto en la forma doble).
