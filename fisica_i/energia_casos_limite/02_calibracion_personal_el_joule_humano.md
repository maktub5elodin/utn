# Calibración personal: el joule humano

## La pregunta que no dejaba dormir

"Con mi mano puedo mover una masa de 1 kg, una distancia de 1 metro, en más o menos 1 segundo. ¿Eso significa que puedo generar 1 joule? ¿1 watt, si lo hago justo en 1 segundo?"

Es una buena pregunta porque es *calculable* con exactamente las herramientas de `01`: cinemática de aceleración constante + $F = m\,a$ + $K = \tfrac{1}{2}\,m\,v^2$. Nada de esto necesita el capítulo 7 ni el 8. Vamos al número.

## El cálculo, paso a paso

Supuestos del experimento: $m = 1\ \text{kg}$, arranca desde $v_0 = 0$, recorre $\Delta x = 1\ \text{m}$ en $t = 1\ \text{s}$, con aceleración constante (la mano empuja parejo, no de un tirón).

**Aceleración necesaria**, de $\Delta x = \tfrac{1}{2}\,a\,t^2$:

$$
1 = \tfrac{1}{2} \cdot a \cdot 1^2 \implies a = 2\ \text{m/s}^2
$$

**Fuerza necesaria** (cap. 4, $F = m\,a$):

$$
F = 1\ \text{kg} \cdot 2\ \text{m/s}^2 = 2\ \text{N}
$$

Dos newtons es *poco* — el peso de una manzana chica ($w = m\,g \approx 0{,}2\ \text{kg} \cdot 9{,}8 \approx 2\ \text{N}$). Empujar 1 kg, 1 metro, en 1 segundo, no exige casi nada de fuerza.

**Velocidad final** ($v = v_0 + a\,t$):

$$
v = 0 + 2 \cdot 1 = 2\ \text{m/s}
$$

**Energía cinética entregada** ($K = \tfrac{1}{2}\,m\,v^2$, y como arrancó del reposo, $\Delta K = K$, y por el teorema trabajo-energía $\Delta K = W$, el trabajo que hizo tu mano):

$$
K = \tfrac{1}{2} \cdot 1 \cdot 2^2 = 2\ \text{J}
$$

**No es 1 joule — son 2.** La intuición estaba en el orden de magnitud correcto, pero no exacta: para que la masa *recorra* 1 metro en 1 segundo arrancando del reposo con aceleración constante, tiene que salir con el doble de velocidad promedio de lo que uno imagina a ojo (la velocidad promedio es 1 m/s, y en efecto arranca en 0 y termina en 2 m/s, promedio $(0 + 2)/2 = 1$, eso cierra — lo que falla la intuición es que la energía depende de $v^2$, no de la velocidad promedio).

**Potencia promedio:**

$$
P = W / t = 2\ \text{J} / 1\ \text{s} = 2\ \text{W}
$$

**Potencia instantánea en el instante de soltar** ($P = F\,v$, con la velocidad final):

$$
P = 2\ \text{N} \cdot 2\ \text{m/s} = 4\ \text{W}
$$

El pico instantáneo (4 W) es el doble del promedio (2 W) — tiene sentido, porque la potencia crece linealmente de 0 a 4 W a lo largo del segundo (fuerza constante, velocidad creciente), y el promedio de una rampa lineal es la mitad del pico. Esto va a importar en `05`, porque las cifras de potencia "de récord" que vas a encontrar en biomecánica casi siempre son picos instantáneos, no promedios — hay que tener cuidado de no comparar peras con manzanas.

## Y si aprieto los tiempos, ¿qué pasa?

Repitiendo la misma cuenta ($m = 1\ \text{kg}$, $\Delta x = 1\ \text{m}$) pero variando cuánto tarda:

$$
\begin{array}{lll}
a = 2/t^2\ (\text{m/s}^2) & F = 2/t^2\ (\text{N, porque } m = 1) & v = 2/t\ (\text{m/s}) \\
K = 2/t^2\ (\text{J}) & P = K/t = 2/t^3\ (\text{W}) &
\end{array}
$$

| $t$ (s) | $a$ (m/s²) | $F$ (N) | $v$ (m/s) | $K$ (J) | $P$ promedio (W) |
|---|---|---|---|---|---|
| 1,00 | 2 | 2 | 2 | 2 | 2 |
| 0,50 | 8 | 8 | 4 | 8 | 16 |
| 0,20 | 50 | 50 | 10 | 50 | 250 |
| 0,10 | 200 | 200 | 20 | 200 | 2 000 |
| 0,05 | 800 | 800 | 40 | 800 | 16 000 |

La potencia escala con $1/t^3$ — achicar el tiempo a la mitad multiplica la potencia por 8, no por 2. Esto es la matemática detrás de por qué los deportes explosivos (lanzamientos, saltos, la salida de una carrera) generan potencias brutales con fuerzas que, aisladas, no sorprenden tanto:

- **t = 0,1 s** ($F = 200\ \text{N}$, $P = 2\,000\ \text{W}$): 200 N son ~20 kgf — una fuerza fuerte pero perfectamente humana para un empujón corto (una trompada, un golpe de tenis). La potencia resultante, 2 000 W, ya está en el orden de magnitud del pico de Usain Bolt saliendo de los tacos (ver `05`).
- **t = 0,05 s** ($F = 800\ \text{N}$, $P = 16\,000\ \text{W}$): 800 N (~82 kgf) generados por *un solo brazo* en 0,05 s ya no es realista — fuerzas de ese orden aparecen en biomecánica humana, pero como resultado de todo el cuerpo (piernas + tronco) actuando en cadena, no de un brazo empujando un objeto de 1 kg. Es la señal de que el modelo "una mano empuja una masa chica" dejó de alcanzar y hay que pasar a otro objeto de estudio.

Ese último punto es exactamente la bisagra hacia `03` y `04`: el lanzamiento de bala y de jabalina son, físicamente, el mismo experimento de esta hoja — una masa que pasa de $v_0 = 0$ a una velocidad final en un tiempo muy corto — pero ejecutado con todo el cuerpo como motor, no con una mano sola.

## Bonus: ¿y si en vez de desplazarlo horizontal lo levanto?

Toda la cuenta de arriba fue horizontal (sin pelear contra la gravedad). Si en cambio *levantás* 1 kg, 1 metro, contra la gravedad, cuasi-estáticamente (sin acelerarlo, solo sosteniéndolo contra $w = m\,g$), el trabajo que hacés es:

$$
W = w\,h = m\,g\,h = 1\ \text{kg} \cdot 9{,}80665\ \text{m/s}^2 \cdot 1\ \text{m} \approx 9{,}81\ \text{J}
$$

Casi 10 joules — cinco veces más que los 2 J de empujarlo horizontal. Esto es energía potencial gravitatoria (*Gravitational Potential Energy*, cap. 7, todavía no cubierto en detalle) asomando la cabeza: contra la gravedad, "1 kg, 1 metro" cuesta mucho más que en el plano horizontal. Queda anotado como adelanto para cuando llegue el capítulo 7.
