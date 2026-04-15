# Unidad 3 — Límites

---

## ¿Para qué sirve esto?

El límite es el concepto que hace que el cálculo exista. Sin él, no hay derivada, no hay integral, no hay análisis matemático.

La pregunta que responde el límite no es *"¿qué vale `f(x)` en `x₀`?"* sino *"¿hacia qué valor se dirige `f(x)` cuando `x` se acerca a `x₀`?"*. La distinción es sutil pero fundamental: una función puede tender hacia un valor en un punto sin ni siquiera estar definida en ese punto.

> **Analogía contable:** imaginá que analizás el flujo de caja de una empresa justo antes de su cierre. No te importa el saldo del día del cierre (puede ser 0 por liquidación), sino *hacia qué valor se dirigía* el flujo en los días previos. Eso es el límite: el comportamiento tendencial, no el valor puntual.

La unidad cubre cinco bloques:
1. Concepto intuitivo y definición formal (épsilon-delta)
2. Límites laterales
3. Propiedades y álgebra de límites
4. Límites con variable tendiente a infinito
5. Formas indeterminadas y técnicas de resolución

---

## Bloque 1 — Concepto de límite

### Motivación intuitiva

Considerá la función `f(x) = (x² − 1) / (x − 1)`. En `x = 1` está **indefinida** (denominador = 0). Pero miremos qué pasa cerca de `x = 1`:

```
  x       f(x)
  0.9     1.9
  0.99    1.99
  0.999   1.999
  0.9999  1.9999
  ↓         ↓
  1       (no definida)
  ↑         ↑
  1.0001  2.0001
  1.001   2.001
  1.01    2.01
  1.1     2.1
```

Desde ambos lados, `f(x)` se acerca a **2**. El límite es 2, aunque `f(1)` no exista.

¿Por qué? Porque `(x² − 1)/(x − 1) = (x+1)(x−1)/(x−1) = x + 1` para todo `x ≠ 1`. Y `x + 1 → 2` cuando `x → 1`.

### Definición informal

```
lim f(x) = L
x → a
```

Se lee: *"el límite de f(x) cuando x tiende a a es L"*.

Significa: **f(x) se acerca arbitrariamente a L cuando x se acerca a a**, sin importar si `f(a)` existe o qué valor tiene.

### Definición formal (épsilon-delta)

Esta es la definición rigurosa que da sustento a todo lo anterior. Aparece en exámenes conceptuales y en demostraciones de propiedades.

> **Definición:** `lim f(x) = L` cuando `x → a` si y solo si:
>
> para todo `ε > 0` existe `δ > 0` tal que:
> si `0 < |x − a| < δ` entonces `|f(x) − L| < ε`

Desglosado:

```
"para todo ε > 0"        → cualquier margen de error en y que se exija
"existe δ > 0"           → se puede encontrar un margen en x suficientemente pequeño
"0 < |x − a| < δ"        → x está en el entorno reducido de a (≠ a, dentro de δ)
"|f(x) − L| < ε"         → f(x) está dentro del margen ε alrededor de L
```

Gráficamente:

```
  f(x)
   │                    ─ ─ L + ε
   │              ┌────────────────────────────
   │         ─ ─ L│ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
   │              └────────────────────────────
   │                    ─ ─ L − ε
   │
   └──────────────┬──┬──┬────────── x
               a−δ  a  a+δ
                   ↑
            punto excluido (entorno reducido)
```

Para que el límite sea `L`, la gráfica de `f` tiene que entrar por la "banda horizontal" `(L−ε, L+ε)` siempre que `x` esté en la "banda vertical" `(a−δ, a+δ)` sin tocar `a`.

> **Analogía contable:** ε es la tolerancia de error en el resultado (como ±$100 en un presupuesto). δ es el ajuste en los parámetros de entrada (como los días de variación). La definición dice: *para cualquier tolerancia en el resultado que te pidan, yo puedo ajustar los parámetros lo suficiente para cumplirla*.

---

## Bloque 2 — Límites laterales

### Motivación

Algunas funciones tienen comportamientos distintos según desde qué lado nos acercamos. Para identificar esto se usan los **límites laterales**.

```
f(x)
 │       /
 │    ╱╱
 │  ─ ─ ─ ─ ─         límite por izquierda ≠ límite por derecha
 │              ╲╲
 │                ─ ─ ─
 └────────────────────── x
                a
```

### Límite lateral por la derecha

```
lim f(x) = L⁺
x → a⁺
```

`x` se acerca a `a` viniendo **desde la derecha** (x > a, x ↓ a).

Formalmente: para todo `ε > 0` existe `δ > 0` tal que si `0 < x − a < δ` entonces `|f(x) − L⁺| < ε`.

### Límite lateral por la izquierda

```
lim f(x) = L⁻
x → a⁻
```

`x` se acerca a `a` viniendo **desde la izquierda** (x < a, x ↑ a).

Formalmente: para todo `ε > 0` existe `δ > 0` tal que si `0 < a − x < δ` entonces `|f(x) − L⁻| < ε`.

### Relación entre límite bilateral y laterales

> **Teorema fundamental:**
>
> `lim f(x) = L` si y solo si `lim f(x) = L` y `lim f(x) = L`
> `x → a`                    `x → a⁺`           `x → a⁻`
>
> Es decir: el límite (bilateral) existe y vale L **si y solo si los dos límites laterales existen y son iguales**.

```
  Situación                  Conclusión
  ─────────────────────────────────────────────────────────
  L⁻ = L⁺ = L             El límite existe y vale L
  L⁻ ≠ L⁺                 El límite NO existe
  Solo uno de los dos       El límite NO existe
  existe
```

### Ejemplo 1 — Función a trozos

```
        │ x + 1    si x < 2
f(x) = ─┤
        │ x² − 1   si x ≥ 2
```

Calcular `lim f(x)` cuando `x → 2`.

```
Límite por izquierda (x → 2⁻, usamos x + 1):
  lim (x + 1) = 2 + 1 = 3
  x → 2⁻

Límite por derecha (x → 2⁺, usamos x² − 1):
  lim (x² − 1) = 4 − 1 = 3
  x → 2⁺

L⁻ = L⁺ = 3  →  lim f(x) = 3  ✓
                  x → 2
```

Notar que `f(2) = 2² − 1 = 3` también. En este caso el límite coincide con el valor de la función — pero eso es casualidad, no la regla.

### Ejemplo 2 — Límite que no existe

```
        │ 1    si x < 0
g(x) = ─┤
        │ −1   si x ≥ 0
```

```
lim g(x) = 1    (desde la izquierda)
x → 0⁻

lim g(x) = −1   (desde la derecha)
x → 0⁺

L⁻ ≠ L⁺  →  el límite en x = 0 NO EXISTE
```

Gráficamente (función escalón):

```
  g(x)
   │
 1 │─────────○
   │          0
  −│─────────────────── x
   │          ●─────────
−1 │
```

### Ejemplo 3 — Valor absoluto

La función `f(x) = |x| / x` (signo de x) tiene comportamiento distinto a cada lado del 0:

```
Para x > 0:  |x|/x = x/x = 1
Para x < 0:  |x|/x = −x/x = −1

lim |x|/x = 1    lim |x|/x = −1
x → 0⁺           x → 0⁻

→ el límite en 0 no existe.
```

### Límites laterales con variable tendiente a infinito

Los límites laterales también aplican cuando `x → ±∞`:

- `lim f(x)` con `x → +∞`: x crece sin cota.
- `lim f(x)` con `x → −∞`: x decrece sin cota.

Estos se tratan en el Bloque 4.

---

## Bloque 3 — Propiedades y álgebra de límites

Este bloque es el núcleo de la unidad — la clase hizo mucho énfasis en él porque **todas las técnicas de cálculo de límites se derivan de estas propiedades**.

### Hipótesis de partida

Para todas las propiedades a continuación se asume que los siguientes límites **ya existen**:

```
lim f(x) = L    lim g(x) = M
x → a           x → a
```

### Propiedades fundamentales

**P1 — Límite de una constante:**

```
lim c = c      (una constante no cambia sin importar a dónde va x)
x → a
```

**P2 — Límite de la identidad:**

```
lim x = a
x → a
```

**P3 — Suma y diferencia:**

```
lim [f(x) ± g(x)] = L ± M
x → a
```

**P4 — Producto:**

```
lim [f(x) · g(x)] = L · M
x → a
```

**P5 — Cociente:**

```
lim [f(x) / g(x)] = L / M     siempre que M ≠ 0
x → a
```

**P6 — Constante por función:**

```
lim [c · f(x)] = c · L
x → a
```

**P7 — Potencia:**

```
lim [f(x)]ⁿ = Lⁿ    (n entero positivo)
x → a
```

**P8 — Raíz:**

```
lim ⁿ√f(x) = ⁿ√L    (con L > 0 si n es par)
x → a
```

**P9 — Composición (continuidad):**

Si `lim g(x) = M` y `f` es continua en `M`:
```
lim f(g(x)) = f(M) = f(lim g(x))
x → a                  x → a
```

> **Analogía contable:** las propiedades son como las reglas de las cuentas T: podés separar el debe y el haber, combinar asientos, aplicar un factor a toda una cuenta — cada operación tiene su regla y las reglas son consistentes. Una vez que sabés las reglas, podés calcular cualquier cosa armando la operación adecuada.

### Uso combinado — cómo calcular límites de polinomios

Para un **polinomio** `P(x)`, el límite se calcula simplemente **evaluando**:

```
lim P(x) = P(a)
x → a
```

Demostración esquemática (usando P1, P2, P3, P6, P7):

```
lim (3x² − 2x + 5) = lim 3x² − lim 2x + lim 5    (P3)
x → 2                  x→2       x→2      x→2

= 3·(lim x)² − 2·(lim x) + 5                       (P6, P7, P1)
      x→2           x→2

= 3·(2)² − 2·(2) + 5                                (P2)
= 12 − 4 + 5 = 13
```

### Uso combinado — funciones racionales

Para `R(x) = P(x)/Q(x)` con `Q(a) ≠ 0`:

```
lim R(x) = P(a) / Q(a)    si Q(a) ≠ 0
x → a
```

Si `Q(a) = 0`, aparece una **forma indeterminada** — ver Bloque 5.

### Teorema del Sandwich (o del emparedado)

Si en un entorno de `a` se cumple:

```
g(x) ≤ f(x) ≤ h(x)
```

y además `lim g(x) = lim h(x) = L`, entonces:

```
lim f(x) = L
x → a
```

```
    h(x) ─────────┐
                  │ → L
    f(x) ─────────┤
                  │ → L
    g(x) ─────────┘

   (f queda "atrapada" entre g y h, que convergen al mismo valor)
```

**Ejemplo clásico:** `lim x·sen(1/x)` cuando `x → 0`.

```
−1 ≤ sen(1/x) ≤ 1  para todo x ≠ 0

→  −|x| ≤ x·sen(1/x) ≤ |x|

Como lim |x| = 0 y lim (−|x|) = 0, por Sandwich:
     x→0              x→0

lim x·sen(1/x) = 0
x → 0
```

### Unicidad del límite

> **Teorema:** si el límite existe, es **único**.

No puede haber dos valores `L₁ ≠ L₂` que sean simultáneamente el límite de `f` en `a`.

---

## Bloque 4 — Límites con variable tendiente a infinito

### Límite finito cuando x → ±∞

```
lim f(x) = L
x → +∞
```

Significa: `f(x)` se acerca a `L` cuando `x` crece sin cota.

**Definición formal:** para todo `ε > 0` existe `M > 0` tal que si `x > M` entonces `|f(x) − L| < ε`.

```
  f(x)
   │
   │         ─ ─ L + ε
   │     ─────────────────────────────────
   │ ─ ─ L
   │     ─────────────────────────────────
   │         ─ ─ L − ε
   └──────────────────────────────────── x
                         →  +∞
```

Cuando este límite existe y es finito, la recta `y = L` es una **asíntota horizontal** de `f`. Ver Unidad de Asíntotas.

### Propiedades esenciales al infinito

**Límites básicos que conviene memorizar:**

```
lim  1/xⁿ = 0    (n > 0)      la potencia "aplasta" al denominador
x→+∞

lim  xⁿ = +∞    (n > 0)      un polinomio crece sin cota
x→+∞

lim  aˣ = +∞    (a > 1)      exponencial crece más rápido que cualquier potencia
x→+∞

lim  aˣ = 0     (0 < a < 1)  exponencial decrece a 0
x→+∞

lim  ln(x) = +∞              el logaritmo crece pero más lento que xⁿ
x→+∞

lim  ln(x) = −∞              el logaritmo "explota" negativamente
x→0⁺
```

### Jerarquía de infinitos

Cuando `x → +∞`, estas funciones crecen en el siguiente orden (de menor a mayor velocidad):

```
ln(x)  ≪  xᵅ  ≪  aˣ  ≪  x!   (para α > 0, a > 1)

Ejemplos concretos:
  ln(x) ≪ √x ≪ x ≪ x² ≪ x³ ≪ 2ˣ ≪ eˣ
```

Esta jerarquía es fundamental para resolver formas `∞/∞`.

> **Analogía contable:** es como comparar el crecimiento de distintas inversiones. El interés compuesto continuo (`eˣ`) eventualmente supera a cualquier crecimiento polinomial, sin importar el exponente. Un fondo de renta fija (`ln x`) siempre quedará atrás.

### Técnica — División por el término dominante

Para `lim P(x)/Q(x)` cuando `x → ±∞`, donde P y Q son polinomios:

**Regla práctica:** el comportamiento está determinado por el **cociente de los términos de mayor grado**.

```
      aₙxⁿ + ... + a₀        aₙ
lim  ──────────────────  =  ──── · lim x^(n−m)
x→∞  bₘxᵐ + ... + b₀        bₘ   x→∞
```

Casos:

```
Si n < m:   lim = 0           (numerador "pierde" al denominador)
Si n = m:   lim = aₙ/bₘ      (cociente de coeficientes principales)
Si n > m:   lim = ±∞          (numerador "gana", el signo depende de aₙ/bₘ)
```

**Procedimiento formal:** dividir numerador y denominador por la potencia más alta del denominador.

**Ejemplo:**

```
     3x² − 2x + 1            ÷ x²         3 − 2/x + 1/x²
lim  ──────────────── = lim  ─────── = lim ──────────────────
x→∞  5x² + x − 4             ÷ x²    x→∞  5 + 1/x − 4/x²

   3 − 0 + 0     3
= ─────────── = ───
   5 + 0 − 0     5
```

### Límites infinitos (resultado infinito)

```
lim f(x) = +∞
x → a
```

Significa: `f(x)` crece sin cota cuando `x` se acerca a `a`.

**Definición formal:** para todo `M > 0` existe `δ > 0` tal que si `0 < |x − a| < δ` entonces `f(x) > M`.

Gráficamente corresponde a una **asíntota vertical** en `x = a`.

```
  f(x)
   │      ↑  ↑
   │      │  │
   │   ↑  │  │  ↑
   │   │  │  │  │
   └───┼──┼──┼──┼─── x
          a
```

**Regla de signos para cocientes:**

```
c/0⁺ = +∞    (c > 0 dividido por algo positivo pequeñísimo)
c/0⁻ = −∞    (c > 0 dividido por algo negativo pequeñísimo)
```

**Ejemplo:** `lim 1/(x−2)` cuando `x → 2`:

```
Por derecha (x → 2⁺): x − 2 → 0⁺  →  1/(x−2) → +∞
Por izquierda (x → 2⁻): x − 2 → 0⁻  →  1/(x−2) → −∞

Los laterales son distintos (±∞): el límite bilateral no existe, pero hay A.V. en x = 2.
```

---

## Bloque 5 — Formas indeterminadas y técnicas de resolución

### ¿Qué es una forma indeterminada?

Cuando al evaluar `f(a)` se obtiene una expresión sin valor matemático definido. Las formas indeterminadas **no tienen un valor predeterminado** — requieren análisis.

```
┌─────────────────────────────────────────────────────────────────┐
│  Las 7 formas indeterminadas                                    │
│                                                                  │
│   0/0     ∞/∞     0·∞     ∞−∞     0⁰     1^∞     ∞⁰           │
└─────────────────────────────────────────────────────────────────┘
```

> **Nota importante:** `∞/∞` no es "1" y `∞ − ∞` no es "0". Son formas que *podrían* dar cualquier resultado — la carrera entre numerador y denominador decide quién gana.

> **Analogía contable:** es como ver dos cuentas que crecen simultáneamente (ingresos y gastos). Si ambas tienden a ∞, no podés saber el resultado neto (`∞ − ∞`) hasta analizar *cuál crece más rápido*. El resultado puede ser ganancia, pérdida o equilibrio.

### Forma `0/0` — Técnicas

#### Técnica 1 — Factorización algebraica

Es la primera herramienta a usar. Si numerador y denominador tienen un factor común que se anula en `a`, se cancela.

**Ejemplo clásico:**

```
     x² − 4       (x − 2)(x + 2)
lim ─────────── = lim ─────────────── = lim (x + 2) = 4
x→2   x − 2      x→2    (x − 2)        x→2
```

El factor `(x − 2)` se cancela porque `x ≠ 2` (estamos en el entorno reducido).

**Ejemplo con cúbica:**

```
     x³ − 1       (x − 1)(x² + x + 1)
lim ─────────── = lim ─────────────────── = lim (x² + x + 1) = 3
x→1   x − 1      x→1      (x − 1)          x→1
```

Recordar la factorización: `a³ − b³ = (a − b)(a² + ab + b²)`.

#### Técnica 2 — Racionalización

Cuando hay raíces cuadradas, se multiplica por el **conjugado**.

```
Conjugado de (√A − B) es (√A + B)
Conjugado de (√A − √B) es (√A + √B)
```

**Ejemplo:**

```
     √(x + 4) − 2                     √(x+4) − 2   √(x+4) + 2
lim  ──────────────── = lim           ──────────── · ──────────
x→0        x           x→0                x         √(x+4) + 2

            (x + 4) − 4            x
= lim  ─────────────────── = lim ──────────────────
x→0    x · (√(x+4) + 2)   x→0   x · (√(x+4) + 2)

            1                1        1
= lim  ──────────────── = ──────── = ───
x→0    √(x + 4) + 2       √4 + 2     4
```

#### Técnica 3 — División por factor común (fracciones complejas)

Cuando aparecen fracciones dentro de fracciones, se simplifica primero.

**Ejemplo:**

```
     1/x − 1/2             (2 − x) / (2x)        2 − x       2x        −1
lim  ──────────── = lim    ──────────────── = lim ─────── · ───── = lim ────
x→2    x − 2       x→2        x − 2           x→2  2x       x−2    x→2   2x

= −1/4
```

### Forma `∞/∞` — División por término dominante

Ya vista en el Bloque 4. El procedimiento es dividir por la mayor potencia del **denominador**.

**Ejemplo con raíz:**

```
     3x − 2              ÷ x          3 − 2/x
lim  ────────────── = lim ──── = lim ──────────────
x→∞  √(4x² + 1)          ÷ x    x→∞  √(4 + 1/x²)

                          3 − 0       3
=                        ────────── = ───
                          √(4 + 0)    2
```

Atención: al dividir `√(4x² + 1)` por `x` (con `x > 0`):

```
√(4x² + 1) / x = √((4x² + 1)/x²) = √(4 + 1/x²)
```

### Forma `0 · ∞` — Conversión a cociente

Se convierte en `0/0` o `∞/∞` reescribiendo:

```
f(x) · g(x) = f(x) / (1/g(x))    o    g(x) / (1/f(x))
```

**Ejemplo:**

```
lim x · ln(x)   cuando x → 0⁺
```

```
= lim  ln(x) / (1/x) = lim  ln(x) · x = ?
  x→0⁺                  x→0⁺

Usamos: lim x · ln(x)  →  reescribir como  lim  ln(x) / (1/x)
        x→0⁺                               x→0⁺

Forma ∞/∞ → aplicar L'Hôpital (ver más abajo):
(d/dx ln x) / (d/dx 1/x) = (1/x) / (−1/x²) = −x → 0

→  lim x · ln(x) = 0
   x→0⁺
```

### Forma `∞ − ∞` — Conversión a cociente

Se intenta llevar a `0/0` o `∞/∞` mediante algebraización.

**Ejemplo:**

```
lim (1/(x−1) − 2/(x²−1))   cuando x → 1
x→1

Denominador común: x² − 1 = (x−1)(x+1)

= lim  (x+1)/(x²−1) − 2/(x²−1) = lim  (x+1−2)/(x²−1) = lim  (x−1)/((x−1)(x+1))
  x→1                              x→1                   x→1

= lim  1/(x+1) = 1/2
  x→1
```

### Límites notables — tablas de referencia

Estos límites se demuestran con herramientas más avanzadas (Sandwich, series) pero **se usan directamente** en el curso.

#### Límites trigonométricos

```
lim  sen(x)/x = 1          ← EL más importante de todos
x→0

lim  (1 − cos x)/x = 0
x→0

lim  (1 − cos x)/x² = 1/2
x→0

lim  tan(x)/x = 1
x→0

lim  arcsen(x)/x = 1
x→0
```

**Uso de sen(x)/x:** si el argumento del seno no es exactamente `x`, se reescribe:

```
lim  sen(3x) / x = lim  3 · sen(3x)/(3x) = 3 · 1 = 3
x→0                x→0

lim  sen(ax) / sen(bx) = lim  [sen(ax)/(ax)] · (ax) / [sen(bx)/(bx)] · (bx) = a/b
x→0                      x→0
```

**Demostración geométrica esquemática de sen(x)/x → 1:**

```
En el círculo unitario, para 0 < x < π/2:

  sen x < x < tan x      (area del triángulo ≤ area del sector ≤ area del triángulo externo)

  → 1 > sen(x)/x > cos(x)

Como cos(x) → 1 cuando x → 0, por Sandwich: sen(x)/x → 1 ✓
```

#### Número e — Límites fundamentales

```
lim  (1 + 1/x)ˣ = e ≈ 2,71828...        (variable x → +∞)
x→∞

lim  (1 + x)^(1/x) = e                  (variable x → 0)
x→0

lim  (eˣ − 1)/x = 1
x→0

lim  ln(1 + x)/x = 1
x→0

lim  (aˣ − 1)/x = ln(a)    (a > 0, a ≠ 1)
x→0
```

**Variante generalizada de `e`:**

```
lim  (1 + α(x))^(β(x)) = e^(lim α(x)·β(x))
x→a

siempre que α(x) → 0 y β(x) → ∞ (forma 1^∞)
```

**Ejemplo:**

```
lim  (1 + 2/x)^(3x)   cuando x → ∞
x→∞

α(x) = 2/x → 0,   β(x) = 3x → ∞
α(x)·β(x) = (2/x)·(3x) = 6

→  lim = e⁶
```

### Formas `0⁰`, `∞⁰`, `1^∞` — Logaritmización

Para límites de la forma `[f(x)]^g(x)`, se usa la técnica de logaritmizar:

```
Sea L = lim [f(x)]^g(x)
x→a

Entonces  ln(L) = lim g(x)·ln(f(x))
                  x→a
```

Y se resuelve el límite del producto (que suele ser `0·∞` convertible a `0/0`).

**Ejemplo (forma `1^∞`):**

```
lim  x^(1/(x−1))   cuando x → 1
x→1

Forma: 1^∞

Sea L = lim x^(1/(x−1))
        x→1

ln(L) = lim  ln(x)/(x−1)    [forma 0/0]
        x→1

Por L'Hôpital: (1/x)/1 = 1/x → 1 cuando x → 1

→  ln(L) = 1  →  L = e¹ = e
```

### Regla de L'Hôpital

> **Teorema:** si `lim f(x)/g(x)` es de la forma `0/0` o `∞/∞`, y si `f` y `g` son diferenciables en un entorno de `a`, y `lim f'(x)/g'(x)` existe, entonces:
>
> ```
> lim  f(x)/g(x) = lim  f'(x)/g'(x)
> x→a              x→a
> ```

**Importante:** se derivan numerador y denominador **por separado** — no es la derivada del cociente.

**Cuándo usar L'Hôpital:**
- Solo en formas `0/0` o `∞/∞`.
- Si sigue siendo indeterminada, se puede aplicar repetidamente.
- Si *no* es indeterminada, no se aplica (da resultados incorrectos).

**Ejemplo:**

```
     ln(x)      forma ∞/∞ cuando x → +∞
lim  ──────
x→∞    x

Aplicando L'Hôpital: derivada de ln(x) es 1/x; derivada de x es 1.

= lim  (1/x)/1 = lim  1/x = 0
  x→∞            x→∞

→  ln(x) crece MUCHO más lento que x (confirma la jerarquía de infinitos)
```

**Ejemplo con forma `0/0`:**

```
     eˣ − 1 − x        forma 0/0
lim  ──────────────
x→0       x²

1ra aplicación: (eˣ − 1)/(2x)    → sigue 0/0

2da aplicación: eˣ/2 → 1/2 cuando x → 0

→  lim = 1/2
```

---

## Ejemplos resueltos completos

### Ejemplo 1 — Polinomio, evaluación directa

```
lim  (x³ − 3x + 2)   cuando x → −1
x→−1

= (−1)³ − 3(−1) + 2 = −1 + 3 + 2 = 4
```

### Ejemplo 2 — Racional, forma 0/0 por factorización

```
     x² − 5x + 6       (x − 2)(x − 3)
lim  ──────────────── = lim ──────────────── = lim (x − 2) = 1
x→3    x − 3            x→3   (x − 3)          x→3
```

### Ejemplo 3 — Racional con tendencia a infinito

```
     2x³ + x          ÷ x³         2 + 1/x²
lim  ──────────── = lim ───── = lim ──────────────
x→∞  x³ − 5           ÷ x³    x→∞  1 − 5/x³

= (2 + 0)/(1 − 0) = 2
```

### Ejemplo 4 — Racionalización

```
     x − 9
lim  ──────────────    cuando x → 9
x→9  √x − 3

Multiplicar por (√x + 3)/(√x + 3):

   (x − 9)(√x + 3)      (x − 9)(√x + 3)
= lim ─────────────── = lim ───────────────── = lim (√x + 3) = 6
  x→9   (x − 9)         x→9    (x − 9)         x→9
```

### Ejemplo 5 — Límite notable sen(x)/x

```
     sen(5x)         sen(5x)
lim  ──────────── = lim ──────────── · (5/5) = 5 · lim sen(5x)/(5x) = 5 · 1 = 5
x→0     x           x→0    x                     x→0
```

### Ejemplo 6 — Función a trozos, verificar existencia

```
         │ x² + 1    si x ≤ 0
f(x) = ──┤
         │ 2x + 1    si x > 0
```

`lim f(x)` cuando `x → 0`:

```
Por izquierda: lim (x² + 1) = 0 + 1 = 1
               x→0⁻

Por derecha:   lim (2x + 1) = 0 + 1 = 1
               x→0⁺

L⁻ = L⁺ = 1  →  lim f(x) = 1  ✓
                  x→0
```

(Además `f(0) = 0² + 1 = 1`, así que `f` es continua en 0 — noción que se formaliza en la unidad de continuidad.)

### Ejemplo 7 — L'Hôpital repetido

```
     x − sen(x)      forma 0/0
lim  ────────────
x→0      x³

1ra: (1 − cos x)/(3x²)   → 0/0

2da: sen(x)/(6x)          → 0/0

3ra: cos(x)/6 → 1/6 cuando x → 0

→  lim = 1/6
```

---

## Mapa conceptual de técnicas

```
¿Qué forma da la sustitución directa?
          │
          ├── Valor definido → ESE ES EL LÍMITE (fin)
          │
          ├── 0/0 ──────────────────────────────────────────────────────┐
          │                                                              │
          │    ¿Hay factores comunes?  → sí → FACTORIZAR y cancelar     │
          │    ¿Hay raíces?            → sí → RACIONALIZAR (conjugado)  │
          │    ¿Hay fracciones?        → sí → DENOMINADOR COMÚN         │
          │    Ninguna funciona        →      L'HÔPITAL                  │
          │                                                              │
          ├── ∞/∞ ─────────────────────────────────────────────────────┘│
          │    Polinomios              → DIVIDIR por mayor potencia denom│
          │    Con exponenciales/log   → L'HÔPITAL                       │
          │                                                               │
          ├── 0·∞  → convertir: f·g = f/(1/g)  → cae en 0/0 o ∞/∞     │
          │                                                               │
          ├── ∞−∞  → algebraizar → denominador común → cae en 0/0       │
          │                                                               │
          └── 0⁰, 1^∞, ∞⁰  → LOGARITMIZAR → ln L = lim g·ln(f) → 0·∞ ─┘
```

---

## Resumen y tabla de referencia

| Concepto | Definición clave | Notas |
|---|---|---|
| Límite bilateral | `f(x) → L` desde ambos lados de `a` | L no depende de `f(a)` |
| Límite lateral | Solo desde un lado (`a⁺` o `a⁻`) | Para funciones a trozos y módulos |
| Condición de existencia | `L⁻ = L⁺ = L` | Si difieren, el límite no existe |
| Propiedad suma | `lim(f+g) = lim f + lim g` | Requiere que ambos límites existan |
| Propiedad cociente | `lim(f/g) = lim f / lim g` | Solo si `lim g ≠ 0` |
| Límite en ∞ | `f(x) → L` con `x` sin cota | Indica asíntota horizontal `y = L` |
| Límite infinito | `f(x) → ±∞` con `x → a` | Indica asíntota vertical `x = a` |
| Forma `0/0` | Indeterminada | Factorizar, racionalizar, L'Hôpital |
| Forma `∞/∞` | Indeterminada | Dividir por término dominante, L'Hôpital |
| sen(x)/x | Límite notable → 1 | Solo cuando x → 0, en radianes |
| `(1+1/x)ˣ` | Límite notable → e | Cuando x → ∞ |
| L'Hôpital | `lim f/g = lim f'/g'` | Solo para `0/0` o `∞/∞` |

---

## Errores comunes a evitar

1. **Evaluar la función en el punto y listo, sin verificar la forma.** Si `f(a)` existe y es finito, sí se puede usar directamente. Pero si da `0/0` o `∞/∞`, no es el límite — es una señal de que hay trabajo que hacer.

2. **Cancelar `x/x = 1` sin verificar `x ≠ 0`.** En el entorno reducido `x ≠ a`, por eso la cancelación es válida. Pero hay que ser consciente de que se está trabajando en `x ≠ a`.

3. **Aplicar L'Hôpital cuando no hay forma indeterminada.** `lim (x+1)/(x+2)` cuando `x → 1` no es indeterminado — da `2/3` directamente. Si se aplica L'Hôpital igual, da `1/1 = 1`, que es incorrecto.

4. **Confundir la derivada del cociente con L'Hôpital.** L'Hôpital dice `lim f'/g'`, no `lim (f/g)'`. Son distintas cosas.

5. **Ignorar el signo en límites laterales infinitos.** `lim 1/(x−2)` por derecha es `+∞` y por izquierda es `−∞`. Si no se distingue el signo, se pierde información sobre la asíntota vertical.

6. **Dividir por `x` sin cuidar el signo cuando `x → −∞`.** Si `x < 0`, entonces `x = −√(x²)`, y `√(x²)/x = −1`. Ignorar esto da signos incorrectos.

7. **Asumir que `∞ − ∞ = 0` o `∞/∞ = 1`.** Son formas indeterminadas — el resultado depende de la velocidad relativa de crecimiento.

8. **Olvidar que el límite ignora el valor en el punto.** Si `f(a)` no está definida o vale algo distinto al límite, eso no afecta al límite. El límite pregunta qué pasa *alrededor* de `a`, no *en* `a`.

---

*Fuentes: Cronograma A1191 2026 (cátedra AM1 UTN FRBA); Apunte funciones (FC) — Cavallaro; clases 13/04/2026 y 20/04/2026.*
