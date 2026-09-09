# Trabajo Práctico N°6 — Principio de Arquímedes (densidad de un líquido)

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

a) Medir la densidad de un líquido desconocido por dos métodos independientes —directo y de la pendiente— y comparar los resultados.  
b) Aplicar propagación de error en las mediciones.  
c) Usar herramientas estadísticas (regresión lineal) para analizar un conjunto de datos y hallar su incerteza.  
d) Utilizar software de ajuste de curvas.  
e) Evaluar la calidad de las mediciones por medio de gráficos.  
f) Afianzar los conceptos sobre el principio de Arquímedes.

### 1.2 Marco teórico

**Principio de Arquímedes**

Todo cuerpo sumergido en un fluido experimenta un empuje `E` hacia arriba igual al peso del líquido que desplaza:

`E = ρ · Vol_d · g`

- `E` = empuje (N)
- `ρ` = densidad del líquido (kg/L)
- `Vol_d` = volumen de líquido desplazado (L)
- `g` = aceleración de la gravedad (m/s²)

Por comodidad la densidad se expresa en **kg/L** (kilogramo por litro), equivalente a g/mL y a g/cm³: `1 g/mL = 1 kg/L`.

**Método 1 — directo (definición de densidad)**

La densidad es el cociente entre la masa de líquido y el volumen que ocupa:

`ρ = m_liq / Vol_liq`

Se determina la masa del líquido por diferencia (probeta con líquido menos probeta vacía) y el volumen por lectura directa de la probeta. Al ser un cociente, la propagación de error es `ε_ρ = ε_m + ε_V`.

**Método 2 — de la pendiente (Arquímedes + regresión lineal)**

Se cuelga un cilindro estanco de un dinamómetro y se lo sumerge, a distintas alturas, en el líquido contenido en la probeta. Sobre el cilindro actúan el peso `P` (hacia abajo), la lectura del dinamómetro `D` (fuerza del resorte, hacia arriba) y el empuje `E` (hacia arriba). En equilibrio:

`E + D = P   →   P − D = E = ρ · Vol_d · g`

Reordenando:

`(P − D) = ρ · (Vol_d · g)`

Es la ecuación de una recta `y = pend · x` que **pasa por el origen** (ordenada al origen nula), con:

- `y = P − D`  (N)
- `x = Vol_d · g`  (L·m/s²)
- `pend = ρ`  →  **la pendiente de la recta es la densidad del líquido**

Variando la altura del cilindro se obtienen pares `(x, y)`; un ajuste lineal por mínimos cuadrados forzado al origen entrega la pendiente y su incerteza.

**Ajuste lineal con ordenada al origen nula**

- Pendiente: `pend = Σ(xᵢ·yᵢ) / Σ(xᵢ²)`
- Coeficiente de determinación: `R² = 1 − Σ(yᵢ − ŷᵢ)² / Σ(yᵢ − ȳ)²` — proporción de la variabilidad de `y` explicada por la recta (`R² = 1`: ajuste perfecto; cuanto más cerca de 1, mejor).
- Desviación estándar de los residuos: `s = √( Σ(yᵢ − ŷᵢ)² / (n − 2) )`, con `ŷᵢ = pend·xᵢ` y residuo `eᵢ = yᵢ − ŷᵢ`.
- Error estándar de la pendiente: `s_m = s / √( Σ(xᵢ − x̄)² )`.

La planilla determina los límites de la densidad como `pend ± 3·s_m` y reporta el resultado final (Tabla 5) como `ρ ± Δρ`, tomando `Δρ` como la amplitud de ese intervalo.

**Propagación de incertezas**

- Método directo: `ρ = m·Vol⁻¹`  →  `ε_ρ = ε_m + ε_V`.
- Método de la pendiente: la incerteza sale del propio ajuste (a partir de `s_m`, el error estándar de la pendiente), que engloba la dispersión de todos los pares medidos; no se propagan por separado los errores de `Vol_0`, `Vol_i` ni `D`.

---

## 2. Procedimiento Experimental

### 2.1 Materiales

Probeta graduada de 1000 mL, balanza mecánica de un plato fijo, líquido desconocido, dos dinamómetros (alcances 1 N y 2,5 N), cilindro estanco y soporte con altura regulable. El cilindro se suspende del dinamómetro, que a su vez cuelga del soporte; la probeta con el líquido se ubica debajo, de modo de poder sumergir el cilindro variando la altura del soporte.

### 2.2 Instrumentos utilizados e incertezas adoptadas

| Instrumento | Magnitud medida | Resolución | Error absoluto adoptado |
|---|---|---|---|
| Balanza mecánica | Masa (probeta, líquido, cilindro) | 0,1 g | Método directo: `Δm_liq = ±0,2 g` (suma de las apreciaciones de las dos pesadas: probeta vacía y probeta con líquido) |
| Probeta graduada 1000 mL | Volumen de líquido | — | Método directo: `ΔVol_liq = ±1 mL` · Método pendiente: `ΔVol_0 = ±10 mL` |
| Dinamómetros (1 N y 2,5 N) | Fuerza del resorte `D` | — | La dispersión de las lecturas se absorbe en el ajuste lineal (error estándar de la pendiente) |

*Pie de tabla: En el método directo la masa del líquido se obtiene por resta de dos pesadas, por lo que su error absoluto es la suma de las apreciaciones (0,1 + 0,1 = 0,2 g). En el método de la pendiente no se propagan individualmente las incertezas de volumen y fuerza: quedan reflejadas en la dispersión de los puntos respecto de la recta de ajuste.*

### 2.3 Método directo

1. Se pesó la probeta vacía: `45,0 g`.
2. Se agregó el líquido desconocido y se volvió a pesar la probeta: `69,6 g`. La masa del líquido, por diferencia, es `24,6 g`.
3. Se leyó el volumen de líquido en la probeta: `Vol_liq = (26 ± 1) mL`.
4. Se calculó la densidad como `ρ = m_liq / Vol_liq` y se propagó el error.

### 2.4 Método de la pendiente

1. Se pesó el cilindro estanco: `m_cil = 0,293 kg`. Su peso es `P = m_cil · g = 0,293 · 9,797 = 2,871 N`, con `g = 9,797 m/s²` (módulo de `g` en Buenos Aires).
2. Se midió el volumen inicial del líquido en la probeta, con el cilindro afuera: `Vol_0 = (720 ± 10) mL`.
3. Se colgó el cilindro del dinamómetro y se lo sumergió en el líquido. Para **10 alturas distintas** del soporte se registró la lectura del dinamómetro `Dᵢ` (N) y el volumen del líquido `Vol_iᵢ` (mL). Se usó el dinamómetro de 1 N hasta su alcance máximo y luego el de 2,5 N.
4. Para cada punto se calculó `Vol_dᵢ = Vol_iᵢ − Vol_0`, `xᵢ = Vol_dᵢ · g` (en L·m/s²) e `yᵢ = P − Dᵢ` (N).
5. Con la planilla de cálculo provista por la cátedra se ajustó la recta `y = pend·x` (ordenada al origen nula) y se obtuvieron la pendiente (densidad), su error estándar `s_m` y el coeficiente `R²`.

---

## 3. Resultados y Análisis

### 3.1 Densidad — método directo

**Tabla 1.** Pesadas y volumen del líquido.

| Magnitud | Valor | Error absoluto |
|---|---|---|
| Masa probeta vacía | 45,0 g | ±0,1 g |
| Masa probeta + líquido | 69,6 g | ±0,1 g |
| Masa del líquido `m_liq` (por diferencia) | 24,6 g | ±0,2 g |
| Volumen del líquido `Vol_liq` | 26 mL | ±1 mL |

*Tabla 1: La masa del líquido se obtiene por resta de las dos pesadas; su error absoluto es la suma de las apreciaciones de la balanza.*

`ρ = m_liq / Vol_liq = 24,6 g / 26 mL = 0,946 g/mL = 0,946 kg/L`

**Propagación** (cociente → suma de errores relativos):

`ε_m = Δm_liq / m_liq = 0,2 / 24,6 = 0,81 %`

`ε_V = ΔVol_liq / Vol_liq = 1 / 26 = 3,85 %`

`ε_ρ = ε_m + ε_V = 0,81 % + 3,85 % = 4,7 %`

`Δρ = ε_ρ · ρ = 0,047 · 0,946 = 0,04 kg/L`

> **`ρ₁ = (0,95 ± 0,04) kg/L`**  
> Intervalo: `[0,91 ; 0,99] kg/L`

El error está dominado por la lectura del volumen (`3,85 %` frente a `0,81 %` de la masa): se midieron apenas 26 mL en una probeta de 1000 mL de alcance, cuya escala no permite mayor precisión en volúmenes tan chicos.

### 3.2 Datos — método de la pendiente

**Tabla 2.** Pares medidos y magnitudes procesadas.

| `i` | `Vol_iᵢ` (mL) | `Dᵢ` (N) | `Vol_dᵢ` (mL) | `xᵢ = Vol_dᵢ·g` (L·m/s²) | `yᵢ = P − Dᵢ` (N) |
|---|---|---|---|---|---|
| 0 | — | — | — | 0,000 | 0,000 |
| 1 | 760 | 2,5 | 40 | 0,392 | 0,371 |
| 2 | 790 | 2,2 | 70 | 0,686 | 0,671 |
| 3 | 810 | 2,0 | 90 | 0,882 | 0,871 |
| 4 | 830 | 1,7 | 110 | 1,078 | 1,171 |
| 5 | 850 | 1,5 | 130 | 1,274 | 1,371 |
| 6 | 880 | 1,3 | 160 | 1,568 | 1,571 |
| 7 | 900 | 1,0 | 180 | 1,763 | 1,871 |
| 8 | 930 | 0,8 | 210 | 2,057 | 2,071 |
| 9 | 950 | 0,5 | 230 | 2,253 | 2,371 |
| 10 | 980 | 0,3 | 260 | 2,547 | 2,571 |

*Tabla 2: `Vol_dᵢ = Vol_iᵢ − Vol_0` con `Vol_0 = 720 mL`; `P = 2,871 N`; `g = 9,797 m/s²`. La fila 0 se fija en `(0 ; 0)` para forzar a la recta a pasar por el origen. Datos y procesamiento reproducidos de la planilla `Planilla_arquimedes_Laboratorio.xlsx` (ver Figura 1 del Anexo).*

### 3.3 Regresión lineal y densidad — método de la pendiente

Del ajuste `y = pend·x` (ordenada al origen nula, `n = 10`) realizado en la planilla de cálculo:

**Tabla 3.** Resultados de la regresión lineal.

| Parámetro | Símbolo | Valor |
|---|---|---|
| Pendiente de la recta (= densidad) | `pend = ρ` | 1,029 kg/L |
| Error estándar de la pendiente | `s_m` | 0,010 kg/L |
| Coeficiente de determinación | `R²` | 0,999 |

*Tabla 3: Valores obtenidos por la planilla de cátedra. Ver el gráfico `(P − D)` vs `(Vol_d·g)` con la recta de ajuste en la Figura 2 del Anexo.*

**Incerteza** (planilla de cátedra, Tabla 5 — Resultados finales):

La planilla calcula los límites de la densidad como `pend ± 3·s_m` (`1,000` y `1,058 kg/L`) y adopta como incerteza absoluta la amplitud de ese intervalo, `Δρ = 1,058 − 1,000 = 0,057 → 0,06 kg/L` (ver Anexo A.3).

> **`ρ₂ = (1,03 ± 0,06) kg/L`**  
> Intervalo: `[0,97 ; 1,09] kg/L`

El coeficiente `R² = 0,999` indica que los puntos se alinean casi perfectamente sobre la recta que pasa por el origen: el modelo lineal —empuje proporcional al volumen desplazado— describe muy bien los datos, lo que confirma el principio de Arquímedes y respalda la calidad de esta serie de mediciones.

### 3.4 Comparación de los dos métodos

**Tabla 4.** Densidad del líquido por cada método.

| Método | `ρ` (kg/L) | `Δρ` (kg/L) | `ε_ρ` | Intervalo (kg/L) |
|---|---|---|---|---|
| Directo (`m/V`) | 0,95 | 0,04 | 4,7 % | [0,91 ; 0,99] |
| Pendiente (Arquímedes + regresión) | 1,03 | 0,06 | 5,8 % | [0,97 ; 1,09] |

*Tabla 4: Los dos métodos determinan la misma magnitud a partir de mediciones distintas: masa y volumen en un caso; fuerza, volumen desplazado y ajuste lineal en el otro.*

Los intervalos `[0,91 ; 0,99]` y `[0,97 ; 1,09]` **se superponen** en `[0,97 ; 0,99] kg/L`: los dos resultados **son compatibles** dentro de las incertezas estimadas. La diferencia entre los valores representativos, `|1,03 − 0,95| = 0,08 kg/L`, es menor que la suma de las incertezas (`0,04 + 0,06 = 0,10 kg/L`), consistente con la superposición.

Ambos métodos ubican la densidad del líquido en torno a `1 kg/L`, valor consistente con un líquido de base acuosa. Las incertezas relativas son del orden del `5 %` en los dos casos: en el método directo pesa la lectura de un volumen pequeño (26 mL) en una probeta de gran alcance (`ε_V = 3,8 %`); en el método de la pendiente, la dispersión de los 10 puntos alrededor de la recta, aunque el ajuste es muy bueno (`R² = 0,999`).

---

## 4. Conclusiones

**Objetivo a — Densidad por dos métodos y comparación:**  
- Método directo: `ρ₁ = (0,95 ± 0,04) kg/L`.  
- Método de la pendiente: `ρ₂ = (1,03 ± 0,06) kg/L`.  
Los intervalos se superponen en `[0,97 ; 0,99] kg/L`: los resultados son compatibles. La diferencia entre los valores representativos (`0,08 kg/L`) es menor que la suma de las incertezas (`0,10 kg/L`).

**Objetivo b — Propagación de error:**  
En el método directo se propagó `ε_ρ = ε_m + ε_V` (cociente). El término dominante es el volumen (`3,8 %` frente a `0,8 %` de la masa), por medir un volumen pequeño en una probeta de gran alcance.

**Objetivos c y d — Herramientas estadísticas y software de ajuste:**  
La densidad del método de la pendiente se obtuvo como la pendiente de la recta `(P − D)` vs `(Vol_d·g)`, ajustada por mínimos cuadrados con ordenada al origen nula en la planilla de cálculo. Su incerteza se tomó de la Tabla 5 de la planilla (`Δρ = 0,06 kg/L`), calculada a partir de los límites `pend ± 3·s_m`.

**Objetivo e — Calidad de las mediciones por gráficos:**  
El ajuste del método de la pendiente tiene `R² = 0,999`: los puntos se alinean casi perfectamente sobre la recta por el origen, lo que confirma la proporcionalidad entre empuje y volumen desplazado y la buena calidad de esa serie. La medición del método directo, al ser única, no admite evaluación gráfica de su dispersión.

**Objetivo f — Principio de Arquímedes:**  
La linealidad de `(P − D)` vs `(Vol_d·g)`, con pendiente igual a la densidad y ordenada al origen nula, es una verificación directa de `E = ρ·Vol_d·g`: el empuje crece en proporción al volumen de líquido desplazado.

**Síntesis:**  
El líquido desconocido tiene una densidad del orden de `1 kg/L`, resultado consistente entre los dos métodos. El método de la pendiente, con 10 mediciones y un ajuste de alta calidad (`R² = 0,999`), aporta la verificación más sólida del comportamiento lineal previsto por el principio de Arquímedes.

---

## Anexo de Cálculos

### A.1 Método directo

```
Pesadas (apreciación de la balanza: 0,1 g):
  m_probeta vacía     = 45,0 g
  m_probeta + líquido  = 69,6 g
  m_liq = 69,6 − 45,0 = 24,6 g
  Δm_liq = 0,1 + 0,1  = 0,2 g          (resta → suma de apreciaciones)

Volumen:
  Vol_liq = (26 ± 1) mL

Densidad:
  ρ = m_liq / Vol_liq = 24,6 / 26 = 0,9462 g/mL = 0,9462 kg/L     (1 g/mL = 1 kg/L)

Propagación (ρ = m · Vol⁻¹ ; cociente → suma de errores relativos):
  ε_m = 0,2 / 24,6 = 0,00813 = 0,81 %
  ε_V = 1   / 26   = 0,03846 = 3,85 %
  ε_ρ = ε_m + ε_V  = 0,04659 = 4,7 %
  Δρ  = ε_ρ · ρ = 0,04659 · 0,9462 = 0,0441 kg/L

Redondeo:  Δρ → 0,04 ; ρ → 0,95
Resultado:  ρ₁ = (0,95 ± 0,04) kg/L      Intervalo: [0,91 ; 0,99] kg/L
```

### A.2 Método de la pendiente — preparación de los datos

```
Datos A:
  m_cil = 0,293 kg
  g     = 9,797 m/s²
  P     = m_cil · g = 0,293 · 9,797 = 2,871 N
  Vol_0 = (720 ± 10) mL

Para cada punto i:
  Vol_dᵢ = Vol_iᵢ − Vol_0            [mL]
  xᵢ     = Vol_dᵢ · g / 1000         [L · m/s²]     (el /1000 pasa mL → L)
  yᵢ     = P − Dᵢ                    [N]

Ejemplo (punto 1):
  Vol_d1 = 760 − 720 = 40 mL
  x1 = 40 · 9,797 / 1000 = 0,392 L·m/s²
  y1 = 2,871 − 2,5 = 0,371 N

Tabla completa de (xᵢ ; yᵢ): ver §3.2.
```

### A.3 Método de la pendiente — regresión lineal (planilla)

```
Ajuste  y = pend · x   (ordenada al origen nula, n = 10) — planilla de cálculo

  pend = Σ(xᵢ·yᵢ) / Σ(xᵢ²) = 1,029 kg/L        →  pendiente = densidad (valor representativo)
  s_m  = 0,010 kg/L                             →  error estándar de la pendiente
  R²   = 0,999                                  →  coeficiente de determinación (calidad del ajuste)

Incerteza — Tabla 5 (Resultados finales) de la planilla:
  límites de la densidad:  pend − 3·s_m ≈ 1,000 kg/L ;  pend + 3·s_m ≈ 1,058 kg/L
  incerteza absoluta = límite superior − límite inferior = 1,058 − 1,000 = 0,057 kg/L → 0,06 kg/L
  valor representativo:  1,029 → 1,03 kg/L

Redondeo:  Δρ → 0,06 ; ρ → 1,03
Resultado (Tabla 5):  ρ₂ = (1,03 ± 0,06) kg/L
Intervalo:  1,03 ∓ 0,06 = [0,97 ; 1,09] kg/L
```

### A.4 Comparación de los dos métodos

```
ρ₁ = (0,95 ± 0,04) kg/L   →  [0,91 ; 0,99]
ρ₂ = (1,03 ± 0,06) kg/L   →  [0,97 ; 1,09]

Zona de superposición:  [0,97 ; 0,99] kg/L   →   los dos métodos son COMPATIBLES.

Diferencia entre valores representativos:
  |ρ₂ − ρ₁| = |1,03 − 0,95| = 0,08 kg/L

Suma de las incertezas:
  0,04 + 0,06 = 0,10 kg/L

Como 0,08 < 0,10, los intervalos se superponen y los resultados son compatibles.
```

### A.5 Criterio de redondeo y cifras significativas

```
1. La incerteza (error absoluto) se redondea a 1 cifra significativa:
     Δρ₁ = 0,0441 kg/L → 0,04 kg/L
     Δρ₂ = 0,057  kg/L → 0,06 kg/L

2. El valor representativo se redondea a la misma posición decimal que su incerteza:
     ρ₁ = 0,9462 kg/L con Δρ = 0,04 → 0,95 kg/L
     ρ₂ = 1,029  kg/L con Δρ = 0,06 → 1,03 kg/L

3. Densidad expresada en kg/L (equivale a g/mL y a g/cm³); 1 g/mL = 1 kg/L.

4. En los pasos intermedios se conservan 1–2 cifras de más y se redondea solo el
   resultado final, para no arrastrar error de redondeo.
```

### A.6 Figuras (se incorporan al informe final)

Las siguientes figuras se agregan a este Anexo al armar la versión final del informe:

- **Figura 1 — Planilla de cálculo del método de la pendiente** (`densidad_pendiente_Excel.jpeg`): Tablas 1 a 5 de la planilla `Planilla_arquimedes_Laboratorio.xlsx` (datos A y B, procesamiento de datos, resultados de la regresión lineal y resultados finales).
- **Figura 2 — Gráfico `(P − D)` vs `(Vol_d·g)`** (`densidad_pendiente.jpeg`): puntos experimentales y recta de ajuste lineal por el origen; la pendiente de la recta es la densidad del líquido.

---

**Fuentes utilizadas:**

- *Guía de Trabajos Prácticos de Fluidos — Principio de Arquímedes* (`Arquímides_V3.pdf`, U.D.B. Física) — teoría, procedimiento y anexo estadístico (pendiente, `R²`, `s`, `s_m`).
- Planilla de cálculo de cátedra `Planilla_arquimedes_Laboratorio.xlsx` — procesamiento de datos y regresión lineal del método de la pendiente.
- *Reglamento para la realización de los trabajos prácticos en los Laboratorios de Física* y *Criterios para la realización de los informes de los Trabajos Prácticos* (U.D.B. Física, en `laboratorio/`).
- TP N°1 — Mediciones y Errores (informe propio, 1ra concurrencia) — criterios de propagación de incertezas y de redondeo.
