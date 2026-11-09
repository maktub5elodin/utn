# CLAUDE.md — Análisis Matemático I (A1191)

## Estado

4 unidades documentadas + `1er_parcial/` (correcciones del parcial rendido el 17/oct/2026, PDF con `pipeline_pdf/`).

## Fuentes

`Cronograma A1191 2026.pdf` (schedule).

## Convenciones específicas — correcciones del 1er parcial (`1er_parcial/`)

Documento `Correcciones_1er_Parcial.md` → `make` → `build/Correcciones_1er_Parcial.pdf`; figuras en `figuras_correcciones.py`. Corrige los errores del parcial del 17/oct/2026: los ejercicios 1, 3, 4 y 5 son los del modelo `1° parcial - Ejemplo 3.pdf` (el archivo en disco se llama `1 parcial - Ejemplo 3.pdf`); el ejercicio 2 fue distinto (distancia mínima de $P(0;6)$ a $x^2 - y^2 = 16$); en el 4, la rama $x > 0$ vino como $\operatorname{sen} x / x$ (equivalente a la $-\cos(x + \pi/2)/x$ del modelo).

- **Brevedad:** solo lo que el usuario pide, sin secciones extra (tabla resumen, errores comunes, mapa conceptual, verificaciones no pedidas) y sin diagramas ASCII. Por ejercicio: enunciado → desarrollo → error → respuesta → figura.
- **Colores:** recuadro rojo `> [!CAUTION]` con "**Mi error:** …" (uno por error del parcial; no repetir dentro del recuadro una fórmula que ya está arriba: se colorea la de arriba con `{\color{BrickRed} …}`); recuadro verde `> [!TIP]` con "**Respuesta:** …"; resultados intermedios destacados (raíces, derivadas, valores de parámetros, primera aparición de una expresión clave) con `{\color{RoyalBlue} …}`; valores obtenidos en recuadro verde `{\color{ForestGreen}\boxed{…}}` (ej. $y = 3$, $x = 5$, cada recta tangente).
- **Desarrollo:** pasos intermedios visibles (expandir cuadrados, `aligned` para cadenas de igualdades); valores exactos con raíz para coordenadas, decimales aproximados para distancias.
- **Figuras:** una por ejercicio, al final o junto al planteo, **sin nota al pie** (`![](figuras/…png)` sin texto alternativo); sin elementos que no se mencionan en el texto (ej. asíntotas); etiquetas sin pisar curvas ni líneas; los puntos que el usuario probó "por fuerza bruta" en el parcial van en violeta con su distancia en decimales.
- **PDF:** sin índice (`table-of-contents: false` en `pdf.yaml`) y sin fuentes (bloque `<!-- solo-md -->`); cada ejercicio en dos hojas, el N en las páginas 2N−1 y 2N (`<!-- salto-pagina -->` antes de cada ejercicio y, si hace falta, dentro); la notación de Leibniz de las reglas de la cadena (y la $\frac{d}{dy}$ del Ej. 2) va solo en el `.md`, el PDF muestra la versión con prima (`<!-- solo-pdf … -->`).
- **Eficiencia:** una sesión por ejercicio; confirmar el enunciado exacto antes de resolver; revisar figuras con el menor número de renders posible.
