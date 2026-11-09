# CLAUDE.md — Ingeniería Mecánica I

## Estado

intro + UT I al XI (12 docs: ingeniería y tecnología, diseño, actividad profesional, proyecto, manufactura, producción, mantenimiento, gestión, seguridad, ética, economía) + dos TP grupales de mecánica rotacional.

**`tp_grupal_mecanica_rotacional/`:** apunte teórico de mecánica rotacional del docente Abud, revisado y corregido, + resolución completa del ejercicio de aplicación tren de engranajes, puntos 1-8; para `I` total se adopta el conjunto rotante completo de cada eje (eje + engranaje + rodamientos, criterio único, sin variantes; el Punto 8 no depende de `I` porque `P = T·ω`); informe final en `tp_mecanica_rotacional.odt`/`.pdf` (locales, excluidos de git) con su brief de estructura en `Mecanica_Rotacional_Brief_Informe.md`; vocabulario del informe: "diámetro interior" (no "bore") y sin desarrollo de `α` en el Punto 8; errores del PDF fuente — `ρ` por `g` en 8.3, factor HP·hora 10⁵ en vez de 10⁶ — se mantienen tal cual con nota de consistencia.

**`tp_grupal_mecanica_rotacional_2/`:** eje de acero Ø25×500 mm a 1400 RPM sobre rodamientos de rodillos cilíndricos SKF NU 10, `F = 500 N` a 400 mm; resolución puntos 1-7 en `Mecanica_Rotacional_2_Resolucion.md`; tabla SKF NU 10 siempre al final como Anexo A con la selección (NU 1005) destacada; pista = aro exterior fijo; `F` tangencial (el NU no admite carga axial); largo del rodillo = 0,9·B (criterio Abud), diámetro 5,5 mm estimado con aros de igual espesor (supuesto a confirmar); `I_mecanismo` = eje + 2 rodamientos como anillo con masa de catálogo, mismo criterio que el TP 1, sin contar rodillos; PDF con `pipeline_pdf/` (`make` → `build/Mecanica_Rotacional_2_Resolucion.pdf`): el PDF no incluye Anexo A ni Fuentes (quedan solo en el `.md`, los datos del NU 1005 ya están en el Punto 1), la Resolución empieza en página nueva y los diagramas ASCII salen como recuadro "Figura pendiente"; figuras PNG/PDF pendientes para una etapa posterior.

## Fuentes

`Ing. Mec. I - Plan de Estudio.pdf` (programa y cronograma 32 clases), `1.El Ing y su Profesión.pdf`, `1.LA ING. ACTUAL UNIDAD I Y UNIDAD III.pdf`, `HABILIDADES BÁSICAS DE LA INGENIERÍA.pdf`, `1.unidad I Ingeniería y Sociedad.pdf` (37 págs — perfil, ética, patentes, Revolución Industrial), `Mantenimiento[1].pdf` (UT VII completa), `ING MEC POWER 1.pdf` y `ING MEC POWER 2.pdf` (slides de cátedra).
