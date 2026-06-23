# Clase 9 — Cargas cíclicas y fatiga

**Fecha:** 4 de junio de 2026  
**Profesor:** Abud  
**Continuación de:** Clase 8 (28/05) — pérdida de estabilidad, pandeo, P_cr de Euler

---

## 1. El ejemplo que organiza la clase: el eje de un tren

Abud eligió un **eje de ferrocarril** como caso de estudio. La situación es:

- Un eje (barra cilíndrica maciza) está simplemente apoyado en sus extremos (los rodamientos)
- Está cargado por el peso del vagón en dos puntos simétricos, separados una distancia `a` de cada apoyo
- El eje **gira** mientras el tren avanza

```
  apoyo A                                        apoyo B
    ↑                                               ↑
    ├────── a ──────┬──────────────────┬────── a ────┤
                    ↓ P                ↓ P
                  (rueda izq.)     (rueda der.)
```

La región **entre las dos cargas** tiene momento flector **constante** (no varía con z en ese tramo) — esto se llama flexión pura. Es el segmento más crítico del análisis.

### El diagrama de momento flector

```
  M
   │
   │            ┌─────────────────┐
   │           /│                 │\
   │          / │                 │ \
   │         /  │    M = P · a    │  \
   │        /   │   (constante)   │   \
   │       /    │                 │    \
  ─┼──────────────────────────────────────── z
  apoyo A    carga               carga    apoyo B
             izq.                der.
  (M = 0)                                 (M = 0)
```

Cero en los apoyos (extremos), máximo constante en el tramo central: es exactamente lo que describiste.

### Distribución de tensiones en la sección transversal

En el tramo central, con M = P·a, la distribución de tensiones normales a través de la sección es:

```
  eje de la fibra → compresión (σ < 0)
  ─────────────────────────────────────────
                    EJE NEUTRO  → σ = 0
  ─────────────────────────────────────────
  eje de la fibra → tracción (σ > 0)
```

- Desde el eje neutro hacia **arriba**: compresión
- Desde el eje neutro hacia **abajo**: tracción
- La distribución es lineal: máxima en la superficie, cero en el eje neutro (idéntico a lo que vimos en clase 6 con σ = M·y/I)

---

## 2. El problema: el eje gira

Hasta acá, todo lo que vimos aplica a una viga estática. Lo que cambia aquí es que el eje **gira**. Y eso transforma completamente la naturaleza de la solicitación.

Pensemos en un punto fijo sobre la superficie del eje (por ejemplo, una marca de pintura). Cuando ese punto está arriba del eje neutro, está en compresión. Cuando el eje gira y ese punto queda abajo del eje neutro, está en tracción. Con cada vuelta completa, el punto pasa de compresión máxima a tracción máxima y vuelve.

```
  Un punto en la superficie del eje, a lo largo de una vuelta:

  posición   → tensión en ese punto
  ─────────────────────────────────────────────────
  arriba     → compresión máxima (σ = -σ_max)
  lateral    → σ = 0
  abajo      → tracción máxima (σ = +σ_max)
  lateral    → σ = 0
  arriba     → compresión máxima (σ = -σ_max)   ← volvió al inicio
  ...
```

Este es el fenómeno de la **carga cíclica**: el mismo punto del material es sometido alternadamente a tracción y compresión, con cada vuelta del eje.

---

## 3. Modelo matemático: σ(t) = f(rotación)

Abud construyó la expresión matemática de cómo varía la tensión en un punto de la superficie con el tiempo.

### Geometría de la rotación

Sea un punto en la superficie del eje a distancia `y` del eje neutro. El radio de la sección es `D/2`. El ángulo `α` indica la posición angular del punto respecto al eje neutro:

```
       eje neutro
          │
          │     ·  ← punto en la superficie
          │   /
          │  /  α
          │ /
          │/
         eje del cilindro
```

La distancia `y` del punto al eje neutro en función del ángulo:

```
  sen(α) = y / (D/2)   →   y = (D/2) · sen(α)
```

### Introducir la rotación en el tiempo

Como el eje gira con velocidad angular ω (omega):

```
  α = ω · t
```

Y la velocidad angular se relaciona con las revoluciones por segundo n:

```
  ω = 2π · n    [rad/s]
```

Entonces la posición del punto respecto al eje neutro en función del tiempo:

```
  y(t) = (D/2) · sen(ω · t)
```

### La tensión como función del tiempo

Usando la fórmula de flexión σ = M·y/I (con M = P·a constante en el tramo central):

```
  σ(t) = M · y(t) / I_xx = P · a · (D/2) · sen(ω·t) / I_xx

               P · a · D · sen(ω·t)
  σ(t) = ─────────────────────────────
                    2 · I_xx
```

Esta es la tensión en un punto de la superficie del eje en función del tiempo: una **sinusoide** perfecta.

> **Nota:** en las notas de clase aparece "G" para esta tensión — es la letra griega σ (sigma) que en escritura manuscrita puede parecerse a una G. Es la misma tensión normal que venimos usando.

### La tensión máxima

Cuando `sen(ω·t) = 1` (punto en la posición extrema inferior o superior):

```
        P · a · D
  σ_max = ─────────────
           2 · I_xx
```

Esta es la amplitud de la oscilación de tensión. El punto en la superficie pasa de `+σ_max` (tracción) a `−σ_max` (compresión) con cada vuelta.

```
  σ(t)
   │   ╭─╮        ╭─╮
   │  ╭╯  ╰╮    ╭╯  ╰╮
  ─┼─╯     ╰────╯     ╰──── t
   │
   │╰╮  ╭╯╰╮  ╭╯
   │  ╰─╯   ╰─╯
   │
  -σ_max              +σ_max arriba, -σ_max abajo
```

---

## 4. Fatiga — definición y concepto

> **Fatiga** es la falla progresiva de un material sometido a cargas cíclicas repetidas, incluso cuando la tensión máxima aplicada está **por debajo** del límite elástico del material.

Este es el punto vital: el material **no falla en la primera aplicación de carga** — podría aplicarse una vez sin consecuencias. El problema es la repetición. Con millones de ciclos, el material desarrolla microfisuras que crecen gradualmente hasta provocar una rotura abrupta.

### Por qué es tan importante

Un eje de ferrocarril gira miles de veces por kilómetro recorrido. Un motor a 3.000 RPM somete sus componentes a 50 ciclos de tensión por segundo. Una hélice de avión, un eje de transmisión, un resorte de válvula — todos trabajan bajo fatiga. La mayoría de las fallas mecánicas en servicio son por fatiga, no por sobrecarga estática.

### Fatiga es puramente empírica — no hay ley

Abud lo marcó explícitamente: a diferencia de la flexión (σ = M·c/I) o la torsión (τ = G·ρ·θ), **no existe una fórmula teórica para predecir la fatiga**. Solo se pueden determinar los límites de fatiga experimentalmente, ensayando muestras a distintas amplitudes de tensión y contando los ciclos hasta la rotura.

Los resultados se grafican en la **curva S-N** (o curva de Wöhler): tensión S en función del número de ciclos N hasta la rotura. Cada punto de la curva es un ensayo de fatiga. La curva la construye el laboratorio, no la ecuación.

---

## 5. La superficie de rotura por fatiga — dos zonas

Una pieza rota por fatiga siempre muestra **dos zonas diferenciadas** en la superficie de fractura:

```
  Vista de la sección de rotura:

  ┌─────────────────────────────┐
  │  ZONA LISA                  │  ← propagación de fisura (lenta, progresiva)
  │  (pulida, brillante)        │
  │  ─────────────────          │
  │  ZONA RUGOSA                │  ← rotura final (brusca, frágil)
  │  (granular, opaca)          │
  └─────────────────────────────┘
```

### Zona lisa

- Aquí comenzó todo: una **microfisura** en un punto de irregularidad de la pieza
- La fisura avanza muy lentamente con cada ciclo — apenas nanómetros por ciclo
- Como las caras de la fisura se abren y cierran millones de veces, quedan pulidas (de ahí el aspecto liso y brillante)
- Esta zona puede ocupar la mayor parte de la sección antes de que el operador note algo

### Zona rugosa

- Cuando la fisura creció lo suficiente, la sección resistente restante ya no soporta la carga
- Ocurre una **rotura frágil súbita** — idéntica a la que ocurriría en una probeta frágil bajo carga estática
- La superficie es granular y rugosa porque fue una fractura rápida, sin el pulido de ciclos sucesivos

### ¿Dónde inician las microfisuras?

Siempre en un punto de **concentración de tensión**:
- Irregularidades superficiales (rayaduras, marcas de torno, óxido)
- Cambios bruscos de sección (entallas, ranuras de chaveta)
- Inclusiones o impurezas del material
- Porosidades internas

Por eso el acabado superficial es crítico en piezas sometidas a fatiga: una pieza pulida resiste muchos más ciclos que una con la misma geometría pero superficie rugosa.

---

## 6. Tipos de ciclos

Abud describió tres tipos de ciclo de tensión:

### Ciclo simétrico (o alternado)

La tensión oscila simétricamente alrededor de cero. La tensión media es cero.

```
  σ
   │   ╭─╮   ╭─╮
   │  ╱  ╰─╮╱  ╰─╮
  ─┼─────────────────── t     σ_med = 0
   │        ╰─╯   ╰─
   │
  → el eje del ferrocarril es un ejemplo clásico de ciclo simétrico
```

### Ciclo de pulsación

La tensión va desde un máximo (o mínimo) hasta **cero**. La tensión media es distinta de cero.

```
  σ
   │  ╭─╮   ╭─╮
   │ ╱  ╰─╮╱  ╰─╮
  ─┼─╯    ╰─╯   ╰──── t     σ_min = 0
   │
  → ejemplo: un resorte que se comprime y vuelve a su posición natural (nunca se estira)
```

### Ciclo genérico

La tensión oscila alrededor de una tensión media constante no nula. Es el caso más general.

```
  σ
   │       ╭─╮   ╭─╮
   │──────╱──╰─╮╱──╰─╮────── σ_med (tensión media constante)
   │      ╯   ╰─╯   ╰
  ─┼──────────────────────── t
  → ejemplo: un eje que además de flexión alternante lleva una carga axial estática de tracción
```

---

## 7. El límite de fatiga

Experimentalmente se encontró que para el acero existe una tensión por debajo de la cual el material **no falla por fatiga**, sin importar cuántos ciclos se apliquen. Ese valor se llama **límite de fatiga** (σ_f).

> **Abud:** σ_max ≈ 0,4 a 0,5 × σ_rotura

Para acero, el límite de fatiga en ciclo simétrico es aproximadamente el 40-50% de la resistencia a la rotura estática. Esto es una relación empírica, no una ley.

```
  σ_rotura = 600 MPa  →  σ_f ≈ 240 a 300 MPa  (límite de fatiga estimado)
```

Para el diseño: si la amplitud de tensión cíclica en servicio está por debajo de σ_f, la pieza tiene **vida infinita** (no falla por fatiga). Si la supera, falla en un número finito de ciclos que depende de cuánto la supera.

> **Importante:** el aluminio y muchos otros metales no ferrosos **no tienen límite de fatiga verdadero** — siempre fallan eventualmente si se aplican suficientes ciclos, aunque la tensión sea muy baja. El acero es el material más favorable en este sentido.

---

## Resumen de la clase

| Concepto | Definición |
|---|---|
| Carga cíclica | Tensión que varía repetidamente entre máximo y mínimo con cada ciclo |
| σ(t) = P·a·D·sen(ωt) / (2·I_xx) | Tensión en la superficie de un eje giratorio en función del tiempo |
| σ_max = P·a·D / (2·I_xx) | Amplitud máxima de tensión (para sen = 1) |
| ω = 2π·n | Velocidad angular en función de las revoluciones por segundo |
| Fatiga | Falla progresiva por cargas cíclicas, con σ_max < σ_elástico |
| Fatiga es empírica | No existe fórmula teórica — solo curvas S-N experimentales |
| Zona lisa | Propagación lenta de microfisura — superficie pulida |
| Zona rugosa | Rotura final brusca — superficie granular |
| Inicio de fisuras | Siempre en un punto de concentración de tensión (irregularidad superficial) |
| Ciclo simétrico | σ oscila entre +σ_max y −σ_max; tensión media = 0 |
| Ciclo de pulsación | σ oscila entre σ_max y 0 |
| Ciclo genérico | Oscilación alrededor de una tensión media no nula |
| Límite de fatiga (acero) | σ_f ≈ 0,4 a 0,5 × σ_rotura |

---
*Fuente: apuntes de clase — Prof. Abud, 04/06/2026*
