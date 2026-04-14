# Sistemas de Representación — LibreCAD y formato DXF

## 1. ¿Por qué CAD en esta materia?

El dibujo técnico manual (láminas y croquis) enseña a pensar en el lenguaje del plano. El CAD (Computer Aided Design) es la herramienta con la que ese lenguaje se produce profesionalmente.

En la industria, los planos se entregan en formato digital. AutoCAD es el estándar de facto, pero su licencia cuesta cientos de dólares al año. LibreCAD es software libre, corre en Linux sin problemas, y produce archivos **DXF** que AutoCAD lee de manera nativa.

> **Analogía contable:** Es como usar LibreOffice Calc para producir archivos `.xlsx` que el cliente abre en Excel. El formato es el que importa, no el software que lo generó.

---

## 2. El formato DXF

**DXF** (Drawing Exchange Format) fue creado por Autodesk en 1982 como formato de interoperabilidad para AutoCAD. Hoy es el estándar abierto del dibujo técnico vectorial.

| Característica | Detalle |
|---|---|
| Tipo de archivo | Texto plano (ASCII) o binario |
| Extensión | `.dxf` |
| Creado por | Autodesk (1982) |
| Estándar actual | DXF 2018 (basado en AutoCAD 2018) |
| Soporte en LibreCAD | DXF R12, R14, 2000, 2004 |
| Soporte en AutoCAD | Todas las versiones |

### ¿Qué contiene un DXF?

Un archivo DXF es una descripción textual del dibujo organizada en secciones:

```
HEADER   → variables globales (unidades, límites del dibujo)
TABLES   → capas (layers), estilos de línea, estilos de texto
BLOCKS   → definiciones de bloques reutilizables
ENTITIES → los objetos del dibujo (líneas, arcos, texto, cotas)
EOF      → fin de archivo
```

Esto es relevante porque al exportar desde LibreCAD a DXF, cada capa del dibujo se mapea a una capa en el DXF, y AutoCAD las importa correctamente.

---

## 3. LibreCAD

### 3.1 Instalación en Linux (Debian/Ubuntu)

```bash
sudo apt install librecad
```

O desde el gestor de paquetes gráfico. La versión en los repositorios de Ubuntu suele ser la 2.x (estable). Para la versión más reciente:

```bash
sudo add-apt-repository ppa:librecad-dev/librecad-stable
sudo apt update
sudo apt install librecad
```

### 3.2 Interfaz principal

```
┌─────────────────────────────────────────────────────────────┐
│  Barra de menú: File | Edit | View | Tools | Draw | ...     │
├──────┬──────────────────────────────────────────────────────┤
│      │                                                      │
│ Cap- │           ÁREA DE DIBUJO                             │
│ as   │                                                      │
│      │                                                      │
│(Doc- │                                                      │
│ked)  │                                                      │
├──────┴──────────────────────────────────────────────────────┤
│  Barra de comandos (línea de texto — como AutoCAD)          │
├─────────────────────────────────────────────────────────────┤
│  Barra de estado: coordenadas X, Y | snap | escala         │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 Configuración inicial para los TPs

Antes de empezar a dibujar, configurar:

**1. Unidades → milímetros**
`Edit → Application Preferences → Units → Millimeter`

**2. Formato de papel A4**
`Edit → Current Drawing Preferences → Paper → A4 (210×297mm) | Portrait`

**3. Cuadrícula**
`View → Grid → activar | snap cada 1 mm`

**4. Escala**
Para los TPs de esta materia: escala 1:1 (1 mm en pantalla = 1 mm real)

---

## 4. Capas (Layers) — equivalente a los tipos de línea IRAM

Las capas en CAD son la versión digital de los distintos lápices. Cada tipo de línea IRAM se asigna a una capa con su grosor y estilo.

### Configuración de capas para esta materia

| Capa | Color sugerido | Tipo de línea | Grosor | Uso |
|---|---|---|---|---|
| `CONTORNO` | Negro (7) | Continuous | 0,50 mm | Aristas visibles (01.2) |
| `COTAS` | Amarillo (2) | Continuous | 0,25 mm | Acotación completa (01.1) |
| `OCULTAS` | Azul (5) | Dashed | 0,25 mm | Aristas ocultas (02.1) |
| `EJES` | Rojo (1) | Center | 0,25 mm | Ejes de simetría (04.1) |
| `ROTULO` | Negro (7) | Continuous | 0,35 mm | Texto del rótulo |
| `CONSTRUCCION` | Gris (8) | Continuous | 0,13 mm | Auxiliares (se desactiva al imprimir) |

Para crear una capa: `Layer → Add Layer` o desde el panel lateral de capas.

---

## 5. Flujo de trabajo para un TP en LibreCAD

### Paso 1 — Configurar el documento

```
1. Nuevo archivo (Ctrl+N)
2. Unidades: mm
3. Papel: A4
4. Crear las 6 capas con sus grosores y estilos
5. Activar capa CONSTRUCCION para el trazado auxiliar
```

### Paso 2 — Trazar el marco A4

Con la capa `ROTULO` activa:

```
Rectángulo desde (25, 10) hasta (205, 287)
→ Esto da el marco interno: 180 × 277 mm
→ VERIFICAR: el área útil es 175 × 257 mm (el marco tiene grosor)
```

Coordenadas del rótulo (ángulo inferior derecho del área útil):
```
Esquina inferior derecha del área: (205, 10)
Rótulo: 175 mm ancho × 20 mm alto
Empieza en: (30, 10) → termina en: (205, 30)
```

### Paso 3 — Dibujar el contenido

- Cambiar a la capa correspondiente antes de cada tipo de trazo
- Usar las herramientas: `Draw → Line`, `Draw → Arc`, `Draw → Circle`
- Coordenadas absolutas: escribir `x,y` en la barra de comandos
- Coordenadas relativas: escribir `@dx,dy`

### Paso 4 — Acotación

LibreCAD incluye herramientas de acotación automática:

```
Draw → Dimension → Horizontal / Vertical / Aligned / Radius / Diameter
```

Configurar el estilo de cota antes de acotar:
`Edit → Current Drawing Preferences → Dimensions`
- Texto height: 3,5 mm (para que el número quede visible en A4)
- Arrow size: 2,5 mm (relación 4:1 aproximada con línea 0,25 mm)

### Paso 5 — Texto y caligrafía

Para el rótulo y etiquetas:
```
Draw → Text (o presionar T)
→ Font: ISO 3098 (si está disponible) o cualquier fuente monoespacio
→ Altura: 5 mm (h=5 según tabla IRAM)
```

> LibreCAD no reproduce exactamente la caligrafía IRAM tipo A dibujada a mano. Para los TPs que evalúan caligrafía (TP 09, 10), el trabajo se hace a mano. LibreCAD se usa para geometría y acotación.

---

## 6. Exportar a DXF para usar en AutoCAD (Windows)

### 6.1 Desde LibreCAD (Linux)

```
File → Save As → Formato: "Drawing Exchange DXF R2004 (*.dxf)"
```

Recomendaciones:
- Usar **DXF R2004** como target: compatible con AutoCAD 2004 en adelante y con todas las versiones de licencia estudiantil de Autodesk
- Evitar DXF R12 (no soporta capas con grosor) salvo que sea el único formato aceptado

### 6.2 Abrir en AutoCAD (Windows) con licencia estudiantil

La licencia estudiantil de AutoCAD (Autodesk Education) es gratuita y se obtiene en `autodesk.com/education`. Incluye AutoCAD completo durante 1 año renovable.

```
En AutoCAD:
  File → Open → seleccionar el .dxf exportado desde LibreCAD
  → Las capas, grosores y tipos de línea se importan automáticamente
```

**Marca de agua en impresión:** Los archivos creados o editados con la versión estudiantil incluyen automáticamente una marca de agua "EDUCATIONAL VERSION" en el impreso. Para los TPs de la materia esto es aceptable; para uso profesional, no.

### 6.3 Workflow recomendado (Linux nativo)

```
LibreCAD (Linux)
     │
     │ Dibujar y acotar
     │
     ▼
 Guardar como .dxf R2004
     │
     │ Transferir via USB / nube / mail
     │
     ▼
AutoCAD (Windows, licencia estudiantil)
     │
     │ Revisión final, impresión
     │
     ▼
 PDF / impresión física
```

Para transferir el archivo sin necesitar Windows:
- **Imprimir directo desde LibreCAD:** `File → Print Preview → Print` → exportar a PDF
- **Visor online:** los archivos DXF pueden abrirse en `viewer.autodesk.com` (web, sin instalar nada)

---

## 7. Atajos de teclado útiles en LibreCAD

| Acción | Atajo |
|---|---|
| Nueva línea | `L` |
| Nuevo arco | `A` |
| Nuevo círculo | `C` |
| Texto | `T` |
| Zoom extensión (ver todo) | `V` + Enter |
| Zoom ventana | `Z` |
| Deshacer | `Ctrl+Z` |
| Rehacer | `Ctrl+Y` |
| Snap a cuadrícula | `Ctrl+G` |
| Snap a punto final | `E` |
| Snap a punto medio | `M` |
| Snap perpendicular | `P` |
| Cancelar operación | `Esc` |
| Ingresar coordenadas | Escribir en barra de comando |

---

## 8. Diferencias clave con AutoCAD

| Característica | LibreCAD | AutoCAD |
|---|---|---|
| Precio | Gratuito | Pago (o licencia estudiantil) |
| Plataforma | Linux, Windows, Mac | Windows (principal), Mac |
| Formato nativo | `.dxf` | `.dwg` (propietario) |
| Lee `.dwg` | No (requiere plugin de pago) | Sí (nativo) |
| Lee `.dxf` | Sí | Sí |
| 3D | No | Sí |
| Capas | Sí (completo) | Sí (completo) |
| Acotación automática | Sí (básica) | Sí (avanzada) |
| Marcas de agua | No | Sí (versión estudiantil) |

Para los TPs de esta materia (dibujo plano 2D), LibreCAD cubre todo lo necesario. La transición a AutoCAD es directa: los conceptos de capas, tipos de línea, acotación y coordenadas son idénticos.

---

## 9. Errores comunes

| Error | Solución |
|---|---|
| DXF exportado no se abre en AutoCAD | Exportar como R2004 en vez de R12 |
| Líneas sin grosor en AutoCAD | Asignar grosor explícito a cada capa en LibreCAD antes de exportar |
| Tipos de línea se pierden | Verificar que los nombres de line type coincidan (DASHED, CENTER, etc.) |
| El dibujo queda fuera del papel en impresión | Verificar que el modelo esté en el área definida por el marco A4 |
| Coordenadas en pulgadas | Cambiar unidades a mm en Application Preferences |
| Texto demasiado pequeño | Altura de texto ≥ 3,5 mm para imprimir en A4 legible |

---

## 10. Mapa conceptual

```
HERRAMIENTAS CAD — SISTEMAS DE REPRESENTACIÓN
│
├── LibreCAD (Linux)
│   ├── Gratuito y libre
│   ├── Formato nativo: .dxf
│   ├── Capas = tipos de línea IRAM
│   └── Exporta a DXF R2004 para AutoCAD
│
├── DXF (Drawing Exchange Format)
│   ├── Estándar abierto de Autodesk (1982)
│   ├── Texto ASCII — interoperable
│   └── Secciones: HEADER, TABLES, BLOCKS, ENTITIES
│
├── AutoCAD (Windows)
│   ├── Licencia estudiantil gratuita (Autodesk Education)
│   ├── Lee .dxf directamente
│   └── Marca de agua en impresión (versión estudiantil)
│
└── Workflow
    ├── Dibujar en LibreCAD (Linux)
    ├── Exportar .dxf R2004
    ├── Abrir en AutoCAD o viewer online
    └── Imprimir PDF desde LibreCAD o AutoCAD
```
