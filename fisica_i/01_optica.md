# Óptica — La Física de la Luz

---

## Antes de empezar: ¿qué es la luz?

Antes de hablar de reflexión, refracción y lentes, hay que entender con qué estamos trabajando.

La **luz** es una forma de energía que se propaga en el espacio. Más precisamente, es una **onda electromagnética**: una perturbación que combina campos eléctricos y magnéticos que se regeneran mutuamente mientras viajan.

Lo más importante de esto para la óptica clásica es lo siguiente:

- La luz **viaja en línea recta** dentro de un medio uniforme (aire, agua, vidrio...).
- La luz tiene una **velocidad finita**. En el vacío, esa velocidad es `c ≈ 3 × 10⁸ m/s` (300 millones de metros por segundo). Es la velocidad más alta posible en el universo.
- La luz **no necesita un medio material** para propagarse (a diferencia del sonido, que no viaja en el vacío).
- La luz visible es solo una pequeña franja de un espectro mucho más amplio que incluye rayos X, microondas, ondas de radio, etc. Todos son lo mismo, solo difieren en su frecuencia.

### El modelo de rayos

Para la mayoría de los problemas de óptica de ingeniería, no necesitamos pensar en la luz como onda. Usamos el **modelo de rayos**: representamos la luz como líneas rectas (rayos) que indican la dirección en que viaja.

Este modelo simplificado es suficiente para entender espejos, lentes y la formación de imágenes. Es la misma idea que cuando dibujás una flecha en contabilidad para indicar flujo de fondos: el gráfico simplifica la realidad pero captura lo que necesitás.

---

## Parte 1: Reflexión

### ¿Qué es la reflexión?

Cuando un rayo de luz llega a una superficie, parte de esa luz **rebota** de vuelta. Eso es la reflexión. Ocurre en todo tipo de superficies: metales pulidos, agua, vidrio, papel (aunque el papel la dispersa en muchas direcciones).

### La Ley de la Reflexión

La ley es elegantemente simple. Para entenderla, necesitamos definir un concepto primero:

**Normal:** la línea perpendicular a la superficie en el punto donde llega el rayo. Es imaginaria, pero es la referencia para medir todos los ángulos en óptica.

```
         Normal
           |
    Rayo   |   Rayo
  incidente|  reflejado
     \     |     /
      \    |    /
       \θi |θr /
        \  |  /
─────────────────────  ← Superficie (espejo)
```

- **θᵢ** = ángulo de incidencia (entre el rayo entrante y la normal)
- **θᵣ** = ángulo de reflexión (entre el rayo reflejado y la normal)

**Ley de la reflexión:**

```
θᵢ = θᵣ
```

El ángulo de incidencia es igual al ángulo de reflexión. Siempre. Sin excepciones.

> **Ojo:** los ángulos se miden respecto a la **normal**, no respecto a la superficie. Es un error muy común al principio.

---

### Espejos planos

El espejo más simple es el espejo plano: una superficie lisa y reflectante.

Cuando te mirás en un espejo, tu imagen tiene estas características:

| Característica | Imagen en espejo plano |
|---|---|
| Derecha / Invertida | Derecha (no está boca abajo) |
| Tamaño | Igual al objeto |
| Distancia | Tan detrás del espejo como el objeto está adelante |
| Real / Virtual | **Virtual** (la luz no pasa realmente por ese punto) |

**¿Qué significa imagen virtual?** La luz que ves rebotó en el espejo; detrás del espejo no hay nada. Tu cerebro traza hacia atrás las líneas de los rayos reflejados y "ve" la imagen ahí, pero la luz nunca estuvo ahí. Por eso se llama virtual: existe solo como percepción, no como concentración real de luz.

---

### Espejos curvos

Los espejos curvos más comunes son los **esféricos**: su superficie es un fragmento de una esfera.

- **Espejo cóncavo:** curva hacia adentro (como un cuenco). El interior reflectante.
- **Espejo convexo:** curva hacia afuera (como la parte exterior de una esfera). Los espejos retrovisores del auto son convexos.

#### Conceptos clave de los espejos esféricos

```
         C    F
         |    |
─────────o────o──────►  Eje principal
         |    |
       Centro Foco
      curvatura
```

- **Centro de curvatura (C):** el centro de la esfera de la cual el espejo es un fragmento. Distancia al espejo = `R` (radio de curvatura).
- **Foco (F):** el punto donde convergen (o de donde parecen divergir) los rayos paralelos al eje principal tras rebotar en el espejo. Distancia al espejo = `f` (distancia focal).
- **Eje principal:** la línea que pasa por el centro del espejo y el foco.

**Relación fundamental:**

```
f = R / 2
```

La distancia focal es la mitad del radio de curvatura. Si sabés uno, sabés el otro.

---

#### La ecuación de espejos (y lentes)

Para saber dónde se forma la imagen de un objeto, usamos la **ecuación de la imagen**:

```
1/f = 1/dₒ + 1/dᵢ
```

Donde:
- `f` = distancia focal del espejo
- `dₒ` = distancia del **objeto** al espejo (*do* de "objeto")
- `dᵢ` = distancia de la **imagen** al espejo (*di* de "imagen")

Y para saber qué tamaño tiene la imagen respecto al objeto, usamos el **aumento lateral (m)**:

```
m = -dᵢ / dₒ
```

- Si `|m| > 1`: la imagen es más grande que el objeto.
- Si `|m| < 1`: la imagen es más chica.
- Si `m > 0`: imagen derecha (mismo sentido que el objeto).
- Si `m < 0`: imagen invertida.

---

#### Convención de signos (fundamental para no perderse)

Los signos en óptica no son arbitrarios. Siguen una convención que hay que respetar:

| Magnitud | Positivo (+) | Negativo (−) |
|---|---|---|
| `dₒ` (distancia objeto) | Objeto del mismo lado que la luz incidente | Objeto detrás del espejo (raro) |
| `dᵢ` (distancia imagen) | Imagen del mismo lado que la luz reflejada (imagen **real**) | Imagen detrás del espejo (imagen **virtual**) |
| `f` (distancia focal) | Espejo cóncavo | Espejo convexo |
| `m` (aumento) | Imagen derecha | Imagen invertida |

> **Regla práctica para espejos:** si la imagen se forma del mismo lado que el objeto (adelante del espejo), la imagen es real y `dᵢ` es positiva. Si se forma detrás del espejo, es virtual y `dᵢ` es negativa.

---

#### Ejemplo resuelto: espejo cóncavo

**Enunciado:** Un objeto está a 30 cm de un espejo cóncavo de distancia focal 10 cm. ¿Dónde se forma la imagen? ¿Cómo es?

**Datos:**
- `dₒ = 30 cm`
- `f = +10 cm` (cóncavo → positivo)

**Paso 1: aplicar la ecuación**

```
1/f = 1/dₒ + 1/dᵢ
1/10 = 1/30 + 1/dᵢ
1/dᵢ = 1/10 - 1/30
1/dᵢ = 3/30 - 1/30
1/dᵢ = 2/30
dᵢ = 15 cm
```

**Paso 2: calcular el aumento**

```
m = -dᵢ / dₒ = -15/30 = -0,5
```

**Interpretación:**
- `dᵢ = +15 cm` → imagen real, del mismo lado que el objeto (adelante del espejo).
- `|m| = 0,5` → imagen más chica (mitad del tamaño).
- `m < 0` → imagen invertida.

---

## Parte 2: Refracción

### ¿Qué es la refracción?

Cuando la luz pasa de un medio a otro (por ejemplo, del aire al agua), **cambia su velocidad**. Y cuando una onda cambia de velocidad al cruzar una frontera en ángulo, **cambia de dirección**. Eso es la refracción.

Es el fenómeno responsable de:
- La cuchara que parece quebrada en un vaso de agua.
- Los anteojos y lentes de contacto.
- Los espejismos en el desierto.
- Los arcoíris.

### Índice de refracción

Cada medio transparente tiene un **índice de refracción (n)** que indica cuánto más lento viaja la luz en ese medio comparado con el vacío:

```
n = c / v
```

Donde:
- `c = 3 × 10⁸ m/s` (velocidad de la luz en el vacío)
- `v` = velocidad de la luz en ese medio
- `n` = índice de refracción (siempre ≥ 1, sin unidades)

**Índices de refracción comunes:**

| Medio | n |
|---|---|
| Vacío | 1,000 |
| Aire | 1,003 ≈ 1 |
| Agua | 1,33 |
| Vidrio (común) | 1,5 |
| Diamante | 2,42 |

> Cuanto mayor el índice, más lento viaja la luz y más "dobla" al entrar a ese medio.

---

### Ley de Snell

La Ley de Snell describe exactamente cómo cambia la dirección de la luz al cambiar de medio:

```
n₁ · sin(θ₁) = n₂ · sin(θ₂)
```

Donde:
- `n₁` = índice del primer medio
- `θ₁` = ángulo de incidencia (respecto a la normal)
- `n₂` = índice del segundo medio
- `θ₂` = ángulo de refracción (respecto a la normal)

```
            Normal
              |
Medio 1 (n₁)  |
   Rayo ──►\  |
             \|  θ₁
──────────────●───────────────  ← Interfaz
              |\  θ₂
              | \──►  Rayo refractado
Medio 2 (n₂)  |
              |
```

**¿Hacia dónde dobla la luz?**

- Si la luz pasa a un medio **más denso ópticamente** (mayor n), se acerca a la normal (θ₂ < θ₁).
- Si la luz pasa a un medio **menos denso** (menor n), se aleja de la normal (θ₂ > θ₁).

> **Regla mnemotécnica:** al entrar a un medio más "lento" (mayor n), la luz "frena" y se dobla hacia la normal, como un auto que entra en barro: la rueda que toca el barro primero frena, el auto gira hacia ese lado.

---

#### Ejemplo resuelto: Ley de Snell

**Enunciado:** Un rayo de luz pasa del aire (n₁ = 1) al vidrio (n₂ = 1,5) con un ángulo de incidencia de 30°. ¿Cuál es el ángulo de refracción?

**Datos:**
- `n₁ = 1`
- `θ₁ = 30°`
- `n₂ = 1,5`

**Aplicando la Ley de Snell:**

```
n₁ · sin(θ₁) = n₂ · sin(θ₂)
1 · sin(30°) = 1,5 · sin(θ₂)
0,5 = 1,5 · sin(θ₂)
sin(θ₂) = 0,5 / 1,5 = 0,333
θ₂ = arcsin(0,333) ≈ 19,5°
```

La luz se acercó a la normal (de 30° pasó a 19,5°), como era de esperarse al entrar a un medio más denso.

---

### Reflexión total interna

Hay un caso especial fascinante: si la luz viaja en un medio denso (vidrio, agua) y choca con la interfaz hacia un medio menos denso (aire), puede ocurrir que el ángulo de refracción llegue a 90° o más. En ese caso, la luz no sale: **toda rebota hacia adentro**. Esto se llama **reflexión total interna**.

El ángulo a partir del cual ocurre esto se llama **ángulo crítico (θc)**:

```
sin(θc) = n₂ / n₁         (con n₁ > n₂)
```

Si el ángulo de incidencia es mayor que θc, hay reflexión total interna.

**¿Dónde se usa esto?**
- Fibra óptica: la luz viaja dentro de un cable de vidrio sin escaparse gracias a la reflexión total interna. Es la base de las telecomunicaciones modernas e internet.
- Periscopios y algunos prismáticos.

---

## Parte 3: Lentes

### ¿Qué es una lente?

Una lente es un objeto transparente (generalmente vidrio o plástico) con superficies curvas diseñadas para **doblar la luz de manera controlada** y así formar imágenes.

Hay dos tipos fundamentales:

**Lente convergente (convexa):** más gruesa en el centro que en los bordes. Hace converger los rayos paralelos en un punto (el foco). Es la lupa, el objetivo de la cámara, el cristalino del ojo.

```
  ───────►    \  /    ────►
  ───────►     \/     ────►●   ← Foco
  ───────►    /  \    ────►
               Lente convergente
```

**Lente divergente (cóncava):** más delgada en el centro que en los bordes. Hace divergir los rayos; el foco está del mismo lado que la luz incidente (foco virtual).

```
  ───────►    | |    ────►
  ───────►    | |  ↗ ────►     ← Los rayos se separan
  ───────►    | |  ↘ ────►
               Lente divergente
```

---

### La ecuación de lentes (o del fabricante de lentes)

Para lentes delgadas (espesor despreciable), se usa **la misma ecuación que para espejos**:

```
1/f = 1/dₒ + 1/dᵢ
```

Y el aumento lateral también es el mismo:

```
m = -dᵢ / dₒ
```

La convención de signos para lentes es levemente diferente:

| Magnitud | Positivo (+) | Negativo (−) |
|---|---|---|
| `f` | Lente **convergente** | Lente **divergente** |
| `dₒ` | Objeto del lado de la luz incidente | Objeto del otro lado (caso raro) |
| `dᵢ` | Imagen del lado opuesto a la luz incidente (**real**) | Imagen del mismo lado que la luz incidente (**virtual**) |

> La diferencia clave con los espejos: en lentes, la imagen real se forma del **otro** lado de la lente (la luz la atraviesa). En espejos, la imagen real se forma del mismo lado que el objeto.

---

### Los tres rayos principales (para dibujos de lentes)

Para encontrar gráficamente dónde se forma la imagen, se trazan tres rayos desde la punta del objeto:

1. **Rayo paralelo al eje:** después de la lente, pasa por el foco (o su prolongación para divergentes).
2. **Rayo por el centro de la lente:** sigue derecho, sin desviarse.
3. **Rayo por el foco:** después de la lente, sale paralelo al eje.

La imagen se forma donde se cortan (al menos) dos de estos rayos.

```
            F'         F
            |          |
     |      |          |      |
Obj──●──────o──────────o──────●── Eje
     |      |          |      |
     |←dₒ→ |          |←dᵢ→ |
            ↑
          Lente convergente
```

---

#### Ejemplo resuelto: lente convergente

**Enunciado:** Un objeto está a 20 cm de una lente convergente de distancia focal 15 cm. ¿Dónde se forma la imagen? ¿Cómo es?

**Datos:**
- `dₒ = 20 cm`
- `f = +15 cm` (convergente → positivo)

**Paso 1: ecuación de la imagen**

```
1/f = 1/dₒ + 1/dᵢ
1/15 = 1/20 + 1/dᵢ
1/dᵢ = 1/15 - 1/20
1/dᵢ = 4/60 - 3/60
1/dᵢ = 1/60
dᵢ = 60 cm
```

**Paso 2: aumento**

```
m = -dᵢ / dₒ = -60/20 = -3
```

**Interpretación:**
- `dᵢ = +60 cm` → imagen real, del otro lado de la lente.
- `|m| = 3` → imagen 3 veces más grande que el objeto.
- `m < 0` → imagen invertida.

---

### Casos según la posición del objeto (lente convergente)

La posición del objeto respecto al foco determina completamente las características de la imagen:

| Posición del objeto | Imagen | Tamaño | Orientación | Tipo |
|---|---|---|---|---|
| Muy lejos (∞) | En el foco (dᵢ = f) | Puntual | — | Real |
| Más allá de 2F | Entre F y 2F | Reducida | Invertida | Real |
| En 2F | En 2F | Igual | Invertida | Real |
| Entre F y 2F | Más allá de 2F | Ampliada | Invertida | Real |
| En F | En el infinito | — | — | — |
| Entre F y la lente | Del mismo lado | Ampliada | Derecha | **Virtual** |

El último caso (objeto entre F y la lente) es la **lupa**: el ojo ve una imagen virtual ampliada del mismo lado que el objeto.

---

## Parte 4: El ojo humano como sistema óptico

El ojo es en sí un sistema óptico sofisticado:

- La **córnea** y el **cristalino** actúan como una lente convergente.
- La **retina** es la pantalla donde se forma la imagen (la imagen siempre es real e invertida, el cerebro la corrige).
- El cristalino puede cambiar su curvatura (y por tanto su distancia focal) para enfocar objetos a diferentes distancias. Esto se llama **acomodación**.

**Defectos visuales y su corrección:**

| Defecto | Causa | Corrección |
|---|---|---|
| Miopía | El ojo es muy largo; la imagen se forma antes de la retina | Lente **divergente** (aleja el foco) |
| Hipermetropía | El ojo es muy corto; la imagen se formaría detrás de la retina | Lente **convergente** (acerca el foco) |

> La receta del oftalmólogo en dioptrías es simplemente `D = 1/f` (con f en metros). Una receta de −2 dioptrías significa una lente divergente con f = −0,5 m = −50 cm.

---

## Resumen de fórmulas

| Fórmula | Nombre | Cuándo usarla |
|---|---|---|
| `θᵢ = θᵣ` | Ley de la reflexión | Cualquier espejo o superficie reflectante |
| `f = R/2` | Relación focal-radio | Espejos esféricos |
| `1/f = 1/dₒ + 1/dᵢ` | Ecuación de la imagen | Espejos curvos y lentes (¡la misma!) |
| `m = −dᵢ / dₒ` | Aumento lateral | Para saber tamaño y orientación de la imagen |
| `n = c / v` | Índice de refracción | Para caracterizar un medio óptico |
| `n₁ sin(θ₁) = n₂ sin(θ₂)` | Ley de Snell | Cuando la luz cambia de medio |
| `sin(θc) = n₂ / n₁` | Ángulo crítico | Condición para reflexión total interna |
| `D = 1/f` | Potencia en dioptrías | Óptica oftalmológica |

---

## Errores comunes a evitar

1. **Medir ángulos desde la superficie, no desde la normal.** La normal es siempre la referencia.
2. **Confundir imagen real y virtual.** Real = la luz realmente pasa por ahí. Virtual = el ojo traza hacia atrás los rayos, pero la luz no está realmente ahí.
3. **Olvidar los signos.** Una imagen con `dᵢ` negativo es virtual. Una lente divergente tiene `f` negativo. No omitir los signos cambia completamente el resultado.
4. **Confundir distancia focal con radio de curvatura.** `f = R/2`, son cosas distintas.
5. **Aplicar la ecuación de la imagen sin definir el sistema de referencia.** El espejo o la lente es siempre el origen.
