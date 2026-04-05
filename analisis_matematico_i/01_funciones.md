# Unidad 1 — Funciones

---

## Repaso rápido: lo que ya sabés

Esta sección es un resumen comprimido del apunte de Cavallaro. Si ya lo tenés claro, usala como referencia rápida y salteá directo a las secciones de secantes e hiperbólicas.

### Concepto de función

Una función `f: A → B` asigna a cada elemento del **dominio** `A` exactamente un elemento de la **imagen** `B`. Lo clave: *exactamente uno* — si un valor de x produce dos valores de y, no es función.

- **Dom(f):** todos los x válidos (restricciones: denominador ≠ 0, raíz de no-negativo, log de positivo).
- **Im(f):** todos los y que realmente toma la función.

### Familias elementales — síntesis

| Función | Forma | Dom | Im | Clave |
|---|---|---|---|---|
| Lineal | `y = mx + b` | ℝ | ℝ | Pendiente `m = tan(φ)` |
| Cuadrática | `y = ax² + bx + c` | ℝ | depende de `a` | Vértice en `xv = -b/2a` |
| Exponencial | `y = aˣ` (a>0, a≠1) | ℝ | (0, +∞) | Siempre positiva, pasa por (0,1) |
| Logarítmica | `y = logₐ(x)` | (0,+∞) | ℝ | Inversa de la exponencial |

**El número e:** `e = lim (1 + 1/n)ⁿ ≈ 2,71828...` — aparece naturalmente en crecimiento continuo y, como verás más adelante, en las funciones hiperbólicas.

**Función inversa:** `f⁻¹` existe si y solo si `f` es estrictamente monótona. Gráficamente, es la reflexión de `f` sobre la recta `y = x`.

**Composición:** `(f ∘ g)(x) = f(g(x))` — primero se aplica `g`, luego `f`.

---

## Parte 1: El círculo trigonométrico y los radianes

### Por qué radianes y no grados

Los grados son una convención histórica (360 elegido porque es divisible por muchos números). Los **radianes** son la medida *natural* del ángulo: el ángulo en radianes es directamente la longitud del arco sobre el radio.

```
θ (rad) = longitud de arco / radio
```

En una circunferencia de radio 1, el ángulo en radianes *es* la longitud del arco. Esto hace que todas las fórmulas del cálculo salgan limpias — las derivadas de sin y cos funcionan solo en radianes.

**Conversión:**
```
radianes = grados × π/180
grados   = radianes × 180/π

π rad = 180°     →    1 rad ≈ 57,3°
```

### El círculo trigonométrico

El círculo trigonométrico es la circunferencia de radio 1 centrada en el origen. Cualquier punto `P = (a, b)` sobre él define un ángulo `θ` medido desde el semieje x positivo en sentido antihorario.

```
              π/2
          (0, 1)
              |
              |
(-1,0) ───────┼──────── (1,0)
   π          |              0 = 2π
              |
          (0,-1)
             3π/2
```

Las definiciones directamente desde el círculo:

```
sin(θ) = b   (coordenada y del punto)
cos(θ) = a   (coordenada x del punto)
tan(θ) = b/a = sin(θ)/cos(θ)
```

La identidad fundamental sale directo de Pitágoras sobre el círculo unitario:

```
sin²(θ) + cos²(θ) = 1
```

### Ángulos clave en el círculo (en radianes)

```
 Ángulo  | Radianes |  sin   |  cos   |  tan
─────────┼──────────┼────────┼────────┼──────────
   0°    |    0     |   0    |   1    |   0
  30°    |   π/6   |  1/2   |  √3/2  |  √3/3
  45°    |   π/4   |  √2/2  |  √2/2  |   1
  60°    |   π/3   |  √3/2  |  1/2   |  √3
  90°    |   π/2   |   1    |   0    |  ∞ (indef.)
 120°    |  2π/3   |  √3/2  | -1/2   | -√3
 135°    |  3π/4   |  √2/2  | -√2/2  |  -1
 150°    |  5π/6   |  1/2   | -√3/2  | -√3/3
 180°    |   π     |   0    |  -1    |   0
 270°    |  3π/2   |  -1    |   0    |  ∞ (indef.)
 360°    |  2π     |   0    |   1    |   0
```

**Truco para memorizar los valores:** en el primer cuadrante, sin crece de 0 a 1 pasando por √2/2 y √3/2. Para cos, al revés. La raíz del número de la tabla (1, 2, 3) dividida por 2 da los valores: `√1/2, √2/2, √3/2`.

### Signos por cuadrante

```
         II  |  I
    sin +  |  todo +
    cos −  |
    ────────┼────────
    sin −  |  sin −
    cos −  |  cos +
        III |  IV
```

Mnemotecnia: **"Todos Saben Calcular Tangentes"** (T, S, C, T — en I todo, en II solo Sin, en III solo Cos... no funciona, la clásica es "ASTC" en inglés). Mejor recordarlo desde el círculo: en I todos positivos; en II x es negativo → cos negativo; en III ambos negativos; en IV y es negativo → sin negativo.

---

## Parte 2: La familia de las secantes

El apunte de Cavallaro define estas funciones en una línea y las abandona. Pero aparecen en derivadas, integrales y en ingeniería (óptica, mecánica ondulatoria). Vale la pena entenderlas bien.

### Las tres funciones recíprocas

Las funciones de la familia de las secantes son los **recíprocos** de las tres funciones básicas:

```
sec(x)  = 1 / cos(x)       ← recíproco del coseno
csc(x)  = 1 / sin(x)       ← recíproco del seno  (cosecante)
cot(x)  = cos(x) / sin(x)  ← recíproco de la tangente (cotangente)
```

> **Ojo con la notación:** `sec` no es `arccos`. El arco-coseno (`arccos` o `cos⁻¹`) es la función inversa. La secante (`sec`) es el recíproco. Son cosas completamente distintas.

---

### Secante: `sec(x) = 1/cos(x)`

**Intuición:** donde el coseno vale 1, la secante vale 1. Donde el coseno se acerca a 0, la secante explota hacia ±∞. Donde el coseno vale -1, la secante vale -1.

```
Dom(sec) = ℝ − { π/2 + kπ, k ∈ ℤ }   (donde cos = 0)
Im(sec)  = (−∞, −1] ∪ [1, +∞)         (nunca entre −1 y 1)
Período  = 2π
```

Gráfica (ASCII):

```
   y
   |      |              |
 3 |   ╱  |  ╲        ╱  |  ╲
 2 | ╱    |    ╲    ╱    |    ╲
 1 |──────|──────╲╱──────|──────  ← mínimos locales en cos=1
   |      |      /\      |
-1 |──────|────/──  \────|──────  ← máximos locales en cos=−1
-2 |    ╲ |  /        \  |  /
-3 |      |              |
   ├──────┼──────────────┼────── x
 -π/2    π/2           3π/2
     ↑                ↑
  asíntota          asíntota
```

**Propiedad clave:** la secante nunca toma valores entre -1 y 1. Esto tiene sentido: si `sec = 1/cos`, y `|cos| ≤ 1`, entonces `|sec| ≥ 1`.

---

### Cosecante: `csc(x) = 1/sin(x)`

Exactamente el mismo comportamiento que la secante pero desfasado π/2 (porque csc es al seno lo que sec es al coseno).

```
Dom(csc) = ℝ − { kπ, k ∈ ℤ }          (donde sin = 0)
Im(csc)  = (−∞, −1] ∪ [1, +∞)
Período  = 2π
```

```
   y
   |  |              |
 3 | ╱|╲           ╱|╲
 2 |╱ |  ╲       ╱  |  ╲
 1 |──|──── ─── ────|────  ← mínimos en sin=1 (π/2)
   |  |      ╲╱     |
-1 |──|──────/\─────|────  ← máximos en sin=−1 (3π/2)
-2 |  |    /    \   |
-3 |  |              |
   ├──┼──────────────┼───── x
   0  π             2π
   ↑                ↑
 asíntota        asíntota
```

---

### Cotangente: `cot(x) = cos(x)/sin(x)`

La cotangente es el recíproco de la tangente, pero tiene algunas diferencias importantes:

```
Dom(cot) = ℝ − { kπ, k ∈ ℤ }   (donde sin = 0, igual que csc)
Im(cot)  = ℝ                     (a diferencia de sec y csc, toma todos los valores)
Período  = π                     (igual que tan)
```

La tangente crece de −∞ a +∞ en cada período. La cotangente **decrece** de +∞ a −∞:

```
   y
+∞ |╲          ╲
 2 |  ╲          ╲
 1 |    ╲          ╲
 0 |─────╲──────────╲───  ← cero en π/2, 3π/2...
-1 |      ╲          ╲
-2 |        ╲          ╲
−∞ |          ╲
   ├────────────────────── x
   0     π         2π
   ↑                ↑
asíntota         asíntota
```

Ceros de `cot`: donde `cos(x) = 0`, es decir en `x = π/2 + kπ`.

---

### Identidades con la familia de las secantes

Las identidades pitagóricas de la trigonometría básica tienen versiones para cada familia recíproca:

**Identidad base:**
```
sin²(x) + cos²(x) = 1
```

**Dividiendo por cos²(x):**
```
tan²(x) + 1 = sec²(x)
```

**Dividiendo por sin²(x):**
```
1 + cot²(x) = csc²(x)
```

Estas tres identidades son equivalentes — son la misma relación expresada de tres formas. La segunda y tercera aparecen mucho en integrales trigonométricas.

---

### Tabla resumen de la familia

| Función | Definición | Dom | Im | Período | Asíntotas |
|---|---|---|---|---|---|
| `sec(x)` | `1/cos(x)` | `ℝ − {π/2 + kπ}` | `(−∞,−1]∪[1,+∞)` | `2π` | `x = π/2 + kπ` |
| `csc(x)` | `1/sin(x)` | `ℝ − {kπ}` | `(−∞,−1]∪[1,+∞)` | `2π` | `x = kπ` |
| `cot(x)` | `cos(x)/sin(x)` | `ℝ − {kπ}` | `ℝ` | `π` | `x = kπ` |

---

## Parte 3: Funciones sinusoidales hiperbólicas

Estas funciones **no están en el apunte de Cavallaro** pero aparecen en AM1 (integración, ecuaciones diferenciales), en física (catenaria, ondas) y en ingeniería mecánica (pandeo de vigas, transferencia de calor). Son el contenido nuevo de esta sección.

### ¿De dónde salen?

Tomá la función exponencial `eˣ`. Cualquier función puede descomponerse en su parte **par** (simétrica respecto al eje y) y su parte **impar** (antisimétrica):

```
eˣ = (eˣ + e⁻ˣ)/2  +  (eˣ − e⁻ˣ)/2
      ───────────────    ───────────────
       parte par          parte impar
       (= cosh x)         (= sinh x)
```

Eso es todo. Las funciones hiperbólicas son exactamente las partes par e impar de la exponencial. No hay misterio adicional.

```
cosh(x) = (eˣ + e⁻ˣ) / 2       ← "coseno hiperbólico"
sinh(x) = (eˣ − e⁻ˣ) / 2       ← "seno hiperbólico"
```

La "h" de hiperbólico hace referencia a la **hipérbola**, del mismo modo que sin/cos/tan se relacionan con el círculo. Las funciones trigonométricas ordinarias parametrizan el círculo unitario `x² + y² = 1`; las hiperbólicas parametrizan la hipérbola unitaria `x² − y² = 1`.

---

### Coseno hiperbólico: `cosh(x)`

```
cosh(x) = (eˣ + e⁻ˣ) / 2
```

Es el **promedio** de `eˣ` y `e⁻ˣ`. Como suma dos positivos y divide por 2, siempre es ≥ 1.

```
Dom(cosh) = ℝ
Im(cosh)  = [1, +∞)
Paridad:    función PAR   →  cosh(−x) = cosh(x)
Mínimo:     cosh(0) = 1
```

Gráfica:
```
   y
 4 |          ╲     ╱
 3 |           ╲   ╱
 2 |            ╲ ╱
 1 |─────────────●─────────────  ← mínimo en (0,1)
   |             |
   ├─────────────┼─────────────── x
                 0
```

> **La catenaria:** el cable eléctrico colgante que aparece en el apunte de Cavallaro (`y = eˣ + e⁻ˣ`) es exactamente `y = 2·cosh(x)`. La forma general de una catenaria es `y = a·cosh(x/a)`, donde `a` depende de la densidad del cable y la tensión horizontal. Es la curva que minimiza la energía potencial de una cuerda flexible colgada por sus extremos.

---

### Seno hiperbólico: `sinh(x)`

```
sinh(x) = (eˣ − e⁻ˣ) / 2
```

Es la **diferencia** de `eˣ` y `e⁻ˣ`. Cuando x > 0, `eˣ > e⁻ˣ` → resultado positivo. Cuando x < 0, al revés.

```
Dom(sinh) = ℝ
Im(sinh)  = ℝ        (toma todos los valores reales)
Paridad:    función IMPAR   →  sinh(−x) = −sinh(x)
Cero:       sinh(0) = 0
```

Gráfica:
```
   y
 4 |                  ╱
 2 |               ╱
   |─────────────●─────────────── x
-2 |          ╲
-4 |       ╲
```

La curva crece más rápido que cualquier polinomio (sigue al exponencial), pero a diferencia de `eˣ`, es impar (simétrica respecto al origen).

---

### Tangente hiperbólica: `tanh(x)`

```
tanh(x) = sinh(x) / cosh(x) = (eˣ − e⁻ˣ) / (eˣ + e⁻ˣ)
```

Como `|sinh(x)| < cosh(x)` para todo x, el cociente siempre está en (−1, 1).

```
Dom(tanh) = ℝ
Im(tanh)  = (−1, +1)        ← acotada, nunca llega a ±1
Paridad:    función IMPAR
Asíntotas horizontales: y = 1 (cuando x → +∞) y y = −1 (cuando x → −∞)
```

Gráfica:
```
   y
+1 |─────────────────────────────  ← asíntota
   |              ╱────────
   |          ╱
   |──────────────────────────────  x
   |      ╲
-1 |──────────────────────────────  ← asíntota
```

> `tanh` tiene la forma de la función sigmoide que se usa en redes neuronales. Es la versión hiperbólica de la tangente, y en muchos modelos físicos describe transiciones suaves entre dos estados estables.

---

### Las tres funciones recíprocas hiperbólicas

Exactamente como sec/csc/cot son recíprocos de cos/sin/tan, existen los recíprocos hiperbólicos:

```
sech(x)  = 1 / cosh(x) = 2 / (eˣ + e⁻ˣ)
csch(x)  = 1 / sinh(x) = 2 / (eˣ − e⁻ˣ)   (x ≠ 0)
coth(x)  = cosh(x) / sinh(x)                (x ≠ 0)
```

| Función | Dom | Im | Notas |
|---|---|---|---|
| `sech(x)` | ℝ | (0, 1] | Máximo en x=0, asíntota y=0 |
| `csch(x)` | ℝ − {0} | ℝ − {0} | Asíntota vertical en x=0 |
| `coth(x)` | ℝ − {0} | (−∞,−1)∪(1,+∞) | Asíntotas en x=0 e y=±1 |

---

### La identidad fundamental hiperbólica

La relación análoga a `sin² + cos² = 1` para las hiperbólicas es:

```
cosh²(x) − sinh²(x) = 1
```

**Demostración:**
```
cosh²(x) − sinh²(x)
= [(eˣ + e⁻ˣ)/2]² − [(eˣ − e⁻ˣ)/2]²
= [e²ˣ + 2 + e⁻²ˣ]/4 − [e²ˣ − 2 + e⁻²ˣ]/4
= 4/4
= 1  ✓
```

Dividiendo por `cosh²` o `sinh²` se obtienen las otras:
```
1 − tanh²(x) = sech²(x)
coth²(x) − 1 = csch²(x)
```

---

### Tabla de analogías: trigonométricas vs. hiperbólicas

| Trigonométrica | Hiperbólica | Diferencia clave |
|---|---|---|
| `sin²x + cos²x = 1` | `cosh²x − sinh²x = 1` | Signo cambia |
| `sin(−x) = −sin(x)` | `sinh(−x) = −sinh(x)` | Igual |
| `cos(−x) = cos(x)` | `cosh(−x) = cosh(x)` | Igual |
| `tan²x + 1 = sec²x` | `1 − tanh²x = sech²x` | Signo cambia |
| Im(sin) = [−1,1] | Im(sinh) = ℝ | Hiperbólico no acotado |
| Im(cos) = [−1,1] | Im(cosh) = [1,+∞) | Hiperbólico siempre ≥ 1 |
| Periódico | No periódico | Diferencia fundamental |

> La diferencia de signo en la identidad fundamental (`+1` vs `−1`) refleja exactamente la geometría: círculo (`x²+y²=1`) vs. hipérbola (`x²−y²=1`).

---

### Funciones hiperbólicas inversas (arcohiperbólicas)

Las funciones hiperbólicas inversas se pueden expresar con logaritmos naturales — esto es lo que las hace especialmente útiles en integración, donde aparecen como primitivas.

```
arcsinh(x) = ln( x + √(x² + 1) )              Dom: ℝ
arccosh(x) = ln( x + √(x² − 1) )              Dom: [1, +∞)
arctanh(x) = (1/2) · ln( (1+x)/(1−x) )        Dom: (−1, 1)
```

**¿Por qué logaritmos?** Porque `sinh(y) = x` implica `(eʸ − e⁻ʸ)/2 = x`, que es una ecuación cuadrática en `eʸ`, y al resolverla aparece el logaritmo naturalmente.

**Derivadas** (fundamentales para AM1):
```
d/dx [sinh(x)] = cosh(x)
d/dx [cosh(x)] = sinh(x)
d/dx [tanh(x)] = sech²(x) = 1 − tanh²(x)

d/dx [arcsinh(x)] = 1 / √(x² + 1)
d/dx [arccosh(x)] = 1 / √(x² − 1)
d/dx [arctanh(x)] = 1 / (1 − x²)
```

Comparar con las derivadas trigonométricas inversas — son casi iguales pero con signos distintos en la raíz (`x²+1` vs `1−x²`).

---

### Aplicaciones en ingeniería mecánica

- **Catenaria:** la forma de un cable, cadena o arco colgante es `y = a·cosh(x/a)`. También la forma óptima de un arco que soporta su propio peso.
- **Pandeo de columnas:** las soluciones de ecuaciones diferenciales de vigas bajo carga axial involucran `sinh` y `cosh`.
- **Transferencia de calor en aletas:** la temperatura a lo largo de una aleta de enfriamiento sigue un perfil de `cosh`.
- **Ondas en medios dispersivos:** la relación de dispersión de ondas de agua en profundidad finita involucra `tanh`.
- **Mecánica relativista:** la transformación de Lorentz se puede escribir con `sinh` y `cosh` del parámetro de rapidez.

---

## Resumen de fórmulas clave

**Familia de las secantes:**
```
sec(x)  = 1/cos(x)           tan²(x) + 1 = sec²(x)
csc(x)  = 1/sin(x)           1 + cot²(x) = csc²(x)
cot(x)  = cos(x)/sin(x)
```

**Funciones hiperbólicas:**
```
cosh(x) = (eˣ + e⁻ˣ)/2       cosh²(x) − sinh²(x) = 1
sinh(x) = (eˣ − e⁻ˣ)/2       1 − tanh²(x) = sech²(x)
tanh(x) = sinh(x)/cosh(x)
```

**Inversas hiperbólicas:**
```
arcsinh(x) = ln(x + √(x²+1))
arccosh(x) = ln(x + √(x²−1))    x ≥ 1
arctanh(x) = ½·ln((1+x)/(1−x))  |x| < 1
```

---

## Errores comunes a evitar

1. **Confundir `sec(x)` con `arccos(x)`.** Son opuestos en significado: `sec = 1/cos` (recíproco); `arccos` (inversa). La notación `cos⁻¹(x)` para arccos es fuente de confusión por esto.

2. **Asumir que `cosh` y `sinh` son periódicas.** No lo son. Se parecen a sin y cos en nombre y en las identidades, pero son funciones exponenciales — crecen sin límite.

3. **Olvidar que `Im(cosh) = [1, +∞)`.** `cosh(x) ≥ 1` siempre, nunca vale 0. En cambio `sinh` toma todos los valores reales.

4. **Confundir la identidad:** `cosh² − sinh² = 1`, no `sinh² + cosh² = 1`. El signo cambia respecto a la identidad circular.

5. **En el círculo trigonométrico:** el coseno es la coordenada x (abscisa) y el seno es la coordenada y (ordenada). El apunte de Cavallaro tiene una inversión en la descripción textual — las fórmulas `sin θ = b, cos θ = a` con `P=(a,b)` son las correctas.

6. **Los ángulos en radianes no llevan unidad escrita.** `sin(π/2)` está bien; `sin(π/2 rad)` es redundante. En cambio si usás grados, siempre escribís el símbolo °.
