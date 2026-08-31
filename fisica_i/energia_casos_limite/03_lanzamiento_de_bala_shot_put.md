# Caso límite 1 — Lanzamiento de bala (shot put)

## El objeto y la cancha

```
   Masa oficial de la bala (shot):
     Varones:  7.26 kg   (16 lb)
     Damas:    4.00 kg

   Círculo de lanzamiento:
                     ┌──────────────┐
                    ╱                ╲
                   │   diámetro       │
                   │   2.135 m        │
                    ╲                ╱
                     └──────tope─────┘     ← "stop board", 10 cm de alto,
                                              al frente del círculo

              sector de caída: 34.92°  (medido desde el centro del círculo)
```

A diferencia de la jabalina (`04`), acá el atleta **no corre en línea recta**: se mueve dentro de un círculo de apenas 2.135 m de diámetro, con una técnica de traslación (*glide*, deslizamiento) o de giro (*spin*, técnica rotacional, tomada del disco). Confirma la intuición: bala es rotacional/circular, jabalina es longitudinal — son biomecánicamente parientes distintos aunque el objetivo final (maximizar el alcance de un proyectil) sea el mismo problema de cap. 3.

## Los números de elite

| | Varones | Damas |
|---|---|---|
| Récord mundial | Ryan Crouser — 23.56 m (2023) | Natalya Lisovskaya — 22.63 m (1987) |
| Masa del objeto | 7.26 kg | 4.00 kg |

Referencia de biomecánica medida (no récord de distancia, sino el mejor dato de velocidad de salida documentado): en el Mundial 2018, **Tom Walsh** registró la mayor velocidad de salida del campeonato: **14.12 m/s**, con un ángulo de salida de **37.3°** y una altura de liberación de **2.11 m** sobre el suelo.

## Energía cinética en el instante de la suelta

Con el teorema trabajo-energía de `01` (`K = ½mv²`), usando el dato real de Walsh:

```
   K = ½ · 7.26 kg · (14.12 m/s)²
   K = ½ · 7.26 · 199.37
   K ≈ 723.7 J
```

Para tener una referencia: son casi 724 julios entregados a un objeto en una fracción de segundo — comparalo con los 2 J del experimento casero de `02` para "mi mano mueve 1 kg, 1 m, en 1 s". Tres órdenes de magnitud de diferencia, y el objeto acá pesa siete veces más, no menos.

## ¿Por qué el ángulo óptimo NO es 45°?

Cap. 3 (*Motion in Two or Three Dimensions*) da el alcance de un proyectil lanzado y aterrizado **al mismo nivel**: ahí sí, 45° maximiza el alcance. Pero acá la bala sale de una altura `h = 2.11 m` y cae al nivel del piso — no es el mismo problema. Hay que rehacer el cálculo con esa altura de salida, que es álgebra directa sobre las ecuaciones de posición de cap. 3 — que no son dos fórmulas sueltas, sino las dos componentes del vector posición `r⃗(t) = (x(t), y(t))`, cada una viniendo de descomponer la velocidad de salida `v⃗` en sus componentes `vx = v·cos θ` y `vy = v·sin θ` con `θ` medido desde el eje `+x`:

```
   x(t) = v·cos θ · t
   y(t) = h + v·sin θ · t - ½·g·t²
```

Igualando `y(t) = 0` (cuando toca el piso) y resolviendo la cuadrática en `t` (raíz positiva):

```
          v·sin θ + √( (v·sin θ)² + 2·g·h )
   t  =  ────────────────────────────────────
                        g
```

Sustituyendo en `x(t)`, el alcance con altura de salida es:

```
        v·cos θ
   R = ───────── · [ v·sin θ + √(v²·sin²θ + 2·g·h) ]
           g
```

Maximizando `R` respecto de `θ` (cálculo que no vamos a desplegar acá, es derivar e igualar a cero), el resultado conocido es:

```
                    v
   θ_óptimo = arctan( ──────────────── )
                    √(v² + 2·g·h)
```

Con `v = 14.12`, `h = 2.11`, `g = 9.80665`:

```
   v² = 199.37
   2·g·h = 2 · 9.80665 · 2.11 ≈ 41.38
   v² + 2·g·h ≈ 240.75  →  √240.75 ≈ 15.52

   θ_óptimo = arctan(14.12 / 15.52) = arctan(0.910) ≈ 42.3°
```

Coincide con lo que reporta la literatura de biomecánica del atletismo: la teoría pura de alcance da un óptimo de **41°–43°** — mi cálculo con los datos reales de Walsh cae justo en ese rango. Pero los mejores lanzadores del mundo, en la práctica, sueltan a **37°–38°**, no a 42°. La diferencia no es un error de técnica: es que `v` y `θ` **no son independientes** en el cuerpo humano. El brazo y el tronco generan más velocidad de salida cuando el ángulo de salida es más bajo (biomecánicamente, empujar "más horizontal" permite aplicar fuerza en un recorrido más largo y más alineado con la cadena de piernas-tronco-brazo). Como la distancia depende de `v²` pero de `θ` con menos peso relativo (~75% de la variación del alcance entre lanzadores de elite se explica por `v`, no por `θ`), conviene sacrificar unos grados de ángulo "ideal" a cambio de más velocidad. Ese ajuste fino ya es biomecánica del deporte, no física de proyectiles pura — pero el modelo de cap. 3 explica el 90% del fenómeno y predice el rango correcto.

## Estimación de potencia

Acá hay que ser honesto sobre qué es dato y qué es supuesto: la velocidad de salida (14.12 m/s) y la masa (7.26 kg) son datos reales. La *duración* de la fase final de aceleración (desde que el atleta empieza a extender el brazo hasta la suelta) no la tengo medida — la literatura de biomecánica la ubica, según técnica y atleta, en un rango aproximado de **0.10 a 0.20 s**. Con eso:

| t supuesto (s) | P = K/t (W) |
|---|---|
| 0.10 | ≈ 7 240 W |
| 0.15 | ≈ 4 825 W |
| 0.20 | ≈ 3 620 W |

Tomando el punto medio (~0.15 s) como estimación central: **≈ 4.8 kW** de potencia promedio en la fase final del lanzamiento de bala. En `05` esto se compara con otras potencias humanas documentadas — spoiler: cae justo en el rango de la segunda tirada (*second pull*) de una arrancada olímpica de halterofilia, que también dura una fracción de segundo.

---
**Fuentes:** World Athletics (récords y especificaciones oficiales de la bala, círculo y sector); datos de velocidad/ángulo/altura de salida de Tom Walsh, Mundial de Atletismo 2018; N. Linthorne, *Optimum release angle in the shot put* (modelo de ángulo óptimo con altura de liberación); `g = 9.80665 m/s²` (valor estándar, el mismo que usa la calculadora).
