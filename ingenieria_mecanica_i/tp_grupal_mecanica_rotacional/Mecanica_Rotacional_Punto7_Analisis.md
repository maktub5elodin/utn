# Punto 7 — Cantidad de movimiento angular respecto de la base: análisis comparativo

Análisis del Punto 7 del ejercicio de aplicación (tren de engranajes, apunte de Mecánica Rotacional del Ing. Abud, págs. 14-15). Compara la resolución preparada en `Mecanica_Rotacional_Apuntes.md` con la que propuso un compañero del grupo (`Ej 7.pdf`, págs. 8-9, local). El objetivo es entender por qué las dos parten del mismo principio y aun así llegan a respuestas distintas, y cuál es la respuesta correcta a una consigna que el enunciado deja poco explicada.

---

## Índice

1. [La consigna](#1-la-consigna)
2. [Datos que se usan (de los Puntos 1 a 5)](#2-datos-que-se-usan-de-los-puntos-1-a-5)
3. [El principio común a las dos resoluciones](#3-el-principio-común-a-las-dos-resoluciones)
4. [Nuestra resolución](#4-nuestra-resolución)
5. [La resolución del compañero](#5-la-resolución-del-compañero)
6. [Análisis: dónde se separan las dos resoluciones](#6-análisis-dónde-se-separan-las-dos-resoluciones)
7. [Qué pide realmente la consigna](#7-qué-pide-realmente-la-consigna)
8. [Respuesta final](#8-respuesta-final)
9. [Tabla comparativa](#9-tabla-comparativa)
10. [Errores comunes](#10-errores-comunes)
11. [Mapa conceptual](#11-mapa-conceptual)

---

## 1. La consigna

> 7) ¿Qué sucedería con la cantidad de movimiento angular del mecanismo respecto de un sistema de referencia ubicado en la base de la máquina anclada al piso? ¿Cuánto es su valor?

El enunciado da la altura del eje 1 sobre la base ($H_1 = 1500$ mm) y marca $H_2$ en el esquema **sin valor**. No dice nada más: ni qué significa "qué sucedería", ni si hay que considerar algún movimiento de la base.

La pregunta tiene dos partes:

- **Cualitativa** ("qué sucedería"): cómo cambia $L$ al pasar de medirlo sobre los propios ejes a medirlo desde un punto de la base.
- **Cuantitativa** ("cuánto es su valor"): un número, en kg·m²/s.

---

## 2. Datos que se usan (de los Puntos 1 a 5)

Cada **conjunto rotante** (rotor) es eje + engranaje + 2 rodamientos, y gira sobre su propio eje.

| Rotor | $\omega$ (rad/s) | $I$ propio (kg·mm²) | $L = I\,\omega$ (kg·m²/s) | Masa total $M$ (kg) |
|---|---|---|---|---|
| 1 | $293{,}2$ | $31.349$ | $9{,}19$ | $1{,}156 + 3{,}948 + 2\cdot0{,}128 \approx 5{,}36$ |
| 2 | $366{,}5$ | $13.558$ | $4{,}97$ | $2{,}266 + 2{,}474 + 2\cdot0{,}288 \approx 5{,}32$ |

**Unidades:** igual que en los apuntes, $I$ se expresa en **kg·mm²** y $L$ en **kg·m²/s** (SI). Para pasar de una a otra se usa $1 \text{ kg}\cdot\text{mm}^2 = 10^{-6} \text{ kg}\cdot\text{m}^2$, así que, con $I$ en kg·mm² y $\omega$ en rad/s:

$$L = I\,\omega\cdot10^{-6} \qquad\Rightarrow\qquad L_1 = 31.349 \cdot 293{,}2 \cdot 10^{-6} \approx 9{,}19 \text{ kg}\cdot\text{m}^2/\text{s}$$

Los engranajes están engranados por el exterior, así que **giran en sentidos opuestos**.

```
        vista según los ejes (ejes perpendiculares al papel)

             rotor 1                 rotor 2
          ┌─────────┐            ┌───────┐
          │    ↺    │◄── 225 ──► │   ↻   │      ↺ = sentido +  (L₁ saliente)
          │  (O₁)   │    mm      │  (O₂) │      ↻ = sentido −  (L₂ entrante)
          └─────────┘            └───────┘
               │                     │
               │ H₁ = 1500 mm        │ H₂ = ?  (sin valor en el enunciado)
               │                     │
   ════════════╧═════════════════════╧════════════  base anclada al piso
                          O  (origen del sistema de referencia)
```

---

## 3. El principio común a las dos resoluciones

Las dos resoluciones arrancan de la misma ecuación, que es correcta. La cantidad de movimiento angular de un cuerpo respecto de un origen $O$ se descompone en dos términos:

$$\vec{L}_O = \vec{L}_{cm} + \vec{r}_{cm} \times \vec{P}_{cm}$$

| Término | Nombre | Qué mide |
|---|---|---|
| $\vec{L}_{cm}$ | giro propio (*spin*) | el cuerpo girando alrededor de su propio centro de masa |
| $\vec{r}_{cm} \times \vec{P}_{cm}$ | término orbital | el centro de masa moviéndose respecto de $O$ ($\vec{P}_{cm} = M\,\vec{v}_{cm}$) |

**Qué es cada símbolo.** Sí: el subíndice $cm$ significa **centro de masa**, en todos los casos.

| Símbolo | Nombre | Qué es | Unidad |
|---|---|---|---|
| $\vec{L}_{cm}$ | momento angular respecto del centro de masa | la cantidad de movimiento angular del cuerpo medida desde su propio centro de masa: solo "ve" el giro del cuerpo sobre sí mismo | kg·m²/s |
| $\vec{r}_{cm}$ | vector posición del centro de masa | la flecha que va **desde el origen $O$** del sistema de referencia **hasta el centro de masa** del cuerpo. Dice *dónde está* el centro de masa visto desde $O$ | m |
| $\vec{v}_{cm}$ | velocidad del centro de masa | la rapidez y dirección con que **se traslada** el centro de masa. No es la velocidad de los puntos del cuerpo que giran, sino la del "punto promedio" de toda la masa | m/s |
| $M$ | masa total del cuerpo | toda la masa del rotor (eje + engranaje + rodamientos) | kg |
| $\vec{P}_{cm} = M\,\vec{v}_{cm}$ | cantidad de movimiento lineal | la cantidad de movimiento de **traslación** del cuerpo completo, como si toda su masa estuviera concentrada en el centro de masa | kg·m/s |
| $\times$ | producto vectorial | da un vector perpendicular a $\vec{r}_{cm}$ y a $\vec{P}_{cm}$, de módulo $r_{cm}\,P_{cm}\sin\theta$ (con los módulos de cada vector; regla de la mano derecha) | — |

**Cómo leer el término orbital.** $\vec{r}_{cm} \times \vec{P}_{cm}$ es exactamente el $\vec{L} = \vec{r} \times \vec{p}$ de una **partícula puntual**, aplicado a una partícula imaginaria de masa $M$ ubicada en el centro de masa. La descomposición de arriba separa el movimiento de cualquier cuerpo en dos partes independientes:

```
   movimiento del cuerpo  =  traslación del CM          +  giro alrededor del CM
                             (como una partícula de       (el cuerpo girando
                              masa M en r_cm, con v_cm)    sobre sí mismo)
                                       │                             │
   L_O                    =     r_cm × P_cm               +        L_cm
```

**En el TP.** Para el rotor 1, con el origen $O$ en la base justo debajo del eje:

- $\vec{r}_{cm}$ va desde $O$ hasta el centro de masa del rotor 1, que está sobre su eje: es un vector de módulo $H_1 = 1500$ mm, vertical. Para el rotor 2 va hasta el eje 2, y su módulo depende de $H_2$ y de la separación horizontal.
- $\vec{v}_{cm} = 0$: los puntos del engranaje se mueven (el borde a $36{,}65$ m/s), pero el centro de masa, sobre el eje, está quieto. Por eso $\vec{P}_{cm} = M\cdot\vec{0} = \vec{0}$.
- En componentes, con $\vec{r}_{cm} = (0,\ H_1,\ 0)$ y $\vec{P}_{cm} = (0,\ 0,\ 0)$:

$$\vec{r}_{cm} \times \vec{P}_{cm} = (0,\ 0,\ 0)$$

Un $\vec{r}_{cm}$ grande no alcanza para que el término exista: con $\vec{P}_{cm}$ nulo, el producto vale cero.

Para un sistema de varios cuerpos, se suma lo de cada uno:

$$\vec{L}_{total} = \sum \left( \vec{L}_{cm} + \vec{r}_{cm} \times \vec{P}_{cm} \right)$$

Todo el Punto 7 se juega en **cuánto vale el término orbital**.

---

## 4. Nuestra resolución

**Giro propio.** Cada rotor es simétrico respecto de su eje y gira alrededor de ese eje, que pasa por su centro de masa. Entonces $L_{cm} = I\,\omega$, dirigido según el eje: son los $L_1$ y $L_2$ de los Puntos 4 y 5.

**Término orbital.** El centro de masa de cada rotor está sobre su eje. Los ejes están fijos a la máquina, y la máquina está anclada al piso. El centro de masa no se mueve:

$$\vec{v}_{cm} = 0 \quad\Rightarrow\quad \vec{P}_{cm} = M\,\vec{v}_{cm} = 0 \quad\Rightarrow\quad \vec{r}_{cm} \times \vec{P}_{cm} = 0$$

No importa cuánto valga $\vec{r}_{cm}$ (o sea $H_1$, $H_2$ o la separación horizontal): multiplica a cero.

**Suma con signos.** Los rotores giran en sentidos opuestos, así que $\vec{L}_1$ y $\vec{L}_2$ son antiparalelos. Tomando como positivo el sentido del eje 1:

$$L_{total} = L_1 - L_2 = 9{,}19 - 4{,}97 \approx 4{,}22 \text{ kg}\cdot\text{m}^2/\text{s}$$

**Conclusión:** $L$ respecto de la base es el mismo que respecto de los ejes. $H_1$ y $H_2$ no intervienen, y por eso no hace falta el valor de $H_2$.

---

## 5. La resolución del compañero

Transcripción de su desarrollo (`Ej 7.pdf`, págs. 8-9). Él trabajó en metros y kg·m²; acá sus momentos de inercia se pasan a **kg·mm²** (y sus distancias a mm) para compararlos directamente con los nuestros. Los valores numéricos son los suyos, solo cambia la unidad.

1. Plantea el principio general: $\vec{L}_{total} = \sum \left( \vec{L}_{cm} + \vec{r}_{cm} \times \vec{P}_{cm} \right)$.
2. Lo aplica al sistema: $L_{total} = L_1 - L_2 + L_H$, con $L_H = \vec{r}_{cm} \times \vec{P}_{cm}$.
3. Argumenta que, al cambiar de sistema de referencia, hay que calcular un nuevo momento de inercia con Steiner, $I = I_{cm} + M H^2$, y lo aplica a cada rotor:

$$I_{H1} = 31.340 + 5{,}356\cdot(1500)^2 \approx 12.082.000 \text{ kg}\cdot\text{mm}^2$$

$$I_{H2} = 13.600 + 5{,}326\cdot(1275)^2 \approx 8.670.000 \text{ kg}\cdot\text{mm}^2$$

4. Escribe el término orbital con una "velocidad angular genérica" $\omega_H$ (con $I$ en kg·mm², y pasado a SI con el factor $10^{-6}$):

$$L_H = (12.082.000 + 8.670.000)\,\omega_H = 20.752.000\,\omega_H \;[\text{kg}\cdot\text{mm}^2] \quad\Rightarrow\quad L_H = 20{,}752\,\omega_H \text{ kg}\cdot\text{m}^2/\text{s}$$

5. Resultado (él lo expresa en J·s, que es la misma unidad):

$$L_{total} = 20{,}752\,\omega_H + 4{,}21 \text{ kg}\cdot\text{m}^2/\text{s}$$

**Lo que está bien:**

- El principio de partida (paso 1) y su forma para este sistema (paso 2), **incluido el signo** $L_1 - L_2$.
- Las cuentas numéricas: $31.340 + 5{,}356\cdot2.250.000 \approx 12.082.000$ y $13.600 + 5{,}326\cdot1.625.625 \approx 8.670.000$ kg·mm².
- El valor de $L_1 - L_2 = 4{,}21$ kg·m²/s, que coincide con nuestro $4{,}22$ salvo redondeo. Él usó $I_1 = 31.340$ e $I_2 = 13.600$ kg·mm², lo que da $9{,}190 - 4{,}985 = 4{,}205 \approx 4{,}21$; con $I_2 = 13.558$ kg·mm² sale $4{,}22$.
- Las masas de cada rotor: $5{,}356$ y $5{,}326$ kg, contra nuestras $5{,}360$ y $5{,}316$, con una diferencia menor al 0,2 %.

**Supuesto propio:** $H_2 = 1275 \text{ mm} = 1500 - 225$, o sea que ubica el eje 2 exactamente 225 mm debajo del eje 1. El enunciado no da ese dato.

**Orden de magnitud:** su $I_{H1}$ es unas **385 veces** el $I$ propio del rotor 1 ($12.082.000$ contra $31.349$ kg·mm²). Casi todo es el término $M H^2$: con $H = 1500$ mm, la distancia al cuadrado domina por completo, igual que en el ejemplo del rodamiento corrido de la sección 3.5 de los apuntes.

---

## 6. Análisis: dónde se separan las dos resoluciones

Hasta el paso 2 las dos resoluciones son idénticas. La diferencia está en el paso 3, en **cómo se evalúa $L_H = \vec{r}_{cm} \times \vec{P}_{cm}$**.

### 6.1 El término orbital es cero, y su propia fórmula lo dice

$L_H$ está definido como $\vec{r}_{cm} \times \vec{P}_{cm}$. En vez de evaluar $\vec{P}_{cm}$, el paso 3 lo reemplaza por un cálculo con Steiner. Si se lo evalúa directamente, con $\vec{v}_{cm} = 0$ porque los ejes no se mueven:

$$\vec{P}_{cm} = M\,\vec{v}_{cm} = 0 \quad\Rightarrow\quad L_H = 0$$

Su planteo ya tenía la respuesta correcta en el paso 2: faltaba ver que $\vec{P}_{cm}$ es cero.

### 6.2 Qué calcula realmente Steiner

$L = I_O\,\omega$ con $I_O = I_{cm} + M H^2$ vale para un cuerpo que **gira como un todo alrededor del eje que pasa por $O$**. El ejemplo típico es una piedra atada a una cuerda que gira alrededor de la mano. En ese caso el centro de masa describe una circunferencia de radio $H$ con velocidad $v_{cm} = \omega H$, y:

$$I_O\,\omega = \underbrace{I_{cm}\,\omega}_{\text{giro propio}} + \underbrace{M H^2\,\omega}_{\text{órbita del CM}} \qquad\text{con}\qquad r_{cm}\,P_{cm} = H \cdot M(\omega H) = M H^2\,\omega$$

Es decir, Steiner es la misma descomposición de la sección 3 ($\vec{L}_{cm} + \vec{r}_{cm} \times \vec{P}_{cm}$), escrita para el caso particular de un cuerpo rígido que orbita alrededor de $O$. El término $M H^2$ **representa** el movimiento orbital del centro de masa: si no hay órbita, no hay término.

```
   CUERPO QUE ORBITA (Steiner aplica)        ROTOR DEL TP (Steiner no aplica)

          ↺ ω                                        ↺ ω
        ●─────── H ───────○ O                    ●  gira sobre su propio eje
      el CM recorre un círculo                   │  el CM no se mueve
      v_cm = ω·H ≠ 0                             │  v_cm = 0
                                                 │ H
                                          ═══════○═══════ base
   L_O = I_cm·ω + M·H²·ω                   L_O = I_cm·ω + 0
```

Los rotores del TP están en el caso de la derecha: el centro de masa está quieto sobre el eje, que está fijo a la base.

### 6.3 Qué es $\omega_H$

La resolución deja $\omega_H$ como "velocidad angular genérica", y eso es lo que delata el problema: para ponerle un número habría que responder **a qué velocidad angular giran los centros de masa alrededor de la base**. Con la máquina anclada al piso, la respuesta es cero. Con $\omega_H = 0$ su resultado queda en:

$$L_{total} = 0 + 4{,}21 = 4{,}21 \text{ kg}\cdot\text{m}^2/\text{s}$$

que es el nuestro.

### 6.4 Aun con $\omega_H \neq 0$ habría dos problemas más

Supongamos que la máquina sí orbitara, por ejemplo montada sobre una plataforma giratoria. Aun así, $L_H = (I_{H1} + I_{H2})\,\omega_H$ tendría dos problemas:

1. **Cuenta dos veces el giro propio.** $I_H = I_{cm} + M H^2$ ya incluye $I_{cm}$. Como $L_1 - L_2$ ya aporta $I_{cm}\,\omega$, el término orbital debería ser solo $M H^2\,\omega_H$, sin volver a sumar $I_{cm}$.
2. **Suma $I$ referidos a ejes distintos.** Sumar $I_{H1} + I_{H2}$ y multiplicar por una sola $\omega$ supone que los dos rotores forman un único cuerpo que gira con una sola velocidad. Pero su giro propio es con $\omega$ distintas y en sentidos opuestos. Es el mismo error que se señala en los Puntos 4/5 de los apuntes: no se suman momentos de inercia referidos a ejes distintos.

### 6.5 No responde "¿cuánto es su valor?"

Una expresión con $\omega_H$ libre no es un valor. La consigna pide un número.

---

## 7. Qué pide realmente la consigna

La pregunta "¿qué sucedería respecto de un sistema en la base?" invita a pensar que el cambio de origen exige un cálculo nuevo, y de ahí la tentación de usar Steiner con la altura. La respuesta de fondo es un teorema general.

**Cambio de origen del momento angular.** Para dos orígenes $O$ y $O'$ cualesquiera:

$$\vec{L}_O = \vec{L}_{O'} + \left(\vec{r}_{O'} - \vec{r}_O\right) \times \vec{P}_{total}$$

donde $\vec{P}_{total}$ es la cantidad de movimiento lineal de **todo** el sistema.

- Si $\vec{P}_{total} \neq 0$, $L$ depende del origen elegido.
- Si $\vec{P}_{total} = 0$, **$L$ vale lo mismo respecto de cualquier punto**.

En el mecanismo, ningún centro de masa se mueve, así que $\vec{P}_{total} = 0$. Entonces:

1. **Qué sucede:** nada. Pasar el origen de los ejes a la base no cambia $L$. Que el enunciado no dé $H_2$ es coherente con esto: no hace falta porque no interviene.
2. **Cuánto vale:** lo mismo que respecto de los ejes, $L_1 - L_2$.

**Qué más se puede decir de "qué sucede":**

- **Es constante en el tiempo.** La fuerza de 200 N entre engranajes es un par acción-reacción interno: no aporta momento externo neto. Las reacciones en los rodamientos solo dan momentos perpendiculares a los ejes.
- **Se conserva también en el cambio del Punto 6.** Con $I' = I/2$ y $\omega' = 2\,\omega$, en cada rotor $I'\,\omega' = I\,\omega$.
- **Lectura física del "anclada al piso":** para llevar el mecanismo de $L = 0$ (detenido) a $4{,}22$ kg·m²/s, el motor aplica un par, y la reacción opuesta la recibe la carcasa y, a través de los anclajes, el piso. Por eso la base tiene que estar anclada: absorbe el momento angular de reacción en el arranque y en el frenado. Esto no cambia el valor pedido, pero le da sentido a mencionar la base en la consigna.

---

## 8. Respuesta final

> Respecto de un sistema de referencia en la base, la cantidad de movimiento angular del mecanismo **es la misma que respecto de los propios ejes**, porque los centros de masa de los rotores no se mueven ($\vec{P}_{total} = 0$) y el término orbital $\vec{r}_{cm} \times \vec{P}_{cm}$ se anula para cualquier origen. Las alturas $H_1$ y $H_2$ no intervienen.
>
> Como los rotores giran en sentidos opuestos:
>
> $$L_{total} = L_1 - L_2 \approx 9{,}19 - 4{,}97 \approx 4{,}22 \text{ kg}\cdot\text{m}^2/\text{s}$$
>
> dirigido según los ejes, con el sentido de giro del eje 1. Es **constante** (no hay momento externo según los ejes) y se conserva también en la reducción de $I$ del Punto 6.

---

## 9. Tabla comparativa

| Aspecto | Resolución del compañero | Nuestra resolución |
|---|---|---|
| Principio de partida | $\sum(\vec{L}_{cm} + \vec{r}_{cm} \times \vec{P}_{cm})$ ✓ | El mismo ✓ |
| Giro propio | $L_1 - L_2$, con signo ✓ | $L_1 - L_2$, con signo ✓ |
| Término orbital $\vec{r}_{cm} \times \vec{P}_{cm}$ | Reemplazado por Steiner con $H$: $20{,}752\,\omega_H$ kg·m²/s (de $I_{H1} + I_{H2} = 20.752.000$ kg·mm²) ✗ | $\vec{v}_{cm} = 0 \Rightarrow 0$ ✓ |
| Uso de Steiner | Aplicado, suponiendo un giro alrededor de la base ✗ | No aplica: no hay órbita ✓ |
| $H_2$ | Supuesto: $1{,}275$ m | No hace falta |
| $\omega_H$ | Genérica, sin valor | No existe (sería 0) |
| Resultado | $20{,}752\,\omega_H + 4{,}21$ kg·m²/s (indeterminado) | **≈ 4,22 kg·m²/s** |
| Con $\omega_H = 0$ | $4{,}21$ kg·m²/s | Coincide (diferencia de redondeo) |

---

## 10. Errores comunes

| Error | Por qué está mal | Lo correcto |
|---|---|---|
| Aplicar Steiner con la altura $H$ para "cambiar de sistema de referencia" | Steiner representa la órbita del CM alrededor del nuevo eje; acá el CM no se mueve | $L_O = L_{cm}$ cuando $v_{cm} = 0$ |
| Dejar una $\omega$ "genérica" en el resultado | La consigna pide un valor; la única velocidad orbital posible es 0 | Evaluar $P_{cm} = M\,v_{cm}$ |
| Sumar $I_H$ a $L_1 - L_2$ | $I_H$ ya contiene $I_{cm}$: el giro propio se cuenta dos veces | Término orbital solo $M H^2\,\omega_{orbital}$ |
| Sumar $I_1 + I_2$ (o $I_{H1} + I_{H2}$) y multiplicar por una sola $\omega$ | Son rotores distintos, con $\omega$ y sentidos distintos, referidos a ejes distintos | Se combinan los $L$, no los $I$ |
| $L_{total} = L_1 + L_2 \approx 14{,}16$ | Los engranajes giran en sentidos opuestos | $L_{total} = L_1 - L_2 \approx 4{,}22$ |
| Pensar que falta un dato porque no se da $H_2$ | Con $P_{total} = 0$, $L$ no depende del origen | $H_2$ no interviene |

---

## 11. Mapa conceptual

```
                         L respecto de la base  (Punto 7)
                                     │
                    L_O = Σ ( L_cm  +  r_cm × P_cm )
                                │            │
               ┌────────────────┘            └────────────────┐
               ▼                                              ▼
        GIRO PROPIO                                   TÉRMINO ORBITAL
        L_cm = I·ω por rotor                          P_cm = M·v_cm
               │                                              │
     sentidos opuestos (engrane externo)            ejes fijos, máquina anclada
               │                                              │
        L₁ − L₂ ≈ 9,19 − 4,97                         v_cm = 0 ⇒ término = 0
               │                                              │
               │                          ┌───────────────────┤
               │                          ▼                   ▼
               │            Steiner (I_cm + M·H²)      P_total = 0 ⇒ L no depende
               │            solo si el CM orbita:      del origen: H₁, H₂ no entran
               │            NO es este caso
               │                                              │
               └──────────────────────┬───────────────────────┘
                                      ▼
                        L_total ≈ 4,22 kg·m²/s
                  constante · según los ejes · sentido del eje 1
                     se conserva también en el Punto 6
```

---

*Fuentes: "UTN – FRBA – Apunte Teórico – Mecánica Rotacional", Ing. Abud (Ing. Mecánica I), ejercicio de aplicación págs. 14-15; `Mecanica_Rotacional_Apuntes.md` (Puntos 1 a 7 y sección 3.5, Teorema de Steiner); `Ej 7.pdf` (resolución del Punto 7 de un compañero del grupo, págs. 8-9, local, no versionado).*
