# Mecánica Rotacional — Ing. Mecánica I

**UTN – FRBA | Ciclo 2018**
Docente: Ing. Abud, Moisés Rolando
Ayudantes T.P.: Ing. Costucica, Leonardo — Ing. Gallo, Federico

---

## Índice

1. [Rotación de una partícula](#1-rotación-de-una-partícula)
2. [Cantidad de movimiento angular](#2-cantidad-de-movimiento-angular)
3. [Energía cinética de rotación y momento de inercia](#3-energía-cinética-de-rotación-y-momento-de-inercia)
4. [Tabla de momentos de inercia de cuerpos rígidos comunes](#4-tabla-de-momentos-de-inercia-de-cuerpos-rígidos-comunes)
5. [Trabajo y potencia de rotación](#5-trabajo-y-potencia-de-rotación)
6. [Ecuación fundamental de la dinámica rotacional](#6-ecuación-fundamental-de-la-dinámica-rotacional)
7. [Conservación de la cantidad de movimiento angular](#7-conservación-de-la-cantidad-de-movimiento-angular)
8. [Movimiento combinado: rotación y traslación (rodadura)](#8-movimiento-combinado-rotación-y-traslación-rodadura)
9. [Dinámica de ejes no fijos: movimiento de precesión](#9-dinámica-de-ejes-no-fijos-movimiento-de-precesión)
10. [Cantidad de movimiento angular y velocidad angular (L y ω no paralelos)](#10-cantidad-de-movimiento-angular-y-velocidad-angular-l-y-ω-no-paralelos)
11. [Ejercicio de aplicación (págs. 14-15): tren de engranajes](#11-ejercicio-de-aplicación-págs-14-15-tren-de-engranajes)

---

## 1. Rotación de una partícula

**Momento de rotación (torque):**

$$\vec{T} = \vec{r} \times \vec{F} \qquad |T| = r \cdot F \cdot \sin\theta$$

Donde θ es el ángulo entre el vector posición **r** y la fuerza **F** aplicada.

---

## 2. Cantidad de movimiento angular

### 2.1 De una partícula

$$\vec{P} = m\vec{v} \qquad \vec{L} = \vec{r} \times \vec{P}$$

- **P**: cantidad de movimiento lineal
- **L**: cantidad de movimiento angular, que puede originarse por dos causas:
  - Momentos de rotación ejercidos por fuerzas **internas** del sistema
  - Momentos de rotación ejercidos por fuerzas **externas**

### 2.2 De un sistema de partículas

$$\vec{P}_S = \sum m_C \cdot \vec{v}_C \quad \Rightarrow \quad \vec{L} = \vec{r} \times \vec{P}_S \quad \Leftrightarrow \quad \vec{L} = \sum_{i=1}^{n} \vec{L}_i$$

**Ecuaciones fundamentales del sistema:**

$$T_{ext} = \frac{dL}{dt} \qquad \text{(suma de todos los momentos de rotación externos)}$$

$$F_{ext} = \frac{dP}{dt} \qquad \text{(fuerza externa resultante sobre el sistema, rígido o no)}$$

---

## 3. Energía cinética de rotación y momento de inercia

Las ecuaciones que siguen son válidas no solo para un marco de referencia inercial, sino también si:

- El eje pasa por el centro de masa, **y**
- El eje móvil mantiene siempre la misma dirección en el espacio

### 3.1 Momento de inercia de un cuerpo rígido

$$I = \sum m\, r_C^2 \quad [\text{Kg}\cdot\text{m}^2]$$

- Es función del eje con respecto al cual se está rotando
- Es función de cómo está distribuida la masa respecto al eje de rotación

### 3.2 Energía cinética de rotación

$$k = \frac{1}{2} I \omega^2$$

### 3.3 Energía cinética de traslación (para comparar)

$$K = \frac{1}{2} m v^2$$

> El momento de inercia es a la rotación lo que la masa es a la traslación: una medida de la **resistencia a cambiar** el estado de movimiento (rotacional o lineal, respectivamente).

### 3.4 Momento de inercia de un sistema de masas infinitesimales

$$I = \int_0^m r^2 \, dm$$

### 3.5 Teorema de Steiner (ejes paralelos)

$$I = I_m + M h^2$$

Donde *h* es la distancia entre el eje considerado y el eje paralelo que pasa por el centro de masa.

---

## 4. Tabla de momentos de inercia de cuerpos rígidos comunes

*(Referencia gráfica adjunta en el apunte — resumen de fórmulas usuales)*

| Cuerpo | Eje | Fórmula |
|---|---|---|
| Aro (anillo delgado) | Eje del cilindro | $I = MR^2$ |
| Cilindro anular (anillo grueso) | Eje del cilindro | $I = \dfrac{M}{2}(R_1^2 + R_2^2)$ |
| Cilindro sólido (disco) | Eje del cilindro | $I = \dfrac{MR^2}{2}$ |
| Cilindro sólido (disco) | Diámetro central | $I = \dfrac{MR^2}{4} + \dfrac{Ml^2}{12}$ |
| Varilla delgada | Eje perpendicular por el centro | $I = \dfrac{Ml^2}{12}$ |
| Varilla delgada | Eje perpendicular por un extremo | $I = \dfrac{Ml^2}{3}$ |
| Esfera sólida | Diámetro cualquiera | $I = \dfrac{2MR^2}{5}$ |
| Cascarón esférico delgado | Diámetro cualquiera | $I = \dfrac{2MR^2}{3}$ |
| Aro | Diámetro cualquiera | $I = \dfrac{MR^2}{2}$ |
| Aro | Línea tangente cualquiera | $I = \dfrac{3MR^2}{2}$ |

*(M = masa total, R = radio, l = longitud, R₁/R₂ = radios interior/exterior)*

---

## 5. Trabajo y potencia de rotación

Solo las componentes de la fuerza en la **dirección del eje** hacen girar al cuerpo rígido; las componentes perpendiculares tienden a mover al eje de su posición fija (son absorbidas por los apoyos).

$$ds = r\, d\theta$$

$$dw = F\cos\phi \, ds = (F\cos\phi)(r\,d\theta)$$

Como $F\cos\phi \cdot r$ es la magnitud del momento de rotación instantáneo ejercido por F:

$$dw = T\, d\theta \qquad \text{(diferencial de trabajo en rotación en torno a un eje fijo)}$$

**Potencia instantánea:**

$$\frac{dw}{dt} = T\frac{d\theta}{dt} \quad \Rightarrow \quad P = T\cdot\omega \qquad (1)$$

> Analogía con traslación: $P = F \cdot v$

**Trabajo para un desplazamiento angular entre θ₁ y θ₂ (T constante):**

$$W = T(\theta_2 - \theta_1)$$

---

## 6. Ecuación fundamental de la dinámica rotacional

La rapidez con que aumenta la energía cinética de un cuerpo rígido:

$$\frac{d\left(\frac{1}{2}I\omega^2\right)}{dt} = I\omega\frac{d\omega}{dt} = I\omega\alpha \qquad (\alpha: \text{aceleración angular})$$

Igualando con la ecuación (1) de potencia ($P = T\omega$):

$$T\omega = I\omega\alpha \quad \Rightarrow \quad \boxed{T = I\alpha} \quad \Rightarrow \quad P = I\omega\alpha$$

### Comparación con la Ley de Newton (sistema de partículas)

| Traslación | Rotación |
|---|---|
| $F_{ext} = \dfrac{dP}{dt}$ | $T_{ext} = \dfrac{dL}{dt}$ |
| $P = m\cdot v$ | $L = I\cdot\omega$ |

> Para un cuerpo rígido **simétrico** respecto al eje de rotación: $L = I\omega$. Si L representa la componente vectorial de L según el eje de rotación (L_y), la ecuación vale para **cualquier** cuerpo rígido, sea simétrico o no.

---

## 7. Conservación de la cantidad de movimiento angular

Partiendo de $T_{ext} = dL/dt$: si el momento de rotación de todas las fuerzas exteriores es cero:

$$\frac{dL}{dt} = 0 \quad \Rightarrow \quad L = \text{cte}$$

$$\boxed{I_1\,\omega_1 = I_2\,\omega_2}$$

> Esta ley es aplicable tanto en la mecánica de cuerpos como en la física atómica/cuántica, ya que —a diferencia de las leyes de la mecánica newtoniana clásica— es de **aplicación universal** (también para cuerpos celestes y estrellas).

**Principio general:**
> "La cantidad de movimiento angular total L de un sistema cualquiera respecto al origen de un marco de referencia inercial se puede calcular sumando la cantidad de movimiento angular respecto a su centro de masa con la cantidad de movimiento angular que proviene del movimiento del centro de masa respecto al origen."

**Ecuaciones cinemáticas de referencia (rotación):**

$$\theta = \omega_0 t + \frac{1}{2}\alpha t^2 \qquad \omega = \omega_0 + \alpha t \qquad \alpha = \frac{d\omega}{dt}$$

---

## 8. Movimiento combinado: rotación y traslación (rodadura)

### 8.1 Eje instantáneo de rotación

Cada partícula del cuerpo rígido se comporta como si instantáneamente rotara en torno a un eje fijo P (punto de contacto).

$$k = \frac{1}{2}I_P\,\omega^2$$

Usando Steiner: $I_P = I_{CM} + MR^2$

$$k = \frac{1}{2}I_{CM}\,\omega^2 + \frac{1}{2}MR^2\omega^2$$

Como $R\omega = V_{CM}$:

$$\boxed{k = \frac{1}{2}I_{CM}\,\omega^2 + \frac{1}{2}M V_{CM}^2}$$

**Interpretación:**
- $\frac{1}{2}I_{CM}\omega^2$ → energía cinética de rotación pura (alrededor del CM)
- $\frac{1}{2}MV_{CM}^2$ → energía cinética de traslación pura

> La combinación de rotación (alrededor del CM) + traslación equivale a una **rotación pura** en torno a un eje que pasa por el punto de contacto instantáneo.

### 8.2 Velocidades en distintos puntos de un cuerpo que rueda

| Punto | Velocidad |
|---|---|
| Q (superior) | $v = 2v_{CM}$ → $v = v_{CM} + \omega R$ |
| C (centro) | $v = v_{CM}$ → $v = v_{CM} + \omega\cdot 0$ |
| P (contacto, inferior) | $v = 0$ → $v = v_{CM} - \omega R$ |

### 8.3 Rodadura vs. deslizamiento (plano inclinado)

- Rodando: $v = \sqrt{\dfrac{4}{3}\rho h}$
- Deslizando: $v = \sqrt{2\rho h}$

> **Nota de consistencia con la fuente:** tal cual figura en el apunte original del docente (pág. 7 del PDF), ambas fórmulas usan el símbolo `ρ`. Se mantiene así en este documento porque refleja fielmente el material provisto por el profesor. Sin embargo, dimensionalmente `ρ` no puede corresponder a una densidad (no da unidades de velocidad); la ecuación sale de igualar `mgh = ½mv² + ½Iω²`, que solo cierra si ese símbolo es **g (aceleración de la gravedad)**. **Al resolver cálculos reales, usar `g`, no `ρ`.**

> La velocidad del centro de masa es **menor** rodando que deslizando → la rodadura es un estado **más estable**. Por eso es fundamental que exista una fuerza mínima de rozamiento entre las superficies para que haya rodadura pura.

### 8.4 Momento perpendicular al eje

Si se aplica un momento con componente perpendicular al eje (tendiendo a hacerlo girar en otra dirección), los apoyos aplican automáticamente un contra-momento igual y opuesto que anula el efecto de esa componente.

---

## 9. Dinámica de ejes no fijos: movimiento de precesión

A diferencia de las secciones anteriores, aquí se trata la rotación de un cuerpo rígido en torno a un eje que **no está fijo** en el marco de referencia inercial, examinando momentos con componentes perpendiculares al eje de rotación (caso típico: el trompo).

### 9.1 Planteo

El trompo gira sobre un punto O, pero L varía su **dirección** (no su magnitud) debido al momento externo. Fuerzas actuantes: peso (m·g) y reacción vertical en O (esta última no genera momento por pasar por O).

$$T = r \times F \; (\text{vectorial}) = r\cdot mg \cdot \sin(\pi - \theta)$$

T, L y r giran alrededor del eje Y con velocidad angular **ω_P** (velocidad de precesión) conforme el trompo precede.

### 9.2 Relación fundamental

$$T = \frac{dL}{dt}$$

Como dL debe apuntar en la dirección de T, y T es perpendicular a L, el cambio dL es perpendicular a L → **la punta del vector L describe un círculo horizontal** con el tiempo (ver Fig. 2 del apunte: cono de precesión).

$$\Delta L = T\,\Delta t \quad (\Delta t \text{ pequeño})$$

$$\omega_P = \frac{\Delta\phi}{\Delta t}$$

Como ΔL << L:

$$\Delta\phi = \frac{\Delta L}{L\sin\theta} = \frac{T\,\Delta t}{L\sin\theta} \quad \Rightarrow \quad \omega_P = \frac{T}{L\sin\theta} \qquad (1)$$

Y como $T = r\,mg\,\sin\theta$:

$$\boxed{\omega_P = \frac{r\,mg}{L}}$$

> La velocidad angular de precesión es **independiente de θ** y **inversamente proporcional a L**: si L aumenta, ω_P disminuye, y viceversa.

**Forma vectorial (de la ecuación 1):**

$$\vec{T} = \vec{\omega}_P \times \vec{L}$$

---

## 10. Cantidad de movimiento angular y velocidad angular (L y ω no paralelos)

Se estudia ahora la relación entre L y ω para una partícula girando en torno a un eje fijo inercial, cuando **L y ω no son paralelos** (L cambia de dirección con el tiempo, aunque su magnitud se mantiene constante).

### 10.1 Caso de una partícula

Como $dL/dt \neq 0$, debe existir un momento T no nulo actuando sobre la partícula respecto al origen O (por ejemplo, la fuerza centrípeta ejercida mediante una cuerda).

**Aceleración centrípeta:**

$$F = \frac{mv^2}{r} = m\omega^2 r$$

Este caso es análogo al del trompo: hay precesión del vector L alrededor de un eje vertical con velocidad angular ω. En ambos casos, T es perpendicular al plano formado por L y ω.

$$T = L\,\omega\,\sin(90-\theta) = L\,\omega\cos\theta$$

Con el radio del círculo $a = r\sin\theta$:

$$T = F\, r\,\sin(90+\theta) = \left[m\omega^2(r\sin\theta)\right]r\cos\theta$$

$$L = r\, m\, v = m\, r^2\,\omega\sin\theta$$

Tomando la componente Ly (según el eje Y):

$$L_y = L\sin\theta = m\,r^2\,\omega\sin^2\theta = m\,a^2\,\omega$$

Donde $m\,a^2$ es el momento de inercia de la partícula respecto al eje Y. Luego:

$$\boxed{L_y = I\,\omega}$$

> Nótese: en este caso L y ω **no** apuntan en la misma dirección, pero **L_y** y ω sí.

### 10.2 Caso de dos partículas diametralmente opuestas

Para dos partículas en la misma órbita, diametralmente opuestas, con $m_1 = m_2$ y $|r_1| = |r_2|$:

$$L = L_1 + L_2 \quad \Rightarrow \quad L \parallel \omega$$

> Las componentes perpendiculares de L₁ y L₂ se cancelan entre sí por simetría, quedando un vector L neto **coincidente** con ω. Este resultado se puede extender a un cuerpo rígido con infinitos pares de partículas diametralmente opuestas (lo que explica por qué, en cuerpos simétricos respecto al eje de giro, L = Iω es válido sin ambigüedad de dirección).

---

## 11. Ejercicio de aplicación (págs. 14-15): tren de engranajes

### 11.1 Esquema del mecanismo

Sistema de dos ejes paralelos engranados entre sí, cada uno apoyado sobre dos rodamientos.

**Materiales:**
- Eje: acero al carbono
- Engranajes: aluminio
- Rodamientos: acero

**Densidades:**
$$\delta_{Al} = 2{,}708 \text{ g/cm}^3 \qquad \delta_{Acero} = 7{,}85 \text{ g/cm}^3$$

**Geometría — Eje 1 (n₁):**
- Diámetro del eje: 25 mm
- Diámetro del engranaje: 250 mm
- Altura respecto a la base: H₁ = 1500 mm
- Largo del eje: 300 mm

**Geometría — Eje 2 (n₂):**
- Diámetro del eje: 35 mm
- Diámetro del engranaje: 200 mm
- Altura respecto a la base: H₂ (sin valor en el enunciado; no hace falta para resolver el ejercicio — ver Punto 7)

**Ancho de cara de los engranajes:** 30 mm

> **⚠ Aclaración de nomenclatura — "chico"/"grande" no es consistente entre eje y engranaje:**
> - Por diámetro de **eje**: eje 1 = 25 mm (el más chico), eje 2 = 35 mm (el más grande).
> - Por diámetro de **engranaje**: engranaje del eje 1 = 250 mm (el más grande de los dos), engranaje del eje 2 = 200 mm (el más chico de los dos).
>
> Es decir, el eje **chico** (eje 1) lleva el engranaje **grande**, y el eje **grande** (eje 2) lleva el engranaje **chico** — el orden se invierte. Los calificativos "chico"/"grande" que se usan más abajo para los **rodamientos** siguen el criterio del diámetro de **eje** (bore), no el de engranaje, y no deben confundirse entre sí. Por eso, en este documento los engranajes se identifican siempre por su eje ($R_1$ = radio del engranaje del eje 1 = 125 mm; $R_2$ = radio del engranaje del eje 2 = 100 mm), nunca como "chico"/"grande".

**Rodamientos (según tabla SKF, serie 62 — rígidos de una hilera de bolas):**

| Rodamiento | Bore (d) | Diámetro exterior (D) | Ancho axial (B) | Masa |
|---|---|---|---|---|
| Chico (eje 1) | 25 mm | 52 mm | 15 mm | 0,128 kg |
| Grande (eje 2) | 35 mm | 72 mm | 17 mm | 0,288 kg |

*(Corresponden a los rodamientos 6205 y 6207 de la serie 62 SKF. **Bore** = diámetro interior del rodamiento, es decir el diámetro del agujero central por donde pasa el eje — por eso coincide con el "Diámetro del eje" de cada geometría.)*

### 11.2 Datos del problema

- $n_1 = 2800$ RPM
- $F = 200$ N (fuerza tangencial aplicada entre engranajes)
- Factores de conversión: $1\text{ HP}\cdot\text{hora} = 2{,}685\times10^5$ J; $\;1\text{ HP} = 745{,}8$ J/s

> **Nota de consistencia con la fuente:** los dos factores, tal cual figuran en el enunciado (pág. 15), son incompatibles entre sí: $1\text{ HP}\cdot\text{hora} = 745{,}8\ \text{J/s}\times 3600\ \text{s} = 2{,}685\times10^{6}$ J, no $10^{5}$. Se mantiene el valor del enunciado porque refleja fielmente el material del profesor, pero el exponente correcto es $10^{6}$. Para el Punto 8 se usa $1\text{ HP} = 745{,}8$ J/s (conversión de potencia); el factor HP·hora, que es de energía, no interviene.

### 11.3 Consigna — 8 puntos a calcular

1. **n₂** — velocidad de rotación del eje 2
2. **Momento de inercia de los rodamientos**
3. **Momento de inercia de los ejes**
4. $L_1 = I_1\,\omega_1$ — cantidad de movimiento rotacional del eje 1
5. $L_2 = I_2\,\omega_2$ — cantidad de movimiento rotacional del eje 2
6. Si repentinamente $I_1$ e $I_2$ se reducen a la mitad: ¿cuánto valen $\omega_1$ y $\omega_2$?
7. ¿Qué sucede con la cantidad de movimiento angular del mecanismo respecto de un sistema de referencia fijo al piso (en la base de la máquina)? ¿Cuánto vale?
8. ¿Cuánto vale la potencia del mecanismo en HP? (considerando el momento de inercia del conjunto engranaje + eje)

---

## Resolución — avance registrado en esta sesión

### Punto 1: n₂ (y ω₁, ω₂)

**Dato de partida:** $n_1 = 2800$ RPM (revoluciones por minuto — dato del enunciado, pág. 15 del apunte de Abud).

**Paso previo — de RPM a ω (rad/s):**

Todas las ecuaciones de esta guía (5, 6, 7 — $T=I\alpha$, $L=I\omega$, $P=T\cdot\omega$, etc.) están planteadas en unidades del Sistema Internacional: ángulo en **radianes** y tiempo en **segundos**. RPM ("revoluciones por minuto") no es una unidad de ese sistema, así que **antes de reemplazar en cualquier fórmula hay que convertir n → ω**. Esta conversión se va a reutilizar en los puntos 4, 5, 6 y 8, así que se deja fija acá como referencia:

- 1 revolución (vuelta completa) = $2\pi$ rad
- 1 minuto = 60 s

$$\omega\left[\frac{\text{rad}}{\text{s}}\right] = n\left[\frac{\text{rev}}{\text{min}}\right] \cdot \frac{2\pi\,\text{rad}}{1\,\text{rev}} \cdot \frac{1\,\text{min}}{60\,\text{s}}$$

$$\boxed{\omega = \frac{2\pi\,n}{60} = \frac{\pi\,n}{30}} \qquad \text{(n en RPM} \rightarrow \omega \text{ en rad/s)}$$

Aplicado a $\omega_1$:

$$\omega_1 = \frac{2\pi \cdot 2800}{60} \approx 293{,}2 \text{ rad/s}$$

**Condición de engrane:** en el punto donde dos engranajes están en contacto (sin deslizar entre sí), ambos tienen la **misma velocidad tangencial lineal** en ese punto:

$$v_{contacto} = \omega_1 R_1 = \omega_2 R_2$$

Con $R_1 = 0{,}125$ m (radio del engranaje del eje 1) y $R_2 = 0{,}1$ m (radio del engranaje del eje 2) — ver aclaración de nomenclatura en 11.1:

$$\omega_2 = \omega_1\cdot\frac{R_1}{R_2} = 293{,}2 \cdot \frac{0{,}125}{0{,}1} \approx 366{,}5 \text{ rad/s}$$

*Verificación de $v_{contacto}$ (debe dar el mismo valor por los dos lados):*

$$v_{contacto} = \omega_1 R_1 = 293{,}2 \times 0{,}125 \approx 36{,}6 \text{ m/s} \qquad v_{contacto} = \omega_2 R_2 = 366{,}5 \times 0{,}1 \approx 36{,}6 \text{ m/s} \quad \checkmark$$

**Volviendo a RPM** (despejando n de la misma fórmula de conversión, $n = 60\,\omega/2\pi$):

$$n_2 = \frac{60 \cdot 366{,}5}{2\pi} \approx \boxed{3500 \text{ RPM}}$$

*(Atajo equivalente, sin pasar por ω: como el factor $2\pi/60$ es el mismo para ambos ejes, se cancela y queda directamente $n_2 = n_1\cdot R_1/R_2 = 2800\cdot125/100=3500$ RPM. Se llega al mismo resultado por las dos vías — se muestra el desarrollo completo acá porque ω₁ y ω₂ en rad/s son insumo directo de los puntos 4, 5, 6 y 8.)*

**Resultados de este punto (para reutilizar más adelante):**

| Eje | n (RPM) | ω (rad/s) |
|---|---|---|
| 1 | 2800 | ≈ 293,2 |
| 2 | 3500 | ≈ 366,5 |

### Punto 2: Momento de inercia de los rodamientos

Modelo: corona circular (anillo), usando la **masa real de catálogo** (no masa calculada por densidad×volumen, ya que el rodamiento real tiene huecos internos — bolas, jaula):

$$I = \frac{1}{2}m\left(R_{ext}^2 + R_{int}^2\right)$$

**Rodamiento chico (eje 1 — bore 25 mm)**

- $m = 0{,}128$ kg (dato de tabla SKF)
- $R_{ext} = 52/2 = 26$ mm $= 0{,}026$ m $\Rightarrow R_{ext}^2 = 6{,}76\times10^{-4}$ m² *(D = 52 mm: dato de tabla SKF)*
- $R_{int} = 25/2 = 12{,}5$ mm $= 0{,}0125$ m $\Rightarrow R_{int}^2 = 1{,}5625\times10^{-4}$ m² *(d = 25 mm: diámetro del eje 1, dato del esquema del mecanismo — apunte de Abud, pág. 14; no de la tabla SKF)*

$$I_{1,rod} = \frac{1}{2}(0{,}128)\left(6{,}76\times10^{-4} + 1{,}5625\times10^{-4}\right) = \frac{1}{2}(0{,}128)\left(8{,}3225\times10^{-4}\right)$$

$$I_{1,rod} \approx 5{,}33\times10^{-5} \text{ kg}\cdot\text{m}^2 \quad \text{(por rodamiento)}$$

Total eje 1 (×2 rodamientos):

$$I_{1,rodamientos} \approx 1{,}065\times10^{-4} \text{ kg}\cdot\text{m}^2$$

**Rodamiento grande (eje 2 — bore 35 mm)**

- $m = 0{,}288$ kg (dato de tabla SKF)
- $R_{ext} = 72/2 = 36$ mm $= 0{,}036$ m $\Rightarrow R_{ext}^2 = 1{,}296\times10^{-3}$ m² *(D = 72 mm: dato de tabla SKF)*
- $R_{int} = 35/2 = 17{,}5$ mm $= 0{,}0175$ m $\Rightarrow R_{int}^2 = 3{,}0625\times10^{-4}$ m² *(d = 35 mm: diámetro del eje 2, dato del esquema del mecanismo — apunte de Abud, pág. 14; no de la tabla SKF)*

$$I_{2,rod} = \frac{1}{2}(0{,}288)\left(1{,}296\times10^{-3} + 3{,}0625\times10^{-4}\right) = \frac{1}{2}(0{,}288)\left(1{,}60225\times10^{-3}\right)$$

$$I_{2,rod} \approx 2{,}307\times10^{-4} \text{ kg}\cdot\text{m}^2 \quad \text{(por rodamiento)}$$

Total eje 2 (×2 rodamientos):

$$I_{2,rodamientos} \approx 4{,}614\times10^{-4} \text{ kg}\cdot\text{m}^2$$

### Punto 3: Momento de inercia de los ejes

**Alcance:** este punto calcula **solo el eje** (acero al carbono). El momento de inercia de los engranajes (aluminio) se calcula aparte, a continuación, como cilindro anular con bore igual al diámetro del eje (caso (b) de la tabla), para no contar dos veces el núcleo que el eje ocupa dentro del engranaje. Los momentos de inercia totales de cada conjunto ($I_1$, $I_2$ para los Puntos 4 y 5) se arman después sumando eje + engranaje + rodamientos.

Modelo: cilindro sólido respecto de su propio eje (caso (c) de la tabla, sección 4):

$$I = \frac{1}{2}MR^2$$

A diferencia de los rodamientos (Punto 2), acá no hay masa de catálogo: la masa se obtiene por densidad × volumen, con el eje como cilindro macizo:

$$M = \delta_{Acero}\cdot V = \delta_{Acero}\cdot\pi R^2 L$$

**Datos comunes a ambos ejes:**

- $\delta_{Acero} = 7{,}85$ g/cm³ $= 7850$ kg/m³ *(dato del esquema, apunte de Abud, pág. 14; conversión: $7{,}85\ \text{g/cm}^3 = 7{,}85\times10^{-3}\ \text{kg} \,/\, 10^{-6}\ \text{m}^3$)*
- $L = 300$ mm $= 0{,}3$ m *(dato del enunciado, pág. 15; se da una sola vez, por lo que se asume el mismo largo para ambos ejes)*

**Eje 1 (diámetro 25 mm)**

- $R_1 = 25/2 = 12{,}5$ mm $= 0{,}0125$ m $\Rightarrow R_1^2 = 1{,}5625\times10^{-4}$ m² *(diámetro: dato del esquema, apunte de Abud, pág. 14)*

$$V_1 = \pi R_1^2 L = \pi\,(1{,}5625\times10^{-4})(0{,}3) \approx 1{,}473\times10^{-4} \text{ m}^3$$

$$M_1 = 7850 \cdot 1{,}473\times10^{-4} \approx 1{,}156 \text{ kg}$$

$$I_{1,eje} = \frac{1}{2}(1{,}156)(1{,}5625\times10^{-4}) \approx 9{,}03\times10^{-5} \text{ kg}\cdot\text{m}^2$$

**Eje 2 (diámetro 35 mm)**

- $R_2 = 35/2 = 17{,}5$ mm $= 0{,}0175$ m $\Rightarrow R_2^2 = 3{,}0625\times10^{-4}$ m² *(diámetro: dato del esquema, apunte de Abud, pág. 14)*

$$V_2 = \pi R_2^2 L = \pi\,(3{,}0625\times10^{-4})(0{,}3) \approx 2{,}886\times10^{-4} \text{ m}^3$$

$$M_2 = 7850 \cdot 2{,}886\times10^{-4} \approx 2{,}266 \text{ kg}$$

$$I_{2,eje} = \frac{1}{2}(2{,}266)(3{,}0625\times10^{-4}) \approx 3{,}47\times10^{-4} \text{ kg}\cdot\text{m}^2$$

*Verificación cruzada con la forma simplificada* $I = \tfrac{1}{2}\,\delta\,\pi\,L\,R^4$ *(elimina el paso intermedio de la masa):* $I_{1,eje} \approx 9{,}03\times10^{-5}$ y $I_{2,eje} \approx 3{,}47\times10^{-4}$ kg·m² — coinciden con lo calculado arriba.

**Resultados de este punto (para reutilizar más adelante):**

| Eje | Diámetro (mm) | M (kg) | I (kg·m²) |
|---|---|---|---|
| 1 | 25 | ≈ 1,156 | ≈ 9,03×10⁻⁵ |
| 2 | 35 | ≈ 2,266 | ≈ 3,47×10⁻⁴ |

### Punto 3b: Momento de inercia de los engranajes

Los engranajes no figuran como ítem propio de la consigna, pero hacen falta para armar $I_1$ e $I_2$ en los Puntos 4, 5 y 8 ("conjunto engranaje y eje").

**Modelo:** cilindro anular (caso (b) de la tabla, sección 4), con radio interior igual al radio del eje que lo atraviesa. Así se evita contar dos veces el núcleo que el eje ya ocupa (Punto 3). Se desprecia el dentado: el engranaje se trata como un cilindro liso de diámetro igual al dado en el esquema, y de largo axial igual al ancho de cara.

$$I = \frac{1}{2}M\left(R_{ext}^2 + R_{int}^2\right) \qquad M = \delta_{Al}\cdot\pi\left(R_{ext}^2 - R_{int}^2\right)b$$

**Datos comunes a ambos engranajes:**

- $\delta_{Al} = 2{,}708$ g/cm³ $= 2708$ kg/m³ *(dato del esquema, apunte de Abud, pág. 14; misma conversión que para el acero)*
- $b = 30$ mm $= 0{,}03$ m *(ancho de cara, dato del esquema, apunte de Abud, pág. 14)*

**Engranaje del eje 1 (diámetro 250 mm)**

- $R_{ext} = 250/2 = 125$ mm $= 0{,}125$ m $\Rightarrow R_{ext}^2 = 1{,}5625\times10^{-2}$ m² *(diámetro: dato del esquema)*
- $R_{int} = 25/2 = 12{,}5$ mm $= 0{,}0125$ m $\Rightarrow R_{int}^2 = 1{,}5625\times10^{-4}$ m² *(radio del eje 1, Punto 3)*

$$V = \pi\left(R_{ext}^2 - R_{int}^2\right)b = \pi\,(1{,}5625\times10^{-2} - 1{,}5625\times10^{-4})(0{,}03) \approx 1{,}458\times10^{-3} \text{ m}^3$$

$$M = 2708 \cdot 1{,}458\times10^{-3} \approx 3{,}948 \text{ kg}$$

$$I_{1,eng} = \frac{1}{2}(3{,}948)\left(1{,}5625\times10^{-2} + 1{,}5625\times10^{-4}\right) = \frac{1}{2}(3{,}948)(1{,}578\times10^{-2}) \approx 3{,}12\times10^{-2} \text{ kg}\cdot\text{m}^2$$

**Engranaje del eje 2 (diámetro 200 mm)**

- $R_{ext} = 200/2 = 100$ mm $= 0{,}1$ m $\Rightarrow R_{ext}^2 = 1{,}0\times10^{-2}$ m² *(diámetro: dato del esquema)*
- $R_{int} = 35/2 = 17{,}5$ mm $= 0{,}0175$ m $\Rightarrow R_{int}^2 = 3{,}0625\times10^{-4}$ m² *(radio del eje 2, Punto 3)*

$$V = \pi\,(1{,}0\times10^{-2} - 3{,}0625\times10^{-4})(0{,}03) \approx 9{,}136\times10^{-4} \text{ m}^3$$

$$M = 2708 \cdot 9{,}136\times10^{-4} \approx 2{,}474 \text{ kg}$$

$$I_{2,eng} = \frac{1}{2}(2{,}474)\left(1{,}0\times10^{-2} + 3{,}0625\times10^{-4}\right) = \frac{1}{2}(2{,}474)(1{,}0306\times10^{-2}) \approx 1{,}27\times10^{-2} \text{ kg}\cdot\text{m}^2$$

*Verificación cruzada con la forma simplificada* $I = \tfrac{1}{2}\,\delta\,\pi\,b\left(R_{ext}^4 - R_{int}^4\right)$*:* $I_{1,eng} \approx 3{,}12\times10^{-2}$ y $I_{2,eng} \approx 1{,}27\times10^{-2}$ kg·m² — coinciden.

**Resultados de este punto (para reutilizar más adelante):**

| Engranaje | Diámetro (mm) | M (kg) | I (kg·m²) |
|---|---|---|---|
| Eje 1 | 250 | ≈ 3,948 | ≈ 3,12×10⁻² |
| Eje 2 | 200 | ≈ 2,474 | ≈ 1,27×10⁻² |

*Nótese que, pese a que el eje 2 es el de mayor diámetro de eje, su engranaje es el de menor momento de inercia (ver aclaración de nomenclatura en 11.1).*

### Puntos 4 y 5: Cantidad de movimiento rotacional $L_1$ y $L_2$

Ambos puntos son el mismo cálculo aplicado a cada eje: $L = I\,\omega$ (sección 6), con $I$ total del conjunto y $\omega$ del Punto 1 (en rad/s, nunca en RPM).

**Qué entra en $I_1$ e $I_2$ — se calculan dos variantes:**

- **Variante A — PRINCIPAL (eje + engranaje + rodamientos):** usa todo lo calculado en los Puntos 2, 3 y 3b. Es la lectura que justifica que la consigna pida el momento de inercia de los rodamientos como ítem propio (Punto 2), ya que solo los Puntos 4, 5 y 7 podrían usarlo.
- **Variante B — alternativa (eje + engranaje):** deja afuera los rodamientos. Es la lectura literal del Punto 8, que aclara "considerar el momento de inercia del conjunto engranaje y eje" — aclaración que sería innecesaria si los rodamientos no estuvieran en el resto de los puntos.

La consigna no lo define para los Puntos 4 y 5: se adopta la **variante A como respuesta principal** y se presenta la **B como alternativa**, declarando el supuesto. La diferencia es de ≈ 0,3 % (eje 1) y ≈ 3,5 % (eje 2). Lo ideal es confirmar el criterio con los ayudantes (Costucica, Gallo). El Punto 8 (potencia) da el mismo resultado con ambas.

**Componentes de $I$ (de los Puntos 2, 3 y 3b), en kg·m²:**

| Eje | $I_{eje}$ | $I_{engranaje}$ | $I_{rodamientos}$ (×2) |
|---|---|---|---|
| 1 | $9{,}03\times10^{-5}$ | $3{,}115\times10^{-2}$ | $1{,}065\times10^{-4}$ |
| 2 | $3{,}47\times10^{-4}$ | $1{,}275\times10^{-2}$ | $4{,}614\times10^{-4}$ |

**Eje 1**

$$I_1^{(B)} = I_{eje} + I_{eng} = 9{,}03\times10^{-5} + 3{,}115\times10^{-2} \approx 3{,}124\times10^{-2} \text{ kg}\cdot\text{m}^2$$

$$I_1^{(A)} = I_1^{(B)} + I_{rod} = 3{,}124\times10^{-2} + 1{,}065\times10^{-4} \approx 3{,}135\times10^{-2} \text{ kg}\cdot\text{m}^2$$

$$L_1^{(B)} = I_1^{(B)}\,\omega_1 = (3{,}124\times10^{-2})(293{,}2) \approx 9{,}16 \text{ kg}\cdot\text{m}^2/\text{s}$$

$$L_1^{(A)} = I_1^{(A)}\,\omega_1 = (3{,}135\times10^{-2})(293{,}2) \approx 9{,}19 \text{ kg}\cdot\text{m}^2/\text{s}$$

**Eje 2**

$$I_2^{(B)} = 3{,}47\times10^{-4} + 1{,}275\times10^{-2} \approx 1{,}310\times10^{-2} \text{ kg}\cdot\text{m}^2$$

$$I_2^{(A)} = 1{,}310\times10^{-2} + 4{,}614\times10^{-4} \approx 1{,}356\times10^{-2} \text{ kg}\cdot\text{m}^2$$

$$L_2^{(B)} = I_2^{(B)}\,\omega_2 = (1{,}310\times10^{-2})(366{,}5) \approx 4{,}80 \text{ kg}\cdot\text{m}^2/\text{s}$$

$$L_2^{(A)} = I_2^{(A)}\,\omega_2 = (1{,}356\times10^{-2})(366{,}5) \approx 4{,}97 \text{ kg}\cdot\text{m}^2/\text{s}$$

*(Unidad: $\text{kg}\cdot\text{m}^2/\text{s}$, equivalente a $\text{N}\cdot\text{m}\cdot\text{s}$ o $\text{J}\cdot\text{s}$.)*

**Resultados de estos puntos:**

| Eje | $\omega$ (rad/s) | $I^{(A)}$ principal (kg·m²) | $L^{(A)}$ principal (kg·m²/s) | $I^{(B)}$ alternativa (kg·m²) | $L^{(B)}$ alternativa (kg·m²/s) | Diferencia A vs B |
|---|---|---|---|---|---|---|
| 1 | ≈ 293,2 | ≈ 3,135×10⁻² | ≈ 9,19 | ≈ 3,124×10⁻² | ≈ 9,16 | ≈ 0,3 % |
| 2 | ≈ 366,5 | ≈ 1,356×10⁻² | ≈ 4,97 | ≈ 1,310×10⁻² | ≈ 4,80 | ≈ 3,5 % |

*Los engranajes están engranados, por lo que giran en **sentidos opuestos**: los valores de arriba son módulos. El signo relativo importa en el Punto 7.*

*Salvedad física: en un rodamiento real solo el aro interior (y parte de las bolas) gira con el eje; el aro exterior queda fijo a la carcasa. Modelar el rodamiento completo girando (Punto 2) sobreestima su aporte, por eso la variante A es una cota superior.*

### Punto 6: $I_1$ e $I_2$ se reducen a la mitad — ¿cuánto valen $\omega_1$ y $\omega_2$?

**Planteo:** el cambio es "repentino" y la consigna no menciona ningún momento externo sobre los ejes, por lo que se aplica la conservación de la cantidad de movimiento angular (sección 7, $T_{ext}=0 \Rightarrow L=\text{cte}$).

**Notación:** en la sección 7 los subíndices 1 y 2 significan "estado inicial" y "estado final". En este ejercicio 1 y 2 identifican al **eje**, así que el estado final se marca con prima ($\,'\,$):

$$I_1\,\omega_1 = I_1'\,\omega_1' \qquad\qquad I_2\,\omega_2 = I_2'\,\omega_2'$$

Con $I_1' = I_1/2$ e $I_2' = I_2/2$:

$$\omega_1' = \frac{I_1}{I_1'}\,\omega_1 = \frac{I_1}{I_1/2}\,\omega_1 = 2\,\omega_1 \qquad\qquad \omega_2' = 2\,\omega_2$$

*(El resultado no depende de cuánto valga $I$, solo de la relación $I/I'=2$: es idéntico en las variantes A y B del Punto 4, y también vale como resultado general de la conservación de $L$.)*

**Valores** (con $\omega_1 \approx 293{,}2$ rad/s y $\omega_2 \approx 366{,}5$ rad/s del Punto 1):

$$\omega_1' = 2\,(293{,}2) \approx 586{,}4 \text{ rad/s} \qquad\qquad \omega_2' = 2\,(366{,}5) \approx 733{,}0 \text{ rad/s}$$

**En RPM** (con $n = 60\,\omega/2\pi$, misma conversión del Punto 1):

$$n_1' = \frac{60 \cdot 586{,}4}{2\pi} \approx 5600 \text{ RPM} \qquad\qquad n_2' = \frac{60 \cdot 733{,}0}{2\pi} \approx 7000 \text{ RPM}$$

**Verificación de coherencia con el engrane:** al duplicarse ambas velocidades, la relación entre ellas no cambia, y la condición de engrane del Punto 1 se sigue cumpliendo:

$$\omega_1' R_1 = 586{,}4 \times 0{,}125 \approx 73{,}3 \text{ m/s} \qquad \omega_2' R_2 = 733{,}0 \times 0{,}1 \approx 73{,}3 \text{ m/s} \quad \checkmark$$

**Qué se conserva y qué no:** $L$ se conserva (es el dato de partida), pero la energía cinética de rotación $K = \tfrac{1}{2}I\omega^2$ **no**: $K' = \tfrac{1}{2}\left(\tfrac{I}{2}\right)(2\omega)^2 = 2K$. Por ejemplo, en el eje 1 (variante A) pasa de $K_1 \approx 1{,}35\times10^{3}$ J a $K_1' \approx 2{,}70\times10^{3}$ J. Ese incremento de energía debe provenir del trabajo realizado por lo que produce la reducción de $I$ (análogo a una patinadora que cierra los brazos).

**Resultados de este punto:**

| Eje | $\omega$ antes (rad/s) | $\omega'$ después (rad/s) | $n$ antes (RPM) | $n'$ después (RPM) |
|---|---|---|---|---|
| 1 | ≈ 293,2 | ≈ 586,4 | 2800 | 5600 |
| 2 | ≈ 366,5 | ≈ 733,0 | 3500 | 7000 |

### Punto 7: cantidad de movimiento angular del mecanismo respecto de un sistema de referencia en la base

**Qué pide:** el $L$ total del mecanismo medido respecto de un origen $O$ ubicado en la base de la máquina (anclada al piso), y qué sucede con él. El enunciado da $H_1 = 1500$ mm como distancia del eje 1 a esa base, y $H_2$ (eje 2) figura en el esquema sin valor.

**Principio a usar** (sección 7, "Principio general"): el $L$ total respecto de un origen es la suma del $L$ respecto del centro de masa más el $L$ que proviene del movimiento del centro de masa respecto de ese origen:

$$\vec{L}_O = \vec{L}_{CM} + \vec{r}_{CM}\times M\,\vec{v}_{CM}$$

**Aplicado a cada eje (con su engranaje y rodamientos):**

- Cada conjunto es simétrico respecto de su eje de giro y gira alrededor de un eje fijo que pasa por su centro de masa, por lo que $L_{CM} = I\,\omega$, dirigido según el eje (secciones 6 y 10.2).
- El centro de masa **no se mueve** ($v_{CM} = 0$), así que el segundo término se anula: $\vec{r}_{CM}\times M\vec{v}_{CM} = 0$.

$$\vec{L}_{O,\,eje\,1} = I_1\,\omega_1 \qquad\qquad \vec{L}_{O,\,eje\,2} = I_2\,\omega_2$$

**Consecuencia:** $L$ no depende de dónde esté el origen. Las distancias $H_1$ y $H_2$ **no intervienen** en el resultado: el sistema de referencia en la base da el mismo valor que uno ubicado sobre los propios ejes. Por eso $H_2$ no hace falta y su ausencia en el enunciado no impide resolver el punto.

**Sentidos de giro:** los dos engranajes están engranados por el exterior, así que sus ejes (paralelos) giran en **sentidos opuestos** y sus vectores $\vec{L}_1$ y $\vec{L}_2$ son antiparalelos. Tomando como positivo el sentido de giro del eje 1:

$$L_{total} = L_1 - L_2$$

*(Error a evitar: sumar los módulos, $L_1 + L_2$. Con la variante A daría ≈ 14,16 en vez de ≈ 4,22 kg·m²/s.)*

**Valores** (de los Puntos 4 y 5, en kg·m²/s; variante A principal, B alternativa):

$$L_{total}^{(A)} = 9{,}19 - 4{,}97 \approx 4{,}22 \text{ kg}\cdot\text{m}^2/\text{s} \qquad\qquad L_{total}^{(B)} = 9{,}16 - 4{,}80 \approx 4{,}36 \text{ kg}\cdot\text{m}^2/\text{s}$$

**Qué sucede con $L_{total}$:**

- No es nulo: al tener los ejes distinto $I\,\omega$, los dos momentos angulares no se cancelan; queda un $L$ neto en la dirección de los ejes y con el sentido de giro del eje 1.
- Es **constante en el tiempo** mientras no haya un momento externo según el eje: la fuerza de $200$ N entre engranajes es una acción y reacción interna (se cancela en $T_{ext}$), y las reacciones de los apoyos solo aportan momentos perpendiculares al eje (sección 8.4).
- **Se conserva también en el cambio del Punto 6:** con $I' = I/2$ y $\omega' = 2\omega$ en cada eje, $I'\omega' = I\omega$, por lo que $L_{total}$ tiene el mismo valor antes y después.

**Resultados de este punto:**

| Variante | $L_1$ (kg·m²/s) | $L_2$ (kg·m²/s) | $L_{total} = L_1 - L_2$ (kg·m²/s) |
|---|---|---|---|
| **A — principal** (con rodamientos) | ≈ 9,19 | ≈ 4,97 | **≈ 4,22** |
| B — alternativa (eje + engranaje) | ≈ 9,16 | ≈ 4,80 | ≈ 4,36 |

### Punto 8: Potencia del mecanismo en HP

**Planteo:** la potencia de rotación es $P = T\cdot\omega$ (sección 5) o, usando $T = I\alpha$, $P = I\,\omega\,\alpha$ (sección 6). La consigna pide considerar el momento de inercia del "conjunto engranaje y eje" (variante B: sin rodamientos; es la única aclaración explícita de la consigna sobre qué entra en $I$). El torque sale de la fuerza tangencial $F = 200$ N aplicada en el punto de contacto entre engranajes (pág. 15 del apunte de Abud). Las velocidades son las del estado inicial (Punto 1, $n_1 = 2800$ RPM), no las del Punto 6.

**Paso 1 — torque en cada eje** ($F$ es tangencial, perpendicular al radio: $\sin\theta = 1$, sección 1):

$$T_1 = F\,R_1 = 200 \cdot 0{,}125 = 25 \text{ N}\cdot\text{m} \qquad\qquad T_2 = F\,R_2 = 200 \cdot 0{,}1 = 20 \text{ N}\cdot\text{m}$$

**Paso 2 — aceleración angular** ($\alpha = T/I$, con $I^{(B)}$ del Punto 4):

$$\alpha_1 = \frac{25}{3{,}124\times10^{-2}} \approx 800 \text{ rad/s}^2 \qquad\qquad \alpha_2 = \frac{20}{1{,}310\times10^{-2}} \approx 1527 \text{ rad/s}^2$$

**Paso 3 — potencia** ($P = I\,\omega\,\alpha$, con $\omega$ en rad/s del Punto 1):

$$P_1 = (3{,}124\times10^{-2})(293{,}2)(800{,}2) \approx 7330 \text{ W} \qquad\qquad P_2 = (1{,}310\times10^{-2})(366{,}5)(1527) \approx 7330 \text{ W}$$

*(Unidad: $\text{kg}\cdot\text{m}^2 \cdot \text{rad/s} \cdot \text{rad/s}^2 = \text{N}\cdot\text{m}/\text{s} = \text{W} = \text{J/s}$; el radián es adimensional.)*

**El momento de inercia se cancela:** como $I\,\alpha = T$, resulta $P = I\,\omega\,\alpha = T\,\omega$. Considerar $I$ sirve para obtener $\alpha$, pero **no modifica $P$**: el resultado es el mismo con las variantes A o B.

**Verificación cruzada** ($P = F\cdot v_{contacto}$, con $v_{contacto} \approx 36{,}65$ m/s del Punto 1):

$$P = 200 \cdot 36{,}65 \approx 7330 \text{ W} \qquad T_1\omega_1 = 25 \cdot 293{,}2 \approx 7330 \text{ W} \qquad T_2\omega_2 = 20 \cdot 366{,}5 \approx 7330 \text{ W} \quad \checkmark$$

Ambos ejes transmiten la misma potencia (engrane ideal, sin pérdidas), como corresponde.

**Conversión a HP** (con $1\text{ HP} = 745{,}8$ J/s del enunciado):

$$P = \frac{7330 \text{ J/s}}{745{,}8 \text{ J/s por HP}} \approx \boxed{9{,}83 \text{ HP}}$$

*Salvedad sobre $\alpha$:* $\alpha_1 R_1 \neq \alpha_2 R_2$ (≈ 100 vs ≈ 153 m/s²), es decir, esas aceleraciones no cumplen la condición de engrane. Tomar $F$ como único torque sobre cada eje de forma independiente es la lectura simple de la consigna; por eso los valores de $\alpha$ son orientativos. La potencia, en cambio, no depende de $\alpha$ y queda bien determinada por $P = F\cdot v_{contacto}$.

**Resultados de este punto:**

| Eje | $T$ (N·m) | $\omega$ (rad/s) | $P = T\,\omega$ (W) | $P$ (HP) |
|---|---|---|---|---|
| 1 | 25 | ≈ 293,2 | ≈ 7330 | ≈ 9,83 |
| 2 | 20 | ≈ 366,5 | ≈ 7330 | ≈ 9,83 |

---

*Documento generado a partir de "UTN – FRBA – Apunte Teórico – Mecánica Rotacional" (Ing. Mecánica I, Ciclo 2018) y del proceso de resolución del ejercicio de aplicación (págs. 14-15).*
