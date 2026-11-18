# Diseño de la Entrega 2 Rev. 1 y de la Entrega 3 — TP Final Ingeniería Mecánica I

> Especificación previa a la redacción (Fase 0). Un solo texto fuente genera las dos entregas; describe el prototipo construido (`08_modelo_2/`). Fuentes leídas: `Entrega 2 TP Final S1091 S1092.pdf` (manual de formato), `Entrega_2_Reentrega_0_S1091_Grupo_1.pdf` (informe reprobado), `Caratula Entrega 2 TP FINAL Mecanica 1 S1092 S1091.docx` (carátula oficial), `00_consignas/Entrega 1 TP Final S1091 S1092.pdf` y la documentación de `08_modelo_2/`.

## 0. Decisiones tomadas (16 y 17/nov/2026)

Aprobado. Las dudas de la sección 11 se resolvieron así, y esto prevalece sobre lo que dicen las secciones siguientes:

| Duda | Decisión |
|---|---|
| 1. Textos internos en los planos | Planos regenerados con el rótulo «Prototipo»; sin «Modelo 2.0», «(concepto, 4.1)» ni «(resultados.json)». Además se corrigió `a_pdf.sh`: la fecha fija rompía la tabla xref de los PDF |
| 2. Escala de las láminas | A4 apaisado, con la aclaración en el epígrafe |
| 3. Fuente del PDF | Times New Roman instalada (fuentes de Microsoft, verificadas contra el paquete de Ubuntu): PDF y Word usan la misma |
| 4. Pie | Texto + número en todas las páginas del cuerpo; la carátula, con su pie oficial (sin el campo de número) |
| 5. Fuentes sin verificar | Se quitó la rotura de la tira (55 MPa sin fuente) del Marco teórico y de los Resultados; no se cita el manual de FDM |
| 6. Fuentes web | Con nota al pie y listadas en «Links de interés» |
| 7. Lectura del ancho | Causas probables: chapita sin colocar, flexión de la hoja, tramo medido (inicio cortado con tijera, primeras vueltas más irregulares que las últimas) e irregularidades de la botella |
| 8. Dónde se midió | «En cinco puntos de las tiras obtenidas» |
| 9. Campo «Resumen» | E3: el abstract; E2 (sin abstract): vacío |
| 10. python-docx | Instalado; la carátula se completa con python-docx |
| 11. Tamaño de la carátula | A4, como todo el documento |
| 12. Google Docs | Pendiente: prueba de subida del `.docx` |

Varilla de 7,3 mm: se menciona como dato; el prisionero del zócalo la traba firme y no afecta el funcionamiento. El tornillo del mango ya no roza la tira (se invirtió, con la cabeza Allen abajo): no se menciona.

## 1. Datos de las entregas

| | Entrega 2, Revisión 1 | Entrega 3 (final) |
|---|---|---|
| Archivo | `Entrega_2_Reentrega_1_S1091_Grupo_1` (.pdf y .docx) | `S1091-G1-E3` (.pdf y .docx) |
| Línea de la carátula | GRUPO 01 - CURSO S1091 - ENTREGA N°2 - REVISIÓN N°1 | GRUPO 01 - CURSO S1091 - ENTREGA N°3 - REVISIÓN N°0 |
| Abstract, Resultados, Conclusión | No | Sí |
| Planos y Bibliografía | Sí (obligatorios) | Sí (obligatorios) |
| `make` | `make e2` | `make e3` |

Comunes: título «Cortadora Manual de Botellas PET»; Profesor: Abud, Moises Rolando; ATP: Caceres Guido, Jeronimo; alumnos y legajos como en la reentrega 0: Burelli, Angelo (233.072-6); Fernandez, Lautaro (260.809-1); Franco Solignac, Matias (260.815-7); Kainer, Martin (260.825-0); Ledesma Blanco, Camila Cecilia (260.827-3); Paredes, Sergio Gaston (260.861-3).

## 2. Correcciones del ATP y cómo se atienden

| Corrección | Dónde se atiende | Control automático |
|---|---|---|
| E2: falta Planos/Diagramas | Sección 6 «Planos», con las 4 láminas A3 de `08_modelo_2/planos/` a página completa, apaisadas, en las dos versiones | El build falla si la sección falta, está vacía o no tiene las 4 láminas |
| E2: falta Bibliografía (además de las notas al pie) | Sección final «Bibliografía» (APA, alfabética) + «Links de interés», en las dos versiones | El build falla si falta o está vacía |
| E1: Introducción innecesariamente extensa | 2 párrafos breves: problema, propuesta y alcance | ≤ 150 palabras y ≤ 2 párrafos |
| E1: Estado del arte sin nota al pie | Cada dato de fuente externa con nota al pie numerada, también en el Estado del arte | Toda nota con fuente tiene URL o DOI; notas ↔ Bibliografía ∪ Links, en los dos sentidos; Bibliografía en orden alfabético |
| E1: Objetivos y Marco teórico correctos | Cambio mínimo: misma estructura y redacción en lo que sigue valiendo (sección 5) | — |
| E1: Desarrollo no se pedía | En E2/E3 sí se pide: Desarrollo completo | — |

## 3. Índice propuesto

Página 2: título del trabajo y, debajo, el índice. La numeración 1–6 es la misma en las dos versiones; Resultados y Conclusión solo existen en E3, después de Planos, así que no corren ningún número.

| E3 (final) | E2 Rev. 1 |
|---|---|
| Carátula | Carátula |
| Título · Índice | Título · Índice |
| Abstract (sin número) | — |
| 1. Introducción | 1. Introducción |
| 2. Objetivos (Principal · Secundarios) | 2. Objetivos (Principal · Secundarios) |
| 3. Estado del arte | 3. Estado del arte |
| 4. Marco teórico | 4. Marco teórico |
| 5. Desarrollo del diseño | 5. Desarrollo del diseño |
| 5.1 Configuración general y criterios de diseño | 5.1 (ídem) |
| 5.2 Cabezal de corte y ancho constante | 5.2 |
| 5.3 Accionamiento y carrete | 5.3 |
| 5.4 Autoavance y lastre | 5.4 |
| 5.5 Verificaciones del modelo digital | 5.5 |
| 5.6 Materiales, fabricación y montaje | 5.6 |
| 6. Planos (Láminas 1 a 4) | 6. Planos (Láminas 1 a 4) |
| 7. Resultados (7.1 Ancho de tira medido · 7.2 Observaciones de funcionamiento · 7.3 Valores calculados del modelo) | — |
| 8. Conclusión | — |
| Anexo A. Piezas impresas y comerciales | Anexo A |
| Anexo B. Secuencia de armado | Anexo B |
| Bibliografía · Links de interés | Bibliografía · Links de interés |

Contenido de cada bloque:

- **Introducción** (≤ 150 palabras): (1) problema: transformar botellas PET en tiras continuas; el corte manual da ancho irregular y expone al operador al filo. (2) propuesta y alcance: dispositivo manual en el que la propia tira, enrollada en un carrete con manivela, hace girar la botella contra una cuchilla fija; se diseñó, se construyó un prototipo impreso en PLA y se evaluó el corte del tramo cilíndrico.
- **5.1** Principio de tiro, disposición general (botella vertical sobre varilla y tapa perforada, cabezal, ojal fijo, torre con dos 608ZZ, base de MDF), criterios de diseño (ancho constante, seguridad, una sola entrada manual, piezas imprimibles sin soportes). Figura 1: conjunto. **Un párrafo de «alternativas evaluadas»**: transmisión por rodillo de fricción, engranajes y husillo con carro, descartada por riesgo de deslizamiento y porque cargaba el cuello.
- **5.2** Ranura entre labios (0,85 mm), chapita de apoyo, calce que fija `w`, hoja y pisador; por qué el ancho no depende del diámetro de la botella; calces de 7 a 10 mm según el espesor de pared (tabla de Function 3D / Precious Plastic, con nota). Figura 2: detalle del cabezal.
- **5.3** Carrete de eje vertical, manivela de 80 mm, ojal fijo; `F = T·r/(i·R)`; tabla de opciones de transmisión (multiplicación 1:6,6 de una bobinadora de filamento a manivela, **carrete directo 1:1**, reducción 1:3), con valores calculados por script desde los parámetros del modelo; tiro de 40 N presentado como hipótesis de diseño.
- **5.4** Equilibrio axial: peso de la botella frente a la componente axial del rozamiento en los labios y en la tapa; lastre estimado (115 g); vaso de lastre opcional sobre la tapa.
- **5.5** Choques en el armado (inicio y fin del corte), giro de la manivela en 36 posiciones, lugar para la mano (46 mm), secuencia de 26 pasos sin interferencias, 15 piezas sin soportes; todo como verificaciones del modelo digital, en pasado.
- **5.6** PLA (FDM), MDF, piezas comerciales; 194 g y ~6,1 h de impresión estimados; montaje en 7 etapas. **Varilla de acero de Ø7,3 mm** en el prototipo (el diseño considera Ø8 mm): una frase, sin dramatizar. Chapita sin colocar en el prototipo: una frase (el resultado se discute en 7).
- **7.1** Tabla de la sección 6 de este documento + lectura. **7.2** Observaciones: corte continuo y varias tiras con botellas relativamente lisas; avance parejo con giro constante; arranque acompañado a mano hasta que el borde se asienta; el corte termina en el hombro (límite de uso previsto: se corta el tramo cilíndrico); peso adicional sobre la tapa como lastre. **7.3** Tabla rotulada «valores calculados»: fuerza en la mano 13,2 N (con T = 40 N, hipótesis), rotura de la tira 124 N (3,1 veces el tiro), hélice 1,86°, ancho por construcción 9,000 mm.
- **8. Conclusión** (2–3 párrafos, ≤ media carilla): corte continuo, cumplido; ancho uniforme, parcial, y por qué; limitaciones (chapita sin colocar, dispersión, arranque asistido, solo tramo cilíndrico, botellas con nervaduras); mejora concreta: colocar la chapita metálica y volver a medir.
- **Abstract** (150–250 palabras, en pasado, sin citas): qué, cómo, qué se encontró (ancho medio 9,83 mm) y qué significa. Se escribe al final.
- **Anexo A**: 15 piezas impresas (función, cantidad) y lista de comerciales. **Anexo B**: 7 etapas / 26 pasos resumidos, con 3 o 4 vistas de `instructivo/pasos/`.

## 4. Mapa: reentrega 0 → nueva versión

| Sección de la reentrega 0 | Acción | Qué cambia |
|---|---|---|
| Carátula | Se conserva | Carátula oficial de la cátedra completada; línea de entrega según la versión |
| Índice | Se ajusta | Generado automáticamente; mismo estilo de fuente que el cuerpo (en la reentrega 0 salió en otra fuente) |
| 1. Introducción (3 párrafos, ~170 palabras, en futuro) | Se reescribe | 2 párrafos, ≤ 150 palabras, en pasado lo hecho |
| 2. Objetivos — principal | Se conserva | Textual |
| 2. Objetivos — secundarios 1 a 5 | Se ajustan | Cambio mínimo; ver tabla de abajo |
| 3. Estado del arte | Se ajusta | Tylman y Dzierżek (2020) y Meraj et al. (2024) se conservan, con nota al pie en la primera mención (ya la tenían; se mantiene); se suman las cortadoras abiertas (PETALOT, Precious Plastic, Low-tech Lab, Appropedia) con nota. Los dos últimos párrafos (propuesta con rodillo, husillo y carro) se reescriben: describen el dispositivo construido |
| 4. Marco teórico | Se ajusta | Misma estructura (intro + párrafos con título en negrita); ver tabla de abajo |
| 5. Desarrollo del diseño (5.1–5.5) | Se reescribe | Describe el dispositivo construido (sección 3); el concepto anterior queda en un solo párrafo de alternativas en 5.1 |
| Fórmulas `nb·Db = nr·Dr`, `i = z₂/z₁`, `v = L·nh`, `a = L·Db/(i·Dr)` | Se eliminan | No corresponden al mecanismo construido |
| Notas KHK (engranajes), Thomson (husillo), OpenStax 11.1 (rodadura) | Se eliminan | Ya no hay datos que las usen |
| — | Se agrega | 6. Planos, Anexos A y B, Bibliografía y Links de interés (ambas versiones); Abstract, 7. Resultados y 8. Conclusión (E3) |

**Objetivos secundarios (cambio mínimo):**

| # | Reentrega 0 | Nueva versión |
|---|---|---|
| 1 | Diseñar un sistema de sujeción exterior del cuello que permita el giro de la botella y su retención axial, evaluando la necesidad de apoyos complementarios para mantener su estabilidad durante el corte. | Diseñar un sistema de sostén interior de la botella, mediante una varilla y su tapa perforada, que permita su giro y su descenso axial, con apoyo del borde en el cabezal de corte para mantener su estabilidad durante el corte. |
| 2 | Desarrollar un sistema de guiado longitudinal que permita desplazar la botella frente a una cuchilla fija, con el propósito de obtener una tira de ancho uniforme. | Desarrollar un cabezal de corte que guíe el borde y la pared de la botella frente a una cuchilla fija, con el propósito de obtener una tira de ancho uniforme. |
| 3 | Integrar una transmisión manual mediante manivela, rodillo por fricción, engranajes reductores y husillo, que coordine el movimiento de rotación de la botella con su avance longitudinal. | Integrar una transmisión manual mediante manivela y carrete, en la que la propia tira haga girar la botella y el avance longitudinal resulte del apoyo del borde en la guía. |
| 4 | Incorporar regulaciones y elementos intercambiables que permitan adaptar el dispositivo a un rango definido de diámetros, longitudes y formatos de cuello de botellas PET. | Incorporar elementos intercambiables que permitan adaptar el ancho de la tira al espesor de pared de botellas PET de distintos diámetros con tapa de 28 mm. |
| 5 | Construir un prototipo experimental para evaluar la sujeción, la transmisión del movimiento y la continuidad y uniformidad del corte. | Construir un prototipo experimental para evaluar el sostén de la botella, la transmisión del movimiento y la continuidad y uniformidad del corte. |

**Marco teórico (misma estructura, contenido de lo que se usa):**

| Párrafo de la reentrega 0 | Nueva versión | Nota al pie |
|---|---|---|
| Sujeción y guiado | **Sostén y guiado**: varilla y tapa centran; labios y guía fijan la pared | — |
| Transmisión por fricción (`Ft ≤ μs·N`) | **Rozamiento**: misma ley, aplicada a los labios, a la tapa sobre la varilla y al autoavance | OpenStax 6.2 |
| Coordinación del movimiento | **Momento en la manivela** (`F = T·r/(i·R)`) y **equilibrio axial** de la botella | OpenStax 10.6 y 12.1 |
| — | **Geometría de la hélice** (`tan α = w/(π·D)`), por desarrollo del cilindro | — (deducción propia) |
| Rigidez y comportamiento del envase | **Tensión normal**: rotura de la tira `σ = T/(w·t)` | OpenStax 12.3; resistencia del PET: ver duda 5 |
| Materiales y fabricación | **Fabricación por impresión FDM en PLA**: orientación de capas, voladizos, impresión sin soportes | Fuente FDM: ver duda 5 |

## 5. Estadística del ancho medido

Calculada con `anchos_medidos.py` (5 puntos, calce de 9 mm, criterio 9 ± 0,5 mm):

| Magnitud | Valor |
|---|---|
| Mediciones (mm) | 9,79; 10,79; 8,73; 9,36; 10,47 |
| Promedio (mm) | 9,83 |
| Desvío estándar muestral, n − 1 (mm) | 0,83 |
| Mínimo / máximo (mm) | 8,73 / 10,79 |
| Rango (mm) | 2,06 |
| Promedio − nominal (mm) | 0,83 |
| Puntos dentro de 9 ± 0,5 mm | 2 de 5 |

**Lectura propuesta:** el ancho medio supera el nominal en 0,83 mm y la dispersión excede ±0,5 mm. Causa más probable (no demostrada): la chapita metálica no se colocó y el borde apoya sobre el PLA, lo que según el modelo ensancha la tira hasta 0,5 mm; a eso se suman las irregularidades de la botella. Ver duda 7: el exceso medido es mayor que esos 0,5 mm y un punto quedó por debajo del nominal.

## 6. Valores calculados que usa el texto

Todos salen de `08_modelo_2/resultados.json` o de `parametros.py`; ninguno se escribe a mano. En el `.md` cada número va marcado con su clave, y un filtro comprueba en cada build que el número escrito coincide con la fuente (si cambia el modelo, el build falla en vez de quedar desactualizado).

| Valor | Fuente | Dónde |
|---|---|---|
| Tira 9 mm · 5,53 m · 20 vueltas de botella · rollo de 16 a 26,4 mm · 42 vueltas de manivela | `resultados.json` → `funcionamiento` | 5.3 |
| Fuerza en la mano 13,2 N · tiro admisible 61 N | ídem | 5.3, 7.3 |
| Opciones de transmisión (1:6,6, 1:1, 1:3) | script que aplica `F = T·r/(i·R)` a `parametros.py` | 5.3 |
| Rotura de la tira 124 N (3,1 veces el tiro) | `resultados.json` | 7.3 |
| Hélice 1,86° · ancho por construcción 9,000 mm | `resultados.json` | 4, 7.3 |
| Rozamiento axial 0,23 + 0,40 = 0,63 N · lastre 115 g | `resultados.json` | 5.4 |
| Choques, 36 posiciones, 46 mm, 26 pasos, 15 piezas sin soportes, 194 g / 6,1 h | `resultados.json` | 5.5, 5.6 |
| Tiro de diseño 40 N | `parametros.py` (`T_DISENO`), siempre como hipótesis | 5.3, 7.3 |

## 7. Figuras y planos

Solo imágenes que ya existen; numeradas, con epígrafe.

| | Archivo | Sección |
|---|---|---|
| Figura 1 | `08_modelo_2/figuras/conjunto.png` (recortado el margen blanco al insertarlo, sin modificar el archivo) | 5.1 |
| Figura 2 | `08_modelo_2/figuras/detalle_cabezal.png` | 5.2 |
| Figura 3 | una vista del carrete y la manivela de `instructivo/pasos/` (a elegir al redactar) | 5.3 |
| Figuras del Anexo B | 3 o 4 vistas de `instructivo/pasos/` | Anexo B |
| Láminas 1 a 4 | `08_modelo_2/planos/01_conjunto.pdf` … `04_esquema.pdf`, vectoriales, una por página A4 apaisada (en Word, PNG a 300 ppp de esos mismos PDF) | 6 |

## 8. Bibliografía y Links de interés

Cada nota al pie lleva la referencia APA completa (como en la reentrega 0, cuyas citas el ATP aprobó).

**Bibliografía (APA, alfabética):** Meraj et al. (2024); OpenStax (2016a) 12.1 *Conditions for static equilibrium*; OpenStax (2016b) 6.2 *Friction*; OpenStax (2016c) 12.3 *Stress, strain, and elastic modulus*; OpenStax (2016d) 10.6 *Torque*; Tylman y Dzierżek (2020); y las fuentes de la duda 5, si se verifican.

**Links de interés:** Function 3D, PETALOT; Precious Plastic, *PET filament from bottles*; Low-tech Lab, *Découpeuse de bouteille plastique*; Appropedia, *3D printed improved PET bottle stripper*; Engineering Toolbox, *Friction coefficients*; Irimie, *Cell Spool Winder* (MakerWorld), si se mantiene la opción 1:6,6 en la tabla de 5.3.

Toda URL se verifica antes de compilar la versión final.

## 9. Formato e infraestructura

- **Perfil nuevo `pipeline_pdf/tp_mecanica/`**, análogo a `lab_fisica/`: `tp.mk` (nombre de salida desde `pdf.yaml` según la versión), `pdf.yaml`/`docx.yaml` (reemplazan a `base.yaml`/`docx.yaml`), `tp-mecanica.lua` (carátula, página de título e índice, planos, bloques por versión), `preambulo.tex`, `docx_tp.py` (Word) y `controles_tp.py`. No se toca nada compartido; si hiciera falta, se recompilan y comparan todos los documentos que lo usan.
- **Documento** en `03_entrega_2/`: `informe.md` (único texto), `pdf.yaml` (datos de carátula, versiones, límites y vocabulario controlado), `Makefile` corto con `SOURCE_DATE_EPOCH`, `anchos_medidos.py`. `make e2` y `make e3` → PDF; `make docx` → los dos Word; `make` → los cuatro archivos + controles.
- **Flag de versión**: los bloques solo de E3 van en `::: {.solo-e3}` … `:::`; el filtro los quita en E2. Un solo `.md`.
- **Formato**: Times 12, justificado en todo el cuerpo, interlineado 1,15, A4; notas al pie reales (LaTeX y Word); tablas y epígrafes en 11, notas en 10. Pie en el cuerpo: «Ing. Mecánica - Grupo 01 - Curso S1091 - Año 2026» + número de página (duda 4). La carátula cuenta como página 1 sin número, como en la reentrega 0.
- **Carátula**: en Word, la oficial misma: sus párrafos, su logo, sus estilos y su pie, completados (marcadores rojos `XX`/`X`/«(Reemplazar por el título)» reemplazados y en negro), en su propia sección con sus márgenes. En el PDF, réplica fiel con las mismas medidas, tamaños y posiciones. El campo «Resumen:» queda tal cual (duda 9).
- **Word compatible con Google Docs**: formato escrito en cada párrafo y celda (Google Docs ignora parte de los estilos), imágenes en línea, índice como campo real con las entradas ya cargadas (para que no aparezca vacío), planos en secciones apaisadas.
- **Versionado**: `build/*.pdf` se versiona (regla del pipeline); `.docx`, `.tex` y PNG de los planos para Word, no. Sin `git add -f`, sin push.

## 10. Controles (el build falla si alguno no pasa)

| Control | Qué comprueba |
|---|---|
| Secciones obligatorias | Planos (con 4 láminas) y Bibliografía presentes y no vacías en las dos versiones; Abstract, Resultados y Conclusión presentes solo en E3 |
| Citas ↔ Bibliografía | Cada nota con fuente tiene URL/DOI; el conjunto de fuentes de las notas es igual al de Bibliografía ∪ Links de interés; Bibliografía en orden alfabético |
| Vocabulario | Ningún término prohibido fuera del párrafo de alternativas: rodillo motriz, transmisión por fricción, engranajes reductores, husillo, tuerca fija, carro, guías paralelas, sujeción exterior del cuello, `a = L·Db/(i·Dr)`, «se propone», «se prevé», «se evaluará», Maty, [SUP], [PROTO], make, verificar.py, H1–H7, «modelo 2.0», «modelo 1», nombres de carpetas y de scripts |
| Introducción | ≤ 150 palabras y ≤ 2 párrafos |
| Abstract (E3) | 150–250 palabras, 1 párrafo |
| Conclusión (E3) | 2 o 3 párrafos y ≤ 250 palabras (media carilla) |
| Valores | Cada número marcado coincide con `resultados.json`, `parametros.py` o `anchos_medidos.py` |
| Referencias | Sin referencias LaTeX sin resolver; toda imagen existe; toda figura citada en el texto |
| PDF | A4; fuentes embebidas solo Times (texto y fórmulas); renglones del cuerpo justificados (los bordes derechos alineados, salvo el último de cada párrafo); pie presente |
| Word | Times New Roman 12, interlineado 1,15, justificado en todos los párrafos del cuerpo; carátula sin marcadores rojos; A4; misma cantidad de notas que el PDF |

Además, verificación visual: páginas rasterizadas del PDF (carátula, índice, cuerpo justificado, notas, planos, bibliografía) y del Word convertido.

## 11. Dudas abiertas

1. **Textos internos dentro de los planos.** Las láminas dicen «Modelo 2.0» y «Prototipo 2.0» en el rótulo, y la lámina 4 cita «(concepto, 4.1)» y «(resultados.json)». Como son PDF vectoriales que no se regeneran, el control de vocabulario no los alcanza. Opciones: (a) usarlas tal cual (por defecto); (b) autorizar regenerarlas desde `08_modelo_2/` con el rótulo neutro, lo que cambia archivos fuera de esta tarea.
2. **Escala de las láminas.** Son A3; reducidas a A4 apaisado, las escalas del rótulo (1:2,5; 1:1; 4:1) dejan de valer al imprimir. Por defecto: A4 con una nota en el epígrafe («lámina A3 reducida a A4; las escalas corresponden al formato A3»). Alternativa: páginas A3 dentro del PDF, que conservan la escala.
3. **Fuente del PDF.** Times New Roman no está instalada y no se instala nada: el PDF usa TeX Gyre Termes (Times) y en sus propiedades figurará ese nombre. El Word sí usa «Times New Roman». ¿Alcanza, o el PDF final se exporta desde el Word en una máquina con Word?
4. **Pie de página.** En la reentrega 0, el texto «Ing. Mecánica - Grupo 01 - Curso S1091 - Año 2026» aparecía solo en la carátula y el resto de las páginas tenía solo el número. Por defecto: texto + número en todas las páginas del cuerpo, y la carátula con su pie oficial.
5. **Fuentes sin verificar.** (a) La rotura de la tira (124 N) usa 55 MPa como resistencia del PET (cota baja, sin orientar); en el repo ese valor no tiene fuente, y en una búsqueda rápida no apareció una citable que lo respalde. (b) Para FDM (anisotropía entre capas, voladizos de 45°) el candidato es Redwood, Schöffer y Garret (2017), *The 3D printing handbook*, 3D Hubs, todavía sin verificar. Plan: buscarlas y verificarlas al redactar; si no aparece una fuente para los 55 MPa, presentarlo como hipótesis de diseño del lado seguro, sin nota.
6. **Fuentes web.** PETALOT, Precious Plastic, Low-tech Lab, Appropedia y Engineering Toolbox van con nota al pie donde se usan, pero se listan en «Links de interés», no en la Bibliografía APA. El control de correspondencia acepta Bibliografía ∪ Links. ¿De acuerdo?
7. **Lectura del ancho.** El exceso medio medido (+0,83 mm) es mayor que lo que el modelo atribuye a la chapita faltante (hasta +0,5 mm), y un punto (8,73 mm) quedó por debajo del nominal, cosa que la chapita no explica. Redacción por defecto: la falta de la chapita explicaría parte del exceso; el resto y la dispersión se atribuyen, como hipótesis, a las irregularidades de la botella. No se vincula con la varilla de 7,3 mm (que da más juego a la tapa) salvo que lo pidas.
8. **Dónde se midió.** ¿Los 5 puntos son de una misma tira o de varias? Por defecto: «en cinco puntos de las tiras obtenidas».
9. **Campo «Resumen:» de la carátula** (decisión tuya, no se completa): dejarlo vacío (por defecto), completarlo con el abstract en E3, o completarlo en las dos versiones con un resumen de una línea.
10. **python-docx no está instalado** (y no se instala). La carátula oficial se completa editando directamente el XML del `.docx` oficial con la biblioteca estándar, como ya hace `lab_fisica/`: mismo resultado.
11. **Tamaño de página de la carátula.** La oficial es Carta; pasa a A4, conservando sus márgenes, para que todo el documento sea A4.
12. **Google Docs y páginas apaisadas.** Si al subir el `.docx` Google Docs no respeta la orientación de las secciones de planos, la alternativa es la lámina girada 90° en página vertical. Requiere una prueba de subida tuya.

---
*Fuentes: `Entrega 2 TP Final S1091 S1092.pdf`, `Entrega_2_Reentrega_0_S1091_Grupo_1.pdf`, `Caratula Entrega 2 TP FINAL Mecanica 1 S1092 S1091.docx`, `00_consignas/Entrega 1 TP Final S1091 S1092.pdf`; `08_modelo_2/` (README, 00_concepto.md, hallazgos_prototipo.md, parametros.py, resultados.json, planos, figuras, instructivo); `07_referencias/bobinadora_maty/README.md`; mediciones del grupo (16/11/2026).*
