# Brief para armar el informe — TP grupal Mecánica Rotacional (tren de engranajes)

> **Uso de este archivo:** está pensado para pasárselo completo a Claude (web) junto con la orden "armá el informe siguiendo este brief". Contiene todo lo necesario: datos, marco teórico mínimo, supuestos, resultados ya calculados y la estructura pedida. No hace falta ningún otro archivo.

> **⚠ Nota de divergencia de unidades (22/sep/2026):** esta versión trabaja con longitudes en milímetros y momento de inercia en **kg·mm²** (ver sección 3 y el Punto 2/3/3b), en línea con `Mecanica_Rotacional_Apuntes.md` e `index.html`. El informe final ya entregado (`tp_mecanica_rotacional.odt`/`.pdf`, local, no versionado) se generó **antes** de este cambio y quedó en kg·m² (Sistema Internacional puro); no se regeneró para mantenerlo tal cual fue entregado. Si se vuelve a armar el informe desde este brief, el documento resultante usará kg·mm² y por lo tanto **no coincidirá numéricamente en esa columna** con el `.odt`/`.pdf` ya entregado (los resultados físicos — L, T, P — son los mismos; solo cambia cómo se expresa `I`).

---

## 0. Instrucciones para quien arma el informe

1. **Idioma:** español rioplatense técnico, oraciones cortas. El informe debe ser **claro, conciso, breve y completo** (criterio de cátedra: que un lector pueda entender y reproducir el trabajo).
2. **Estructura obligatoria:** la de la sección 1 de este brief (adaptación de la estructura de informes de laboratorio de Física I de UTN FRBA).
3. **Los resultados ya están calculados** (sección 4). Usarlos tal cual; no recalcular ni "corregir". Si al verificar algo diera distinto, **avisar aparte** en lugar de cambiarlo en el informe.
4. **Sin diagramas ASCII.** Donde haga falta una figura (esquema del mecanismo), dejar el marcador `[INSERTAR FIGURA N: descripción]` con su pie; las figuras las inserta el grupo después, sobre el Word que se reciba (no dibujarlas ni describirlas con caracteres).
5. **Tablas numeradas con pie de tabla autoexplicativo** ("Tabla 1. …"). Todo resultado con **unidades** y **cifras significativas coherentes con los datos** (3–4 cifras; el enunciado no da incertezas, no se propagan errores).
6. **Notación:** fórmulas en línea entre backticks o en formato ecuación de Word; vectores solo donde importe el sentido (Punto 7).
7. **Marco teórico mínimo:** solo las fórmulas de la sección 3, cada una con una línea que diga qué es y para qué se usa. Sin demostraciones.
8. **No copiar el enunciado como si fuera el informe:** el enunciado se resume en "Datos" y "Objetivos".
9. **Entregable:** un archivo **Word (.docx)** con el informe completo (carátula, secciones, tablas numeradas con pie, fórmulas). Si no es posible generar el .docx, entregar el texto listo para pegar en Word. Las figuras **no se generan ahora**: dejar el marcador `[INSERTAR FIGURA N: descripción]` con su pie en el lugar correspondiente; el grupo las inserta después sobre el Word recibido. Al final, listar en el chat (no en el documento) cualquier dato que falte.

---

## 1. Estructura del informe (qué va en cada sección)

| Sección | Contenido en este TP |
|---|---|
| **Carátula** | Título, materia, integrantes, curso/comisión, turno, docente y ayudantes (ver sección 2) |
| **1. Introducción** | 1.1 Objetivos (a–f, sección 2.2) · 1.2 Marco teórico mínimo (sección 3) |
| **2. Desarrollo** *(equivale al "Procedimiento Experimental")* | 2.1 Descripción del mecanismo + Figura 1 · 2.2 Datos de entrada (Tabla 1) · 2.3 Modelos y supuestos adoptados (en lugar de "instrumentos e incertezas": acá no hay medición, los datos son del enunciado y del catálogo SKF) · 2.4 Método de resolución, punto por punto, en 1–3 líneas cada uno |
| **3. Resultados y Análisis** | Una tabla por grupo de resultados (Tablas 2–7, sección 4) con su pie · un **ejemplo de cálculo completo** (recomendado: el de `I` del engranaje del eje 1, ya que reúne volumen → masa → `I`, con la densidad como dato) · análisis breve al pie de cada punto |
| **4. Conclusiones** | Una conclusión **por objetivo** (a–f), retomando el objetivo y respondiendo con el número obtenido |
| **Anexo de cálculos** | Cálculos intermedios de la sección 4 (volúmenes, masas, sumas de `I`, verificaciones cruzadas) |
| **Fuentes** | Apunte teórico de Mecánica Rotacional (Ing. Abud, UTN FRBA, Ing. Mecánica I) y enunciado del ejercicio de aplicación (págs. 14–15); catálogo SKF, rodamientos rígidos de una hilera de bolas, serie 62 |

---

## 2. Datos de carátula y objetivos

### 2.1 Carátula

- **Título:** Mecánica Rotacional — Ejercicio de aplicación: tren de engranajes
- **Materia:** Ingeniería Mecánica I — UTN FRBA
- **Docente:** Ing. Abud, Moisés Rolando
- **Asistentes de Trabajo Práctico (ATP):** Belén Molina — Jerónimo Cáceres Guido
- **Integrantes** (orden alfabético por apellido):

| Apellido | Nombre |
|---|---|
| Castro | Iván |
| Langelotti | Leandro |
| Mingorance | Victoria |
| Paredes | Sergio |
| Rallo | Caterina |

- **Curso:** S1091 | **Turno:** Noche
- **Fecha de entrega:** jueves 24 de septiembre de 2026

*(Nota: el apunte teórico es del ciclo 2018 y nombra como ayudantes a Costucica y Gallo; no citarlos en el informe, los ATP actuales son los de arriba.)*

### 2.2 Objetivos (para la sección 1.1)

a) Determinar la velocidad de rotación del segundo eje de un tren de engranajes a partir de la del primero.
b) Calcular los momentos de inercia de los rodamientos, ejes y engranajes del mecanismo.
c) Calcular la cantidad de movimiento angular de cada conjunto rotor.
d) Aplicar la conservación de la cantidad de movimiento angular ante una reducción brusca del momento de inercia.
e) Analizar la cantidad de movimiento angular total del mecanismo respecto de un sistema de referencia fijo a la base.
f) Calcular la potencia transmitida por el mecanismo.

---

## 3. Marco teórico mínimo (para la sección 1.2)

**Conversión de velocidad.** Las fórmulas se plantean en SI (rad y s), por lo que `n` [RPM] se convierte a `ω` [rad/s]:
`ω = 2π·n / 60`

**Engrane sin deslizamiento.** Los puntos de contacto de dos engranajes tienen la misma velocidad tangencial: `v = ω₁·R₁ = ω₂·R₂`, de donde `n₂ = n₁·R₁/R₂`.

**Momento de inercia** (`I = Σ m·r²`). Mide la resistencia a cambiar la velocidad de giro; depende de cómo se distribuye la masa respecto del eje. Se usan dos casos, ambos respecto del eje del cuerpo:

| Cuerpo | Fórmula | Se usa en |
|---|---|---|
| Cilindro sólido | `I = M·R²/2` | Ejes |
| Cilindro anular (radios interior `R₁`, exterior `R₂`) | `I = M·(R₁² + R₂²)/2` | Engranajes y rodamientos |

**Convención de unidades de `I` en este informe:** las longitudes del enunciado (diámetros, radios, largos, alturas) ya vienen en milímetros, así que `I` se calcula y se reporta directamente en **kg·mm²** en vez de kg·m² (números más legibles para piezas de este tamaño: decenas a decenas de miles, en vez de `10⁻⁴`–`10⁻²`). La masa a partir de la densidad usa `δ` en kg/mm³ (`δ_acero = 7850 kg/m³ = 7,85×10⁻⁶ kg/mm³`; `δ_Al = 2708 kg/m³ = 2,708×10⁻⁶ kg/mm³`), de modo que `V` en mm³ × `δ` en kg/mm³ da la masa directo en kg: `M = δ·V`; con `V = π·R²·L` (cilindro sólido) o `V = π·(R_ext² − R_int²)·b` (cilindro anular).

**Dónde convertir de vuelta a SI:** `kg·mm² = 10⁻⁶ kg·m²`. Cada vez que `I` se combina con `ω` para dar `L` (que sí se reporta en SI, kg·m²/s), se multiplica `I` por `10⁻⁶` antes de operar — paso explícito en el Punto 4/5. Para el torque (`T = F·R`, Punto 8) el ajuste es distinto: `R` en mm da `T` en N·mm, y se divide por 1000 para pasar a N·m (no interviene el `10⁻⁶` de `I`, porque en `P=T·ω` el momento de inercia se cancela).

**Cantidad de movimiento angular** de un cuerpo que gira en torno a un eje de simetría: `L = I·ω` [kg·m²/s] (con `I` ya convertido a kg·m²).

**Conservación de `L`.** Si el momento externo es nulo, `dL/dt = 0` y `L = cte`: `I·ω = I'·ω'`.

**`L` respecto de un origen cualquiera:** `L_O = L_CM + r_CM × M·v_CM`. Si el centro de masa está fijo (`v_CM = 0`), el segundo término es nulo y `L_O = I·ω`, independiente de dónde se ubique el origen.

**Torque y potencia de rotación.** `T = r × F` (fuerza tangencial: `T = F·R`); `P = T·ω`. Equivalente traslacional: `P = F·v`.

**Conversión de potencia:** `1 HP = 745,8 W (J/s)`.

---

## 4. Desarrollo y resultados (material para las secciones 2, 3 y Anexo)

### 4.1 Descripción del mecanismo (sección 2.1 del informe)

Dos ejes paralelos, cada uno con un engranaje, engranados entre sí; cada eje apoya en dos rodamientos. El eje 1 es el motriz (dato: 2800 RPM). Los engranajes se identifican **siempre por su eje** (no como "chico/grande"): el eje 1 (Ø25 mm, el más fino) lleva el engranaje de mayor diámetro (250 mm), y el eje 2 (Ø35 mm) lleva el de menor diámetro (200 mm). Los calificativos "chico/grande" de los rodamientos siguen el diámetro del eje (diámetro interior del rodamiento = diámetro del eje).

`[INSERTAR FIGURA 1: esquema del mecanismo con dos ejes, engranajes y rodamientos, cotas del enunciado (pág. 14)]`

### 4.2 Datos de entrada (Tabla 1)

| Dato | Eje 1 | Eje 2 |
|---|---|---|
| Diámetro del eje | 25 mm | 35 mm |
| Largo del eje | 300 mm | 300 mm |
| Diámetro del engranaje (`R` = radio) | 250 mm (`R₁ = 125 mm`) | 200 mm (`R₂ = 100 mm`) |
| Ancho de cara del engranaje | 30 mm | 30 mm |
| Rodamiento SKF serie 62 (2 por eje) | 6205: d = 25, D = 52, B = 15 mm; m = 0,128 kg | 6207: d = 35, D = 72, B = 17 mm; m = 0,288 kg |
| Altura del eje respecto de la base | `H₁ = 1500 mm` | `H₂` sin valor en el enunciado |

Materiales y densidades: ejes de acero al carbono (`δ = 7850 kg/m³ = 7,85×10⁻⁶ kg/mm³`); engranajes de aluminio (`δ = 2708 kg/m³ = 2,708×10⁻⁶ kg/mm³`); rodamientos de acero (se usa la masa de catálogo).
Datos de operación: `n₁ = 2800 RPM`; fuerza tangencial entre engranajes `F = 200 N`; `1 HP = 745,8 J/s`.

*Pie de tabla sugerido: "Datos del enunciado (págs. 14–15 del apunte de Abud) y del catálogo SKF. `H₂` no se informa porque no interviene en la resolución (Punto 7)."*

*Nota al pie a incluir (una sola vez, breve):* el enunciado da `1 HP·hora = 2,685×10⁵ J`, valor incompatible con `1 HP = 745,8 J/s` (daría 2,685×10⁶ J). Ese factor **no se usa** en el ejercicio, por lo que no afecta ningún resultado; se deja tal cual figura en el enunciado.

### 4.3 Modelos y supuestos (sección 2.3 del informe)

1. **Engranajes:** cilindros anulares lisos (se desprecia el dentado), diámetro exterior el dado, largo axial = ancho de cara, radio interior = radio del eje que los atraviesa (evita contar dos veces el núcleo del eje).
2. **Ejes:** cilindros macizos de acero; largo 300 mm para ambos (el enunciado lo da una sola vez).
3. **Rodamientos:** cilindro anular con `R_int = d/2` (diámetro del eje) y `R_ext = D/2` (catálogo SKF), usando la **masa de catálogo** (el rodamiento real tiene huecos: bolas y jaula, por lo que `δ·V` sobreestimaría la masa).
4. **Engrane ideal:** sin deslizamiento ni pérdidas.
5. **Momento de inercia del conjunto (Puntos 4, 5, 6 y 7):** el enunciado no lo define. **Decisión del grupo:** se adopta el **conjunto rotante completo** de cada eje, es decir eje + engranaje + rodamientos: `I = I_eje + I_engranaje + I_rodamientos`. Se justifica porque el Punto 2 pide el `I` de los rodamientos como ítem propio, lo que solo tiene uso si luego se suman al del conjunto. La aclaración del Punto 8 ("conjunto engranaje y eje") no lo contradice: allí `P = T·ω` y el `I` se cancela, de modo que el resultado de ese punto no depende de qué componentes se incluyan.
6. **Unidades de trabajo:** longitudes en mm e `I` en kg·mm² (ver sección 3); se convierte a SI explícitamente donde hace falta (`L` en kg·m²/s, `T` en N·m).

### 4.4 Resultados punto por punto (sección 3 del informe; cálculos intermedios → Anexo)

**Punto 1 — Velocidad del eje 2 (Tabla 2)**

Conversión: `ω₁ = 2π·2800/60 ≈ 293,2 rad/s`. Engrane: `ω₂ = ω₁·R₁/R₂ = 293,2·125/100 ≈ 366,5 rad/s`.
Verificación: `v_contacto = ω₁R₁ = 293,2·125 ≈ 36.652 mm/s ≈ 36,65 m/s` y `ω₂R₂ = 366,5·100 ≈ 36.652 mm/s ≈ 36,65 m/s` ✓.
Atajo: `n₂ = n₁·R₁/R₂ = 2800·125/100 = 3500 RPM`.

| Eje | n (RPM) | ω (rad/s) |
|---|---|---|
| 1 | 2800 | 293,2 |
| 2 | 3500 | 366,5 |

*Análisis:* el eje con el engranaje más chico (eje 2) gira más rápido, en proporción inversa a los radios.

**Punto 2 — Momento de inercia de los rodamientos (Tabla 3)**

`I = ½·m·(R_ext² + R_int²)`, con `R` en mm → `I` en kg·mm².

| Eje | Rodamiento | m (kg) | R_ext (mm) | R_int (mm) | I por rodamiento (kg·mm²) | I total ×2 (kg·mm²) |
|---|---|---|---|---|---|---|
| 1 | 6205 | 0,128 | 26 | 12,5 | 53,26 | **106,5** |
| 2 | 6207 | 0,288 | 36 | 17,5 | 230,7 | **461,4** |

Cálculo ejemplo eje 1: `½·0,128·(676 + 156,25) = ½·0,128·832,25 ≈ 53,26 kg·mm²`.

**Punto 3 — Momento de inercia de los ejes (Tabla 4)**

`M = δ_acero·π·R²·L` (con `R`, `L` en mm y `δ` en kg/mm³, `V` sale en mm³); `I = ½·M·R²` (verificación: `I = ½·δ·π·L·R⁴`).

| Eje | R (mm) | V (mm³) | M (kg) | I (kg·mm²) |
|---|---|---|---|---|
| 1 | 12,5 | 147.263 | 1,156 | **90,3** |
| 2 | 17,5 | 288.634 | 2,266 | **346,9** |

**Punto 3b — Momento de inercia de los engranajes** *(no figura como ítem de la consigna pero es insumo de los Puntos 4 a 7; incluir en la misma Tabla 4 o en una Tabla 4b)*

`M = δ_Al·π·(R_ext² − R_int²)·b`; `I = ½·M·(R_ext² + R_int²)`.

| Engranaje | R_ext (mm) | R_int (mm) | V (mm³) | M (kg) | I (kg·mm²) |
|---|---|---|---|---|---|
| Eje 1 | 125 | 12,5 | 1.457.864 | 3,948 | **31.152** |
| Eje 2 | 100 | 17,5 | 913.614 | 2,474 | **12.749** |

*Análisis:* aunque el eje 2 es el de mayor diámetro de eje, su engranaje tiene menor `I` (menor radio, menor masa): `I` crece con `R²`, por eso domina el engranaje sobre eje y rodamientos (ver componentes en la Tabla 5).

**Puntos 4 y 5 — Cantidad de movimiento angular `L₁` y `L₂` (Tablas 5 y 6)**

`I = I_eje + I_engranaje + I_rodamientos` (kg·mm²); se convierte a SI (`×10⁻⁶`) antes de aplicar `L = I·ω` con `ω` en rad/s.

Tabla 5 — Componentes de `I` (kg·mm²):

| Eje | I_eje | I_engranaje | I_rodamientos (×2) |
|---|---|---|---|
| 1 | 90,3 | 31.152 | 106,5 |
| 2 | 346,9 | 12.749 | 461,4 |

Tabla 6 — `I` total (kg·mm² y su conversión a SI) y `L`:

| Eje | ω (rad/s) | I (kg·mm²) | I (kg·m²) | L (kg·m²/s) |
|---|---|---|---|---|
| 1 | 293,2 | 31.349 | 3,135×10⁻² | **9,19** |
| 2 | 366,5 | 13.558 | 1,356×10⁻² | **4,97** |

Unidad de `L`: kg·m²/s = N·m·s = J·s (por eso se reporta en SI, a diferencia de `I`). Los valores son módulos (los engranajes giran en sentidos opuestos).

**Punto 6 — `I₁` e `I₂` se reducen a la mitad (Tabla 7)**

El cambio es brusco y no se indica momento externo ⇒ `L` se conserva. Notación: prima (`'`) = estado final (los subíndices 1 y 2 identifican al eje, no al estado).
`I·ω = I'·ω'` con `I' = I/2` ⇒ `ω' = 2·ω`. El resultado **no depende del valor de `I` ni de en qué unidad esté expresado** (kg·mm² o kg·m² dan la misma relación `I/I' = 2`).

| Eje | ω antes (rad/s) | ω' después (rad/s) | n antes (RPM) | n' después (RPM) |
|---|---|---|---|---|
| 1 | 293,2 | **586,4** | 2800 | **5600** |
| 2 | 366,5 | **733,0** | 3500 | **7000** |

Verificación de engrane: `ω₁'R₁ = 586,4·125 ≈ 73.304 mm/s ≈ 73,30 m/s = ω₂'R₂ = 733,0·100 ≈ 73.304 mm/s ≈ 73,30 m/s` ✓ (la relación entre velocidades no cambia).

*Análisis (qué se conserva y qué no):* `L` se conserva pero la energía cinética `K = ½·I·ω²` **se duplica** (`K' = ½·(I/2)·(2ω)² = 2K`, con `I` en kg·m² para que `K` salga en joules); p. ej. eje 1: de ≈ 1,35×10³ J a ≈ 2,70×10³ J. Esa energía adicional la aporta el trabajo de lo que reduce `I` (análogo a una patinadora que cierra los brazos).

**Punto 7 — `L` total respecto de un sistema fijo a la base**

Principio: `L_O = L_CM + r_CM × M·v_CM`. Cada conjunto es simétrico, gira en torno a un eje fijo que pasa por su centro de masa ⇒ `v_CM = 0`, el segundo término se anula y `L_O = I·ω`, **independiente de `H₁` y `H₂`** (por eso `H₂` no hace falta).

Sentidos: engranajes engranados por fuera ⇒ giran en sentidos opuestos ⇒ `L₁` y `L₂` son antiparalelos ⇒ `L_total = L₁ − L₂` (error a evitar: sumar módulos, que daría ≈ 14,16 en vez de ≈ 4,22).

| L₁ (kg·m²/s) | L₂ (kg·m²/s) | L_total = L₁ − L₂ (kg·m²/s) |
|---|---|---|
| 9,19 | 4,97 | **≈ 4,22** |

*Análisis:* `L_total` **no es nulo** (los ejes tienen distinto `I·ω`), queda dirigido según los ejes con el sentido de giro del eje 1, y es **constante en el tiempo**: la fuerza entre engranajes es un par acción-reacción interno (no aporta a `T_ext`) y las reacciones de los apoyos solo dan momentos perpendiculares al eje. **También se conserva en el cambio del Punto 6**, porque `I'ω' = Iω` en cada eje.

**Punto 8 — Potencia del mecanismo en HP (Tabla 8)**

Se usan las velocidades iniciales (Punto 1). La consigna pide considerar el `I` del conjunto engranaje y eje, pero en `P = T·ω` el `I` no interviene, así que el resultado no depende de qué componentes se incluyan.

1. Torques (fuerza tangencial, `sen θ = 1`, `R` en mm): `T₁ = F·R₁ = 200·125 = 25.000 N·mm = 25 N·m`; `T₂ = F·R₂ = 200·100 = 20.000 N·mm = 20 N·m`.
2. `P = T·ω` (con `T` ya en N·m): `P₁ = 25·293,2 ≈ 7330 W`; `P₂ = 20·366,5 ≈ 7330 W`. El momento de inercia se cancela (si se escribe `P = I·ω·α`, como `I·α = T` resulta `P = T·ω`) y no modifica `P`.
3. Verificación: `P = F·v_contacto = 200·36,65 ≈ 7330 W` ✓.
4. Conversión: `P = 7330 / 745,8 ≈ 9,83 HP`.

| Eje | T (N·m) | ω (rad/s) | P = T·ω (W) | P (HP) |
|---|---|---|---|---|
| 1 | 25 | 293,2 | ≈ 7330 | **≈ 9,83** |
| 2 | 20 | 366,5 | ≈ 7330 | **≈ 9,83** |

*Análisis:* ambos ejes transmiten la misma potencia (engrane ideal, sin pérdidas), como corresponde. El eje 1 recibe más torque y gira más lento; el eje 2, menos torque y más velocidad.

---

## 5. Conclusiones sugeridas (una por objetivo — reformular, no copiar)

a) `n₂ = 3500 RPM` (`ω₂ ≈ 366,5 rad/s`), mayor que `n₁` en la relación `R₁/R₂ = 1,25`.
b) Los engranajes de aluminio concentran casi todo el `I` (≈ 31.150 y 12.750 kg·mm²); ejes y rodamientos aportan ≈ 0,6 % del `I` total en el eje 1 y ≈ 6 % en el eje 2 (`I` crece con `R²`).
c) `L₁ ≈ 9,19` y `L₂ ≈ 4,97 kg·m²/s`.
d) Al reducirse `I` a la mitad con `L` constante, las velocidades se duplican (5600 y 7000 RPM); la energía cinética también se duplica, por lo que el proceso requiere aporte de trabajo.
e) `L_total ≈ 4,22 kg·m²/s` por giro en sentidos opuestos; constante, no nulo y independiente de la altura del sistema de referencia.
f) `P ≈ 7330 W ≈ 9,83 HP`, igual en ambos ejes e independiente de `I`.

Cerrar con la **limitación del modelo**: (i) dentado despreciado; (ii) rodamientos modelados como cilindros anulares que giran completos con la masa de catálogo, cuando en un rodamiento real solo gira con el eje el aro interior (y parte de las bolas) y el aro exterior queda fijo a la carcasa, por lo que su `I` es una **cota superior** del real, con un aporte pequeño al `I` del conjunto; (iii) engrane ideal (sin pérdidas).

---

## 6. Checklist final antes de entregar

- [ ] Carátula completa (integrantes, curso S1091, turno Noche, entrega 24/sep/2026).
- [ ] Figura 1 (esquema del mecanismo) insertada, con pie.
- [ ] Todas las tablas numeradas y con pie autoexplicativo.
- [ ] Todos los resultados con unidades; `ω` en rad/s en toda fórmula; `I` en kg·mm², convertido a SI donde se combina con `ω` para dar `L`.
- [ ] Criterio de `I` del conjunto (eje + engranaje + rodamientos) declarado en 2.3.
- [ ] Una conclusión por objetivo.
- [ ] Nota al pie del factor HP·hora (no interviene) presente una sola vez.
- [ ] Fuentes citadas al final.

---

*Brief generado a partir de `Mecanica_Rotacional_Apuntes.md` (sección 11 y resolución de los puntos 1–8) y de la estructura de informes de laboratorio de Física I (`fisica_i/laboratorio/propuesta de estructura de informe.pdf`, informes TP5 y TP6). Fuente original: "UTN – FRBA – Apunte Teórico – Mecánica Rotacional" (Ing. Abud, Ing. Mecánica I) y catálogo SKF serie 62. Convención de unidades (mm / kg·mm²) actualizada el 22/sep/2026; ver nota de divergencia con el informe ya entregado al inicio de este archivo.*
