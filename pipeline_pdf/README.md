# pipeline_pdf/ — pipeline compartido de PDF

Toda la lógica de armado de PDF vive en un solo lugar y la usan todos los documentos; no se copia a cada materia. Las mejoras se hacen acá, y después se recompilan los PDFs de todos los documentos que la usan para verificar que no cambiaron (o que cambiaron solo como se buscaba).

| Archivo | Qué hace |
|---|---|
| `base.yaml` | Configuración común de pandoc: plantilla, fuentes, tablas, índice, caracteres Unicode, lista de filtros |
| `comun.mk` | Reglas de `make`: figuras (opcional), `.md` → `.tex` → `.pdf`, pasadas de xelatex, verificaciones (referencias, caracteres sin glifo); `make docx` → `build/<doc>.docx` |
| `docx.yaml` | Configuración de pandoc para la salida Word (`make docx`): mismo `.md` y mismos filtros de contenido, sin la estética de LaTeX (fórmulas como ecuaciones nativas de Word, figuras en PNG). El `.docx` no se versiona |
| `filtros/*.lua` | `tablas-cebra` (filas alternadas), `png-a-pdf` (PNG en el `.md`, PDF vectorial en el documento), `referencias-fig` (`@fig:x`), `solo-md` (bloques `<!-- solo-md -->` … `<!-- /solo-md -->` y diagramas ASCII no llegan al PDF; a la inversa, `<!-- solo-pdf` … `-->` entra al PDF y no se ve en el `.md`), `salto-pagina` (`<!-- salto-pagina -->` → salto de página en el PDF, invisible en el `.md`), `seleccion-catalogo` (tabla con fila marcada ► → solo esa fila, vertical), `destacados` (alertas de GitHub: `> [!CAUTION]` → recuadro rojo de error, `> [!TIP]` → recuadro verde de respuesta correcta, `> [!NOTE]` → texto azul en recuadro negro, para notas aparte; en GitHub ya se ven en color, en Word quedan como cita común), `portada-docx` (solo Word: subtítulo y fecha del `pdf.yaml`). `solo-md`, `salto-pagina`, `seleccion-catalogo` y `referencias-fig` actúan igual en PDF y en Word; `png-a-pdf` y `tablas-cebra` son solo de PDF |

Cada documento tiene solo dos archivos propios: un `Makefile` corto (define `DOC`, `SOURCE_DATE_EPOCH` y, si hay figuras, `FIG_SCRIPT`/`FIG_NAMES`, y termina con `include ../../pipeline_pdf/comun.mk`) y un `pdf.yaml` con título, subtítulo y fecha. Para un documento nuevo, copiar esos dos de `ingenieria_mecanica_i/tp_grupal_mecanica_rotacional_2/` y ajustarlos.

## Qué se versiona

Excepción a la regla general del `.gitignore` (PDFs e imágenes excluidos) para trabajos con pipeline de compilación (ej. `ayga/excercise/`, `ingenieria_mecanica_i/tp_grupal_mecanica_rotacional_2/`: `.md` → figuras Python → pandoc/xelatex → PDF, con `make`). Reglas generales en `.gitignore`, válidas para cualquier ejercicio nuevo con la misma estructura (no hace falta editarlo cada vez).

| Se versiona | Por qué |
|---|---|
| Fuentes: `.md`, scripts `.py`, `Makefile`, `pdf.yaml` (y `pipeline_pdf/` completo) | Son el trabajo en sí: texto liviano con diffs legibles |
| `build/*.pdf` (documento final) | Es el producto: se lee en GitHub sin compilar |
| `figuras/*.png` | Vista previa: el `.md` apunta a los PNG para que se vean en GitHub |

| No se versiona | Por qué |
|---|---|
| `figuras/*.pdf` | Intermedios vectoriales: ya están dentro del PDF final y `make` los regenera |
| Resto de `build/` (`.tex`, `.aux`, `.log`, `.toc`) | Subproductos de cada compilación; el `.tex` se inspecciona localmente |
| `__pycache__/`, `#*.dxf` (autoguardado de LibreCAD) | Archivos temporales de herramientas |

**Requisito: builds reproducibles.** El `Makefile` fija `SOURCE_DATE_EPOCH` (y `FORCE_SOURCE_DATE=1`) para que xelatex, incluido el que usa matplotlib para las figuras, no embeba la fecha de compilación: así el PDF y los PNG salen idénticos byte a byte si el contenido no cambió, y `make` no genera cambios falsos en git. Todo Makefile nuevo que produzca archivos versionados debe hacer lo mismo. Fuera de `build/` y `figuras/`, PDFs y PNGs siguen ignorados (bibliografía, guías, fotos); no usar `git add -f` para saltear eso.
