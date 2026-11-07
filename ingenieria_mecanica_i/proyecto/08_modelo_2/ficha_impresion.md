# Ficha de impresión: cortadora 2.0

> Generada por `exportar_stl.py` a partir del modelo: no editar a mano. Para Maty.

**Configuración común:** PLA, boquilla de 0,4 mm, capa de 0,2 mm, Bambu Lab P1S con placa texturada o lisa. **Ninguna pieza lleva soportes:** todas se comprobaron sin voladizos de más de 45° y con puentes de 5,8 mm como máximo. **Cada STL ya está orientado como se imprime:** abrirlo y laminar, sin rotarlo.

Las tuercas cautivas se colocan después de imprimir: todos los alojamientos quedan abiertos hacia abajo o de costado. No hace falta pausar la impresión.

| N.° | Archivo | Cant. | Tamaño en la cama (mm) | Relleno | Perímetros | Soportes | Peso aprox. | Observaciones |
|---|---|---|---|---|---|---|---|---|
| 1 | `stl/01_Cabezal.stl` | 1 | 68 × 80 × 58 | 30 % | 4 | No | 151 g | Imprimir primero y probar con la botella real: la pared tiene que pasar por la ranura sin trabarse. La chapita entra por la ranura de la cara de atrás (0,6 mm de alto: no limpiarla con nada que la agrande). Las tuercas M3 entran de costado |
| 2 | `stl/02_Calce_9mm.stl` | 1 | 34 × 46 × 8,9 | 100 % | 3 | No | 17 g | Define el ancho de la tira: macizo, para que no se aplaste al apretar. Mide 0,1 mm menos que el ancho, porque apoya en el piso de PLA y la chapita queda 0,1 mm más abajo. Medirlo con calibre: el laminador puede dejarlo 0,1 mm arriba o abajo |
| 3 | `stl/03_Calce_7mm.stl` | 1 | 34 × 46 × 6,9 | 100 % | 3 | No | 13 g | Para pared de 0,35 mm |
| 4 | `stl/04_Calce_8mm.stl` | 1 | 34 × 46 × 7,9 | 100 % | 3 | No | 15 g | Para pared de 0,30 mm |
| 5 | `stl/05_Calce_10mm.stl` | 1 | 34 × 46 × 9,9 | 100 % | 3 | No | 19 g | Para pared de 0,20 mm |
| 6 | `stl/06_Pisador.stl` | 1 | 34 × 46 × 5 | 40 % | 3 | No | 6 g | Aprieta la hoja; caras planas |
| 7 | `stl/07_Zocalo.stl` | 1 | 59 × 53 × 28 | 30 % | 4 | No | 20 g | La tuerca M8 entra por abajo, antes de atornillarlo |
| 8 | `stl/08_Ojal.stl` | 1 | 38 × 18 × 53,9 | 20 % | 3 | No | 5 g | Revisar que la ranura de 1,5 mm quede limpia |
| 9 | `stl/09_Torre.stl` | 1 | 60 × 60 × 36 | 40 % | 4 | No | 22 g | Los 608ZZ entran a presión desde arriba. Si entran muy duros o flojos, ajustar D_608_ALOJ en parametros.py |
| 10 | `stl/10_CarreteInferior.stl` | 1 | 72,7 × 72,7 × 16 | 30 % | 3 | No | 14 g | La tuerca M8 entra por abajo. La punta de la tira se engancha en la ranura del núcleo |
| 11 | `stl/11_CarreteSuperior.stl` | 1 | 72,7 × 72,7 × 3 | 20 % | 3 | No | 7 g | Disco suelto: lo aprieta la manivela |
| 12 | `stl/12_Manivela.stl` | 1 | 101 × 22 × 12 | 40 % | 4 | No | 10 g | La tuerca M8 entra por abajo. Es la pieza más cargada en flexión |
| 13 | `stl/13_Mango.stl` | 1 | 22 × 22 × 55 | 15 % | 3 | No | 11 g | Gira sobre el tornillo M5 |
| 14 | `stl/14_Lastre.stl` | 1 | 50 × 50 × 30 | 15 % | 2 | No | 8 g | Opcional: solo si la botella no baja sola (prueba 2) |

**Total aproximado: 319 g de PLA**, sin contar purgas ni pruebas. El peso es una estimación: paredes macizas más el relleno indicado. Bambu Studio da el valor exacto al laminar.

## Antes de imprimir todo

1. **Primero el cabezal (1) y el calce de 9 mm (2).** Con la botella real: la pared tiene que entrar en la ranura y el borde tiene que apoyar en el piso. Si la pared no entra, aumentar `HOLG_RANURA` en `parametros.py` y volver a correr `make`.
2. **Después la torre (9):** probar el ajuste de los 608ZZ antes de imprimir el carrete.
3. El resto, en cualquier orden.

## Con la boquilla de 0,2 mm

La captura de Bambu Studio que mandó Maty usa boquilla de 0,2 mm y capa de 0,10 mm. Con esa boquilla, estas piezas también se pueden imprimir, pero tardan bastante más; las holguras se calcularon para 0,4 mm.
