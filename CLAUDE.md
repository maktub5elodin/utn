# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

Study notes for **UTN FRBA — Ingeniería Mecánica**, written in Markdown. The student comes from an accounting background (Contabilidad), so all explanatory material should include conceptual bridges to that prior knowledge. Notes are in **Spanish**.

## Repository structure

```
utn/
├── fisica_i/        # Física I — notes and explanations
│   ├── 00_introduccion.md
│   └── 01_optica.md
└── ayga/            # Álgebra y Geometría Analítica
    ├── 00_introduccion.md
    └── Programa ALGEBRA Y GEOMETRIA ANALITICA.pdf   ← official syllabus
    └── Nociones de geometría analitica y algebra lineal - KOZAK.pdf  ← main textbook
```

`fisica_i/` is its own git repo. `ayga/` is not versioned yet.

## Writing style and conventions

- Files are numbered `00_`, `01_`, `02_`... within each subject folder.
- Every new topic file follows the structure established in `fisica_i/01_optica.md`: concept introduction → theory with ASCII diagrams → worked examples → summary table → common mistakes.
- Introduction files (`00_introduccion.md`) follow the structure in `fisica_i/00_introduccion.md`: what the subject is → why engineers need it → bridges from accounting → overview of major blocks → ASCII course map → practical advice.
- Use ASCII diagrams (not images) for all figures.
- Analogies referencing accounting concepts (balance sheets, cash flows, ledger entries) are encouraged wherever they aid understanding.
- Formulas are written inline with backticks: `` `F = m·a` ``. No LaTeX.

## Key source material

- **Official syllabus PDFs** live in each subject folder — always read them before writing new content to stay aligned with the 9 thematic units and parcial structure.
- **AyGA cátedra site:** `https://aga.frba.utn.edu.ar/` — theory, videos, GeoGebra applets, and solved exams.
- **Kozak textbook** (`ayga/`) is the primary AyGA reference; it is 738 pages — use `pages:` parameter when reading it.
