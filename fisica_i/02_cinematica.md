# Cinemática — Descripción del Movimiento

> *La cinemática responde a "¿cómo se mueve?" sin preguntar "¿por qué se mueve?".*
> Esa pregunta — el por qué — es la dinámica (Newton). Primero hay que saber describir.

---

## 1. Sistema de Unidades MKS y Análisis Dimensional

### El sistema MKS

En física de ingeniería usamos el **Sistema Internacional (SI)**, cuya base es:

```
  M — Metro     (m)    longitud
  K — Kilogramo (kg)   masa
  S — Segundo   (s)    tiempo
```

Todo lo demás se construye desde estas tres unidades base.

| Magnitud | Unidad | Símbolo | En términos de base |
|----------|--------|---------|---------------------|
| Longitud | metro | m | base |
| Masa | kilogramo | kg | base |
| Tiempo | segundo | s | base |
| Velocidad | metro por segundo | m/s | m · s⁻¹ |
| Aceleración | metro por segundo cuadrado | m/s² | m · s⁻² |
| Fuerza | Newton | N | kg · m · s⁻² |
| Energía | Joule | J | kg · m² · s⁻² |

### El método de conversión: siempre multiplicar por 1

El profesor enseñó un método infalible: **toda conversión es multiplicar por 1**, escrito de forma conveniente.

El principio: si `1 km = 1000 m`, entonces la fracción `1000 m / 1 km` es igual a 1 (mismo valor arriba y abajo, distintas unidades). Multiplicar por 1 no cambia el valor físico, pero sí cancela unidades.

**Ejemplo canónico: convertir 72 km/h a m/s**

```
           1000 m     1 h
72 km/h × ——————— × ————————
            1 km     3600 s

Paso 1: cancelar km
  km/h × (m/km)  →  m/h      ← los "km" se cancelan (uno arriba, uno abajo)

Paso 2: cancelar horas
  m/h × (h/s)   →  m/s       ← las "h" se cancelan

Resultado:
  72 × 1000 / 3600  =  72000 / 3600  =  20 m/s
```

```
  Regla práctica:
  km/h → m/s:   dividir por 3,6   (72 / 3,6 = 20)
  m/s → km/h:   multiplicar por 3,6
```

**¿Por qué m/s²?**
La aceleración es variación de velocidad por unidad de tiempo:

```
  a = Δv / Δt  →  (m/s) / s  =  m/s²  =  m · s⁻²
```

No es "metros por segundo, al cuadrado" en el sentido de área. Es "metros por segundo, por segundo" — cuántos m/s gana o pierde cada segundo.

### Análisis dimensional: la auditoria de la física

El análisis dimensional es la herramienta para **verificar que una ecuación es físicamente consistente**. Si los lados izquierdo y derecho no tienen las mismas unidades, la ecuación está mal.

Notación: `[X]` significa "las unidades de X".

```
  [posición]    = m
  [velocidad]   = m/s  = m · s⁻¹
  [aceleración] = m/s² = m · s⁻²
  [tiempo]      = s
```

**Verificación de la ecuación de posición en MRUA:**

```
  x(t) = x₀ + v₀·t + ½·a·t²

  Verificando cada término:
  [x₀]     = m                      ✓ metro
  [v₀·t]   = (m/s) · s  = m         ✓ metro
  [½·a·t²] = (m/s²) · s² = m        ✓ metro

  Los tres términos tienen unidades de metro → la ecuación es dimensionalmente válida.
```

Si al verificar obtenés unidades distintas en algún término, encontraste un error antes de calcular nada.

> **Analogía contable:** El análisis dimensional es exactamente la verificación de que un balance cuadra — activos en pesos no pueden sumarse con pasivos en dólares sin conversión. En física, metros no suman con segundos.

---

## 2. Magnitudes Vectoriales y Escalares

Antes de definir posición, velocidad y aceleración, hay que distinguir dos tipos de magnitudes:

| Tipo | Definición | Ejemplos |
|------|-----------|---------|
| **Escalar** | Solo tiene magnitud (número + unidad) | temperatura, masa, tiempo, distancia recorrida |
| **Vectorial** | Tiene magnitud, dirección y sentido | posición, desplazamiento, velocidad, aceleración, fuerza |

```
  Escalar:   "temperatura = 25°C"      (un número)
  Vectorial: "velocidad = 20 m/s al norte"   (número + dirección + sentido)
```

En la notación escrita:
- Vectores con flecha arriba: `→v` o `v⃗`
- Módulo (magnitud) del vector: `|v|` o simplemente `v` en itálica
- En el pizarrón suelen subrayarse: `v`

---

## 3. La Cadena Posición → Velocidad → Aceleración

Esta es **la idea central de la cinemática**. Las tres magnitudes principales están relacionadas por derivación:

```
  Posición       →  derivar  →  Velocidad      →  derivar  →  Aceleración
   x(t)  [m]                    v(t)  [m/s]                    a(t)  [m/s²]
```

Y en sentido inverso, integración:

```
  Aceleración    →  integrar →  Velocidad      →  integrar →  Posición
   a(t)  [m/s²]                 v(t)  [m/s]                    x(t)  [m]
```

> **Analogía contable perfecta:**
> - **Aceleración** = tasa de cambio de la velocidad (como la tasa de crecimiento del sueldo)
> - **Velocidad** = tasa de cambio de la posición (como el sueldo mensual)
> - **Posición** = acumulado (como el patrimonio acumulado)
>
> La aceleración es la "segunda derivada" del patrimonio. Si tu sueldo crece $500/mes cada mes, tu patrimonio acumula acelerado.

### Las tres definiciones formales

#### Posición — x(t)

La posición es la **función vectorial** que dice dónde está el objeto en cada instante `t`:

```
  x⃗(t)  o  r⃗(t)   [metros]

  En 1D (recta):     x(t)    — un escalar positivo o negativo
  En 2D (plano):     r⃗(t) = (x(t), y(t))
  En 3D (espacio):   r⃗(t) = (x(t), y(t), z(t))
```

La posición siempre se mide **desde un origen de referencia**. El origen es una elección — lo definimos donde nos convenga.

```
  Ejemplo en 1D:
  
  Origen   A        B
    |——————|————————|————→  eje x
    0      3m       8m

  Posición en A: x_A = +3 m
  Posición en B: x_B = +8 m
  Posición detrás del origen: x = -2 m (a la izquierda)
```

#### Desplazamiento vs. Distancia recorrida

Dos conceptos que el profesor distinguió:

```
  Desplazamiento (vectorial): Δx⃗ = x⃗_final - x⃗_inicial

  Distancia recorrida (escalar): longitud total del camino seguido
```

```
  Ejemplo:
  Vas de A (0 m) → B (10 m) → C (4 m)

  Distancia recorrida: 10 + 6 = 16 m   ← sumás todos los trayectos

  Desplazamiento: 4 - 0 = +4 m          ← solo importa inicio y fin
```

Si volvés exactamente al punto de partida: desplazamiento = 0, pero distancia recorrida > 0.

#### Velocidad media

```
            Δx⃗        x⃗_final - x⃗_inicial
  v⃗_m  =  ————  =  ————————————————————    [m/s]
            Δt          t_final - t_inicial
```

La velocidad media es el **cociente de variaciones finitas**. Δx y Δt son diferencias entre valores separados por un intervalo de tiempo real.

```
  Ejemplo:
  Posición a t=0s:  x₀ = 2 m
  Posición a t=4s:  x₁ = 18 m

       Δx   18 - 2   16
  v_m = —— = ——————— = —— = 4 m/s
       Δt    4 - 0    4
```

> **Analogía:** Velocidad media = promedio de velocidad en el período, como la "velocidad promedio de ventas por mes en el trimestre". No dice nada de los picos o valles internos.

#### Velocidad instantánea

La velocidad instantánea es el **límite cuando el intervalo de tiempo tiende a cero**:

```
           Δx⃗         dx⃗
  v⃗(t) = lim ———  =  ———   [m/s]
         Δt→0 Δt        dt
```

Esto es exactamente la **derivada de la posición respecto al tiempo**.

```
  Δt grande → velocidad media (promedio del intervalo)
  Δt → 0    → velocidad instantánea (en ese instante exacto)

  Representación gráfica en x(t):
  
  x │       *
    │      /
    │     /← secante (velocidad media entre dos puntos)
    │    /
    │   * ← tangente en ese punto (velocidad instantánea)
    │
    └──────── t
  
  La velocidad instantánea es la PENDIENTE de la tangente a x(t).
```

> **Analogía:** Velocidad media = tasa de crecimiento del trimestre. Velocidad instantánea = tasa en este momento exacto (la derivada del gráfico de patrimonio).

#### Aceleración

La aceleración es la variación de velocidad por unidad de tiempo:

```
           Δv⃗         dv⃗    d²x⃗
  a⃗(t) = lim ———  =  ———  = ————   [m/s²]
         Δt→0 Δt        dt    dt²
```

Es la **derivada de la velocidad**, y también la **segunda derivada de la posición**.

```
  Si v aumenta con el tiempo → a > 0  (aceleración en sentido del movimiento)
  Si v disminuye con el tiempo → a < 0  (desaceleración o frenado)
  Si v no cambia → a = 0  (movimiento uniforme)
```

**La aceleración gravitatoria:**
```
  g ≈ 9,8 m/s²  ≈  10 m/s²   (aproximación habitual en ejercicios)

  Significa: cada segundo, un objeto en caída libre gana 10 m/s de velocidad
  
  t = 0s:  v = 0 m/s
  t = 1s:  v = 10 m/s
  t = 2s:  v = 20 m/s
  t = 3s:  v = 30 m/s
```

La aceleración es siempre un **vector**. En caída libre apunta hacia abajo (hacia el centro de la Tierra). Si el objeto cae, a⃗ y v⃗ apuntan en el mismo sentido → el objeto acelera. Si el objeto sube, v⃗ apunta arriba pero a⃗ apunta abajo → el objeto desacelera.

---

## 4. La Δ y la d — Diferencias Finitas vs. Infinitesimales

El profesor marcó esta distinción claramente. Es la diferencia entre álgebra y cálculo:

```
  Δx  =  x₂ - x₁          ← diferencia FINITA (intervalo real, medible)
  dx  =  lím Δx  cuando Δt → 0   ← diferencial (infinitamente pequeño)
```

| Símbolo | Nombre | Cuándo usarlo |
|---------|--------|---------------|
| `Δx` | "delta x" | variación entre dos instantes concretos |
| `dx` | diferencial de x | en derivadas e integrales (proceso límite) |
| `dx/dt` | derivada | velocidad instantánea (razón de cambio exacta) |
| `Δx/Δt` | cociente de diferencias | velocidad media (aproximación discreta) |

```
  En la práctica:

  v_media     = Δx / Δt    (usás dos mediciones reales)
  v_instantánea = dx / dt   (derivás la función x(t))
```

---

## 5. Ecuación de Trayectoria y Ecuación Horaria

Dos formas distintas de describir un movimiento:

### Ecuación horaria (o ecuación del movimiento)

Describe **dónde está el objeto en función del tiempo**:

```
  x = f(t)    o    r⃗ = r⃗(t)

  Ejemplo:  x(t) = 3 + 4t + 2t²   [m], con t en segundos
```

La ecuación horaria contiene al tiempo `t` como variable independiente. Es la descripción completa del movimiento.

### Ecuación de trayectoria

Describe la **curva geométrica que recorre el objeto en el espacio**, eliminando el tiempo:

```
  y = f(x)    (en 2D, relación entre coordenadas)

  Ejemplo: si x(t) = t  e  y(t) = t²
  Eliminando t: y = x²   ← esa es la trayectoria (una parábola)
```

La trayectoria es la "huella en el espacio" — no dice cuándo pasa el objeto por cada punto, solo qué camino sigue.

```
  Ecuación horaria:   x(t) = ..., y(t) = ...   ← incluye el tiempo
  Ecuación de trayectoria:   y = f(x)            ← solo geometría
```

---

## 6. Sistemas Curvilíneos — Velocidad Escalar vs. Vectorial

Cuando el movimiento **no es en línea recta**, hay que distinguir con más cuidado:

```
  Trayectoria curvilínea (ejemplo: curva de una ruta):
  
       B
      /
     /← camino real (arco)
    /
   A
```

En este caso:

| Magnitud | Símbolo | Tipo | Definición |
|----------|---------|------|-----------|
| Desplazamiento | Δr⃗ | Vectorial | Vector de A a B (línea recta) |
| Distancia recorrida | Δs | Escalar | Longitud del arco de A a B |
| Velocidad vectorial media | v⃗_m | Vectorial | Δr⃗ / Δt |
| Velocidad escalar media | v_em | Escalar | Δs / Δt |

```
  Distancia ≥ Desplazamiento  siempre
  (el arco siempre es mayor o igual a la cuerda)

  En movimiento rectilíneo sin cambio de sentido:
  distancia = |desplazamiento|   (son iguales en módulo)
```

**Velocidad escalar vs. velocidad vectorial:**
- La **velocidad vectorial** lleva dirección y sentido (cambia cuando la trayectoria curva)
- La **velocidad escalar** (o celeridad, *speed* en inglés) es solo el módulo: |v⃗|

Un auto en una rotonda puede tener velocidad escalar constante (el velocímetro no varía) pero velocidad vectorial cambiante (la dirección cambia continuamente → hay aceleración).

---

## 7. Casos Particulares: MRU y MRUA

Los dos casos más simples son los que el profesor desarrolló. Ambos son **movimiento rectilíneo** (en línea recta).

### MRU — Movimiento Rectilíneo Uniforme

**Definición:** velocidad constante → aceleración cero.

```
  a = 0  →  v = constante
```

**Ecuaciones:**

```
  v(t) = v₀               ← velocidad no cambia

  x(t) = x₀ + v₀ · t     ← posición lineal en el tiempo
```

**Gráficas características:**

```
  v(t)                x(t)
  │                   │    /
  │ ————————————      │   /  ← pendiente = v₀
  │                   │  /
  └────────── t       └────────── t

  Constante           Línea recta
```

**Interpretación geométrica:**
- En `v(t)`: línea horizontal — la pendiente es cero (a=0)
- En `x(t)`: línea recta con pendiente `v₀`
- El **área bajo la curva v(t)** entre dos instantes = desplazamiento en ese intervalo

```
  Área = base × altura = Δt × v₀ = desplazamiento ✓
```

**Ejemplo:**
```
  Un auto pasa x₀ = 10 m a t=0 con v = 25 m/s. ¿Dónde está a t=3s?

  x(3) = 10 + 25 · 3 = 10 + 75 = 85 m
```

> **Analogía:** MRU es exactamente el "capital con interés simple": crece a tasa constante, la posición aumenta linealmente. `x = x₀ + v·t` es idéntico a `M = C + C·r·t`.

---

### MRUA — Movimiento Rectilíneo Uniformemente Acelerado

**Definición:** aceleración constante → velocidad varía linealmente → posición varía cuadráticamente.

```
  a = cte ≠ 0
```

**Ecuaciones (las tres fundamentales):**

```
  v(t) = v₀ + a · t                    ← velocidad lineal en t

  x(t) = x₀ + v₀·t + ½·a·t²           ← posición cuadrática en t

  v² = v₀² + 2·a·(x - x₀)             ← sin tiempo (relaciona v y x)
```

La tercera ecuación se obtiene combinando las dos primeras eliminando `t`. Útil cuando no tenés el tiempo pero sí la distancia recorrida.

**Gráficas características:**

```
  a(t)                 v(t)               x(t)
  │                    │        /          │       .·
  │ ————————————       │       /           │     .·
  │                    │      / ← pdte=a   │   .·  ← parábola
  └────────── t        └────────── t       └────────── t

  Constante           Línea recta         Parábola (cóncava arriba si a>0)
```

**Interpretación geométrica:**
- En `a(t)`: línea horizontal (a constante)
- En `v(t)`: línea recta con pendiente `a`
  - El **área bajo v(t)** = desplazamiento
- En `x(t)`: parábola
  - La **pendiente de la tangente** en cada punto = velocidad instantánea

**El área bajo a(t) = variación de velocidad:**
```
  Área = a · Δt = Δv   ✓  (porque a = Δv/Δt → Δv = a·Δt)
```

**Ejemplo completo:**
```
  Un cuerpo parte del reposo (v₀ = 0) desde x₀ = 0 con a = 3 m/s².

  v(t) = 0 + 3t = 3t
  x(t) = 0 + 0·t + ½·3·t² = 1,5t²

  A t = 4s:
    v(4) = 3 × 4 = 12 m/s
    x(4) = 1,5 × 16 = 24 m

  Verificación dimensional:
    [1,5] = m/s²  (por ser ½a)
    [t²] = s²
    [1,5·t²] = (m/s²)·s² = m   ✓
```

**Caso particular importante — caída libre:**
```
  a = g = 9,8 m/s² ≈ 10 m/s²   (hacia abajo, definimos positivo hacia abajo)

  v(t) = v₀ + g·t
  y(t) = y₀ + v₀·t + ½·g·t²

  Objeto soltado desde el reposo (v₀ = 0):
  v(t) = 10t   →   a t=1s: 10 m/s; a t=2s: 20 m/s; a t=3s: 30 m/s
  y(t) = 5t²   →   a t=1s: 5 m; a t=2s: 20 m; a t=3s: 45 m
```

> **Analogía:** MRUA es el "capital con interés compuesto sobre el flujo": la posición acumula una tasa que ella misma está creciendo. En contabilidad sería el caso de reinversión de utilidades donde la base de cálculo crece cada período.

---

## 8. Relaciones Geométricas — Resumen Visual

La física del movimiento se puede "leer" en las gráficas:

```
  ┌─────────────────────────────────────────────────────────┐
  │              LECTURA DE GRÁFICAS                        │
  │                                                         │
  │  Gráfica x(t):                                          │
  │    Pendiente en un punto  →  velocidad instantánea      │
  │    Pendiente media        →  velocidad media            │
  │    Curva hacia arriba (cóncava) → a > 0                 │
  │    Curva hacia abajo (convexa)  → a < 0                 │
  │    Línea recta            →  v = cte (MRU)              │
  │    Parábola               →  a = cte (MRUA)             │
  │                                                         │
  │  Gráfica v(t):                                          │
  │    Pendiente en un punto  →  aceleración                │
  │    Área bajo la curva     →  desplazamiento             │
  │    Horizontal             →  a = 0 (MRU)                │
  │    Recta inclinada        →  a = cte (MRUA)             │
  │    Cruza eje horizontal   →  objeto cambia de sentido   │
  │                                                         │
  │  Gráfica a(t):                                          │
  │    Área bajo la curva     →  variación de velocidad     │
  │    Horizontal             →  MRU o MRUA (según valor)   │
  └─────────────────────────────────────────────────────────┘
```

---

## 9. Tabla Resumen — MRU vs. MRUA

| Característica | MRU | MRUA |
|----------------|-----|------|
| Aceleración | `a = 0` | `a = cte ≠ 0` |
| Velocidad | constante | varía linealmente |
| Posición | varía linealmente | varía cuadráticamente |
| Ecuación x(t) | `x = x₀ + v₀·t` | `x = x₀ + v₀·t + ½·a·t²` |
| Ecuación v(t) | `v = v₀` | `v = v₀ + a·t` |
| Ecuación v(x) | no aplica | `v² = v₀² + 2a·(x-x₀)` |
| Gráfica x(t) | línea recta | parábola |
| Gráfica v(t) | horizontal | recta inclinada |
| Gráfica a(t) | sobre el eje (a=0) | horizontal (a=cte) |

---

## 10. Mapa Conceptual de la Cinemática

```
  CINEMÁTICA
  │
  ├── Sistema de referencia
  │     ├── Origen → define dónde es x = 0
  │     └── Sistema MKS: m, kg, s
  │
  ├── Conversión de unidades → multiplicar por 1
  │     └── Ejemplo: 72 km/h × (1000m/km) × (1h/3600s) = 20 m/s
  │
  ├── Análisis dimensional → verificar unidades en toda ecuación
  │
  ├── Magnitudes
  │     ├── Escalares: masa, temperatura, distancia recorrida
  │     └── Vectoriales: posición, velocidad, aceleración
  │
  ├── La cadena fundamental
  │     posición x(t) → derivar → velocidad v(t) → derivar → aceleración a(t)
  │     aceleración a(t) → integrar → velocidad v(t) → integrar → posición x(t)
  │
  ├── Velocidad media: Δx/Δt (cociente de variaciones finitas)
  │   Velocidad instantánea: dx/dt (derivada, límite cuando Δt→0)
  │
  ├── Ecuación horaria: x = f(t)   ← dónde está en cada instante
  │   Ecuación de trayectoria: y = f(x) ← qué camino sigue en el espacio
  │
  ├── Sistemas curvilíneos
  │     ├── Desplazamiento vectorial: Δr⃗ (línea recta punto a punto)
  │     ├── Distancia recorrida: Δs (longitud del arco)
  │     └── Velocidad escalar ≠ Velocidad vectorial
  │
  └── Casos particulares (rectilíneo)
        ├── MRU: a=0, v=cte, x(t) lineal
        └── MRUA: a=cte, v(t) lineal, x(t) cuadrática
              └── Caída libre: a = g ≈ 10 m/s²
```

---

## 11. Errores Comunes

### 1. Confundir distancia y desplazamiento
```
  ✗  "recorrió 10 m de desplazamiento" → si volvió, el desplazamiento puede ser 0
  ✓  distancia recorrida = 10 m,  desplazamiento = 0 m   (si volvió al origen)
```

### 2. Confundir velocidad media y velocidad instantánea
```
  ✗  "si el auto tardó 2h en ir 120 km, siempre fue a 60 km/h"
  ✓  su velocidad MEDIA fue 60 km/h; en cada instante pudo ir a cualquier velocidad
```

### 3. Creer que desaceleración implica a negativa
```
  Depende del sistema de referencia:
  Si definís positivo hacia adelante:
    v = +20 m/s, a = -5 m/s²  →  el cuerpo frena (desacelera)
  Si definís positivo hacia atrás:
    v = -20 m/s, a = +5 m/s²  →  el mismo cuerpo, mismo comportamiento físico
  
  El signo de a depende del sistema, no de la "realidad"
```

### 4. Olvidar el ½ en la ecuación de posición del MRUA
```
  ✗  x = x₀ + v₀t + at²
  ✓  x = x₀ + v₀t + ½at²

  El ½ sale de integrar: ∫at dt = ½at²
```

### 5. Mezclar unidades sin convertir
```
  ✗  v = 72 km/h, t = 30 s  →  x = 72 × 30 = 2160 ???
  ✓  Convertir primero: v = 20 m/s  →  x = 20 × 30 = 600 m
  
  Análisis dimensional hubiera detectado esto:
  (km/h) × s ≠ m   (las unidades no cuadran)
```

### 6. Confundir la ecuación v² con dirección
```
  v² = v₀² + 2a·Δx

  El resultado v² es siempre positivo → v puede ser +√ o -√
  Hay que determinar el signo de v por contexto físico (¿el objeto va o viene?)
```

---

## 12. Ejercicio Integrador

**Enunciado:**
Un colectivo que viaja a 72 km/h frena uniformemente hasta detenerse en 5 segundos.
a) ¿Cuál es la aceleración de frenado?
b) ¿Cuánto recorre mientras frena?
c) Verificar dimensionalmente la respuesta b).

**Solución:**

```
  Paso 0: Convertir unidades
    v₀ = 72 km/h = 20 m/s    (× 1000/3600)
    v_f = 0 m/s               (se detiene)
    t = 5 s

  Paso 1: Aceleración (a)
    v_f = v₀ + a·t
    0 = 20 + a·5
    a = -20/5 = -4 m/s²       (negativa → frena)

  Paso 2: Distancia recorrida durante el frenado
    x = v₀·t + ½·a·t²
    x = 20·5 + ½·(-4)·5²
    x = 100 + ½·(-4)·25
    x = 100 - 50
    x = 50 m

  Verificación dimensional:
    [v₀·t] = (m/s)·s = m    ✓
    [½·a·t²] = (m/s²)·s² = m  ✓
    [x] = m    ✓

  Verificación alternativa con v²:
    v² = v₀² + 2·a·x
    0 = 20² + 2·(-4)·x
    0 = 400 - 8x
    x = 400/8 = 50 m   ✓  (mismo resultado)
```

---

---

## 13. Caída de Cuerpos en el Vacío

La **caída libre** (o caída en el vacío) es el caso en que el único agente que actúa sobre el cuerpo es la gravedad — sin resistencia del aire. Es un MRUA con aceleración constante `g`.

```
  g ≈ 9,8 m/s²   (valor exacto)
  g ≈ 10 m/s²    (aproximación habitual en ejercicios)
```

### Convención de signos — paso previo obligatorio

Antes de plantear cualquier ecuación hay que definir el sentido positivo. Las dos convenciones más usadas:

```
  OPCIÓN A: positivo hacia ARRIBA (la más común en física universitaria)
    eje y ↑ positivo
    a = −g = −10 m/s²   (la gravedad apunta hacia abajo → negativa)

  OPCIÓN B: positivo hacia ABAJO (útil si el objeto solo cae)
    eje y ↓ positivo
    a = +g = +10 m/s²   (la gravedad apunta hacia abajo → positiva)
```

> **Regla de oro:** elegir UNA convención al principio del problema y no cambiarla. Ambas son correctas; el error es mezclarlas.

---

### Caso 1 — Objeto soltado desde el reposo (v₀ = 0)

El cuerpo se suelta desde altura H con velocidad inicial cero.

**Convención: positivo hacia abajo (simplifica los signos)**

```
  v₀ = 0    a = +g = 10 m/s²    y₀ = 0

  v(t) = g·t
  y(t) = ½·g·t²

  Tiempo de caída desde altura H:
    H = ½·g·t²  →  t = √(2H/g)

  Velocidad al llegar al suelo:
    v = g·t = g·√(2H/g) = √(2·g·H)
```

**Tabla de valores a g = 10 m/s²:**

```
  t (s)  │  v (m/s)  │  y (m)
  ───────┼───────────┼────────
    0    │     0     │    0
    1    │    10     │    5
    2    │    20     │   20
    3    │    30     │   45
    4    │    40     │   80
```

**Ejemplo:** ¿Desde qué altura cae un objeto si tarda 3 s en llegar al suelo?

```
  y = ½·g·t² = ½ × 10 × 9 = 45 m
```

---

### Caso 2 — Objeto lanzado hacia arriba con velocidad inicial

El cuerpo se lanza hacia arriba con velocidad v₀ desde el nivel del suelo.

**Convención: positivo hacia arriba**

```
  v₀ > 0    a = −g = −10 m/s²

  v(t) = v₀ − g·t
  y(t) = v₀·t − ½·g·t²
```

**Instante de altura máxima** — cuando v = 0:

```
  v = 0  →  v₀ − g·t_max = 0  →  t_max = v₀/g

  h_max = v₀·(v₀/g) − ½·g·(v₀/g)²
        = v₀²/g − v₀²/(2g)
        = v₀²/(2g)
```

**Tiempo total de vuelo** (hasta volver al suelo, y = 0):

```
  0 = v₀·t − ½·g·t²  =  t·(v₀ − ½·g·t)
  →  t = 0   (salida)
  →  t = 2v₀/g  (llegada)   =  2 × t_max

  ∴  tiempo de subida = tiempo de bajada  (simetría)
```

**Velocidad al volver al punto de lanzamiento:**

```
  v² = v₀² − 2g·(y − y₀)   con  y = y₀ = 0
  v² = v₀²   →   |v| = v₀

  Misma magnitud que al salir, sentido contrario (hacia abajo).
```

```
  Diagrama de velocidad:

  ↑ v₀              ← sube desacelerando
       ↑ v₀/2
            v=0     ← altura máxima
       ↓ v₀/2
  ↓ v₀              ← baja acelerando (misma magnitud al llegar)
```

**Ejemplo:** Pelota lanzada hacia arriba con v₀ = 20 m/s.

```
  t_max = 20/10 = 2 s

  h_max = 20²/(2×10) = 400/20 = 20 m

  t_vuelo = 2 × 2 = 4 s

  v al volver = 20 m/s (hacia abajo)
```

---

### Caso 3 — Objeto lanzado hacia abajo con velocidad inicial

El cuerpo se lanza desde altura H con velocidad v₀ hacia abajo.

**Convención: positivo hacia abajo**

```
  v₀ > 0    a = +g = 10 m/s²    y₀ = 0

  v(t) = v₀ + g·t           ← ya tiene velocidad inicial en el sentido de caída
  y(t) = v₀·t + ½·g·t²

  Velocidad al llegar al suelo (recorre distancia H):
    v² = v₀² + 2·g·H
    v = √(v₀² + 2gH)
```

---

### Gráficas — objeto lanzado hacia arriba

```
  y(t)                    v(t)                  a(t)
   │      *               │  v₀                  │
   │    *   *             │ /                     │ ─────────────
   │   *     *            │/                      │
   │  *       *           ●──────────── t         │     −g
   │ *         *          │\                      │
   │*           *         │ \                     │
   ●─────────────── t     │  −v₀                  └────────────── t

  Parábola cóncava ↓     Recta decreciente       Constante (−g)
  Pico = h_max           Cruza en t_max          (negativo en conv. ↑)
```

---

### Tabla resumen — caída de cuerpos

| Caso | v₀ | Ecuación y(t) (conv. ↑) | Tiempo suelo | Velocidad suelo |
|---|---|---|---|---|
| Soltado | 0 | `−½gt²` (desde H) | `√(2H/g)` | `√(2gH)` |
| Lanzado ↑ | `+v₀` | `v₀t − ½gt²` | `2v₀/g` | `v₀` (↓) |
| Lanzado ↓ | `−v₀` | `−v₀t − ½gt²` | despejar | `√(v₀²+2gH)` |

---

## 14. Tiro Oblicuo

El **tiro oblicuo** es el movimiento de un proyectil lanzado con velocidad inicial `v₀` formando un ángulo `θ` con la horizontal. Es el caso más general de movimiento en el plano.

**Idea central:** el movimiento se descompone en dos independientes:
```
  Eje x  →  MRU    (no hay fuerza horizontal, ignorando el aire)
  Eje y  →  MRUA   (actúa la gravedad, a = −g)
```

```
              v₀
              /
             /  ← ángulo θ con la horizontal
            /θ
           ●──────────────────────────────────────────
          P₀                                     suelo
```

---

### Descomposición de la velocidad inicial

```
  vₓ₀ = v₀ · cos(θ)     ← componente horizontal
  v_y₀ = v₀ · sen(θ)    ← componente vertical
```

```
         v_y₀ = v₀·sen(θ)
           ↑
           │  /  v₀
           │ /
           │/ θ
           ●─────────────→  vₓ₀ = v₀·cos(θ)
```

---

### Ecuaciones de movimiento

**Componente horizontal (MRU):**

```
  vₓ(t) = v₀·cos(θ)          ← constante en todo el vuelo

  x(t)  = v₀·cos(θ)·t        ← crece linealmente
```

**Componente vertical (MRUA con a = −g, conv. positivo ↑):**

```
  v_y(t) = v₀·sen(θ) − g·t   ← decrece, se anula en h_max, luego negativa

  y(t)   = v₀·sen(θ)·t − ½·g·t²
```

**Velocidad en cualquier instante:**

```
  v(t) = √(vₓ² + v_y²)       ← módulo

  α(t) = arctan(v_y/vₓ)      ← ángulo con la horizontal (varía en el tiempo)
```

---

### Puntos clave del movimiento

**Altura máxima** — cuando v_y = 0:

```
  0 = v₀·sen(θ) − g·t_sub
  t_sub = v₀·sen(θ) / g

  h_max = (v₀·sen(θ))² / (2g)
```

**Tiempo total de vuelo** (regresa a y = 0):

```
  0 = v₀·sen(θ)·t − ½·g·t²  =  t·[v₀·sen(θ) − ½·g·t]
  →  t = 0   (salida)
  →  t_vuelo = 2·v₀·sen(θ) / g  =  2·t_sub
```

**Alcance horizontal (rango R):**

```
  R = vₓ₀ · t_vuelo
    = v₀·cos(θ) · 2·v₀·sen(θ)/g
    = v₀²·sen(2θ) / g            ← usando identidad: 2·senθ·cosθ = sen(2θ)
```

**Ángulo de máximo alcance:**

```
  R es máximo cuando sen(2θ) = 1  →  2θ = 90°  →  θ = 45°

  R_max = v₀² / g
```

**Ángulos complementarios — mismo alcance:**

```
  sen(2θ) = sen(2·(90°−θ))  →  θ y (90°−θ) producen igual R

  Ejemplos: 30° y 60°, 20° y 70°, 15° y 75°   → mismo alcance horizontal
```

```
        h_max (45° < θ < 90°, más alto)
        │
        │         h_max (θ = 45°)
        │           │
        │   h_max (θ < 45°, más bajo)
        │     │     │
  ──────┼─────┼─────┼──────────────────→ x
        0           R_max

  Todos estos ángulos pueden dar el mismo R si son complementarios
```

---

### Ecuación de la trayectoria (parábola)

Eliminar el tiempo `t` entre las ecuaciones de x e y:

```
  De x:  t = x / (v₀·cos θ)

  Sustituir en y:

  y = v₀·senθ · x/(v₀cosθ)  −  ½g · [x/(v₀cosθ)]²

  y = x·tanθ  −  g·x² / (2·v₀²·cos²θ)
```

**Es la ecuación de una parábola** `y = Ax + Bx²` con:
- `A = tan θ` (pendiente inicial)
- `B = −g/(2v₀²cos²θ)` (coeficiente negativo → abre hacia abajo)

---

### Velocidad en cualquier punto de la trayectoria

```
  vₓ = v₀·cosθ              (constante)
  v_y = v₀·senθ − g·t       (varía)

  En la altura máxima: v_y = 0  →  v = vₓ = v₀·cosθ  (mínima velocidad del vuelo)
  En el suelo al caer: v_y = −v₀·senθ  →  |v| = v₀    (misma que al salir)
```

---

### Ejercicio resuelto completo

**Enunciado:** Un proyectil se lanza con v₀ = 40 m/s a θ = 30° sobre la horizontal desde el suelo. Calcular: a) altura máxima, b) tiempo de vuelo, c) alcance horizontal.

```
  Datos:
    v₀ = 40 m/s     θ = 30°     g = 10 m/s²

  Componentes:
    vₓ₀ = 40·cos(30°) = 40 × 0,866 = 34,64 m/s
    v_y₀ = 40·sen(30°) = 40 × 0,5  = 20 m/s

  a) Altura máxima:
    t_sub = v_y₀/g = 20/10 = 2 s
    h_max = v_y₀²/(2g) = 20²/(2×10) = 400/20 = 20 m

  b) Tiempo de vuelo:
    t_vuelo = 2·t_sub = 2 × 2 = 4 s

  c) Alcance horizontal:
    R = vₓ₀·t_vuelo = 34,64 × 4 = 138,56 m

    Verificación con fórmula directa:
    R = v₀²·sen(2θ)/g = 40²·sen(60°)/10 = 1600×0,866/10 = 138,56 m  ✓
```

---

### Casos especiales del tiro oblicuo

| Ángulo θ | Movimiento |
|---|---|
| 0° | Tiro horizontal (proyectil lanzado horizontalmente) |
| 90° | Lanzamiento vertical (tiro hacia arriba, sube y baja) |
| 45° | Máximo alcance horizontal |
| θ y (90°−θ) | Mismo alcance, distintas trayectorias |

**Tiro horizontal (θ = 0°) — caso frecuente en ejercicios:**

```
  vₓ₀ = v₀    v_y₀ = 0

  x(t) = v₀·t           (MRU)
  y(t) = −½·g·t²        (cae desde altura H)

  Tiempo de caída: t = √(2H/g)   (igual que caída libre, independiente de v₀)
  Alcance:         R = v₀·√(2H/g)
```

---

### Tabla resumen — tiro oblicuo

| Magnitud | Fórmula |
|---|---|
| Componentes de v₀ | `vₓ₀ = v₀cosθ` · `v_y₀ = v₀senθ` |
| Posición x(t) | `x = v₀cosθ · t` |
| Posición y(t) | `y = v₀senθ · t − ½gt²` |
| Velocidad vₓ(t) | `v₀cosθ` (constante) |
| Velocidad v_y(t) | `v₀senθ − gt` |
| Tiempo a h_max | `t_sub = v₀senθ / g` |
| Altura máxima | `h_max = (v₀senθ)² / (2g)` |
| Tiempo de vuelo | `t_vuelo = 2v₀senθ / g` |
| Alcance | `R = v₀²sen(2θ) / g` |
| Alcance máximo | `R_max = v₀²/g` (a θ=45°) |
| Trayectoria | `y = x·tanθ − gx²/(2v₀²cos²θ)` |

---

*Fuentes: clase de Física I (UTN FRBA, abril–mayo 2026) — cinemática: MRU, MRUA, caída libre y tiro oblicuo; `Programa- Bibliografia.pdf` (Física I). Elaborado para Ingeniería Mecánica, sistema MKS.*
