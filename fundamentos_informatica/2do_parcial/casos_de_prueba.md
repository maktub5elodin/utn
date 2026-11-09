# Casos de prueba — `farmacia.cpp`

## Cómo correrlo en Windows

Así lo va a probar el docente. Conviene hacerlo al menos una vez antes de entregar. Hay dos formas: con PowerShell (opción A), que comprueba, descarga, instala, compila y ejecuta, o a mano desde Dev-C++ (opción B).

### Opción A — PowerShell

Abrir **Windows PowerShell** y pegar los bloques **en orden, en la misma ventana**: cada bloque usa variables del anterior.

> [!NOTE]
> **Por qué la comprobación está armada así:** el objetivo es compilar con el mismo compilador que va a usar el docente, no con cualquiera. Por eso el paso 1 busca primero las instalaciones de **Dev-C++**: la 4.9.9.2 de su link original y la 5.x del `.rar` que compartió. Solo si no encuentra ninguna acepta otro `g++` que esté en el PATH, y en ese caso avisa que no es el entorno del profesor. Si no hay ningún compilador, el paso 2 instala **el mismo Dev-C++ 5.5.3 que compartió el docente**, bajado de su link de Google Drive y verificado contra el archivo original. La compilación usa `-std=c++98`, el estándar con el que compilan esos Dev-C++.

**Paso 0 — Carpeta de trabajo.** Usa una ruta corta y sin espacios, porque los Dev-C++ viejos fallan con espacios o tildes en la ruta.

```powershell
$dir = 'C:\farmacia'
New-Item -ItemType Directory -Force $dir | Out-Null
Set-Location $dir
$ProgressPreference = 'SilentlyContinue'      # sin esto, las descargas en PowerShell 5.1 son muy lentas
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
```

**Paso 1 — Comprobación: ¿ya hay con qué compilar?**

```powershell
$gpp = $null
$candidatos = @(
    'C:\Dev-Cpp\bin\g++.exe',                               # Dev-C++ 4.9.9.2 (link original del docente)
    'C:\Program Files (x86)\Dev-Cpp\MinGW64\bin\g++.exe',   # Dev-C++ 5.x de 64 bits (el .rar del docente)
    'C:\Program Files (x86)\Dev-Cpp\MinGW32\bin\g++.exe',   # Dev-C++ 5.x de 32 bits
    'C:\Program Files\Dev-Cpp\MinGW64\bin\g++.exe',
    'C:\Program Files\Dev-Cpp\MinGW32\bin\g++.exe'
)
$gpp = $candidatos | Where-Object { Test-Path $_ } | Select-Object -First 1
if ($gpp) {
    "OK: Dev-C++ encontrado -> $gpp  (mismo entorno que el docente)"
} else {
    $otro = Get-Command g++ -ErrorAction SilentlyContinue
    if ($otro) {
        $gpp = $otro.Source
        "AVISO: no hay Dev-C++, pero hay otro g++ en el PATH -> $gpp"
        "       Sirve para probar, aunque no es el compilador del docente."
    } else {
        "No hay compilador: hace falta el paso 2 (instalar Dev-C++ 5.5.3)."
    }
}
if ($gpp) { & $gpp --version | Select-Object -First 1 }
```

**Paso 2 — Solo si el paso 1 dijo que no hay compilador: descargar e instalar Dev-C++ 5.5.3.**

```powershell
$rar   = "$dir\Dev-Cpp 5.5.3 TDM-GCC x64 4.7.1 Setup.rar"
$setup = "$dir\Dev-Cpp 5.5.3 TDM-GCC x64 4.7.1 Setup.exe"

# 1) el mismo .rar que compartio el docente en Google Drive (43,7 MB)
Invoke-WebRequest 'https://drive.usercontent.google.com/download?id=1fCsTpvkcOqkju7zYNzRdhlgvbfIPx7PP&export=download&confirm=t' -OutFile $rar

# 2) verificar que es exactamente ese archivo
if ((Get-FileHash $rar -Algorithm SHA256).Hash -ne '91DF7626EBE4E936BBD80129CE7D3471973F1BBA053732F1AC2C31AB177683C8') {
    throw 'El archivo descargado no coincide con el del docente: no instalar.'
}

# 3) descomprimir: tar ya viene en Windows 11; si no puede (Windows 10), probar con 7-Zip
tar -xf $rar -C $dir 2>$null
if (-not (Test-Path $setup) -and (Test-Path 'C:\Program Files\7-Zip\7z.exe')) {
    & 'C:\Program Files\7-Zip\7z.exe' x $rar "-o$dir" -y | Out-Null
}
if (-not (Test-Path $setup)) { throw 'No se pudo descomprimir: abrir el .rar con WinRAR o 7-Zip y seguir desde el punto 4.' }

# 4) instalar en modo silencioso (pide permiso de administrador)
Unblock-File $setup
Start-Process $setup -ArgumentList '/S' -Verb RunAs -Wait
```

Después del paso 2, **volver a correr el paso 1**: tiene que decir `OK: Dev-C++ encontrado`. Si la instalación silenciosa no funcionara, se puede hacer doble clic en `C:\farmacia\Dev-Cpp 5.5.3 TDM-GCC x64 4.7.1 Setup.exe` e instalarlo con las opciones por defecto.

**Paso 3 — Bajar el `.cpp` de la entrega, compilarlo y ejecutarlo.**

```powershell
Invoke-WebRequest 'https://raw.githubusercontent.com/maktub5elodin/utn/main/fundamentos_informatica/2do_parcial/entrega/Paredes_Sergio_S1554.cpp' -OutFile "$dir\Paredes_Sergio_S1554.cpp"

$env:Path = (Split-Path $gpp) + ';' + $env:Path      # las herramientas del compilador quedan a mano
& $gpp -std=c++98 -Wall -static Paredes_Sergio_S1554.cpp -o Paredes_Sergio_S1554.exe
if ($LASTEXITCODE -eq 0) { .\Paredes_Sergio_S1554.exe } else { 'La compilacion fallo: ver los errores de arriba.' }
```

Si compila bien, no muestra nada y arranca el programa en la misma ventana. `-static` mete dentro del `.exe` las bibliotecas que necesita, así se puede ejecutar también fuera de esta ventana.

**Paso 4 — Volver a ejecutar sin compilar (con el `.exe`).**

```powershell
Set-Location C:\farmacia
.\Paredes_Sergio_S1554.exe
```

También funciona con doble clic en `C:\farmacia\Paredes_Sergio_S1554.exe`: la ventana se queda abierta hasta el `Presione ENTER para salir...` final. Recordar que el `.exe` **no se entrega**.

### Opción B — A mano en Dev-C++

1. **Instalar Dev-C++ 5.5.3:** descomprimir `fuentes/Dev-Cpp 5.5.3 TDM-GCC x64 4.7.1 Setup.rar` con 7-Zip o WinRAR, ejecutar el `Setup.exe` y aceptar las opciones por defecto. Al abrirlo por primera vez, pregunta el idioma.
2. **Copiar `farmacia.cpp`** a una carpeta con ruta corta, sin espacios ni tildes, por ejemplo `C:\farmacia\`. Las versiones viejas de Dev-C++ fallan con rutas como `C:\Users\José\Mis documentos\`.
3. **Abrirlo:** *Archivo → Abrir* (*File → Open*) y elegir `farmacia.cpp`.
4. **Compilar y ejecutar:** *Ejecutar → Compilar y Ejecutar* (*Execute → Compile & Run*), o **F11**. En Dev-C++ 4.9.9.2, el que linkea el docente, es **Ctrl+F10**. Se abre una consola negra con el menú.
5. **Si no compila:** los errores aparecen en la pestaña *Compilador* de abajo, con el número de línea. El archivo tal como está compila sin errores ni warnings, así que un error suele indicar que se modificó algo al copiarlo.
6. **Al terminar:** el programa muestra `Presione ENTER para salir...`. En Dev-C++ 5.5.3, después aparece además `Presione una tecla para continuar...`: es del IDE, no del programa.

Detalles de la consola de Windows:

- **Pegar** una entrada copiada de este documento: clic derecho dentro de la consola.
- **Fin de entrada (Caso 8):** `Ctrl+Z` y después `ENTER`.
- **Decimales:** con punto (`5600.50`). La coma se rechaza a propósito (Caso 5).
- Al compilar se genera `farmacia.exe` en la misma carpeta. **No se entrega**: se sube solo el `.cpp`.

## Cómo correrlo en Linux

```bash
make && ./build/farmacia
```

## Casos

Cada caso arranca con el programa **recién abierto** (base inicial sin tocar).

En los bloques de pantalla, lo que se tipea va después de cada `:`. `⏎` es un ENTER solo. El menú, que se repite antes de cada `Opcion:`, no se muestra.

### Caso 1 — Listado ordenado

```
Opcion: 5
LISTADO DE MEDICAMENTOS (orden alfabetico)
POS  CODIGO  MEDICAMENTO           PRECIO   STOCK
1    1111    ACIDO FOLICO         1980.00       3   STOCK CRITICO
2    1104    AMOXICILINA          6750.00      12
3    1118    ATENOLOL             2970.00      16
4    1108    ATORVASTATINA        8920.00      10
5    1115    AZITROMICINA         9850.00       2   STOCK CRITICO
6    1116    BUDESONIDA          11200.00       5   STOCK CRITICO
7    1117    CETIRIZINA           3360.00       4   STOCK CRITICO
8    1113    CLONAZEPAM           5780.00       8
9    1109    DICLOFENAC           2640.00      22
10   1106    ENALAPRIL            3540.75      18
11   1102    IBUPROFENO           2890.50      35
12   1114    LEVOTIROXINA         6230.00      14
13   1105    LORATADINA           3180.00      25
14   1110    LOSARTAN             5310.00      15
15   1107    METFORMINA           4890.00      30
16   1103    OMEPRAZOL            4120.00      20
17   1101    PARACETAMOL          2350.00      40
18   1112    SALBUTAMOL           7450.00       6
```

**Qué verifica:** orden alfabético, que cada medicamento conserve su código, precio y stock después del burbujeo, y la marca de stock crítico (entre 1 y 5 unidades).

### Caso 2 — Consulta: minúsculas, espacios y nombres inválidos

```
Opcion: 2
Nombre del medicamento: ibuprofeno␣            ← con un espacio al final
Codigo: 1102
Nombre: IBUPROFENO
Precio: 2890.50
Stock:  35

Opcion: 2
Nombre del medicamento: acido folico
Codigo: 1111
Nombre: ACIDO FOLICO
Precio: 1980.00
Stock:  3

Opcion: 2
Nombre del medicamento: aspirina
   ASPIRINA: no figura en la base de la farmacia

Opcion: 2
Nombre del medicamento: ABCDEFGHIJABCDEFGHIJABCDEFGHIJABCDEFGHIJ
   Nombre demasiado largo (maximo 29 letras)
```

**Qué verifica:** el paso a mayúsculas, que se recorten los espacios del final, la lectura de nombres con espacio interno (`cin.getline`), el aviso de nombre inexistente y el de nombre de 30 caracteres o más. Este último aparece **sin** el "no figura" a continuación.

### Caso 3 — Lote de ventas e informes finales

```
Opcion: 1
Nombre del medicamento (PPPPPPP para terminar): ibuprofeno
Cantidad: 3
Obra social (1 a 20): 5
   VENDIDO: IBUPROFENO   Importe total: $ 8671.50
Nombre del medicamento (PPPPPPP para terminar): azitromicina
Cantidad: 5
Obra social (1 a 20): 2
   AZITROMICINA: sin existencia
Nombre del medicamento (PPPPPPP para terminar): aspirina
   ASPIRINA: no figura en la base de la farmacia
Nombre del medicamento (PPPPPPP para terminar): Acido Folico
Cantidad: 3
Obra social (1 a 20): 12
   VENDIDO: ACIDO FOLICO   Importe total: $ 5940.00
Nombre del medicamento (PPPPPPP para terminar): ppppppp
--- Lote cerrado: 2 aceptadas, 1 rechazadas, importe del lote $ 14611.50

Opcion: 0

===== INFORMES FINALES =====

Medicamentos con existencia nula:
   1111  ACIDO FOLICO

Medicamentos a reponer (stock 5 o menos):
   1111  ACIDO FOLICO    stock   0
   1115  AZITROMICINA    stock   2
   1116  BUDESONIDA      stock   5
   1117  CETIRIZINA      stock   4

Importe por obra social:
   Obra social  5:  $      8671.50
   Obra social 12:  $      5940.00

Ventas aceptadas:   2
Ventas rechazadas:  1
Recaudacion total:  $ 14611.50

Presione ENTER para salir...⏎
```

**Qué verifica:**
- **Venta aceptada:** 3 × 2890,50 = 8671,50.
- **Sin existencia:** había 2 y se pidieron 5. El stock de AZITROMICINA sigue en 2.
- **Nombre inexistente:** no pide cantidad ni obra social, y no cuenta como rechazada.
- **Venta que deja el stock en 0:** ACIDO FOLICO aparece en "existencia nula" (punto 2 del enunciado).
- **La clave de fin en minúsculas** cierra el lote.
- **Importe por obra social** (punto 3), solo de las que tuvieron ventas.
- **La pausa final.**

### Caso 4 — Validación de números

```
Opcion: abc
   Valor invalido. Ingrese un entero entre 0 y 6: 9
   Valor invalido. Ingrese un entero entre 0 y 6: 1
Nombre del medicamento (PPPPPPP para terminar): ibuprofeno
Cantidad: xyz
   Valor invalido. Ingrese un entero entre 1 y 10000: -3
   Valor invalido. Ingrese un entero entre 1 y 10000: 2.5
   Valor invalido. Ingrese un entero entre 1 y 10000: 12abc
   Valor invalido. Ingrese un entero entre 1 y 10000: 2
Obra social (1 a 20): 25
   Valor invalido. Ingrese un entero entre 1 y 20: 0
   Valor invalido. Ingrese un entero entre 1 y 20: 3
   VENDIDO: IBUPROFENO   Importe total: $ 5781.00
Nombre del medicamento (PPPPPPP para terminar): PPPPPPP
--- Lote cerrado: 1 aceptadas, 0 rechazadas, importe del lote $ 5781.00
```

**Qué verifica:**
- **Letras** donde va un número: no se forma un bucle infinito, gracias al valor inválido explícito en `leerEntero`.
- **Fuera de rango:** opción 9, cantidad -3, obra social 25 y 0.
- **Basura después del número:** `2.5` y `12abc` se rechazan, no se aceptan como 2 y 12.

### Caso 5 — Cambio de precio con coma decimal

```
Opcion: 3
Nombre del medicamento: losartan
Precio actual: $ 5310.00
Precio nuevo: 5600,50
   Valor invalido. Ingrese un numero mayor que 0 y hasta 1000000.00 (use punto para los decimales): 0
   Valor invalido. Ingrese un numero mayor que 0 y hasta 1000000.00 (use punto para los decimales): 5600.50
   LOSARTAN: $ 5310.00 -> $ 5600.50
```

**Qué verifica:** la coma decimal se rechaza (antes se tomaba como 5600 sin avisar), el mensaje pide usar punto, y un precio 0 no es válido.

### Caso 6 — Aumento general de precios

```
Opcion: 6
Porcentaje de aumento (ej. 8.5): 150
   Valor invalido. Ingrese un numero mayor que 0 y hasta 100.00 (use punto para los decimales): 8,5
   Valor invalido. Ingrese un numero mayor que 0 y hasta 100.00 (use punto para los decimales): 10
   Precios aumentados un 10.00 %

LISTADO DE MEDICAMENTOS (orden alfabetico)
POS  CODIGO  MEDICAMENTO           PRECIO   STOCK
1    1111    ACIDO FOLICO         2178.00       3   STOCK CRITICO
...
10   1106    ENALAPRIL            3894.83      18
11   1102    IBUPROFENO           3179.55      35
...
14   1110    LOSARTAN             5841.00      15
```

**Qué verifica:**
- **Tope** del porcentaje (100).
- **Coma rechazada.**
- **Listado automático** después del aumento.
- **Redondeo a centavos:** 3540,75 × 1,10 = 3894,825 → 3894,83.

### Caso 7 — Reposición de stock

```
Opcion: 4
Nombre del medicamento: acido folico
Stock actual: 3
Cantidad que ingresa: 0
   Valor invalido. Ingrese un entero entre 1 y 10000: 7
   ACIDO FOLICO: stock 3 -> 10

Opcion: 5
LISTADO DE MEDICAMENTOS (orden alfabetico)
POS  CODIGO  MEDICAMENTO           PRECIO   STOCK
1    1111    ACIDO FOLICO         1980.00      10
...
```

**Qué verifica:** que la reposición sume al stock y que ACIDO FOLICO deje de tener la marca de stock crítico.

### Caso 8 — Fin de la entrada de datos

```
Opcion: 1
Nombre del medicamento (PPPPPPP para terminar): ibuprofeno
Cantidad: Ctrl+Z ⏎   (Windows)   /   Ctrl+D   (Linux)
Fin de la entrada de datos: el programa termina.
```

**Qué verifica:** que el programa termine en vez de repetir "Valor invalido" para siempre. Al cortarse así no se muestran los informes finales, porque ya no hay teclado para seguir.

### Caso 9 — Nombre con tilde

```
Opcion: 2
Nombre del medicamento: ácido folico
   áCIDO FOLICO: no figura en la base de la farmacia
```

**Qué verifica:** que una letra con tilde no rompa el programa. En Windows esa letra se guarda como un `char` negativo, y `toupper` con un negativo es comportamiento indefinido: podría cerrar el programa. Con `toupper((unsigned char)...)` la letra con tilde queda sin cambiar, se pasa a mayúsculas el resto, y el nombre se informa como inexistente porque la base no lleva tildes. Según la consola, la `á` puede verse como otro símbolo.

<!-- solo-md -->
---
**Fuentes:** salidas obtenidas corriendo `build/farmacia` (compilado con `make`, g++ `-std=c++98`) con cada secuencia de entradas, el 09/nov/2026; enunciado del Final 3 en `00_consigna_y_contexto.md`.
<!-- /solo-md -->
