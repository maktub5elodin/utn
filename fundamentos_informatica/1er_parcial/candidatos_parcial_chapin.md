# Candidatos para el TP/parcial — Fundamentos de Informática (Ing. Alaniz)

> Transcripción de los problemas 12 a 16 de la guía, marcados por el profesor como de dificultad aceptable para el parcial, más un análisis de cuál conviene preparar primero y por qué.

---

## Problema 12

Se tiene un conjunto de registros, cada uno correspondiente a una venta realizada en el día en un negocio de ferretería. Determinar la cantidad de ventas realizadas cuyos montos superen los $20 y sean menores de $30, las comprendidas entre $50 y $70, y aquellas que superan los $100.

Para indicar fin del proceso se coloca un registro cuyo importe es $0,00.

**Estructura implícita:** lectura centinela (`Mientras importe ≠ 0`), tres contadores independientes, cada venta se clasifica contra tres rangos mutuamente excluyentes mediante `Si` en cascada (o tres `Si` independientes, a evaluar).

---

## Problema 13

Una empresa desea realizar la selección de personal para cada uno de los puestos publicados, de referencia:

- **(IM/100) (3)** — Ingeniero Mecánico, Masculino, edad entre 25 y 30 años, con experiencia.
- **(A/200) (2)** — Arquitecto/a, edad entre 25 y 30 años.
- **(TM/300) (5)** — Técnico matricero, edad entre 20 y 30 años.

Por cada postulante se realiza un registro con: Apellido y Nombre, Cargo, Sexo, Edad, Condición (1 = con experiencia, 2 = sin experiencia). Ejemplo: `José Sarralde, TM/2300, F/M, ¿?, 1/2`.

Fin de registros: `Apellido y Nombre = "ZZZZ ZZZZZ"`.

El algoritmo debe informar, por cada referencia, cosas distintas:

1. **IM/100:** a) si se cubren los cargos solicitados, b) cuántos postulantes se presentaron, c) cuántos cumplen la condición solicitada.
2. **A/200:** a) cuántos hombres y mujeres se presentaron en general, b) si se cubren los cargos solicitados.
3. **TM/300:** a) cuántos postulantes en condiciones se presentaron.

> Nota: en su resolución del pizarrón, el punto 2a lo resuelve como "cuántos se presentaron en general" (un solo contador total), sin separar por hombres y mujeres como sugiere la letra del enunciado — probablemente una simplificación propia al dictarlo en clase. Conviene replicar lo que él mostró (un contador total) antes que la lectura literal del enunciado.

**Estructura implícita:** lectura centinela + filtrado por cargo (comparación de texto) combinado con rangos de edad y sexo — tres bloques de criterios distintos corriendo en paralelo dentro del mismo bucle.

> ⚠️ **El profesor ya resolvió este problema en el pizarrón** (ver sección siguiente). Esto lo saca de la lista de "riesgosos" y lo pone como uno de los candidatos más probables — si ya lo armó en clase con este nivel de detalle, es una señal fuerte de que es justamente el tipo de ejercicio que quiere ver resuelto en el parcial.

### Resolución del profesor (transcripta del pizarrón)

```
contIM/100 <- 0 ; contA/200 <- 0 ; contTM/300 <- 0
Leer ApyN
Mientras (ApyN <> "ZZZZ ZZZZZ")
  Leer cargo, sexo, edad, cond
  Si cargo == "IM/100"
    V:
      contIM/100++
      Si sexo == "M"
        V:
          Si 25<=edad<=30
            V:
              Si cond==1
                V: cumpleIM/100++
                F: (nada)
            F: (nada)
        F: (nada)
    F:
      Si cargo == "A/200"
        V:
          contA/200++
          Si 25<=edad<=30
            V: cumpleA/200++
            F: (nada)
        F:
          Si cargo == "TM/300"
            V:
              contTM/300++
              Si 20<=edad<=30
                V: cumpleTM/300++
                F: (nada)
            F: (no corresponde a ninguna referencia, se descarta)
  Leer ApyN
Informar "Por IM/100 se presentaron en general:", contIM/100, ", cumplen la condición IM/100:", cumpleIM/100
Si cumpleIM/100 >= 3
  V: Informar "Se cubren los cargos IM/100"
  F: (nada)
Informar "Por el cargo A/200 se presentaron en general:", contA/200
Si cumpleA/200 >= 2
  V: Informar "Se cubren los cargos A/200"
  F: (nada)
Informar "Se presentaron en condiciones por el cargo TM/300:", cumpleTM/300
```

**Mapeo confirmado inciso por inciso** (así lo marcó el propio profesor con círculos numerados sobre su diagrama):

| Inciso del enunciado | Line del diagrama que lo resuelve |
|---|---|
| 1a) ¿Se cubren los cargos IM/100? | El `Si cumpleIM/100 >= 3` → informa "Se cubren los cargos IM/100" |
| 1b) ¿Cuántos postulantes se presentaron? | `contIM/100` dentro del primer `Informar` posterior al bucle |
| 1c) ¿Cuántos cumplen la condición? | `cumpleIM/100` en ese mismo `Informar` |
| 2a) ¿Cuántos se presentaron en general (A/200)? | `contA/200` en el `Informar` correspondiente |
| 2b) ¿Se cubren los cargos A/200? | El `Si cumpleA/200 >= 2` → informa "Se cubren los cargos A/200" |
| 3) ¿Cuántos postulantes en condiciones (TM/300)? | `cumpleTM/300` en el último `Informar` |

Los umbrales `>= 3` y `>= 2` no son arbitrarios: son exactamente los cupos que pide cada referencia en el enunciado — `(IM/100) (3)` y `(A/200) (2)`. Para TM/300 no hay un `Si` de "se cubren los cargos" porque el enunciado no lo pide (el punto 3 solo pregunta la cantidad, no si se cubre el cupo de 5).

**Lo importante de cómo lo arma:**

- Usa `contIM/100`, `contA/200`, `contTM/300` para "cuántos postulantes se presentaron" por referencia (la respuesta b/a de cada punto), y variables separadas `cumpleIM/100`, `cumpleA/200`, `cumpleTM/300` para "cuántos cumplen la condición" — dos contadores por referencia, no uno solo.
- La clasificación por `cargo` es un **`Si/Sino-Si/Sino-Si` en cascada de tres niveles** (si no es IM/100, pregunta si es A/200; si tampoco, pregunta si es TM/300) — a diferencia del positivo/negativo/cero del problema 7, acá **sí** anida porque un postulante solo puede corresponder a un cargo a la vez (son mutuamente excluyentes).
- Dentro de cada rama de cargo, **descompone la condición compuesta en varios `Si` anidados, uno por cada criterio simple** (primero sexo, después edad, después condición), en vez de escribir una sola condición con "Y" lógico. Cada caja de selección evalúa una sola comparación.
- Las ramas `F` de los niveles internos (sexo, edad, condición) quedan vacías — si el postulante no cumple algún filtro, simplemente no incrementa el contador de "cumple" y el flujo sigue de largo.
- **Detalle de nombres a tener en cuenta:** en la inicialización y en el cuerpo del bucle usa `contIM/100`, `contA/200`, `contTM/300`; en algún punto de los `Informar` finales se lo ve escribir `contgralIM/100` / `contgralA/200` en vez de repetir el mismo nombre — es casi seguro el mismo lapsus de "cambiar de nombre a mitad de camino" que ya vimos con `tmin`/`mmin` en el problema de temperatura.

### Complemento: resolución de un compañero (Francisco Sticotti)

Un compañero resolvió el mismo problema 13 con letra mucho más legible, siguiendo el mismo esqueleto que el profesor (misma cascada de tres niveles, misma selección anidada por criterio, mismos umbrales `>=3` y `>=2`). No cambia la estructura, pero **aclara tres puntos que en la foto del pizarrón habían quedado ambiguos o incompletos:**

1. **TM/300 lleva un solo contador, no dos.** El enunciado solo pide "cuántos postulantes en condiciones se presentaron" (un único número) — no hace falta un contador de "presentados en general" para esa referencia, solo el que suma cuando se cumple el rango de edad.
2. **Las ramas `F` de los `Si` de umbral también informan.** "¿Se cubren los cargos?" es una pregunta de sí/no — así que conviene informar el resultado negativo también (`"No se cubren los cargos solicitados de IM/100"`), no dejar la rama F vacía como en la transcripción original del pizarrón.
3. **Maneja el cargo inválido con un mensaje explícito.** Si el `cargo` leído no coincide con ninguna de las tres referencias, informa `"Error de tipeo"` en vez de descartarlo en silencio — una interpretación razonable aunque el enunciado no lo pida de forma explícita.

Además usa una nomenclatura más sistemática: `CONTGI`/`CONTAI` (cuenta general / cuenta aprobados de IM/100), `CONTGA`/`CONTAA` (ídem A/200), `CONTATM` (único contador de TM/300) — evita del todo la ambigüedad `cont` vs. `contgral` que tenía la versión del pizarrón.

### Versión recomendada (incorporando las tres correcciones)

```
CONTGI <- 0 ; CONTAI <- 0
CONTGA <- 0 ; CONTAA <- 0
CONTATM <- 0
Leer ApyN
Mientras (ApyN <> "ZZZZ ZZZZZ")
  Leer cargo, sexo, edad, cond
  Si cargo == "IM/100"
    V:
      CONTGI++
      Si sexo == "M"
        V:
          Si 25<=edad<=30
            V:
              Si cond==1
                V: CONTAI++
                F: (nada)
            F: (nada)
        F: (nada)
    F:
      Si cargo == "A/200"
        V:
          CONTGA++
          Si 25<=edad<=30
            V: CONTAA++
            F: (nada)
        F:
          Si cargo == "TM/300"
            V:
              Si 20<=edad<=30
                V: CONTATM++
                F: (nada)
            F: Informar "Error de tipeo: el cargo ingresado no corresponde a ninguna referencia"
  Leer ApyN
Informar "Se presentaron:", CONTGI, "postulantes para IM/100, de los cuales", CONTAI, "cumplen las condiciones"
Si CONTAI >= 3
  V: Informar "Se cubren los cargos solicitados de IM/100"
  F: Informar "No se cubren los cargos solicitados de IM/100"
Informar "Se presentaron:", CONTGA, "postulantes para el cargo A/200"
Si CONTAA >= 2
  V: Informar "Se cubren los cargos solicitados de A/200"
  F: Informar "No se cubren los cargos solicitados de A/200"
Informar "Los aspirantes en condiciones para TM/300 son:", CONTATM
```

---

## Problema 14

Se desea procesar los pedidos de piezas realizadas a un depósito de repuestos.

Por cada pieza se dispone de un lote de registro donde el primero indica **Código de pieza y Cantidad en existencia** (ej.: `PLO231, 500`). A continuación se disponen los pedidos: **Código de pieza y Cantidad solicitada** (ej.: `PLO231, 50`). Por cada pieza distinta se genera un ordenamiento similar (existencia + sus pedidos).

Fin del conjunto: se ingresa un registro con código de pieza igual a cero.

El algoritmo debe determinar, por cada pieza solicitada, si hay existencia o no para satisfacer las solicitudes.

**Estructura implícita:** requiere correlacionar dos tipos de registro distintos (existencia vs. pedidos) agrupados por pieza — más cercano a un *quiebre de control* de dos niveles que a lo que el profesor mostró en pizarrón hasta ahora.

---

## Problema 15

Se quiere procesar los registros de lluvias correspondientes al año 2000. Los registros contienen: **Mes, Día, Registro de lluvia** (ej.: `Enero, 4, 1`). Si no hubo lluvia en un día, el valor de registro de lluvia es cero. Los registros están agrupados por mes.

Fin de registros: `Mes = "ZZZZ"`.

El algoritmo debe informar:

1. Promedio de lluvias por mes.
2. Cantidad de días sin lluvia en cada mes.
3. Mes con mayor promedio de lluvias.
4. Cantidad de días con lluvia durante los meses de julio y agosto.

**Estructura implícita:** lectura centinela agrupada por mes (control break simple, un solo nivel), acumuladores de suma/cantidad para promedio, contador de días sin lluvia, comparación acumulativa para detectar el máximo, y un contador condicionado a julio/agosto.

---

## Problema 16

Por cada venta realizada en un supermercado se realiza un registro con: **Artículo, Cantidad, Unidades, Precio unitario, Rubro** (1 = Bebidas con alcohol, 2 = Bebidas sin alcohol, 3 = Carnes rojas, 4 = Lácteos).

Fin de registros: `Artículo = "Nafta"`.

El algoritmo debe informar:

1. Cantidad total de ventas realizadas por rubro (total 4).

**Estructura implícita:** lectura centinela + clasificación en una de 4 categorías mutuamente excluyentes (equivalente a extender la lógica de "positivos/negativos/ceros" del problema 7 a 4 ramas).

---

## ¿Cuál conviene preparar como candidato principal?

**El problema 13 es EL candidato — ya no hay que adivinar nada.** Con las últimas dos fotos, la resolución del profesor quedó completa de punta a punta: desde la inicialización, pasando por la cascada de clasificación por cargo, hasta los seis `Informar`/`Si` finales — y él mismo marcó con círculos numerados (1a, 1b, 1c, 2a, 2b, 3) qué línea del diagrama contesta cada inciso exacto del enunciado. Preparar este ejercicio ya no es "aplicar el estilo que él prefiere" — es directamente reproducir la solución que mostró en clase, con los nombres de variable, los umbrales (`>=3`, `>=2`) y el orden que él mismo usó.

Prioridad de estudio:

1. **Problema 13** — memorizar y poder reproducir esta resolución completa es la apuesta más segura de toda la guía.
2. **Problema 15 (lluvias)** — como plan B: cubre el otro patrón fuerte que sabemos que él enseña (agrupamiento + acumuladores + seguimiento de un extremo, visto en el ejemplo de temperatura), por si el parcial pide algo estructuralmente distinto al 13.
3. **Problema 16 (supermercado)** — as bajo la manga si el tiempo apremia: incorpora la cascada `Si/Sino-Si` de 4 ramas, la misma lógica que el 13 pero sin los niveles anidados de sexo/edad/condición.
4. **Problema 12** — buena práctica adicional aplicando la misma cascada de rangos mutuamente excluyentes.
5. **Problema 14** — el único que sigue sin evidencia de cómo lo resolvería el profesor (correlación entre dos tipos de registro); dejarlo para el final si sobra tiempo.

---

## Notas sobre el estilo y la metodología del profesor

Esto es lo que se puede inferir de sus propias resoluciones en el pizarrón, para alinear cualquier diagrama a lo que él espera ver:

- **Todo vive en un único rectángulo grande** (diagrama de Chapin / Nassi-Shneiderman): sin flechas, sin GOTO, lectura de arriba hacia abajo, subdivisión en cajas anidadas.
- **Tres estructuras únicamente:** secuencia (filas apiladas), selección (`Si` dibujado como un pico con V a la izquierda y F a la derecha, condición arriba), iteración (`Para`/`Mientras` con una franja de encabezado y el cuerpo anidado debajo).
- **Elige `For` cuando el enunciado da un rango fijo** (`Para hora=0 hasta 23`, `Para min=0 hasta 59`) y **`While` con centinela cuando el enunciado dice "hasta ingresar un registro cuyo valor es X"** — como en casi todos estos problemas (12 a 16), todos tienen centinela explícito, así que el patrón esperable es `While` con lectura previa al bucle.
- **Inicializa todos los acumuladores/contadores en una sola línea antes del bucle**, agrupados con comas (`SUMPOS=0, PRODNEG=1, CANTCEROS=0` / `TMAX=-100, tmin=100`).
- **La regla para elegir entre `Si` en paralelo o `Si/Sino-Si` en cascada depende de si las categorías son mutuamente excluyentes por naturaleza:** cuando un mismo registro puede activar más de una actualización de forma independiente (una temperatura puede ser candidata a mínima sin dejar de evaluarse como candidata a máxima), usa selecciones paralelas. Cuando el registro solo puede pertenecer a **una** categoría de un conjunto cerrado (un postulante solo tiene un cargo; una venta solo tiene un rubro), usa cascada `Si/Sino-Si/Sino-Si...` — así resolvió el problema 13 con los tres cargos, y es de esperar el mismo criterio para el 12 (rangos de importe) y el 16 (rubros).
- **Descompone las condiciones compuestas (con "Y" lógico) en varios `Si` anidados, uno por cada criterio simple**, en vez de escribir una sola condición combinada. Se ve claramente en el problema 13: primero pregunta el cargo, después el sexo, después el rango de edad, después la condición — cuatro cajas de selección en cascada en vez de una sola con cuatro comparaciones unidas por "Y".
- **Convención de nombres:** minúsculas para variables auxiliares de comparación dentro del bucle (`num`, `temp`, `tmin`), mayúsculas para los acumuladores/resultados finales que se informan (`SUMPOS`, `PRODNEG`, `TMAX`, `HMAX`, `MMAX`). Vale la pena mantener esa distinción visual en cualquier diagrama que se le entregue.
- **Usa `<-` para asignación**, no `=`, dentro del cuerpo del algoritmo (reserva `=` para las inicializaciones iniciales en algunos casos, pero no es estricto).
- **Los `Informar` van todos juntos al final**, fuera de cualquier bucle, y suelen incluir texto literal entre comillas intercalado con las variables en una sola instrucción por línea de salida.
- **Marca el alcance de bucles anidados con flechas verticales a la izquierda del diagrama**, una por cada nivel de anidamiento — es un refuerzo visual personal que no es parte estricta de la notación de Chapin, pero conviene replicarlo porque es lo que él dibuja y lo que reconoce de un vistazo al corregir.

### Requisitos administrativos del TP (de la pizarra, no del algoritmo)

1. Un ejercicio en papel, en letra clara, con diagramación estructurada.
2. Datos del alumno en el ángulo superior derecho de la hoja.
3. Subir a una nube.
4. Compartir a `amadeoruben@yahoo.com.ar`.
