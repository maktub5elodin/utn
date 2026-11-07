# Modelo 2.0 de la cortadora: modelo en FreeCAD

Modelo por código del principio de tiro descripto en [00_concepto.md](00_concepto.md): la botella va vertical sobre una varilla, la tira se enrolla en un carrete de eje vertical y ese tiro hace girar la botella contra una cuchilla fija. Sigue el método del modelo 1: `parametros.py` es la única fuente de verdad y `make` verifica todo.

![](figuras/conjunto.png)

## 1. Qué se puede confiar y qué no

- **Sale del concepto aprobado:** botella vertical con el pico arriba, carrete directo de eje vertical, sin lector, ancho fijado por un calce bajo la hoja, y ojal fijo.
- **Son supuestos `[SUP]`:** casi todas las medidas de las piezas, y también la botella (Ø88 mm, pared de 0,25 mm), el tiro de 40 N, la boquilla de 0,4 mm y la base de MDF. Se ajustan cuando lleguen la prueba 1 y las respuestas de Maty.
- **Qué se verificó:** geometría, armado, imprimibilidad y cuentas de funcionamiento (sección 3).
- **Qué no se verificó:** cómo corta la hoja, el rozamiento real, la deformación de la botella y la calidad de impresión. Eso lo responden las pruebas del concepto (sección 9 y anexo A).

## 2. Cómo está armado

![](figuras/detalle_cabezal.png)

| Grupo | Piezas | Cómo se une |
|---|---|---|
| **Eje de la botella** | Zócalo impreso, varilla roscada M8 de 380 mm | Tuerca M8 cautiva abajo y contratuerca arriba; el zócalo va a la base con 3 tornillos para madera |
| **Cabezal de corte** | Cabezal, chapita, calce, hoja, pisador | 4 tornillos para madera a la base. La hoja queda entre el calce y el pisador, apretada con 2 tornillos M3 × 25 a tuercas cautivas que entran de costado |
| **Ojal** | Ojal | 2 tornillos para madera |
| **Carrete** | Torre, dos 608ZZ, tornillo M8 × 60, carrete en dos discos, manivela, mango | La torre va a la base con 3 tornillos. El tornillo M8 gira en los rodamientos. El carrete y la manivela tienen una tuerca M8 cautiva cada uno: enroscadas una contra otra, aprietan el carrete y quedan trabadas como tuerca y contratuerca |
| **Botella** | Botella con su tapa perforada a 9 mm, vaso de lastre opcional | Baja por la varilla; el borde se apoya en la chapita |

**Medidas que ordenan todo:**

| Medida | Valor | Por qué |
|---|---|---|
| Altura de la guía sobre el MDF | 41,9 mm en la cara de la chapita; el piso de PLA está a 42,0 | El carrete tiene que tomar la tira a esa altura, encima de una torre con dos rodamientos |
| Ranura entre labios | 0,85 mm | Pared de 0,25 mm más 0,30 mm por lado |
| Labio interior | 6 mm de alto | Menos que el calce más chico (7 mm): la hoja pasa por encima |
| Chapita bajo la ranura | Desde el filo hasta 10,9 mm aguas arriba | El borde se apoya en metal justo donde se define el ancho. Una canaleta de 0,3 mm bajo el resto de la ranura evita que toque el PLA: `make` comprueba que queda a 0,3 mm |
| Distancia entre la botella y el carrete | 181 mm | Deja 46 mm entre el mango y la botella para la mano |
| Brazo de la manivela | 80 mm | Sección 4.1 del concepto |

**Sentido de giro:** vista desde arriba, la manivela gira en **sentido horario**, igual que la botella. Con rosca derecha, ese giro aprieta la tuerca de la manivela contra el carrete: al girar se traba más, no se afloja.

**Holguras de impresión**, todas en `parametros.py` para ajustarlas después de una pieza de prueba:

| Encastre | Holgura |
|---|---|
| Agujeros para tornillos y varillas | +0,4 mm en el diámetro |
| Hexágonos de tuercas cautivas | +0,3 mm entre caras |
| Alojamiento del 608ZZ, a presión | 22,15 mm para 22,00 mm |
| Ranura de la pared | 0,30 mm por lado |
| Ranura de la chapita | 0,6 mm de alto, tres capas de 0,2 mm, para una chapa de 0,5 mm; 0,2 mm por lado en el ancho |
| Calce | 0,1 mm menos que el ancho: apoya en el piso de PLA, que queda 0,1 mm más alto que la chapita |

## 3. Qué verifica `make`

Si algún control falla, `make` termina con error, y `resultados.json` dice qué y dónde. Los números de abajo son los de la última corrida.

| Control | Resultado |
|---|---|
| **Choques en el armado**, con la botella al inicio y al final del corte | Ninguno. Solo se permiten dos cruces, que son el propio corte: la hoja con la pared, y la tira con la botella de la que sale. El borde cortado se modela como hélice, en escalones de 10°: apoya en la chapita junto al filo y sube hasta `w` en una vuelta |
| **La manivela da la vuelta**, en 36 posiciones, al inicio y al final | No toca nada |
| **Lugar para la mano** | 46 mm entre el mango y la botella; el mínimo es 40 |
| **Armado en orden**, 23 pasos | Cada pieza llega a su lugar sin atravesar lo ya armado: bajando, de costado o desde abajo, según corresponda |
| **Impresión**, 14 piezas | Todas entran en la cama, sin voladizos de más de 45° y con puentes de 5,8 mm como máximo. **Ninguna necesita soportes**, y cada una es un sólido único |
| **STL** | Cada archivo se vuelve a leer: es un sólido cerrado, está apoyado en la cama y su volumen difiere menos de 0,1 % del de la pieza |
| **Borde sobre metal** | El borde toca la chapita y queda a 0,3 mm del PLA |

### Control negativo

Para saber que los controles detectan errores, se corrió una copia con tres errores a propósito: ranura más angosta que la pared, brazo de 120 mm y núcleo del carrete más bajo que la tira. `make` falló y detectó los tres:
- la botella choca con el cabezal al bajar;
- la manivela choca y la mano queda a 6 mm de la botella;
- el carrete no toma la tira.

## 4. Funcionamiento

Con el tiro de diseño de 40 N y la botella de referencia:

| Magnitud | Valor |
|---|---|
| Tira | 9 mm de ancho, 5,53 m, 20 vueltas de botella |
| Rollo | De 16 a 26,4 mm de radio |
| Vueltas de manivela por botella | 42 |
| Fuerza en la mano, rollo lleno | **13,2 N**; criterio: hasta 20 N |
| Tiro admisible con ese criterio | 61 N, o 49 N con la pared más gruesa de la tabla (0,35 mm), porque el rollo llega a 32 mm |
| Rotura de la tira | 124 N: 3,1 veces el tiro |
| Hélice | 1,86° |
| Ancho por construcción | 9,000 mm: es el espesor del calce. Solo lo afecta la tolerancia de impresión del calce, que en FDM es de unas décimas, dentro de ±0,5 mm |
| Torre del carrete, flexión entre capas | 0,58 MPa: unas 26 veces por debajo de lo que resiste el PLA entre capas |
| Tornillos del cabezal | 10 N de corte cada uno |

### Autoavance: va a hacer falta un poco de lastre

| Fuerza a lo largo del eje | Valor |
|---|---|
| Peso de la botella | 0,31 N al empezar; **0,14 N al final**, porque se va consumiendo |
| Rozamiento que frena la bajada | 0,23 N: es la componente axial, con μ = 0,35 y los labios cargados con la mitad del tiro, del lado seguro |

Al final del corte, el peso de la botella ya no alcanza con margen 2. Con un lastre total de **unos 35 g** sí alcanza. El vaso de lastre vacío pesa 17 g, así que hay que **agregarle unos 15 g**, por ejemplo tres tuercas M8. La prueba 2 dirá si hace falta: el rozamiento y la carga de los labios son supuestos.

## 5. Cómo se usa

```
make          # verifica; después, figuras, .FCStd, STL, ficha de impresión y lista de compras
```

Se cambia una medida en `parametros.py` y se vuelve a correr. Las piezas son formas generadas por código: para modificarlas se edita el código, no el `.FCStd`. Para recorrerlo en FreeCAD sirve la guía del modelo 1, [guia_revisar_en_freecad.md](../06_modelo_3d/guia_revisar_en_freecad.md): los nombres de los objetos cambian, pero el método es el mismo.

| Archivo | Qué es |
|---|---|
| `00_concepto.md` | Documento conceptual aprobado |
| `parametros.py` | Medidas con su origen, holguras y datos de las cuentas |
| `piezas.py` | Sólidos de cada pieza, armados en su lugar |
| `verificar.py` | Choques, giro de la manivela, armado en orden, impresión y funcionamiento |
| `vista.py` | Figuras y `modelo/cortadora_v2.FCStd`, con colores: naranja impreso, gris comercial |
| `exportar_stl.py` | `stl/`, un archivo por pieza impresa, orientado para la cama; además escribe la ficha y la lista |
| [ficha_impresion.md](ficha_impresion.md) | **Para Maty:** pieza, cantidad, relleno, perímetros, soportes, peso y observaciones |
| [lista_compras.md](lista_compras.md) | Piezas comerciales, con cantidades contadas del modelo |
| `resultados.json` | Números de la última verificación |

El `.FCStd` cambia en cada `make` aunque el modelo no cambie, porque FreeCAD guarda la fecha adentro. Las figuras, los STL y las fichas salen idénticos byte a byte.

---
*Fuentes: [00_concepto.md](00_concepto.md) y sus fuentes; método de `../06_modelo_3d/`; medidas de piezas comerciales: rodamiento 608ZZ (8 × 22 × 7), tuercas y tornillos métricos ISO, rosca de cuello PCO 1881 y hoja de trincheta de 18 mm. La resistencia entre capas del PLA (~15 MPa) es un valor de referencia bajo, a confirmar.*
