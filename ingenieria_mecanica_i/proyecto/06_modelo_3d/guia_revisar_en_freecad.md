# Cómo abrir y revisar el modelo 3D en FreeCAD

Guía para recorrer la cortadora sin saber FreeCAD todavía. Se hace en orden, con FreeCAD abierto al lado, y lleva cerca de una hora. Al final vas a saber moverte por el modelo, medirlo, mirar adentro, hacerlo avanzar y comprobar vos mismo los hallazgos.

Probada con FreeCAD 1.1.3. Los valores "esperados" y los bloques de Python se comprobaron sobre el modelo actual; los clics dentro de la ventana no se pudieron probar, así que algún detalle de la pantalla puede variar.

> **Regla de esta guía: no guardes.** Revisar no cambia nada mientras no guardes. Al cerrar, elegí **no guardar**. Si guardaste sin querer, se recupera desde la carpeta `06_modelo_3d`:
> `git restore modelo/cortadora_pet.FCStd`

## 1. Qué archivo es cada uno

| Archivo | Qué es | Para qué sirve |
|---|---|---|
| `modelo/cortadora_pet.FCStd` | Modelo para FreeCAD, con marcas de giro | **Con este trabajás en esta guía** |
| `salida/cortadora_pet.step` | Las 22 piezas para otros programas | SolidWorks y similares (sección 9) |
| `salida/cortadora_pet.mp4` | Video del corte completo | Ver la botella consumiéndose y la tira |
| `parametros.py` | Todas las medidas y su origen | **Acá se cambia el modelo**, no en el `.FCStd` |

Lo más importante para no confundirse: **este modelo lo genera código**. En otros tutoriales vas a ver piezas con croquis y operaciones editables. Acá no: cada objeto es una forma ya terminada, sin historial. Sirve para mirar, medir y comprobar. Si cambiás una medida en la ventana, el próximo `make` la pisa.

## 2. Abrirlo

En una terminal:

```bash
cd ~/utn/ingenieria_mecanica_i/proyecto/06_modelo_3d
~/Aplicaciones/FreeCAD.AppImage modelo/cortadora_pet.FCStd
```

Tarda unos segundos. Después, una sola vez:

1. En **View → Panels**, activá **Python Console** y **Report View**.
2. En el selector de **workbenches** de la barra superior, elegí **Part**. Un workbench es un juego de herramientas; este es el indicado para sólidos ya hechos.
3. Pulsá `V` y después `F` para encuadrar la máquina.

```
+-----------------------------------------------------------+
| Menus  |  Workbench selector            |  toolbars       |
+------------------+----------------------------------------+
| Model (árbol)    |                                        |
| lista de objetos |                 3D View                |
|                  |                                        |
+------------------+                                        |
| Property View    |                                        |
| Data | View      |                                        |
+------------------+----------------------------------------+
| Report View             |  Python Console                 |
+-------------------------+---------------------------------+
```

La guía está en español, y los nombres de la interfaz van en inglés, como en tu FreeCAD.

## 3. Moverse por la vista

Tu instalación usa el estilo de navegación **CAD**:

| Acción | Cómo |
|---|---|
| Seleccionar | Clic izquierdo |
| Seleccionar varias | `Ctrl` + clic |
| Zoom | Rueda |
| Desplazar | Mantener apretado el botón del medio y mover |
| Rotar | Mantener apretado el botón del medio, sumar el izquierdo y mover |

| Tecla | Vista | Qué se ve en esta máquina |
|---|---|---|
| `0` | Isometric | El conjunto |
| `1` | Front | El largo: botella, carro y husillo |
| `2` | Top | Guías, base y carro |
| `3` | Right | Desde el borde abierto de la botella, hacia el cuello |
| `V`, `F` | Fit All | Sirve para recuperarse cuando te perdiste |
| `V`, `S` | Fit Selection | Acercarse a una pieza |

Referencia de los ejes: **X** es el eje de la botella, con el cuello hacia −X y el borde abierto hacia +X; **Y** es lateral; **Z** va hacia arriba.

**Práctica:** pulsá `0`, rotá, perdete a propósito y volvé con `V`, `F`.

## 4. Conocer las piezas

Hacé clic en un objeto del árbol (pestaña **Model**) y se resalta en la vista. La **barra espaciadora** (Toggle Visibility) lo oculta o lo muestra. Con eso podés ir desarmando la máquina.

El árbol tiene 28 objetos:

| Conjunto | Objetos | Cómo se mueve |
|---|---|---|
| Fijo | `Base`, `Guias`, `Tuerca`, `Portacuchilla`, `Cuchilla` | No se mueve |
| Carro | `Carro`, `SoporteCuello`, `RodamientoCuello`, `Placa1`, `Placa2` | Avanza en +X |
| Eje del rodillo | `Eje`, `NucleoRodillo`, `Rodillo`, `Manivela`, `EngranajeZ1` | Gira y avanza con el carro |
| Husillo | `Husillo`, `EngranajeZ2`, `Collares` | Gira y avanza con el carro |
| Botella | `Mordaza`, `BotellaFija`, `Cuerpo`, `Helice` | Gira y avanza con el carro |
| Solo ayudas visuales | `MarcaZ1`, `MarcaZ2`, `MarcaHusillo`, `MarcaRodillo`, `Marcas`, `Tira` | No son piezas |

Las placas están casi transparentes a propósito, para dejar ver los engranajes.

**Sólidos y mallas.** La botella y el husillo (`BotellaFija`, `Cuerpo`, `Helice`, `Husillo`) son **mallas**: superficies hechas de triángulos, livianas para el video. Con ellas la herramienta de medición puede no servir; sus medidas se piden por consola (sección 8).

**Por qué 28 objetos acá y 22 piezas en el STEP.** El STEP no lleva las marcas ni las mallas de ayuda, trae la botella y el husillo como sólidos, y separa `Guias` y `Collares` en dos piezas cada uno.

**Práctica: seguir la cadena.** Encontrá cada pieza en el árbol, en este orden, y ubicala en la vista:

```
Manivela
   |  mismo eje
   v
  Eje ---- mismo eje ----> Rodillo ---- contacto ----> Botella
   |                     (Ø50, gira)                    (Ø88)
   |  mismo eje
   v
EngranajeZ1 (20 dientes)
   |  engrane
   v
EngranajeZ2 (40 dientes)
   |  mismo eje
   v
Husillo ---- rosca en la Tuerca fija ----> avanza el Carro
```

Una sola entrada, la manivela, mueve todo. Si podés explicar esta cadena mirando la máquina, entendiste el mecanismo.

## 5. Medir

Abrí **Tools → Measure**, hacé clic en lo que quieras medir (una arista, una cara circular, dos caras) y leé el resultado. Compará con esta tabla:

| Qué medir | Valor esperado |
|---|---|
| Largo del `Eje` | 149 mm |
| Diámetro del `Eje` | 30 mm |
| Diámetro del `Rodillo` | 50 mm |
| Ancho del `Rodillo` | 20 mm |
| Largo × ancho × espesor de la `Base` | 380 × 230 × 8 mm |
| Ancho de cara de los engranajes | 10 mm |
| Distancia entre los ejes del `EngranajeZ1` y el `EngranajeZ2` | 60 mm |

Si el clic no toma la pieza que querés, ocultá con la barra espaciadora la que estorba. Para el diámetro exterior de los engranajes, conviene la consola: el dentado no ofrece una cara circular donde medirlo.

**Si una medida no coincide,** avisá antes de corregir nada: puede ser un clic en otra arista o un error del modelo.

## 6. Mirar adentro

| Herramienta | Dónde | Sirve para |
|---|---|---|
| Plano de corte | **View → Clipping View** | Cortar la vista con un plano móvil. Solo cambia lo que ves, no las piezas |
| Wireframe | `V`, `3` | Ver todas las aristas, también las de atrás |
| As is, la vista normal | `V`, `1` | Deshacer el estilo anterior |
| Toggle Transparency | Seleccionar la pieza y `V`, `T` | Ver a través de ella |

**Qué revisar:**

1. Con la vista `3` y el plano de corte, los engranajes entre `Placa1` y `Placa2`: `EngranajeZ1` sobre el `Eje`, `EngranajeZ2` sobre el `Husillo`.
2. Con la vista `1`, el rodillo en voladizo: el `Eje` sale de `Placa2` y lo sostiene de un solo lado (hallazgo 2.2).
3. El cuello de la botella dentro de la `Mordaza`, y esta dentro de `RodamientoCuello`.
4. En la base, cómo los patines del `Carro` abrazan las `Guias`.

## 7. Hacerla avanzar

El archivo no se anima solo, pero se puede mover desde la consola. Hacé clic en la **Python Console**, pegá este bloque completo con `Ctrl+V` y pulsá `Enter` hasta volver a ver `>>>`:

```python
import sys, time
sys.path.insert(0, "/home/juje/utn/ingenieria_mecanica_i/proyecto/06_modelo_3d")
import parametros as P, piezas as Z
doc = App.ActiveDocument
doc.Tira.ViewObject.Visibility = False
CARRO = ["Carro", "SoporteCuello", "RodamientoCuello", "Placa1", "Placa2"]
EJE = ["Eje", "NucleoRodillo", "Rodillo", "Manivela", "EngranajeZ1", "MarcaZ1", "MarcaRodillo"]
HUSILLO = ["Husillo", "EngranajeZ2", "Collares", "MarcaZ2", "MarcaHusillo"]
BOTELLA = ["Mordaza", "BotellaFija", "Marcas", "Cuerpo", "Helice"]
def posar(vueltas):
    est = P.estado(vueltas)
    for n in CARRO:
        doc.getObject(n).Placement = Z.colocar(None, "carro", None, None, est)
    for n in EJE:
        doc.getObject(n).Placement = Z.colocar(None, "gira", (P.Y_R, P.Z_R), "rodillo", est)
    for n in HUSILLO:
        doc.getObject(n).Placement = Z.colocar(None, "gira", (P.Y_H, P.Z_H), "husillo", est)
    for n in BOTELLA:
        doc.getObject(n).Placement = Z.colocar(None, "gira", (0.0, P.H_EJE), "botella", est)
    Gui.updateGui()
    print(f"{vueltas} vueltas: carro {est['s']:.1f} mm, botella {est['botella'] / 360:.2f} vueltas")

```

No hace falta entender todo el código. Lo central es `P.estado(vueltas)`: a partir de las vueltas de manivela calcula el resto de la cadena, con las mismas relaciones de `parametros.py`.

Ahora escribí, de a una línea:

```python
posar(0.25)
posar(10)
posar(45)
posar(0)
```

Lo esperado:

| Orden | Carro | Botella |
|---|---|---|
| `posar(10)` | 40 mm | 5,68 vueltas |
| `posar(45)`, final del corte | 180 mm | 25,57 vueltas |
| `posar(0)`, inicio | 0 mm | 0 vueltas |

Para verlo en movimiento (tarda unos segundos; mientras tanto no toques la ventana):

```python
for i in range(181):
    posar(i * 0.25)
    time.sleep(0.02)

posar(0)
```

**Qué mirar:**

- Con `posar(45)`, el carro queda cerca de la `Tuerca`, y el husillo sobresale mucho de la base.
- Con `posar(0.25)` y la vista `3`, la manivela se mueve en sentido horario (hallazgo 2.4).
- El engranaje grande gira la mitad que el chico. Las marcas de color ayudan a seguirlo.

**Limitación:** acá la botella no se consume, así que el `Cuerpo` atraviesa la cuchilla. Es esperable: el corte y la tira solo están en el video.

## 8. Comprobar los hallazgos

Comprobá vos los números de [hallazgos.md](hallazgos.md). Con el bloque de la sección 7 ya cargado, pegá este:

```python
posar(0)
botella = Z.botella_solida()
barrido = Z.barrido_manivela(P.X_RODILLO[1] + 12, +1)
print("Manivela dentro de la botella, mm3:", round(barrido.common(botella).Volume))
print("Placa2 a la botella, mm:", round(doc.Placa2.Shape.distToShape(botella)[0], 2))
print("Dientes superpuestos, mm3:", round(doc.EngranajeZ1.Shape.common(doc.EngranajeZ2.Shape).Volume, 3))
print("Holgura entre dientes, mm:", round(doc.EngranajeZ1.Shape.distToShape(doc.EngranajeZ2.Shape)[0], 3))
print("Diámetro exterior Z1, mm:", round(doc.EngranajeZ1.Shape.BoundBox.YLength, 1))
print("Diámetro exterior Z2, mm:", round(doc.EngranajeZ2.Shape.BoundBox.YLength, 1))
posar(45)
print("Husillo fuera de la base, mm:", doc.Husillo.Mesh.BoundBox.XMax - doc.Base.Shape.BoundBox.XMax)
print("Carro a la tuerca, mm:", round(doc.Carro.Shape.distToShape(doc.Tuerca.Shape)[0], 2))
posar(0)

```

| Línea | Resultado | Qué significa |
|---|---|---|
| Manivela dentro de la botella | 282 830 | Hallazgo 2.1: del lado del cuerpo no entra |
| Placa2 a la botella | 1,32 | Hallazgo 2.2: pasa muy justa. Es la distancia mínima entre los sólidos |
| Dientes superpuestos | 0 | Hallazgo 2.3: engranan sin pisarse |
| Holgura entre dientes | 0,155 | Es la holgura en esta posición, no un valor de diseño |
| Diámetro exterior Z1 | 44 | `m·(z + 2)` = 2·(20 + 2) |
| Diámetro exterior Z2 | 83,8 | Nominal 84; la caja mide un poco menos según cómo cae el dentado |
| Husillo fuera de la base | 158 | Hallazgo 2.5 |
| Carro a la tuerca | 6 | La holgura definida en `HOLGURA_TUERCA` |

**Dos métodos que ya estás usando:**

- `A.common(B).Volume` es el volumen compartido por dos sólidos. Si da más que cero, chocan.
- `A.distToShape(B)[0]` es la distancia mínima entre dos sólidos.

Si querés, reemplazá los nombres para probar otros pares, siempre con sólidos, no con mallas.

**Qué no prueba esto:** es solo geometría. No dice nada de fuerzas, fricción ni calidad del corte; eso lo responde el prototipo. Y casi todas las medidas son supuestos: en `parametros.py` cada una indica su origen.

## 9. Abrir el STEP

Es lo que recibió el grupo. Con **File → Open** elegí `salida/cortadora_pet.step`. Si aparece una ventana de opciones de importación, aceptá los valores por defecto.

Deberías ver un contenedor con **22 piezas**, ya sin las marcas: `Guias_1`, `Guias_2`, `Collares_1`, `Collares_2`, `Botella` y `Husillo` como sólidos. Probá la barra espaciadora en algunas para confirmar que son independientes.

Esto confirma que el archivo trae las piezas separadas, pero no reemplaza una prueba en SolidWorks, que importa el STEP a su manera.

## 10. Errores comunes

| Qué pasa | Qué hacer |
|---|---|
| La máquina desapareció de la vista | `V`, `F` |
| Rotar no funciona | Revisá el estilo de navegación, abajo a la derecha, en la barra de estado: debe ser **CAD** |
| No encuentro **Measure** | Está en **Tools**. Revisá que estés en el workbench **Part** |
| `NameError: name 'posar' is not defined` | Falta pegar el bloque de la sección 7. Si cerraste FreeCAD, hay que pegarlo otra vez |
| `AttributeError` sobre `doc` | Hacé clic en la ventana del `.FCStd` y volvé a pegar el bloque: `doc` toma el documento activo |
| `ModuleNotFoundError: parametros` | Otra ruta: corregí el `sys.path.insert` del bloque |
| Preguntó si guardar al cerrar | Respondé que no: moviste piezas, pero el modelo no cambió |
| Guardé sin querer | `git restore modelo/cortadora_pet.FCStd`, desde `06_modelo_3d` |
| Cambié una medida y no quedó | El `.FCStd` no manda: se edita `parametros.py` y se corre `make` |

## 11. Cómo seguir

```
Revisar este modelo (esta guía)
          |
          v
Aprender a modelar: ~/FreeCAD/GUIA_FreeCAD_Sistema_Rotor.md
lecciones 1 a 7, con macros que podés leer y cambiar
(esa guía nombra los menús en español)
          |
          v
Cambiar una medida en parametros.py y correr make
(si genera un choque, make falla y resultados.json dice dónde)
          |
          v
Armar la cadena con restricciones reales (workbench Assembly):
todavía sin guía ni prueba en este proyecto
```

Para ver qué archivos cambió `make` y deshacer la prueba de una medida, desde `06_modelo_3d`:

```bash
git status --short .
git restore .
```

Ojo: `git restore .` descarta **todos** los cambios sin commit de esa carpeta. Miralos antes con `git status`.

**Práctica recomendada para empezar:** en **Edit → Preferences → Python → Macro**, activá *Show script commands in python console*. Desde ahí, cada clic muestra el Python equivalente en la consola. Es la forma más rápida de aprender cómo está hecho todo.

---
*Fuentes: [hallazgos.md](hallazgos.md), [parametros.py](parametros.py), [piezas.py](piezas.py), `modelo/cortadora_pet.FCStd`, `salida/cortadora_pet.step` y `~/FreeCAD/GUIA_FreeCAD_Sistema_Rotor.md` (secciones 2 y 3). Nombres de menús leídos de FreeCAD 1.1.3 en inglés.*
