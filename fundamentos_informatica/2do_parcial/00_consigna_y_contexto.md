# 2do parcial — Programa en C++

Docente: **Ing. Rubén Morales**, Fundamentos de Informática, Dpto. de Mecánica.

## 1. Consigna

- **Entrega:** hasta el **20/nov/2026, 23:59 h**.
- **Qué se entrega:** un programa en C++ **que funcione**. Se sube **solo el `.cpp`** a la nube propia y se comparte con el docente; el `.exe` no se comparte.
- **Obligatorio:** no se promedia con otras notas. Si no se entrega, queda **ausente**. Hay que verificar estar inscripto en el SIU, porque si no el docente no tiene dónde cargar la nota.
- **Corrección:** el docente baja cada trabajo (unos 250) y lo hace funcionar en su máquina. Si no compila, no hay garantía de devolución en un plazo razonable.
- **Control de copia:** todas las entregas se pasan por IA. Si dos proyectos son "gemelos", **se anulan los dos**. Lo que se compara es el **código**, no el tema: basarse en un final modelo es justamente lo que pide la consigna. El riesgo está en que muchos resuelvan el mismo final con IA y les salga un código parecido. Por eso el programa toma decisiones propias y coherentes (nombres de vectores y variables, orden de las etapas, mensajes, extensiones) en vez de la solución más obvia.

### Contenido exigido

- Tiene que haber una **base de datos**, más simple o más compleja.
- Base posible: los **finales N.º 2, 3, 4 y 5** (sección 3), con **ordenamiento** o **búsqueda secuencial o binaria** agregados una vez cargada la base.
- Alternativa: una **base de datos inventada**, con control de stock, actualización de valores, etc. **La nota depende de la complejidad.**

### Formato exigido

En la **línea 1** van todos los datos, **sin excepciones**. En la línea 2, un comentario que explique qué hace el programa. Comentarios `//` a lo largo del código marcan cada etapa:

```cpp
/* Sergio Paredes - Legajo 260.861-3 - Comision S1554 - Sede: Campus - Horario: Jue 18:15 a 21:30 */
/* Este programa sirve para ............................. */
...
// en esta linea comienza el proceso de ordenamiento
```

> Ojo: en el modelo del docente los comentarios `/*` no están cerrados. En C++, un `/*` sin su `*/` convierte en comentario todo lo que sigue y el programa no compila. Hay que cerrar cada uno con `*/`, o usar `//` en cada línea.

La sede es **Campus**, aunque el modelo del docente diga "Sede: Medrano".

### Decisiones sobre los datos

- **"Base de datos" = vectores paralelos en memoria:** un vector por campo, como en el apunte. No se usa un motor de base de datos.
- **Base inicial (maestro) dentro del `.cpp`:** va en un bloque separado y comentado al principio, con una constante para la cantidad de registros (15-20, no los 500 del enunciado). Como se entrega solo el `.cpp`, un archivo externo podría no llegar, o no encontrarse desde donde Dev-C++ ejecute el `.exe`. **No se leen archivos.**
- **Novedades por teclado** (ventas, pedidos, movimientos): se ingresan durante la ejecución, con la clave de fin de lote del enunciado o con un menú, para que el docente lo pruebe en vivo.
- **Objetivo de nota:** uno de los finales 2-5 como base, extendido con al menos **ordenamiento** (y listado ordenado) más **búsqueda binaria** sobre la base ordenada. Se suma lo que aumente la complejidad sin complicarlo de más: control de stock, actualización de precios, validación de entradas.
- **Código:** C++98 estricto, `make` sin warnings. Solo lo que cubren los tutoriales y el apunte (vectores paralelos, `for`/`while`, `if`, cadenas), sin structs ni clases. Tiene que ser legible para alguien que programa en C++ por primera vez.

## 2. Compilador

| | Versión | Compilador interno | Origen |
|---|---|---|---|
| Link original del docente | Dev-C++ 4.9.9.2 (2005) | GCC 3.4.2 | SourceForge |
| Alternativa del docente | Dev-C++ 5.5.3 (2013) | TDM-GCC 4.7.1 x64 | `fuentes/Dev-Cpp 5.5.3 TDM-GCC x64 4.7.1 Setup.rar` |
| Local (Linux) | g++ 15.2 | — | ya instalado |

Ambas versiones del docente son viejas: corren sobre Windows y, por defecto, compilan **C++98**. Como no se sabe con cuál va a probar los trabajos, el programa se escribe en **C++98**, para que compile en cualquiera de las dos:

- Nada de C++11 en adelante: ni `auto`, ni `for (x : v)`, ni `nullptr`, ni `std::to_string`, ni `#include <bits/stdc++.h>`.
- Sin tildes ni `ñ` en los textos que se muestran: la consola de Windows los muestra como basura.
- La pausa al final (`system("pause")` solo existe en Windows) se decide más adelante.

Prueba local: `make` en esta carpeta compila cada `.cpp` con `g++ -std=c++98 -pedantic -Wall -Wextra` y deja el ejecutable en `build/`. Así se detecta cualquier cosa que el compilador viejo rechazaría.

### Tutoriales del docente (YouTube)

| Parte | Tema | Link |
|---|---|---|
| 1 | Tipos de datos, entrada y salida | https://youtu.be/8_Gy5UMkFZY |
| 2 | Ciclos y bucles | https://youtu.be/4RfJ7vApTmA |
| 3 | Vectores, arreglos y matrices | https://youtu.be/RQmutaFB-LM |
| 4 | Cadenas de caracteres | https://youtu.be/JRBhYjtFpck |
| 5 | Ordenamiento | https://youtu.be/mj0p5JWZ2PQ |
| 6 | Búsqueda secuencial y binaria | https://youtu.be/d6k995ZWTAA |

## 3. Finales modelo (transcriptos de `fuentes/final_*.jpg`)

El docente propone como base los finales 2 a 5. El 1 vino en el mismo paquete, pero no lo nombra.

### Final 1 — Empresa de colectivos

100 unidades, 1 día de servicio. Un registro por cada venta de pasaje: **número de interno** (1 a 100), **importe del boleto** (unitario, real), **cantidad de pasajes** (entero). Fin de datos: interno = 0.
Informar:
1. Por cada unidad, número de interno e importe total recaudado.
2. Número de interno con la mayor recaudación.
3. Listado de unidades que no salieron al recorrido.

### Final 2 — Banco, cajas de ahorro

5000 clientes, cada uno con un registro inicial: **número de cuenta**, **nombre y apellido**, **saldo** (ej. `510258  Alberto PEREZ  1.500`). Después llegan registros de movimiento: **número de cuenta**, **movimiento** (1 depósito, 2 extracción), **importe**, **fecha** (ej. `4235167  2  100  12/05/05`). Fin de datos: cuenta = 0.
Informar:
1. Al final, listado de cuentas con cantidad de operaciones y saldo.
2. Cuentas sin movimientos en el período.
3. Nombre y apellido del cliente con la mayor extracción, y la fecha en que la hizo.

### Final 3 — Farmacia

500 medicamentos en depósito: **código**, **nombre genérico**, **precio unitario**, **cantidad en stock**. Cada venta genera un registro: **nombre genérico**, **cantidad**, **obra social** (1 a 20). Fin de datos: nombre genérico = `PPPPPPP`.
Informar:
1. Por cada venta, nombre del medicamento e importe total. Solo se vende si hay stock suficiente para el total pedido; si no, se informa el nombre y la leyenda "sin existencia".
2. Al final, medicamentos que quedaron con existencia nula.
3. Importe total abonado por cada obra social.

### Final 4 — Empresa de turismo (04/11/2004)

10 agencias (1 a 10). 200 vuelos: **código de vuelo**, **capacidad**, **importe unitario** (ej. `LUV-123  250  450`). Cada pedido: **apellido y nombre**, **vuelo solicitado**, **cantidad de pasajes**, **número de agencia** (ej. `Julian RUIZ  LUV-478  3  7`). Fin de datos: agencia = 00.
Informar:
- A) Listado de solicitudes con su resultado: apellido y nombre, Aceptado/Rechazado, importe.
- B) Códigos de vuelo que completaron su capacidad.
- C) Recaudación por ventas de cada agencia.

### Final 5 — Autopartista

1000 componentes: **código**, **cantidad en stock**, **precio unitario**. Cada pedido de un día: **código de cliente**, **código de componente**, **descripción**, **cantidad**. Un cliente puede hacer varios pedidos, y el sistema los ordena automáticamente agrupados por cliente. Fin de datos: campos en `000000` o "blanco".
Informar:
1. Por cada cliente, el remito: código de cliente; por renglón, componente, descripción, cantidad y precio total; al pie, importe total del pedido.
2. Importe total de compra por cada artículo.
3. Código del cliente con el pedido de mayor importe total.

### Patrón común

Todos tienen la misma forma, que es la que pide la consigna:

1. **Carga de la base:** un vector por campo, con cantidad conocida → `for`.
2. **Proceso de novedades** (ventas, movimientos, pedidos): cantidad desconocida y clave de fin de lote → `while`. Cada novedad se **busca** en la base (secuencial o binaria), se valida (stock, capacidad, saldo) y se **actualiza**.
3. **Informes** al final, con acumuladores y máximos. El **ordenamiento** se agrega para listar o para habilitar la búsqueda binaria.

## 4. Apunte manuscrito "Vectores / Arrays / Arreglos" (`fuentes/apunte_vectores_1..5.jpg`)

| Hoja | Contenido |
|---|---|
| 1 | Qué es un vector: variable del usuario, en memoria, todos los elementos del mismo tipo. Declaración: `int PACO[100]`, `float LOLA[100]`, `char ESCANEO[100]`. Carga de 100 enteros con `for`. |
| 2 | Inicialización `int VALORES[] = {0}`. Guardar con un índice (`q`) e informar con otro (`p`) es válido. La memoria como una escalera de celdas consecutivas. |
| 3 | Cantidad desconocida: `while (valor <> 5)` con clave de fin de lote, a lo sumo 650 datos, contador `cont` como índice de carga. Después de `DATOS[cont]` empieza una "zona desconocida" de la memoria. |
| 4 | Búsqueda secuencial recorriendo todo el vector, con bandera `encontrado` e `indice`. Conclusión: nunca pisar la variable que guarda el tamaño (`cont`). |
| 5 | Búsqueda secuencial que se detiene al encontrar: `while (DATOS[i] <> X && i <= cont)`. Para dos razones: lo encontró, o se pasó del final del vector. |

### Detalles a tener en cuenta al pasar el apunte a C++

- **Índices desde 1:** el apunte recorre `1..100`, pero en C++ un vector `int V[100]` va de `V[0]` a `V[99]`. Para usar `1..100`, hay que declararlo `V[101]` y dejar `V[0]` sin usar.
- **`int VALORES[] = {0}`** sin tamaño crea un vector de **un solo** elemento. Lo correcto es `int VALORES[101] = {0}`.
- **`<>`** es "distinto" del pseudocódigo. En C++ se escribe `!=`.
- **Hoja 3:** `for (m = 1; m <= cont; cont++)` incrementa `cont` en vez de `m`. En C++ el ciclo no termina nunca: debe ser `m++`.
- **Hoja 5:** la condición `DATOS[i] != X && i <= cont` lee `DATOS[i]` antes de comprobar que `i` esté dentro del vector. Se invierte el orden, `i <= cont && DATOS[i] != X`, y C++ ya no evalúa la segunda parte cuando la primera es falsa.

<!-- solo-md -->
---
**Fuentes:** correo del Ing. Rubén Morales con la consigna del 2do parcial (pegado por el usuario el 09/nov/2026); fotos de los finales modelo 1-5 y del apunte manuscrito en `fuentes/`; instalador `Dev-Cpp 5.5.3 TDM-GCC x64 4.7.1 Setup.rar` (link de Google Drive del docente).
<!-- /solo-md -->
