# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

Study notes for **UTN FRBA — Ingeniería Mecánica**, written in Markdown. The student comes from an accounting background (Contabilidad), so all explanatory material must include conceptual bridges to that prior knowledge. All notes are in **Spanish**.

## Subject folders

| Carpeta | Materia | Estado |
|---|---|---|
| `analisis_matematico_i/` | Análisis Matemático I (A1191) | 4 unidades documentadas |
| `ayga/` | Álgebra y Geometría Analítica | intro + Unidad I |
| `fisica_i/` | Física I | intro + óptica + cinemática + laboratorio (TPN1 + TPN2) |
| `griego/` | Griego Científico | alfabeto griego completo con pronunciación |
| `ingenieria_mecanica_i/` | Ingeniería Mecánica I | vacío |
| `ingenieria_y_sociedad/` | Ingeniería y Sociedad | Arocena (1 doc) + 4 textos con preguntas MC (§1–§56) |
| `quimica_general/` | Química General (R1091) | intro + estructura atómica + gases + soluciones |
| `sistemas_de_representacion/` | Sistemas de Representación | expectativas + TPs + normas IRAM + LibreCAD/DXF (3 docs) |
| `su_myf/` | (excluido de git) | — |

## Writing conventions

**File naming:** `00_introduccion.md`, `01_tema.md`, `02_tema.md`... within each subject folder.

**Document structure — topic files (`01_` onward):**
concept introduction → theory with ASCII diagrams → worked examples → summary table → common mistakes → conceptual map

**Document structure — introduction files (`00_introduccion.md`):**
what the subject is → why engineers need it → bridges from accounting → overview of major blocks → ASCII course map → practical advice

**Style rules:**
- ASCII diagrams only — no images, no LaTeX
- Formulas inline with backticks: `` `F = m·a` ``
- Accounting analogies (balance sheets, cash flows, ledger entries, weighted averages) wherever they aid understanding
- Source footer at end of each file citing PDFs and guides used

## Source material workflow

Before writing any new content:
1. Read the **official syllabus PDF** in the subject folder to identify the thematic unit (UT) and parcial coverage
2. Read the **exercise guide PDF** for that subject to extract the problem types expected in parciales
3. Read any **professor slide PDFs** provided — they define the exact vocabulary and depth required

Key sources per subject:
- **Química General:** `PLANIFICACIÓN R1091 TN 1ER CUAT Ricotti-Cruz_v2.pdf` (syllabus), `Guia QUIMICA GENERAL 2020 FINAL.pdf` (exercises), `La Química.pdf` (theory), professor slides as PDFs
- **AM1:** `Cronograma A1191 2026.pdf` (schedule)
- **AyGA:** `Programa ALGEBRA Y GEOMETRIA ANALITICA.pdf` (syllabus), `Nociones de geometría analitica y algebra lineal - KOZAK.pdf` (738-page textbook — always use `pages:` parameter); cátedra site: `https://aga.frba.utn.edu.ar/`
- **Física I:** `Programa- Bibliografia.pdf`
- **Sistemas de Representación:** `CLASE 1.pdf` (condiciones, materiales, A4, rótulo, TP 1-2), `CLASE 2.pdf` (tipos de línea IRAM, aplicaciones, TP 3-6), `CLASE 3.pdf` (caligrafía tipo A tabla completa, acotación, TP 7-10). Nota: no tiene parciales — aprobación por carpeta completa.
- **Ingeniería y Sociedad:** 4 textos del parcial, cada uno con archivo `textoN_preguntas_mc.md`. Los textos son: Bitocchi "Ciencia. Noción, origen, paradigmas y encuadre social" (§1–§27), "Estado - Nación" (§28–§36), Ramallo y Repetto "Ciencia y Tecnología en interacción. Cambio tecnológico e innovación" (§37–§47), Gottardo et al. "Globalización: noción, múltiples sentidos y perspectivas" (§48–§56).

## Convenciones específicas — Ingeniería y Sociedad (preguntas MC)

- **5 opciones** por pregunta (a, b, c, d, e) — nunca 4.
- Una sola correcta, marcada con `**negritas**`, símbolo `✓` y referencia de línea del PDF numerado: *(líneas X–Y)*.
- **Numeración de secciones continua** entre textos: no reiniciar desde §1 en cada texto nuevo; continuar desde §(N+1) donde terminó el texto anterior.
- Una pregunta por sección (recuadro numerado ☐N del texto); el stem testa el concepto central, no detalles periféricos.
- Los distractores deben ser plausibles (requieren pensar) pero sin ambigüedad excesiva; no es necesario que provengan literalmente del texto, basta coherencia conceptual.

## Git and .gitignore

PDFs, Office files (ppt/pptx, doc/docx), and images (jpg/png) are excluded from the repo — they live locally only. The `su_myf/` directory is fully excluded. Do not force-add these file types.
