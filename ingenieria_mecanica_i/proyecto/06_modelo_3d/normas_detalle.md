# Normas ISO e IRAM: detalle para más adelante

Anexo de [hallazgos.md](hallazgos.md). Reúne el relevamiento de normas hecho para los planos de la cortadora.

**Qué describe:** la versión de las láminas del commit `fdebf70`, a nivel industria, con rótulo ISO 7200, tabla de alteraciones y tolerancias generales. Las láminas actuales se simplificaron a nivel de cursada, con el rótulo de la cátedra, así que "Qué se aplicó" y "Quedó" no siempre describen lo que se ve hoy. Siguen vigentes líneas, márgenes, escala, letra, método E y representación de engranajes y roscas. La investigación de origen está en [normas_investigacion_paralela.md](normas_investigacion_paralela.md).

**Criterio:** IRAM es la norma de aplicación, porque es un trabajo de una cátedra argentina y la industria local la usa. ISO es la referencia de alineación internacional. Cuando difieren, manda IRAM y queda indicado:

| Tema | ISO | IRAM | Quedó |
|---|---|---|---|
| Escala | 1:2, 1:5, 1:10… (sin 1:2,5) | Además 1:1,25, 1:2,5 y 1:7,5 | 1:2,5 en la lámina 1, declarada en una nota. Entra en A3, el formato más chico que da claridad; 1:5 queda chica para 18 globos y 1:2 exige A2. También la usa el plano NEFA 2-70-3-5010 |
| Margen izquierdo | 20 mm | 25 mm | 25 mm |
| Retícula de referencia | Obligatoria | Sin confirmar | No se dibuja: los planos NEFA y GVO revisados tampoco la llevan |
| Flecha de cota | Cerrada y rellena; ISO 129:1985 admite de 15° a 90°. El ángulo de la edición 2018 está sin confirmar | Apunte de cátedra: 4:1, unos 14° | 4:1 en el bloque del DXF. LibreCAD la redibuja a su modo |
| Rótulo | Campos de ISO 7200 | Disposición de IRAM 4508 | Campos ISO con la disposición de los planos NEFA. El texto de IRAM 4508 está sin confirmar |

Autor y aprobación dicen "A completar": los define el grupo.

| Norma ISO | Equivalente IRAM | Qué se aplicó | Fuente | Tipo de fuente |
|---|---|---|---|---|
| ISO 128-2:2022 (líneas; reemplazó a 128-20 y 128-24) | IRAM 4502-20, -22 y -24. Equivalencia sin confirmar; la 4502-24 figura como adaptación de ISO 128-24:1999 en una fuente secundaria | Gruesa 0,5 y fina 0,25; trazos de 12d y 3d; trazo largo de 24d y punto de 0,5d; trazo y dos puntos para la posición extrema | [IS 10714-20](https://law.resource.org/pub/in/bis/S01/is.10714.20.2001.pdf), [BSI](https://www.bsigroup.com/en-VN/blog/manufacturing-blog/when-six-became-one--in-the-presentation-of-lines), [apunte EIS](https://www.eis.unl.edu.ar/z/adjuntos/121/Norma_4502-24,_4504,_4505.pdf) | Primaria de la edición 128-20:1996. De la edición 2022, solo su vigencia |
| ISO 129-1:2018 (cotas) | IRAM 4513, equivalencia sin confirmar | Número sobre la línea de cota; cotas `DIMENSION` que miden solas | [ISO](https://www.iso.org/standard/64007.html), [IS 11669](https://law.resource.org/pub/in/bis/S01/is.11669.1986.pdf) (ISO 129:1985), `CLASE 3.pdf` | De la edición 2018, solo vigencia y alcance. Primaria de la edición 1985 |
| ISO 5457:1999 (formatos) | IRAM 4504, equivalencia sin confirmar | A3 apaisado; recuadro de 0,7; marcas de centrado; rótulo abajo a la derecha; margen IRAM | [IS 10711](https://law.resource.org/pub/in/bis/S01/is.10711.2001.pdf), idéntica a ISO; [apunte EIS](https://www.eis.unl.edu.ar/z/adjuntos/121/Norma_4502-24,_4504,_4505.pdf) | Primaria. La enmienda 1 de 2010 no se leyó |
| ISO 5455:1979 (escalas) | IRAM 4505, equivalencia sin confirmar | Designación en el rótulo; 1:1 y 1:2 valen en ambas | [IS 10713](https://law.resource.org/pub/in/bis/S01/is.10713.1983.pdf), [apunte EIS](https://www.eis.unl.edu.ar/z/adjuntos/121/Norma_4502-24,_4504,_4505.pdf) | Primaria para ISO; secundaria para IRAM |
| ISO 7200:2004 (rótulo) | IRAM 4508, equivalencia sin confirmar | Campos obligatorios y optativos, 180 mm de ancho, fecha de 10 caracteres, índice de revisión | [IS 11665](https://law.resource.org/pub/in/bis/S01/is.11665.2010.pdf), plantilla `A3_Landscape_ISO5457_advanced.svg` de FreeCAD, [NEFA 2-70-3-5010](https://www.argentina.gob.ar/sites/default/files/nefa_7/NEFA_2_70_3_5010.pdf) | Primaria. La plantilla y NEFA son ejemplos |
| ISO 7573:2008 (lista de piezas) | IRAM 4508, equivalencia sin confirmar | Lista sobre el rótulo, leída hacia arriba, con ítem, descripción, cantidad y especificación | [ISO](https://www.iso.org/standard/43883.html), [GVO 904](https://www.argentina.gob.ar/sites/default/files/planos_gvo/GVO_904.pdf) | Solo título y alcance de ISO: las columnas salen de los planos argentinos |
| ISO 3098-2:2000 (letra) | IRAM 4503-1, equivalencia sin confirmar | Alturas nominales de 2,5, 3,5, 5 y 7 mm; fuente `iso3098` de LibreCAD | [IS 9609-1](https://law.resource.org/pub/in/bis/S01/is.9609.1.2006.pdf), `CLASE 3.pdf` | Primaria. Sin confirmar a qué tipo de letra (A o B) corresponde esa fuente |
| ISO 2203:1973 (engranajes) | IRAM 4522-2, equivalencia sin confirmar | Rueda sin dientes hasta la cabeza; primitivo en trazo largo y punto, que sobresale de costado; fondo en fina; ninguna tapa a la otra en el engrane | [ISO 2203, muestra iTeh](https://cdn.standards.iteh.ai/samples/7006/509893f86f1947f790ca42b4bdab558d/ISO-2203-1973.pdf) | Primaria |
| ISO 6410-1:1993 (roscas) | IRAM 4520, equivalencia sin confirmar | Cresta gruesa, fondo en fina y arco de 3/4 en la vista de extremo | [ISO](https://www.iso.org/standard/12750.html), apunte de la Universidad de Cantabria visto solo en el buscador | Secundaria: el texto de la regla está sin confirmar |
| ISO 2768-1:1989 (tolerancias) | IRAM ISO 2768-1, adopción según el [Manual IRAM 2017](https://koha.ucp.edu.ar/bib/48049) | Clase m solo en el despiece, como propuesta; no aplica al conjunto, al esquema ni al estudio. Sin letra de geometría, porque la parte 2 fue reemplazada por ISO 22081 | [IS 2102-1](https://law.resource.org/pub/in/bis/S01/is.2102.1.1993.pdf), [iTeh](https://iteh.eu/catalog/standards/iso/5bb1f91d-50a4-44cf-bdbf-3652b92dd8ee/iso-22081-2021) | Primaria. Vigencia de la adopción IRAM sin confirmar |

**Sin confirmar, además:** la vigencia actual de cada norma IRAM (el listado de la UNLP es de 2007) y el texto de IRAM 4504, 4505 y 4508, conocidos por apuntes y planos. No se pudieron leer: las vistas previas de ANSI (no devuelven un PDF desde acá), la NC ISO 5455 de Cuba (el dominio no resuelve), el PDF de ISO 5457 del foro de Autodesk (pide inicio de sesión) y el apunte de Cantabria (certificado no verificable; no se forzó la descarga). El esquema cinemático usa símbolos de dibujo propios: sus símbolos no se cotejaron con una norma.

**Material de la cursada** (`sistemas_de_representacion/`, solo está `CLASE 3.pdf`; no se modificó):

| Dónde | Qué dice | Estado |
|---|---|---|
| `CLASE 3.pdf`, tabla de letras | Tipo A, de (14/14)h | Coincide con ISO 3098-2 |
| `CLASE 3.pdf`, flecha | Triángulo ennegrecido 4:1 | Dentro del rango de ISO 129:1985 |
| `CLASE 3.pdf`, modelo de caligrafía | "IRAM 4502" | Error: la letra es IRAM 4503; la 4502 es de líneas |
| `01_materiales_y_normas_iram.md` | Acotación en IRAM 4504 | Error: 4504 es formatos; acotación es 4513 |
| `01_materiales_y_normas_iram.md` | Mismo trazo de 6 y 1,5 mm en línea gruesa y fina | ISO lo hace proporcional al ancho: 6 y 1,5 corresponden solo a d = 0,5 |

**Escritor de DXF:** los archivos se escriben ahora con `ezdxf`. El escritor propio ya daba 0 errores, pero esa auditoría no prueba que AutoCAD lo acepte, y sus estructuras escritas a mano (`LAYOUT`, bloques de cotas) eran el mayor riesgo. El costo es depender de `python3-ezdxf` para regenerar. Sigue sin probarse en AutoCAD.

---
*Fuentes: las citadas en cada fila de las tablas, `sistemas_de_representacion/CLASE 3.pdf`, `sistemas_de_representacion/01_materiales_y_normas_iram.md` y [normas_investigacion_paralela.md](normas_investigacion_paralela.md).*
