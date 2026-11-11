# Preguntas sugeridas — Parcial 2 — Ingeniería Mecánica I

> ⚠ **Ninguna de estas preguntas salió de un examen.** Son inventadas para practicar, imitando la forma en que pregunta Abud. El banco de preguntas reales está en [preparacion_parcial_2.md](preparacion_parcial_2.md); no mezclar.

**Cómo están armadas:**

- Cada una sale de una frase concreta del material de cátedra (`material_catedra/`); la nota dice de dónde.
- Copian los formatos que usa en las preguntas reales: "quién se mueve", pares espejo, frases con dos huecos, "directa o inversamente proporcional", "¿cuál NO…?", combinaciones "I y II".
- Los distractores son, siempre que se puede, la respuesta correcta de otra pregunta del mismo tema — igual que hace él.

**Por dónde empezar:** los bloques `S-TE` y `S-EM` cubren los dos temas anunciados para los que no apareció ninguna pregunta real (teoría del engrane; árboles, ejes y demás elementos). El resto rellena huecos de temas que sí tienen preguntas reales.

| Código | Tema | Preguntas | Fuente principal |
|---|---|---|---|
| `S-TE` | Teoría del engrane y transmisiones | 18 | Unidad X |
| `S-EM` | Elementos de máquinas | 22 | Unidades IX y X |
| `S-MH` | Máquinas-herramienta | 18 | Unidad VII |
| `S-SV` | Procesos sin arranque de viruta | 13 | Unidades VI y VII |
| `S-CA` | Control automático | 16 | Apunte de control automático |
| `S-RO` | Mecánica rotacional | 10 | Apunte de mecánica rotacional |
| `S-PI` | Marcas, patentes y derecho de autor | 7 | Unidad de ética y propiedad intelectual |

---

## Bloque S-TE — Teoría del engrane y transmisiones

---

#### S-TE1 — En un engranaje formado por dos ruedas dentadas, la mayor se denomina ___ y la menor ___:

- ( ) a. Piñón / corona.
- ( ) b. Rueda motriz / rueda conducida.
- ( ) c. Planetario / satélite.
- **(✓) d. Corona / piñón.**

> Unidad X: "la mayor se denomina corona y el menor piñón". Motriz y conducida dependen de cuál recibe la potencia, no del tamaño.

---

#### S-TE2 — La principal ventaja de las transmisiones por engranaje respecto de la transmisión por poleas es que:

- ( ) a. Son más silenciosas.
- ( ) b. No necesitan lubricación.
- **(✓) c. No patinan, con lo que se obtiene exactitud en la relación de transmisión.**
- ( ) d. Permiten mayores distancias entre ejes.

> Unidad X, textual.

---

#### S-TE3 — El módulo de un engranaje se define como:

- **(✓) a. La relación entre el diámetro primitivo, en milímetros, y el número de dientes.**
- ( ) b. La relación entre el número de dientes y el diámetro exterior.
- ( ) c. La longitud de la circunferencia primitiva correspondiente a un diente y un vano.
- ( ) d. La altura total del diente.

> `M = Dp / Z`. La c es el paso circular (S-TE7).

---

#### S-TE4 — Para que dos engranajes puedan engranar entre sí deben tener:

- ( ) a. El mismo número de dientes.
- ( ) b. El mismo diámetro primitivo.
- ( ) c. El mismo diámetro exterior.
- **(✓) d. El mismo módulo.**

> Unidad X: "Dos engranajes que engranen tienen que tener el mismo módulo".

---

#### S-TE5 — El perfil del diente de un engranaje, es decir, la forma de sus flancos, está constituido por:

- **(✓) a. Dos curvas evolventes de círculo, simétricas respecto del eje del diente.**
- ( ) b. Dos arcos de circunferencia.
- ( ) c. Dos rectas inclinadas a 20°.
- ( ) d. Una hélice.

> Unidad X.

---

#### S-TE6 — La circunferencia primitiva de un engranaje es:

- ( ) a. La que limita la parte exterior del engranaje.
- ( ) b. La que limita el pie del diente.
- **(✓) c. La circunferencia a lo largo de la cual engranan los dientes.**
- ( ) d. La circunferencia base de la evolvente.

> La a es el diámetro exterior; la b, el interior. Todas las medidas del diente se refieren a la primitiva.

---

#### S-TE7 — El paso circular es:

- **(✓) a. La longitud de la circunferencia primitiva correspondiente a un diente y un vano consecutivos.**
- ( ) b. La distancia entre los centros de dos engranajes.
- ( ) c. El grosor del diente en la zona de contacto.
- ( ) d. La suma de la cabeza y el pie del diente.

> `Pc = π·M`. La c es el espesor del diente; la d, su altura.

---

#### S-TE8 — En el diente de un engranaje, la parte comprendida entre la circunferencia primitiva y el diámetro exterior se llama ___ y la comprendida entre la circunferencia interior y la primitiva, ___:

- ( ) a. Pie (dedendum) / cabeza (adendum).
- ( ) b. Flanco / vano.
- ( ) c. Módulo / paso.
- **(✓) d. Cabeza (adendum) / pie (dedendum).**

> Cabeza = `M` · pie = `1,25·M` · altura del diente = `2,25·M`.

---

#### S-TE9 — Los ángulos de presión normalizados en los engranajes son:

- ( ) a. 55° y 60°.
- **(✓) b. 20° y 25°.**
- ( ) c. 15° y 45°.
- ( ) d. 30° y 60°.

> Unidad X. La a es la trampa: 55° y 60° son los ángulos de las roscas Whitworth y métrica (EM4, EM5).

---

#### S-TE10 — El número de dientes de un engranaje con ángulo de presión de 20° no debe estar por debajo de:

- ( ) a. 8 dientes.
- ( ) b. 12 dientes.
- **(✓) c. 18 dientes.**
- ( ) d. 25 dientes.

> Unidad X: 18 dientes con 20°; 12 dientes con 25°.

---

#### S-TE11 — Un piñón de 20 dientes gira a 1.000 RPM y engrana con una corona de 40 dientes. La corona gira a:

- ( ) a. 2.000 RPM.
- ( ) b. 1.000 RPM.
- **(✓) c. 500 RPM.**
- ( ) d. 250 RPM.

> Ecuación general de transmisión: `N·Z = n·z` → `1.000·20 = n·40`. La rueda con más dientes gira más despacio. Es el punto 1 del ejercicio del apunte de rotacional.

---

#### S-TE12 — En una transmisión simple formada por dos ruedas dentadas, el sentido de giro del eje conducido es:

- ( ) a. El mismo que el del eje motor.
- ( ) b. Depende del módulo.
- ( ) c. Depende del número de dientes.
- **(✓) d. Contrario al del eje motor.**

> Unidad X, textual.

---

#### S-TE13 — Respecto de los engranajes cilíndricos de dientes rectos, los de dientes helicoidales:

- ( ) a. Transmiten menos potencia, pero son más baratos de fabricar.
- ( ) b. Son más ruidosos y más baratos.
- **(✓) c. Transmiten más potencia y más velocidad y son más silenciosos, pero se desgastan más y son más caros.**
- ( ) d. No necesitan engrase.

> Unidad X. Generan además un empuje axial, que se elimina con el dentado doble helicoidal.

---

#### S-TE14 — Los engranajes cónicos permiten transmitir movimiento entre:

- **(✓) a. Ejes que se cortan.**
- ( ) b. Ejes paralelos.
- ( ) c. Un eje y una cremallera.
- ( ) d. Ejes alineados.

> Unidad X: "tienen forma de tronco de cono y permiten transmitir movimiento entre ejes que se cortan".

---

#### S-TE15 — El tratamiento que recibe la mayoría de los engranajes (cementación o nitruración) busca obtener:

- ( ) a. Una gran dureza en el núcleo y una superficie dúctil.
- ( ) b. La eliminación de tensiones internas.
- **(✓) c. Una gran dureza en la zona de contacto de los dientes y tenacidad en el núcleo.**
- ( ) d. Un material blando para poder tallarlo.

> Unidad X. La misma lógica que F2 del 1er parcial (dureza superficial, núcleo tenaz).

---

#### S-TE16 — El mecanismo diferencial de un vehículo tiene por objeto:

- ( ) a. Aumentar la potencia en las ruedas motrices.
- ( ) b. Invertir el sentido de giro de las ruedas.
- ( ) c. Frenar la rueda interior.
- **(✓) d. Permitir que las ruedas motrices giren a distinta velocidad al tomar una curva.**

> Unidad X: planetarios y satélites. El mismo tren diferencial aparece en control automático como comparador de posiciones angulares.

---

#### S-TE17 — En un sistema de dos poleas unidas por una correa:

- **(✓) a. A mayor diámetro, menos vueltas: el número de vueltas está en razón inversa del diámetro.**
- ( ) b. A mayor diámetro, más vueltas.
- ( ) c. Las dos poleas giran siempre a la misma velocidad.
- ( ) d. La velocidad no depende de los diámetros.

> Unidad X: `n·d = N·D`.

---

#### S-TE18 — El mecanismo de piñón y cremallera:

- ( ) a. Reduce la velocidad entre dos ejes paralelos.
- ( ) b. Transmite movimiento entre ejes que se cortan.
- ( ) c. Acumula energía.
- **(✓) d. Transforma un movimiento circular en uno lineal, y viceversa.**

> Clase de mecanismos (carpeta de otro año). En control automático lo usa para comparar traslaciones.

---

## Bloque S-EM — Elementos de máquinas

---

#### S-EM1 — La diferencia entre un árbol y un eje es que:

- ( ) a. El árbol no gira y el eje sí.
- ( ) b. El eje es siempre hueco.
- **(✓) c. El árbol transmite potencia mediante su giro; el eje solo soporta, sin transmitir movimiento.**
- ( ) d. No hay diferencia: son sinónimos.

> Unidad X: "el eje puede girar libremente o no, pero no transmite movimiento; solamente soporta el peso".

---

#### S-EM2 — Un árbol está sometido, en la mayor parte de los casos, a esfuerzos de:

- ( ) a. Solo flexión.
- ( ) b. Solo torsión.
- ( ) c. Tracción y compresión.
- **(✓) d. Flexión y torsión.**

> Torsión por el momento de giro que transmite; flexión por el peso de lo que lleva montado.

---

#### S-EM3 — Un eje, que no transmite movimiento, está sometido a esfuerzos de:

- **(✓) a. Flexión.**
- ( ) b. Torsión.
- ( ) c. Flexión y torsión.
- ( ) d. Ninguno.

> Par espejo de S-EM2.

---

#### S-EM4 — Al fabricar un árbol hueco en lugar de uno macizo:

- ( ) a. Se ahorra peso y además aumenta la resistencia.
- **(✓) b. Se ahorra hasta un 25 % del peso y la resistencia se reduce hasta un 6,25 %.**
- ( ) c. Se ahorra un 6,25 % del peso y la resistencia se reduce un 25 %.
- ( ) d. No cambia ni el peso ni la resistencia.

> Unidad X, textual. La c tiene los números invertidos.

---

#### S-EM5 — El árbol acodado (cigüeñal) se emplea cuando se quiere:

- ( ) a. Transmitir grandes momentos de giro sin debilitar el árbol.
- **(✓) b. Transformar un movimiento alternativo en giratorio, y viceversa.**
- ( ) c. Dejar pasar otro árbol por su interior.
- ( ) d. Reducir la inercia.

> La a es el árbol estriado; la c y la d, el hueco.

---

#### S-EM6 — Los árboles estriados se emplean para:

- ( ) a. Soportar cargas sin girar.
- ( ) b. Transformar movimiento alternativo en giratorio.
- **(✓) c. Transmitir grandes momentos de giro sin tener que debilitar grandemente el árbol.**
- ( ) d. Reducir el peso.

> Unidad X.

---

#### S-EM7 — Las estrías de un árbol se tallan por ___ y las del cubo donde se acopla, por ___:

- ( ) a. Brochado / fresado.
- ( ) b. Torneado / rectificado.
- ( ) c. Limado / cepillado.
- **(✓) d. Fresado / brochado.**

> Unidad X. Cruza elementos de máquinas con máquinas-herramienta: el brochado es el proceso de los perfiles interiores.

---

#### S-EM8 — En un árbol con cambios bruscos de diámetro se producen ___, que se resuelven con ___:

- **(✓) a. Concentraciones de esfuerzos / redondeos en los cambios de sección.**
- ( ) b. Deformaciones plásticas / temple.
- ( ) c. Vibraciones / contrapesos.
- ( ) d. Pandeo / una mayor longitud.

> Unidad X. Es D6 del 1er parcial aplicada a un árbol escalonado.

---

#### S-EM9 — En un eje fijo, los elementos mecánicos montados sobre él:

- ( ) a. Giran solidarios con el eje.
- ( ) b. No pueden girar.
- **(✓) c. Giran libremente sobre el eje, sin girar solidarios con él.**
- ( ) d. Le transmiten el momento torsor.

> Unidad X: ejes fijos y ejes giratorios.

---

#### S-EM10 — Las funciones básicas de un lubricante son:

- ( ) a. Reducción de la fricción, aumento de la temperatura y sellado.
- ( ) b. Solo la reducción de la fricción.
- ( ) c. Aumento de la viscosidad y de la presión.
- **(✓) d. Reducción de la fricción, disipación del calor y dispersión de los contaminantes.**

> Unidad X, textual.

---

#### S-EM11 — En un cojinete hidrodinámico, la presión de la película de aceite:

- ( ) a. La suministra una bomba exterior.
- **(✓) b. Se autogenera por el movimiento relativo de las superficies.**
- ( ) c. No existe: el cojinete trabaja en seco.
- ( ) d. Se mantiene aunque el árbol esté detenido.

> La a es el cojinete hidrostático. Por eso al arrancar y al detenerse el hidrodinámico trabaja con fricción mixta.

---

#### S-EM12 — ¿Cuál de las siguientes NO es una ventaja de los rodamientos frente a los cojinetes de fricción?

- ( ) a. Menor necesidad de lubricación.
- ( ) b. Menor calentamiento.
- **(✓) c. Son más silenciosos.**
- ( ) d. Menor longitud, lo que permite diseños más reducidos.

> Unidad X: entre los inconvenientes figura que "son más ruidosos", además de sensibles a los choques y a la suciedad y exigentes en el montaje.

---

#### S-EM13 — Un rodamiento radial admite cargas:

- **(✓) a. En sentido perpendicular a su eje.**
- ( ) b. En el sentido de su eje.
- ( ) c. En cualquier sentido.
- ( ) d. Solo de torsión.

> Unidad X. Los axiales, en el sentido de su eje.

---

#### S-EM14 — La capacidad de carga dinámica de un rodamiento es la carga constante bajo la cual alcanza una durabilidad de:

- ( ) a. Mil revoluciones.
- **(✓) b. Un millón de revoluciones.**
- ( ) c. Diez años de servicio.
- ( ) d. Un millón de horas.

> Unidad X.

---

#### S-EM15 — Las chavetas son órganos mecánicos destinados a:

- ( ) a. Unir piezas en forma permanente.
- ( ) b. Reducir el rozamiento entre el árbol y el cubo.
- **(✓) c. Unir piezas que deben girar solidarias con un árbol para transmitir un par motriz, permitiendo un fácil montaje y desmontaje.**
- ( ) d. Sellar la unión entre dos piezas.

> Unidad IX (diapositivas).

---

#### S-EM16 — Según la forma del filete, la rosca más usada para fijación es la ___ y la que se usa para transmitir fuerza, la ___:

- **(✓) a. Triangular / trapecial.**
- ( ) b. Trapecial / triangular.
- ( ) c. Redonda / cuadrada.
- ( ) d. En diente de sierra / triangular.

> Unidad IX (diapositivas).

---

#### S-EM17 — Un tornillo marcado "8.8" tiene:

- ( ) a. 8 mm de diámetro y 8 mm de paso.
- **(✓) b. Una resistencia a la rotura de 800 N/mm² y un límite elástico del 80 % de ese valor.**
- ( ) c. 88 hilos por pulgada.
- ( ) d. Un diámetro de 8,8 mm.

> Unidad IX: la primera cifra es la centésima parte de la resistencia a la rotura; la segunda, el factor para obtener el límite elástico (640 N/mm²).

---

#### S-EM18 — Un bulón se compone de:

- ( ) a. Un vástago roscado en sus dos extremos.
- **(✓) b. Un tornillo y una tuerca del mismo diámetro.**
- ( ) c. Un remache y una arandela.
- ( ) d. Un pasador y una chaveta.

> Unidad IX. La a es un espárrago.

---

#### S-EM19 — Una unión con remaches, frente a una atornillada:

- ( ) a. Es desmontable y más resistente.
- ( ) b. Solo sirve para piezas de gran espesor.
- ( ) c. Exige que las dos caras sean accesibles.
- **(✓) d. No es desmontable y alcanza menor resistencia, pero es barata y automatizable.**

> Unidad IX: no es adecuada para grandes espesores y permite uniones ciegas.

---

#### S-EM20 — Las correas de transmisión planas y trapezoidales basan su funcionamiento en:

- **(✓) a. Las fuerzas de fricción entre la correa y las poleas.**
- ( ) b. La interferencia mecánica entre dientes.
- ( ) c. La presión de un fluido.
- ( ) d. La fuerza centrífuga.

> Unidad X. La b es lo que distingue a las cadenas y a las correas dentadas.

---

#### S-EM21 — En el sistema de ajuste de agujero único (agujero base):

- ( ) a. Se cambia la tolerancia del agujero y se mantiene la del eje.
- ( ) b. Ni el eje ni el agujero tienen tolerancia.
- **(✓) c. Se mantiene la posición de la tolerancia del agujero y se cambia la del eje.**
- ( ) d. Todos los ajustes resultan con aprieto.

> Unidad IX. Caso típico: montar un rodamiento, cuyo agujero ya viene dado, sobre un eje que se mecaniza.

---

#### S-EM22 — En un ajuste hay "juego" cuando:

- **(✓) a. El diámetro del eje es menor que el del agujero.**
- ( ) b. El diámetro del eje es mayor que el del agujero.
- ( ) c. Los dos diámetros son exactamente iguales.
- ( ) d. El eje es hueco.

> Unidad IX. La b es el "aprieto".

---

## Bloque S-MH — Máquinas-herramienta

---

#### S-MH1 — En el torneado, el movimiento de corte:

- ( ) a. Es rectilíneo y lo realiza la herramienta.
- ( ) b. Es circular y lo realiza la herramienta.
- ( ) c. Es alternativo y lo realiza la pieza.
- **(✓) d. Es circular y lo realiza la pieza, que gira alrededor de su propio eje.**

> Unidad VII: "El movimiento de corte es circular. Lo realiza la pieza".

---

#### S-MH2 — En el fresado, el movimiento circular de corte lo realiza ___ y los movimientos de avance y de aproximación, ___:

- **(✓) a. La fresa / la pieza.**
- ( ) b. La pieza / la fresa.
- ( ) c. La fresa / la fresa.
- ( ) d. La pieza / la pieza.

> Unidad VII, textual. Es el torno dado vuelta.

---

#### S-MH3 — En el fresado cilíndrico, el eje de la fresa se halla dispuesto:

- ( ) a. Normal a la superficie de trabajo.
- ( ) b. A 45° de la superficie de trabajo.
- **(✓) c. Paralelamente a la superficie de trabajo.**

> Par espejo de MH4 (frontal → perpendicular). No confundir con MH3, que pregunta por el **plano de giro** y tiene clave propia.

---

#### S-MH4 — La característica principal de la fresadora universal es que:

- ( ) a. Tiene el husillo dispuesto verticalmente.
- **(✓) b. La mesa de fresar puede girar hacia la derecha o hacia la izquierda, lo que permite, por ejemplo, fresar ranuras en espiral.**
- ( ) c. Tiene varios husillos de fresar.
- ( ) d. La pieza gira.

> Unidad VII. La a es la fresadora vertical.

---

#### S-MH5 — El alesado consiste en:

- ( ) a. Abrir un agujero en material macizo.
- **(✓) b. Ensanchar un agujero a fin de dejarlo exactamente a la medida deseada.**
- ( ) c. Tallar una rosca exterior.
- ( ) d. Pulir una superficie plana.

> Unidad VII. La a es el taladrado.

---

#### S-MH6 — El rectificado es una operación que se lleva a cabo en piezas que requieren:

- **(✓) a. Tolerancias exigentes: dimensionales, geométricas y de acabado superficial.**
- ( ) b. Grandes arranques de material en poco tiempo.
- ( ) c. Baja precisión.
- ( ) d. Deformación plástica.

> Unidad VII.

---

#### S-MH7 — La herramienta del rectificado se llama ___ y su parte activa está formada por ___:

- ( ) a. Fresa / dientes de acero rápido.
- ( ) b. Brocha / filos crecientes.
- ( ) c. Broca / dos filos cortantes.
- **(✓) d. Muela / granos abrasivos unidos por un aglomerante.**

> Unidad VII: los abrasivos (carborundum o corindón) producen la viruta; el aglomerante da la forma y la dureza de la muela.

---

#### S-MH8 — En las brochadoras, el movimiento de avance:

- **(✓) a. Queda cumplido por la propia herramienta, en función de sus filos cada vez más grandes.**
- ( ) b. Lo da la mesa portapieza.
- ( ) c. Lo da un carro transversal.
- ( ) d. No existe, porque la brocha no arranca viruta.

> Unidad VII: "Estas máquinas solo dan el movimiento principal longitudinal a la herramienta". Explica MH10.

---

#### S-MH9 — En el cepillado el movimiento de corte lo efectúa ___ y en el limado, ___:

- ( ) a. La herramienta / la pieza.
- ( ) b. La pieza / la pieza.
- ( ) c. La herramienta / la herramienta.
- **(✓) d. La pieza / la herramienta.**

> El temario de la Unidad VII pide "establecer diferencias y similitudes entre los 3 procesos" (cepillado, limado, amortajado): esta es la diferencia.

---

#### S-MH10 — El limado también se conoce como:

- ( ) a. Cepillado vertical.
- ( ) b. Brochado exterior.
- **(✓) c. Amortajado horizontal.**
- ( ) d. Fresado frontal.

> Unidad VII: "Este proceso también es conocido como amortajado horizontal".

---

#### S-MH11 — La limadora se presta para trabajar piezas ___ y la cepilladora, piezas ___:

- ( ) a. Largas / pequeñas.
- ( ) b. Cilíndricas / planas.
- ( ) c. Huecas / macizas.
- **(✓) d. Pequeñas / largas.**

> Unidad VII.

---

#### S-MH12 — Cepillado, limado y amortajado tienen en común que:

- ( ) a. Usan una herramienta giratoria de múltiples filos.
- ( ) b. Usan una herramienta abrasiva.
- **(✓) c. Arrancan viruta con una herramienta de un solo filo que no está continuamente en acción.**
- ( ) d. La pieza gira.

> Unidad VII: la similitud entre los tres procesos.

---

#### S-MH13 — Creado y afeitado son dos procesos diferentes pero relacionados entre sí porque:

- **(✓) a. El creado talla los dientes y el afeitado da el acabado a los flancos de los dientes ya tallados.**
- ( ) b. Los dos tallan los dientes del engranaje, con distinta máquina.
- ( ) c. El afeitado talla los dientes y el creado los endurece.
- ( ) d. Son dos tratamientos térmicos sucesivos.

> El temario de la Unidad VII pide justamente "decir por qué son 2 procesos diferentes, pero relacionados entre sí".

---

#### S-MH14 — En el afeitado de engranajes:

- ( ) a. Se accionan la herramienta y el engranaje.
- ( ) b. Solo se acciona el engranaje.
- ( ) c. La herramienta no gira.
- **(✓) d. Solo se acciona la herramienta de rasurar; el engranaje gira libremente.**

> Unidad VII: principio funcional de las afeitadoras.

---

#### S-MH15 — La sección diametral de un "creador" (tornillo-fresa) es idéntica al perfil de:

- ( ) a. Un engranaje de dientes rectos.
- ( ) b. Una rosca Whitworth.
- **(✓) c. Una cremallera del mismo módulo.**
- ( ) d. Una brocha.

> Diapositivas de la Unidad VII.

---

#### S-MH16 — En el taladrado, la broca tiene:

- **(✓) a. Un movimiento de rotación, que es el de corte, y un movimiento rectilíneo de avance en la dirección del agujero.**
- ( ) b. Solo movimiento de rotación; el avance lo da la pieza al girar.
- ( ) c. Un movimiento alternativo.
- ( ) d. Solo movimiento de avance.

> Diapositivas de la Unidad VII.

---

#### S-MH17 — La electroerosión arranca material por medio de:

- ( ) a. Una muela abrasiva.
- ( ) b. Un chorro de agua a presión.
- ( ) c. Golpes de una estampa.
- **(✓) d. Chispas eléctricas entre un electrodo y la pieza, rodeados de un líquido dieléctrico.**

> Unidad VII: procedimiento no mecánico, apto sobre todo para materiales duros (aceros templados, metal duro).

---

#### S-MH18 — ¿Cuál de estas máquinas-herramienta trabaja con menor error?

- ( ) a. Cepilladora.
- ( ) b. Fresadora.
- ( ) c. Torno paralelo.
- **(✓) d. Rectificadora.**

> Tabla de la Unidad IX: cepilladora 100 µm · fresadora 50 µm · torno paralelo 20 µm · rectificadora 1 a 5 µm.

---

## Bloque S-SV — Procesos sin arranque de viruta

---

#### S-SV1 — El moldeo en arena es un procedimiento de:

- ( ) a. Molde permanente.
- ( ) b. Molde metálico.
- **(✓) c. Molde perdido.**
- ( ) d. Molde de cera.

> Unidad VI. Por eso "el molde no puede volver a utilizarse" es verdadera en SV2.

---

#### S-SV2 — El modelo que se usa para hacer el molde de fundición debe ser, respecto de la pieza final:

- **(✓) a. Ligeramente más grande, para compensar la contracción al enfriarse.**
- ( ) b. Exactamente igual.
- ( ) c. Ligeramente más chico.
- ( ) d. Del doble de tamaño.

> Unidad VI. Además lleva sobremedida si después se mecaniza, y ángulos de salida.

---

#### S-SV3 — Si la pieza que se quiere fundir es hueca, en el molde se colocan:

- ( ) a. Mazarotas.
- ( ) b. Bebederos.
- ( ) c. Coquillas.
- **(✓) d. Machos (corazones).**

> Unidad VI.

---

#### S-SV4 — En la fundición en coquilla el molde es:

- ( ) a. De arena.
- ( ) b. De cera.
- **(✓) c. Metálico.**
- ( ) d. De yeso.

> Unidad VI.

---

#### S-SV5 — En la forja libre ___; en la forja por estampación ___:

- **(✓) a. La deformación del metal no está limitada / la fluencia del material queda limitada a la cavidad de la estampa.**
- ( ) b. Se trabaja en frío / se trabaja en caliente.
- ( ) c. Se usan dos matrices / no se usan matrices.
- ( ) d. Se obtienen piezas huecas / se obtienen alambres.

> Unidad VII.

---

#### S-SV6 — El embutido permite obtener:

- ( ) a. Alambres de sección cada vez menor.
- **(✓) b. Piezas huecas a partir de chapa, en general sin pretender una variación del espesor.**
- ( ) c. Piezas macizas por golpes.
- ( ) d. Piezas a partir de polvo metálico.

> Unidad VII. La a es el trefilado; la c, la forja; la d, el sinterizado.

---

#### S-SV7 — Los metales laminados en frío:

- ( ) a. Quedan más blandos que los laminados en caliente.
- ( ) b. No sufren ningún cambio.
- ( ) c. Se funden superficialmente.
- **(✓) d. Adquieren acritud y deben someterse a un recocido final.**

> Unidad VII, textual. Enlaza con F4 del 1er parcial (recocido).

---

#### S-SV8 — En el trefilado en frío, el alambre se estira haciéndolo pasar por hileras cuyo diámetro es:

- **(✓) a. Paulatinamente menor.**
- ( ) b. Paulatinamente mayor.
- ( ) c. Constante.
- ( ) d. Alternadamente mayor y menor.

> Unidad VII. Antes se le da un "patentado" para que tenga ductilidad suficiente.

---

#### S-SV9 — Respecto del trefilado en frío, el trefilado en caliente da un material con:

- ( ) a. Mayor acritud y mejor terminación superficial.
- ( ) b. La misma acritud y la misma terminación.
- **(✓) c. Menor (o nula) acritud y una terminación superficial de menor calidad.**
- ( ) d. Mayor dureza.

> Unidad VII.

---

#### S-SV10 — Las etapas de la metalurgia de polvos, en orden, son:

- **(✓) a. Polvos, mezclado, compactado y sinterizado.**
- ( ) b. Mezclado, sinterizado, compactado y polvos.
- ( ) c. Polvos, sinterizado, mezclado y compactado.
- ( ) d. Compactado, polvos, mezclado y sinterizado.

> Unidad VII. Mismo formato de "orden correcto" que A4 del 1er parcial; refuerza SV4.

---

#### S-SV11 — El sinterizado de la pieza ya compactada se realiza:

- ( ) a. A una temperatura superior al punto de fusión del polvo.
- ( ) b. A temperatura ambiente.
- **(✓) c. A una temperatura inferior al punto de fusión del metal base, en hornos de atmósfera controlada.**
- ( ) d. Con un enfriamiento rápido en agua.

> Unidad VII.

---

#### S-SV12 — La restricción principal de la extrusión de plásticos es que los productos deben tener:

- ( ) a. Forma hueca cerrada.
- ( ) b. Un espesor menor a 1 mm.
- ( ) c. Poco peso.
- **(✓) d. Una sección transversal constante a lo largo de su longitud.**

> Unidad VII: tubos, perfiles, láminas, filamentos.

---

#### S-SV13 — El moldeo por soplado se utiliza para producir:

- ( ) a. Perfiles macizos.
- ( ) b. Piezas metálicas de precisión.
- **(✓) c. Artículos de plástico huecos, como botellas.**
- ( ) d. Láminas planas.

> Unidad VII.

---

## Bloque S-CA — Control automático

---

#### S-CA1 — En un termostato, la posición del dial establece:

- ( ) a. La variable controlada.
- ( ) b. La señal de error.
- ( ) c. La perturbación.
- **(✓) d. La entrada de referencia (la temperatura deseada).**

> Apunte de control. Par con S-CA2.

---

#### S-CA2 — En un termostato, la temperatura verdadera del sistema es:

- **(✓) a. La variable controlada.**
- ( ) b. La entrada de referencia.
- ( ) c. La señal actuadora.
- ( ) d. La función de transferencia.

> Apunte de control.

---

#### S-CA3 — Para que un sistema pueda considerarse de control realimentado es necesario que:

- ( ) a. La entrada de referencia se mantenga fija.
- **(✓) b. La variable controlada sea realimentada y comparada con la entrada de referencia.**
- ( ) c. No existan perturbaciones.
- ( ) d. La variable controlada sea una posición.

> Apunte de control, textual. La a es el regulador y la d el servomecanismo: casos particulares, no la condición general.

---

#### S-CA4 — En los sistemas de lazo abierto:

- ( ) a. La variable controlada se compara con la entrada de referencia.
- ( ) b. El error tiende a cero.
- **(✓) c. No existe el comparador: cada ajuste de la entrada determina una posición fija de los elementos de control.**
- ( ) d. La señal actuadora varía continuamente.

> Apunte de control.

---

#### S-CA5 — La principal ventaja de un sistema de control de lazo cerrado es que:

- **(✓) a. La variable controlada tiende a mantenerse igual a la entrada de referencia, independientemente de las perturbaciones externas.**
- ( ) b. Es más económico.
- ( ) c. No necesita comparador.
- ( ) d. La entrada de referencia se ajusta sola.

> Apunte de control, textual.

---

#### S-CA6 — En un diagrama de bloques, el círculo representa ___ y el rectángulo, ___:

- ( ) a. Una multiplicación / una adición.
- **(✓) b. Una adición (suma o resta de señales) / una multiplicación.**
- ( ) c. Una integración / una derivación.
- ( ) d. La entrada / la salida.

> Apunte de control. Es la base de CA10.

---

#### S-CA7 — Los elementos representados por H(p) se llaman:

- ( ) a. De acción directa.
- ( ) b. Comparadores.
- ( ) c. Integradores.
- **(✓) d. De acción realimentada.**

> Los de `G(p)` son los de acción directa.

---

#### S-CA8 — Cuando el lazo tiene elementos de realimentación H(p), la señal de realimentación b vale:

- ( ) a. b = G(p)·e
- **(✓) b. b = H(p)·c**
- ( ) c. b = r − c
- ( ) d. b = H(p)·r

> Apunte de control. Y la señal actuadora pasa a ser `e = r − b`.

---

#### S-CA9 — Un amortiguador viscoso es sometido a una fuerza Fd. En un diagrama de bloques con entrada Fd y salida x, la función de transferencia es:

- ( ) a. c·p
- **(✓) b. 1/(c·p)**
- ( ) c. 1/k
- ( ) d. c/p

> `Fd = c·p·x`, con `p = d/dt`. La c es el resorte (CA3).

---

#### S-CA10 — Un eje de torsión soporta un disco que gira en un medio viscoso bajo una cupla T. La función de transferencia entre T y el ángulo θ es:

- ( ) a. Directamente proporcional a la suma (Ks + Cv·p + I·p²).
- ( ) b. Igual a Ks.
- ( ) c. Independiente del momento de inercia del disco.
- **(✓) d. Inversamente proporcional a la suma (Ks + Cv·p + I·p²).**

> Versión rotativa de CA4: `θ = T / (Ks + Cv·p + I·p²)`.

---

#### S-CA11 — Si en el comparador de cremalleras se invierte el sentido positivo de xc, se obtiene:

- ( ) a. Un integrador.
- **(✓) b. Un dispositivo sumador.**
- ( ) c. Un regulador.
- ( ) d. Un amortiguador.

> Apunte de control, textual. Explica por qué en CA6 la opción con el signo "+" es la falsa.

---

#### S-CA12 — En el comparador de tren diferencial de engranajes, θe es:

- ( ) a. La entrada de referencia.
- ( ) b. La posición angular realimentada.
- **(✓) c. La posición angular del portaplanetas y una medida del error: θe = (θr − θc)/2.**
- ( ) d. La suma de las dos posiciones: θe = θr + θc.

> Apunte de control. Misma forma que el de cremalleras, con ángulos.

---

#### S-CA13 — En el mecanismo integrador de bolillas y disco, la posición angular del eje de salida resulta proporcional a:

- **(✓) a. La integral del error respecto del tiempo.**
- ( ) b. El error.
- ( ) c. La derivada del error respecto del tiempo.
- ( ) d. El cuadrado del error.

> Apunte de control. Por eso su salida crece con el tiempo aunque el error sea chico (CA7).

---

#### S-CA14 — Una caldera cuyo funcionamiento se ajusta según la temperatura exterior es un ejemplo de ___, y la temperatura exterior actúa como ___:

- ( ) a. Sistema de lazo cerrado / entrada de referencia.
- ( ) b. Servomecanismo / variable controlada.
- ( ) c. Regulador / señal actuadora.
- **(✓) d. Sistema de lazo abierto / perturbación.**

> Apunte de control: el ejemplo de lazo abierto.

---

#### S-CA15 — ¿Cuál de los siguientes es un servomecanismo?

- ( ) a. El control de temperatura de un horno.
- **(✓) b. El control de la posición angular de un eje que regula la entrada de aire de un quemador.**
- ( ) c. Una estufa sin termostato.
- ( ) d. Un resorte comprimido por una fuerza.

> Es el ejemplo del apunte. La a es un regulador; la c, lazo abierto.

---

#### S-CA16 — En la analogía entre sistemas mecánicos y eléctricos que da la cátedra, el amortiguador equivale a ___ y la masa a ___:

- ( ) a. Una capacitancia / una resistencia.
- **(✓) b. Una resistencia / una capacitancia.**
- ( ) c. Una inductancia / una resistencia.
- ( ) d. Una resistencia / una inductancia.

> Completa CA11 (resorte = inductancia). La a es exactamente lo que dicen las opciones falsas de CA11.

---

## Bloque S-RO — Mecánica rotacional

---

#### S-RO1 — El momento de inercia de un cuerpo rígido es función de:

- ( ) a. Su velocidad angular.
- ( ) b. Su aceleración angular.
- **(✓) c. El eje respecto del cual gira y cómo está distribuida la masa respecto de ese eje.**
- ( ) d. Solo de su masa total.

> Apunte de rotacional, textual. Es el fundamento de RO3.

---

#### S-RO2 — Si repentinamente el momento de inercia de un eje se reduce a la mitad, sin mediar momentos exteriores, su velocidad angular:

- ( ) a. Se reduce a la mitad.
- **(✓) b. Se duplica.**
- ( ) c. Se mantiene.
- ( ) d. Se cuadruplica.

> `I₁·ω₁ = I₂·ω₂`. Es el punto 6 del ejercicio del apunte y la inversa de RO4.

---

#### S-RO3 — La variación de la cantidad de movimiento angular respecto del tiempo es igual a:

- ( ) a. La fuerza exterior resultante.
- **(✓) b. La suma de los momentos de rotación exteriores.**
- ( ) c. La energía cinética de rotación.
- ( ) d. La potencia.

> `T_ext = dL/dt`. La a es la versión de traslación (`F_ext = dP/dt`).

---

#### S-RO4 — Si se duplica la velocidad angular de un eje sin variar su momento de inercia, su cantidad de movimiento angular ___ y su energía cinética de rotación ___:

- **(✓) a. Se duplica / se cuadruplica.**
- ( ) b. Se duplica / se duplica.
- ( ) c. Se cuadruplica / se duplica.
- ( ) d. No varía / se duplica.

> `L = I·ω` es lineal en `ω`; `K = ½·I·ω²` es cuadrática. Junta RO1 con RO8.

---

#### S-RO5 — En un cilindro que rueda sin deslizar, la velocidad del punto de contacto con el piso y la del punto superior valen, respectivamente:

- ( ) a. v_CM y v_CM.
- ( ) b. 0 y v_CM.
- **(✓) c. 0 y 2·v_CM.**
- ( ) d. v_CM y 2·v_CM.

> Apunte de rotacional: `v = v_CM − ω·R` abajo y `v = v_CM + ω·R` arriba.

---

#### S-RO6 — Un cilindro que baja rodando por un plano inclinado llega abajo con una velocidad del centro de masa:

- **(✓) a. Menor que si bajara deslizando.**
- ( ) b. Mayor que si bajara deslizando sin rodar.
- ( ) c. Igual que si bajara deslizando.
- ( ) d. Nula.

> Apunte de rotacional: `√(4/3·g·h)` rodando frente a `√(2·g·h)` deslizando. Parte de la energía queda en la rotación.

---

#### S-RO7 — La velocidad angular de precesión de un trompo es:

- ( ) a. Proporcional a L e independiente de θ.
- ( ) b. Proporcional a sen θ.
- ( ) c. Independiente de L.
- **(✓) d. Independiente del ángulo θ e inversamente proporcional a L.**

> Apunte de rotacional, textual: `ωp = r·m·g / L`.

---

#### S-RO8 — El momento de inercia de un cuerpo respecto de un eje paralelo al que pasa por su centro de masa, a una distancia h, vale:

- ( ) a. I_CM − M·h²
- **(✓) b. I_CM + M·h²**
- ( ) c. I_CM·M·h²
- ( ) d. I_CM + M·h

> Es lo que se usa en RO12 para el punto de contacto: `I_P = I_CM + M·R²`.

---

#### S-RO9 — La potencia en un movimiento de rotación, P = T·ω, es análoga en traslación a:

- ( ) a. P = m·a
- **(✓) b. P = F·v**
- ( ) c. P = F·d
- ( ) d. P = m·v

> Apunte de rotacional: "Analogía con traslación P = F·v".

---

#### S-RO10 — La ley de conservación de la cantidad de movimiento angular:

- ( ) a. Solo vale para cuerpos rígidos simétricos.
- ( ) b. No es aplicable a nivel atómico.
- **(✓) c. Es de aplicación universal: vale para los cuerpos, a nivel atómico y para los cuerpos celestes.**
- ( ) d. Solo vale si el momento de inercia es constante.

> Apunte de rotacional, textual: "a diferencia de las leyes de la mecánica newtoniana […] es de aplicación universal".

---

## Bloque S-PI — Marcas, patentes y derecho de autor

---

#### S-PI1 — Para que una invención sea patentable debe reunir:

- ( ) a. Novedad y bajo costo.
- **(✓) b. Novedad, actividad inventiva y aplicación industrial.**
- ( ) c. Originalidad estética y distintividad.
- ( ) d. Registro previo como marca.

> Los tres requisitos de patentabilidad. La c mezcla los de diseños y marcas.

---

#### S-PI2 — Una marca protege ___ y una patente, ___:

- **(✓) a. La identidad del origen de un producto o servicio / la función o el funcionamiento de una invención.**
- ( ) b. La función de una invención / la apariencia del producto.
- ( ) c. Una obra literaria / un logotipo.
- ( ) d. Un secreto comercial / una marca.

> Marca = quién lo hace; patente = cómo funciona.

---

#### S-PI3 — El derecho de autor:

- ( ) a. Requiere un registro para existir.
- **(✓) b. Nace en el momento de la creación de la obra, sin necesidad de registro.**
- ( ) c. Solo protege invenciones industriales.
- ( ) d. Dura 20 años no renovables.

> La d es la patente (PI2).

---

#### S-PI4 — Al vencer el plazo de una patente:

- ( ) a. El inventor puede renovarla por otros 20 años.
- ( ) b. La patente pasa al Estado.
- ( ) c. Se convierte en una marca.
- **(✓) d. La invención pasa al dominio público.**

> Consecuencia de "no renovable" (PI2).

---

#### S-PI5 — A diferencia de una patente, una marca:

- ( ) a. No puede renovarse.
- **(✓) b. Puede renovarse indefinidamente, cada 10 años, mientras se la use.**
- ( ) c. Dura lo que vive su titular.
- ( ) d. Dura 20 años.

> Junta PI1 con PI2: patente 20 años no renovable; marca 10 años renovable.

---

#### S-PI6 — El organismo argentino encargado de otorgar patentes y registrar marcas es:

- ( ) a. El INTI.
- ( ) b. El IRAM.
- ( ) c. La UTN.
- **(✓) d. El INPI.**

> Instituto Nacional de la Propiedad Industrial.

---

#### S-PI7 — De las siguientes afirmaciones sobre una patente: I) impide a terceros fabricar, usar o vender la invención sin autorización del titular; II) puede licenciarse o venderse.

- ( ) a. I es verdadera y II es falsa.
- **(✓) b. I y II son verdaderas.**
- ( ) c. I es falsa y II es verdadera.
- ( ) d. I y II son falsas.

> Formato "I y II" de VJ17. La II es PI4.

---

*Fuentes: apuntes y diapositivas de cátedra en `material_catedra/` (Mecánica Rotacional e Ingeniería del control automático, ciclo 2018; Unidades VI, VII, IX y X); para S-PI, el resumen de propiedad intelectual de `campus_virtual/10_etica.md`; para S-TE17 y S-TE18, la carpeta de otro año en `2do_parcial/fuentes/descargas_web/`.*

