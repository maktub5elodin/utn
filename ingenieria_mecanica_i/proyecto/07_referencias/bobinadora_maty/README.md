# Bobinadora de filamento de Maty (Cell Spool Winder)

Archivos de una bobinadora de filamento a manivela que Maty imprimió en su Bambu Lab P1S. Sirven de **referencia** para el modelo 2.0 de la cortadora, sobre todo el carrete con manivela y el eje de rosca doble con su "lector". **No son piezas del proyecto.** Según Maty, la bobinadora se rompe con facilidad; falta saber qué pieza.

## Origen y licencia

| Dato | Valor |
|---|---|
| Modelo | *Cell Spool Winder*, MakerWorld, modelo 561571: <https://makerworld.com/en/models/561571-cell-spool-winder> |
| Diseñador | Sergiu Irimie (usuario `Sergiu_Irimie` en MakerWorld) |
| Instrucciones de armado | Por chronos00, según el propio PDF |
| Licencia | **Standard Digital File License de MakerWorld**, según una copia de la página de julio de 2024. No se pudo confirmar en la página actual, porque MakerWorld no permite leerla de forma automática. Algunas variantes se publicaron después bajo la licencia *Exclusive* |
| Obtenido por | Maty, desde MakerWorld, el 06/nov/2026 |

**Qué implica.** Esa licencia permite usar los archivos de forma personal y no comercial, pero no redistribuirlos. Como este repositorio es público, **los STL, el PDF y las capturas quedan solo en esta computadora**: no se suben a git. Lo único versionado de esta carpeta es este README.

**Atribución.** Si el informe o la presentación muestran algo de este diseño, hay que citar: "Cell Spool Winder, de Sergiu Irimie, MakerWorld (modelo 561571)". Que Maty confirme la licencia en la página del modelo: la ve al descargarlo.

## Archivos

Los números de pieza son los de la página 1 del PDF de armado (`n.º 1` a `n.º 10`) y de la página 2 (`n.º 11` a `n.º 20`). Las medidas salieron de leer cada STL: todos son sólidos cerrados, en mm.

| Archivo | Pieza (n.º del PDF) | Tamaño (mm) | Qué tiene |
|---|---|---|---|
| `stl/Base II.stl` | Bastidor (sin número) | 250 × 98 × 246 | Pieza única, calada. Ocupa casi toda la cama de 256 × 256 mm |
| `stl/Foot.stl` | Pie (1, 2 unidades) | 208 × 50 × 22 | Encastra a presión en el bastidor |
| `stl/Worm5_v2.stl` | Eje de rosca doble con engranaje (8) | 102 × 102 × 119 | Engranaje de 66 dientes, módulo 1,5, Ø102. Eje roscado de Ø20, con dos hélices que se cruzan; puntas de Ø12 |
| `stl/Slider 02.stl` | Lector o guía del filamento (7) | 32 × 16 × 37 | Corre por un riel del bastidor y sigue las hélices del eje |
| `stl/middle gear.stl` | Engranaje intermedio doble (5) | 112 × 112 × 15 | Uno grande de 54 dientes, módulo 2, Ø112, y uno chico de 30 dientes, módulo 1,5, Ø48 |
| `stl/Axis Middle Gear.stl` | Eje corto del intermedio (3) | 25 × 22 × 35 | Cabeza hexagonal que traba en el bastidor; eje de Ø11,8 |
| `stl/Axis Small_p3.stl` | Eje del carrete de destino, con piñón (13) | 40 × 40 × 111 | Piñón de 18 dientes, módulo 2, Ø40; muñones de Ø20 y Ø15 |
| `stl/Axis Donor.stl` | Eje del carrete de origen (18) | 24 × 24 × 106 | Muñones de Ø20 y Ø15, sin engranaje |
| `stl/Axis Small_p1.stl` | Brida roscada (12, 14, 17 o 19) | 70 × 70 × 40 | Disco de Ø70 con rosca exterior; centra el carrete comercial |
| `stl/Axis Small_p2.stl` | Brida roscada, pareja de la anterior | 70 × 70 × 60 | Disco de Ø70 con rosca interior |
| `stl/Cell_Spool_Winder_-_V12.stl` | **Duplicado** de `Axis Small_p1.stl` | 70 × 70 × 40 | Misma pieza con otro orden de triángulos: mismos momentos de inercia |
| `stl/Handle.stl` | Manivela (10) | 35 × 179 × 85 | Brazo calado de 6 mm de espesor y unos 150 mm de radio; mango de 85 mm |
| `stl/Handle shaft.stl` | Eje cuadrado de la manivela | 13 × 43 × 13 | Sección cuadrada cónica, de 12,95 a 12,6 mm: entra a presión |
| `stl/Retaining Clip D12.stl`, `D12_V2`, `D15_V2`, `D16_V2`, `D18-45` | Arandelas de retención (4, 6, 9, 15, 20) | 25 a 33 de ancho | Clips en "C" para el diámetro del eje que indica el nombre |
| `Cell Spool Winder - Assembly instructions.pdf` | Instrucciones de armado | 8 páginas | Vistas explotadas y pasos de armado, en inglés |
| `capturas/bambu_studio_placas.jpeg` | Captura de Maty | — | Las cuatro placas de impresión en Bambu Studio |
| `capturas/bambu_studio_p1s.jpeg` | Captura de Maty | — | Su configuración: P1S, boquilla de 0,2 mm, capa de 0,10 mm, ABS, PLA Matte y PLA Tough |

Los dos archivos de capturas tenían el nombre de WhatsApp; se renombraron para saber qué son. Los STL conservan su nombre original.

## Cómo funciona

```
Manivela (10)
    | eje cuadrado
    v
Eje de rosca doble (8) ---------------------------> Lector (7)
    | engranaje de 66 dientes                       va y viene:
    v                                               ~12 mm por vuelta
Intermedio (5): 30 dientes -> 54 dientes            de manivela
    |
    v
Piñón de 18 dientes en el eje del carrete (13)
    |
    v
Carrete de destino: gira 6,6 veces por vuelta de manivela
```

- **Relación:** `(66/30) · (54/18) = 6,6`. La bobinadora **multiplica la velocidad**: conviene para pasar filamento, que casi no ofrece resistencia, no para tirar con fuerza.
- **Distancia entre ejes:** los dos pares dan 72 mm, `1,5 · (66 + 30)/2` y `2 · (54 + 18)/2`.
- **Avance del lector:** unos 12 mm por vuelta del eje roscado, es decir `12/6,6 ≈ 1,8 mm` por vuelta del carrete. Es el paso justo para acomodar filamento de 1,75 mm, una vuelta al lado de la otra. Las dos hélices de sentido contrario hacen que el lector vuelva solo al llegar al extremo.

El avance de 12 mm se midió por la separación de los surcos a lo largo del eje, y la relación salió de contar dientes en el STL. Se pueden confirmar contando dientes en las piezas impresas.

## Qué sirve para la cortadora

Lo analiza el documento conceptual del modelo 2.0, en `08_modelo_2/`. En resumen: sirven la manivela con eje cuadrado, la idea de las bridas que sujetan un carrete y los pies. El tren de engranajes multiplica la velocidad, que es lo contrario de lo que necesita el tiro de la tira. El lector reparte una hebra redonda a lo ancho del carrete, y una tira plana conviene enrollarla como una cinta, una vuelta sobre la otra.

---
*Fuentes: PDF de armado y STL de esta carpeta; capturas de Bambu Studio enviadas por Maty el 06/nov/2026; página del modelo en MakerWorld (561571), consultada solo a través de resultados del buscador (entre ellos, una copia de 3dgo.app de julio de 2024), porque MakerWorld bloquea la lectura automática.*
