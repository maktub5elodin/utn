# Trabajo Práctico N°1 — Mediciones y Errores

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

1. Determinar el volumen de un cilindro metálico utilizando tres instrumentos distintos: regla milimetrada, calibre y probeta graduada.
2. Realizar mediciones directas e indirectas contemplando las incertezas propias de cada instrumento.
3. Comparar y analizar los resultados obtenidos con cada método de medición.

### 1.2 Marco teórico

**Magnitudes y medición**

Una magnitud es todo aspecto observable y medible de un sistema físico: longitud, temperatura, masa, volumen, entre otros. Medir es comparar esa magnitud con una unidad de referencia establecida (patrón). El resultado de esa comparación nunca es un valor exacto: toda medición contiene una incerteza inevitable, denominada error.

**Representación de una medición — Intervalo de indeterminación**

Dado que el valor verdadero de una magnitud es imposible de conocer con exactitud, una medición se expresa como un intervalo que lo contiene. Dicho intervalo queda definido por un valor central y una incerteza:

`X = X₀ ± ΔX`

donde:
- `X₀` = Valor Representativo (punto medio del intervalo, valor leído directamente del instrumento en mediciones directas)
- `ΔX` = Error Absoluto (incerteza del intervalo; indica cuánto puede alejarse el valor verdadero del valor representativo)
- `X_min = X₀ − ΔX` (límite inferior del intervalo posible)
- `X_max = X₀ + ΔX` (límite superior del intervalo posible)

El valor verdadero se encuentra, con alta probabilidad, dentro del intervalo `[X_min ; X_max]`.

**Fuentes de error**

Se identifican tres fuentes principales de error en toda medición experimental:

| Fuente | Descripción |
|---|---|
| **Instrumento** | Limitaciones propias del instrumento: su apreciación (mínima división legible), posibles descalibraciones o deformaciones |
| **Observador** | Errores en la lectura: paralaje visual, interpretación de la escala, fatiga |
| **Objeto** | Características propias de lo medido: superficies irregulares, geometría imperfecta, condiciones variables durante la medición |

**Error absoluto y error relativo**

El error de una medición puede expresarse de dos maneras complementarias:

- **Error absoluto** `ΔX`: tiene las mismas unidades que la magnitud medida. Indica cuánto puede variar el valor en unidades concretas.
- **Error relativo** `ε_X = ΔX / X₀`: adimensional, toma valores entre 0 y 1 (o se expresa como porcentaje). Indica qué fracción del valor representativo representa la incerteza; es una medida de la *calidad* de la medición. Cuanto más cercano a 0, más precisa es la medición.

**Medición directa e indirecta**

- **Medición directa:** el valor de la magnitud se obtiene leyendo directamente el instrumento. El error absoluto es igual a la apreciación del instrumento.
- **Medición indirecta:** el valor se obtiene a partir de una fórmula que combina dos o más mediciones directas. El error absoluto se calcula mediante propagación de errores.

**Propagación de errores**

Dadas dos mediciones directas `a = a₀ ± Δa` y `b = b₀ ± Δb`, las reglas para obtener el valor representativo y el error absoluto de la magnitud indirecta son:

*Suma y resta:*

`R₀ = a₀ + b₀`  (o  `a₀ − b₀`)  →  `ΔR = Δa + Δb`

En ambos casos —suma Y resta— los errores absolutos se suman. La lógica: siempre se asume el escenario más desfavorable. Para la suma, los errores de cada magnitud pueden actuar en la misma dirección (uno hacia arriba, el otro también hacia arriba), acumulándose. Para la resta, también: `(a₀ + Δa) − (b₀ − Δb) = (a₀ − b₀) + (Δa + Δb)`. En ambos casos el error del resultado es `Δa + Δb`.

*Producto y cociente:*

`P₀ = a₀ · b₀`  (o  `a₀ / b₀`)  →  `ε_P = ε_a + ε_b`  →  `ΔP = ε_P · P₀`

Aquí conviene trabajar con errores relativos porque al multiplicar o dividir, los errores se *componen como proporciones*: un 5% de error en `a` y un 3% de error en `b` producen aproximadamente un 8% de error en el producto. Por eso se suman los errores relativos de los factores y luego se convierte al error absoluto multiplicando por el valor representativo del resultado.

*Potencia y raíz:*

`Z = aⁿ`  →  `ΔZ = n · ε_a · Z₀`

El exponente actúa como multiplicador del error relativo. Para raíces, `n` es un número entre 0 y 1 (ej.: raíz cuadrada → n = 1/2), lo que reduce el error relativo respecto del original.

**Fórmula del volumen del cilindro**

El volumen de un cilindro en función de su diámetro `d` y su altura `h` es:

`V = π · r² · h = π · (d/2)² · h = (π/4) · d² · h`

Se utiliza el diámetro en lugar del radio porque es la magnitud que se puede medir directamente con regla y calibre. El valor de π se tomó con todos los decimales disponibles en la calculadora, de modo que su incerteza sea despreciable frente a los errores de medición.

Propagación del error del volumen `V = (π/4) · d² · h`:
- `π/4` es constante (sin error)
- `d²` → aplicando la regla de potencia: `ε_{d²} = 2 · ε_d`
- `d² · h` → producto, se suman errores relativos: `ε_V = ε_{d²} + ε_h = 2 · ε_d + ε_h`
- `ΔV = ε_V · V₀`

**Conversión de unidades: mL a mm³**

La probeta mide volumen en mililitros (mL). Para expresar los resultados en la misma unidad que los obtenidos con regla y calibre (mm³), se aplica la siguiente conversión:

`1 mL = 1 cm³`  y  `1 cm³ = (10 mm)³ = 1000 mm³`

Por lo tanto: `1 mL = 1000 mm³`

Esto se aplica tanto al valor representativo como al error absoluto.

---

## 2. Procedimiento Experimental

### 2.1 Objeto de estudio

Cilindro metálico, cuyas dimensiones características son el diámetro `d` y la altura `h`.

### 2.2 Instrumentos utilizados e incertezas adoptadas

| Instrumento | Magnitud medida | Apreciación | Error absoluto adoptado |
|---|---|---|---|
| Regla milimetrada | Longitud (d, h) | 1 mm | `Δd = Δh = ±1 mm` |
| Calibre | Longitud (d, h) | 0,02 mm | `Δd = Δh = ±0,02 mm` |
| Probeta graduada | Volumen (lectura de nivel) | 1 mL = 1000 mm³ | `ΔV_i = ΔV_f = ±1000 mm³` |

Para las mediciones de longitud (regla y calibre), el error absoluto de las mediciones directas es igual a la apreciación del instrumento.

### 2.3 Descripción del procedimiento

**Con regla y calibre:**
Se midieron el diámetro `d` y la altura `h` del cilindro directamente con cada instrumento. A partir de estas mediciones directas se calcula el volumen como medición indirecta mediante la fórmula `V = (π/4) · d² · h`. El error del volumen se obtiene por propagación.

**Con probeta:**
Se registró el nivel inicial de agua `V_i` antes de sumergir el cilindro, y el nivel final `V_f` con el cilindro sumergido. El volumen del cilindro es la diferencia `V = V_f − V_i`, lo cual constituye una medición indirecta obtenida a partir de dos mediciones directas. Los valores se convierten de mL a mm³ multiplicando por 1000.

---

## 3. Resultados y Análisis

### 3.1 Mediciones directas

**Tabla 1.** Mediciones de diámetro y altura con regla milimetrada.

| Magnitud | Valor representativo | Error absoluto | Resultado |
|---|---|---|---|
| Diámetro `d₀` | 13 mm | ±1 mm | `(13 ± 1) mm` |
| Altura `h₀` | 51 mm | ±1 mm | `(51 ± 1) mm` |

*Tabla 1: Mediciones directas con regla milimetrada. Apreciación del instrumento: 1 mm.*

**Tabla 2.** Mediciones de diámetro y altura con calibre.

| Magnitud | Valor representativo | Error absoluto | Resultado |
|---|---|---|---|
| Diámetro `d₀` | 12,72 mm | ±0,02 mm | `(12,72 ± 0,02) mm` |
| Altura `h₀` | 50,6 mm | ±0,02 mm | `(50,6 ± 0,02) mm` |

*Tabla 2: Mediciones directas con calibre. Apreciación del instrumento: 0,02 mm.*

**Tabla 3.** Mediciones de nivel en probeta (mediciones directas de volumen en mm³).

| Lectura | Valor representativo | Error absoluto | Resultado |
|---|---|---|---|
| Nivel inicial `V_i` | 30.000 mm³ (30 mL) | ±1.000 mm³ | `(30.000 ± 1.000) mm³` |
| Nivel final `V_f` | 36.000 mm³ (36 mL) | ±1.000 mm³ | `(36.000 ± 1.000) mm³` |

*Tabla 3: Lecturas directas de la probeta. Apreciación: 1 mL = 1.000 mm³. Conversión aplicada: 1 mL = 1 cm³ = 1.000 mm³.*

### 3.2 Cálculo del volumen — Con regla milimetrada

**Valor representativo:**

`V₀ = (π/4) · d₀² · h₀ = (π/4) · 13² · 51 = (π/4) · 169 · 51 = (π/4) · 8619 = 6769,35 mm³`

**Errores relativos de las mediciones directas:**

`ε_d = Δd / d₀ = 1 / 13 = 0,07692`

`ε_h = Δh / h₀ = 1 / 51 = 0,01961`

**Error relativo del volumen** (regla de potencia para `d²` y producto para `d² · h`):

`ε_V = 2 · ε_d + ε_h = 2 · 0,07692 + 0,01961 = 0,15385 + 0,01961 = 0,17346`

**Error absoluto del volumen:**

`ΔV = ε_V · V₀ = 0,17346 · 6769,35 = 1174,17 mm³`

**Resultado redondeado:**

> **V_regla = (6770 ± 1170) mm³**  
> Intervalo: `[5600 ; 7940] mm³`

---

### 3.3 Cálculo del volumen — Con calibre

**Valor representativo:**

`V₀ = (π/4) · (12,72)² · 50,6 = (π/4) · 161,7984 · 50,6 = (π/4) · 8187,0 = 6430,05 mm³`

**Errores relativos de las mediciones directas:**

`ε_d = 0,02 / 12,72 = 0,001572`

`ε_h = 0,02 / 50,6 = 0,000395`

**Error relativo del volumen:**

`ε_V = 2 · 0,001572 + 0,000395 = 0,003144 + 0,000395 = 0,003539`

**Error absoluto del volumen:**

`ΔV = 0,003539 · 6430,05 = 22,76 mm³`

**Resultado redondeado:**

> **V_calibre = (6430 ± 20) mm³**  
> Intervalo: `[6410 ; 6450] mm³`

---

### 3.4 Cálculo del volumen — Con probeta

**Valor representativo** (diferencia entre mediciones directas):

`V₀ = V_f − V_i = 36.000 − 30.000 = 6.000 mm³`

**Error absoluto** (la resta de magnitudes suma los errores absolutos):

`ΔV = ΔV_f + ΔV_i = 1.000 + 1.000 = 2.000 mm³`

**Resultado:**

> **V_probeta = (6.000 ± 2.000) mm³**  
> Intervalo: `[4.000 ; 8.000] mm³`

---

### 3.5 Síntesis y gráfico comparativo

**Tabla 4.** Comparación de resultados de volumen obtenidos con los tres instrumentos.

| Instrumento | V₀ (mm³) | ΔV (mm³) | V_min (mm³) | V_max (mm³) | ε_V (%) |
|---|---|---|---|---|---|
| Calibre | 6430 | 20 | 6410 | 6450 | 0,35% |
| Regla | 6770 | 1170 | 5600 | 7940 | 17,3% |
| Probeta | 6000 | 2000 | 4000 | 8000 | 33,3% |

*Tabla 4: Síntesis de resultados. Los instrumentos están ordenados de mayor a menor precisión según su error relativo.*

El gráfico comparativo de los intervalos de volumen se encuentra representado en el archivo **`f_lab_01.dxf`** (LibreCAD, escala 1 mm = 20 mm³, rango 4.000–8.000 mm³). Dicho archivo será completado, impreso e incorporado al informe final como figura adjunta.

**Observación sobre la escala y la precisión del calibre:**
La escala adoptada (20 mm³ por milímetro) pone de manifiesto la alta precisión del calibre: su error absoluto de volumen es exactamente `ΔV = 20 mm³`, lo que equivale a **1 mm a cada lado** del valor representativo en el gráfico CAD (`f_lab_01.dxf`). Un intervalo de 2 mm total sería imposible de trazar con fidelidad a mano alzada, lo que justifica el uso del entorno CAD para esta representación.

**Análisis de compatibilidad entre resultados:**
Los tres intervalos de medición se superponen parcialmente. El valor representativo del calibre (6430 mm³) se encuentra dentro del intervalo de la regla [5600; 7940] y dentro del intervalo de la probeta [4000; 8000]. Esto indica que los tres métodos son **compatibles** entre sí: sus resultados no se contradicen. La diferencia en los valores representativos (6430 vs. 6770 vs. 6000) refleja exclusivamente la limitación de precisión de cada instrumento, no una discrepancia experimental.

---

## 4. Conclusiones

**Objetivo 1 — Determinación del volumen con tres instrumentos:**
Se determinó el volumen del cilindro metálico con los tres instrumentos solicitados, obteniendo:
- Regla: `V = (6770 ± 1170) mm³`
- Calibre: `V = (6430 ± 20) mm³`
- Probeta: `V = (6000 ± 2000) mm³`

**Objetivo 2 — Mediciones con incertezas:**
Las incertezas de las mediciones directas corresponden a la apreciación de cada instrumento. Para las mediciones indirectas de volumen (calculadas a partir de diámetro y altura) se aplicó propagación de errores mediante errores relativos. La medición directa de volumen con probeta utilizó la regla de propagación de la resta.

**Objetivo 3 — Comparación de resultados:**
Los tres resultados son compatibles, ya que sus intervalos se superponen. Sin embargo, se observa una diferencia notable en la precisión:

- El **calibre** ofreció el menor error relativo (0,35%), produciendo el intervalo más acotado. Es el instrumento más preciso para esta determinación.
- La **regla** presentó un error relativo de 17,3%, razonable para un instrumento de apreciación milimétrica.
- La **probeta** tuvo el mayor error relativo (33,3%), ya que su apreciación (1 mL = 1000 mm³) es gruesa en relación al volumen del cilindro (≈6000 mm³).

La comparación ilustra un principio fundamental de la metrología: la precisión del resultado de una medición indirecta está limitada por la precisión de las mediciones directas que la componen. Un instrumento más preciso (calibre vs. regla) reduce notablemente el error del resultado final, incluso cuando ambos miden la misma magnitud.

---

## Anexo de Cálculos

### A.1 Conversión de unidades — probeta

```
Apreciación de la probeta: 1 mL

1 mL = 1 cm³
1 cm³ = (1 cm)³ = (10 mm)³ = 10³ mm³ = 1000 mm³

Por lo tanto:
  V_i = 30 mL = 30 × 1000 mm³ = 30.000 mm³   →   ΔV_i = 1 mL = 1.000 mm³
  V_f = 36 mL = 36 × 1000 mm³ = 36.000 mm³   →   ΔV_f = 1 mL = 1.000 mm³
```

### A.2 Desarrollo completo — volumen con regla

```
Datos:
  d₀ = (13 ± 1) mm
  h₀ = (51 ± 1) mm

Valor representativo:
  V₀ = (π / 4) · d₀² · h₀
     = (3,14159265358979 / 4) · 13² · 51
     = 0,78539816... · 169 · 51
     = 0,78539816... · 8619
     = 6769,35 mm³

Errores relativos:
  ε_d = Δd / d₀ = 1 / 13 = 0,076923...
  ε_h = Δh / h₀ = 1 / 51 = 0,019608...

Error relativo del volumen:
  ε_V = 2 · ε_d + ε_h
      = 2 · 0,076923 + 0,019608
      = 0,153846 + 0,019608
      = 0,173454

Error absoluto del volumen:
  ΔV = ε_V · V₀ = 0,173454 · 6769,35 = 1174,17 mm³

Redondeo (ΔV con 1 cifra significativa → 1000? vs. retención 1170 a 3 cs):
  Se reporta: ΔV = 1170 mm³  →  V₀ = 6770 mm³

Resultado:  V_regla = (6770 ± 1170) mm³
Intervalo:  [6770 - 1170 ; 6770 + 1170] = [5600 ; 7940] mm³
```

### A.3 Desarrollo completo — volumen con calibre

```
Datos:
  d₀ = (12,72 ± 0,02) mm
  h₀ = (50,6  ± 0,02) mm

Valor representativo:
  d₀²  = 12,72² = 161,7984 mm²
  d₀² · h₀ = 161,7984 · 50,6 = 8187,0 mm³
  V₀ = (π/4) · 8187,0 = 0,785398... · 8187,0 = 6430,05 mm³

Errores relativos:
  ε_d = 0,02 / 12,72 = 0,0015723...
  ε_h = 0,02 / 50,6  = 0,0003953...

Error relativo del volumen:
  ε_V = 2 · 0,0015723 + 0,0003953
      = 0,0031446 + 0,0003953
      = 0,0035399

Error absoluto del volumen:
  ΔV = 0,0035399 · 6430,05 = 22,76 mm³

Redondeo (ΔV → 20 mm³;  V₀ → 6430 mm³):
  Resultado:  V_calibre = (6430 ± 20) mm³
  Intervalo:  [6410 ; 6450] mm³
```

### A.4 Desarrollo completo — volumen con probeta

```
Datos:
  V_i = (30.000 ± 1.000) mm³
  V_f = (36.000 ± 1.000) mm³

Valor representativo (diferencia):
  V₀ = V_f − V_i = 36.000 − 30.000 = 6.000 mm³

Error absoluto (resta → suma de errores absolutos):
  ΔV = ΔV_f + ΔV_i = 1.000 + 1.000 = 2.000 mm³

Resultado:  V_probeta = (6.000 ± 2.000) mm³
Intervalo:  [4.000 ; 8.000] mm³

Error relativo:
  ε_V = ΔV / V₀ = 2.000 / 6.000 = 0,333... = 33,3%
```

### A.5 Escala del gráfico comparativo

```
Rango elegido: 4.000 mm³ a 8.000 mm³ → amplitud = 4.000 mm³
Longitud de trabajo en el dibujo: 200 mm (20 cm)

Escala: 200 mm / 4.000 mm³ = 1 mm por cada 20 mm³

Posición de cada valor representativo en el dibujo
(tomando x = 0 en V = 4.000 mm³):

  Calibre: x = (6430 - 4000) / 20 = 2430 / 20 = 121,5 mm  desde el origen
  Regla:   x = (6770 - 4000) / 20 = 2770 / 20 = 138,5 mm  desde el origen
  Probeta: x = (6000 - 4000) / 20 = 2000 / 20 = 100,0 mm  desde el origen

Rango del calibre en el dibujo:
  ΔV = 20 mm³  →  20 / 20 = 1 mm  a cada lado del valor representativo
  (rango total en el gráfico: 2 mm — justifica el uso de CAD)
```