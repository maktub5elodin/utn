# Unidad I — Vectores Geométricos, Recta y Plano

---

## Antes de empezar: escalares vs. vectores

Algunos conceptos físicos quedan completamente descriptos con un número y una unidad: la temperatura de una pieza es 200°C, la masa de un bloque es 5 kg. A esos los llamamos **escalares**.

Otros conceptos necesitan además una **dirección y un sentido**: la velocidad de un auto no es solo "90 km/h", también importa hacia dónde va. La fuerza sobre un perno no es solo "500 N", también importa en qué dirección actúa. Esos son **vectores**.

Un vector en el plano tiene 2 componentes; en el espacio, 3. Lo escribimos como:

```
v = (vx, vy, vz)
```

Geométricamente, es una flecha. El punto de partida es el **origen**, el extremo es la **punta**. Lo que importa de la flecha es su dirección, sentido y longitud — no desde dónde está dibujada.

> **Analogía contable:** un escalar es como el saldo de una cuenta (un número). Un vector es como un asiento contable: tiene magnitud (el importe), dirección (debe/haber) y referencia (a qué cuenta). No alcanza con el número solo.

---

## Parte 1: Operaciones básicas con vectores

### Suma y resta

La suma de dos vectores se hace **componente a componente**:

```
u + v = (ux + vx,  uy + vy,  uz + vz)
```

Geométricamente, es la regla del paralelogramo: colocás el origen de `v` en la punta de `u`, y la suma es la flecha del origen de `u` a la punta de `v`.

```
        v
    ●──────►●
    ↑        ↑
  u |        | u
    |        |
    ●──────►●
        v
         \
          ►  u + v  (diagonal del paralelogramo)
```

La resta `u - v` equivale a sumar `u + (-v)`, donde `-v` invierte el sentido de `v`.

**Propiedades:**
- Conmutativa: `u + v = v + u`
- Asociativa: `(u + v) + w = u + (v + w)`
- Elemento neutro: `u + 0 = u`

---

### Producto de un vector por un escalar

Multiplicar un vector `v` por un escalar `k` escala su longitud:

```
k · v = (k·vx,  k·vy,  k·vz)
```

- Si `k > 0`: mismo sentido, distinta longitud.
- Si `k < 0`: sentido invertido.
- Si `k = 0`: resultado es el vector nulo `(0, 0, 0)`.

---

### Módulo (longitud del vector)

El **módulo** o **norma** de un vector es su longitud. Se calcula con Pitágoras generalizado:

```
|v| = √(vx² + vy² + vz²)
```

En 2D:  `|v| = √(vx² + vy²)`

Un vector con módulo 1 se llama **vector unitario**. Para convertir cualquier vector en unitario:

```
v̂ = v / |v|
```

#### Ejemplo

`v = (3, 4, 0)`

```
|v| = √(3² + 4² + 0²) = √(9 + 16) = √25 = 5

v̂ = (3/5, 4/5, 0) = (0,6 ; 0,8 ; 0)
```

---

## Parte 2: Producto escalar (dot product)

### Definición

El **producto escalar** entre dos vectores da como resultado un **número** (escalar), no un vector. Tiene dos formas equivalentes:

**Forma algebraica:**
```
u · v = ux·vx + uy·vy + uz·vz
```

**Forma geométrica:**
```
u · v = |u| · |v| · cos(θ)
```

donde `θ` es el ángulo entre los dos vectores (0° ≤ θ ≤ 180°).

Las dos fórmulas son iguales. La geométrica es más útil para calcular ángulos; la algebraica para calcular el valor numérico.

---

### Ángulo entre dos vectores

Despejando de la forma geométrica:

```
cos(θ) = (u · v) / (|u| · |v|)
```

**Casos especiales:**
- `u · v = 0` → `cos(θ) = 0` → `θ = 90°` → los vectores son **perpendiculares** (ortogonales).
- `u · v > 0` → ángulo agudo.
- `u · v < 0` → ángulo obtuso.

> **Ojo:** el producto escalar de un vector consigo mismo es `v · v = |v|²`. Esto aparece mucho en fórmulas.

---

### Proyección de un vector sobre otro

La **proyección escalar** de `u` sobre `v` es la "sombra" de `u` en la dirección de `v`:

```
proy escalar = (u · v) / |v|
```

La **proyección vectorial** (el vector en sí, en la dirección de `v`):

```
proy_v(u) = [ (u · v) / |v|² ] · v
```

```
       u
      /|
     / |
    /  |  ← componente perpendicular
   /θ  |
  ●────●──────►  v
   ←──►
  proyección de u sobre v
```

#### Ejemplo

`u = (2, 3, 0)`,  `v = (4, 0, 0)`

```
u · v = 2·4 + 3·0 + 0·0 = 8
|v|² = 16

proy_v(u) = (8/16) · (4, 0, 0) = 0,5 · (4, 0, 0) = (2, 0, 0)
```

La proyección de `u` sobre el eje x es el vector `(2, 0, 0)`. Tiene sentido: `u` tiene componente x = 2.

---

## Parte 2b: Matrices y Regla de Sarrus

### Qué es una matriz

Una **matriz** es una tabla rectangular de números organizados en filas y columnas. Una matriz 3×3 tiene 3 filas y 3 columnas:

```
    ⎡ a  b  c ⎤
A = ⎢ d  e  f ⎥
    ⎣ g  h  i ⎦
```

El **determinante** de una matriz 3×3 es un número que se obtiene combinando sus elementos según una regla fija. Aparece en el cálculo del producto vectorial y del producto mixto.

### Regla de Sarrus

La regla de Sarrus es el truco mnemotécnico para calcular determinantes 3×3 a mano.

**Paso 1:** Escribí la matriz y repetí las dos primeras columnas a la derecha:

```
a  b  c │ a  b
d  e  f │ d  e
g  h  i │ g  h
```

**Paso 2:** Sumá los productos de las tres diagonales que bajan hacia la derecha (↘):

```
↘ 1:  a·e·i
↘ 2:  b·f·g
↘ 3:  c·d·h
```

**Paso 3:** Restá los productos de las tres diagonales que suben hacia la derecha (↗):

```
↗ 1:  c·e·g
↗ 2:  a·f·h
↗ 3:  b·d·i
```

**Resultado:**

```
det(A) = (a·e·i + b·f·g + c·d·h) − (c·e·g + a·f·h + b·d·i)
```

#### Ejemplo con Sarrus

```
| 2  1  3 |
| 0  4  1 |
| 5  2  6 |

Extendida:
2  1  3 │ 2  1
0  4  1 │ 0  4
5  2  6 │ 5  2

↘: 2·4·6 + 1·1·5 + 3·0·2 = 48 + 5 + 0 = 53
↗: 3·4·5 + 2·1·2 + 1·0·6 = 60 + 4 + 0 = 64

det = 53 − 64 = −11
```

> **Nota:** la Regla de Sarrus solo funciona para matrices 3×3. Para 2×2: `det = a·d − b·c`. Para 4×4 en adelante se usan otros métodos.

---

## Parte 3: Producto vectorial (cross product)

### Definición

El **producto vectorial** entre dos vectores da como resultado **otro vector**, perpendicular a ambos. Solo está definido en R³.

```
u × v = | i    j    k   |
        | ux   uy   uz  |
        | vx   vy   vz  |
```

Expandiendo el determinante:

```
u × v = ( uy·vz - uz·vy ,  uz·vx - ux·vz ,  ux·vy - uy·vx )
```

Truco para no confundirse con los signos: la componente i se calcula tapando la fila y columna de i, la j con signo cambiado, la k normal.

---

### Interpretación geométrica

```
|u × v| = |u| · |v| · sin(θ)
```

El módulo del producto vectorial es el **área del paralelogramo** formado por `u` y `v`.

```
    ●──────────►  v
    |            /
    |           /
    |          /
    ●─────────►  u

Área del paralelogramo = |u × v|
```

La **dirección** de `u × v` es perpendicular al plano que forman `u` y `v`. El **sentido** se determina con la **regla de la mano derecha**: apuntás los dedos de `u` hacia `v` doblándolos, y el pulgar indica el sentido de `u × v`.

**Propiedades importantes:**
- `u × v = -(v × u)` → **no** es conmutativo (cambia el sentido).
- `u × u = 0` → el producto vectorial de un vector consigo mismo es el vector nulo.
- Si `u × v = 0` y ninguno es nulo → `u` y `v` son **paralelos** (o antiparalelos).

---

#### Ejemplo

`u = (1, 2, 0)`,  `v = (3, 4, 0)`

```
u × v = ( 2·0 - 0·4 ,  0·3 - 1·0 ,  1·4 - 2·3 )
      = (    0      ,     0      ,   4 - 6    )
      = (0, 0, -2)
```

El resultado apunta en la dirección z negativa (mano derecha, desde (1,2) girando hacia (3,4) en sentido horario en el plano xy → sentido -z).

Área del paralelogramo: `|(0, 0, -2)| = 2`

---

## Parte 4: Producto mixto

### Definición

El **producto mixto** de tres vectores `u`, `v`, `w` es el escalar:

```
u · (v × w)
```

Se calcula como el determinante de la matriz formada con los tres vectores como filas:

```
u · (v × w) = | ux  uy  uz |
              | vx  vy  vz |
              | wx  wy  wz |
```

### Interpretación geométrica

El **valor absoluto** del producto mixto es el **volumen del paralelepípedo** (el "ladrillo" torcido) definido por los tres vectores.

```
          ●─────────►  w
         /|           /|
        / |          / |
       ●──────────►● u |
       |  ●─────────|──►  v
       | /           | /
       |/            |/
       ●─────────────●

Volumen = |u · (v × w)|
```

**Aplicación clave:** si el producto mixto es 0, los tres vectores son **coplanares** (están todos en el mismo plano).

---

#### Ejemplo: ¿son coplanares estos tres vectores?

`u = (1, 2, 3)`,  `v = (0, 1, 2)`,  `w = (2, 3, 4)`

```
| 1  2  3 |
| 0  1  2 | = 1·(1·4 - 2·3) - 2·(0·4 - 2·2) + 3·(0·3 - 1·2)
| 2  3  4 |

= 1·(4 - 6) - 2·(0 - 4) + 3·(0 - 2)
= 1·(-2)  - 2·(-4)  + 3·(-2)
= -2 + 8 - 6
= 0
```

El producto mixto es 0 → los tres vectores son coplanares.

---

## Parte 5: La recta

### Recta en R² (el plano)

En el plano, una recta se puede describir de varias formas equivalentes:

**Ecuación general:**
```
ax + by + c = 0
```

**Ecuación explícita (pendiente-ordenada):**
```
y = m·x + b
```

**Ecuación vectorial paramétrica:**
```
(x, y) = (x₀, y₀) + t·(dx, dy)
```

donde `(x₀, y₀)` es un punto de la recta y `(dx, dy)` es el **vector director** (la dirección de la recta). El parámetro `t` recorre todos los reales.

---

### Recta en R³ (el espacio)

En 3D, una sola ecuación no alcanza para definir una recta (define un plano). Necesitamos un **punto** y una **dirección**.

**Ecuación vectorial:**
```
P = P₀ + t · d
```

donde `P₀ = (x₀, y₀, z₀)` es un punto conocido de la recta, `d = (dx, dy, dz)` es el vector director, y `t ∈ ℝ`.

**Ecuaciones paramétricas** (expandiendo componente a componente):
```
x = x₀ + t·dx
y = y₀ + t·dy
z = z₀ + t·dz
```

**Ecuaciones simétricas** (despejando t de cada una, cuando ninguna componente es cero):
```
(x - x₀)/dx = (y - y₀)/dy = (z - z₀)/dz
```

> **¿Qué pasa si una componente del director es 0?** Por ejemplo, `dz = 0` → la recta es paralela al plano xy → la ecuación simétrica no existe para esa componente; en cambio se escribe `z = z₀` por separado.

---

#### Ejemplo: ecuación de la recta

Punto `P₀ = (1, 2, 3)`, dirección `d = (2, -1, 4)`.

**Vectorial:** `(x, y, z) = (1, 2, 3) + t·(2, -1, 4)`

**Paramétrica:**
```
x = 1 + 2t
y = 2 - t
z = 3 + 4t
```

**Simétrica:**
```
(x - 1)/2 = (y - 2)/(-1) = (z - 3)/4
```

---

### Posiciones relativas entre dos rectas en R³

Dos rectas en el espacio pueden estar en cuatro situaciones:

| Situación | Condición |
|---|---|
| **Coincidentes** | Mismo director (o proporcional) y un punto de una pertenece a la otra |
| **Paralelas** | Mismo director (o proporcional), no coincidentes |
| **Secantes** | Directores no proporcionales, se cortan en un punto |
| **Cruzadas** | Directores no proporcionales, no se cortan (no son paralelas ni secantes) |

Las rectas cruzadas no existen en el plano — es algo exclusivo del espacio 3D.

---

### Recta como intersección de dos planos

Una recta en R³ puede definirse como la intersección de dos planos secantes π₁ y π₂:

```
π₁:  a₁x + b₁y + c₁z + d₁ = 0
π₂:  a₂x + b₂y + c₂z + d₂ = 0
```

**Vector director de la recta:** es perpendicular a las dos normales, por lo tanto:

```
d = n₁ × n₂   donde n₁ = (a₁,b₁,c₁)  y  n₂ = (a₂,b₂,c₂)
```

**Punto de la recta:** se obtiene resolviendo el sistema de dos ecuaciones. El truco práctico es fijar el valor de una de las variables (la que resulte más cómoda) y resolver para las otras dos.

#### Ejemplo

```
π₁:  x + y + z − 1 = 0
π₂:  x − y + z + 1 = 0
```

Director:
```
n₁ = (1, 1, 1)    n₂ = (1, −1, 1)

d = n₁ × n₂ = | i   j   k  |
              | 1   1   1  |
              | 1  −1   1  |

d = ( 1·1−1·(−1),  1·1−1·1,  1·(−1)−1·1 )
  = ( 1+1, 1−1, −1−1 )
  = (2, 0, −2)
```

Punto (fijamos z = 0):
```
x + y = 1
x − y = −1
→ x = 0,  y = 1
```

Punto P₀ = (0, 1, 0). Ecuación vectorial: `(x,y,z) = (0,1,0) + t·(2,0,−2)`

---

## Parte 6: El plano

### Ecuación vectorial del plano

Un plano en R³ queda determinado por:
- Un punto `P₀ = (x₀, y₀, z₀)` del plano.
- Un vector **normal** `n = (a, b, c)`, perpendicular al plano.

La ecuación vectorial dice: cualquier punto `P = (x, y, z)` del plano cumple que el vector `P - P₀` es perpendicular a `n`:

```
(P - P₀) · n = 0
```

```
           n (normal al plano)
           ↑
           |
    ───────●─────────
           P₀
    ────────────────── ← Plano
```

### Ecuación general del plano

Expandiendo el producto escalar:

```
a·(x - x₀) + b·(y - y₀) + c·(z - z₀) = 0
```

Que se reordena en la **ecuación general**:

```
ax + by + cz + d = 0
```

donde `d = -(a·x₀ + b·y₀ + c·z₀)`.

> **Clave:** los coeficientes `(a, b, c)` de la ecuación general son siempre las componentes del vector normal al plano.

---

### Cómo obtener la ecuación del plano en distintas situaciones

**Dado un punto y un vector normal:**
Usás directamente la ecuación vectorial `(P - P₀) · n = 0`.

**Dado un punto y dos vectores directores del plano:**
El vector normal se obtiene como el producto vectorial de los dos directores:
```
n = u × v
```
Luego usás el punto y la normal como arriba.

**Dados tres puntos (no colineales):**
Con los tres puntos `A`, `B`, `C`:
1. Formás dos vectores: `u = B - A` y `v = C - A`.
2. Normal: `n = u × v`.
3. Ecuación: `(P - A) · n = 0`.

---

#### Ejemplo: plano por tres puntos

`A = (1, 0, 0)`,  `B = (0, 1, 0)`,  `C = (0, 0, 1)`

**Paso 1:** vectores en el plano:
```
u = B - A = (-1, 1, 0)
v = C - A = (-1, 0, 1)
```

**Paso 2:** normal:
```
n = u × v = | i   j   k  |
            |-1   1   0  |
            |-1   0   1  |

n = ( 1·1 - 0·0 ,  0·(-1) - (-1)·1 ,  (-1)·0 - 1·(-1) )
  = (   1       ,      0 + 1        ,      0 + 1        )
  = (1, 1, 1)
```

**Paso 3:** ecuación con punto A = (1, 0, 0):
```
1·(x - 1) + 1·(y - 0) + 1·(z - 0) = 0
x - 1 + y + z = 0
x + y + z = 1
```

Es el plano que corta los tres ejes en el punto (1,0,0), (0,1,0) y (0,0,1). Tiene lógica.

---

### Posiciones relativas entre planos

Dos planos con normales `n₁ = (a₁, b₁, c₁)` y `n₂ = (a₂, b₂, c₂)`:

| Situación | Condición |
|---|---|
| **Coincidentes** | `n₁` paralela a `n₂` y un punto de uno pertenece al otro |
| **Paralelos** | `n₁` paralela a `n₂` (proporcionales), no coincidentes |
| **Secantes** | `n₁` no proporcional a `n₂` → se intersecan en una recta |

Dos planos **perpendiculares** tienen normales con producto escalar cero: `n₁ · n₂ = 0`.

---

### Procedimiento: de ecuación general a ecuación vectorial del plano

Dada la ecuación general `ax + by + cz + d = 0`, para obtener la forma vectorial `P = P₀ + s·u + t·v`:

**Paso 1 — Identificar la normal:** `n = (a, b, c)`

**Paso 2 — Encontrar un punto P₀ del plano:** fijar dos coordenadas en 0 y resolver para la tercera (eligiendo la que tenga coeficiente ≠ 0).

```
Si c ≠ 0: fijar x=0, y=0 → z = −d/c → P₀ = (0, 0, −d/c)
Si b ≠ 0: fijar x=0, z=0 → y = −d/b → P₀ = (0, −d/b, 0)
Si a ≠ 0: fijar y=0, z=0 → x = −d/a → P₀ = (−d/a, 0, 0)
```

**Paso 3 — Encontrar dos vectores directores del plano:** deben ser perpendiculares a `n` y linealmente independientes entre sí. Una forma sistemática: tomar cualquier vector `e` no paralelo a `n` y hacer `u = n × e`. Luego `v = n × u`.

Método alternativo más rápido: encontrar dos puntos más del plano (P₁ y P₂) y calcular `u = P₁ − P₀` y `v = P₂ − P₀`.

**Paso 4 — Escribir la ecuación vectorial paramétrica:**

`P = P₀ + s·u + t·v`    con s, t ∈ ℝ

#### Ejemplo

Plano: `2x − y + 3z − 6 = 0`

```
Paso 1: n = (2, −1, 3)

Paso 2: fijar x=0, y=0 → 3z = 6 → z = 2  →  P₀ = (0, 0, 2)

Paso 3: dos puntos más:
  fijar x=3, y=0: 6 + 3z = 6 → z = 0  →  P₁ = (3, 0, 0)
  fijar x=0, y=−6: 6 + 3z = 6 → z = 0  → P₂ = (0, 6, 0)  [check: 2·0−(−6)+0=6 ✓]

  u = P₁ − P₀ = (3, 0, −2)
  v = P₂ − P₀ = (0, 6, −2)

Paso 4: P = (0, 0, 2) + s·(3, 0, −2) + t·(0, 6, −2)
```

---

### Planos particulares

#### Plano que pasa por el origen

Si el plano pasa por O = (0, 0, 0), al sustituir: `a·0 + b·0 + c·0 + d = 0` → `d = 0`.

**Forma:** `ax + by + cz = 0`

Todo plano con término independiente nulo pasa por el origen.

#### Planos coordenados

Son los tres planos definidos por los ejes coordenados:

```
Plano xy:  z = 0   →  normal n = (0, 0, 1)  (eje z)
Plano xz:  y = 0   →  normal n = (0, 1, 0)  (eje y)
Plano yz:  x = 0   →  normal n = (1, 0, 0)  (eje x)
```

```
          z
          |
          |   Plano xz (y=0)
          |  /
          | /
──────────●──────────── y
         /|
        / |   Plano xy (z=0)
       /  |
      x   Plano yz (x=0)
```

#### Planos paralelos a los planos coordenados

Un plano paralelo a xy tiene la misma normal (0,0,1), solo cambia d:

```
Paralelo a xy:  z = k   (solo tiene componente z)
Paralelo a xz:  y = k   (solo tiene componente y)
Paralelo a yz:  x = k   (solo tiene componente x)
```

Todos pasan por el plano coordenado correspondiente cuando k = 0.

#### Planos paralelos a un eje de coordenadas

Un plano es paralelo a un eje cuando su normal es perpendicular a ese eje, es decir, cuando el coeficiente de ese eje en la ecuación es **cero**:

```
Paralelo al eje x:  a = 0  →  by + cz + d = 0   (no depende de x)
Paralelo al eje y:  b = 0  →  ax + cz + d = 0   (no depende de y)
Paralelo al eje z:  c = 0  →  ax + by + d = 0   (no depende de z)
```

> **Regla práctica:** el coeficiente que falta es el del eje al que el plano es paralelo. Si en la ecuación no aparece `x`, el plano es paralelo al eje x.

Tabla resumen:

| Tipo de plano | Forma de la ecuación | Ejemplo |
|---|---|---|
| Por el origen | `ax + by + cz = 0` | `2x − y + z = 0` |
| Plano xy | `z = 0` | — |
| Plano xz | `y = 0` | — |
| Plano yz | `x = 0` | — |
| Paralelo a xy | `z = k` | `z = 5` |
| Paralelo a xz | `y = k` | `y = −3` |
| Paralelo a yz | `x = k` | `x = 2` |
| Paralelo al eje x | `by + cz + d = 0` | `y + 2z − 1 = 0` |
| Paralelo al eje y | `ax + cz + d = 0` | `3x − z + 4 = 0` |
| Paralelo al eje z | `ax + by + d = 0` | `x + y − 2 = 0` |

---

### Posiciones relativas entre plano y recta

Dado el plano `π: ax + by + cz + d = 0` con normal `n = (a, b, c)`, y la recta con vector director `r = (rx, ry, rz)` y punto P₀.

Calcular `r · n`:

```
r · n = 0  →  r ⊥ n  →  r es paralelo al plano
                           ┌ P₀ ∈ π  →  recta CONTENIDA en el plano
                           └ P₀ ∉ π  →  recta PARALELA (sin intersección)

r · n ≠ 0  →  r no es paralelo al plano  →  recta SECANTE (corta en un punto)
```

**Para encontrar el punto de intersección** (caso secante): sustituir las ecuaciones paramétricas de la recta en la ecuación del plano y despejar t:

```
a(x₀ + t·rx) + b(y₀ + t·ry) + c(z₀ + t·rz) + d = 0
→ despejar t
→ sustituir t en las paramétricas → punto de intersección
```

#### Ejemplo

Plano: `x + y + z − 3 = 0`.  Recta: P₀ = (1, 0, 0), r = (1, 1, 1).

```
r · n = (1,1,1)·(1,1,1) = 3 ≠ 0  →  secante

Paramétricas: x = 1+t, y = t, z = t

Sustituir en el plano:
(1+t) + t + t − 3 = 0
1 + 3t − 3 = 0
3t = 2  →  t = 2/3

Punto: x = 1+2/3 = 5/3,  y = 2/3,  z = 2/3
```

---

### Haz de planos

Un **haz de planos** es el conjunto de todos los planos que contienen a una recta dada (llamada **charnela** o eje del haz).

Si la charnela es la intersección de dos planos `π₁` y `π₂`:

```
π₁:  a₁x + b₁y + c₁z + d₁ = 0
π₂:  a₂x + b₂y + c₂z + d₂ = 0
```

**Ecuación general del haz:**

```
π₁ + λ·π₂ = 0    (λ ∈ ℝ)
```

Desarrollada:

```
(a₁ + λa₂)x + (b₁ + λb₂)y + (c₁ + λc₂)z + (d₁ + λd₂) = 0
```

Para cada valor de λ se obtiene un plano distinto que pasa por la charnela. El plano π₁ corresponde a λ = 0; π₂ no se obtiene directamente (requeriría λ → ∞, por eso a veces se usa la forma `λ·π₁ + π₂ = 0`).

**Uso típico:** encontrar el plano del haz que cumple una condición adicional (pasa por un punto dado, es perpendicular a otro plano, etc.) — se impone la condición y se despeja λ.

> **Nota sobre la "forma reducida":** el profesor mencionó que no la usa mucho. Es la forma en que se toma uno de los dos planos como referencia y se parametriza el haz con un solo parámetro libre. En la práctica, la ecuación `π₁ + λ·π₂ = 0` ya es la forma estándar de trabajo.

#### Ejemplo

Charnela: intersección de `π₁: x + y − 1 = 0` y `π₂: y + z − 2 = 0`.

Ecuación del haz: `(x + y − 1) + λ(y + z − 2) = 0`

Encontrar el plano del haz que pasa por P = (0, 0, 3):

```
(0 + 0 − 1) + λ(0 + 3 − 2) = 0
−1 + λ·1 = 0  →  λ = 1

Plano: (x + y − 1) + (y + z − 2) = 0
        x + 2y + z − 3 = 0
```

---

## Parte 7: Distancias y ángulos

### Ángulo entre dos planos

El ángulo entre dos planos es el ángulo entre sus normales (o su suplemento, se toma el agudo):

```
cos(θ) = |n₁ · n₂| / (|n₁| · |n₂|)
```

### Ángulo entre dos rectas

Se toma el ángulo entre sus vectores directores:

```
cos(θ) = |d₁ · d₂| / (|d₁| · |d₂|)
```

### Ángulo entre recta y plano

Complementario al ángulo entre el director de la recta y la normal al plano:

```
sin(θ) = |d · n| / (|d| · |n|)
```

---

### Distancia de un punto a un plano

Dado el plano `ax + by + cz + d = 0` y el punto `Q = (x₀, y₀, z₀)`:

```
dist(Q, plano) = |a·x₀ + b·y₀ + c·z₀ + d| / √(a² + b² + c²)
```

> **Regla práctica:** sustituís las coordenadas del punto en la ecuación del plano, tomás valor absoluto y dividís por el módulo de la normal.

#### Ejemplo

Plano: `2x - y + 2z - 3 = 0`. Punto: `Q = (1, 1, 1)`.

```
dist = |2·1 - 1·1 + 2·1 - 3| / √(4 + 1 + 4)
     = |2 - 1 + 2 - 3| / √9
     = |0| / 3
     = 0
```

El punto está en el plano (resultado 0). Tiene sentido verificarlo: `2(1) - 1 + 2(1) - 3 = 0` ✓

---

### Distancia entre dos planos paralelos

Dos planos son paralelos cuando sus normales son proporcionales. Si los coeficientes `(a, b, c)` ya están igualados (mismo vector normal), la distancia es:

```
π₁:  ax + by + cz + d₁ = 0
π₂:  ax + by + cz + d₂ = 0

dist(π₁, π₂) = |d₁ − d₂| / √(a² + b² + c²)
```

Si los coeficientes no son iguales (son proporcionales pero no idénticos), hay que normalizar primero dividiendo una ecuación por su factor de proporcionalidad.

**Método alternativo siempre válido:** tomar cualquier punto P₀ de π₁ y calcular su distancia a π₂.

#### Ejemplo

`π₁: 2x − y + 2z + 3 = 0`  y  `π₂: 2x − y + 2z − 9 = 0`

```
Misma normal (2, −1, 2). d₁ = 3, d₂ = −9.

dist = |3 − (−9)| / √(4 + 1 + 4)
     = 12 / √9
     = 12 / 3
     = 4
```

---

### Distancia de un punto a una recta

Dada la recta con punto `P₀` y director `d`, y el punto externo `Q`:

```
dist(Q, recta) = |(Q - P₀) × d| / |d|
```

El vector `Q - P₀` va del punto base de la recta al punto externo. El módulo del producto vectorial dividido por el módulo del director da la distancia perpendicular.

---

### Distancia entre dos rectas paralelas

Si `d₁ ∥ d₂`, tomás un punto `P₁` de la primera recta y calculás su distancia a la segunda:

```
dist = |(P₁ - P₂) × d| / |d|
```

### Distancia entre dos rectas cruzadas

```
dist = |( P₁ - P₂) · (d₁ × d₂)| / |d₁ × d₂|
```

---

## Resumen de fórmulas

| Concepto | Fórmula |
|---|---|
| Módulo | `` `\|v\| = √(vx² + vy² + vz²)` `` |
| Vector unitario | `v̂ = v / \|v\|` |
| Producto escalar | `u · v = ux·vx + uy·vy + uz·vz = \|u\|·\|v\|·cos(θ)` |
| Ángulo entre vectores | `cos(θ) = (u·v) / (\|u\|·\|v\|)` |
| Proyección vectorial | `proy_v(u) = [(u·v) / \|v\|²] · v` |
| Producto vectorial | `u × v = (uy·vz−uz·vy , uz·vx−ux·vz , ux·vy−uy·vx)` |
| Área paralelogramo | `\|u × v\| = \|u\|·\|v\|·sin(θ)` |
| Producto mixto | `u·(v×w) = det([u;v;w])` |
| Volumen paralelepípedo | `\|u·(v×w)\|` |
| Ecuación del plano | `a(x−x₀) + b(y−y₀) + c(z−z₀) = 0` |
| Normal al plano `ax+by+cz+d=0` | `n = (a, b, c)` |
| Recta paramétrica | `x=x₀+t·dx, y=y₀+t·dy, z=z₀+t·dz` |
| Recta simétrica | `(x−x₀)/dx = (y−y₀)/dy = (z−z₀)/dz` |
| Dist. punto a plano | `\|ax₀+by₀+cz₀+d\| / √(a²+b²+c²)` |
| Dist. planos paralelos | `\|d₁−d₂\| / √(a²+b²+c²)` |
| Dist. punto a recta | `\|(Q−P₀)×d\| / \|d\|` |
| Dist. rectas cruzadas | `\|(P₁−P₂)·(d₁×d₂)\| / \|d₁×d₂\|` |
| Ángulo entre planos | `cos(θ) = \|n₁·n₂\| / (\|n₁\|·\|n₂\|)` |
| Det. 3×3 (Sarrus) | `(aei+bfg+cdh) − (ceg+afh+bdi)` |
| Director recta (intersec. planos) | `d = n₁ × n₂` |
| Haz de planos | `π₁ + λ·π₂ = 0` |
| Recta ∥ plano | `r · n = 0` (y P₀ ∉ π) |
| Recta contenida en plano | `r · n = 0` (y P₀ ∈ π) |
| Recta secante al plano | `r · n ≠ 0` |

---

## Errores comunes a evitar

1. **Confundir producto escalar con vectorial.** El escalar da un número; el vectorial da un vector. Usarlos al revés lleva a errores de tipo (estás tratando de igualar un vector con un número).

2. **Olvidar que el producto vectorial no es conmutativo.** `u × v = -(v × u)`. El orden importa y cambia el sentido del resultado.

3. **Confundir vector normal con vector director del plano.** El vector normal es perpendicular al plano. Los vectores directores están contenidos en él. Son cosas opuestas.

4. **No verificar si los vectores son paralelos antes de calcular el producto vectorial.** Si son paralelos, `u × v = 0`, y no hay normal definida — señal de que los datos del problema pueden estar mal (por ejemplo, los tres puntos son colineales).

5. **En la distancia punto-plano, olvidar el valor absoluto.** La fórmula tiene `|...|`; sin él el resultado puede dar negativo, que geométricamente no tiene sentido.

6. **En la recta simétrica, dividir por cero.** Si una componente del director es 0, esa ecuación simétrica no existe: se reemplaza por la ecuación `variable = constante`.

7. **Confundir "recta en el plano xy" con "recta en R³ con z=0".** Son equivalentes, pero la representación y las fórmulas de distancias cambian.

8. **En la Regla de Sarrus, mezclar las diagonales.** Las tres ↘ se suman, las tres ↗ se restan. Invertir el signo da un resultado con signo cambiado — error clásico en producto mixto.

9. **Concluir paralelismo plano-recta sin verificar si la recta está contenida.** Si `r · n = 0`, hay que verificar también si el punto de la recta pertenece al plano. Son dos casos distintos: paralela o contenida.

10. **En planos particulares, confundir "paralelo al eje x" con "paralelo al plano yz".** Un plano paralelo al eje x tiene a = 0. Un plano paralelo al plano yz tiene normal proporcional a (1,0,0), es decir, tiene forma `x = k`. Son situaciones opuestas.

11. **En el haz de planos, creer que λ = 0 da π₂.** Cuando λ = 0 se obtiene π₁. El plano π₂ no se obtiene directamente con la forma `π₁ + λ·π₂ = 0` — requeriría λ → ∞.

12. **Al pasar de ecuación general a vectorial, tomar un solo vector director.** Se necesitan dos vectores directores linealmente independientes para parametrizar un plano (un solo director define una recta, no un plano).
