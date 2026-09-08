# Trabajo Práctico N°5 — Resorte

**Materia:** Física I — U.D.B. Física  
**Curso:** A1193 | **Turno:** Noche | **Grupo N°5**

**Integrantes presentes:**

| Apellido | Nombre |
|---|---|
| Fleitas | Facundo |
| Gonzalez | Federico |
| Lissi | Lucas |
| Palazzo | Juan |
| Paredes | Sergio |
| Perez | Lautaro |

**Profesor/a de la materia:** Prof. Vella  
**Jefe de Trabajos Prácticos (JTP):** Ing. Pella, Martín  
**Asistentes de Trabajos Prácticos (ATP):** Ing. Lasala, José — Ing. Quevedo, Rubén — Ing. Smoisman, Sergio

---

## 1. Introducción

### 1.1 Objetivos

1. Determinar la constante elástica `k` del resorte por dos métodos independientes: el **dinámico** (a partir del período de oscilación del sistema masa-resorte) y el **estático** (a partir de la ley de Hooke y el estiramiento producido por una carga conocida).
2. Determinar el período `T` y la frecuencia `f` de oscilación del sistema masa-resorte.
3. Comparar los valores de `k` obtenidos por ambos métodos.

### 1.2 Marco teórico

**Método dinámico — oscilación del sistema masa-resorte**

Una masa `m` unida a un resorte y apartada una distancia `x` de su posición de equilibrio recibe una fuerza recuperadora dada por la ley de Hooke, `fₑ = −k·x` (el signo menos indica que se opone al desplazamiento). Aplicando la segunda ley de Newton en la dirección del movimiento:

`ΣFₓ = m·aₓ   →   −k·x = m·(d²x/dt²)   →   d²x/dt² = −(k/m)·x`

Esta es la ecuación de un movimiento oscilatorio armónico, `d²x/dt² = −ω²·x`, con pulsación `ω² = k/m`. Como además `ω = 2π/T` (una oscilación completa equivale a `2π` rad de fase), igualando ambas expresiones:

`4π²/T² = k/m   →   T = 2π·√(m/k)   →   k = 4π²·m / T²`

Esta última es la ecuación de trabajo del método dinámico: `k` se obtiene de una sola medición del período y de la masa oscilante. El período `T` es el tiempo de una oscilación completa; la frecuencia es su inversa, `f = 1/T`, en hertz (`Hz = 1/s`).

Para el resorte en posición **vertical**, colgar la masa solo desplaza la posición de equilibrio (el resorte se estira hasta que `k·d = m·g`); medida desde ese nuevo equilibrio, la fuerza recuperadora sigue siendo `−k·x`, por lo que el período y `k` son los mismos que en el caso horizontal.

**Método estático — ley de Hooke**

Con la masa colgada y en reposo en la nueva posición de equilibrio, la fuerza elástica equilibra al peso:

`k·Δx = m·g   →   k = m·g / Δx`

donde `Δx` es el estiramiento del resorte entre la posición sin carga y la posición con la carga `m`. Este método no involucra el tiempo: `k` se obtiene de una medición de longitud y una de masa.

**Medición de varias oscilaciones (método dinámico)**

El error dominante del cronómetro manual es el tiempo de reacción del operador al arrancarlo y detenerlo (`≈ 0,1–0,2 s`), muy superior a su resolución (`0,01 s`). Cronometrando `N = 10` oscilaciones y dividiendo el tiempo por 10, ese error —que se comete una sola vez— queda dividido por 10, reduciendo en el mismo factor el error relativo del período individual.

**Mediciones repetidas**

El tiempo de 10 oscilaciones se mide varias veces. Se adopta como valor representativo el promedio de las mediciones, y como incerteza la dispersión de esas repeticiones, que es menor que la de una medición aislada porque el promedio filtra las fluctuaciones al azar.

**Propagación de incertezas**

Para un producto o cociente de potencias, los errores relativos se suman pesados por el valor absoluto del exponente:

- Método dinámico: `k = 4π²·m·T⁻²`   →   `ε_k = ε_m + 2·ε_T`  (el exponente `−2` duplica el error relativo del período).
- Método estático: `k = m·g·Δx⁻¹`   →   `ε_k = ε_m + ε_(Δx)`  (`g` es un valor constante, sin incerteza).

En ambos casos `Δk = ε_k · k`.

---

## 2. Procedimiento Experimental

### 2.1 Objeto de estudio

Un resorte helicoidal de acero suspendido de un soporte fijo por su extremo superior, y un conjunto de pesas de masa total `m` colgado del extremo inferior. Se determinó `k` por dos métodos sobre la misma configuración: dinámico (oscilación vertical del sistema masa-resorte) y estático (medición del estiramiento del resorte bajo la carga).

### 2.2 Instrumentos utilizados e incertezas adoptadas

| Instrumento | Magnitud medida | Resolución | Error absoluto adoptado |
|---|---|---|---|
| Balanza | Masa del conjunto de pesas | — | `Δm = ±0,01 kg` (apreciación de la balanza) |
| Cronómetro digital | Tiempo de 10 oscilaciones | 0,01 s | `Δt = ±0,3 s` (dispersión de 5 mediciones repetidas, promediadas) |
| Regla milimetrada | Estiramiento del resorte `Δx` | 1 mm | `Δ(Δx) = ±3 mm` (tres veces la apreciación de la regla) |

*Pie de tabla: La incerteza del tiempo no se toma de la resolución del cronómetro (0,01 s) sino de la dispersión de las mediciones repetidas, ya que la fuente de error dominante es el tiempo de reacción del operador (≈ 0,1–0,2 s). Para `Δx` no se adopta la apreciación de la regla sino el triple, porque el estiramiento surge de comparar dos posiciones del extremo del resorte que no quedan nítidamente definidas (extremo libre sin carga y posición de reposo con carga).*

### 2.3 Método dinámico — oscilación

1. Se pesó el conjunto de pesas: `m = (0,112 ± 0,01) kg`.
2. Se colgó el conjunto del extremo libre del resorte y se dejó alcanzar el equilibrio.
3. Se apartó la masa una pequeña distancia hacia abajo respecto del equilibrio y se la soltó sin impulso inicial.
4. Se midió con cronómetro el tiempo de **10 oscilaciones completas**, repitiendo la medición **5 veces** en idénticas condiciones.
5. El período se obtuvo dividiendo el tiempo promedio por 10; la constante elástica, con `k = 4π²·m/T²`.

### 2.4 Método estático — ley de Hooke

1. Con el resorte descargado, se registró la posición de su extremo libre (posición de referencia).
2. Se colgó la misma masa `m = (0,112 ± 0,01) kg` y, alcanzado el reposo, se registró la nueva posición del extremo.
3. El estiramiento es la diferencia entre ambas posiciones: `Δx = (30,5 ± 0,3) cm = (0,305 ± 0,003) m`.
4. La constante elástica se calculó con `k = m·g/Δx`, adoptando `g = 9,797 m/s²` (valor indicado por la cátedra, tomado como constante sin incerteza).

---

## 3. Resultados y Análisis

### 3.1 Mediciones de tiempo (método dinámico)

**Tabla 1.** Tiempo de 10 oscilaciones completas del sistema masa-resorte.

| Medición `i` | `tᵢ` — tiempo de 10 oscilaciones (s) |
|---|---|
| 1 | 10,70 |
| 2 | 9,70 |
| 3 | 11,00 |
| 4 | 9,63 |
| 5 | 10,82 |

*Tabla 1: Tiempos medidos con cronómetro digital para 10 oscilaciones completas, con masa colgante `(0,112 ± 0,01) kg`. Las 5 repeticiones se realizaron en condiciones idénticas.*

Promedio de las cinco mediciones: `t̄ = 10,37 s`. A partir de la dispersión de las mediciones repetidas se adoptó una incerteza de `±0,3 s` para el promedio.

> **`t₁₀ = (10,4 ± 0,3) s`** — tiempo de 10 oscilaciones

### 3.2 Período y frecuencia

El conteo de `N = 10` oscilaciones es un número exacto, sin incerteza. Al dividir por él, el valor y su error absoluto se dividen por 10 y el error relativo se conserva.

`T = t̄ / 10 = 10,37 / 10 = 1,037 s`

`ΔT = Δt / 10 = 0,3 / 10 = 0,03 s`   →   `ε_T = ΔT/T = 2,9 %`

> **`T = (1,04 ± 0,03) s`**

Para la frecuencia, como `f = T⁻¹`, su error relativo es igual al del período:

`f = 1 / T = 1 / 1,037 = 0,964 Hz`

`Δf = ε_T · f = 0,029 · 0,964 = 0,028 Hz`

> **`f = (0,96 ± 0,03) Hz`**

La frecuencia se expresa en **hertz (Hz)**, unidad equivalente a `1/s`: `f ≈ 0,96 Hz` significa aproximadamente una oscilación por segundo, coherente con un período de `≈ 1,04 s`.

### 3.3 Constante elástica — método dinámico

Aplicando la ecuación de trabajo con `m = 0,112 kg` y `T = 1,037 s`:

`k = 4π² · m / T² = 39,478 · 0,112 / (1,037)² = 4,422 / 1,075 = 4,11 N/m`

**Propagación de la incerteza** (`k = 4π²·m·T⁻²`, con `4π²` constante):

`ε_m = Δm / m = 0,01 / 0,112 = 0,089 = 8,9 %`

`ε_T = ΔT / T = 0,03 / 1,037 = 0,029 = 2,9 %`

`ε_k = ε_m + 2·ε_T = 0,089 + 2·0,029 = 0,089 + 0,058 = 0,147 = 14,7 %`

`Δk = ε_k · k = 0,147 · 4,11 = 0,6 N/m`

> **`k_din = (4,1 ± 0,6) N/m`**  
> Intervalo: `[3,5 ; 4,7] N/m`

**Verificación por vía independiente:** a partir de la pulsación `ω = 2π/T = 6,06 rad/s` y de `ω² = k/m` se obtiene `k = ω²·m = (6,06)²·0,112 = 4,11 N/m`, que coincide con el cálculo directo.

### 3.4 Constante elástica — método estático

Aplicando la ley de Hooke con `m = 0,112 kg`, `Δx = 0,305 m` y `g = 9,797 m/s²`:

`k = m · g / Δx = 0,112 · 9,797 / 0,305 = 1,097 / 0,305 = 3,60 N/m`

**Propagación de la incerteza** (`k = m·g·Δx⁻¹`, con `g` constante):

`ε_m = Δm / m = 0,01 / 0,112 = 0,089 = 8,9 %`

`ε_(Δx) = Δ(Δx) / Δx = 0,003 / 0,305 = 0,010 = 1,0 %`

`ε_k = ε_m + ε_(Δx) = 0,089 + 0,010 = 0,099 = 9,9 %`

`Δk = ε_k · k = 0,099 · 3,60 = 0,4 N/m`

> **`k_est = (3,6 ± 0,4) N/m`**  
> Intervalo: `[3,2 ; 4,0] N/m`

### 3.5 Comparación de los dos métodos

**Tabla 2.** Constante elástica del resorte obtenida por cada método.

| Método | `k` (N/m) | `Δk` (N/m) | `ε_k` | Intervalo (N/m) |
|---|---|---|---|---|
| Dinámico (`4π²·m/T²`) | 4,1 | 0,6 | 15 % | [3,5 ; 4,7] |
| Estático (`m·g/Δx`) | 3,6 | 0,4 | 10 % | [3,2 ; 4,0] |

*Tabla 2: Los dos métodos determinan la misma magnitud física a partir de mediciones distintas —período y masa en un caso, estiramiento y masa en el otro—.*

Los intervalos `[3,5 ; 4,7]` (dinámico) y `[3,2 ; 4,0]` (estático) se superponen en `[3,5 ; 4,0] N/m`: **los dos resultados son compatibles** dentro de las incertezas. La diferencia entre los valores representativos, `|4,11 − 3,60| = 0,5 N/m`, es menor que la incerteza combinada `√(0,6² + 0,4²) = 0,7 N/m`, de modo que no es significativa.

El método estático resulta algo más preciso en términos absolutos (`± 0,4` frente a `± 0,6`). El método dinámico arrastra una incerteza mayor porque el período interviene al cuadrado en `k = 4π²·m/T²`: su error relativo (`2,9 %`) se duplica al propagarse (`5,8 %`). Las incertezas relativas de ambos resultados (`10–15 %`) quedan gobernadas por la apreciación con que se midieron la masa, el tiempo y el estiramiento, y son razonables para las condiciones del experimento.

---

## 4. Conclusiones

**Objetivo 1 — Constante elástica por dos métodos:**  
- Método dinámico (oscilación): `k_din = (4,1 ± 0,6) N/m`, a partir del período `T = (1,04 ± 0,03) s` y la masa `(0,112 ± 0,01) kg`. Verificado por dos vías (`4π²·m/T²` y `ω²·m`), que coincidieron.
- Método estático (ley de Hooke): `k_est = (3,6 ± 0,4) N/m`, a partir del estiramiento `Δx = (30,5 ± 0,3) cm` bajo la misma carga y `g = 9,797 m/s²`.

**Objetivo 2 — Período y frecuencia:**  
`T = (1,04 ± 0,03) s` y `f = (0,96 ± 0,03) Hz`. Cronometrar 10 oscilaciones en lugar de 1 y promediar 5 repeticiones redujo el error relativo del período hasta `≈ 3 %`.

**Objetivo 3 — Comparación:**  
Los intervalos de ambos métodos se superponen en `[3,5 ; 4,0] N/m`: los resultados son compatibles, y la diferencia entre sus valores representativos (`0,5 N/m`) no es significativa frente a la incerteza combinada (`0,7 N/m`). El método dinámico presenta una incerteza algo mayor porque el período interviene al cuadrado en la fórmula de `k`, lo que duplica su error relativo al propagarse. Ambas determinaciones son consistentes con una constante elástica del orden de `k ≈ 3,6–4,1 N/m`.

---

## Anexo de Cálculos

### A.1 Tiempo, período y frecuencia

```
Mediciones del tiempo de 10 oscilaciones (s):
  10,70 ; 9,70 ; 11,00 ; 9,63 ; 10,82

Promedio:
  t̄ = (10,70 + 9,70 + 11,00 + 9,63 + 10,82) / 5 = 51,85 / 5 = 10,37 s

Incerteza adoptada para el promedio (dispersión de las 5 repeticiones):
  Δt = 0,3 s

Período  (N = 10 oscilaciones, número exacto de conteo):
  T   = t̄ / N = 10,37 / 10 = 1,037 s
  ΔT  = Δt / N = 0,3 / 10   = 0,03 s
  ε_T = ΔT / T = 0,03 / 1,037 = 0,029 = 2,9 %

  Redondeo:  ΔT → 0,03 s ; T → 1,04 s
  Resultado:  T = (1,04 ± 0,03) s

Frecuencia:
  f = 1 / T = 1 / 1,037 = 0,9643 Hz
  Como f = T⁻¹  →  ε_f = ε_T = 2,9 %
  Δf = ε_f · f = 0,029 · 0,9643 = 0,028 Hz

  Redondeo:  Δf → 0,03 Hz ; f → 0,96 Hz
  Resultado:  f = (0,96 ± 0,03) Hz

Verificación cruzada (pulsación):
  ω = 2π / T = 6,2832 / 1,037 = 6,06 rad/s
  k = ω² · m = (6,06)² · 0,112 = 36,7 · 0,112 = 4,11 N/m   ✓ (coincide con A.2)
```

### A.2 Constante elástica — método dinámico

```
Datos:
  m = (0,112 ± 0,01) kg      →  ε_m = 0,01 / 0,112 = 0,089 = 8,9 %
  T = (1,037 ± 0,03) s       →  ε_T = 0,03 / 1,037 = 0,029 = 2,9 %

Valor representativo:
  4π² = 39,478
  k = 4π² · m / T² = 39,478 · 0,112 / (1,037)²
    = 4,4216 / 1,0754 = 4,11 N/m

Propagación (k = 4π² · m · T⁻² ; 4π² constante):
  ε_k = |+1|·ε_m + |−2|·ε_T = ε_m + 2·ε_T
      = 0,089 + 2·0,029
      = 0,089 + 0,058
      = 0,147 = 14,7 %
  Δk  = ε_k · k = 0,147 · 4,11 = 0,60 N/m

  Redondeo:  Δk → 0,6 ; k → 4,1
  Resultado:  k_din = (4,1 ± 0,6) N/m      Intervalo: [3,5 ; 4,7] N/m
```

### A.3 Constante elástica — método estático

```
Datos:
  m  = (0,112 ± 0,01) kg     →  ε_m  = 0,01  / 0,112 = 0,089 = 8,9 %
  Δx = (0,305 ± 0,003) m     →  ε_Δx = 0,003 / 0,305 = 0,010 = 1,0 %   [ (30,5 ± 0,3) cm ]
  g  = 9,797 m/s²            (constante, sin incerteza)

Valor representativo:
  k = m · g / Δx = 0,112 · 9,797 / 0,305
    = 1,0973 / 0,305 = 3,60 N/m

Propagación (k = m · g · Δx⁻¹ ; g constante):
  ε_k = ε_m + ε_Δx = 0,089 + 0,010 = 0,099 = 9,9 %
  Δk  = ε_k · k = 0,099 · 3,60 = 0,36 N/m

  Redondeo:  Δk → 0,4 ; k → 3,6
  Resultado:  k_est = (3,6 ± 0,4) N/m      Intervalo: [3,2 ; 4,0] N/m
```

### A.4 Comparación de los dos métodos

```
k_din = (4,1 ± 0,6) N/m   →  [3,5 ; 4,7]
k_est = (3,6 ± 0,4) N/m   →  [3,2 ; 4,0]

Zona de superposición:  [3,5 ; 4,0] N/m   →   los dos métodos son COMPATIBLES.

Diferencia entre valores representativos:
  |k_din − k_est| = |4,11 − 3,60| = 0,5 N/m

Incerteza combinada (suma en cuadratura):
  √(0,6² + 0,4²) = √(0,36 + 0,16) = √0,52 = 0,7 N/m

Como 0,5 < 0,7, la diferencia entre ambos resultados no es significativa.
```

### A.5 Criterio de redondeo y cifras significativas

```
Reglas aplicadas (convención de la cátedra):

1. La incerteza (error absoluto) se redondea a 1 cifra significativa.
     ΔT     = 0,03 s
     Δf     = 0,028 Hz  → 0,03 Hz
     Δk_din = 0,60 N/m  → 0,6 N/m
     Δk_est = 0,36 N/m  → 0,4 N/m

2. El valor representativo se redondea a la misma posición decimal que su incerteza.
     T     = 1,037 s  con ΔT = 0,03 → T = 1,04 s
     f     = 0,964 Hz con Δf = 0,03 → f = 0,96 Hz
     k_din = 4,11 N/m con Δk = 0,6  → 4,1 N/m
     k_est = 3,60 N/m con Δk = 0,4  → 3,6 N/m

3. Nunca se informa el valor con más precisión que la que admite su incerteza.

4. En los pasos intermedios se conservan 1–2 cifras de más y se redondea solo el
   resultado final, para no arrastrar error de redondeo.

5. Unidad de la frecuencia: hertz (Hz) = 1/s = s⁻¹. Las tres notaciones son
   equivalentes; se prefiere Hz por ser la unidad SI de frecuencia.
```

---

**Fuentes utilizadas:**

- *Apoyo teórico para la Tercera Concurrencia: Movimiento Oscilatorio Armónico* (U.D.B. Física, material de cátedra) — deducción de `ω = 2π/T`, `ω² = k/m` y `T = 2π·√(m/k)`.
- *Reglamento para la realización de los trabajos prácticos en los Laboratorios de Física* (U.D.B. Física).
- *Criterios para la realización de los informes de los Trabajos Prácticos* (U.D.B. Física) — estructura del informe.
- TP N°1 — Mediciones y Errores (informe propio, 1ra concurrencia) — criterios de propagación de incertezas y de redondeo.
