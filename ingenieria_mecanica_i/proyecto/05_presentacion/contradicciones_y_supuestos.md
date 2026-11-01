# Contradicciones entre fuentes y supuestos de la presentación

Criterio: **prevalece la Entrega 2** (`03_entrega_2/Entrega_2_Reentrega_0_S1091_Grupo_1.pdf`, en adelante E2), que es lo último entregado. Lo que E2 no resuelve queda como pendiente del grupo.

## 1. Contradicciones entre fuentes

| # | Tema | Versiones encontradas | Usada en el deck | Fuente |
|---|---|---|---|---|
| 1 | Transmisión al husillo | E2: par de engranajes cilíndricos de dientes rectos. DXF: cota "Unidos por correa" (165 mm), sin husillo ni engranajes dibujados. Proyecto base: menciona además "tornillo sin fin" | Engranajes. La cota de correa y esas vistas no aparecen | E2, 5.3 |
| 2 | Sujeción de la botella | E2: pieza exterior de dos mitades en el cuello, sobre rodamientos. Proyecto base y Entrega 1: esfera y contrapunta regulable. DXF: fila superior con lo que parece cono, resorte y media esfera | Dos mitades en el cuello. La fila superior del DXF no aparece | E2, 5.4 |
| 3 | Accionamiento | E2: manual. Proyecto base: manual, pero el cap. 12 dice una vez "accionamiento motorizado" | Manual | E2, 5.1 y 5.2 |
| 4 | Sentido de la reducción | E2: el engranaje conducido (husillo) tiene más dientes, `i > 1`. Imagen IA: engranaje **chico** alineado con el husillo y grande arriba, lo que multiplica la velocidad | Reducción, como en E2. La imagen sigue en las láminas 1 y 5 | E2, 5.3 |
| 5 | Qué fija el ancho de la tira | E2: el paso `a` lo fija la transmisión, y su correspondencia con el ancho debe verificarse. Proyecto base: lo fija la posición de la cuchilla | Título "paso del corte"; `a` no se presenta como igual al ancho | E2, 5.3 |
| 6 | Tipo de corte | E2: helicoidal. Proyecto base, cap. 6: "corte longitudinal continuo" | Helicoidal | E2, 5.1 |
| 7 | Guiado | E2: base, dos guías paralelas y carro móvil. Proyecto base, cap. 6: guías laterales que posicionan el envase | Carro con guías | E2, 5.1 |
| 8 | Fin de recorrido | E2: el corte se detiene antes de la franja del rodillo. Proyecto base: topes mecánicos regulables e incisión inicial | Detenerse antes de la franja; sin topes | E2, 5.4 |
| 9 | Objetivos secundarios | E2: incluye adaptación a envases. Entrega 1: incluía viabilidad industrial | Los cinco de E2 | E2, sección 2 |
| 10 | Carátula de E2 | Dice "REVISIÓN N°0"; el archivo y la consigna dicen "Reentrega_0" | No se muestra en el deck | Consigna de la Entrega 2 |

## 2. No resuelto en la Entrega 2 (decide el grupo)

| # | Tema | Qué dicen las fuentes | Cómo quedó en el deck |
|---|---|---|---|
| A | Materiales del prototipo | E2 no los define. Proyecto base: estructura de MDF, piezas en PLA/PETG. Imagen IA: todo impreso, rodillo en TPU. **Propuesta del grupo, en charla, no decidida:** varias piezas impresas en 3D en PLA, con relleno de ~30 % como máximo. Dudas abiertas: el rodillo (PLA vs. TPU o recubrimiento elastomérico, por la fricción) y si el husillo es comercial (varilla roscada o T8) o impreso en PLA. La cuchilla no está en duda: es metálica comercial según todas las fuentes | Lámina 11: "Prototipo: piezas impresas en 3D en PLA (en definición)"; el relleno, en las notas. Los rótulos de la imagen dicen "impreso" |
| B | Valores de la transmisión | E2: se definen en el dimensionamiento | Lámina 10: ejemplo rotulado "Valores de referencia" (sección 3) |
| C | Rango de envases | E2: "por definir" | Lámina 13: "Cerrar dimensiones" |
| D | Apoyos complementarios | E2: "se evaluará la necesidad" | No se mencionan |
| E | Si la correa del DXF es un cambio de diseño | E2 no la menciona | Se mantienen los engranajes (ver contradicción 1) |

## 3. Supuestos y datos

| Dato | Valor | Origen | Estado |
|---|---|---|---|
| Duración de la exposición | 15 min (6 bloques de 2:30) | Informada por el usuario el 01/nov/2026 | Confirmado |
| Ritmo de lectura | 115 palabras/min | Supuesto propio para estimar tiempos | Ensayar |
| `D_b` botella de ejemplo | 88 mm | Supuesto propio, sin medir | Medir |
| `D_b` del gráfico | 65 y 110 mm | Supuesto propio, sin medir | Medir |
| `D_r` rodillo | 50 mm | Leído del DXF; la identificación de la pieza como rodillo es interpretación propia | Confirmar con quien dibujó |
| Eje, manivela, porta rodamientos | Ø30, Ø70, 70 × 80 mm | Leídos del DXF, con la misma interpretación | Confirmar con quien dibujó |
| Husillo de referencia | T8 de 4 entradas, `L` = 8 mm | Supuesto propio; valor comercial habitual, sin cotización | Confirmar con proveedor |
| Husillo de comparación | M8, `L` = 1,25 mm, `i` = 1 | Paso normal según ISO 261; la cita la agregué y no la cotejé con la norma | Revisar |
| Reducción | `i` = 2 | Supuesto propio; E2 solo exige `i > 1` | Decidir |
| Tramo de corte | 180 mm | Supuesto propio, solo en las notas de la lámina 10 | Medir |
| Resultados | `a` ≈ 7 mm; ≈ 7 m de tira; ≈ 45 vueltas de manivela | Cálculo con los valores anteriores y la ecuación de E2 | Dependen de los supuestos |
| Métodos de ensayo | Marcas, calibre, registro de cortes | Propuesta propia, en las notas de la lámina 13; E2 solo dice qué verificar | Validar |
| Integrantes | Burelli, Fernandez, Franco Solignac, Kainer, Ledesma Blanco, Paredes | Carátula de E2 | Confirmado en fuente |
| Docentes | Abud (profesor), Cáceres Guido (ATP) | Carátula de E2; la tilde de "Cáceres" viene de la firma de la devolución | Confirmado en fuente |
| Curso, grupo, año | S1091, Grupo 1, 2026 | Carátula de E2 | Confirmado en fuente |
| Citas de antecedentes y técnicas | APA | Copiadas de E2; no las volví a contrastar con los originales | Aceptadas por la cátedra en la Entrega 1 las dos primeras |
| Ilustraciones | Generadas con IA, 31/oct/2026 | Compañeros del grupo; fecha tomada del nombre de archivo | Aclarado en cada lámina |

---
*Fuentes: `03_entrega_2/Entrega_2_Reentrega_0_S1091_Grupo_1.pdf`, `02_entrega_1/`, `01_proyecto_base/Proyecto Cortadora de Botellas PET.txt`, `04_material_grafico/` (DXF e imágenes IA), `00_consignas/Entrega 2 TP Final S1091 S1092.pdf`.*
