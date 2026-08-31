# Calibración personal: el joule humano

## La pregunta que no dejaba dormir

"Con mi mano puedo mover una masa de 1 kg, una distancia de 1 metro, en más o menos 1 segundo. ¿Eso significa que puedo generar 1 joule? ¿1 watt, si lo hago justo en 1 segundo?"

Es una buena pregunta porque es *calculable* con exactamente las herramientas de `01`: cinemática de aceleración constante + `F = m·a` + `K = ½mv²`. Nada de esto necesita el capítulo 7 ni el 8. Vamos al número.

## El cálculo, paso a paso

Supuestos del experimento: `m = 1 kg`, arranca desde `v₀ = 0`, recorre `Δx = 1 m` en `t = 1 s`, con aceleración constante (la mano empuja parejo, no de un tirón).

**Aceleración necesaria**, de `Δx = ½·a·t²`:

```
   1 = ½ · a · 1²   →   a = 2 m/s²
```

**Fuerza necesaria** (cap. 4, `F = m·a`):

```
   F = 1 kg · 2 m/s² = 2 N
```

Dos newtons es *poco* — el peso de una manzana chica (`w = m·g ≈ 0.2 kg · 9.8 ≈ 2 N`). Empujar 1 kg, 1 metro, en 1 segundo, no exige casi nada de fuerza.

**Velocidad final** (`v = v₀ + a·t`):

```
   v = 0 + 2·1 = 2 m/s
```

**Energía cinética entregada** (`K = ½mv²`, y como arrancó del reposo, `ΔK = K`, y por el teorema trabajo-energía `ΔK = W`, el trabajo que hizo tu mano):

```
   K = ½ · 1 · 2² = 2 J
```

**No es 1 joule — son 2.** La intuición estaba en el orden de magnitud correcto, pero no exacta: para que la masa *recorra* 1 metro en 1 segundo arrancando del reposo con aceleración constante, tiene que salir con el doble de velocidad promedio de lo que uno imagina a ojo (la velocidad promedio es 1 m/s, y en efecto arranca en 0 y termina en 2 m/s, promedio `(0+2)/2 = 1`, eso cierra — lo que falla la intuición es que la energía depende de `v²`, no de la velocidad promedio).

**Potencia promedio:**

```
   P = W / t = 2 J / 1 s = 2 W
```

**Potencia instantánea en el instante de soltar** (`P = F·v`, con la velocidad final):

```
   P = 2 N · 2 m/s = 4 W
```

El pico instantáneo (4 W) es el doble del promedio (2 W) — tiene sentido, porque la potencia crece linealmente de 0 a 4 W a lo largo del segundo (fuerza constante, velocidad creciente), y el promedio de una rampa lineal es la mitad del pico. Esto va a importar en `05`, porque las cifras de potencia "de récord" que vas a encontrar en biomecánica casi siempre son picos instantáneos, no promedios — hay que tener cuidado de no comparar peras con manzanas.

## Y si aprieto los tiempos, ¿qué pasa?

Repitiendo la misma cuenta (`m = 1 kg`, `Δx = 1 m`) pero variando cuánto tarda:

```
  a = 2/t²  (m/s²)     F = 2/t²  (N, porque m=1)     v = 2/t  (m/s)
  K = 2/t²  (J)        P = K/t = 2/t³  (W)
```

| t (s) | a (m/s²) | F (N) | v (m/s) | K (J) | P promedio (W) |
|---|---|---|---|---|---|
| 1.00 | 2 | 2 | 2 | 2 | 2 |
| 0.50 | 8 | 8 | 4 | 8 | 16 |
| 0.20 | 50 | 50 | 10 | 50 | 250 |
| 0.10 | 200 | 200 | 20 | 200 | 2 000 |
| 0.05 | 800 | 800 | 40 | 800 | 16 000 |

La potencia escala con `1/t³` — achicar el tiempo a la mitad multiplica la potencia por 8, no por 2. Esto es la matemática detrás de por qué los deportes explosivos (lanzamientos, saltos, la salida de una carrera) generan potencias brutales con fuerzas que, aisladas, no sorprenden tanto:

- **t = 0.1 s** (`F = 200 N`, `P = 2 000 W`): 200 N son ~20 kgf — una fuerza fuerte pero perfectamente humana para un empujón corto (una trompada, un golpe de tenis). La potencia resultante, 2 000 W, ya está en el orden de magnitud del pico de Usain Bolt saliendo de los tacos (ver `05`).
- **t = 0.05 s** (`F = 800 N`, `P = 16 000 W`): 800 N (~82 kgf) generados por *un solo brazo* en 0.05 s ya no es realista — fuerzas de ese orden aparecen en biomecánica humana, pero como resultado de todo el cuerpo (piernas + tronco) actuando en cadena, no de un brazo empujando un objeto de 1 kg. Es la señal de que el modelo "una mano empuja una masa chica" dejó de alcanzar y hay que pasar a otro objeto de estudio.

Ese último punto es exactamente la bisagra hacia `03` y `04`: el lanzamiento de bala y de jabalina son, físicamente, el mismo experimento de esta hoja — una masa que pasa de `v₀ = 0` a una velocidad final en un tiempo muy corto — pero ejecutado con todo el cuerpo como motor, no con una mano sola.

## Bonus: ¿y si en vez de desplazarlo horizontal lo levanto?

Toda la cuenta de arriba fue horizontal (sin pelear contra la gravedad). Si en cambio *levantás* 1 kg, 1 metro, contra la gravedad, cuasi-estáticamente (sin acelerarlo, solo sosteniéndolo contra `w = m·g`), el trabajo que hacés es:

```
   W = w · h = m · g · h = 1 kg · 9.80665 m/s² · 1 m ≈ 9.81 J
```

Casi 10 joules — cinco veces más que los 2 J de empujarlo horizontal. Esto es energía potencial gravitatoria (*Gravitational Potential Energy*, cap. 7, todavía no cubierto en detalle) asomando la cabeza: contra la gravedad, "1 kg, 1 metro" cuesta mucho más que en el plano horizontal. Queda anotado como adelanto para cuando llegue el capítulo 7.
