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
| Dist. punto a recta | `\|(Q−P₀)×d\| / \|d\|` |
| Dist. rectas cruzadas | `\|(P₁−P₂)·(d₁×d₂)\| / \|d₁×d₂\|` |
| Ángulo entre planos | `cos(θ) = \|n₁·n₂\| / (\|n₁\|·\|n₂\|)` |

---

## Errores comunes a evitar

1. **Confundir producto escalar con vectorial.** El escalar da un número; el vectorial da un vector. Usarlos al revés lleva a errores de tipo (estás tratando de igualar un vector con un número).

2. **Olvidar que el producto vectorial no es conmutativo.** `u × v = -(v × u)`. El orden importa y cambia el sentido del resultado.

3. **Confundir vector normal con vector director del plano.** El vector normal es perpendicular al plano. Los vectores directores están contenidos en él. Son cosas opuestas.

4. **No verificar si los vectores son paralelos antes de calcular el producto vectorial.** Si son paralelos, `u × v = 0`, y no hay normal definida — señal de que los datos del problema pueden estar mal (por ejemplo, los tres puntos son colineales).

5. **En la distancia punto-plano, olvidar el valor absoluto.** La fórmula tiene `|...|`; sin él el resultado puede dar negativo, que geométricamente no tiene sentido.

6. **En la recta simétrica, dividir por cero.** Si una componente del director es 0, esa ecuación simétrica no existe: se reemplaza por la ecuación `variable = constante`.

7. **Confundir "recta en el plano xy" con "recta en R³ con z=0".** Son equivalentes, pero la representación y las fórmulas de distancias cambian.
