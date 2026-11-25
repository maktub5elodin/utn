# CLAUDE.md — Álgebra y Geometría Analítica

## Estado

intro + Unidad I.

Estructura: `tp7/` (TP7 ej. 1 b, pipeline a PDF), `interactivos/` (HTML de rotación 2D/3D),
`material_catedra/` (PDFs de la cátedra, locales), `1er_parcial/`, `2do_parcial/` (fuentes del campus, sin trabajar todavía;
el rendido fue el `1246`).

**1er parcial** (Parte A, Unidades I–V):
- `1er_parcial/fuentes/` (local, no versionado): los 7 modelos del campus renombrados por fecha
  (`AAAA-MM-DD_turno_instancia.pdf`; el nombre original del campus está en el documento) y la foto
  del parcial rendido el 08/08/2026, que es **idéntico al Tema 2 del 13/05/2019** (P1).
- `1er_parcial/por_parcial/`: un PDF con todos resueltos, por parcial (P1–P7 cronológicos; Tema 1 completo,
  Tema 2 abreviado salvo el de P1), figuras 3D por ejercicio de geometría (`figuras.py`, vista elegida por
  `vista_auto` y cada figura verificada con assert), apéndices: herramientas, frecuencia, resultados.
  Cada ejercicio del Tema 1 lleva `<!-- temas: COD … -->`; `temas.py` (códigos en `TEMAS`) arma la tabla y el gráfico.
  Los enunciados se cotejan con la imagen de la página, no con `pdftotext` (corrió una `t` de traspuesta).
- Pendiente, si se pide: `1er_parcial/por_tema/`, generado con un script que lea esas marcas
  (como `fisica_i/2do_parcial/integrador/`).

## Fuentes

En `material_catedra/` (local, no versionado): `programa.pdf` (syllabus), `kozak_nociones.pdf` (Kozak, *Nociones de geometría analítica y álgebra lineal*, 738 páginas — always use `pages:` parameter), `guia_ejercicios.pdf`, `unidad_7_teoria.pdf`, `tp7_resueltos_parte_{1,2,3}.pdf`; cátedra site: `https://aga.frba.utn.edu.ar/`
