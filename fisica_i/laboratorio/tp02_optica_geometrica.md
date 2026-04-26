# Trabajo Práctico N°2 — Óptica Geométrica

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

**Profesor/a:** ___________________________  
**Docentes auxiliares:** ___________________________

---

## 1. Introducción

### 1.1 Objetivos

1. Determinar el índice de refracción `n` del acrílico con respecto al aire.
2. Determinar el ángulo límite del acrílico y compararlo con el valor teórico.
3. Determinar la distancia focal `f` de una lente convergente.

### 1.2 Marco teórico

**Ley de Snell — Refracción de la luz**

Cuando un rayo de luz pasa de un medio transparente a otro, cambia su velocidad de propagación y se desvía respecto de la normal a la superficie de separación. La Ley de Snell describe esta relación:

`n₁ · sen(α) = n₂ · sen(β)`

donde `α` es el ángulo de incidencia (en el medio 1) y `β` es el ángulo de refracción (en el medio 2), ambos medidos respecto de la normal. Cuando el rayo va del aire al acrílico (n_aire = 1), el índice de refracción del acrílico respecto del aire resulta:

`n_acrílico-aire = sen(α) / sen(β)`

El índice inverso (del aire respecto del acrílico) se obtiene por reciprocidad:

`n_aire-acrílico = 1 / n_acrílico-aire`

**Ángulo límite — Reflexión total interna**

Cuando la luz viaja desde un medio ópticamente más denso (acrílico) hacia uno menos denso (aire), existe un ángulo de incidencia crítico, denominado ángulo límite `l`, para el cual el rayo refractado sale rasante a la superficie de separación (β = 90°). Para ángulos de incidencia mayores que `l` se produce reflexión total interna: ningún rayo penetra en el segundo medio.

El valor teórico del ángulo límite se obtiene aplicando la Ley de Snell con `β = 90°`:

`n_acrílico-aire · sen(l) = n_aire · sen(90°) = 1`

`sen(l) = n_aire-acrílico   →   l = arcsen(n_aire-acrílico)`

**Lente convergente — Fórmula de Gauss**

Para una lente delgada, la relación entre la abscisa del objeto `x`, la abscisa de la imagen `x'` y la distancia focal `f` está dada por:

`1/f = 1/x - 1/x'`

Despejando la distancia focal:

`f = (x · x') / (x' - x)`

La propagación del error de `f` se obtiene aplicando las reglas de propagación para productos, cocientes y diferencias:

`Δf = ( Δx/|x₀| + Δx'/|x'₀| + (Δx + Δx')/|x'₀ - x₀| ) · |f₀|`

---

## 2. Procedimiento Experimental

### 2.1 Materiales e instrumental

| Elemento | Función en el experimento |
|---|---|
| Fuente de luz | Generación del rayo incidente |
| Disco de Hartl semicilíndrico de acrílico | Medición de ángulos de refracción y ángulo límite |
| Lente convergente (biconvexa) | Formación de imágenes reales |
| Banco óptico | Soporte y medición de posiciones de objeto e imagen |
| Transportador (escala en grados) | Lectura directa de ángulos |

**Estimación de incertezas:**

Las incertezas no coinciden con la mínima división de los instrumentos porque el grosor físico de las patas de la fuente y de los accesorios del banco óptico impide determinar con precisión de 1 mm o 1° la posición o dirección de cada elemento. Por ello se adoptaron:

- `Δα = Δβ = Δl = ±2°` para todos los ángulos.
- `Δx = ±2 mm` para la abscisa del objeto.
- `Δx' = ±4 mm` para la abscisa de la imagen (mayor incerteza por la dificultad de ubicar el plano focal en la pantalla).

### 2.2 Experimento 1 — Refracción: determinación de n del acrílico

Se colocó el disco de Hartl con la superficie plana como interfaz. Se hizo incidir un rayo de luz desde el aire formando un ángulo `α` con la normal, y se midió el ángulo de refracción `β` dentro del acrílico.

```
          Normal a la superficie
                 |
    AIRE   α  ↗ |
   ─────────────+─────────────
    ACRÍLICO    | ↘ β
                |
```

Se registraron los ángulos de incidencia y refracción para calcular el índice de refracción.

### 2.3 Experimento 2 — Ángulo límite del acrílico

Se orientó el rayo para que incidiera desde el interior del acrílico hacia la superficie plana. Se fue aumentando el ángulo de incidencia hasta observar que el rayo refractado emergía rasante a la superficie de separación. El ángulo de incidencia en ese instante es el ángulo límite experimental `l_exp`.

```
    ACRÍLICO  |  AIRE
              |
      rayo ↗  |→ rasante (β ≈ 90°)
        l_exp |
```

### 2.4 Experimento 3 — Distancia focal de la lente convergente

Se montó en el banco óptico la fuente (objeto), la lente convergente y la pantalla. Se desplazó la pantalla hasta obtener una imagen nítida. Se registraron las posiciones del objeto y de la imagen respecto del centro óptico de la lente.

```
  Fuente        Lente          Pantalla
    |              |               |
    |<---- x₀ --->|<--- |x'₀| --->|
                  O
          (centro óptico)
```

---

## 3. Resultados y Análisis

### 3.1 Índice de refracción del acrílico

**Tabla 1.** Mediciones de ángulos en la interfaz aire-acrílico.

| Magnitud | Valor representativo | Error absoluto | Resultado |
|---|---|---|---|
| Ángulo de incidencia `α` | 30° | ±2° | `(30 ± 2)°` |
| Ángulo de refracción `β` | 20° | ±2° | `(20 ± 2)°` |

*Tabla 1: Ángulos medidos con el disco de Hartl semicilíndrico. La incerteza de ±2° se adoptó por el grosor de los soportes del dispositivo experimental.*

**Cálculo de `n_acrílico-aire` — Método de valores extremos**

Dado que el cálculo involucra funciones trigonométricas, cuya respuesta no es lineal con el ángulo, se empleó el método de máximos y mínimos en lugar de propagación directa de errores.

Valor máximo del índice (se maximiza α y se minimiza β):

`n_max = sen(α_max) / sen(β_min) = sen(32°) / sen(18°) = 0,5299 / 0,3090 = 1,715`

Valor mínimo del índice (se minimiza α y se maximiza β):

`n_min = sen(α_min) / sen(β_max) = sen(28°) / sen(22°) = 0,4695 / 0,3746 = 1,253`

Valor representativo y error absoluto:

`n₀ = (n_max + n_min) / 2 = (1,715 + 1,253) / 2 = 1,484`

`Δn = (n_max - n_min) / 2 = (1,715 - 1,253) / 2 = 0,231`

Aplicando criterio de redondeo (Δn con una sola cifra significativa, X₀ con la misma cantidad de decimales):

> **n_acrílico-aire = (1,5 ± 0,2)**

El valor de referencia del acrílico (PMMA) es n ≈ 1,49, que se encuentra dentro del intervalo obtenido `[1,3 ; 1,7]`.

**Cálculo de `n_aire-acrílico`**

Se aplica la reciprocidad del índice de refracción relativo usando los valores extremos de n_acrílico-aire:

`n_max_aire-acr = 1 / n_min_acr-aire = 1 / 1,253 = 0,798`

`n_min_aire-acr = 1 / n_max_acr-aire = 1 / 1,715 = 0,583`

`n₀_aire-acrílico = (0,798 + 0,583) / 2 = 0,691`

`Δn_aire-acrílico = (0,798 - 0,583) / 2 = 0,108`

Redondeado:

> **n_aire-acrílico = (0,7 ± 0,1)**

### 3.2 Ángulo límite

**Tabla 2.** Comparación entre el ángulo límite teórico y el experimental.

| Magnitud | Valor (°) | Error (°) | Resultado |
|---|---|---|---|
| Ángulo límite teórico `l_teo` | 44 | ±9 | `(44 ± 9)°` |
| Ángulo límite experimental `l_exp` | 43 | ±2 | `(43 ± 2)°` |

*Tabla 2: El ángulo límite teórico se calculó a partir de n_aire-acrílico mediante el método de valores extremos. El experimental fue medido directamente observando la emergencia rasante del rayo en el disco de Hartl.*

**Cálculo del ángulo límite teórico:**

`l_max = arcsen(n_max_aire-acr) = arcsen(0,798) = 52,9°`

`l_min = arcsen(n_min_aire-acr) = arcsen(0,583) = 35,7°`

`l₀_teo = (52,9 + 35,7) / 2 = 44,3°`

`Δl_teo = (52,9 - 35,7) / 2 = 8,6°`

Redondeado: `l_teo = (44 ± 9)°`

**Compatibilidad:** El intervalo experimental es `[41° ; 45°]` y el teórico es `[35° ; 53°]`. El intervalo experimental está completamente contenido dentro del teórico, lo que confirma la coherencia entre ambas determinaciones.

### 3.3 Distancia focal de la lente convergente

**Tabla 3.** Mediciones de posiciones en el banco óptico.

| Magnitud | Valor representativo | Error absoluto | Resultado |
|---|---|---|---|
| Abscisa objeto `x₀` | +136 mm | ±2 mm | `(136 ± 2) mm` |
| Abscisa imagen `x'₀` | −331 mm | ±4 mm | `(−331 ± 4) mm` |

*Tabla 3: Posiciones medidas en el banco óptico respecto del centro óptico de la lente. El signo negativo de x'₀ corresponde a la convención de signos del banco, en la que la imagen real se forma en el lado opuesto al objeto. La mayor incerteza en x'₀ refleja la dificultad para determinar el plano de imagen nítida sobre la pantalla.*

**Cálculo del valor representativo de `f`:**

`f₀ = (x₀ · x'₀) / (x'₀ − x₀) = (136 × (−331)) / ((−331) − 136) = −45016 / −467 = 96,4 mm`

**Cálculo de `Δf` — Propagación de errores:**

Se aplica la fórmula de propagación para `f = x·x'/(x'−x)`, usando valores absolutos de los denominadores dado que representan magnitudes en el error:

`Δf = ( Δx/|x₀| + Δx'/|x'₀| + (Δx + Δx')/|x'₀ − x₀| ) · |f₀|`

`Δf = ( 2/136 + 4/331 + (2 + 4)/467 ) · 96,4`

`Δf = ( 0,01471 + 0,01208 + 0,01285 ) · 96,4`

`Δf = 0,03964 · 96,4 = 3,82 mm`

Redondeado (Δf con una cifra significativa → 4 mm; f₀ a la misma posición decimal → 96 mm):

> **f = (96 ± 4) mm**

El error relativo es: `ε_f = 4/96 ≈ 0,04 = 4%`, lo que indica una medición de buena calidad para las condiciones del banco óptico utilizado.

---

## 4. Conclusiones

**Objetivo 1 — Índice de refracción del acrílico:**  
Se determinó `n_acrílico-aire = (1,5 ± 0,2)`, con un intervalo posible `[1,3 ; 1,7]`. El valor de referencia del acrílico (n ≈ 1,49) se encuentra dentro de dicho intervalo, lo que valida el resultado experimental. La incerteza relativamente amplia se debe principalmente a la sensibilidad de la función seno para ángulos pequeños, combinada con las limitaciones de la lectura angular (±2°).

**Objetivo 2 — Ángulo límite:**  
El ángulo límite experimental `(43 ± 2)°` es compatible con el teórico `(44 ± 9)°`, ya que el intervalo experimental está completamente contenido en el teórico. La gran amplitud del intervalo teórico refleja la propagación de la incerteza de n_aire-acrílico a través de la función arcoseno. La medición directa del ángulo límite resultó ser más precisa que el cálculo teórico derivado del índice, lo que resalta la importancia de la medición experimental directa cuando es posible realizarla.

**Objetivo 3 — Distancia focal:**  
Se determinó `f = (96 ± 4) mm`, con un error relativo del 4%. El resultado es coherente con el comportamiento esperado de una lente convergente (f positivo), y la incerteza es acotada considerando las dificultades de posicionamiento en el banco óptico.

Los tres objetivos del trabajo práctico fueron alcanzados satisfactoriamente. Los resultados experimentales son compatibles con los valores teóricos dentro de las incertezas obtenidas, lo que confirma la validez del procedimiento experimental empleado.

---

## Anexo de Cálculos

### A.1 Valores trigonométricos utilizados

| Ángulo | sen |
|---|---|
| 18° | 0,3090 |
| 20° | 0,3420 |
| 22° | 0,3746 |
| 28° | 0,4695 |
| 30° | 0,5000 |
| 32° | 0,5299 |

| n_aire-acrílico | arcsen |
|---|---|
| 0,583 | 35,7° |
| 0,691 | 43,6° |
| 0,798 | 52,9° |

### A.2 Desarrollo completo — n_acrílico-aire

```
Datos:  α = (30 ± 2)°   β = (20 ± 2)°

n_max = sen(α_max) / sen(β_min)
      = sen(32°) / sen(18°)
      = 0,5299 / 0,3090
      = 1,7148

n_min = sen(α_min) / sen(β_max)
      = sen(28°) / sen(22°)
      = 0,4695 / 0,3746
      = 1,2533

n₀ = (1,7148 + 1,2533) / 2 = 2,9681 / 2 = 1,484
Δn = (1,7148 - 1,2533) / 2 = 0,4615 / 2 = 0,231

Redondeo:  Δn → 0,2  ;  n₀ → 1,5

Resultado:  n_acrílico-aire = (1,5 ± 0,2)
```

### A.3 Desarrollo completo — n_aire-acrílico

```
n_max_aire-acr = 1 / n_min_acr-aire = 1 / 1,2533 = 0,7980
n_min_aire-acr = 1 / n_max_acr-aire = 1 / 1,7148 = 0,5832

n₀_aire-acr = (0,7980 + 0,5832) / 2 = 1,3812 / 2 = 0,6906
Δn_aire-acr = (0,7980 - 0,5832) / 2 = 0,2148 / 2 = 0,1074

Redondeo:  Δn → 0,1  ;  n₀ → 0,7

Resultado:  n_aire-acrílico = (0,7 ± 0,1)
```

### A.4 Desarrollo completo — ángulo límite teórico

```
l_max = arcsen(n_max_aire-acr) = arcsen(0,7980) = 52,9°
l_min = arcsen(n_min_aire-acr) = arcsen(0,5832) = 35,7°

l₀_teo = (52,9 + 35,7) / 2 = 88,6 / 2 = 44,3°
Δl_teo = (52,9 - 35,7) / 2 = 17,2 / 2 = 8,6°

Redondeo:  Δl → 9°  ;  l₀ → 44°

Resultado:  l_teo = (44 ± 9)°
```

### A.5 Desarrollo completo — distancia focal

```
Datos:  x₀ = (136 ± 2) mm    x'₀ = (−331 ± 4) mm

f₀ = (x₀ · x'₀) / (x'₀ − x₀)
   = (136 · (−331)) / ((−331) − 136)
   = −45016 mm² / −467 mm
   = 96,4 mm

Δf = ( Δx/|x₀| + Δx'/|x'₀| + (Δx + Δx')/|x'₀ − x₀| ) · |f₀|

   = ( 2/136 + 4/331 + (2 + 4)/|−331 − 136| ) · 96,4

   = ( 2/136 + 4/331 + 6/467 ) · 96,4

   = ( 0,01471 + 0,01208 + 0,01285 ) · 96,4

   = 0,03964 · 96,4

   = 3,82 mm

Redondeo:  Δf → 4 mm  ;  f₀ → 96 mm

Resultado:  f = (96 ± 4) mm
```
