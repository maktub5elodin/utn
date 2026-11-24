# CLAUDE.md

Study notes for **UTN FRBA — Ingeniería Mecánica**, in Markdown, all in **Spanish**.
**No accounting analogies or "puentes contables"** in any new or edited material, any subject
(permanent since 31/oct/2026; older notes keep them unless the user asks).

## Subjects

Each subject folder has its own `CLAUDE.md` with sources, conventions and status;
it loads automatically when working there. Read it before touching that subject.

| Carpeta | Materia | Detalle |
|---|---|---|
| `analisis_matematico_i/` | Análisis Matemático I (A1191) | [CLAUDE.md](analisis_matematico_i/CLAUDE.md) |
| `ayga/` | Álgebra y Geometría Analítica | [CLAUDE.md](ayga/CLAUDE.md) |
| `fisica_i/` | Física I (A1193) | [CLAUDE.md](fisica_i/CLAUDE.md) |
| `fundamentos_informatica/` | Fundamentos de Informática | [CLAUDE.md](fundamentos_informatica/CLAUDE.md) |
| `griego/` | Griego Científico | alfabeto griego con pronunciación |
| `ingenieria_mecanica_i/` | Ingeniería Mecánica I | [CLAUDE.md](ingenieria_mecanica_i/CLAUDE.md) |
| `ingenieria_y_sociedad/` | Ingeniería y Sociedad | [CLAUDE.md](ingenieria_y_sociedad/CLAUDE.md) |
| `quimica_general/` | Química General (R1091) | [CLAUDE.md](quimica_general/CLAUDE.md) |
| `herramientas/` | (mantenimiento) | `fechas_readme.py`: fecha de última edición por materia |
| `recursos/` | (transversal) | constantes de la calculadora; enlazados en «Recursos comunes» del README junto con el alfabeto griego y las hojas de fórmulas |
| `sistemas_de_representacion/` | Sistemas de Representación | [CLAUDE.md](sistemas_de_representacion/CLAUDE.md) |
| `su_myf/` | (excluido de git) | — |

## Writing conventions

**File naming:** `00_introduccion.md`, `01_tema.md`, `02_tema.md`... per subject folder.

**Topic files (`01_`+):** concept intro → theory with ASCII diagrams → worked examples →
summary table → common mistakes → conceptual map.
**Intro files (`00_`):** what the subject is → why engineers need it → major blocks →
ASCII course map → practical advice.

**Style:**
- ASCII diagrams only, no images (subject files list their exceptions).
- Formulas: LaTeX preferred (`$…$`, `$$…$$`, decimal comma `{,}`); simple ones may use
  backticks. One convention per file. Inside ASCII diagrams, plain text.
- Source footer at the end of each file citing PDFs and guides used.

## README

GitHub only shows `README.md`, so it must stay current. Update it in the same commit as
any change to a subject's content:
- **Materias table:** one row per subject (`griego/` lives in «Recursos comunes», not here).
  «Último trabajo» = one short line on what was done on the «Última edición» date — not
  the subject's full document list. «Última edición» = `python3 herramientas/fechas_readme.py -v`
  (date `dd/mmm/yyyy`, lowercase 3-letter month). It counts real content edits only:
  no `make` rebuilds, no files rewritten identical, no maintenance commits.
- **Recursos comunes:** cross-subject reference material (calculator constants, Greek
  alphabet, formula sheets). Link sheets in place; don't move them out of their subject.
- New top-level folders go in the table above and, if readers need them, in the README.

## Source material workflow

Before writing new content: 1) read the subject's syllabus PDF (unit, parcial coverage);
2) the exercise guide PDF (problem types); 3) professor slides (vocabulary and depth).
Each subject's `CLAUDE.md` lists its key sources. Large PDFs: always use `pages:`.

## Git

PDFs, Office files and images (jpg/png) are git-ignored and stay local; `su_myf/` is fully
excluded. Never `git add -f`. Exception: documents built with `pipeline_pdf/`
(`.md` → figures → PDF via `make`) version their `build/*.pdf` and `figuras/*.png`;
the `.gitignore` rules already cover any new one.
Commits that only fix, rebuild or reorganize — no new content — start with
`mantenimiento:` (e.g. pipeline changes, path renames, PDFs regenerated without
source edits); `fechas_readme.py` ignores them so they don't bump «Última edición».

## PDF pipeline

All PDF/Word build logic lives in `pipeline_pdf/` (shared, never copied). Each document
has only a short `Makefile` (`include ../../pipeline_pdf/comun.mk`) and a `pdf.yaml`.
Makefiles must set `SOURCE_DATE_EPOCH` for reproducible builds. `build/` holds only
deliverables (`.pdf`, `.docx`); intermediates (`.tex`, `.aux`, `.log`, `.toc`) go to a
hidden, git-ignored `.build/` next to it — also in the standalone LaTeX sheets. After changing the
pipeline, rebuild every document that uses it. Filters, markers (`<!-- solo-md -->`,
`<!-- salto-pagina -->`, `> [!CAUTION]`…) and the versioning tables:
[pipeline_pdf/README.md](pipeline_pdf/README.md).
