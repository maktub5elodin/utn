# Clase 7 — Torsión pura: análisis geométrico y relación tensión-ángulo

**Fecha:** 21 de mayo de 2026  
**Profesor:** Abud  
**Continuación de:** Clase 6 (14/05) — tensión, fórmula de flexión, corte puro

---

## 1. Contexto: dónde estamos

Abud repasó el recorrido hecho hasta ahora: estuvimos viendo **casos de solicitaciones** (esfuerzos característicos) como el sometimiento de acciones exteriores. El caso de hoy es la **torsión**.

> **Torsión pura** significa que la única solicitación presente es el momento torsor T. No hay otras — ni flexión, ni axial, ni cortante.

El objetivo de la clase es construir, paso a paso, la relación matemática entre el ángulo de giro de la barra y la tensión que aparece internamente.

---

## 2. Marco de estudio: hipótesis

El análisis se hace sobre una **barra de alma llena** (sección maciza) de material **homogéneo** en estado de **equilibrio dinámico** — lo que en la práctica representa, por ejemplo, un eje de transmisión girando a velocidad constante: hay rotación, pero no aceleración angular (la suma de momentos netos es cero).

Hipótesis fundamental:

> **Las secciones planas antes de la deformación permanecen planas luego de la deformación. No se alabean.**

Esto merece atención. "Alabear" significa que la sección plana se curva o tuerce fuera de su propio plano. Para barras de **sección circular** (macizas o huecas) esta hipótesis es rigurosamente verdadera — se puede demostrar matemáticamente. Para secciones no circulares (I, U, L), NO es válida: esas secciones sí alabean al torsionarse, lo que complica el análisis. Por eso se parte siempre del caso circular.

Sección de análisis: **cilindro macizo** (sección circular sólida).

---

## 3. El segmento diferencial dz

En lugar de analizar toda la barra de una vez, Abud aisla un **segmento infinitesimal** de longitud `dz`:

```
    eje z →
    ───────────────────────────────────────────
              ╔════╗              ╔════╗
              ║    ║      dz      ║    ║
              ║    ╟──────────────╢    ║
              ║    ║              ║    ║
              ╚════╝              ╚════╝
              sección             sección
              en z                en z+dz

         m →  (momento exterior aplicado en los extremos)
```

- `m` = momentos exteriores (el torque aplicado)
- `dz` = longitud del segmento (incremento diferencial de z)
- Los momentos están aplicados en los extremos del segmento

La **acción exterior** (momento aplicado) genera una **acción interior** (momento torsor T) que equilibra la sección. Esto es lo que ya vimos: el esfuerzo interno reacciona ante la carga externa para mantener el equilibrio.

---

## 4. Geometría de la deformación: la generatriz

Para ver cómo se deforma el material, Abud trabaja sobre la **superficie lateral** del cilindro.

### ¿Qué es una generatriz?

> Una **generatriz** es una línea sobre la superficie lateral del cilindro que va desde un punto A (en la sección de z) hasta un punto B (en la sección de z+dz), paralela al eje.

Si imaginás el cilindro como una lata: cualquier línea vertical dibujada sobre la superficie de la lata, de arriba hacia abajo, es una generatriz. Tiene longitud `dz`.

```
  ANTES de torcer (vista de la superficie desarrollada):

  A ─────────────── B       ← generatriz AB (línea recta paralela al eje)
  │                 │
  │      dz         │
  │                 │
```

### Qué pasa cuando se aplica el torque

La acción exterior hace girar la sección en `z+dz` un ángulo `dφ` (d-phi) respecto a la sección en `z`. El punto B se mueve a la posición **B'**.

```
  DESPUÉS de torcer:

  A ────────────────── B'   ← la generatriz AB se convirtió en AB'
  │                  /
  │                 /
  │                /
  │              B           ← B se movió a B' (arco de giro)
```

El arco BB' tiene longitud `ρ · dφ`, donde `ρ` (rho) es el **radio** de la superficie (la distancia desde el eje al punto B en la sección circular).

---

## 5. El ángulo γ (gamma): distorsión de la superficie

El ángulo que forma la generatriz deformada (AB') con la generatriz original (AB) se llama **γ (gamma)**, y es el **ángulo de distorsión de la superficie**.

```
  A ─────────────────────── B'
   \                       /
    \         γ           /
     \                   /
      ──────────────── B
             dz
```

γ mide cuánto se "inclina" la generatriz al torcer. Es exactamente la **deformación de corte** (shear strain) en la superficie del cilindro.

---

## 6. El ángulo de torsión unitario θ (theta)

El ángulo total de giro entre las dos secciones (separadas por dz) se llama `dφ`. Si dividimos ese ángulo por la longitud del segmento, obtenemos el **ángulo de torsión por unidad de longitud**, que Abud llama θ (theta):

```
       dφ
  θ = ────    [rad/mm]
       dz
```

θ representa **cuántos radianes gira la sección por cada milímetro de barra**. Es constante a lo largo de toda la barra cuando el torque es uniforme.

---

## 7. Relación γ = ρ · θ (la ecuación geométrica central)

Ahora conectamos todo. El arco BB' se puede expresar de dos maneras:

```
  Desde la geometría circular:    BB' = ρ · dφ
  Desde la distorsión angular:    BB' = γ · dz    (arco ≈ cuerda para ángulos pequeños)
```

### Cuándo vale BB' ≈ γ · dz

Aquí aparece la **aproximación de ángulo pequeño**, que el usuario de estas notas preguntó en clase. La relación exacta sería BB' = dz · tan γ. Pero para ángulos muy pequeños (γ → 0), **tan γ ≈ γ** (en radianes). Como estamos trabajando con incrementos infinitesimales (dz → 0), el ángulo dφ también tiende a cero, y la aproximación es exacta en el límite.

> **Cuándo aplica:** la aproximación sin θ ≈ θ (o tan θ ≈ θ) es válida para cualquier ángulo muy pequeño expresado en radianes. Matemáticamente, es exacta en el límite dz → 0, que es precisamente el cálculo diferencial. Cuanto más pequeño el ángulo, más precisa la aproximación.

Igualando las dos expresiones para BB':

```
  ρ · dφ = γ · dz

  →  γ = ρ · dφ/dz

  →  γ = ρ · θ
```

**γ = ρ · θ**

Conclusión directa: la deformación de corte γ en la superficie **es proporcional al radio ρ**. En el eje (ρ = 0), γ = 0 — el eje no se deforma. En la superficie exterior (ρ máximo), γ es máxima.

```
  Distribución de γ a lo largo del radio:

  eje  ─── ρ₁ ─── ρ₂ ─── ρ_max (superficie)
   │         │         │         │
   γ=0      γ₁        γ₂       γ_max
  
  (distribución lineal, proporcional al radio)
```

---

## 8. Ley de Hooke — desarrollo pedagógico

Esta ley aparece constantemente en mecánica. Vale la pena entenderla a fondo.

### La idea original

Robert Hooke observó en 1678 que al estirar un resorte, el alargamiento es proporcional a la fuerza aplicada. Lo expresó en latín: *"ut tensio, sic vis"* — como la extensión, así la fuerza.

### La versión para materiales (normal)

En mecánica de materiales, la Ley de Hooke para deformación axial (normal) dice:

```
  σ = E · ε
```

- `σ` = tensión normal [Pa]
- `ε` = deformación unitaria [adimensional] = ΔL/L₀ (cuánto se alargó respecto a la longitud original)
- `E` = módulo de elasticidad (o de Young) [Pa] — constante del material

**Qué dice:** la tensión es proporcional a la deformación. Si duplico la fuerza (y por ende σ), se duplica el alargamiento (y por ende ε). Esta proporcionalidad solo vale en la **zona elástica** — la parte recta del diagrama tensión-deformación que vimos en Clase 2.

### La versión para cortante (tangencial)

Para deformaciones de corte (shear), existe una versión análoga:

```
  τ = G · γ
```

- `τ` = tensión tangencial [Pa]
- `γ` = distorsión angular (shear strain) [adimensional, radianes] — el ángulo de inclinación que vimos en la sección anterior
- `G` = módulo de rigidez (o módulo de elasticidad transversal) [Pa] — constante del material para cortante

**Qué dice:** la tensión de corte es proporcional al ángulo de distorsión. Esta es la Ley de Hooke en su forma de cortante.

### ¿Por qué G se llama "transversal"?

- E (módulo de Young) describe la resistencia a deformación **en la dirección de la carga** (longitudinal).
- G (módulo de rigidez) describe la resistencia a deformación **perpendicular a la carga** — la resistencia al cizallamiento, que es una deformación transversal al eje de la barra.

Por eso G se llama módulo de elasticidad **transversal** — aunque ambos tienen las mismas unidades [Pa].

### ¿Por qué G es "empírico"?

Abud lo marcó explícitamente. G se determina experimentalmente para cada material — no se puede deducir solo desde primeros principios sin medir. Sin embargo, para materiales isótropos existe una relación teórica que lo conecta con E y el coeficiente de Poisson ν:

```
       E
  G = ─────────
      2·(1 + ν)
```

Esto muestra que G y E no son propiedades independientes para un material isótropo — conocer dos de los tres (E, G, ν) determina el tercero.

Para acero estructural: E ≈ 200.000 MPa, ν ≈ 0,30, por lo tanto G ≈ 77.000 MPa.

---

## 9. Tensión tangencial en torsión pura: τ = G · ρ · θ

Combinando Ley de Hooke en cortante con la relación geométrica γ = ρ · θ:

```
  τ = G · γ      (Hooke en cortante)
  γ = ρ · θ      (relación geométrica)

  →  τ = G · ρ · θ
```

**En torsión pura, solo hay tensiones tangenciales — nunca normales.** No hay σ. El material se "distorsiona" angularmente, no se estira ni comprime.

Distribución de τ a lo largo del radio:

```
  eje  ─── ρ₁ ─── ρ₂ ─── ρ_max
   │         │         │         │
  τ=0       τ₁        τ₂       τ_max

  (distribución lineal, igual que γ)
```

La tensión máxima ocurre en la **superficie exterior** (ρ = ρ_max). El eje central no tiene tensión tangencial.

Unidades de τ: mismas que G → **N/mm² (MPa)**, o si se trabaja en cm: **N/cm²**.

---

## 10. Lo que venía después (nota)

Abud comenzó a hablar de la multiplicación entre área y algo — esto es el **momento polar de inercia** J (o I_p), la propiedad geométrica de la sección para torsión, análoga al momento de inercia I para flexión. Con J se puede calcular el torque total que resiste la sección:

```
  M_t = G · J · θ     (torque total en función del ángulo de torsión unitario)

  τ = M_t · ρ / J     (tensión en cualquier punto a distancia ρ del eje)
```

Para un cilindro macizo de radio R: `J = π·R⁴ / 2`

Esta parte quedó incompleta en las notas de clase — probablemente se desarrolló al inicio de la siguiente clase.

---

## Resumen de la clase

| Concepto | Definición |
|---|---|
| Torsión pura | Solo actúa T (momento torsor) — sin N, Q ni M |
| Hipótesis de Bernoulli | Secciones planas permanecen planas — no alabean |
| Equilibrio dinámico | Rotación a velocidad constante (eje de transmisión) → sin aceleración angular |
| Generatriz | Línea sobre la superficie del cilindro paralela al eje, de longitud dz |
| γ (gamma) | Ángulo de distorsión de la superficie (shear strain) |
| dφ (d-phi) | Ángulo de giro entre dos secciones separadas por dz |
| θ (theta) = dφ/dz | Ángulo de torsión unitario [rad/mm] |
| Aprox. ángulo pequeño | Para dz → 0: tan γ ≈ γ, lo que permite igualar arco y cuerda |
| γ = ρ · θ | La distorsión es proporcional al radio — cero en el eje, máxima en la superficie |
| Ley de Hooke normal | σ = E · ε (tensión normal proporcional a deformación axial) |
| Ley de Hooke cortante | τ = G · γ (tensión tangencial proporcional a distorsión angular) |
| G (módulo de rigidez) | Módulo de elasticidad transversal — empírico, mismas unidades que E |
| τ = G · ρ · θ | Fórmula de tensión en torsión pura |
| Distribución de τ | Lineal con ρ — máxima en la superficie, cero en el eje |

---
*Fuente: apuntes de clase — Prof. Abud, 21/05/2026*
