# CLAUDE.md — Ingeniería Mecánica I

## Estado

Docente: Abud. Dos parciales multiple choice de 30 preguntas (las incorrectas restan; las no respondidas valen 0) y final del mismo tipo, que mezcla preguntas de ambos. Abud repite preguntas textuales de un año a otro: por eso se trabaja con bancos de preguntas.

| Carpeta | Contenido |
|---|---|
| `clases/` | Apuntes de clase 1–11 (primer cuatrimestre). De la segunda mitad del año no hay carpeta propia. |
| `material_catedra/` | Apuntes y diapositivas de Abud, con los nombres del campus. Local, fuera de git. |
| `1er_parcial/` | `preparacion_parcial_1.md` (banco de ~52 preguntas) + `fuentes/`. |
| `2do_parcial/` | `preparacion_parcial_2.md` (banco de 102 preguntas reales) + `preguntas_sugeridas_parcial_2.md` (104 inventadas) + `fuentes/`. |
| `final/` | Por ahora solo `fuentes/`. |
| `campus_virtual/` | Intro + UT I al XI + esfuerzos característicos (13 docs). No se usaron: desde nov/2026 quedan solo en disco, fuera de git. |
| `proyecto/` | TP Final: cortadora de botellas PET. |
| `tp_grupal_mecanica_rotacional*/` | Dos TP grupales (detalle abajo). |

**Bancos de preguntas:** la respuesta correcta se marca `**(✓) …**`; cada pregunta lleva su nivel de confianza (`[OFICIAL]` clave del campus · `[ALUMNOS]` marcada por alumnos · `[DEDUCIDA]` del apunte) y `[★×N]` según en cuántas fuentes aparece. Las preguntas inventadas van siempre en archivo aparte, nunca mezcladas con las reales. En cada `fuentes/descargas_web/` va lo bajado de internet. Las dudas abiertas del 2° parcial y las discrepancias detectadas con el banco del 1er parcial (pendientes para el final) están en la sección 5 de `preparacion_parcial_2.md`.

**`tp_grupal_mecanica_rotacional/`:** apunte teórico de mecánica rotacional del docente Abud, revisado y corregido, + resolución completa del ejercicio de aplicación tren de engranajes, puntos 1-8; para `I` total se adopta el conjunto rotante completo de cada eje (eje + engranaje + rodamientos, criterio único, sin variantes; el Punto 8 no depende de `I` porque `P = T·ω`); informe final en `tp_mecanica_rotacional.odt`/`.pdf` (locales, excluidos de git) con su brief de estructura en `Mecanica_Rotacional_Brief_Informe.md`; vocabulario del informe: "diámetro interior" (no "bore") y sin desarrollo de `α` en el Punto 8; errores del PDF fuente — `ρ` por `g` en 8.3, factor HP·hora 10⁵ en vez de 10⁶ — se mantienen tal cual con nota de consistencia.

**`tp_grupal_mecanica_rotacional_2/`:** eje de acero Ø25×500 mm a 1400 RPM sobre rodamientos de rodillos cilíndricos SKF NU 10, `F = 500 N` a 400 mm; resolución puntos 1-7 en `Mecanica_Rotacional_2_Resolucion.md`; tabla SKF NU 10 siempre al final como Anexo A con la selección (NU 1005) destacada; pista = aro exterior fijo; `F` tangencial (el NU no admite carga axial); largo del rodillo = 0,9·B (criterio Abud), diámetro 5,5 mm estimado con aros de igual espesor (supuesto a confirmar); `I_mecanismo` = eje + 2 rodamientos como anillo con masa de catálogo, mismo criterio que el TP 1, sin contar rodillos; PDF con `pipeline_pdf/` (`make` → `build/Mecanica_Rotacional_2_Resolucion.pdf`): el PDF no incluye Anexo A ni Fuentes (quedan solo en el `.md`, los datos del NU 1005 ya están en el Punto 1), la Resolución empieza en página nueva y los diagramas ASCII salen como recuadro "Figura pendiente"; figuras PNG/PDF pendientes para una etapa posterior.

## Fuentes

**Cátedra (`material_catedra/`):** `Mecanica Rotacional.pdf` e `ingenieria_del_control_automatico.pdf` (apuntes teóricos, ciclo 2018); `6.Unidad VI proceso de Moldeo.docx`; `7.UNIDADAD VII Maquinas Herramientas.docx` y su `.pptx` de procesos con y sin arranque de viruta; `9.UNIDAD IX Elementos usados en Ingeniería.docx` (roscas, tornillos, resortes, chavetas, ajustes y tolerancias); `10.X.1 ARBOLES,ENGRANAJES.docx` (árboles, ejes, cojinetes, rodamientos, correas, engranajes); `11.UNIDAD XI Graficos, Curvas, Manuales.docx`. Las diapositivas de las unidades X y XI son casi solo imágenes con título.

**Exámenes anteriores:** inventario con origen en la sección "Fuentes" de cada banco. La más confiable es `2do_parcial/fuentes/descargas_web/2° Parcial - S1021.pdf` (campus 2021, con clave). El foro de Mecánica de UTNianos tiene 38 hilos de la materia; los adjuntos bajan sin login.

**Campus virtual (base de `campus_virtual/`; los PDF ya no están en la carpeta):** `Ing. Mec. I - Plan de Estudio.pdf` (programa y cronograma 32 clases), `1.El Ing y su Profesión.pdf`, `1.LA ING. ACTUAL UNIDAD I Y UNIDAD III.pdf`, `HABILIDADES BÁSICAS DE LA INGENIERÍA.pdf`, `1.unidad I Ingeniería y Sociedad.pdf` (37 págs — perfil, ética, patentes, Revolución Industrial), `Mantenimiento[1].pdf` (UT VII completa), `ING MEC POWER 1.pdf` y `ING MEC POWER 2.pdf` (slides de cátedra).
