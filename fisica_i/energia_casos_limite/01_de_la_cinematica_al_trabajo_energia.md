# De la cinemática al trabajo y la energía cinética

## Punto de partida: las dos ecuaciones que ya tenías

Todo lo que sigue sale de dos ecuaciones de movimiento rectilíneo uniformemente acelerado (cap. 2 del Sears), las mismas con las que arrancó toda la cursada:

```
(1)   v = v₀ + a·t
(2)   x = x₀ + v₀·t + ½·a·t²
```

`v₀` es la *initial velocity*, `a` es constante (aceleración constante — el caso que se trabaja en todo el capítulo 2). El objetivo: sacar el tiempo `t` de la jugada, porque en la mayoría de los problemas de energía no importa *cuánto tardó* algo en pasar, importa *cuánto se desplazó* bajo qué fuerza.

## Paso 1 — despejar t de (1)

```
v = v₀ + a·t
v - v₀ = a·t

        v - v₀
   t = ────────
          a
```

## Paso 2 — sustituir en (2)

Tomando `x₀ = 0` y llamando `Δx = x` al desplazamiento:

```
        (v - v₀)      1     (v - v₀)²
Δx = v₀·──────── + ─·a·─────────────
            a       2         a²
```

Sacando factor común `1/a` y operando el numerador:

```
        2·v₀·(v - v₀) + (v - v₀)²
Δx = ─────────────────────────────
                 2·a
```

El numerador es `(v - v₀)·[2v₀ + (v - v₀)] = (v - v₀)·(v + v₀) = v² - v₀²` (diferencia de cuadrados). Queda:

```
                v² - v₀²
        Δx = ────────────
                  2·a

  →      v² = v₀² + 2·a·Δx
```

Esta es la ecuación a la que llegaste vos solo, y es la tercera ecuación clásica de cinemática — la que no tiene `t`. Hasta acá, cero física nueva: es álgebra sobre lo que ya sabías.

## Paso 3 — el salto: multiplicar por m/2

Acá es donde cinemática (que describe *cómo* se mueve algo) se convierte en dinámica de la energía (que describe *qué hace falta* para que se mueva así). Multiplicá los dos lados de `v² = v₀² + 2·a·Δx` por `m/2`:

```
   m         m
   ─·v²  =   ─·v₀²  +  m·a·Δx
   2         2
```

El lado izquierdo menos el primer término del derecho es, por definición, la diferencia de **energía cinética** (*Kinetic Energy*, `K = ½·m·v²`, en joules):

```
   ½·m·v² - ½·m·v₀²  =  m·a·Δx  =  (m·a)·Δx
```

Y por la segunda ley de Newton (cap. 4), `m·a = F` — la fuerza neta que causó esa aceleración. `F·Δx`, cuando `F` es constante y apunta en la dirección del desplazamiento, es exactamente la definición de **trabajo** (*Work*, `W`). Entonces:

```
        ΔK  =  W

   ½·m·v² - ½·m·v₀²  =  F·Δx
```

Este es el **teorema trabajo-energía** (*work-energy theorem*), cap. 6. No es un axioma nuevo que hay que memorizar por separado: es la ecuación de cinemática que ya usabas, mirada desde el ángulo de la fuerza y no del tiempo.

## Definiciones formales, ahora que ya se entiende de dónde salen

```
  Work            W = F · d · cos θ         [N·m = J]
  Kinetic Energy  K = ½ · m · v²            [kg·m²/s² = J]
  Work-Energy Th. W_net = ΔK = K_f - K_i    [J]
  Power           P = W / t   (promedio)    [J/s = W]
                  P = F · v   (instantánea) [W]
```

`θ` es el ángulo entre la fuerza y el desplazamiento — si empujás algo perpendicular a cómo se mueve (por ejemplo, cargar una valija caminando horizontal mientras la sostenés hacia arriba), el trabajo de esa fuerza es cero aunque haya fuerza y haya movimiento. Es una trampa clásica de examen.

## Chequeo de unidades (porque recién te estás acostumbrando a N, J y W)

```
  [a] = m/s²                    (cap. 2)
  [F] = kg · m/s²  =  N         (cap. 4, F = m·a)
  [W] = N · m = kg·m²/s² = J    (cap. 6)
  [P] = J/s = kg·m²/s³ = W      (cap. 6)
```

Un vatio (`W`, la unidad — no confundir con `W` de *Work*, el libro reutiliza la letra) es un joule por segundo. Si en algún cálculo te da un resultado en `kg·m²/s³` y no lo simplificaste a W, es una señal de que no cerraste unidades.

## Nota al margen: μs y μk, para más adelante

El capítulo 5 introduce la fricción con dos coeficientes: `μs` (*static*, fricción estática — la que hay que vencer para que algo *empiece* a moverse) y `μk` (*kinetic*, fricción cinética — la que actúa mientras ya se está moviendo, típicamente algo menor que `μs`). No entran todavía en esta carpeta porque los casos de `03` y `04` asumen que no hay fricción relevante en el aire (sí hay resistencia aerodinámica, que es otra cosa, no fricción de contacto) — pero van a ser necesarios el día que se quiera modelar, por ejemplo, la fricción del pie del atleta contra el suelo del círculo de bala, que es justamente lo que le permite empujar sin resbalar.

## Mapa de la derivación

```
  v = v₀ + a·t  ──┐
                   ├─→  v² = v₀² + 2·a·Δx  ──→  ½mv² - ½mv₀² = m·a·Δx
  x = x₀+v₀t+½at² ─┘         (cap. 2)                    │
                                                            │ F = m·a  (cap. 4)
                                                            ▼
                                                   ΔK = F·Δx = W
                                                   (cap. 6 — work-energy theorem)
```
