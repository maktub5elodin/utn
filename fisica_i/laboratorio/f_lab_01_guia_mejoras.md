# Guía de mejoras — `f_lab_01.dxf`

**TP N°1 — Mediciones y Errores | Física I — UTN FRBA**  
Objetivo: convertir el archivo DXF en una figura de nivel informe de laboratorio de ingeniería.

---

## Referencia rápida — escala y posiciones clave

```
Escala adoptada:  1 mm en el dibujo = 20 mm³

Origen de la recta:  x = 52  →  4000 mm³
Fin de la recta:     x = 252  →  8000 mm³
Longitud total:      200 mm   →  4000 mm³

Conversión posición ↔ volumen:
  x_dibujo = 52 + (V − 4000) / 20
  V = 4000 + (x − 52) · 20
```

| Punto notable | x (mm) | V (mm³) |
|---|---|---|
| Inicio eje | 52 | 4000 |
| 5000 mm³ (marca mayor) | 102 | 5000 |
| Probeta V₀ | 152 | 6000 |
| Calibre V₀ | 173,5 | 6430 |
| Regla V₀ | 190,5 | 6770 |
| 7000 mm³ (marca mayor) | 202 | 7000 |
| Fin eje | 252 | 8000 |

---

## Estado actual del archivo

### Elementos ya presentes y correctos

| Elemento | Capa | Observación |
|---|---|---|
| Contorno hoja A4 (297×210) | `ROTULO_2H` | ✓ |
| Marco interior del dibujo (10,10)→(287,185) | `MARCO` | ✓ |
| Separadores de rótulo (y=45 y y=165) | `ROTULO_2H` | ✓ |
| Recuadro del área de rectas (30,60)→(267,150) | `ROTULO_2H` | ✓ |
| Líneas de referencia de eje (capa GEOMETRIA) | `GEOMETRIA` | ✓ |
| 21 ticks cada 10 mm (cada 200 mm³) en PROBETA | `2H` | ✓ |
| 21 ticks cada 10 mm (cada 200 mm³) en REGLA | `2H` | ✓ |
| 21 ticks cada 10 mm (cada 200 mm³) en CALIBRE | `2H` | ✓ |
| Flechas de eje izquierda y derecha (los tres niveles) | `2B` | ✓ |
| Tapas semicirculares de PROBETA (arcos en x=55 y x=249) | `2H` | ✓ |
| Tapas semicirculares de REGLA (arcos en x=135 y x=246) | `2H` | ✓ |
| Marcador V₀ PROBETA: tick grueso en x=152 | `2B` | ✓ |
| Marcador V₀ REGLA: tick grueso en x=190,5 | `2B` | ✓ |
| Marcador V₀ CALIBRE: símbolo ◇ en x=173,5 | `2B` | ✓ |

### Errores de geometría detectados

| Elemento | Problema | Lo que debería ser |
|---|---|---|
| Línea REGLA (y=105) | Va de x=52 a x=252 (ancho completo) | Debe ir de **x=135 a x=246** |
| Línea CALIBRE (y=150) | Va de x=52 a x=252 (ancho completo) | Debe **eliminarse** (ver nota abajo) |

> **Nota sobre el calibre:** su intervalo es `(6430 ± 20) mm³` → solo **±1 mm** en el dibujo.
> Es físicamente imposible representarlo como una barra visible a esta escala.
> El símbolo ◇ ya lo representa correctamente. Si se desea dar consistencia visual,
> se puede agregar una línea de apenas 2 mm centrada en x=173,5 (de x=172,5 a x=174,5).

---

## PASO 1 — Corregir geometría (crítico)

### 1.1 Recortar la línea de la REGLA

1. En LibreCAD: seleccionar la línea gruesa de REGLA (y=105, de x=52 a x=252, capa `2B`).
2. Borrarla.
3. Dibujar una nueva línea en capa `2B`:
   - Punto inicio: `(135, 105)`
   - Punto fin: `(246, 105)`

El resultado visual con las tapas semicirculares ya existentes cubrirá el intervalo `[5600; 7940] mm³`.

### 1.2 Eliminar (o reemplazar) la línea del CALIBRE

**Opción A — Eliminar directamente:**
Seleccionar la línea gruesa de CALIBRE (y=150, de x=52 a x=252, capa `2B`) y borrarla.
El símbolo ◇ + el tick A5 permanecen y son suficientes.

**Opción B — Reemplazar por una línea de 2 mm:**
Borrar la línea actual y dibujar en capa `2B`:
- Punto inicio: `(172,5 ; 150)`
- Punto fin: `(174,5 ; 150)`

Esto muestra visualmente que el intervalo existe pero es minúsculo.

---

## PASO 2 — Agregar texto (necesario)

En LibreCAD: **Herramienta → Texto** (o `T` con teclado).
Usar capa `2H` para textos secundarios, `2B` para etiquetas principales.
Altura de texto sugerida: **3,5 mm** para etiquetas, **2,5 mm** para valores.

### 2.1 Etiquetas de instrumento (izquierda de cada recta)

Ubicar el texto **a la izquierda de x=30**, alineado verticalmente con cada recta.

| Texto | Posición (x, y) | Capa | Altura |
|---|---|---|---|
| `PROBETA` | (10, 58) | `2B` | 3,5 mm |
| `REGLA` | (10, 103) | `2B` | 3,5 mm |
| `CALIBRE` | (10, 148) | `2B` | 3,5 mm |

> En LibreCAD el texto tiene anclaje en la esquina inferior izquierda por defecto.
> Ajustar la posición y hasta que visualmente quede centrado con la recta.

### 2.2 Valores del eje (debajo de las rectas)

Agregar los 5 valores principales debajo del área de dibujo. Posición y sugerida: **y = 52** (2 mm debajo de la recta de PROBETA en y=60, contando hacia abajo).

| Texto | Posición (x, y) | Capa | Altura |
|---|---|---|---|
| `4000` | (49, 52) | `2H` | 2,5 mm |
| `5000` | (99, 52) | `2H` | 2,5 mm |
| `6000` | (149, 52) | `2H` | 2,5 mm |
| `7000` | (199, 52) | `2H` | 2,5 mm |
| `8000` | (249, 52) | `2H` | 2,5 mm |
| `[mm³]` | (255, 52) | `2H` | 2,5 mm |

> Las posiciones x están levemente desplazadas a la izquierda para centrar el número
> sobre el tick correspondiente. Ajustar a ojo en LibreCAD.

### 2.3 Anotaciones de valor representativo y error absoluto

Agregar cerca de cada marcador central. Formato sugerido: V₀ arriba de la recta, ΔV abajo.

**PROBETA** (marcador en x=152, y=60):

| Texto | Posición (x, y) | Capa | Altura |
|---|---|---|---|
| `6000` | (150, 63) | `2H` | 2,5 mm |
| `±2000` | (148, 55) | `2H` | 2,0 mm |

**REGLA** (marcador en x=190,5, y=105):

| Texto | Posición (x, y) | Capa | Altura |
|---|---|---|---|
| `6770` | (188, 108) | `2H` | 2,5 mm |
| `±1170` | (186, 100) | `2H` | 2,0 mm |

**CALIBRE** (marcador ◇ en x=173,5, y=150):

| Texto | Posición (x, y) | Capa | Altura |
|---|---|---|---|
| `6430` | (171, 153) | `2H` | 2,5 mm |
| `±20` | (172, 145) | `2H` | 2,0 mm |

### 2.4 Leyenda de escala

Agregar en la zona libre del área de dibujo (sugerencia: esquina superior izquierda, cerca de y=148):

| Texto | Posición (x, y) | Capa | Altura |
|---|---|---|---|
| `Esc.: 1 mm = 20 mm³` | (32, 158) | `2H` | 2,5 mm |

---

## PASO 3 — Completar el rótulo (nivel informe)

La estructura del rótulo ya está dibujada. Falta agregar el contenido textual dentro de las cajas.

Zona del rótulo inferior: entre y=10 e y=45.  
Zona del rótulo superior (estrecha): entre y=165 e y=185.

### Contenido mínimo del rótulo inferior

| Campo | Texto a ingresar | Posición aproximada |
|---|---|---|
| Materia | `Física I — A1193` | (15, 38) |
| TP | `TP N°1 — Mediciones y Errores` | (15, 30) |
| Título del dibujo | `Comparación de intervalos de volumen` | (15, 22) |
| Grupo | `Grupo N°5 — Turno Noche` | (15, 15) |
| Escala | `1 mm = 20 mm³` | (200, 30) |
| Fecha | (fecha de entrega) | (200, 22) |
| Institución | `UTN FRBA` | (200, 15) |

> Altura de texto para rótulo: **3,5 mm** para título, **2,5 mm** para el resto.
> Usar capa `ROTULO_2B` para el título principal y `ROTULO_2H` para los campos secundarios.

---

## PASO 4 — Mejoras opcionales (nivel presentación)

### 4.1 Diferenciar ticks mayores de menores

Actualmente todos los ticks tienen la misma altura (±3 mm). Para que el eje sea legible sin texto de escala adicional:

**Ticks mayores** (en x=52, 102, 152, 202, 252 → múltiplos de 1000 mm³): aumentar a **±5 mm**.
**Ticks menores** (resto, cada 200 mm³): reducir a **±2 mm**.

En LibreCAD: seleccionar los ticks en esos x y editar sus puntos extremos (y_inicio = línea−5, y_fin = línea+5).

### 4.2 Nota aclaratoria sobre el calibre

Agregar un texto pequeño (altura 2 mm) junto al ◇:

```
"Intervalo ±1 mm en el dibujo"
```

Posición sugerida: (177, 153), capa `2H`.

Esto justifica ante el lector por qué el calibre aparece como punto mientras los demás tienen barras visibles.

---

## Checklist de validación final

Antes de imprimir / exportar a PDF:

- [ ] Línea REGLA va de x=135 a x=246 (no x=52 a x=252)
- [ ] Línea CALIBRE eliminada o reemplazada por segmento de 2 mm
- [ ] Etiquetas PROBETA / REGLA / CALIBRE visibles a la izquierda
- [ ] Valores 4000 / 5000 / 6000 / 7000 / 8000 [mm³] debajo del eje
- [ ] V₀ y ΔV anotados junto a cada marcador central
- [ ] Leyenda de escala presente
- [ ] Rótulo con título, TP, grupo, fecha y escala completo
- [ ] Ninguna entidad cruza fuera del marco MARCO
- [ ] Exportar como PDF con vista de impresión (A4, sin recortes)
