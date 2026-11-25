# UTN FRBA — Ingeniería Mecánica · Apuntes

Notas de estudio para la carrera de **Ingeniería Mecánica** en la [Universidad Tecnológica Nacional — Facultad Regional Buenos Aires](https://www.frba.utn.edu.ar/).

Escritas en Markdown, en español, con diagramas ASCII. Algunos documentos (correcciones de parciales, ejercicios resueltos, informes de laboratorio, hojas de fórmulas) usan figuras generadas con Python y se compilan a PDF con `make`.

---

## Materias

«Último trabajo» resume lo que se hizo en la fecha de «Última edición»: el día en que se editó por última vez el contenido de la materia (no cuenta recompilar PDFs ni el mantenimiento). El detalle de cada materia está en su carpeta.

| Carpeta | Materia | Último trabajo | Última edición |
|---|---|---|---|
| [`analisis_matematico_i/`](analisis_matematico_i/) | Análisis Matemático I | Resolución paso a paso del 1er parcial, con figura y PDF | 09/nov/2026 |
| [`ayga/`](ayga/) | Álgebra y Geometría Analítica | 1er parcial: los 7 modelos del campus resueltos por parcial, con figuras 3D (el rendido repitió uno) | 25/nov/2026 |
| [`fisica_i/`](fisica_i/) | Física I | Hoja de fórmulas, cap. 8 (cantidad de movimiento, impulso, choques); 2do parcial con la notación de la hoja | 23/nov/2026 |
| [`fundamentos_informatica/`](fundamentos_informatica/) | Fundamentos de Informática | 2do parcial: programa en C++98, casos de prueba y archivo de entrega | 09/nov/2026 |
| [`quimica_general/`](quimica_general/) | Química General | Hoja de fórmulas: referencia del Chang al pie | 09/nov/2026 |
| [`ingenieria_y_sociedad/`](ingenieria_y_sociedad/) | Ingeniería y Sociedad | Mapa conceptual interactivo de Arocena (CTS) | 10/jun/2026 |
| [`ingenieria_mecanica_i/`](ingenieria_mecanica_i/) | Ingeniería Mecánica I | 2° parcial 2026 (Temas 16 y 17) resuelto y cruzado con el banco, para el recuperatorio | 24/nov/2026 |
| [`sistemas_de_representacion/`](sistemas_de_representacion/) | Sistemas de Representación | TP19 en LibreCAD | 30/sep/2026 |

---

## Recursos comunes

Material de consulta que sirve para varias materias.

| Recurso | Qué es |
|---|---|
| [Constantes de la calculadora](recursos/calculadora_casio_constantes.md) | Las 47 constantes científicas de la Casio fx-991LA CW (CODATA 2018), por categoría, y cómo llegar a cada una en el catálogo |
| [Alfabeto griego](griego/00_alfabeto_griego.md) | Las 24 letras con pronunciación y su uso en ciencia e ingeniería |
| Hoja de fórmulas de Física I | [Apunte](fisica_i/hoja_formulas/hoja_formulas.md) · [PDF](fisica_i/hoja_formulas/build/hoja_formulas.pdf) |
| Hoja de fórmulas de Química General | [Apunte](quimica_general/hoja_formulas/hoja_formulas.md) · [PDF](quimica_general/hoja_formulas/build/hoja_formulas.pdf) |

---

## Estructura de cada apunte

Los archivos de tema siguen siempre la misma estructura:
introducción conceptual → teoría con diagramas ASCII → ejemplos resueltos → tabla resumen → errores comunes → mapa conceptual.

Las fórmulas se escriben en LaTeX (`$…$` y `$$…$$`, con coma decimal), que GitHub muestra renderizado; las muy simples pueden ir con backticks (`` `E = m·c²` ``). Cada archivo usa una sola convención.

---

## Nota

Los PDFs de cátedra, presentaciones, apuntes oficiales, archivos de Office e imágenes no están incluidos en el repositorio (`.gitignore`). Se versiona el contenido propio: Markdown, scripts y Makefiles. Excepción: los documentos que se compilan con [`pipeline_pdf/`](pipeline_pdf/) (`.md` → figuras → PDF) versionan también su PDF final (`build/*.pdf`) y las figuras PNG (`figuras/*.png`), para leerlos en GitHub sin compilar.
