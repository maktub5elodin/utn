# Investigación paralela de normas: insumo para los planos de la cortadora PET

> Preparado en paralelo a tu propia búsqueda, para no duplicar esfuerzo. Te aporta tres cosas: fuentes primarias legales y gratuitas (textos completos, no resúmenes), ejemplos reales de planos que cumplen las normas, para hacer ingeniería inversa, y una corrección a lo que te pedí antes. Verificá vos cada dato antes de aplicarlo: acá queda marcado qué es fuente primaria y qué es secundaria.

## 0. Corrección importante: la escala 1:2,5 SÍ es válida

En el prompt anterior te dije que 1:2,5 "no es una escala normalizada". Eso es cierto para ISO, pero **no para IRAM**:

- **ISO 5455:1979** no incluye 1:2,5. Escalas de reducción: 1:2, 1:5, 1:10, 1:20, 1:50, 1:100… Ampliación: 2:1, 5:1, 10:1, 20:1, 50:1. Fuente primaria: IS 10713:1983, adopción india idéntica a ISO 5455 (ver tabla de fuentes).
- **IRAM 4505** sí la incluye. Recomienda 1:1,25, 1:2, **1:2,5**, 1:5 y 1:7,5, y sus inversas para ampliación. Fuente: el apunte de la Escuela Industrial Superior (UNL) que ya descargaste.
- **En la práctica argentina se usa:** los planos ferroviarios NEFA de la CNRT (sección 2) usan "E. 1:2,5".

**Conclusión:** la 1:2,5 puede quedar si la lámina declara que sigue IRAM 4505. Decidí vos el criterio general (sección 3) y aplicalo de forma coherente.

## 1. Fuentes primarias gratuitas y legales

| Tema | Fuente | Qué trae | Tipo |
|---|---|---|---|
| Rótulo (ISO 7200:2004) | `https://law.resource.org/pub/in/bis/S01/is.11665.2010.pdf` (IS 11665, idéntica a ISO 7200:2004) | Texto completo: Tabla 1 con campos, cantidad de caracteres y obligatoriedad | Primaria |
| Escalas (ISO 5455:1979) | `https://law.resource.org/pub/in/bis/S01/is.10713.1983.pdf` (IS 10713, idéntica a ISO 5455) | Tabla completa de escalas recomendadas y regla de designación | Primaria |
| Escalas, versión en castellano | `https://descargas.epconsgtmo.co.cu/Normalizacion%20Actualizadas/Normas%20de%20la%20construccion/Normas%20De%20Dibujo/NC%20ISO%205455-2004%20Dibujo%20T%C3%A9cnico.Escalas.pdf` (NC ISO 5455:2004, Cuba) | La misma tabla, en español | Primaria (adopción nacional) |
| Formatos y márgenes (ISO 5457:1999) | `https://forums.autodesk.com/autodesk/attachments/autodesk/v1232/48404/1/ISO5457.pdf` | Margen izquierdo de 20 mm (archivado) y 10 mm en el resto, rótulo abajo a la derecha, marcas de centrado | Primaria, pero alojada en un foro |
| Engranajes (ISO 2203:1973) | `https://webstore.ansi.org/preview-pages/ISO/preview_ISO+2203-1973.pdf` | Vista previa con las reglas principales | Primaria, parcial |
| Líneas (ISO 128-2:2022) | `https://webstore.ansi.org/preview-pages/ISO/preview_ISO+128-2-2022.pdf` | Vista previa: índice y alcance | Primaria, parcial |
| Roscas (ISO 6410-1:1993) | `https://webstore.ansi.org/preview-pages/ISO/preview_ISO+6410-1-1993.pdf` | Vista previa | Primaria, parcial |
| Lista de normas IRAM de dibujo, con vigencias | `https://catedras.ing.unlp.edu.ar/grafica/giga/gpi/apuntes/anexo01_normasiram07.pdf` (UNLP, 2007; ya lo descargaste) | Números y títulos: 4520 roscas, 4522-2 engranajes, 4513 acotación, etc. | Secundaria confiable, puede estar desactualizada |

Ojo: la nota de que iso.org bloquea la lectura no aplica a estas fuentes. Son adopciones nacionales publicadas o vistas previas oficiales.

## 2. Ingeniería inversa: planos reales que ya cumplen las normas

### 2.1 Plantillas ISO 7200 que ya tenés instaladas (sin descargar nada)

FreeCAD trae plantillas de TechDraw que siguen ISO 7200 y ISO 5457. Están dentro del AppImage, por ejemplo `.../Mod/TechDraw/Templates/A3_Landscape_ISO7200TD.svg` (y sus variantes de otros formatos).

- Extraelas con `~/Aplicaciones/FreeCAD.AppImage --appimage-extract` en build/, o buscalas con `App.getResourceDir()` desde freecadcmd.
- Leé el SVG: margen, recuadro, posición y medidas del rótulo, nombres de los campos y alturas de letra. Son números concretos ya aplicados por la comunidad de FreeCAD.
- Cuidado: que una plantilla diga "ISO7200" no garantiza que sea perfecta. Contrastala con la Tabla 1 de IS 11665.

### 2.2 Planos industriales argentinos reales: serie NEFA y GVO (CNRT, argentina.gob.ar)

Son planos ferroviarios de fabricación, públicos y en PDF. Muestran cómo aplica las IRAM la industria argentina. Ejemplos:
- `https://www.argentina.gob.ar/sites/default/files/subidos_tanda_5/NEFA_1258.pdf`
- `https://www.argentina.gob.ar/sites/default/files/nefa_7/NEFA_2_70_3_5010.pdf` (escala 1:2,5)
- `https://www.argentina.gob.ar/sites/default/files/nefa_7/NEFA_2_70_3_5031.pdf`
- `https://www.argentina.gob.ar/sites/default/files/subidos_tanda_4/NEFA_803.pdf`
- `https://www.argentina.gob.ar/sites/default/files/planos_gvo/GVO_904.pdf`

Qué extraer de ellos, con pdftotext y pdftoppm:
- **Campos del rótulo que usa la industria:** N.° de plano, escala, emisión, firma y fecha de aprobación, alteraciones, ítem, cantidad, descripción y especificación.
- **Notas estándar:** "Tolerancias no especificadas" con norma de referencia, y "Símbolos de labrado IRAM 4517". Sirve para decidir cómo escribir la nota de tolerancias generales.
- **Lista de materiales:** columnas y orden.
- **Cómo se indican escalas múltiples** en una misma lámina.

Son planos viejos (algunos de décadas atrás): tomá el formato y la lógica, no las referencias normativas puntuales, que pueden estar reemplazadas.

### 2.3 Material didáctico de la UTN, con criterio de cátedra argentina

- UTN FRH, Unidad 00 "Introducción a los planos" (2025): `https://frh.cvg.utn.edu.ar/mod/resource/view.php?id=73286`. Puede pedir login; si falla, no insistas. Según el resumen del buscador, aplica IRAM 4504 con 25 mm a la izquierda y 10 mm en el resto, y define rótulo, lista de materiales y lista de modificaciones según IRAM 4508.

## 3. Criterio sugerido cuando ISO e IRAM difieren

Propuesta, a confirmar con el usuario si dudás: **IRAM como norma de aplicación** (es un trabajo de una cátedra argentina, y la industria local la usa) e **ISO como referencia de alineación internacional**. En cada lámina, la nota indica la norma aplicada.

Los conflictos detectados hasta ahora:

| Tema | ISO | IRAM | Sugerencia |
|---|---|---|---|
| Margen izquierdo | 20 mm (ISO 5457) | 25 mm (IRAM 4504) | 25 mm (IRAM) |
| Escala 1:2,5 | No está en ISO 5455 | Sí en IRAM 4505 | Válida bajo IRAM; también sirve 1:2 o 1:5 si preferís quedar dentro de ambas |
| Letra | ISO 3098: tipo A (h/14) y tipo B (h/10, la más usada) | IRAM 4503 (los apuntes de la cursada usan tipo A, h = 5) | Tipo A, h = 3,5 en cotas y 5 en títulos, como en la cursada; la fuente iso3098.lff de LibreCAD sirve |
| Flecha de cota | ISO 129-1: cerrada y rellena; según una fuente secundaria, 15° y largo de unas 10 veces el ancho de línea | Apunte de la cátedra: triángulo ennegrecido 4:1 | Mantené la 4:1 de la cátedra; anotá la diferencia en la tabla de hallazgos.md |
| Rótulo | ISO 7200: 8 campos obligatorios (ver sección 4) | IRAM 4508: rótulo, lista de materiales y lista de modificaciones | Que el rótulo cumpla los dos: campos ISO 7200 con la disposición IRAM 4508 |

## 4. Datos verificados con fuente primaria

**ISO 7200:2004, campos del rótulo** (IS 11665, Tabla 1 y siguientes). Según la tabla, los campos de identificación son:
- legal owner (M);
- identification number (M, 16 caracteres);
- revision index (O, 2);
- date of issue (M, 10);
- segment/sheet number (M, 4);
- number of sheets (O, 4);
- language code (O).

Además hay campos descriptivos (title, M) y administrativos (approval person, M; creator, M; document type, M). **Leé la tabla completa en el PDF:** sólo confirmé los campos que aparecieron en la búsqueda.

Mapeo propuesto al proyecto:
- Propietario legal: "UTN FRBA - Ing. Mecánica I - Grupo 1"
- N.° de identificación: algo como "CPET-001" a "CPET-004"
- Índice de revisión: "A"
- Fecha de emisión: "2026-11-02" (ISO 8601)
- Hoja: "1/4" … "4/4"
- Título: el de cada lámina
- Tipo de documento: "Plano de conjunto", "Despiece", "Esquema", "Estudio"
- Creador y aprobación: dejalo **en blanco o como "A completar"**. No inventes nombres ni asignes integrantes: el usuario pidió explícitamente no asignar personas.

**ISO 2203:1973, engranajes** (vista previa oficial):
- En vista sin cortar, el engranaje se dibuja como sólido limitado por la superficie de cabeza, **sin dientes**.
- La superficie primitiva va en **línea fina de trazo largo y punto**, incluso en partes ocultas y en cortes.
- En vista normal al eje, se dibuja la circunferencia primitiva.
- Las figuras de la norma usan el método E (primer diedro).
- Para el pie del diente y el detalle de las líneas, completá con la vista previa y con IRAM 4522-2.

**ISO 5455:** ver la sección 0. La designación completa es la palabra "ESCALA" seguida de la relación.

## 5. Tareas propuestas, en orden

1. Descargá a `build/normas/` las fuentes de la sección 1, ignoradas por git, y leelas. Confirmá o corregí cada dato de las secciones 0 y 4.
2. Extraé las plantillas ISO 7200 de FreeCAD (2.1) y medilas.
3. Bajá 3 o 4 planos NEFA o GVO (2.2), rasterizalos y mirá rótulo, notas y lista de materiales.
4. Con eso, decidí el criterio (sección 3) y rediseñá: rótulo con los campos ISO 7200 en disposición IRAM 4508, márgenes, escalas (manteniendo o cambiando la 1:2,5, con justificación), nota de tolerancias generales y representación de engranajes según ISO 2203 e IRAM 4522-2.
5. Completá la tabla de normas de hallazgos.md con cuatro columnas: norma | qué se aplicó | fuente (URL) | tipo de fuente (primaria, vista previa o secundaria).
6. Regenerá con make, auditá con ezdxf, revisá a ojo, y hacé commit y push.

## 6. Lo que esta investigación NO pudo confirmar

- Equivalencias exactas IRAM ↔ ISO, salvo IRAM 4502-24 (adaptación modificada de ISO 128-24) e IRAM 4503-0 (de ISO 3098-0). El resto quedó sin confirmar.
- Vigencia actual de cada norma IRAM: el listado de la UNLP es de 2007.
- La flecha de 15° de ISO 129-1: sólo tengo fuentes secundarias.
- El ancho máximo del rótulo según ISO 7200 o ISO 5457: las fuentes secundarias dicen 170 o 180 mm y se contradicen. Medilo en la plantilla de FreeCAD o en el PDF de ISO 5457.
