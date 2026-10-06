# TP Mecánica Rotacional 2 — Eje sobre rodamientos de rodillos cilíndricos

Segundo ejercicio de aplicación de mecánica rotacional (docente Abud). Usa la teoría y las convenciones del TP 1 (carpeta `tp_grupal_mecanica_rotacional/`): cálculo en mm y kg·mm² con pasaje explícito a SI, $\omega = 2\pi n/60$, Steiner. La novedad es el rodamiento: allá eran **de bolas (SKF serie 62)**, acá son **de rodillos cilíndricos (SKF serie NU 10)**.

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

| Dato | Valor |
|---|---|
| Material del eje | Acero, $\delta = 7{,}85$ g/cm³ |
| Diámetro del eje | 25 mm |
| Largo del eje | 500 mm (entre caras exteriores de los rodamientos) |
| Velocidad de giro | $n = 1400$ RPM |
| Fuerza | $F = 500$ N, a 400 mm del eje de giro |
| Rodamientos | SKF, una hilera de rodillos cilíndricos, serie NU 10 (catálogo SKF) |

### 1.3 Consigna — "Determinar y calcular"

1. Selección de rodamientos
2. Momento de inercia de los rodillos respecto de la pista
3. Velocidades en los puntos característicos del rodillo ($v_P$, $v_{CM}$, $v_Q$)
4. Potencia del mecanismo
5. Aceleración angular del mecanismo
6. Momento de la cantidad de movimiento del mecanismo
7. Energía cinética de cada rodillo

---

<!-- salto-pagina -->

## 2. Resolución

### Punto 1: Selección de rodamientos

El aro interior calza sobre el eje, así que el **diámetro interior** del rodamiento debe ser igual al del eje ($d = 25$ mm). La serie la fija el enunciado; dentro de ella hay una sola fila con $d = 25$ mm:

$$\boxed{\text{SKF NU 1005}\quad(\text{dos unidades, una por apoyo})}$$

| Magnitud | Valor |
|---|---|
| Diámetro interior $d$ | 25 mm |
| Diámetro exterior $D$ | 47 mm |
| Ancho $B$ | 12 mm |
| Diámetro de pista interior $F$ | 30,5 mm |
| Masa | 0,084 kg |
| $C$ / $C_0$ | 1180 / 640 kgf |
| $n$ máx | 16 000 rpm |

**Verificación rápida:** 1400 RPM ≪ 16 000 rpm, y aun si los 500 N (≈ 51 kgf) cargaran un solo rodamiento, quedan muy por debajo de $C_0 = 640$ kgf. ✔

**Dirección de $F$:** el NU no admite carga axial, así que $F$ se toma **tangencial** a 400 mm del eje: genera un par sobre el eje (Punto 4), no un empuje a lo largo de él.

### Punto 2: Momento de inercia de los rodillos respecto de la pista

**Modelo:** cada rodillo es un **cilindro macizo de acero** que rueda sin deslizar sobre la pista. "Respecto de la pista" significa respecto de la **línea de contacto** $P$, no del centro del rodillo. Como las dos pistas están a la misma distancia $r$ del centro, el resultado no depende de cuál de ellas se tome.

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

**Largo** (criterio Abud, 90 % del ancho): $l = 0{,}9\cdot B = 0{,}9\cdot 12 = 10{,}8$ mm.

**Diámetro** (no lo da el catálogo, se estima): el aro interior tiene un espesor real de $\tfrac{F - d}{2} = 2{,}75$ mm. **Suponiendo** el aro exterior igual de grueso, la pista exterior queda en $E = D - 2\cdot 2{,}75 = 41{,}5$ mm, y el rodillo llena el hueco entre ambas pistas:

$$D_w = \frac{E - F}{2} = \frac{41{,}5 - 30{,}5}{2} = 5{,}5\ \text{mm} \quad\Rightarrow\quad r = 2{,}75\ \text{mm}$$

> **⚠ Supuesto a confirmar con Abud.** Si da otro diámetro, se recalcula con las mismas fórmulas.

#### 2.2 Masa

Un rodillo solo no tiene masa de catálogo, así que sale de densidad × volumen ($\delta = 7{,}85\times10^{-6}$ kg/mm³):

$$m = \delta\,\pi r^2 l = 7{,}85\times10^{-6}\cdot\pi\cdot 2{,}75^2\cdot 10{,}8 = 2{,}014\times10^{-3}\ \text{kg}$$

#### 2.3 Momento de inercia

Respecto del centro (cilindro macizo) y, por Steiner con $h = r$, respecto de la línea de contacto:

$$I_{CM} = \tfrac{1}{2} m r^2 = 7{,}616\times10^{-3}\ \text{kg}\cdot\text{mm}^2 \qquad I_P = I_{CM} + m r^2 = \tfrac{3}{2} m r^2$$

$$\boxed{I_P = \tfrac{3}{2}\cdot 2{,}014\times10^{-3}\cdot 2{,}75^2 = 2{,}285\times10^{-2}\ \text{kg}\cdot\text{mm}^2 = 2{,}285\times10^{-8}\ \text{kg}\cdot\text{m}^2}$$

El término de Steiner duplica a $I_{CM}$: respecto de la pista, el rodillo tiene el triple de inercia que respecto de su centro. Es el $I$ que corresponde a un cuerpo que rueda, y se usa en el Punto 7.

### Punto 3: Velocidades en los puntos característicos del rodillo

**Montaje:** el aro exterior está fijo en el alojamiento (es la **pista**); el aro interior gira con el eje y arrastra a los rodillos. Rodadura sin deslizamiento en ambos contactos.

- $P$: contacto con la pista ($R_e = 20{,}75$ mm del eje del árbol).
- $CM$: centro del rodillo ($R_c = 18{,}00$ mm).
- $Q$: contacto con el aro interior ($R_i = F/2 = 15{,}25$ mm).

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

Respecto del croquis del pizarrón la figura está invertida (la pista quieta es la de afuera), pero la idea es la misma: $P$ quieto, $Q$ el más rápido.

**Velocidad angular del eje:**

$$\omega_{eje} = \frac{2\pi n}{60} = \frac{2\pi\cdot 1400}{60} = 146{,}61\ \text{rad/s}$$

**$Q$** se mueve igual que el aro interior que toca; **$P$** toca un aro quieto; **$CM$**, a mitad de camino entre ambos, tiene la mitad de la velocidad de $Q$ (perfil lineal desde $P$):

$$v_Q = \omega_{eje}\,R_i = 146{,}61\cdot 15{,}25 = 2235{,}8\ \text{mm/s} \qquad v_P = 0 \qquad v_{CM} = \frac{v_Q}{2} = 1117{,}9\ \text{mm/s}$$

$$\boxed{v_P = 0 \qquad v_{CM} \approx 1{,}118\ \text{m/s} \qquad v_Q \approx 2{,}236\ \text{m/s}}$$

$P$ es el **centro instantáneo de rotación**: en cada instante el rodillo gira alrededor de su línea de contacto con la pista (por eso el Punto 2 toma $I$ respecto de ella). Su velocidad angular es:

$$\omega_{rodillo} = \frac{v_{CM}}{r} = \frac{1117{,}9}{2{,}75} = 406{,}5\ \text{rad/s}$$

Gira en sentido contrario al eje y casi 3 veces más rápido, porque es mucho más chico que la pista que lo arrastra. Las velocidades lineales solo dependen de $n$ y de $F$ (catálogo); $\omega_{rodillo}$ depende además del diámetro estimado.

### Punto 4: Potencia del mecanismo

La potencia sale del par y de la velocidad angular — el equivalente rotacional de $P = F\cdot v$ —, sin intervenir el momento de inercia:

$$T = F\cdot R = 500\ \text{N}\cdot 0{,}4\ \text{m} = 200\ \text{N}\cdot\text{m}$$

$$P = T\cdot\omega_{eje} = 200\cdot 146{,}61 = 29\,321{,}5\ \text{W}$$

$$\boxed{P \approx 29{,}32\ \text{kW} \approx 39{,}3\ \text{HP}}\qquad(1\ \text{HP} = 745{,}8\ \text{W, como en el TP 1})$$

### Punto 5: Aceleración angular del mecanismo

$$T = I\,\alpha \quad\Rightarrow\quad \alpha = \frac{T}{I_{mecanismo}}$$

**$I_{mecanismo}$** (mismo criterio que el TP 1): eje + 2 rodamientos, cada rodamiento como **un anillo entre $d$ y $D$ con la masa de catálogo**. Esa masa ya incluye aros, rodillos y jaula, así que no hace falta saber cuántos rodillos tiene.

**Eje** (cilindro macizo, $R = 12{,}5$ mm, $L = 500$ mm):

$$m_{eje} = \delta\,\pi R^2 L = 7{,}85\times10^{-6}\cdot\pi\cdot 12{,}5^2\cdot 500 = 1{,}927\ \text{kg} \qquad I_{eje} = \tfrac{1}{2} m R^2 = 150{,}52\ \text{kg}\cdot\text{mm}^2$$

**Cada rodamiento** (anillo, $R_{int} = 12{,}5$ mm, $R_{ext} = 23{,}5$ mm):

$$I_{rod} = \tfrac{1}{2} m\left(R_{ext}^2 + R_{int}^2\right) = \tfrac{1}{2}\cdot 0{,}084\cdot\left(23{,}5^2 + 12{,}5^2\right) = 29{,}76\ \text{kg}\cdot\text{mm}^2$$

**Total:**

$$I_{mecanismo} = 150{,}52 + 2\cdot 29{,}76 = 210{,}04\ \text{kg}\cdot\text{mm}^2 = 2{,}100\times10^{-4}\ \text{kg}\cdot\text{m}^2$$

Los rodamientos pesan 0,168 kg contra 1,927 kg del eje, pero aportan el 28 % de $I$: su masa está más lejos del eje de giro y en $I$ la distancia va al cuadrado.

$$\boxed{\alpha = \frac{200}{2{,}100\times10^{-4}} \approx 9{,}52\times10^{5}\ \text{rad/s}^2}$$

> **Lectura:** es la aceleración si el par actuara solo, sin carga que se le oponga (llegaría a 1400 RPM en unos 0,15 ms). En régimen, a velocidad constante, el par motor se equilibra con el de la carga y $\alpha = 0$. El criterio cuenta como si giraran con el eje al aro exterior (fijo) y a los rodillos, así que sobreestima un poco $I$.

### Punto 6: Momento de la cantidad de movimiento del mecanismo

Con el mismo $I_{mecanismo}$ y $\omega_{eje}$:

$$\boxed{L = I\,\omega = 2{,}100\times10^{-4}\cdot 146{,}61 \approx 3{,}08\times10^{-2}\ \text{kg}\cdot\text{m}^2/\text{s}}$$

$L$ es un vector sobre el eje de giro, con sentido dado por la regla de la mano derecha. Se vincula con el Punto 5 por $T = dL/dt = I\,\alpha$: a velocidad constante $L$ no cambia.

### Punto 7: Energía cinética de cada rodillo

Como el rodillo gira alrededor de $P$ (centro instantáneo), su energía cinética es la de una rotación pura alrededor de $P$, con $I_P$ (Punto 2) y $\omega_{rodillo}$ (Punto 3):

$$E_c = \tfrac{1}{2} I_P\,\omega_{rodillo}^2 = \tfrac{1}{2}\cdot 2{,}285\times10^{-8}\cdot 406{,}5^2$$

$$\boxed{E_c \approx 1{,}89\times10^{-3}\ \text{J} = 1{,}89\ \text{mJ}\quad(\text{por rodillo})}$$

**Control:** separando el avance del centro y el giro propio se llega a lo mismo,

$$E_c = \underbrace{\tfrac{1}{2} m\,v_{CM}^2}_{1{,}259\ \text{mJ}} + \underbrace{\tfrac{1}{2} I_{CM}\,\omega_{rodillo}^2}_{0{,}629\ \text{mJ}} = 1{,}888\ \text{mJ}\ \checkmark$$

En un cilindro macizo que rueda, la traslación es siempre 2/3 del total y la rotación propia 1/3 (el mismo reparto que $I_P = I_{CM} + 2\,I_{CM}$ del Punto 2).

---

## Resumen de resultados

| Punto | Resultado |
|---|---|
| 1. Rodamiento | SKF NU 1005 (×2) |
| 2. $I_P$ por rodillo | $2{,}285\times10^{-8}$ kg·m² ($r = 2{,}75$ mm estimado, $l = 10{,}8$ mm, $m = 2{,}014$ g) |
| 3. Velocidades | $v_P = 0$; $v_{CM} \approx 1{,}118$ m/s; $v_Q \approx 2{,}236$ m/s; $\omega_{rodillo} = 406{,}5$ rad/s |
| 4. Potencia | $\approx 29{,}32$ kW $\approx 39{,}3$ HP |
| 5. $\alpha$ | $\approx 9{,}52\times10^{5}$ rad/s² ($I_{mecanismo} = 2{,}100\times10^{-4}$ kg·m²) |
| 6. $L$ | $\approx 3{,}08\times10^{-2}$ kg·m²/s |
| 7. $E_c$ por rodillo | $\approx 1{,}89$ mJ |

<!-- solo-md -->

<!-- Anexo A y Fuentes quedan solo en el .md: en el PDF, los datos del NU 1005 ya están en el Punto 1. -->

---

## Anexo A — Tabla SKF: rodamientos de una hilera de rodillos cilíndricos, serie NU 10

Datos de `rodamientos.jpeg` (catálogo SKF, pág. 69).

Transcripción completa de la tabla. En la hoja original están marcados con círculo los diámetros $d$ = 25, 30, 35 y 60 mm.

Designación: `NU 10` + número de tamaño; para $d \geq 20$ mm el número es $d/5$ (ej. $d = 25$ → `NU 1005`).

> **► Rodamiento seleccionado (Punto 1): SKF NU 1005** ($d = 25$ mm = diámetro del eje).

Su fila va destacada en negrita en la tabla.

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

**Magnitudes:** $d$ diámetro interior (donde calza el eje); $D$ diámetro exterior; $B$ ancho; $r$, $r_1$ radios de redondeo; $F$ **diámetro de la pista interior**, sobre la que ruedan los rodillos (no figura en la serie 62); $C$, $C_0$ capacidad de carga dinámica y estática en kgf ($1$ kgf $= 9{,}81$ N); $n$ velocidad máxima.

**Nota del catálogo:** todos, excepto el NU 1005, pueden suministrarse con ranura en el aro exterior (sufijo `N`).

Desde el NU 1006 en adelante (excepto el NU 1016) llevan jaula maciza de latón.

> **Tipo NU frente a los de bolas:** el aro exterior tiene dos rebordes y el interior ninguno, así que el aro interior puede desplazarse axialmente. Resultado: **soporta más carga radial que uno de bolas del mismo tamaño, pero nada de carga axial**.

---

## Fuentes

- `ejercicio.jpeg`: foto del pizarrón con el esquema, los datos y las consignas 1 a 7 (Abud).
- `rodamientos.jpeg`: catálogo SKF, "Rodamientos de una hilera de rodillos cilíndricos — Serie NU 10", pág. 69 (material entregado en clase).
- Apuntes y datos del TP 1, en la carpeta `tp_grupal_mecanica_rotacional/`: teoría, convenciones de unidades y criterio de selección (`Mecanica_Rotacional_Apuntes.md`, `Mecanica_Rotacional_Datos.md`).

<!-- /solo-md -->
