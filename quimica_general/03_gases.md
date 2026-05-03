# UT3 — El Estado Gaseoso
**Química General R1091 · UTN FRBA · Ingeniería Mecánica**

---

## Introducción conceptual

Los gases son el estado de agregación más simple de modelar matemáticamente. A diferencia de sólidos y líquidos, un gas **ocupa todo el volumen disponible**, no tiene forma propia y su comportamiento puede describirse con unas pocas ecuaciones universales cuando las condiciones de presión y temperatura lo permiten.

Para un ingeniero mecánico, los gases aparecen en:
- Cámaras de combustión de motores (mezclas de aire y combustible)
- Sistemas neumáticos e hidráulicos
- Tuberías de transporte de gas natural
- Recipientes a presión (análisis de seguridad, posibilidad de explosión)
- Procesos de soldadura (gases protectores: Ar, CO₂)

> **Analogía contable:** así como en contabilidad existe una ecuación que debe cumplirse siempre (`Activo = Pasivo + PN`), los gases obedecen a una ecuación de estado que es siempre válida: `P·V = n·R·T`. Cada variable es como un rubro del balance — si cambias uno, los demás se ajustan para que la ecuación se cumpla.

---

## Propiedades generales de los gases

Los gases están constituidos por moléculas que pueden ser:

- **Sustancias simples diatómicas:** H₂, N₂, O₂, F₂, Cl₂
- **Gases nobles monoatómicos:** He, Ne, Ar (columna 18 de la tabla periódica)
- **Compuestos gaseosos a 25°C y 1 atm:** CO₂, H₂O (vapor), CH₄, HCl, NH₃, SO₂, NO, NO₂

Propiedades macroscópicas comunes a todos los gases:

```
┌─────────────────────────────────────────────────────────────┐
│ • Ocupan cualquier recipiente (toman su forma y volumen)    │
│ • Son compresibles (reducen volumen al aumentar presión)    │
│ • Se mezclan completamente entre sí (mezclas homogéneas)   │
│ • Densidad baja (mucho menor que sólidos y líquidos)       │
│ • Las moléculas se mueven aleatoriamente y ejercen presión │
│   al chocar contra las paredes del recipiente              │
└─────────────────────────────────────────────────────────────┘
```

---

## Variables de estado de un gas

El estado de cualquier gas queda completamente definido por cuatro variables:

| Variable | Símbolo | Unidades más usadas |
|---|---|---|
| Presión | P | atm, hPa, mmHg (Torr), Pa |
| Volumen | V | L (litros), dm³, m³ |
| Temperatura | T | K (Kelvin — siempre) |
| Cantidad de materia | n | mol |

**Conversión de temperatura — regla de oro:**

```
T (K) = t (°C) + 273,15

  0°C  →  273,15 K   (condición normal de temperatura)
100°C  →  373,15 K
 25°C  →  298,15 K   (temperatura ambiente estándar)
  0 K  → -273,15°C   (cero absoluto — temperatura mínima posible)
```

**Equivalencias de presión:**

```
1 atm = 1013,25 hPa = 760 mmHg = 760 Torr = 101 325 Pa
```

**Condiciones Normales de Presión y Temperatura (CNPT):**

`T = 273,15 K (0°C)` y `P = 1 atm`

---

## Gas ideal vs. gas real

```
GAS IDEAL                          GAS REAL
─────────────────────────────────────────────────────────────
• Moléculas con volumen            • Moléculas tienen volumen
  despreciable (masa puntual)        propio (apreciable a P alta)

• Sin fuerzas entre moléculas      • Existen fuerzas atractivas
  (ni atracción ni repulsión)        y repulsivas entre moléculas

• Choques perfectamente elásticos  • Choques con pérdida de E

• Cumple PV = nRT en TODAS         • Cumple PV ≈ nRT solo a
  las condiciones P y T              P baja y T alta
```

> En la práctica: todos los gases se comportan idealmente a **presiones bajas y temperaturas altas**. Para presiones altas o temperaturas muy bajas hay que usar la ecuación de Van der Waals.

---

## Teoría Cinético Molecular (TCM)

La TCM explica el comportamiento de los gases ideales a nivel microscópico. Sus postulados:

1. Los gases están formados por partículas (moléculas) que se tratan como iguales.
2. Las moléculas se mueven al azar y en línea recta; los choques entre sí y con las paredes son **elásticos** (sin pérdida de energía cinética promedio).
3. El volumen total de las moléculas es **despreciable** respecto al volumen del recipiente.
4. **No existen** fuerzas atractivas ni repulsivas entre moléculas.
5. La **energía cinética promedio** es proporcional a la temperatura absoluta:

`Ec = (1/2)·m·v²` y `Ec_promedio ∝ T`

Consecuencias:
- La **presión** del gas se debe a los choques de moléculas contra las paredes.
- A igual temperatura, gases distintos tienen la misma Ec promedio → los más livianos se mueven más rápido.

---

## Leyes de los gases ideales

Para derivar las leyes, se fijan dos de las cuatro variables (P, V, T, n) y se estudia la relación entre las otras dos.

### Ley de Boyle-Mariotte — Proceso Isotérmico (T y n constantes)

> "A temperatura constante, la presión y el volumen de una masa de gas son inversamente proporcionales."

```
   P↑  →  V↓          P↓  →  V↑

        P₁·V₁ = P₂·V₂ = k
```

**Gráfico (isoterma):** P vs. V → hipérbola; P vs. 1/V → línea recta.

**Ejemplo:** Una muestra de Cl₂ ocupa 946 mL a 726 mmHg. ¿Qué presión necesita para que el volumen baje a 154 mL?

```
P₁·V₁ = P₂·V₂
726 mmHg × 946 mL = P₂ × 154 mL
P₂ = 726 × 946 / 154 = 4 460 mmHg
```

---

### Ley de Charles-Gay Lussac — Proceso Isobárico (P y n constantes)

> "A presión constante, el volumen de un gas es directamente proporcional a su temperatura absoluta."

```
   T↑  →  V↑          T↓  →  V↓

        V/T = k    →    V₁/T₁ = V₂/T₂
```

**Gráfico:** V vs. T(K) → línea recta que al extrapolar llega a V=0 en T=0K.

---

### 2ª Ley de Charles-Gay Lussac — Proceso Isocórico (V y n constantes)

> "A volumen constante, la presión de un gas es directamente proporcional a su temperatura absoluta."

```
   T↑  →  P↑   (más energía cinética → más choques → más presión)

        P/T = k    →    P₁/T₁ = P₂/T₂
```

**Ejemplo:** Una bombita de Ar pasa de 18°C a 85°C con P inicial = 1,20 atm. ¿P final?

```
T₁ = 18 + 273,15 = 291,15 K
T₂ = 85 + 273,15 = 358,15 K

P₂ = P₁ × T₂/T₁ = 1,20 atm × 358,15/291,15 = 1,48 atm
```

---

### Ley de Avogadro — (P y T constantes)

> "A presión y temperatura constantes, el volumen de un gas es directamente proporcional al número de moles."

```
V/n = k    →    V₁/n₁ = V₂/n₂
```

También: "Volúmenes iguales de gases distintos en las mismas condiciones P y T contienen igual número de moléculas."

Consecuencia directa → **relación estequiométrica volumen a volumen:**
```
3 H₂(g) + N₂(g)  →  2 NH₃(g)
3 mol       1 mol      2 mol
3 volúmenes 1 volumen  2 volúmenes  (a igual P y T)
```

---

## Ecuación General de los Gases Ideales

Unificando las cuatro leyes anteriores:

```
         n · T
V ∝  ─────────      →      P · V = n · R · T
           P
```

**`P·V = n·R·T`**

Donde **R** es la Constante Universal de los Gases:

| Valor de R | Unidades |
|---|---|
| `0,08206` | L·atm / (mol·K) |
| `8,314` | J / (mol·K) |
| `1,987` | cal / (mol·K) |

> La R se llama constante de **Regnault** o de los gases ideales. Eligiendo R = 0,08206 L·atm/(mol·K), se trabaja directamente con P en atm, V en litros, T en K.

**Cálculo de R a partir de CNPT:** a 0°C (273,15 K) y 1 atm, 1 mol de gas ideal ocupa 22,414 L:

`R = P·V / (n·T) = (1 atm × 22,414 L) / (1 mol × 273,15 K) = 0,08206 L·atm/(mol·K)`

---

## Volumen Molar de un Gas

**Volumen Molar Normal (VMN):** volumen que ocupa 1 mol de cualquier gas ideal a CNPT (0°C, 1 atm):

**`V_MN = 22,414 L/mol ≈ 22,4 L/mol`**

```
GAS IDEAL a CNPT

   1 mol H₂   →  22,4 L
   1 mol O₂   →  22,4 L
   1 mol CO₂  →  22,4 L   (todos iguales, independiente del gas)
   1 mol N₂   →  22,4 L
```

Esto no ocurre con líquidos y sólidos, donde el volumen molar depende de la sustancia.

---

## Ecuación de Estado

Para un mismo gas que pasa de condiciones (1) a condiciones (2):

```
P₁·V₁       P₂·V₂
──────── = ──────── = R  (constante)
n₁·T₁       n₂·T₂
```

Si la cantidad de gas no cambia (n₁ = n₂), se simplifica:

```
P₁·V₁     P₂·V₂
──────  =  ──────
  T₁          T₂
```

Esta es la forma más útil para problemas donde el gas cambia de condiciones.

**Casos especiales derivados:**

| Proceso | Constantes | Ecuación resultante |
|---|---|---|
| Isotérmico | T, n | `P₁·V₁ = P₂·V₂` (Boyle) |
| Isobárico | P, n | `V₁/T₁ = V₂/T₂` (Charles) |
| Isocórico | V, n | `P₁/T₁ = P₂/T₂` (Gay-Lussac) |

---

## Densidad y Masa Molar del Gas

De `P·V = n·R·T`, sabiendo que `n = m/M` (masa / masa molar):

**Densidad del gas ideal:**

```
         P · M
d =  ─────────      [g/L]
         R · T
```

**Masa molar de un gas a partir de su densidad:**

```
         d · R · T
M =  ─────────────      [g/mol]
           P
```

> Esto es extraordinariamente útil: midiendo P, T y densidad de un gas desconocido, se puede determinar su masa molar sin saber su composición química.

**Ejemplo:** Un contenedor de 2,1 L contiene 4,65 g de gas a 1 atm y 27°C. ¿Masa molar?

```
d = m/V = 4,65 g / 2,1 L = 2,21 g/L
T = 27 + 273,15 = 300,15 K

M = d·R·T/P = 2,21 × 0,08206 × 300,15 / 1 = 54,5 g/mol
```

---

## Mezclas de Gases — Ley de Dalton de las Presiones Parciales

Todas las mezclas gaseosas son homogéneas. El caso más conocido es el aire: 21% O₂ + 79% N₂ (en volumen).

**Ley de Dalton:** "La presión ejercida por cada gas de una mezcla (presión parcial) es igual a la que ejercería si ocupara solo el recipiente."

```
P_total = p_A + p_B + p_C + ...
```

**Fracción molar** del componente i:

```
           n_i
X_i  =  ────────        (adimensional, entre 0 y 1)
          n_total
```

Relación entre presión parcial y fracción molar:

```
p_i = X_i · P_total
```

La suma de fracciones molares es siempre 1: `ΣX_i = 1`

**Ejemplo:** Gas natural con 8,24 mol CH₄, 0,421 mol C₂H₆ y 0,116 mol C₃H₈. P total = 1,37 atm. ¿Presión parcial del propano?

```
n_total = 8,24 + 0,421 + 0,116 = 8,777 mol

X_propano = 0,116 / 8,777 = 0,01322

p_propano = 0,01322 × 1,37 atm = 0,0181 atm
```

---

## Difusión Gaseosa — Ley de Graham

**Difusión:** tendencia de un gas a ocupar homogéneamente todo el espacio disponible.
**Efusión:** escape de un gas a través de un orificio muy pequeño.

La TCM establece que a igual temperatura, todos los gases tienen igual Ec promedio:

```
Ec_A = Ec_B

(1/2)·m_A·v_A² = (1/2)·m_B·v_B²
```

**Ley de Graham:**

```
v_A       M_B
─────  =  ─────    (velocidades inversamente proporcionales a √masa molar)
v_B       M_A
```

A igual T: el gas más liviano se mueve más rápido.

```
Ejemplo: NH₃ (M=17 g/mol) vs. HCl (M=36,5 g/mol)

v_NH₃ / v_HCl = √(36,5/17) = √2,15 = 1,46

NH₃ se difunde 1,46 veces más rápido que HCl.
```

---

## Gases Reales — Ecuación de Van der Waals

A presiones altas, los gases reales se desvían del comportamiento ideal porque:
1. El volumen de las moléculas **no** es despreciable.
2. Existen **fuerzas de atracción** entre moléculas que reducen la presión efectiva.

**Ecuación de Van der Waals:**

```
    ⎛       a·n² ⎞
    ⎜  P + ───── ⎟ · (V - n·b) = n·R·T
    ⎝        V²  ⎠
```

- `P + a·n²/V²` → presión **corregida** (la presión real es menor porque las atracciones frenan las moléculas antes de los choques)
- `V - n·b` → volumen **corregido** (se resta el volumen propio de las moléculas)

Las constantes **a** y **b** son características de cada gas:

| Gas | a (L²·atm/mol²) | b (L/mol) |
|---|---|---|
| H₂ | 0,244 | 0,0266 |
| N₂ | 1,39 | 0,0391 |
| O₂ | 1,36 | 0,0318 |
| CO₂ | 3,59 | 0,0427 |
| NH₃ | 4,17 | 0,0371 |
| H₂O | 5,46 | 0,0305 |

> A presiones bajas: `a·n²/V² → 0` y `n·b → 0`, entonces Van der Waals se reduce a PV = nRT (gas ideal).

---

## Estequiometría con Gases

Los gases permiten conectar estequiometría con volúmenes medibles. El esquema general:

```
                             PV = nRT
                                ↕
MASA (g) ──÷ M──→ MOLES ──→ MOLES ──×M──→ MASA (g)
                     ↓                        ↑
                  VOLUMEN (L)              VOLUMEN (L)
                  (via 22,4 L/mol a CNPT
                   o via PV=nRT en otras condiciones)
```

**Ejemplo integrador:** Reacción `CS₂(l) + O₂(g) → CO₂(g) + SO₂(g)`. Si reaccionan 520 g de CS₂:

```
Paso 1 — Balancear: CS₂ + 3O₂ → CO₂ + 2SO₂

Paso 2 — Moles de CS₂:
  M(CS₂) = 12 + 2×32 = 76 g/mol
  n(CS₂) = 520/76 = 6,842 mol

Paso 3 — Moles de O₂ necesarios (relación 1:3):
  n(O₂) = 6,842 × 3 = 20,53 mol

Paso 4 — Volumen de O₂ en CNPT:
  V(O₂) = 20,53 mol × 22,4 L/mol = 459,8 L

Paso 5 — Volumen de CO₂ en CNPT (relación 1:1 con CS₂):
  V(CO₂) = 6,842 × 22,4 = 153,3 L

Paso 6 — Volumen de SO₂ en CNPT (relación 2:1 con CS₂):
  V(SO₂) = 6,842 × 2 × 22,4 = 306,6 L
```

---

## Ejercicios resueltos

### Ejercicio 1 — Ley general (PV=nRT)
¿Qué volumen ocupan 49,8 g de HCl gaseoso en CNPT?

```
M(HCl) = 1 + 35,5 = 36,5 g/mol
n = 49,8 g / 36,5 g·mol⁻¹ = 1,364 mol

PV = nRT → V = nRT/P
V = 1,364 × 0,08206 × 273,15 / 1
V = 30,6 L
```

### Ejercicio 2 — Masa molar por densidad
Un gas tiene densidad 2,39 g/L a 100°C y 700 Torr. ¿Masa molar?

```
T = 100 + 273,15 = 373,15 K
P = 700 Torr × (1 atm / 760 Torr) = 0,9211 atm

M = d·R·T/P = 2,39 × 0,08206 × 373,15 / 0,9211
M = 79,4 g/mol
```

### Ejercicio 3 — Ecuación de estado
Un recipiente de 0,452 dm³ contiene gas a 628,1 hPa y 87°C.
a) ¿Volumen a 1 atm y 0°C?  b) ¿Cuántos moles?

```
P₁ = 628,1 hPa × (1 atm / 1013,25 hPa) = 0,6199 atm
V₁ = 0,452 L
T₁ = 87 + 273,15 = 360,15 K

P₂ = 1 atm   T₂ = 273,15 K   n₁ = n₂ (masa constante)

a) V₂ = V₁ × P₁/P₂ × T₂/T₁
   V₂ = 0,452 × (0,6199/1) × (273,15/360,15)
   V₂ = 0,213 L

b) n = P₁V₁/(RT₁) = (0,6199 × 0,452) / (0,08206 × 360,15)
   n = 9,48 × 10⁻³ mol
```

### Ejercicio 4 — Mezcla de gases (Dalton)
Mezcla: 16 g H₂, 12 g He, 16 g CH₄. P total = 24 atm. ¿Presiones parciales?

```
n(H₂)  = 16/2  = 8 mol
n(He)  = 12/4  = 3 mol
n(CH₄) = 16/16 = 1 mol
n_total = 12 mol

X(H₂)  = 8/12 = 0,667   →  p(H₂)  = 0,667 × 24 = 16 atm
X(He)  = 3/12 = 0,250   →  p(He)  = 0,250 × 24 =  6 atm
X(CH₄) = 1/12 = 0,083   →  p(CH₄) = 0,083 × 24 =  2 atm
```

---

## Tabla resumen de ecuaciones

| Ley / Concepto | Condición | Ecuación |
|---|---|---|
| Boyle-Mariotte | T, n cte. | `P·V = cte.` → `P₁·V₁ = P₂·V₂` |
| Charles | P, n cte. | `V/T = cte.` → `V₁/T₁ = V₂/T₂` |
| Gay-Lussac | V, n cte. | `P/T = cte.` → `P₁/T₁ = P₂/T₂` |
| Avogadro | P, T cte. | `V/n = cte.` → `V₁/n₁ = V₂/n₂` |
| Gas ideal | general | `P·V = n·R·T` |
| Ecuación de estado | masa cte. | `P₁V₁/T₁ = P₂V₂/T₂` |
| Densidad | — | `d = P·M / (R·T)` |
| Masa molar | — | `M = d·R·T / P` |
| Dalton | mezcla | `P_total = Σ p_i` ; `p_i = X_i · P_total` |
| Graham | igual T | `v_A/v_B = √(M_B/M_A)` |
| Van der Waals | gas real | `(P + an²/V²)(V - nb) = nRT` |
| Vol. molar normal | CNPT | `V_MN = 22,4 L/mol` |

---

## Errores comunes

1. **Temperatura en °C en lugar de K.** Si usás t(°C) en PV=nRT el resultado es un disparate. Siempre convertir: `T(K) = t(°C) + 273,15`.

2. **Unidades de P y R incompatibles.** Si P está en hPa y usás R = 0,08206 (L·atm/mol·K), el resultado es incorrecto. Convertir P a atm, o usar R = 8,314 J/(mol·K) con P en Pa.

3. **Confundir presión total con presión parcial** en mezclas. La ecuación PV=nRT con P_total y n_total da el comportamiento global; con p_i y n_i da el gas i.

4. **Omitir el balanceo** antes de un problema estequiométrico con gases. El paso 1 es siempre balancear.

5. **Usar 22,4 L/mol fuera de CNPT.** El volumen molar de 22,4 L/mol es solo válido a 0°C y 1 atm. En otras condiciones, usar `V = nRT/P`.

6. **Confundir difusión con efusión.** Difusión = mezcla de dos gases en contacto; efusión = escape por orificio pequeño. Ambas siguen la ley de Graham.

---

## Mapa conceptual

```
              GASES
               │
    ┌──────────┴──────────┐
    │                     │
IDEALES               REALES
(P baja, T alta)      (P alta, T baja)
    │                     │
  PV=nRT            Van der Waals
    │              (P + an²/V²)(V-nb)=nRT
    │
    ├─── Variables de estado: P, V, T, n
    │
    ├─── Leyes (fijando 2 variables)
    │       Boyle   → P↔V (T,n cte.)
    │       Charles → V↔T (P,n cte.)
    │       G.L.    → P↔T (V,n cte.)
    │       Avogadro→ V↔n (P,T cte.)
    │
    ├─── Volumen molar normal → 22,4 L/mol (CNPT)
    │
    ├─── Densidad/Masa molar  → d = PM/RT
    │
    ├─── Mezclas → Ley de Dalton → p_i = X_i·P_total
    │
    ├─── Difusión → Ley de Graham → v_A/v_B = √(M_B/M_A)
    │
    └─── Estequiometría con gases → mol ↔ L (via PV=nRT o 22,4)
```

---

*Fuentes: Módulo IV "El Estado Gaseoso" — Ing. Ángel R. Zambrino (Química General, 2019) · Diapositivas de cátedra "2 GASES BETTY corregido" (Prof. Betty) · Guía de Ejercicios y Problemas — Química General (Cataldi/Zambrino, 2020).*
