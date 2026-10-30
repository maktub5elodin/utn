# Hoja de fórmulas — Química General A1095
**Química General A1095 · UTN FRBA · Ingeniería Mecánica**

---

## Qué es este documento

Documentación de la hoja de fórmulas de una carilla (`hoja_formulas.tex` → `make` → `build/hoja_formulas.pdf`). La hoja crece a medida que avanza el estudio:

- **En el PDF** van **solo** las fórmulas que pide el usuario, con unidades y mínimo texto.
- **En este `.md`** van esas mismas fórmulas con una explicación breve, más **sugerencias numeradas** (S6.x para el cap. 6, S11.x para el cap. 11, S12.x para el cap. 12, S14.x para el cap. 14, S15.x para el cap. 15, S16.x para el cap. 16 (pendiente), S19.x para el cap. 19, SC.x para constantes) basadas en el Chang (9.ª ed. en español). Para pasar una al PDF alcanza con indicar su número (ej. "pasá S6.9 y S12.9"). Las que ya pasaron están marcadas con **✓ PDF**.

Formato del PDF: A4, márgenes de 7 mm, cuerpo de 9 pt, 3 columnas que se llenan en orden (de arriba a abajo, de izquierda a derecha). El `make` falla si la hoja pasa de una carilla.

---

## Cap. 4 — Reacciones en disolución acuosa (Chang)

Repaso, base para el cap. 19 (electroquímica). Abre el PDF, antes de termoquímica.

### En el PDF

| Fórmula / dato | Qué dice |
|---|---|
| $\text{ácido} + \text{base} \rightarrow \text{sal} + \text{H}_2\text{O}$ | Neutralización (cap. 4). Ej.: $\text{HCl} + \text{NaOH} \rightarrow \text{NaCl} + \text{H}_2\text{O}$ |
| $\text{H}^+ + \text{OH}^- \rightarrow \text{H}_2\text{O}$ | Ecuación iónica neta: lo único que reacciona de verdad; la sal queda como iones espectadores |
| Arrhenius / Brønsted / Lewis | Ácido: libera H⁺ (H₃O⁺) / dona H⁺ / acepta par de e⁻. Base: libera OH⁻ / acepta H⁺ / dona par de e⁻ |
| $\text{Zn} \rightarrow \text{Zn}^{2+} + 2\,\text{e}^-$ | Oxidación: **pierde** electrones (el n.º de oxidación sube) |
| $\text{Cu}^{2+} + 2\,\text{e}^- \rightarrow \text{Cu}$ | Reducción: **gana** electrones (el n.º de oxidación baja) |
| Reducir = bajar el n.º de oxidación | Para bajar la carga hay que sumar cargas negativas, o sea electrones: por eso la reducción **gana** e⁻ |
| Agentes | El que se oxida es el **agente reductor** (le da sus e⁻ al otro); el que se reduce es el **agente oxidante** |

---

## Cap. 5 — Gases (Chang)

### En el PDF

| Fórmula / dato | Qué dice |
|---|---|
| $PV = nRT$ | Gas ideal, "Pibe Vago no Recibe Título". $R = 0{,}0821\ \text{L}\cdot\text{atm}/(\text{mol}\cdot\text{K}) = 8{,}314\ \text{J}/(\text{mol}\cdot\text{K})$, $T$ en K |

---

## Cap. 6 — Termoquímica (Chang)

### En el PDF

| Fórmula | Unidades | Qué dice |
|---|---|---|
| $\Delta E = q + w$ | J | Primera ley: el cambio de energía interna del sistema es el calor más el trabajo intercambiados |
| $w = -P\,\Delta V$ | L·atm ($1\ \text{L}\cdot\text{atm} = 101{,}3\ \text{J}$) | Trabajo de expansión/compresión contra presión externa constante |
| $H = E + PV$ | J | Definición de entalpía |
| $\Delta H = \Delta E + P\,\Delta V$ | J | Cambio de entalpía a presión constante |
| $q_p = \Delta H$ | — ($P$ cte) | A presión constante, el calor intercambiado es el cambio de entalpía |
| $C = m\,s$ | J/°C | Capacidad calorífica: masa por calor específico ($s$ en J/(g·°C), $m$ en g) |
| $q = m\,s\,\Delta t = C\,\Delta t$ | J | Calor sensible; $\Delta t = t_f - t_i$ |
| $\Delta H^\circ_{\text{rxn}} = \sum n\,\Delta H^\circ_f(\text{prod}) - \sum m\,\Delta H^\circ_f(\text{react})$ | kJ/mol | Entalpía de reacción a partir de entalpías estándar de formación; $n$, $m$ = coeficientes estequiométricos |

### Sugerencias (no están en el PDF)

#### Energía y primera ley (Chang 6.1–6.3)

| N° | Fórmula | Unidades | Para qué |
|---|---|---|---|
| S6.1 | $E_k = \tfrac{1}{2}\,m\,v^2$ | J = kg·m²/s² | Definición de joule; energía cinética |
| S6.2 ✓ PDF | $1\ \text{cal} = 4{,}184\ \text{J}$ | — | Conversión: muchos datos viejos vienen en cal o kcal |
| S6.3 | $\Delta E = E_f - E_i$ | J | $E$ es **función de estado** (solo importan inicio y fin); $q$ y $w$ **no** lo son |
| S6.4 | $\Delta E_{\text{sis}} + \Delta E_{\text{alr}} = 0$ | J | Conservación: lo que gana el sistema lo pierden los alrededores |
| S6.5 ✓ PDF | Signos: $q>0$ absorbe; $q<0$ libera; $w>0$ sobre el sistema; $w<0$ por el sistema | — | Convención del Chang (ver tabla abajo) |
| S6.6 | $\Delta V = 0 \Rightarrow w = 0 \Rightarrow \Delta E = q_v$ | J | Volumen constante (bomba calorimétrica) |

Tabla de signos (S6.5):

| Proceso | $q$ | $w$ |
|---|---|---|
| Sistema absorbe calor (endotérmico) | + | |
| Sistema libera calor (exotérmico) | − | |
| Trabajo sobre el sistema (compresión, $\Delta V<0$) | | + |
| Trabajo hecho por el sistema (expansión, $\Delta V>0$) | | − |

#### Entalpía y ecuaciones termoquímicas (Chang 6.4)

| N° | Fórmula | Unidades | Para qué |
|---|---|---|---|
| S6.7 ✓ PDF | $\Delta E = \Delta H - RT\,\Delta n$ | J ($R = 8{,}314\ \text{J/(mol K)}$, $T$ en K) | Pasar de $\Delta H$ a $\Delta E$ en reacciones con gases; $\Delta n$ = moles de gas productos − moles de gas reactivos |
| S6.8 ✓ PDF | $\Delta H < 0$ exotérmica; $\Delta H > 0$ endotérmica | — | Lectura del signo |
| S6.9 | Invertir la ecuación $\Rightarrow -\Delta H$; multiplicarla por $k \Rightarrow k\,\Delta H$ | kJ | Manipulación de ecuaciones termoquímicas |
| S6.10 | $q = \dfrac{n_X}{\nu_X}\,\Delta H_{\text{rxn}}$ | kJ | Calor para una cantidad dada: moles de la sustancia X sobre su coeficiente $\nu_X$ en la ecuación |

#### Calorimetría (Chang 6.5)

| N° | Fórmula | Unidades | Para qué |
|---|---|---|---|
| S6.11 | $q_{\text{sis}} = -q_{\text{alr}}$ | J | Base de todo problema de calorimetría (calorímetro aislado) |
| S6.12 | $q_{\text{cal}} = C_{\text{cal}}\,\Delta t \quad;\quad q_{\text{rxn}} = -C_{\text{cal}}\,\Delta t$ | J ($C_{\text{cal}}$ en J/°C o kJ/°C) | Bomba calorimétrica (volumen constante) |
| S6.13 | $q_{\text{rxn}} = -\left(m_{\text{agua}}\,s_{\text{agua}} + C_{\text{cal}}\right)\Delta t$ | J | Calorímetro a presión constante con agua (taza de café) |
| S6.14 | $\sum q_i = 0 \Rightarrow t_f = \dfrac{m_1 s_1 t_1 + m_2 s_2 t_2}{m_1 s_1 + m_2 s_2}$ | °C | Mezcla de dos cuerpos a distinta temperatura, sin pérdidas |
| S6.15 | $\Delta t\ [{}^\circ\text{C}] = \Delta T\ [\text{K}]$ | — | Las diferencias valen igual en °C y en K |

Calores específicos (Chang, tabla 6.2), en J/(g·°C) — S6.16 ✓ PDF:

| Sustancia | $s$ | Sustancia | $s$ |
|---|---|---|---|
| Agua (líquida) | 4,184 | Hierro | 0,444 |
| Etanol | 2,46 | Cobre | 0,385 |
| Aluminio | 0,900 | Plomo | 0,158 |
| Carbono (grafito) | 0,720 | Mercurio | 0,139 |
| Carbono (diamante) | 0,502 | Oro | 0,129 |

#### Entalpía de formación y de reacción (Chang 6.6)

| N° | Fórmula | Unidades | Para qué |
|---|---|---|---|
| S6.17 ✓ PDF | $\Delta H^\circ_f = 0$ para elementos en su forma más estable (1 atm, 25 °C) | kJ/mol | Ej.: O₂(g), H₂(g), C(grafito), Fe(s) |
| S6.18 ✓ PDF | Ley de Hess: $\Delta H_{\text{total}} = \sum \Delta H_{\text{etapas}}$ | kJ | Combinar reacciones conocidas para obtener una desconocida |
| S6.19 | $\Delta H^\circ \approx \sum EE(\text{enlaces rotos}) - \sum EE(\text{enlaces formados})$ | kJ/mol | Estimación con energías de enlace (Chang cap. 9); ojo: acá es reactivos − productos |

Entalpías estándar de formación a 298 K y 1 atm, en kJ/mol (selección de la tabla de la guía de la cátedra, pág. 52 del PDF) — **✓ PDF**:

| Sustancia | $\Delta H^\circ_f$ | Sustancia | $\Delta H^\circ_f$ |
|---|---|---|---|
| CO₂(g) | −393,5 | CH₄(g) (metano) | −74,8 |
| H₂O(l) | −285,8 | C₂H₂(g) (acetileno) | +226,8 |
| H₂O(g) | −241,8 | C₃H₈(g) (propano) | −103,8 |
| CO(g) | −110,5 | C₄H₁₀(g) (butano) | −124,7 |
| NH₃(g) | −46,2 | C₈H₁₈(l) (octano) | −269,8 |
| NO(g) | +90,4 | C₂H₅OH(l) (etanol) | −277,7 |
| SO₂(g) | −296,9 | CaCO₃(s) | −1207,1 |
| Fe₂O₃(s) | −822,2 | CaO(s) | −635,5 |
| C diamante(s) | +1,9 | | |

$\Delta H^\circ_f = 0$ para los elementos puros en su forma más estable: O₂(g), H₂(g), N₂(g), C(grafito), Fe(s), Al(s), P₄ blanco(s). El diamante **no** es la forma más estable del carbono, por eso su $\Delta H^\circ_f \neq 0$. Ojo con H₂O(l) vs H₂O(g): difieren en 44 kJ/mol (la entalpía de vaporización).

#### Disolución y cambios de fase (Chang 6.7 y cap. 11)

| N° | Fórmula | Unidades | Para qué |
|---|---|---|---|
| S6.20 | $\Delta H_{\text{disol}} = U + \Delta H_{\text{hidr}}$ | kJ/mol | Calor de disolución de un sólido iónico: energía reticular $U$ (+) más entalpía de hidratación (−) |
| S6.21 ✓ PDF (cap. 11) | $q = n\,\Delta H_{\text{fus}}$ (o $\Delta H_{\text{vap}}$) | kJ | Calor latente: durante el cambio de fase $t$ no cambia |
| S6.22 | $q_{\text{total}} = \sum q_{\text{sensibles}} + \sum q_{\text{latentes}}$ | kJ | Curva de calentamiento (ej. hielo a −10 °C → vapor a 110 °C: 5 tramos) |
| S6.23 | $\Delta H_{\text{cond}} = -\Delta H_{\text{vap}} \quad;\quad \Delta H_{\text{solid}} = -\Delta H_{\text{fus}}$ | kJ/mol | Procesos inversos: mismo valor, signo opuesto |

---

## Cap. 11 — Fuerzas intermoleculares y líquidos y sólidos (Chang)

Es el puente entre termoquímica y soluciones: los $\Delta H$ de cambio de fase **miden** las fuerzas intermoleculares (decenas de kJ/mol), mientras que los $\Delta H^\circ_f$ del cap. 6 miden enlaces químicos (cientos de kJ/mol). Para Ingeniería Mecánica, además, las celdas cúbicas (S11.17–S11.18) son la base de la estructura de los metales (aceros, aluminio, cobre) que vuelve en Materiales.

### En el PDF

| Fórmula | Unidades | Qué dice |
|---|---|---|
| Dispersión < dipolo–dipolo < puente de H < ion–dipolo | — | Orden típico de intensidad de las fuerzas intermoleculares |
| $\Delta H_{\text{sub}} = \Delta H_{\text{fus}} + \Delta H_{\text{vap}}$ | kJ/mol | Sublimación = fusión + vaporización (Hess aplicado a fases) |
| $q = n\,\Delta H_{\text{fus}}$ (o $\Delta H_{\text{vap}}$) | kJ | Calor latente: durante el cambio de fase $t$ no cambia (meseta de la curva de calentamiento) |
| $\text{X–H}\cdots\text{:Y}$, con X, Y = N, O, F | — | Puente de hidrógeno: un H unido a N, O o F (muy electronegativos y chicos, dejan al H casi "desnudo") es atraído por un par libre de otro N, O o F. Es un dipolo–dipolo especial, mucho más fuerte |
| Efectos del puente de H | — | $T_b$ y $\Delta H_{\text{vap}}$ anómalamente altos, menor presión de vapor, mayor tensión superficial; el hielo (red abierta de puentes de H) es menos denso que el agua líquida y flota |
| $T_b$ [°C] con puente de H: H₂O 100, HF 20, NH₃ −33 — sin puente de H: H₂S −60, HCl −85, PH₃ −88 | °C | Comparación con el hidruro del mismo grupo en el período siguiente: sin puente de H, la tendencia sería al revés (más masa molar ⇒ más dispersión ⇒ mayor $T_b$) |

### Sugerencias (no están en el PDF)

#### Fuerzas intermoleculares (Chang 11.2–11.3)

| N° | Dato | Para qué |
|---|---|---|
| S11.1 ✓ PDF | Puente de H: solo con H unido a **N, O o F** | Explica por qué H₂O, NH₃ y HF hierven mucho más alto que sus análogos (H₂S, PH₃, HCl) |
| S11.2 | Dispersión crece con la masa molar (más electrones, más polarizable) | Explica la tendencia de puntos de ebullición en series (CH₄ < C₂H₆ < C₃H₈; F₂ < Cl₂ < Br₂ < I₂) |
| S11.3 | Fuerzas más intensas ⇒ mayor $T_b$, mayor $\Delta H_{\text{vap}}$, mayor tensión superficial y viscosidad, **menor** presión de vapor | Preguntas conceptuales de comparación |
| S11.4 | Ion–dipolo: sales disueltas en agua | Conecta con $\Delta H_{\text{hidr}}$ (S6.20) y con el proceso de disolución (S12.1) |

#### Estructura cristalina (Chang 11.4–11.6)

| N° | Fórmula / dato | Unidades | Para qué |
|---|---|---|---|
| S11.5 | Número de coordinación: cúbica simple 6; BCC 8; FCC 12 | — | Vecinos más cercanos de cada átomo |
| S11.6 | Fracción de empaquetamiento: cúbica simple 52 %; BCC 68 %; FCC 74 % | — | FCC (y hexagonal compacta) es el empaquetamiento más eficiente |
| S11.7 | Conteo: vértice $= \tfrac{1}{8}$, cara $= \tfrac{1}{2}$, arista $= \tfrac{1}{4}$, centro $= 1$ | átomos | De dónde salen 1, 2 y 4 átomos por celda |
| S11.8 | $1\ \text{pm} = 10^{-10}\ \text{cm} \quad;\quad 1\ \text{Å} = 10^{-8}\ \text{cm}$ | — | Los radios vienen en pm o Å y la densidad se pide en g/cm³ |
| S11.9 | $2\,d\,\operatorname{sen}\theta = n\,\lambda$ | $d$, $\lambda$ en las mismas unidades (pm o Å) | Ley de Bragg (difracción de rayos X) |
| S11.10 | Tipos de cristal: iónico (NaCl), covalente (diamante, SiO₂), molecular (hielo, I₂), metálico (Fe, Cu) | — | Propiedades: los covalentes y los iónicos tienen $T_f$ altas; los moleculares, bajas; los metálicos conducen |

#### Cambios de fase y diagramas de fase (Chang 11.8–11.9)

| N° | Fórmula / dato | Unidades | Para qué |
|---|---|---|---|
| S11.11 | $\ln P = -\dfrac{\Delta H_{\text{vap}}}{R\,T} + C$ | $P$ en cualquier unidad, $T$ en K | Forma lineal de Clausius-Clapeyron: graficando $\ln P$ vs $1/T$, la pendiente es $-\Delta H_{\text{vap}}/R$ |
| S11.12 | Agua: $\Delta H_{\text{fus}} = 6{,}01$ kJ/mol; $\Delta H_{\text{vap}} = 40{,}79$ kJ/mol (a 100 °C) | kJ/mol | Datos para la curva de calentamiento (a 25 °C, $\Delta H_{\text{vap}} \approx 44{,}0$ kJ/mol: ver tabla de $\Delta H^\circ_f$) |
| S11.13 | Agua: punto triple 0,01 °C y 4,58 mmHg; punto crítico 374 °C y 218 atm | — | Lectura del diagrama de fases del agua |
| S11.14 | Por encima de $T_c$ el gas no se licúa a ninguna presión | — | Temperatura y presión críticas |
| S11.15 | Agua: la línea sólido–líquido tiene pendiente **negativa** | — | El hielo es menos denso que el agua: al aumentar $P$ se funde (caso anómalo; en casi todas las sustancias es positiva) |
| S11.16 | $\ln\dfrac{P_1}{P_2} = \dfrac{\Delta H_{\text{vap}}}{R}\left(\dfrac{1}{T_2} - \dfrac{1}{T_1}\right)$ | $R = 8{,}314\ \text{J/(mol K)}$, $T$ en K, $\Delta H_{\text{vap}}$ en **J**/mol | Clausius-Clapeyron de dos puntos: presión de vapor a otra temperatura (estuvo en el PDF; se sacó por ahora) |

#### Celdas cúbicas (Chang 11.4) — estuvieron en el PDF; se sacaron por ahora

| N° | Fórmula / dato | Unidades | Para qué |
|---|---|---|---|
| S11.17 | Cúbica simple: 1 átomo/celda, $a = 2r$ — BCC: 2, $a = \dfrac{4r}{\sqrt{3}}$ — FCC: 4, $a = 2\sqrt{2}\,r$ | — | $a$ = arista, $r$ = radio atómico. BCC: Fe α, Cr, Na; FCC: Al, Cu, Au, Ag, Fe γ |
| S11.18 | $\rho = \dfrac{n\,\mathcal{M}}{N_A\,a^3}$ | g/cm³ ($a$ en cm; $N_A = 6{,}022 \times 10^{23}\ \text{mol}^{-1}$) | Densidad a partir de la celda |

---

## Cap. 12 — Propiedades físicas de las soluciones (Chang)

### Unidades de concentración — en el PDF

| Fórmula | Unidades | Qué dice |
|---|---|---|
| $\%\,\text{masa} = \dfrac{m_{\text{soluto}}}{m_{\text{soluto}} + m_{\text{solvente}}} \times 100\%$ | % | Masa de soluto sobre masa de solución |
| $X_A = \dfrac{n_A}{\sum n}$ | adimensional | Fracción molar del componente A |
| $M = \dfrac{n_{\text{soluto}}}{V_{\text{solución}}}$ | mol/L | Molaridad: depende de la temperatura (el volumen cambia con $T$) |
| $m = \dfrac{n_{\text{soluto}}}{m_{\text{solvente}}}$ | mol/kg | Molalidad: **kg de solvente**, no de solución; no depende de $T$ |

### Propiedades coligativas — en el PDF

| Fórmula | Unidades | Qué dice |
|---|---|---|
| $P_1 = X_1\,P_1^\circ$ | atm o mmHg | Ley de Raoult: la presión de vapor del solvente en la solución es su fracción molar por la presión de vapor del solvente puro |

### Sugerencias (no están en el PDF)

#### Tipos de solución y proceso de disolución (Chang 12.1–12.2)

| N° | Fórmula / dato | Unidades | Para qué |
|---|---|---|---|
| S12.1 | $\Delta H_{\text{disol}} = \Delta H_1 + \Delta H_2 + \Delta H_3$ | kJ/mol | Separar solvente (1, +) + separar soluto (2, +) + mezclar (3, −) |
| S12.2 | No saturada < saturada < sobresaturada | — | Según si la cantidad disuelta es menor, igual o mayor que la solubilidad |

#### Unidades de concentración: extras y conversiones (Chang 12.3 y cap. 4)

| N° | Fórmula | Unidades | Para qué |
|---|---|---|---|
| S12.3 | $\sum X_i = 1$ | — | Verificación; en binaria $X_1 = 1 - X_2$ |
| S12.4 | $\text{ppm} = \dfrac{m_{\text{soluto}}}{m_{\text{solución}}} \times 10^6$ | ppm (≈ mg/L en agua diluida) | Soluciones muy diluidas (contaminantes, aditivos) |
| S12.5 | $m_{\text{solución}} = \rho\,V_{\text{solución}}$ | g (ρ en g/mL, $V$ en mL) | Puente entre unidades por volumen (M) y por masa (m, % masa) |
| S12.6 | $m_{\text{solvente}} = m_{\text{solución}} - n_{\text{soluto}}\,\mathcal{M}_{\text{soluto}}$ | g | Paso clave para pasar de M a m; $\mathcal{M}$ = masa molar (g/mol) |
| S12.7 | $n = \dfrac{m}{\mathcal{M}}$ | mol | Moles a partir de masa |
| S12.8 | $M_i\,V_i = M_f\,V_f$ | — (mismas unidades de $V$ en ambos lados) | Dilución: los moles de soluto no cambian al agregar solvente |

Camino de conversión **M → m** (base: 1 L de solución): $n_{\text{soluto}} = M \cdot 1\ \text{L}$ → $m_{\text{solución}} = \rho \cdot 1000\ \text{mL}$ → restar la masa del soluto → dividir $n_{\text{soluto}}$ por los kg de solvente.

Camino **m → M** (base: 1 kg de solvente): $n_{\text{soluto}} = m \cdot 1\ \text{kg}$ → $m_{\text{solución}} = 1000\ \text{g} + n\,\mathcal{M}$ → $V = m_{\text{solución}}/\rho$ → dividir $n_{\text{soluto}}$ por los L de solución.

#### Solubilidad de gases (Chang 12.4–12.5)

| N° | Fórmula | Unidades | Para qué |
|---|---|---|---|
| S12.9 | $c = k\,P$ | $c$ en mol/L, $P$ en atm, $k$ en mol/(L·atm) | Ley de Henry: la solubilidad de un gas es proporcional a su presión parcial |
| S12.10 | Gases: solubilidad **baja** al subir $T$ | — | Por eso el agua caliente retiene menos O₂ (contaminación térmica) |

#### Presión de vapor (Chang 12.6)

| N° | Fórmula | Unidades | Para qué |
|---|---|---|---|
| S12.11 | $\Delta P = P_1^\circ - P_1 = X_2\,P_1^\circ$ | atm o mmHg | Descenso de la presión de vapor con soluto no volátil (sale de Raoult con $X_1 = 1 - X_2$) |
| S12.12 | $P_A = X_A P_A^\circ \quad;\quad P_B = X_B P_B^\circ \quad;\quad P_T = P_A + P_B$ | atm o mmHg | Dos componentes volátiles (solución ideal) |
| S12.13 | $Y_A = \dfrac{P_A}{P_T}$ | adimensional | Fracción molar de A en el **vapor** (Dalton): el vapor se enriquece en el más volátil, base de la destilación fraccionada |
| S12.14 | Desviación positiva: $P_T >$ Raoult; negativa: $P_T <$ Raoult | — | Positiva si las atracciones A–B son más débiles que A–A y B–B; negativa si son más fuertes |

#### Punto de ebullición, de congelación y presión osmótica (Chang 12.6)

| N° | Fórmula | Unidades | Para qué |
|---|---|---|---|
| S12.15 ✓ PDF | $\Delta T_b = K_b\,m$ , con $\Delta T_b = T_b - T_b^\circ$ | °C ($K_b$ en °C/m; agua: 0,52) | Aumento del punto de ebullición |
| S12.16 ✓ PDF | $\Delta T_f = K_f\,m$ , con $\Delta T_f = T_f^\circ - T_f$ | °C ($K_f$ en °C/m; agua: 1,86) | Descenso del punto de congelación (anticongelante, sal en rutas) |
| S12.17 ✓ PDF | $\pi = M\,R\,T$ | atm ($R = 0{,}0821\ \text{L}\cdot\text{atm/(mol K)}$, $T$ en K) | Presión osmótica; usa **molaridad**, no molalidad |
| S12.18 | $\mathcal{M} = \dfrac{m_{\text{soluto}}}{n_{\text{soluto}}}$ , con $n$ despejado de S12.15–S12.17 | g/mol | Determinar la masa molar de un soluto desconocido |

Algunas constantes (Chang, tabla 12.2):

| Solvente | $T_f^\circ$ (°C) | $K_f$ (°C/m) | $T_b^\circ$ (°C) | $K_b$ (°C/m) |
|---|---|---|---|---|
| Agua | 0 | 1,86 | 100 | 0,52 |
| Benceno | 5,5 | 5,12 | 80,1 | 2,53 |
| Etanol | −117,3 | 1,99 | 78,4 | 1,22 |
| Ácido acético | 16,6 | 3,90 | 117,9 | 2,93 |
| Ciclohexano | 6,6 | 20,0 | 80,7 | 2,79 |

#### Electrolitos (Chang 12.7)

| N° | Fórmula | Unidades | Para qué |
|---|---|---|---|
| S12.19 | $i = \dfrac{\text{n° de partículas en solución}}{\text{n° de unidades disueltas}}$ | adimensional | Factor de van't Hoff: no electrolito $i = 1$; NaCl $i \approx 2$; CaCl₂ $i \approx 3$ (valor real algo menor por pares iónicos) |
| S12.20 | $\Delta T_b = i\,K_b\,m \quad;\quad \Delta T_f = i\,K_f\,m \quad;\quad \pi = i\,M\,R\,T \quad;\quad \Delta P = i\,X_2\,P_1^\circ$ | igual que sin $i$ | Propiedades coligativas de electrolitos (dependen del **número** de partículas) |

---

## Cap. 14 — Equilibrio químico (Chang)

### En el PDF

| Fórmula | Unidades | Qué dice |
|---|---|---|
| $a\,A + b\,B \rightleftharpoons c\,C + d\,D$ | — | Reacción general en equilibrio |
| $K_c = \dfrac{[C]^c\cdot[D]^d}{[A]^a\cdot[B]^b}$ | $[\;]$ en mol/L ($K_c$ se informa sin unidades) | Ley de acción de masas: productos sobre reactivos, cada concentración de equilibrio elevada a su coeficiente estequiométrico |

### Sugerencias (no están en el PDF)

#### Formas de expresar K (Chang 14.2)

| N° | Fórmula | Unidades | Para qué |
|---|---|---|---|
| S14.1 ✓ PDF | $K_P = \dfrac{P_C^{\,c}\cdot P_D^{\,d}}{P_A^{\,a}\cdot P_B^{\,b}}$ | $P$ en atm | Equilibrios en fase gaseosa, con presiones parciales |
| S14.2 ✓ PDF | $K_P = K_c\,(RT)^{\Delta n}$ | $R = 0{,}0821\ \text{L}\cdot\text{atm/(mol K)}$, $T$ en K | $\Delta n$ = moles de gas productos − moles de gas reactivos; si $\Delta n = 0$, $K_P = K_c$ |
| S14.3 | Sólidos y líquidos puros **no** aparecen en $K$ | — | Equilibrios heterogéneos (ej. $\text{CaCO}_3(s) \rightleftharpoons \text{CaO}(s) + \text{CO}_2(g)$: $K_c = [\text{CO}_2]$) |
| S14.4 | Invertir la ecuación $\Rightarrow K' = \dfrac{1}{K}$ | — | La constante de la reacción inversa es la recíproca |
| S14.5 | Multiplicar la ecuación por $n \Rightarrow K' = K^{\,n}$ | — | Ej.: duplicar coeficientes eleva $K$ al cuadrado |
| S14.6 | $K = K_1 \cdot K_2$ | — | Equilibrios múltiples: si la reacción es suma de dos, sus $K$ se **multiplican** (comparar con Hess, S6.18, donde los $\Delta H$ se suman) |

#### Significado de K y dirección de la reacción (Chang 14.4)

| N° | Fórmula | Unidades | Para qué |
|---|---|---|---|
| S14.7 ✓ PDF | $K \gg 1$: favorece productos; $K \ll 1$: favorece reactivos | — | Lectura del valor de $K$ |
| S14.8 ✓ PDF | $Q_c = \dfrac{[C]_0^{\,c}\,[D]_0^{\,d}}{[A]_0^{\,a}\,[B]_0^{\,b}}$ | — | Cociente de reacción: misma forma que $K_c$ pero con concentraciones **no** de equilibrio |
| S14.9 ✓ PDF | $Q_c < K_c \Rightarrow$ avanza hacia productos; $Q_c = K_c \Rightarrow$ equilibrio; $Q_c > K_c \Rightarrow$ avanza hacia reactivos | — | Predecir hacia dónde se desplaza la reacción |
| S14.10 | Tabla ICE: inicial / cambio ($\pm$ coef$\cdot x$) / equilibrio | mol/L | Método para calcular concentraciones de equilibrio a partir de $K_c$ |
| S14.11 | Si $K$ es chico: $[A]_0 - x \approx [A]_0$ | — | Aproximación válida si $x < 5\%$ de $[A]_0$; evita la cuadrática |

#### Factores que afectan el equilibrio (Chang 14.5)

| N° | Cambio | Efecto | ¿Cambia $K$? |
|---|---|---|---|
| S14.12 ✓ PDF | Agregar reactivo / quitar producto | Se desplaza hacia productos | No |
| S14.13 ✓ PDF | Aumentar $P$ (reducir $V$) | Hacia el lado con **menos** moles de gas | No |
| S14.14 ✓ PDF | Aumentar $T$ | Endotérmica ($\Delta H>0$): hacia productos; exotérmica: hacia reactivos | **Sí** (único factor que cambia $K$) |
| S14.15 ✓ PDF | Catalizador | Llega antes al equilibrio, no lo desplaza | No |
| S14.16 ✓ PDF | Agregar gas inerte a $V$ constante | Ningún efecto | No |

Principio de Le Châtelier: si se perturba un sistema en equilibrio, se desplaza en el sentido que contrarresta parcialmente la perturbación.

---

## Cap. 15 — Ácidos y bases (Chang)

### En el PDF

| Fórmula | Unidades | Qué dice |
|---|---|---|
| $2\,\text{H}_2\text{O} \rightleftharpoons \text{H}_3\text{O}^+ + \text{OH}^-$ | — | Autoionización del agua: una molécula le cede un H⁺ a otra |
| $K_w = [\text{H}_3\text{O}^+]\cdot[\text{OH}^-] = [\text{H}^+]\cdot[\text{OH}^-]$ | $[\;]$ en mol/L ($K_w$ sin unidades) | Producto iónico del agua. $\text{H}^+$ y $\text{H}_3\text{O}^+$ son la misma especie escrita de dos formas (el H⁺ en agua está siempre hidratado). El agua no aparece en la expresión: es líquido puro (S14.3) |
| $K_w = 1{,}0 \times 10^{-14}$ | a 25 °C | En agua pura $[\text{H}^+] = [\text{OH}^-] = 1{,}0 \times 10^{-7}$ M. $K_w$ vale para **cualquier** solución acuosa, no solo para agua pura |

### Sugerencias (no están en el PDF)

#### Brønsted y pares conjugados (Chang 15.1)

| N° | Fórmula / dato | Unidades | Para qué |
|---|---|---|---|
| S15.1 | Ácido: **dona** H⁺; base: **acepta** H⁺ | — | Definición de Brønsted-Lowry |
| S15.2 | $\text{HA} + \text{H}_2\text{O} \rightleftharpoons \text{H}_3\text{O}^+ + \text{A}^-$ | — | HA y A⁻ son un **par conjugado** (difieren en un H⁺); igual H₂O y H₃O⁺ |
| S15.3 | Ácido más fuerte ⇒ base conjugada más débil | — | Ej.: HCl es fuerte, Cl⁻ es una base despreciable |

#### Agua, neutralidad y pH (Chang 15.2–15.3)

| N° | Fórmula / dato | Unidades | Para qué |
|---|---|---|---|
| S15.4 | $[\text{H}^+] = \dfrac{K_w}{[\text{OH}^-]}$ | mol/L | Despeje: sabiendo una concentración, se obtiene la otra |
| S15.5 ✓ PDF | Neutra: $[\text{H}^+] = [\text{OH}^-]$; ácida: $[\text{H}^+] > [\text{OH}^-]$; básica: $[\text{H}^+] < [\text{OH}^-]$ | — | Clasificación de soluciones |
| S15.6 ✓ PDF | $\text{pH} = -\log[\text{H}^+]$ | adimensional | Definición de pH (en el PDF, en la misma línea que su inversa S15.9) |
| S15.7 ✓ PDF | $\text{pOH} = -\log[\text{OH}^-] \;\Leftrightarrow\; [\text{OH}^-] = 10^{-\text{pOH}}$ | adimensional / mol/L | Definición de pOH y su inversa |
| S15.8 ✓ PDF | $\text{pH} + \text{pOH} = 14{,}00$ | a 25 °C | Sale de aplicar $-\log$ a $K_w$ |
| S15.9 ✓ PDF | $[\text{H}^+] = 10^{-\text{pH}}$ | mol/L | Pasar de pH a concentración |
| S15.10 | A 25 °C: ácida pH < 7; neutra pH = 7; básica pH > 7 | — | Escala de pH |
| S15.11 | Cifras significativas: los decimales del pH = cifras significativas de $[\text{H}^+]$ | — | Ej.: $[\text{H}^+] = 3{,}2 \times 10^{-4}$ (2 cifras) ⇒ pH = 3,49 (2 decimales) |

#### Fuerza de ácidos y bases (Chang 15.4)

| N° | Fórmula / dato | Unidades | Para qué |
|---|---|---|---|
| S15.12 | Ácidos fuertes: HCl, HBr, HI, HNO₃, HClO₄, H₂SO₄ (1.ª ionización) | — | Se ionizan 100 %: $[\text{H}^+] = $ concentración inicial del ácido |
| S15.13 | Bases fuertes: hidróxidos de los grupos 1A y 2A (NaOH, KOH, Ba(OH)₂…) | — | Se disocian 100 %: $[\text{OH}^-] = $ concentración × n° de OH⁻ por fórmula |

#### Ácidos y bases débiles (Chang 15.5–15.7)

| N° | Fórmula | Unidades | Para qué |
|---|---|---|---|
| S15.14 ✓ PDF | $K_a = \dfrac{[\text{H}^+]\cdot[\text{A}^-]}{[\text{HA}]}$ | — | Constante de ionización ácida: mayor $K_a$ ⇒ ácido más fuerte |
| S15.15 ✓ PDF | $K_b = \dfrac{[\text{BH}^+]\cdot[\text{OH}^-]}{[\text{B}]}$ | — | Constante de ionización básica (ej. NH₃) |
| S15.16 ✓ PDF | $\%\ \text{ionización} = \dfrac{[\text{H}^+]_{\text{eq}}}{[\text{HA}]_0} \times 100\%$ | % | Fracción del ácido que se ioniza |
| S15.17 | Si $[\text{HA}]_0 / K_a > 400$: $\;[\text{H}^+] \approx \sqrt{K_a\,[\text{HA}]_0}$ | mol/L | Aproximación $x \ll [\text{HA}]_0$ (evita la cuadrática; verificar ionización < 5 %) |
| S15.18 ✓ PDF | $K_a \cdot K_b = K_w$ | — | Par conjugado: sabiendo una constante se obtiene la otra |
| S15.19 | $\text{p}K_a = -\log K_a \quad;\quad \text{p}K_a + \text{p}K_b = 14{,}00$ | a 25 °C | Forma logarítmica |

---

## Cap. 16 — Equilibrios ácido-base y equilibrios de solubilidad (Chang) — pendiente

Todavía no se estudió: todo es sugerencia. En la 9.ª ed. el capítulo junta neutralización (titulaciones), amortiguadores y solubilidad.

### Sugerencias (no están en el PDF)

#### Neutralización y titulación (Chang 16.4)

| N° | Fórmula / dato | Unidades | Para qué |
|---|---|---|---|
| S16.1 | $\text{ácido} + \text{base} \rightarrow \text{sal} + \text{agua}$ ; neta (fuerte–fuerte): $\text{H}^+ + \text{OH}^- \rightarrow \text{H}_2\text{O}$ | — | Reacción de neutralización |
| S16.2 | En el punto de equivalencia: $n_{\text{H}^+} = n_{\text{OH}^-}$ | mol | Base de toda titulación: moles de H⁺ aportados = moles de OH⁻ aportados |
| S16.3 | $M_a\,V_a\,x_a = M_b\,V_b\,x_b$ | $V$ en las mismas unidades | $x$ = n° de H⁺ (u OH⁻) por fórmula (HCl: 1; H₂SO₄: 2; Ba(OH)₂: 2). Si ambos son 1: $M_a V_a = M_b V_b$ |
| S16.4 | Normalidad: $N = M \cdot x$ $\;\Rightarrow\;$ $N_a\,V_a = N_b\,V_b$ | eq/L | Misma idea que S16.3 con equivalentes (notación usada en muchas guías argentinas) |
| S16.5 | pH en el punto de equivalencia: fuerte–fuerte = 7; débil–fuerte (ác. débil + base fuerte) > 7; fuerte–débil (ác. fuerte + base débil) < 7 | — | La sal formada hidroliza: A⁻ es básico, BH⁺ es ácido |
| S16.6 | Exceso: $[\text{H}^+] = \dfrac{n_{\text{H}^+} - n_{\text{OH}^-}}{V_a + V_b}$ (o al revés si sobra base) | mol/L | pH antes o después del punto de equivalencia en fuerte–fuerte: el volumen total es la **suma** |
| S16.7 | Indicador: cambia de color en $\text{pH} \approx \text{p}K_{\text{In}} \pm 1$ | — | Elegir uno cuyo viraje contenga el pH de equivalencia (fenolftaleína 8,3–10; rojo de metilo 4,2–6,3) |

#### Ion común y amortiguadores (Chang 16.2–16.3)

| N° | Fórmula / dato | Unidades | Para qué |
|---|---|---|---|
| S16.8 | Efecto del ion común: agregar A⁻ a una solución de HA **reduce** su ionización | — | Le Châtelier aplicado a ácidos débiles |
| S16.9 | $\text{pH} = \text{p}K_a + \log\dfrac{[\text{base conj.}]}{[\text{ácido}]}$ | — | Henderson-Hasselbalch: pH de un amortiguador (buffer) |
| S16.10 | Buffer: ácido débil + su base conjugada (o base débil + su ácido conjugado); máxima eficacia si $\text{pH} \approx \text{p}K_a$ | — | Resiste cambios de pH al agregar poco ácido o base |

#### Equilibrios de solubilidad (Chang 16.6–16.9)

| N° | Fórmula / dato | Unidades | Para qué |
|---|---|---|---|
| S16.11 | $\text{M}_m\text{X}_n(s) \rightleftharpoons m\,\text{M}^{n+} + n\,\text{X}^{m-}$ ; $\;K_{ps} = [\text{M}^{n+}]^m\cdot[\text{X}^{m-}]^n$ | — | Producto de solubilidad (el sólido no aparece) |
| S16.12 | Si $s$ = solubilidad molar: AB: $K_{ps} = s^2$; AB₂: $K_{ps} = 4s^3$; A₂B₃: $K_{ps} = 108\,s^5$ | mol/L | Pasar de $K_{ps}$ a solubilidad y al revés |
| S16.13 | $Q < K_{ps}$: no precipita; $Q = K_{ps}$: saturada; $Q > K_{ps}$: precipita | — | Predicción de precipitación (mismo criterio que $Q_c$ vs $K_c$) |
| S16.14 | Ion común: la solubilidad **baja** si ya hay uno de los iones en solución | — | Ej.: AgCl es menos soluble en NaCl que en agua pura |

---

## Cap. 18 — Energía libre y equilibrio (Chang)

No se estudió el capítulo completo; por ahora solo va la relación con $K$.

### En el PDF

| Fórmula / dato | Qué dice |
|---|---|
| $\Delta G^\circ = -R\,T\,\ln K$ | Energía libre estándar (J/mol) a partir de la constante de equilibrio. $R = 8{,}314$ J/(mol·K), $T$ en K. $\Delta G^\circ < 0$ ⇔ $K > 1$: el equilibrio favorece los productos. Igualándola con $\Delta G^\circ = -nFE^\circ$ sale $E^\circ_{\text{celda}} = \dfrac{RT}{nF}\ln K$ (cap. 19) |

---

## Cap. 19 — Electroquímica (Chang)

En estudio. Para Ingeniería Mecánica es especialmente relevante por la **corrosión** (19.7) y la protección catódica.

### En el PDF

| Fórmula / dato | Qué dice |
|---|---|
| Ánodo (−): oxidación; cátodo (+): reducción | Vocal con vocal (**á**nodo–**o**xidación), consonante con consonante (**c**átodo–**r**educción); también por orden alfabético: A–O, C–R. Los e⁻ van del ánodo al cátodo por el cable |
| $2\text{H}^+ + 2\text{e}^- \rightarrow \text{H}_2$, $\;E^\circ = 0{,}00$ V | Electrodo estándar de hidrógeno: la referencia de la tabla de potenciales |
| Mayor $E^\circ_{\text{red}}$ ⇒ se reduce ⇒ **cátodo** | El que tiene más tendencia a reducirse le saca e⁻ al otro (mejor oxidante); el de menor $E^\circ_{\text{red}}$ es el ánodo |
| $E^\circ_{\text{celda}} = E^\circ_{\text{cátodo}} - E^\circ_{\text{ánodo}}$ | **fem** (fuerza electromotriz) estándar de la celda, en V. Estándar (°): 1 M, gases a 1 atm, 25 °C. Los dos valores son de reducción, tal como figuran en la tabla: no se invierte el signo del ánodo, la resta ya lo hace |
| $E^\circ_{\text{celda}} = 0{,}34 - (-0{,}76) = 1{,}10$ V | Pila de Zn y Cu: Cu²⁺/Cu ($+0{,}34$ V) es el cátodo, Zn²⁺/Zn ($-0{,}76$ V) el ánodo. El "menos menos" hace que se sumen |
| $E^\circ_{\text{celda}} > 0$ ⇒ espontánea | Criterio de espontaneidad: si la fem estándar es positiva, la reacción ocurre tal como está escrita |
| $\Delta G^\circ = -n\,F\,E^\circ_{\text{celda}}$ | Energía libre estándar en J. $n$ (mol de e⁻) × $F$ (96 500 C/mol e⁻) = carga total $q$ en C; C × V = J. La fem es el voltaje máximo de la celda, así que $\Delta G$ es el trabajo eléctrico máximo que puede dar la reacción ($\Delta G$ = energía libre, la disponible para hacer trabajo). El signo − indica que el sistema hace trabajo eléctrico sobre los alrededores. $E^\circ > 0$ ⇔ $\Delta G^\circ < 0$ ⇒ espontánea |
| $q = n\,F = I\,t$ | Carga en C: la corriente $I$ (A = C/s) por el tiempo $t$ (s) da los coulombs que circularon; dividiendo por $F$ se obtienen los mol de e⁻ |
| $E^\circ_{\text{celda}} = \dfrac{R\,T}{n\,F}\,\ln K$ | Constante de equilibrio a partir del potencial estándar. $R = 8{,}314$ J/(mol·K), no 0,0821: como $F$ está en C/mol e⁻, hace falta $R$ en J para que el resultado salga en V (J/C). $T$ en K. $E^\circ > 0$ ⇔ $K > 1$ |
| $I\,t = q \xrightarrow{\div F} \text{mol e}^- \xrightarrow{\div\,\text{e}^-/\text{ion}} \text{mol} \xrightarrow{\times\mathcal{M}} m$ | Electrólisis, masa depositada en el cátodo: los amperes por los segundos dan los coulombs; dividiendo por $F$, los mol de e⁻; dividiendo por los e⁻ que necesita cada ion según la hemirreacción (Cr³⁺ + 3 e⁻ → Cr: 3), los mol de metal; y por la masa molar, los gramos. En una sola fórmula: $m = \dfrac{I\,t\,\mathcal{M}}{n\,F}$ |

### Sugerencias

#### Redox y celdas galvánicas (Chang 19.1–19.2)

| N° | Fórmula / dato | Unidades | Para qué |
|---|---|---|---|
| S19.1 | ~~Oxidación = pierde e⁻; reducción = gana e⁻~~ | — | Ya está en el cap. 4 (bloque RedOx) |
| S19.2 ✓ PDF | Celda galvánica: ánodo (−) se oxida; cátodo (+) se reduce; los e⁻ van del ánodo al cátodo por el cable | — | Signos y sentido de la corriente en una pila |
| S19.3 | Notación: $\text{Zn}(s)\,\vert\,\text{Zn}^{2+}(ac)\,\Vert\,\text{Cu}^{2+}(ac)\,\vert\,\text{Cu}(s)$ | — | Ánodo a la izquierda, cátodo a la derecha, $\Vert$ = puente salino |
| S19.4 | Balanceo por ion-electrón: separar en semirreacciones, balancear átomos (O con H₂O, H con H⁺), cargas con e⁻, igualar e⁻ y sumar | — | Método del Chang; en medio básico, neutralizar H⁺ con OH⁻ al final |

#### Potenciales estándar (Chang 19.3)

| N° | Fórmula / dato | Unidades | Para qué |
|---|---|---|---|
| S19.5 ✓ PDF | $E^\circ_{\text{celda}} = E^\circ_{\text{cátodo}} - E^\circ_{\text{ánodo}}$ | V | Ambos como potenciales de **reducción** de tabla (no invertir el signo) |
| S19.6 ✓ PDF | $E^\circ_{\text{celda}} > 0$ ⇒ reacción espontánea | — | Criterio de espontaneidad |
| S19.7 ✓ PDF | Mayor $E^\circ_{\text{red}}$ ⇒ mejor agente oxidante (se reduce más fácil) | — | Lectura de la tabla: F₂ arriba (oxidante fuerte), Li abajo (reductor fuerte) |
| S19.8 | Multiplicar una semirreacción por un número **no** cambia $E^\circ$ | V | $E^\circ$ es propiedad intensiva (a diferencia de $\Delta H$ y $\Delta G$) |
| S19.9 ✓ PDF | Referencia: $2\text{H}^+ + 2e^- \rightarrow \text{H}_2$, $\;E^\circ = 0{,}00$ V | V | Electrodo estándar de hidrógeno |

#### Termodinámica y ecuación de Nernst (Chang 19.4–19.5)

| N° | Fórmula / dato | Unidades | Para qué |
|---|---|---|---|
| S19.10 ✓ PDF | $\Delta G^\circ = -n\,F\,E^\circ_{\text{celda}}$ | J ($F = 96\,500$ C/mol e⁻, $n$ = mol de e⁻) | Relación entre energía libre y potencial |
| S19.11 | $E^\circ_{\text{celda}} = \dfrac{0{,}0592\ \text{V}}{n}\,\log K$ | V, a 25 °C | Constante de equilibrio a partir del potencial |
| S19.12 | $E = E^\circ - \dfrac{0{,}0592\ \text{V}}{n}\,\log Q$ | V, a 25 °C | Ecuación de Nernst: potencial en condiciones no estándar |
| S19.13 | Pila de concentración: mismo electrodo, distinta concentración; $E^\circ = 0$ y $E = -\dfrac{0{,}0592}{n}\log\dfrac{[\text{diluida}]}{[\text{concentrada}]}$ | V | La corriente circula hasta igualar concentraciones |

#### Corrosión (Chang 19.7)

| N° | Dato | Para qué |
|---|---|---|
| S19.14 | Herrumbre: el Fe se oxida (ánodo) y el O₂ se reduce en presencia de agua (cátodo): $\text{O}_2 + 4\text{H}^+ + 4e^- \rightarrow 2\text{H}_2\text{O}$ | Por qué el hierro se corroe más en ambiente húmedo y ácido o salino |
| S19.15 | Protección catódica: unir el Fe a un metal más activo (menor $E^\circ_{\text{red}}$: Zn, Mg) que actúa como **ánodo de sacrificio** | Galvanizado, ánodos de Mg en cascos de barcos y cañerías enterradas |
| S19.16 | Pasivación: capa de óxido protectora (Al₂O₃ en el aluminio, Cr₂O₃ en el acero inoxidable) | Por qué el aluminio y el inoxidable resisten la corrosión pese a ser activos |

#### Electrólisis (Chang 19.8)

| N° | Fórmula / dato | Unidades | Para qué |
|---|---|---|---|
| S19.17 ✓ PDF | $Q = I\,t$ | C ($I$ en A, $t$ en s) | Carga que circula |
| S19.18 ✓ PDF | $n_{e^-} = \dfrac{I\,t}{F}$ | mol de e⁻ ($F = 96\,500$ C/mol e⁻) | Moles de electrones transferidos |
| S19.19 ✓ PDF | $m = \dfrac{I\,t\,\mathcal{M}}{n\,F}$ | g ($n$ = e⁻ por ion; ej. Cu²⁺: 2) | Masa depositada en el electrodo (leyes de Faraday): galvanoplastia, refinación |
| S19.20 | En electrólisis el cátodo es (−) y el ánodo (+): al revés que en la pila | — | La reducción sigue en el cátodo; lo que cambia es el signo |

---

## Constantes y conversiones generales

| N° | Dato | Para qué |
|---|---|---|
| SC.1 | $R = 0{,}0821\ \text{L}\cdot\text{atm/(mol K)} = 8{,}314\ \text{J/(mol K)}$ | Elegir según las unidades: L·atm para $\pi$ y gases; J para energía (S6.7) |
| SC.2 | $1\ \text{atm} = 760\ \text{mmHg} = 760\ \text{torr} = 101\,325\ \text{Pa}$ | Presiones de vapor suelen venir en mmHg |
| SC.3 | $T\,[\text{K}] = t\,[{}^\circ\text{C}] + 273{,}15$ | $R\,T$ siempre en K |
| SC.4 | $P^\circ_{\text{agua}}(25\ {}^\circ\text{C}) = 23{,}76\ \text{mmHg}$ | Dato frecuente en problemas de Raoult |
| SC.5 | $\rho_{\text{agua}} \approx 1\ \text{g/mL}$ | Soluciones acuosas diluidas: 1 L ≈ 1 kg de solvente ⇒ $M \approx m$ |

---

## Espacio en la hoja: candidatos a recortar

Con los caps. 16 y 19 la carilla puede no alcanzar. Si hace falta lugar, los primeros candidatos a reducir (se evalúa en su momento, no antes) son:

1. Tabla de calores específicos (Calorimetría, cap. 6).
2. Tabla de entalpías estándar de formación (Entalpía de reacción, cap. 6).
3. Bloque del puente de hidrógeno (cap. 11).

---

## Errores comunes

| Error | Corrección |
|---|---|
| Usar $w = -P\Delta V$ en L·atm y sumarlo a un $q$ en J | Convertir: $1\ \text{L}\cdot\text{atm} = 101{,}3\ \text{J}$ |
| Olvidar el signo menos de $w = -P\Delta V$ | Expansión ($\Delta V > 0$) ⇒ el sistema **pierde** energía ⇒ $w < 0$ |
| En $\Delta H^\circ_{\text{rxn}}$ no multiplicar por los coeficientes | Cada $\Delta H^\circ_f$ está en kJ/mol: multiplicar por los moles de la ecuación balanceada |
| Hacer reactivos − productos con $\Delta H^\circ_f$ | Siempre **productos − reactivos** (la excepción es con energías de enlace, S6.19) |
| En calorimetría, olvidar que $q_{\text{rxn}} = -q_{\text{agua}}$ | Si el agua se calienta ($\Delta t>0$), la reacción es exotérmica ($q_{\text{rxn}}<0$) |
| En una mezcla, poner $\Delta t$ siempre positivo | Usar $\Delta t = t_f - t_i$ de cada cuerpo con su signo y plantear $\sum q = 0$ |
| Usar $q = m\,s\,\Delta t$ durante un cambio de fase | En el cambio de fase $\Delta t = 0$: usar $q = n\,\Delta H_{\text{fus/vap}}$ |
| $\Delta E = \Delta H - RT\Delta n$ con $\Delta n$ de todas las especies | $\Delta n$ cuenta **solo los gases** |
| Molalidad dividiendo por kg de **solución** | Es por kg de **solvente** |
| Molaridad dividiendo por L de **solvente** | Es por L de **solución** |
| Confundir $m$ (molalidad) con $m$ (masa) | Por contexto: molalidad en mol/kg; masa en g o kg |
| Usar molaridad en $\Delta T_b$ / $\Delta T_f$ o molalidad en $\pi$ | $\Delta T$ con **m** (molalidad); $\pi$ con **M** (molaridad) |
| Olvidar $i$ con electrolitos | NaCl en agua da 2 partículas: el efecto coligativo es ≈ el doble |
| $T$ en °C dentro de $RT$ | Siempre en K |
| En Clausius-Clapeyron, $\Delta H_{\text{vap}}$ en kJ/mol con $R = 8{,}314$ | Pasar $\Delta H_{\text{vap}}$ a J/mol |
| En la densidad de la celda, $a$ en pm o Å | Pasar $a$ a cm antes de elevar al cubo |
| Confundir $a = 4r/\sqrt{3}$ (BCC) con $a = 2\sqrt{2}\,r$ (FCC) | BCC: se tocan sobre la diagonal del **cubo**; FCC: sobre la diagonal de la **cara** |
| Incluir sólidos o líquidos puros (o el agua solvente) en $K$ | No van: su "concentración" es constante |
| Usar concentraciones iniciales en $K_c$ | $K_c$ va con concentraciones **de equilibrio**; con las iniciales se calcula $Q_c$ |
| Olvidar elevar cada concentración a su coeficiente | $[C]^c$, no $c\,[C]$ |
| Usar moles en lugar de mol/L | Dividir por el volumen del recipiente antes de reemplazar en $K_c$ |
| Creer que cambiar concentraciones o presión cambia $K$ | Solo la temperatura cambia $K$ |
| Creer que $K_w = 10^{-14}$ vale solo en agua pura | Vale en **toda** solución acuosa a 25 °C |
| Poner $[\text{H}_2\text{O}]$ en $K_w$ | El agua es líquido puro: no va |
| Pensar que $\text{H}^+$ y $\text{H}_3\text{O}^+$ son especies distintas | Son la misma; se usan indistintamente |
| En una titulación con H₂SO₄ o Ba(OH)₂, usar $M_a V_a = M_b V_b$ | Multiplicar por el n° de H⁺ u OH⁻ por fórmula (S16.3) |
| Calcular el pH después de mezclar con el volumen de una sola solución | El volumen es la suma $V_a + V_b$ |
| Invertir el signo del $E^\circ$ del ánodo y además restarlo | O se invierte y se suma, o se resta tal cual de tabla (S19.5): nunca las dos cosas |
| Multiplicar $E^\circ$ por los coeficientes al balancear | $E^\circ$ no se multiplica (S19.8) |
| En electrólisis, $t$ en minutos u horas | $t$ en segundos para $Q = I\,t$ en C |

---

## Compilación

```bash
cd quimica_general/hoja_formulas
make          # -> build/hoja_formulas.pdf (falla si pasa de una carilla)
make clean
```

Es LaTeX directo (no pasa por `pipeline_pdf/`): una hoja de fórmulas necesita control fino del espacio (3 columnas, márgenes mínimos) que la plantilla de pandoc no da. El `Makefile` fija `SOURCE_DATE_EPOCH` para que el PDF salga idéntico si el contenido no cambió.

Para agregar una fórmula: en `hoja_formulas.tex`, dentro del capítulo (`\capitulo{…}`) y subtema (`\subtema{…}`) correspondiente, `\f{fórmula}{unidades}`; aclaraciones mínimas con `\nota{…}`.

Nota para el `.md`: dentro de fórmulas (`$…$`) no usar `·` ni `°` como caracteres: la KaTeX de la vista previa de VS Code falla con `·` dentro de `\text{}`. Usar `\cdot` y `{}^\circ`.

---

*Fuentes: `Guia QUIMICA GENERAL 2020 FINAL.pdf` (tabla de entalpías estándar de formación, pág. 52 del PDF); Chang, R. — Química, 9.ª ed. en español (McGraw-Hill, ISBN 978-970-10-6111-4; traducción de la 9.ª ed. en inglés, ISBN 978-0-07-298060-8) (cap. 6 «Termoquímica», cap. 11 «Fuerzas intermoleculares y líquidos y sólidos», cap. 12 «Propiedades físicas de las disoluciones», cap. 14 «Equilibrio químico», cap. 15 «Ácidos y bases», cap. 16 «Equilibrios ácido-base y equilibrios de solubilidad», cap. 19 «Electroquímica»; complementos de cap. 4 (dilución), cap. 9 (energías de enlace)).*
