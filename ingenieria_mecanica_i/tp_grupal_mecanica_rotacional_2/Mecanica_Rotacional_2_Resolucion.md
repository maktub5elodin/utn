# TP Mecánica Rotacional 2 — Eje sobre rodamientos de rodillos cilíndricos

Segundo ejercicio de aplicación de mecánica rotacional (docente Abud), planteado en el pizarrón. Reutiliza la teoría y las convenciones del primer TP (`../tp_grupal_mecanica_rotacional/Mecanica_Rotacional_Apuntes.md`): unidades en mm / kg·mm² con conversión explícita a SI, `ω = 2πn/60`, Steiner, etc.

La diferencia principal con el TP anterior es el tipo de rodamiento: allá eran **rígidos de una hilera de bolas (SKF serie 62)**; acá son **de una hilera de rodillos cilíndricos (SKF serie NU 10)**.

---

## 1. Enunciado

### 1.1 Esquema (transcripción del pizarrón)

```
                                                     F = 500 N
                                              ┌────────►
                                              │
                ┌──┐                  ┌──┐    │
                │▒▒│ rodamiento       │▒▒│    │ 400 mm
                │▒▒│                  │▒▒│    │
                ├──┼──────────────────┼──┤ ┬  │
   ─ · ─ · ─ · ─│· ·│· ─ · ─ · ─ · ─ ·│· ·│─┼──┴── eje de giro
                ├──┼──────────────────┼──┤ ┴ 25 mm (diámetro del eje)
                │▒▒│                  │▒▒│
                │▒▒│ rodamiento       │▒▒│
                └──┘                  └──┘
                ├──────── 500 mm ────────┤

   Eje de acero montado sobre rodamientos de rodillos cilíndricos
   n = 1400 RPM
```

### 1.2 Datos

| Dato | Valor | Observación |
|---|---|---|
| Material del eje | Acero | $\delta_{Acero} = 7{,}85$ g/cm³ (mismo valor que el TP 1) |
| Diámetro del eje | 25 mm | cota vertical que abarca el espesor del eje |
| Largo del eje | 500 mm | cota entre caras exteriores de los rodamientos |
| Velocidad de giro | $n = 1400$ RPM | |
| Fuerza | $F = 500$ N | aplicada a 400 mm del eje de giro |
| Rodamientos | SKF, una hilera de rodillos cilíndricos, serie NU 10 | tabla en `rodamientos.jpeg` (Anexo A) |

### 1.3 Consigna — "Determinar y calcular"

1. Selección de rodamientos
2. Calcular el momento de inercia de los rodillos respecto de la pista
3. Velocidades en los puntos característicos del rodillo ($v_P$ en el contacto con la pista, $v_{CM}$ en el centro, $v_Q$ en el punto superior)
4. Potencia del mecanismo
5. Aceleración angular del mecanismo
6. Momento de la cantidad de movimiento del mecanismo
7. ¿Cuánto vale la energía cinética de cada rodillo?

---

## 2. Resolución

### Punto 1: Selección de rodamientos

**Criterio:** el rodamiento se monta con su aro interior sobre el eje, así que el **diámetro interior** $d$ del rodamiento tiene que ser igual al diámetro del eje. Es el mismo criterio del TP 1, donde el eje de 25 mm llevaba el 6205 y el de 35 mm el 6207.

$$d_{rodamiento} = \varnothing_{eje} = 25\ \text{mm}$$

En la tabla de la serie NU 10 hay **una sola** fila con $d = 25$ mm, que es la primera de la serie (y además es una de las que Abud marcó con círculo en la hoja):

$$\boxed{\text{Rodamiento seleccionado: SKF NU 1005}\quad(\text{dos unidades, una en cada apoyo})}$$

**Datos del NU 1005 que se usan en los puntos siguientes:**

| Magnitud | Valor |
|---|---|
| Diámetro interior $d$ | 25 mm |
| Diámetro exterior $D$ | 47 mm |
| Ancho $B$ | 12 mm |
| Diámetro de pista interior $F$ | 30,5 mm |
| Masa | 0,084 kg |
| $C$ dinámica | 1180 kgf ≈ 11 576 N |
| $C_0$ estática | 640 kgf ≈ 6 278 N |
| $n$ máx | 16 000 rpm |

**Verificaciones:**

1. **Velocidad:** $n = 1400$ RPM ≪ $n_{máx} = 16\,000$ rpm (trabaja a menos del 9 % del límite). ✔
2. **Carga:** aunque toda la fuerza $F = 500$ N ≈ 51 kgf cargara un solo rodamiento, queda muy por debajo de $C_0 = 640$ kgf (más de 12 veces). La verificación es cualitativa: el enunciado no da la distancia del punto de aplicación de $F$ al rodamiento más cercano, así que no se pueden calcular las reacciones en cada apoyo. Con un margen de ese tamaño la conclusión no cambia. ✔
3. **Tipo de carga:** el NU no admite carga axial (Anexo A). Por eso $F$ se interpreta como **fuerza tangencial a 400 mm del eje**, que genera un par sobre el eje ($T = F \cdot 0{,}4$ m, se usa en el Punto 4) y no empuja a lo largo del eje. En el pizarrón la flecha está dibujada horizontal en la vista lateral, pero esa lectura literal (fuerza axial) sería incompatible con el rodamiento elegido.

> **Sobre la elección de la serie:** la serie (NU 10) la fija el enunciado; lo único que se "selecciona" es el tamaño dentro de la serie, y lo determina el diámetro del eje. Las verificaciones de velocidad y carga no eligen el rodamiento, solo confirman que el que corresponde por diámetro sirve.

### Punto 2: Momento de inercia de los rodillos respecto de la pista

**Modelo:** cada rodillo es un **cilindro macizo de acero** que rueda sin deslizar sobre la pista del aro interior. Gira alrededor de su propio eje y al mismo tiempo la línea donde toca la pista está instantáneamente quieta. "Respecto de la pista" significa respecto de esa **línea de contacto** (punto $P$ del Punto 3), no respecto del centro del rodillo.

> Este modelo sigue el croquis del pizarrón: un rodillo sobre una pista, con $v_P$ abajo, $v_{CM}$ en el centro y $v_Q$ arriba. Cuál de las dos pistas está quieta (en el montaje real gira el aro interior con el eje y el exterior queda fijo en el alojamiento) importa para las velocidades del Punto 3. **No cambia este punto:** las dos líneas de contacto están a la misma distancia $r$ del centro del rodillo, así que el $I_P$ es el mismo.

```
        sección del NU 1005 (mitad superior, medidas radiales desde el eje del árbol)

   r = 23,50 ─────────────────────────────  D/2   borde exterior del aro exterior
              ░░░░ aro exterior ░░░░░░░░░░         espesor 2,75 (supuesto)
   r = 20,75 ──────────┬──────────────────  E/2   pista exterior
                    ╱  Q  ╲
                   │   •   │  ← rodillo, Ø 5,5 ; centro a r = 18,00
                    ╲  P  ╱
   r = 15,25 ──────────┴──────────────────  F/2   pista interior (dato de catálogo)
              ▓▓▓▓ aro interior ▓▓▓▓▓▓▓▓▓         espesor 2,75
   r = 12,50 ─────────────────────────────  d/2   agujero = eje de 25 mm
```

#### 2.1 Geometría del rodillo

**Largo** (criterio dado por Abud en clase: 90 % del ancho del rodamiento):

$$l = 0{,}9\cdot B = 0{,}9\cdot 12 = 10{,}8\ \text{mm}$$

**Diámetro** (no lo da el catálogo ni el enunciado, así que se estima con las medidas del catálogo):

- Espacio radial total entre agujero y borde exterior: $\dfrac{D - d}{2} = \dfrac{47 - 25}{2} = 11$ mm.
- Espesor del aro interior bajo la pista (dato real, porque el catálogo da $F$): $\dfrac{F - d}{2} = \dfrac{30{,}5 - 25}{2} = 2{,}75$ mm.
- **Supuesto:** el aro exterior tiene el mismo espesor que el interior (2,75 mm). Con eso, el diámetro de la pista exterior queda en $E = D - 2\cdot 2{,}75 = 41{,}5$ mm.
- El rodillo ocupa el hueco entre las dos pistas:

$$D_w = \frac{E - F}{2} = \frac{41{,}5 - 30{,}5}{2} = 5{,}5\ \text{mm} \quad\Rightarrow\quad r = 2{,}75\ \text{mm}$$

> **⚠ Supuesto a confirmar:** el diámetro de 5,5 mm sale de suponer aros de igual espesor. Si Abud indica otro valor, solo cambia $r$ y se recalcula con las mismas fórmulas.

#### 2.2 Masa del rodillo

Con el mismo criterio de unidades del TP 1 (mm y $\delta_{Acero} = 7{,}85\times10^{-6}$ kg/mm³):

$$V = \pi r^2 l = \pi\cdot 2{,}75^2\cdot 10{,}8 = 256{,}59\ \text{mm}^3$$

$$m = \delta\cdot V = 7{,}85\times10^{-6}\cdot 256{,}59 = 2{,}014\times10^{-3}\ \text{kg} \approx 2{,}01\ \text{g}$$

Acá la masa sale de densidad × volumen y no de catálogo, a diferencia del TP 1. Allá el catálogo daba la masa de todo el rodamiento, pero acá interesa un rodillo solo, y el rodillo sí es una pieza maciza.

#### 2.3 Momento de inercia

**Respecto de su propio eje** (centro de masa, cilindro macizo):

$$I_{CM} = \frac{1}{2} m r^2 = \frac{1}{2}\cdot 2{,}014\times10^{-3}\cdot 2{,}75^2 = 7{,}616\times10^{-3}\ \text{kg}\cdot\text{mm}^2$$

**Respecto de la línea de contacto con la pista** (Steiner, con $h = r$ porque la línea de contacto está a un radio del centro):

$$I_P = I_{CM} + m r^2 = \frac{1}{2} m r^2 + m r^2 = \frac{3}{2} m r^2$$

$$I_P = \frac{3}{2}\cdot 2{,}014\times10^{-3}\cdot 2{,}75^2 = 2{,}285\times10^{-2}\ \text{kg}\cdot\text{mm}^2$$

Conversión a SI ($\text{kg}\cdot\text{mm}^2 = 10^{-6}\ \text{kg}\cdot\text{m}^2$):

$$\boxed{I_P \approx 2{,}285\times10^{-2}\ \text{kg}\cdot\text{mm}^2 = 2{,}285\times10^{-8}\ \text{kg}\cdot\text{m}^2\quad(\text{por rodillo})}$$

> **Lectura:** el término de Steiner ($m r^2$) es el doble de $I_{CM}$, así que respecto de la pista el rodillo "pesa" tres veces más en rotación que respecto de su centro. Este $I_P$ es el que corresponde a un cuerpo que rueda: girar alrededor de la línea de contacto equivale a la suma de girar sobre sí mismo y avanzar (se aprovecha en el Punto 7, $E_c = \tfrac{1}{2} I_P\,\omega_{rodillo}^2$).

| Magnitud | Valor |
|---|---|
| Largo $l$ | 10,8 mm (0,9·B, criterio Abud) |
| Radio $r$ | 2,75 mm (estimado, ver supuesto) |
| Masa $m$ | 2,014 g |
| $I_{CM}$ | $7{,}616\times10^{-3}$ kg·mm² |
| $I_P$ (respecto de la pista) | $2{,}285\times10^{-2}$ kg·mm² = $2{,}285\times10^{-8}$ kg·m² |

### Punto 3: Velocidades en los puntos característicos del rodillo

**Montaje:** el aro exterior está fijo en el alojamiento y es la **pista** sobre la que rueda el rodillo. El aro interior gira solidario con el eje a $n = 1400$ RPM y arrastra a los rodillos. Se supone **rodadura sin deslizamiento en los dos contactos**.

**Puntos característicos** (los del croquis del pizarrón, sobre la línea radial que pasa por el centro del rodillo):

- $P$ — contacto con la **pista** (aro exterior fijo, a $R_e = E/2 = 20{,}75$ mm del eje del árbol).
- $CM$ — centro del rodillo (a $R_c = 18{,}00$ mm).
- $Q$ — punto opuesto a $P$, contacto con el **aro interior** (a $R_i = F/2 = 15{,}25$ mm).

```
        vista frontal, un rodillo (medidas radiales desde el eje del árbol)

   ░░░░░░░░░░ aro exterior FIJO (pista) ░░░░░░░░░░
   R = 20,75 ─────────────── P ───────────────     v_P  = 0
                           ╱   ╲
   R = 18,00              │ CM  ●──►               v_CM = 1,118 m/s
                           ╲   ╱
   R = 15,25 ─────────────── Q ─────────►          v_Q  = 2,236 m/s
   ▓▓▓▓▓▓▓▓▓▓ aro interior, gira con el eje ▓▓▓▓▓▓
                         ↻ ω_eje

   Perfil de velocidades sobre el diámetro PQ: lineal, nulo en P
   (centro instantáneo de rotación) y máximo en Q.
```

En el croquis del pizarrón la pista está abajo y $Q$ arriba. Acá la figura está "dada vuelta" porque la pista quieta es la de afuera, pero la relación es la misma: $P$ es el punto quieto y $Q$ el más rápido, a una distancia $2r$ de $P$.

#### 3.1 Velocidad angular del eje

$$\omega_{eje} = \frac{2\pi n}{60} = \frac{2\pi\cdot 1400}{60} = 146{,}61\ \text{rad/s}$$

#### 3.2 Velocidad en $Q$ (contacto con el aro interior)

Sin deslizamiento, $Q$ tiene la misma velocidad que el punto del aro interior que está tocando:

$$v_Q = \omega_{eje}\cdot R_i = 146{,}61\cdot 15{,}25 = 2235{,}8\ \text{mm/s} \approx 2{,}236\ \text{m/s}$$

#### 3.3 Velocidad en $P$ (contacto con la pista)

Sin deslizamiento sobre un aro que no se mueve:

$$v_P = 0$$

$P$ es el **centro instantáneo de rotación** del rodillo: en cada instante el rodillo gira alrededor de la línea de contacto con la pista. Por eso en el Punto 2 el momento de inercia se tomó respecto de esa línea.

#### 3.4 Velocidad del centro $CM$

El perfil de velocidades sobre $PQ$ es lineal desde $P$. $CM$ está a $r$ de $P$ y $Q$ a $2r$, así que:

$$v_{CM} = \frac{v_Q}{2} = \frac{2235{,}8}{2} = 1117{,}9\ \text{mm/s} \approx 1{,}118\ \text{m/s}$$

#### 3.5 Velocidad angular del rodillo

Con centro instantáneo en $P$:

$$\omega_{rodillo} = \frac{v_{CM}}{r} = \frac{v_Q}{2r} = \frac{2235{,}8}{5{,}5} = 406{,}5\ \text{rad/s}$$

El rodillo gira en **sentido contrario** al eje: su punto interior ($Q$) avanza con el aro interior y su punto exterior ($P$) queda quieto. Esta $\omega_{rodillo}$ es la absoluta (respecto del piso) y es la que se usa en el Punto 7 con $I_P$.

#### 3.6 Resultado

| Punto | Distancia a $P$ | Velocidad | Dirección |
|---|---|---|---|
| $P$ (contacto con la pista, aro exterior) | 0 | $v_P = 0$ | — |
| $CM$ (centro del rodillo) | $r = 2{,}75$ mm | $v_{CM} \approx 1{,}118$ m/s | tangencial, mismo sentido que el eje |
| $Q$ (contacto con el aro interior) | $2r = 5{,}5$ mm | $v_Q \approx 2{,}236$ m/s | tangencial, mismo sentido que el eje |

$$\boxed{v_P = 0 \qquad v_{CM} \approx 1{,}118\ \text{m/s} \qquad v_Q = 2\,v_{CM} \approx 2{,}236\ \text{m/s}}$$

> **Consecuencias que conviene tener a mano:**
>
> - **La jaula gira más lento que el eje.** El centro del rodillo describe una circunferencia de radio $R_c = 18$ mm, así que la jaula gira a $\omega_{jaula} = v_{CM}/R_c = 1117{,}9/18 = 62{,}1$ rad/s, que son unas **593 RPM**, el 42 % de la velocidad del eje. Coincide con la fórmula de catálogo $n_{jaula} = \tfrac{n}{2}\left(1 - \tfrac{D_w}{d_m}\right) = 700\cdot\left(1 - \tfrac{5{,}5}{36}\right) = 593$ RPM, con $d_m = 36$ mm el diámetro primitivo.
> - **Velocidad del eje y velocidad del rodillo no son lo mismo.** $\omega_{rodillo} = 406{,}5$ rad/s es casi 3 veces $\omega_{eje}$, porque el rodillo es mucho más chico que la pista interior que lo arrastra.
> - **Qué depende del diámetro estimado.** Las tres velocidades $v_P$, $v_{CM}$ y $v_Q$ salen solo de $n$ y de $F$, que es dato de catálogo, así que no dependen del supuesto del Punto 2. En cambio $\omega_{rodillo}$ y $\omega_{jaula}$ sí dependen del diámetro del rodillo, que es estimado.

### Punto 4: Potencia del mecanismo

**Planteo:** como en el Punto 8 del TP 1, la potencia sale del par aplicado y de la velocidad angular, sin pasar por el momento de inercia:

$$P = T\cdot\omega$$

**Par sobre el eje:** $F = 500$ N tangencial, aplicada a 400 mm del eje de giro (interpretación del Punto 1, observación 3):

$$T = F\cdot R = 500\ \text{N}\cdot 400\ \text{mm} = 200\,000\ \text{N}\cdot\text{mm} = 200\ \text{N}\cdot\text{m}$$

Como en el TP 1, $R$ en mm da $T$ en N·mm, y se pasa a N·m dividiendo por 1000.

**Velocidad angular** (Punto 3.1):

$$\omega_{eje} = 146{,}61\ \text{rad/s}$$

**Potencia:**

$$P = 200\ \text{N}\cdot\text{m}\cdot 146{,}61\ \text{rad/s} = 29\,321{,}5\ \text{W} \approx 29{,}32\ \text{kW}$$

Conversión a HP, con el mismo factor del TP 1 ($1\ \text{HP} = 745{,}8$ J/s):

$$P = \frac{29\,321{,}5}{745{,}8} \approx 39{,}32\ \text{HP}$$

$$\boxed{P \approx 29{,}32\ \text{kW} \approx 39{,}3\ \text{HP}}$$

> **Por qué no interviene el momento de inercia:** $P = T\cdot\omega$ es la potencia que entra al eje por el par $F\cdot R$ girando a 1400 RPM. Es el equivalente rotacional de $P = F\cdot v$ en traslación. Los momentos de inercia (eje, rodillos) entran en el Punto 5 (cuánto acelera ese par al conjunto) y en el Punto 6 ($L = I\,\omega$), pero no en la potencia.
>
> **Referencia de tamaño:** 39 HP para un eje de 25 mm a 1400 RPM es bastante. Equivale a un motor eléctrico industrial mediano. Los rodamientos igual quedan holgados (Punto 1), porque el par lo transmite el eje y no carga a los rodamientos. A los rodamientos solo les llegan las fuerzas radiales.

### Punto 5: Aceleración angular del mecanismo

**Planteo:** segunda ley de Newton para la rotación:

$$T = I\,\alpha \quad\Rightarrow\quad \alpha = \frac{T}{I_{mecanismo}}$$

**Criterio para $I_{mecanismo}$:** el mismo del TP 1, el **conjunto rotante completo**. Acá es el eje más los dos rodamientos, y cada rodamiento se toma **como una sola pieza** (un anillo entre $d$ y $D$) con la masa de catálogo. Esa masa ya incluye aros, rodillos y jaula, así que **no hace falta saber cuántos rodillos tiene** (lo confirmó Abud). Los rodillos individuales se estudian aparte (puntos 2, 3 y 7) y no se suman acá.

No se incluye la pieza que lleva la fuerza a 400 mm (brazo, polea o manivela) porque el enunciado no da sus medidas ni su masa.

#### 5.1 Momento de inercia del eje

Cilindro macizo de acero, $\varnothing 25$ mm ($R = 12{,}5$ mm), largo $L = 500$ mm:

$$V = \pi R^2 L = \pi\cdot 12{,}5^2\cdot 500 = 245\,437\ \text{mm}^3$$

$$m_{eje} = 7{,}85\times10^{-6}\cdot 245\,437 = 1{,}927\ \text{kg}$$

$$I_{eje} = \frac{1}{2} m R^2 = \frac{1}{2}\cdot 1{,}927\cdot 12{,}5^2 = 150{,}52\ \text{kg}\cdot\text{mm}^2$$

#### 5.2 Momento de inercia de cada rodamiento (NU 1005)

Anillo grueso con la masa de catálogo, $R_{int} = d/2 = 12{,}5$ mm, $R_{ext} = D/2 = 23{,}5$ mm:

$$I_{rod} = \frac{1}{2} m\left(R_{ext}^2 + R_{int}^2\right) = \frac{1}{2}\cdot 0{,}084\cdot\left(23{,}5^2 + 12{,}5^2\right) = 29{,}76\ \text{kg}\cdot\text{mm}^2$$

#### 5.3 Momento de inercia del mecanismo

$$I_{mecanismo} = I_{eje} + 2\,I_{rod} = 150{,}52 + 2\cdot 29{,}76 = 210{,}04\ \text{kg}\cdot\text{mm}^2$$

Conversión a SI:

$$I_{mecanismo} = 210{,}04\times10^{-6} = 2{,}100\times10^{-4}\ \text{kg}\cdot\text{m}^2$$

Los dos rodamientos aportan el 28 % del total, aunque son mucho más livianos que el eje (0,168 kg contra 1,927 kg). Pesan más de lo que su masa sugiere porque su material está lejos del eje de giro, y en $I$ la distancia va al cuadrado.

#### 5.4 Aceleración angular

$$\alpha = \frac{T}{I_{mecanismo}} = \frac{200\ \text{N}\cdot\text{m}}{2{,}100\times10^{-4}\ \text{kg}\cdot\text{m}^2} \approx 9{,}52\times10^{5}\ \text{rad/s}^2$$

$$\boxed{\alpha \approx 9{,}52\times10^{5}\ \text{rad/s}^2}$$

> **Cómo leer este número:** es la aceleración que tendría el conjunto si el par de 200 N·m actuara **solo**, sin ninguna carga que se le oponga. Con esa $\alpha$, el eje llegaría a $\omega = 146{,}6$ rad/s (1400 RPM) en $t = \omega/\alpha \approx 0{,}15$ ms. Es enorme porque el rotor es muy liviano para un par tan grande. En funcionamiento normal, a 1400 RPM constantes, el par motor está equilibrado por el par de la carga que se acciona, el par neto es cero y $\alpha = 0$.
>
> **Simplificación del criterio:** al tomar el rodamiento entero como si girara con el eje, se cuentan como si giraran a $\omega_{eje}$ el aro exterior (que está fijo) y los rodillos (que giran a otra velocidad, Punto 3). Por eso el 28 % que aportan los rodamientos está sobreestimado, y $\alpha$ real sería algo mayor. Es la misma simplificación del TP 1, se adopta por coherencia con ese criterio y porque evita depender de la cantidad de rodillos.

### Punto 6: Momento de la cantidad de movimiento del mecanismo

**Planteo:** momento angular (cantidad de movimiento rotacional) de un cuerpo que gira alrededor de un eje fijo:

$$L = I\,\omega$$

Se usa el mismo $I_{mecanismo}$ del Punto 5 (eje + 2 rodamientos, en SI) y la velocidad angular del eje (Punto 3.1):

$$L = 2{,}100\times10^{-4}\ \text{kg}\cdot\text{m}^2\cdot 146{,}61\ \text{rad/s} = 3{,}079\times10^{-2}\ \text{kg}\cdot\text{m}^2/\text{s}$$

$$\boxed{L \approx 3{,}08\times10^{-2}\ \text{kg}\cdot\text{m}^2/\text{s}}$$

**Dirección:** $L$ es un vector sobre el eje de giro del árbol, con el sentido que da la regla de la mano derecha según el sentido de giro.

> **Relación con el Punto 5:** el par es la variación del momento angular en el tiempo, $T = \dfrac{dL}{dt} = I\,\alpha$. A 1400 RPM constantes, $L$ no cambia, porque el par neto es cero (el par motor está equilibrado por el de la carga). Si actuara solo el par de 200 N·m, $L$ crecería a razón de 200 kg·m²/s por segundo. Por eso llegaría a este valor de $L$ en $3{,}08\times10^{-2}/200 \approx 0{,}15$ ms, el mismo tiempo que se obtuvo en el Punto 5.
>
> Como en el Punto 5, el valor arrastra la simplificación del criterio: el aro exterior y los rodillos se cuentan como si giraran a $\omega_{eje}$, así que el aporte de los rodamientos está sobreestimado.

### Punto 7: Energía cinética de cada rodillo

**Planteo:** el rodillo gira alrededor de la línea de contacto con la pista ($P$, centro instantáneo de rotación, Punto 3.3), así que su energía cinética se calcula como una rotación pura alrededor de $P$:

$$E_c = \frac{1}{2} I_P\,\omega_{rodillo}^2$$

Con $I_P$ del Punto 2 (en SI) y $\omega_{rodillo}$ del Punto 3.5:

$$E_c = \frac{1}{2}\cdot 2{,}285\times10^{-8}\ \text{kg}\cdot\text{m}^2\cdot\left(406{,}5\ \text{rad/s}\right)^2 = 1{,}888\times10^{-3}\ \text{J}$$

$$\boxed{E_c \approx 1{,}89\times10^{-3}\ \text{J} \approx 1{,}89\ \text{mJ}\quad(\text{por rodillo})}$$

**Verificación, separando traslación y rotación:** la misma energía se puede calcular como la del centro de masa que avanza más la del rodillo girando sobre sí mismo.

$$E_c = \underbrace{\frac{1}{2} m\,v_{CM}^2}_{\text{traslación}} + \underbrace{\frac{1}{2} I_{CM}\,\omega_{rodillo}^2}_{\text{rotación propia}}$$

$$E_{c,tras} = \frac{1}{2}\cdot 2{,}014\times10^{-3}\cdot 1{,}118^2 = 1{,}259\times10^{-3}\ \text{J}$$

$$E_{c,rot} = \frac{1}{2}\cdot 7{,}616\times10^{-9}\cdot 406{,}5^2 = 0{,}629\times10^{-3}\ \text{J}$$

$$E_c = 1{,}259\times10^{-3} + 0{,}629\times10^{-3} = 1{,}888\times10^{-3}\ \text{J}\ \checkmark$$

| Parte | Energía (mJ) | Proporción |
|---|---|---|
| Traslación del centro ($\tfrac{1}{2} m v_{CM}^2$) | 1,259 | 2/3 |
| Rotación propia ($\tfrac{1}{2} I_{CM}\omega^2$) | 0,629 | 1/3 |
| **Total** ($\tfrac{1}{2} I_P\omega^2$) | **1,888** | 1 |

> **Por qué 2/3 y 1/3:** en un cilindro macizo que rueda sin deslizar, $I_{CM} = \tfrac{1}{2} m r^2$ y $v_{CM} = \omega r$, así que la rotación propia siempre vale la mitad que la traslación. Es el mismo reparto que en el Punto 2, donde el término de Steiner ($m r^2$) era el doble de $I_{CM}$.
>
> **Dependencia del supuesto:** $v_{CM}$ no depende del supuesto, porque sale de $n$ y de $F$. En cambio la masa, $I_P$ y $\omega_{rodillo}$ dependen del diámetro estimado del rodillo (5,5 mm, Punto 2), así que este resultado también depende de ese supuesto.
>
> **Comparación de escala:** la energía cinética del mecanismo es $\tfrac{1}{2} I_{mecanismo}\,\omega_{eje}^2 = \tfrac{1}{2}\cdot 2{,}100\times10^{-4}\cdot 146{,}61^2 \approx 2{,}26$ J. Un rodillo solo tiene menos del 0,1 % de esa energía.

---

## Anexo A — Tabla SKF: rodamientos de una hilera de rodillos cilíndricos, serie NU 10

Transcripción de `rodamientos.jpeg` (catálogo SKF, pág. 69). Copia legible; en la hoja original están marcados con círculo los diámetros $d$ = 25, 30, 35 y 60 mm.

Designación: `NU 10` + número de tamaño (ej. tamaño `05` → `NU 1005`). Igual que en la serie 62, para $d \geq 20$ mm el número de tamaño es $d/5$.

> **► Rodamiento seleccionado (Punto 1): SKF NU 1005** ($d = 25$ mm = diámetro del eje). Su fila va destacada en negrita en la tabla.

| Rodamiento | Peso (kg) | d (mm) | D (mm) | B (mm) | r (mm) | r₁ (mm) | F (mm) | C dinámica (kg) | C₀ estática (kg) | n máx (rpm) |
|---|---|---|---|---|---|---|---|---|---|---|
| **► NU 1005** | **0,084** | **25** | **47** | **12** | **1** | **0,5** | **30,5** | **1180** | **640** | **16000** |
| NU 1006 | 0,121 | 30 | 55 | 13 | 1,5 | 0,8 | 36,5 | 1460 | 850 | 13000 |
| NU 1007 | 0,182 | 35 | 62 | 14 | 1,5 | 0,8 | 42 | 1930 | 1140 | 13000 |
| NU 1008 | 0,223 | 40 | 68 | 15 | 1,5 | 1 | 47 | 2160 | 1370 | 10000 |
| NU 1009 | 0,289 | 45 | 75 | 16 | 1,5 | 1 | 52,5 | 2700 | 1760 | 10000 |
| NU 1010 | 0,306 | 50 | 80 | 16 | 1,5 | 1 | 57,5 | 2700 | 1760 | 8000 |
| NU 1011 | 0,445 | 55 | 90 | 18 | 2 | 1,5 | 64,5 | 3150 | 2160 | 8000 |
| NU 1012 | 0,477 | 60 | 95 | 18 | 2 | 1,5 | 69,5 | 3250 | 2280 | 8000 |
| NU 1013 | 0,506 | 65 | 100 | 18 | 2 | 1,5 | 74,5 | 3250 | 2400 | 8000 |
| NU 1014 | 0,702 | 70 | 110 | 20 | 2 | 1,5 | 80 | 4900 | 3450 | 6000 |
| NU 1015 | 0,735 | 75 | 115 | 20 | 2 | 1,5 | 85 | 5000 | 3650 | 6000 |
| NU 1016 | 0,994 | 80 | 125 | 22 | 2 | 1,5 | 91,5 | 6100 | 4500 | 6000 |
| NU 1017 | 1,04 | 85 | 130 | 22 | 2 | 1,5 | 96,5 | 6300 | 4750 | 5000 |
| NU 1018 | 1,34 | 90 | 140 | 24 | 2,5 | 2 | 103 | 7500 | 5700 | 5000 |
| NU 1019 | 1,40 | 95 | 145 | 24 | 2,5 | 2 | 108 | 7650 | 6000 | 5000 |
| NU 1020 | 1,46 | 100 | 150 | 24 | 2,5 | 2 | 113 | 7800 | 6200 | 4000 |
| NU 1022 | 2,31 | 110 | 170 | 28 | 3 | 2 | 125 | 11400 | 9000 | 4000 |
| NU 1024 | 2,47 | 120 | 180 | 28 | 3 | 2 | 135 | 12200 | 10000 | 3000 |
| NU 1026 | 3,77 | 130 | 200 | 33 | 3 | 2 | 148 | 15000 | 12500 | 3000 |
| NU 1028 | 4,00 | 140 | 210 | 33 | 3 | 2 | 158 | 16000 | 13700 | 3000 |
| NU 1030 | 4,83 | 150 | 225 | 35 | 3,5 | 2,5 | 169,5 | 17300 | 15300 | 2500 |
| NU 1032 | 5,93 | 160 | 240 | 38 | 3,5 | 2,5 | 180 | 20800 | 18300 | 2500 |
| NU 1034 | 7,90 | 170 | 260 | 42 | 3,5 | 3,5 | 193 | 25000 | 22000 | 2500 |
| NU 1036 | 10,5 | 180 | 280 | 46 | 3,5 | 3,5 | 205 | 31500 | 27500 | 2000 |
| NU 1038 | 10,9 | 190 | 290 | 46 | 3,5 | 3,5 | 215 | 32500 | 29000 | 2000 |
| NU 1040 | 14,1 | 200 | 310 | 51 | 3,5 | 3,5 | 229 | 35500 | 32500 | 2000 |

**Significado de las columnas** (según el croquis del catálogo):

- $d$ — **diámetro interior** (agujero del aro interior, donde calza el eje).
- $D$ — diámetro exterior del aro exterior.
- $B$ — ancho axial.
- $r$, $r_1$ — radios de redondeo de los aros.
- $F$ — **diámetro de la pista del aro interior**, es decir, el diámetro sobre el que apoyan y ruedan los rodillos. Columna nueva respecto de la serie 62 y relevante para los puntos 2, 3 y 7 (el rodillo rueda sobre esa pista).
- $C$, $C_0$ — capacidad básica de carga dinámica y estática, en **kg** (kgf, catálogo antiguo; $1\ \text{kgf} = 9{,}81$ N).
- $n$ — velocidad máxima permitida.

**Notas del catálogo:**

- Desde el NU 1006 en adelante (excepto el NU 1016) se construyen con separador (jaula) macizo de latón.
- Todos, excepto el NU 1005, pueden suministrarse con ranura en el aro exterior (sufijo `N`, ej. `NU 1006 N`).

> **Diferencia de diseño con los de bolas (serie 62):** en el tipo **NU** el aro exterior tiene dos rebordes y el aro interior **no tiene rebordes**. Los rodillos quedan guiados por el aro exterior y el aro interior puede desplazarse axialmente respecto de ellos. Consecuencia práctica: **soporta carga radial (más que uno de bolas del mismo tamaño), pero no carga axial**.

---

## Fuentes

- `ejercicio.jpeg`: foto del pizarrón con el esquema, los datos y las consignas 1 a 7 (Abud).
- `rodamientos.jpeg`: catálogo SKF, "Rodamientos de una hilera de rodillos cilíndricos — Serie NU 10", pág. 69 (material entregado en clase).
- `../tp_grupal_mecanica_rotacional/Mecanica_Rotacional_Apuntes.md` y `Mecanica_Rotacional_Datos.md`: teoría, convenciones de unidades y criterio de selección del TP 1.
