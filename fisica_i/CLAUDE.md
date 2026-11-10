# CLAUDE.md — Física I (A1193)

## Estado

intro + óptica + cinemática + laboratorio (por concurrencia: `1er_concurrencia/` TPN1 + TPN2; `3er_concurrencia/` TP5 resorte + TP6 Arquímedes) + `energia_casos_limite/` (estudio personal, no resumen — ver nota abajo) + `hoja_formulas/` + `1er_parcial/`.

**`hoja_formulas/`:** hoja **de estudio**, no de examen: mismo esquema y estética que la de Química — LaTeX directo con `make`, solo las fórmulas que pide el usuario — pero **sin** exigir una carilla; referencias al pie: Sears *Física universitaria* vol. 1, 11.ª ed., 2004, ISBN 970-26-0511-3, en papel, y *University Physics with Modern Physics* 13th ed. en inglés, ISBN 978-0-321-69686-1; sin numeración de ecuaciones del libro; hasta ahora: cap. 2, aceleración constante; cap. 3, proyectiles, movimiento circular uniforme y velocidad relativa en el espacio; cap. 4, leyes de Newton; cap. 5, plano inclinado, rozamiento, dinámica circular y resistencia de fluidos; cap. 6, trabajo y energía cinética: análisis completo en el `.md`, pasa al PDF de a poco a medida que el usuario estudia, con la columna «PDF» de cada tabla; ya están el trabajo con fuerza constante, la derivación desde la ecuación del cap. 2 (enlazadas con estrella roja) y el teorema trabajo-energía; notación del Sears, `s` y `φ`; la aceleración radial va como `a_rad = γ`, `γ` es la notación del docente; en el `.md` de esta hoja, las explicaciones van con figuras matplotlib, `figuras_mcu.py` → `make figuras`, nunca con diagramas ASCII.

**`1er_parcial/`:** correcciones del parcial rendido el 2/sep/2026, los 5 ejercicios: mismo método que `analisis_matematico_i/1er_parcial/` (ver `analisis_matematico_i/CLAUDE.md`), con estas diferencias: unidades en todo el desarrollo, un ejercicio ocupa las páginas que necesite sin dejar renglones sueltos, y las notas aparte van con `> [!NOTE]`.

## Fuentes

`Programa- Bibliografia.pdf`; libro de cátedra `Physics — Sears, Young, Freedman, Zemansky` (12ª/13ª ed., en `Libros/` de la raíz del repo, en inglés).

## `energia_casos_limite/`

A diferencia del resto de la carpeta (resúmenes de clase), es un espacio de estudio personal — parte de una derivación propia (cinemática → trabajo-energía) y la extiende a casos límite reales (lanzamiento de bala y jabalina de alto rendimiento) con datos de récords mundiales y comparativa de potencia humana. No sigue la estructura estándar de "tema" del resto del repo a propósito. Usa notación con referencia en inglés junto al símbolo (`h`=height, `w`=weight, `W`=Work, `μs`/`μk`=static/kinetic friction) — preferencia explícita del usuario, ver memoria `user_fisica_ingles_vocabulario`.

## Laboratorio (`laboratorio/`)

Organizado por concurrencia (`1er_concurrencia/` = TPN1 mediciones + TPN2 óptica; `3er_concurrencia/` = TP5 resorte + TP6 Arquímedes/densidad; el usuario faltó a la 2da, TP3/TP4). Curso **A1193, Turno Noche, Grupo N°5** (integrantes: Fleitas, González, Lissi, Palazzo, Paredes, Pérez — nombres y apellidos siempre con sus tildes). Informes según `laboratorio/propuesta de estructura de informe.pdf` + `laboratorio/Reglamento Tps Laboratorios Física UTN.docx.pdf`; cada concurrencia trae su apoyo teórico propio de los docentes (ej. `3er_concurrencia/Apoyo MOA.pdf`, `Arquímides_V3.pdf`) y a veces una planilla de cálculo (`Planilla_arquimedes_Laboratorio.xlsx`). Estructura: encabezado → Introducción (objetivos + marco teórico) → Procedimiento Experimental → Resultados y Análisis (tablas numeradas con pie) → Conclusiones por objetivo → Anexo de Cálculos → footer de fuentes. **Sin diagramas ASCII en los informes de laboratorio** (excepción a la convención general del repo — preferencia del usuario); las figuras (esquemas, gráficos del Excel) se referencian en el `.md` y el usuario las inserta al armar el Word. Incertezas y redondeo según TP1 (error a 1 cifra significativa). Cada informe puede tener una restricción de consistencia con material firmado/oficial que no hay que "corregir" — ver memoria `project_fisica_lab_3ra_concurrencia`.

**Informes nuevos (desde la 4ta concurrencia):** perfil `pipeline_pdf/lab_fisica/` (`.md` → PDF `A1193-TPn-G5.pdf` con la carátula de la U.D.B. + `.docx` editable para el grupo con `make docx`); copiar `pipeline_pdf/lab_fisica/plantilla/`. Fórmulas en LaTeX (`$…$`), ya no en backticks. Antes de armar cada TP, preguntar al usuario: individual o grupal, presentes ese día, fecha, docentes (si siguen siendo los mismos) y nombre de archivo si es individual. Los TP1/2/5/6 ya entregados quedan como están.
