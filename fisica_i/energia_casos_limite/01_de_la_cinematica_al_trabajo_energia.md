# De la cinemática al trabajo y la energía cinética

## Punto de partida: las dos ecuaciones que ya tenías

Todo lo que sigue sale de dos ecuaciones de movimiento rectilíneo uniformemente acelerado (cap. 2 del Sears), las mismas con las que arrancó toda la cursada:

$$
\begin{aligned}
(1)\quad v &= v_0 + a\,t \\
(2)\quad x &= x_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2
\end{aligned}
$$

$v_0$ es la *initial velocity*, $a$ es constante (aceleración constante — el caso que se trabaja en todo el capítulo 2). El objetivo: sacar el tiempo $t$ de la jugada, porque en la mayoría de los problemas de energía no importa *cuánto tardó* algo en pasar, importa *cuánto se desplazó* bajo qué fuerza.

## Paso 1 — despejar $t$ de (1)

$$
\begin{aligned}
v &= v_0 + a\,t \\
v - v_0 &= a\,t \\
t &= \frac{v - v_0}{a}
\end{aligned}
$$

## Paso 2 — sustituir en (2)

Tomando $x_0 = 0$ y llamando $\Delta x = x$ al desplazamiento:

$$
\Delta x = v_0\,\frac{v - v_0}{a} + \frac{1}{2}\,a\,\frac{(v - v_0)^2}{a^2}
$$

Sacando factor común $1/a$ y operando el numerador:

$$
\Delta x = \frac{2\,v_0\,(v - v_0) + (v - v_0)^2}{2\,a}
$$

El numerador es $(v - v_0)\,[2\,v_0 + (v - v_0)] = (v - v_0)\,(v + v_0) = v^2 - v_0^2$ (diferencia de cuadrados). Queda:

$$
\Delta x = \frac{v^2 - v_0^2}{2\,a} \implies v^2 = v_0^2 + 2\,a\,\Delta x
$$

Esta es la tercera ecuación clásica de cinemática — la que no tiene $t$ — tal como la presenta el libro; el camino de despejar y sustituir para llegar a ella (en vez de memorizarla directo) es el que fui practicando hasta encontrarle el gusto. Hasta acá, cero física nueva: es álgebra sobre lo que ya sabías del capítulo 2.

## Paso 3 — el salto: multiplicar por $m/2$

Acá es donde cinemática (que describe *cómo* se mueve algo) se convierte en dinámica de la energía (que describe *qué hace falta* para que se mueva así). Multiplicá los dos lados de $v^2 = v_0^2 + 2\,a\,\Delta x$ por $m/2$:

$$
\frac{m}{2}\,v^2 = \frac{m}{2}\,v_0^2 + m\,a\,\Delta x
$$

El lado izquierdo menos el primer término del derecho es, por definición, la diferencia de **energía cinética** (*Kinetic Energy*, $K = \tfrac{1}{2}\,m\,v^2$, en joules):

$$
\tfrac{1}{2}\,m\,v^2 - \tfrac{1}{2}\,m\,v_0^2 = m\,a\,\Delta x = (m\,a)\,\Delta x
$$

Y por la segunda ley de Newton (cap. 4), $m\,a = F$ — la fuerza neta que causó esa aceleración. $F\,\Delta x$, cuando $F$ es constante y apunta en la dirección del desplazamiento, es exactamente la definición de **trabajo** (*Work*, $W$). Entonces:

$$
\begin{aligned}
\Delta K &= W \\
\tfrac{1}{2}\,m\,v^2 - \tfrac{1}{2}\,m\,v_0^2 &= F\,\Delta x
\end{aligned}
$$

Este es el **teorema trabajo-energía** (*work-energy theorem*), cap. 6. No es un axioma nuevo que hay que memorizar por separado: es la ecuación de cinemática que ya usabas, mirada desde el ángulo de la fuerza y no del tiempo.

## Definiciones formales, ahora que ya se entiende de dónde salen

Todo lo anterior se hizo en una sola dimensión (cap. 2: movimiento sobre una recta), así que $F$ y $\Delta x$ eran escalares con signo — no hizo falta hablar de vectores porque en una recta solo hay dos direcciones posibles. Pero la definición real de trabajo (cap. 6, y cap. 1.10 para el producto de vectores) es vectorial, y vale la pena escribirla así desde el principio en vez de memorizar directamente la versión escalar:

$$
\begin{array}{lll}
\text{Work (vectorial)} & W = \vec F \cdot \Delta\vec r & [\text{J}] \\
\text{Kinetic Energy} & K = \tfrac{1}{2}\,m\,v^2 \quad (v = \lvert\vec v\rvert,\ \text{rapidez}) & [\text{J}] \\
\text{Work-Energy Th.} & W_{\text{net}} = \Delta K = K_f - K_i & [\text{J}] \\
\text{Power} & P = \vec F \cdot \vec v \quad (\text{instantánea}) & [\text{W}]
\end{array}
$$

El símbolo $\cdot$ entre dos vectores es el **producto escalar** (*dot product*, cap. 1.10): toma dos vectores y devuelve un número (sin dirección), definido como

$$
\begin{aligned}
\vec F \cdot \Delta\vec r &= \lvert\vec F\rvert\,\lvert\Delta\vec r\rvert\cos\theta && \text{(forma “por módulos y ángulo”)} \\
\vec F \cdot \Delta\vec r &= F_x\,\Delta x + F_y\,\Delta y + F_z\,\Delta z && \text{(forma “por componentes” — la que prefiero usar)}
\end{aligned}
$$

Las dos formas son la misma cosa. La ventaja de la forma por componentes es que $\cos\theta$ deja de ser un factor que hay que "traer de afuera" (y del que hay que acordarse el signo según el cuadrante) — sale solo, escondido dentro de $F_x$ y $\Delta x$ una vez que la fuerza y el desplazamiento están descompuestos en sus componentes $x$ / $y$ con el ángulo medido desde el eje $+x$. Por eso el trabajo "sabe" cancelarse cuando la fuerza es perpendicular al desplazamiento (por ejemplo, cargar una valija caminando horizontal mientras la sostenés hacia arriba: $F_x\,\Delta x$ con $F_x = 0$ porque toda la fuerza está en $y$) sin que haga falta memorizar la regla "si es perpendicular, da cero" aparte — es una consecuencia directa de la definición, no una excepción a recordar. Es una trampa clásica de examen justamente para quien memorizó la regla en vez de la definición.

Cuando llegue el capítulo 9 (rotación), el otro producto de vectores del cap. 1.10 — el **producto vectorial** (*cross product*, $\times$, que da como resultado otro vector, perpendicular al plano de los dos originales) — va a tener su lugar para torque y momento angular. Acá todavía no hace falta.

## Chequeo de unidades (porque recién te estás acostumbrando a N, J y W)

$$
\begin{aligned}
{[a]} &= \text{m/s}^2 && (\text{cap. 2}) \\
{[F]} &= \text{kg}\cdot\text{m/s}^2 = \text{N} && (\text{cap. 4},\ F = m\,a) \\
{[W]} &= \text{N}\cdot\text{m} = \text{kg}\cdot\text{m}^2/\text{s}^2 = \text{J} && (\text{cap. 6}) \\
{[P]} &= \text{J/s} = \text{kg}\cdot\text{m}^2/\text{s}^3 = \text{W} && (\text{cap. 6})
\end{aligned}
$$

Un vatio ($\text{W}$, la unidad — no confundir con $W$ de *Work*, el libro reutiliza la letra) es un joule por segundo. Si en algún cálculo te da un resultado en $\text{kg}\cdot\text{m}^2/\text{s}^3$ y no lo simplificaste a W, es una señal de que no cerraste unidades.

## Nota al margen: $\mu_s$ y $\mu_k$, para más adelante

El capítulo 5 introduce la fricción con dos coeficientes: $\mu_s$ (*static*, fricción estática — la que hay que vencer para que algo *empiece* a moverse) y $\mu_k$ (*kinetic*, fricción cinética — la que actúa mientras ya se está moviendo, típicamente algo menor que $\mu_s$). No entran todavía en esta carpeta porque los casos de `03` y `04` asumen que no hay fricción relevante en el aire (sí hay resistencia aerodinámica, que es otra cosa, no fricción de contacto) — pero van a ser necesarios el día que se quiera modelar, por ejemplo, la fricción del pie del atleta contra el suelo del círculo de bala, que es justamente lo que le permite empujar sin resbalar.

## Mapa de la derivación

$$
\begin{aligned}
\left.
\begin{aligned}
v &= v_0 + a\,t \\
x &= x_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2
\end{aligned}
\right\}
&\xrightarrow{\text{cap. 2}} v^2 = v_0^2 + 2\,a\,\Delta x \\
&\longrightarrow \tfrac{1}{2}\,m\,v^2 - \tfrac{1}{2}\,m\,v_0^2 = m\,a\,\Delta x \\
&\xrightarrow{F = m\,a\ (\text{cap. 4})} \Delta K = F\,\Delta x = W \quad (\text{cap. 6 — work-energy theorem})
\end{aligned}
$$
