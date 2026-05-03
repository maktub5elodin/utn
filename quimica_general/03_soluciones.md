# UT7 — Soluciones
**Química General R1091 · UTN FRBA · Ingeniería Mecánica**

---

## Introducción conceptual

Una **solución** es una mezcla homogénea de dos o más componentes. Es el estado en que más interactuamos con la materia en la vida real: el agua que tomamos, la nafta del motor, el acero (aleación), el aire que respiramos.

Para un ingeniero mecánico las soluciones aparecen en:
- Lubricantes y refrigerantes (mezclas de agua + anticongelante)
- Electrolitos de baterías (H₂SO₄ acuoso)
- Tratamientos superficiales (galvanoplastía: soluciones metálicas)
- Control de calidad de fluidos hidráulicos y de corte

> **Analogía contable:** una solución es como una cuenta bancaria mancomunada — el saldo total (masa de solución) es la suma del aporte de cada socio (soluto + solvente), y la "proporción de participación" de cada uno es la concentración. Las distintas expresiones de concentración son como distintas formas de reportar esa participación: en porcentaje, en cantidad de transacciones (moles), o en relación al fondo total.

---

## Componentes de una solución

| Componente | Definición | Ejemplo en agua salada |
|---|---|---|
| **Soluto** (st) | Sustancia presente en menor proporción; se disuelve | NaCl |
| **Solvente** (sv) | Sustancia presente en mayor proporción; disuelve al soluto | H₂O |
| **Solución** (sc) | La mezcla homogénea resultante | NaCl(ac) |

**Relación fundamental de masas:**

`m(sc) = m(st) + m(sv)`

**Características de toda solución:**
- Composición variable (se puede cambiar la proporción)
- Aspecto transparente (puede ser coloreada pero no turbia)
- El soluto está distribuido uniformemente y **no sedimenta**
- El soluto se puede recuperar por métodos físicos (destilación, evaporación, etc.)

---

## Clasificación por estado de agregación

Las soluciones no son solo líquidas. Pueden existir en los tres estados:

| Estado de la sc | Solvente | Soluto | Ejemplo |
|---|---|---|---|
| Gas | Gas | Gas | Aire (N₂ + O₂ + otros) |
| Líquido | Líquido | Gas | O₂ disuelto en agua |
| Líquido | Líquido | Líquido | Alcohol en agua |
| Líquido | Líquido | Sólido | NaCl en agua |
| Sólido | Sólido | Gas | H₂ en paladio |
| Sólido | Sólido | Líquido | Mercurio en plata (amalgama) |
| Sólido | Sólido | Sólido | Plata en oro (aleación) |

---

## Proceso de disolución

El soluto se dispersa entre las moléculas del solvente cuando las **fuerzas de atracción soluto–solvente** son similares o más intensas que las fuerzas soluto–soluto.

Regla general: **"lo semejante disuelve a lo semejante"**
- Solventes polares (agua) disuelven solutos polares o iónicos (NaCl, azúcar)
- Solventes apolares (benceno, hexano) disuelven solutos apolares (grasas, aceites)

---

## La concentración — concepto central

La **concentración** es la cantidad de soluto presente en una cantidad determinada de solvente o solución. Es una **propiedad intensiva** (no depende de cuánta solución tenés, sino de la proporción).

### Mapa de datos — qué necesito para calcular qué

```
                m(sv) — Masa de solvente (g o kg)
                    |
   %m/m ←───────── │ ──────────→  n(st) = m(st)/M(st)
                    │                         |
   m(st) ──────────┼──────────→  m(sc) = m(st) + m(sv)
   Masa de soluto   │                         |
                    │              V(sc) = m(sc) / ρ(sc)
   %m/v ←──────────│──────────→  Molaridad = n(st) / V(sc)[L]
                    │
              ρ(sc) — Densidad de la solución (g/cm³ o kg/L)
```

Las variables que siempre aparecen:
- `m(st)` — masa del soluto [g]
- `m(sv)` — masa del solvente [g]
- `m(sc) = m(st) + m(sv)` — masa de la solución [g]
- `V(sc) = m(sc) / ρ(sc)` — volumen de la solución [cm³ o L]
- `n(st) = m(st) / M(st)` — moles de soluto [mol]
- `M(st)` — masa molar del soluto [g/mol]
- `ρ(sc)` — densidad de la solución [g/cm³]

---

## Expresiones de concentración

### Concentraciones físicas (no requieren masa molar)

**% masa/masa (%m/m)**

```
          m(st) [g]
%m/m = ──────────────── × 100
          m(sc) [g]
```

Indica: cuántos gramos de soluto hay cada 100 g de solución.
Ejemplo: 20 %m/m → 20 g de st en 100 g de sc (y 80 g de sv).

---

**% masa/volumen (%m/v)**

```
          m(st) [g]
%m/v = ──────────────── × 100
         V(sc) [cm³]
```

Indica: cuántos gramos de soluto hay cada 100 cm³ de solución.
Ejemplo: 15 %m/v → 15 g de st en 100 cm³ de sc.
Muy usada en farmacia y laboratorio.

---

**% volumen/volumen (%v/v)**

```
         V(st) [cm³]
%v/v = ──────────────── × 100
         V(sc) [cm³]
```

Indica: cuántos cm³ de soluto hay cada 100 cm³ de solución.
Ejemplo: 14 %v/v → 14 cm³ de st en 100 cm³ de sc.
Usada para mezclas líquido-líquido (alcohol en agua, etc.).

---

### Concentraciones químicas (requieren masa molar del soluto)

**Molaridad (M)**

```
         n(st) [mol]
M = ───────────────────────
       V(sc) [litros]
```

Indica: cuántos moles de soluto hay por litro de solución.
Ejemplo: 4,5 M → 4,5 mol de st en 1 L de sc.
Es la más usada en química analítica y estequiometría.

---

**Molalidad (m)**

```
         n(st) [mol]
m = ───────────────────────
       m(sv) [kg]
```

Indica: cuántos moles de soluto hay por kilogramo de solvente.
Ejemplo: 2,5 m → 2,5 mol de st en 1 kg de sv.
No varía con la temperatura (depende de masas, no de volumen). Útil para propiedades coligativas.

---

**Fracción molar (X)**

```
           n(st)
X(st) = ─────────────────        X(sv) = 1 - X(st)
          n(st) + n(sv)
```

Indica: fracción del total de moles que corresponde al soluto. Adimensional (entre 0 y 1).
La suma de fracciones molares de todos los componentes es siempre 1.

---

### Tabla comparativa de expresiones

| Expresión | Fórmula | Unidad | Varía con T |
|---|---|---|---|
| %m/m | `m(st)/m(sc) × 100` | % | No |
| %m/v | `m(st)/V(sc) × 100` | g/100 cm³ | Sí (V cambia con T) |
| %v/v | `V(st)/V(sc) × 100` | % | Sí |
| Molaridad M | `n(st)/V(sc)[L]` | mol/L | Sí |
| Molalidad m | `n(st)/m(sv)[kg]` | mol/kg | No |
| Fracción molar X | `n(st)/(n(st)+n(sv))` | adimensional | No |

---

## Ejercicios resueltos — concentración

### Ejercicio 1 — Conversión %m/m y %m/v
600 g de solución acuosa, densidad 1,03 g/cm³, contiene 50,0 g de soluto.
Expresar en: a) %m/m   b) %m/v

```
a) %m/m:
   600 g sc ──→ 50,0 g st
   100 g sc ──→ x = 8,33 g st
   C = 8,33 %m/m

b) %m/v:
   V(sc) = m(sc)/ρ = 600 g / 1,03 g·cm⁻³ = 582,5 cm³
   582,5 cm³ sc ──→ 50,0 g st
   100 cm³ sc  ──→ x = 8,58 g st
   C = 8,58 %m/v
```

### Ejercicio 2 — De %m/m a Molaridad
Solución de KNO₃ al 18 %m/m, densidad 1,17 g/cm³.
a) Expresar en Molaridad.   b) ¿Qué masa de soluto hay en 500 g de solvente?

```
M(KNO₃) = 39,1 + 14 + 3×16 = 101,1 g/mol

a) Tomo base de cálculo: 100 g de sc (contiene 18 g de st y 82 g de sv)
   V(sc) = 100 g / 1,17 g·cm⁻³ = 85,5 cm³ = 0,0855 L
   n(st) = 18 g / 101,1 g·mol⁻¹ = 0,178 mol
   M = 0,178 mol / 0,0855 L = 2,08 mol/L  →  C = 2,08 M

b) m(sv) = 82 g en 100 g de sc
   82 g sv ──→ 18 g st
   500 g sv ──→ x = 109,8 g st
```

---

## Dilución

**Diluir** = agregar solvente a una solución para disminuir su concentración.

```
Solución concentrada (c)  +  solvente  →  Solución diluida (d)
```

Lo que se conserva: **la masa de soluto no cambia** (solo agregamos solvente).

Ley de dilución:

`V(c) · C(c) = V(d) · C(d)`

(válida para C en Molaridad, %m/v, o cualquier expresión basada en volumen)

**En masa** (C en %m/m):

`m(sc)c · C(c) = m(sc)d · C(d)`

**Variables que cambian al diluir:**

```
                  Al diluir:
  V(sc)  ────────→  aumenta
  m(sc)  ────────→  aumenta
  ρ(sc)  ────────→  disminuye
  C      ────────→  disminuye
  m(st)  ────────→  NO CAMBIA ← clave
  m(sv)  ────────→  aumenta
```

---

## Concentrar una solución

Dos formas:

1. **Agregar soluto:** m(sv) no varía — m(st) y m(sc) aumentan → C sube.
2. **Evaporar solvente:** m(st) no varía — m(sv) y m(sc) disminuyen → C sube.

---

## Mezcla de dos soluciones del mismo soluto

Cuando se mezclan dos soluciones 1 y 2 del mismo soluto:

```
m(st)_final  = m(st)_1 + m(st)_2
m(sv)_final  = m(sv)_1 + m(sv)_2
m(sc)_final  = m(sc)_1 + m(sc)_2

           m(sc)_final
ρ_final = ─────────────
           V(sc)_final
```

La concentración final se calcula con los valores totales.

---

## Saturación y solubilidad

### Tipos de solución según concentración relativa a la solubilidad

```
NO SATURADA   →  C < S   →  puede disolverse más soluto
SATURADA      →  C = S   →  en equilibrio con soluto sin disolver
SOBRESATURADA →  C > S   →  inestable, precipita con perturbación
```

**Solubilidad (S):** concentración de la solución saturada a una dada T y P.
Se expresa en `g(st) / 100 g(sv)` o también %m/m)sv.

### Efecto de la temperatura sobre la solubilidad

```
Sólidos en líquidos:   generalmente S ↑ cuando T ↑
                       (excepciones: NaCl casi no varía, Ce₂(SO₄)₃ baja)

Gases en líquidos:     S ↓ cuando T ↑  (efecto contrario)
```

> Analogía: un gas disuelto en líquido caliente "quiere escapar" — por eso las bebidas carbonatadas pierden el gas si se calientan.

### Ejercicio — Curvas de solubilidad (KNO₃)
Sistema: 300 g solución saturada de K₂Cr₂O₇ a 60°C (S = 50,5 %m/m)sv).
Se enfría a 20°C (S = 13,1 %m/m)sv). ¿Cuánto soluto precipita?

```
A 60°C → S = 50,5 g(st)/100 g(sv)
Base: m(sv)=100 g, m(st)=50,5 g, m(sc)=150,5 g

Escalar a 300 g de sc:
  150,5 g sc ──→ 50,5 g st   y   100 g sv
  300 g sc   ──→ x = 100,7 g st  y   199,3 g sv

A 20°C → S = 13,1 g(st)/100 g(sv)
El solvente (199,3 g sv) no cambia al enfriar:
  100 g sv ──→ 13,1 g st (queda disuelto)
  199,3 g sv ──→ x = 26,1 g st (queda disuelto)

Precipita = 100,7 g − 26,1 g = 74,6 g de K₂Cr₂O₇
```

---

## Solubilidad de gases en líquidos — Ley de Henry

La solubilidad de un gas en un líquido a temperatura constante es proporcional a la presión parcial del gas sobre el líquido:

`S_g = k_H · P_g`

Donde:
- `S_g` = solubilidad del gas [g/L o mol/L]
- `k_H` = constante de Henry (característica del gas y el solvente a una T dada)
- `P_g` = presión parcial del gas sobre el líquido [atm]

**Aplicaciones prácticas:**
- Descompresión en buceo (N₂ disuelto en sangre a alta presión)
- Carbonatación de bebidas (CO₂ a presión)
- Oxígeno disuelto en agua (vital para peces)

---

## Tabla resumen de ecuaciones

| Expresión | Fórmula | Comentario |
|---|---|---|
| Masa solución | `m(sc) = m(st) + m(sv)` | siempre |
| Volumen solución | `V(sc) = m(sc) / ρ(sc)` | con densidad en g/cm³ |
| Moles de soluto | `n(st) = m(st) / M(st)` | necesita M del soluto |
| %m/m | `m(st)/m(sc) × 100` | — |
| %m/v | `m(st)/V(sc)[cm³] × 100` | g/100cm³ |
| %v/v | `V(st)/V(sc) × 100` | líquidos |
| Molaridad | `n(st) / V(sc)[L]` | mol/L |
| Molalidad | `n(st) / m(sv)[kg]` | mol/kg |
| Fracción molar | `n(st) / (n(st)+n(sv))` | adimensional |
| Dilución | `V(c)·C(c) = V(d)·C(d)` | C en unidades compatibles |
| Henry | `S_g = k_H · P_g` | gases en líquidos |

---

## Errores comunes

1. **Confundir m(sc) con m(sv).** El denominador del %m/m es la masa de **solución** (st + sv), no del solvente. El denominador del %m/m)sv sí es el solvente — son distintas expresiones.

2. **Olvidar convertir cm³ a L** al calcular Molaridad. Si V(sc) = 250 cm³, en la fórmula de M va 0,250 L.

3. **Usar densidad como si fuera del soluto.** La densidad que se da en problemas es siempre de la **solución**, no del soluto.

4. **En dilución, suponer que el volumen final es la suma.** Para líquidos es una aproximación; el dato correcto es V(d) medido o calculado por densidad.

5. **No incluir el soluto al calcular la masa molar para convertir.** Si el soluto es KNO₃, M = M(K) + M(N) + 3×M(O) = 39,1 + 14 + 48 = 101,1 g/mol — no olvidar multiplicar los oxígenos.

6. **Confundir Molaridad (M) con Molalidad (m).** M usa volumen de solución en litros; m usa masa de solvente en kg. Para soluciones muy diluidas son casi iguales; para concentradas difieren.

---

## Mapa conceptual

```
              SOLUCIÓN
          (mezcla homogénea)
                 │
    ┌────────────┼────────────┐
    │            │            │
  SOLUTO      SOLVENTE    SOLUCIÓN
   m(st)       m(sv)    m(sc)=m(st)+m(sv)
                │               │
                │          V(sc)=m(sc)/ρ
                │
         CONCENTRACIÓN
          (prop. intensiva)
                │
    ┌───────────┼──────────────┐
    │           │              │
FÍSICAS    QUÍMICAS       SATURACIÓN
%m/m       Molar (M)      S = [sc] saturada
%m/v       Molal (m)      C < S → no sat.
%v/v       X (fracc.)     C = S → saturada
                           C > S → sobresat.
                │
           OPERACIONES
         ┌──────┴──────┐
       DILUCIÓN    CONCENTRAR
    Vc·Cc = Vd·Cd   (agregar st
                      o evaporar sv)
```

---

*Fuentes: Diapositivas de cátedra "Soluciones Parte 1" y "Soluciones Parte 2" (Prof. Betty) · Esquema para Cálculos de Concentración de Soluciones (cátedra Química General UTN FRBA) · Guía de Ejercicios y Problemas — Química General (Cataldi/Zambrino, 2020).*
