# Datos de referencia — TP Mecánica Rotacional

Extraído de dos imágenes fuente (calidad de escaneo baja/media):
- `momentos_de_inercia.jpg` — tabla de momentos de inercia de cuerpos rígidos (buena legibilidad).
- `tablas_de_rodamientos.jpg` — catálogo SKF, rodamientos rígidos de una hilera de bolas, serie 62 (legibilidad media-baja, ver notas de confianza al final).

Este archivo es para consumo de Claude Code en el resto del TP. Datos numéricos tal como fueron leídos de la fuente; no recalculados ni verificados contra el catálogo oficial.

---

## 1. Momentos de inercia de cuerpos rígidos

Notación: `M` = masa del cuerpo, `R` = radio, `R1`/`R2` = radios interior/exterior, `l` = longitud, `2R` = diámetro.

| Ref | Cuerpo | Eje | Fórmula |
|---|---|---|---|
| a | Aro (anillo delgado) | Eje del cilindro (perpendicular al plano del aro, por el centro) | `I = M·R²` |
| b | Cilindro anular (anillo grueso / tubo) | Eje del cilindro | `I = (M/2)·(R1² + R2²)` |
| c | Cilindro sólido (o disco) | Eje del cilindro | `I = (M·R²)/2` |
| d | Cilindro sólido (o disco) | Diámetro central (perpendicular al eje del cilindro, por el centro) | `I = (M·R²)/4 + (M·l²)/12` |
| e | Varilla delgada | Eje perpendicular a la varilla, por el centro | `I = (M·l²)/12` |
| f | Varilla delgada | Eje perpendicular a la varilla, por un extremo | `I = (M·l²)/3` |
| g | Esfera sólida | Cualquier diámetro | `I = (2·M·R²)/5` |
| h | Cascarón esférico delgado | Cualquier diámetro | `I = (2·M·R²)/3` |
| i | Aro (anillo delgado) | Cualquier diámetro (en el plano del aro) | `I = (M·R²)/2` |
| j | Aro (anillo delgado) | Línea tangente cualquiera (en el plano del aro) | `I = (3·M·R²)/2` |

**Confianza: alta.** Imagen nítida, fórmulas estándar de mecánica racional, consistentes con bibliografía.

---

## 2. Rodamientos rígidos de una hilera de bolas — SKF, Serie 62

Designación base = `62` + Tamaño (ej. Tamaño `04` → `6204`). Sufijos de variante: `Z` (una placa), `2Z` (dos placas), `RS` (una placa+arandela de caucho), `2RS` (dos), `N` (ranura en aro exterior), `ZN` (placa + ranura).

### 2.1 Dimensiones y capacidades (alta confianza — tabla nítida)

| Tamaño | Designación | d (mm) | D (mm) | B (mm) | d1 (mm) | r (mm) | C dinámica (kg) | Co estática (kg) | n máx (rpm) |
|---|---|---|---|---|---|---|---|---|---|
| 00 | 6200 | 10 | 30 | 9  | 15   | 1   | 400   | 224   | 20000 |
| 01 | 6201 | 12 | 32 | 10 | 16.3 | 1   | 540   | 300   | 20000 |
| 02 | 6202 | 15 | 35 | 11 | 19.2 | 1   | 610   | 355   | 16000 |
| 03 | 6203 | 17 | 40 | 12 | 21.5 | 1   | 750   | 440   | 16000 |
| 04 | 6204 | 20 | 47 | 14 | 26   | 1.5 | 1000  | 655   | 16000 |
| 05 | 6205 | 25 | 52 | 15 | 31.4 | 1.5 | 1100  | 710   | 13000 |
| 06 | 6206 | 30 | 62 | 16 | 37.5 | 1.5 | 1530  | 1000  | 13000 |
| 07 | 6207 | 35 | 72 | 17 | 43.9 | 2   | 2000  | 1370  | 10000 |
| 08 | 6208 | 40 | 80 | 18 | 49.8 | 2   | 2280  | 1600  | 10000 |
| 09 | 6209 | 45 | 85 | 19 | 54.4 | 2   | 2550  | 1830  | 8000  |
| 10 | 6210 | 50 | 90 | 20 | 57.4 | 2   | 2750  | 2120  | 8000  |
| 11 | 6211 | 55 | 100| 21 | 63.8 | 2.5 | 3400  | 2600  | 8000  |
| 12 | 6212 | 60 | 110| 22 | 70.9 | 2.5 | 4050  | 3200  | 6000  |
| 13 | 6213 | 65 | 120| 23 | 77.9 | 2.5 | 4400  | 3550  | 6000  |
| 14 | 6214 | 70 | 125| 24 | 81.6 | 2.5 | 4800  | 3700  | 5000  |
| 15 | 6215 | 75 | 130| 25 | 87   | 2.5 | 5200  | 4250  | 5000  |
| 16 | 6216 | 80 | 140| 26 | 93.4 | 3   | 5700  | 4550  | 5000  |
| 17 | 6217 | 85 | 150| 28 | 102.8| 3   | 6550  | 5500  | 4000  |
| 18 | 6218 | 90 | 160| 30 | —    | 3   | 7500  | 6300  | 4000  |
| 19 | 6219 | 95 | 170| 32 | —    | 3.5 | 8500  | 7200  | 4000  |
| 20 | 6220 | 100| 180| 34 | —    | 3.5 | 9650  | 8150  | 3000  |
| 21 | 6221 | 105| 190| 36 | —    | 3.5 | 10400 | 9150  | 3000  |
| 22 | 6222 | 110| 200| 38 | —    | 3.5 | 11200 | 10400 | 3000  |
| 24 | 6224 | 120| 215| 40 | —    | 3.5 | 11400 | 10400 | 3000  |
| 26 | 6226 | 130| 230| 40 | —    | 4   | 12200 | 11600 | 2500  |
| 28 | 6228 | 140| 250| 42 | —    | 4   | 12900 | 12900 | 2500  |
| 30 | 6230 | 150| 270| 45 | —    | 4   | 13700 | 14300 | 2500  |
| 32 | 6232 | 160| 290| 48 | —    | 4   | 14300 | 15600 | 2000  |
| 34 | 6234 | 170| 310| 52 | —    | 5   | 14600 | ?     | 2000  |
| 36 | 6236 | 180| 320| 52 | —    | 5   | ?     | 19000 | 2000  |
| 38 | 6238 | 190| 340| 55 | —    | 5   | 17600 | 20400 | 1600  |
| 40 | 6240 | 200| 360| 58 | —    | 5   | 20000 | 24400 | 1600  |

Notas de la tabla de dimensiones: a partir del Tamaño 6232 en adelante, los rodamientos se construyen con separador macizo de latón (indicado en la imagen original, no repetido fila por fila). Celdas con `?` = número no legible en la copia.

### 2.2 Peso y variantes de sellado disponibles (confianza media — ver nota)

| Tamaño | Peso (kg) | Z / 2Z | RS / 2RS | N / ZN (ranura ext.) |
|---|---|---|---|---|
| 00 | 0.032 | Sí | Sí | No |
| 01 | 0.037 | Sí | Sí | No |
| 02 | 0.045 | Sí | Sí | No |
| 03 | 0.065 | Sí | Sí | No |
| 04 | 0.106 | Sí | Sí | Sí |
| 05 | 0.128 | Sí | Sí | Sí |
| 06 | 0.199 | Sí | Sí | Sí |
| 07 | 0.288 | Sí | Sí | Sí |
| 08 | 0.366 | Sí | Sí | Sí |
| 09 | 0.407 | Sí | Sí | Sí |
| 10 | 0.463 | Sí | Sí | Sí |
| 11 | 0.607 | Sí | Sí | Sí |
| 12 | 0.783 | Sí | Sí | Sí |
| 13 | 0.990 | Sí | Sí | Sí |
| 14 | 1.27  | Sí | Sí | Sí |
| 15 | ~1.48 (dudoso) | Sí | Sí | Sí |
| 16 | 1.40  | Sí | Sí | Sí |
| 17 | 1.79  | Sí | Sí | Sí (solo N/ZN, sin RS) |
| 18 | 2.15  | No | No | No |
| 19 | 2.42  | No | No | No |
| 20 | 3.14  | No | No | No |
| 21 | 3.79  | No | No | No |
| 22 | 4.36  | No | No | No |
| 24 | ~5.15 (verificar) | No | No | No |
| 26 | ~5.82 (verificar) | No | No | No |
| 28 | ~7.47 (verificar) | No | No | No |
| 30 | ~9.41 (verificar) | No | No | No |
| 32 | ~14.3 (verificar) | No | No | No |
| 34 | ~17.5 (verificar) | No | No | No |
| 36 | ~18.3 (verificar) | No | No | No |
| 38 | ~23.0 (verificar) | No | No | No |
| 40 | ~28.2 (verificar) | No | No | No |

**Confianza: alta para Tamaño 00–17 (texto nítido). Media-baja para Tamaño 18–40** (la copia está borrosa en esa zona; los pesos marcados "verificar" son la mejor lectura posible pero deberían confirmarse contra el catálogo SKF oficial antes de usarlos en un cálculo que dependa de precisión, aunque las dimensiones/capacidades de la sección 2.1, tomadas de la otra mitad de la misma imagen, son legibles y confiables para todo el rango).

Aclaración general: los rodamientos de ejecución `2Z` y `2RS` vienen lubricados de fábrica (no deben desarmarse ni relubricarse). Los de ejecución `RS`/`2RS` admiten como velocidad máxima solo 2/3 de la indicada en la tabla (n máx.).

---

## Uso previsto

Estos datos sirven de insumo para el TP grupal de Mecánica Rotacional (selección de rodamiento y cálculo de momento de inercia del sistema). Al usar la sección 2.2 para tamaños ≥18, marcar explícitamente cualquier resultado derivado como dependiente de un dato no verificado.
