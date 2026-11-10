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

## Perfil `lab_fisica/` — informes de laboratorio de Física

Para los informes de la U.D.B. Física (Física I, y Física II si sigue el mismo reglamento). En vez de `comun.mk` directo, el `Makefile` del informe incluye `lab_fisica/lab.mk`, que reutiliza `comun.mk` con otra configuración. Para un TP nuevo, copiar `lab_fisica/plantilla/` y ajustar la ruta del `include`, `SOURCE_DATE_EPOCH` y el `pdf.yaml`.

| Archivo | Qué hace |
|---|---|
| `lab.mk` | Arma el nombre de salida desde `pdf.yaml` (`A1193-TP5-G5`; individual: `A1193-TP3-Apellido`; `archivo:` lo pisa) y genera el logo en PNG para Word (`build/logo/`, no se versiona) |
| `pdf.yaml` / `docx.yaml` | Configuración de pandoc del perfil (reemplazan a `base.yaml` / `docx.yaml`): sin índice, Liberation Sans 10 pt, fórmulas en TeX Gyre Termes Math |
| `lab-fisica.lua` | Carátula de la U.D.B. (PDF, TikZ con las medidas del formulario oficial `carátula .docx`), página de título con tabla de integrantes y docentes, anexo de fotos firmadas; tablas con encabezado azul, `*Tabla N: …*` → pie gris, `> …` → recuadro de resultado; `## 1. Introducción` → sección (el `# Título` del `.md` se descarta) |
| `preambulo.tex` | Estética del PDF, la de los informes TP5/TP6: colores `#2E75B6` / `#1F3864`, encabezado con filete, pie con número de página |
| `docx_lab.py` | Word: carátula con la misma estructura de tablas que el formulario, en su propia sección; encabezado, pie y estilos del PDF. Las franjas largas de la carátula achican la letra, como en el PDF |
| `logo_utn.tex` | Símbolo UTN vectorial (TikZ), con la geometría del manual de identidad oficial; `logo_utn_png.tex` lo pasa a PNG para Word |

Los datos van en `metadata.laboratorio` del `pdf.yaml`: `curso`, `turno`, `dias`, `grupo` (se omite si el TP es individual), `tp`, `titulo`, `fecha`, `profesor`, `jtp`, `atp` (lista), `integrantes` (lista de `{apellido, nombre}`, **solo los presentes ese día**) y, opcionalmente, `anexo` (fotos de las hojas firmadas, una por página). El `.docx` (`make docx`) es la versión editable para el grupo; el PDF es la principal. Para que también se vea bien al subirlo a Google Docs, el `.docx` evita lo que Google Docs no importa: el formato de las tablas (encabezado azul, bordes) va escrito celda por celda y no como estilo de tabla, y el logo va en línea, no anclado.

`plantilla/` es genérica (TP0, datos de ejemplo): sus compilaciones de prueba no se versionan (`pipeline_pdf/**/build/` en `.gitignore`); los informes reales viven en `fisica_i/laboratorio/<concurrencia>/` y ahí sí se versiona su `build/*.pdf`.
