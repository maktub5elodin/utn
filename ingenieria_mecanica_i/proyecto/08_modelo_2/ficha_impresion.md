# Ficha de impresión: cortadora 2.0

> Generada por `exportar_stl.py` a partir del modelo: no editar a mano. Para Maty.

**Configuración común:** PLA, boquilla de 0,4 mm, capa de 0,2 mm, Bambu Lab P1S con placa texturada o lisa. **Ninguna pieza lleva soportes:** todas se comprobaron sin voladizos de más de 45° y con puentes de 5,8 mm como máximo. **Cada STL ya está orientado como se imprime:** abrirlo y laminar, sin rotarlo.

Las tuercas cautivas se colocan después de imprimir: todos los alojamientos quedan abiertos hacia abajo o de costado. No hace falta pausar la impresión.

| N.° | Archivo | Cant. | Tamaño en la cama (mm) | Relleno | Perímetros | Soportes | Peso aprox. | Tiempo aprox. | Observaciones |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `stl/01_Cabezal.stl` | 1 | 68 × 80 × 12 | 40 % | 4 | No | 24 g | 39 min | Placa de 6 mm con el labio interior; va sobre un taco de MDF. Imprimir primero, junto con el labio exterior (15), y probar con la botella real: la pared tiene que pasar entre los labios sin trabarse. Las dos tuercas M3 entran desde abajo |
| 2 | `stl/02_Calce_9mm.stl` | 1 | 34 × 46 × 8,9 | 100 % | 3 | No | 17 g | 28 min | Define el ancho de la tira: macizo, para que no se aplaste al apretar. Mide 0,1 mm menos que el ancho, porque apoya en el piso de PLA y la chapita queda 0,1 mm más abajo. Medirlo con calibre: el laminador puede dejarlo 0,1 mm arriba o abajo |
| 3 | `stl/03_Calce_7mm.stl` | 1 | 34 × 46 × 6,9 | 100 % | 3 | No | 13 g | 21 min | Para pared de 0,35 mm |
| 4 | `stl/04_Calce_8mm.stl` | 1 | 34 × 46 × 7,9 | 100 % | 3 | No | 15 g | 25 min | Para pared de 0,30 mm |
| 5 | `stl/05_Calce_10mm.stl` | 1 | 34 × 46 × 9,9 | 100 % | 3 | No | 19 g | 31 min | Para pared de 0,20 mm |
| 6 | `stl/06_Pisador.stl` | 1 | 34 × 46 × 5 | 40 % | 3 | No | 6 g | 10 min | Aprieta la hoja; caras planas |
| 7 | `stl/07_Zocalo.stl` | 1 | 59 × 53 × 28 | 30 % | 4 | No | 21 g | 38 min | La varilla lisa entra a presión suave; la traba un tornillo M3 cuya tuerca entra de canto por la ranura de arriba. El agujero del tornillo es un rombo: así se imprime sin soporte |
| 8 | `stl/08_Ojal.stl` | 1 | 38 × 18 × 53,9 | 20 % | 3 | No | 5 g | 20 min | Revisar que la ranura de 1,5 mm quede limpia |
| 9 | `stl/09_Torre.stl` | 1 | 60 × 60 × 36 | 40 % | 4 | No | 22 g | 42 min | Los 608ZZ entran a presión desde arriba. Si entran muy duros o flojos, ajustar D_608_ALOJ en parametros.py |
| 10 | `stl/10_CarreteInferior.stl` | 1 | 72,7 × 72,7 × 16 | 30 % | 3 | No | 14 g | 25 min | La tuerca M8 entra por abajo. La punta de la tira se engancha en la ranura del núcleo |
| 11 | `stl/11_CarreteSuperior.stl` | 1 | 72,7 × 72,7 × 3 | 20 % | 3 | No | 7 g | 12 min | Disco suelto: lo aprieta la manivela |
| 12 | `stl/12_Manivela.stl` | 1 | 101 × 22 × 12 | 40 % | 4 | No | 10 g | 18 min | La tuerca M8 entra por abajo. Es la pieza más cargada en flexión |
| 13 | `stl/13_Mango.stl` | 1 | 22 × 22 × 55 | 15 % | 3 | No | 11 g | 30 min | Gira sobre el tornillo M5 |
| 14 | `stl/14_Lastre.stl` | 1 | 50 × 50 × 30 | 15 % | 2 | No | 8 g | 19 min | Opcional: solo si la botella no baja sola (prueba 2). Se carga con tuercas o tornillos sueltos, no con arena: hacen falta unos 100 g |
| 15 | `stl/15_LabioExterior.stl` | 1 | 31,5 × 18,3 × 16 | 40 % | 4 | No | 2 g | 7 min | Retiene la chapita; se atornilla al taco con 2 tornillos para madera |

**Total aproximado: 194 g de PLA y 6,1 h de impresión**, sin contar purgas ni pruebas. Son estimaciones: el peso supone paredes macizas más el relleno indicado, y el tiempo, un caudal medio de 9 mm³/s más 3 s por capa. Bambu Studio da los valores exactos al laminar.

## Antes de imprimir todo

1. **Primero el cabezal (1), el labio exterior (15) y el calce de 9 mm (2).** Con la botella real: la pared tiene que entrar entre los labios y el borde tiene que apoyar en la chapita. Si la pared no entra, aumentar `HOLG_RANURA` en `parametros.py` y volver a correr `make`.
2. **Después la torre (9):** probar el ajuste de los 608ZZ antes de imprimir el carrete.
3. El resto, en cualquier orden.

## Con la boquilla de 0,2 mm

La captura de Bambu Studio que mandó Maty usa boquilla de 0,2 mm y capa de 0,10 mm. Con esa boquilla, estas piezas también se pueden imprimir, pero tardan bastante más; las holguras se calcularon para 0,4 mm.
