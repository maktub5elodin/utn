# CLAUDE.md — Análisis Matemático I (A1191)

## Estado

4 unidades documentadas + `1er_parcial/` (correcciones del parcial rendido el 17/oct/2026, PDF con `pipeline_pdf/`)
+ `2do_parcial/`.

**2do parcial** (Taylor, integrales, ecuaciones diferenciales, integral definida, series):
- `2do_parcial/fuentes/` (local, no versionado): 10 fotos del apunte de la clase de repaso con el modelo
  de examen, renombradas `ejN_tema[_hojaM].jpeg`, y el resumen de alumno del 2do parcial.
- `2do_parcial/modelo/`: `Modelo_2do_Parcial.md` → `make` → PDF de estudio. Los 7 ejercicios en orden de
  cronograma (no el de las hojas), cada uno en dos páginas: lo que hay que saber → resolución → respuesta →
  figura → «si cambian los datos» → «Ojo» (errores del apunte incluidos). Hoja de fórmulas al final.
  `figuras.py` comprueba cada resultado con assert. El segundo miembro del Ej. 4 ($\tfrac{3}{2}x^2$) se
  reconstruyó de la derivada que figura en el apunte.

## Fuentes

Todo local, no versionado; nombres en minúscula con guion bajo.
- `material_catedra/`: `cronograma_2026.pdf` (schedule), `apunte_funciones_cavallaro.pdf` (Ing. F. Cavallaro),
  `definiciones_y_teoremas.pdf`, `formulas.pdf`, `series_numericas_cafferata.pdf` (S. Cafferata Ferri, edUTecNe, §8.2).
- `1er_parcial/fuentes/`: `modelo_ejemplo_3.pdf` (el «1° parcial - Ejemplo 3» de la cátedra) y
  `resumen_1er_parcial_martin_y_herrera.pdf` (resumen de alumno); el del 2do parcial está en `2do_parcial/fuentes/`.

## Convenciones específicas — correcciones del 1er parcial (`1er_parcial/`)

Documento `Correcciones_1er_Parcial.md` → `make` → `build/Correcciones_1er_Parcial.pdf`; figuras en `figuras_correcciones.py`. Corrige los errores del parcial del 17/oct/2026: los ejercicios 1, 3, 4 y 5 son los del modelo `1° parcial - Ejemplo 3.pdf` (en disco, `fuentes/modelo_ejemplo_3.pdf`); el ejercicio 2 fue distinto (distancia mínima de $P(0;6)$ a $x^2 - y^2 = 16$); en el 4, la rama $x > 0$ vino como $\operatorname{sen} x / x$ (equivalente a la $-\cos(x + \pi/2)/x$ del modelo).

- **Brevedad:** solo lo que el usuario pide, sin secciones extra (tabla resumen, errores comunes, mapa conceptual, verificaciones no pedidas) y sin diagramas ASCII. Por ejercicio: enunciado → desarrollo → error → respuesta → figura.
- **Colores:** recuadro rojo `> [!CAUTION]` con "**Mi error:** …" (uno por error del parcial; no repetir dentro del recuadro una fórmula que ya está arriba: se colorea la de arriba con `{\color{BrickRed} …}`); recuadro verde `> [!TIP]` con "**Respuesta:** …"; resultados intermedios destacados (raíces, derivadas, valores de parámetros, primera aparición de una expresión clave) con `{\color{RoyalBlue} …}`; valores obtenidos en recuadro verde `{\color{ForestGreen}\boxed{…}}` (ej. $y = 3$, $x = 5$, cada recta tangente).
- **Desarrollo:** pasos intermedios visibles (expandir cuadrados, `aligned` para cadenas de igualdades); valores exactos con raíz para coordenadas, decimales aproximados para distancias.
- **Figuras:** una por ejercicio, al final o junto al planteo, **sin nota al pie** (`![](figuras/…png)` sin texto alternativo); sin elementos que no se mencionan en el texto (ej. asíntotas); etiquetas sin pisar curvas ni líneas; los puntos que el usuario probó "por fuerza bruta" en el parcial van en violeta con su distancia en decimales.
- **PDF:** sin índice (`table-of-contents: false` en `pdf.yaml`) y sin fuentes (bloque `<!-- solo-md -->`); cada ejercicio en dos hojas, el N en las páginas 2N−1 y 2N (`<!-- salto-pagina -->` antes de cada ejercicio y, si hace falta, dentro); la notación de Leibniz de las reglas de la cadena (y la $\frac{d}{dy}$ del Ej. 2) va solo en el `.md`, el PDF muestra la versión con prima (`<!-- solo-pdf … -->`).
- **Eficiencia:** una sesión por ejercicio; confirmar el enunciado exacto antes de resolver; revisar figuras con el menor número de renders posible.
