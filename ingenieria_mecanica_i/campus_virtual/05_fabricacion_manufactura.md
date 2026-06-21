# Unidad V — Fabricación y Manufactura

## Definición de Ingeniería de Manufactura

La **ingeniería de manufactura** es la ciencia que estudia los procesos de conformado y fabricación de componentes con adecuada precisión dimensional, así como la maquinaria, herramientas y equipos necesarios para la transformación de materiales, su automatización, planificación y verificación.

Su objetivo central: **convertir materia prima en un producto nuevo o actualizado de la forma más económica, eficiente y eficaz posible**.

Diferencia manufactura vs. producción:
- **Manufactura**: transformación de materiales en productos (el proceso físico de hacer algo)
- **Producción**: organización del proceso completo, incluyendo planificación, control y logística

Analogía contable: la manufactura es como la generación del comprobante (el acto físico de registrar); la producción es como el ciclo contable completo (planificación → registro → control → cierre).

## Procesos de Manufactura

Los procesos de manufactura se clasifican según cómo modifican la materia prima:

```
PROCESOS DE MANUFACTURA
│
├── CONFORMADO (cambian la forma sin remover material)
│   ├─ Forja (golpe sobre metal caliente)
│   ├─ Laminado (compresión entre rodillos)
│   ├─ Extrusión (forzar material por un dado)
│   ├─ Trefilado (estiramiento)
│   └─ Estampado / embutición (prensado en frío)
│
├── MECANIZADO (remueven material — viruta)
│   ├─ Torneado (pieza gira, herramienta fija)
│   ├─ Fresado (herramienta gira, pieza avanza)
│   ├─ Taladrado (broca penetra el material)
│   ├─ Rectificado (abrasión de precisión)
│   └─ CNC (Control Numérico Computarizado)
│
├── FUNDICIÓN (material líquido → molde)
│   ├─ Fundición en arena
│   ├─ Fundición a presión (die casting)
│   └─ Fundición centrífuga
│
├── UNIÓN
│   ├─ Soldadura (MIG, TIG, electrodo)
│   ├─ Remachado
│   └─ Adhesivos industriales
│
└── PROCESOS ESPECIALES / AVANZADOS
    ├─ Fabricación aditiva (impresión 3D)
    ├─ Electroerosión (EDM)
    ├─ Corte por láser / agua
    └─ Manufactura asistida por computadora (CAM)
```

## Sistemas de Fabricación

La organización de cómo se produce ha evolucionado históricamente:

### Sistema Artesanal (pre-Industrial)
Un artesano produce el bien completo de principio a fin. Alta personalización, baja productividad, alto costo unitario.

### Sistema Putting-Out (siglo XVIII)
El empresario distribuye materias primas a trabajadores domiciliarios que realizan partes del trabajo. Primer paso hacia la especialización.

### Sistema Fabril (Revolución Industrial)
Los trabajadores se reúnen en una fábrica con maquinaria. División del trabajo por etapas. Nace la línea de producción.

### Sistema Americano de Manufactura (siglo XIX)
Piezas intercambiables con tolerancias dimensionales precisas. Permite ensamblar cualquier pieza de un lote con cualquier otra. Base de la producción en serie.

### Producción en Cadena / Línea de Ensamble (Taylor / Ford, siglo XX)
Cada operario realiza una tarea específica; el producto avanza por puestos de trabajo secuenciales. Máxima eficiencia para productos estandarizados.

```
PUESTO 1 ──► PUESTO 2 ──► PUESTO 3 ──► PUESTO 4 ──► PRODUCTO TERMINADO
(subparte A) (subparte B) (ensamble) (control calidad)
```

### Manufactura Integrada por Computadora (CIM)
Integra diseño (CAD), fabricación (CAM), gestión y control en un sistema computarizado unificado. Máxima automatización y trazabilidad.

```
CAD (diseño) ──► CAE (análisis) ──► CAM (fabricación) ──► SCADA (control)
                     ↑_______________________________________↓
                              MES (Manufacturing Execution System)
```

### Método Justo a Tiempo (JIT — Just In Time)
Producir exactamente lo que se necesita, en el momento en que se necesita, en la cantidad necesaria. Mínimo stock de inventario. Originado en Toyota (Sistema Toyota de Producción).

Analogía contable: JIT es como el presupuesto base cero — no se acumula nada por inercia; cada necesidad se justifica antes de producir.

### Impresión 3D (Manufactura Aditiva)
Construye el objeto capa por capa desde un modelo digital. Permite geometrías imposibles para los procesos convencionales. Materiales: plásticos, metales, cerámicas, hormigón.

Ventajas: rapidez para prototipos, personalización, sin herramientas especiales.
Limitaciones: velocidad baja para producción masiva, acabado superficial inferior al mecanizado.

## Tecnologías de Diseño y Fabricación Asistida

| Tecnología | Definición | Aplicación |
|---|---|---|
| CAD | Diseño asistido por computadora | Planos 2D y modelos 3D |
| CAM | Fabricación asistida por computadora | Trayectorias de CNC |
| CAE | Ingeniería asistida por computadora | Análisis FEA, CFD |
| CNC | Control numérico computarizado | Ejecución automatizada de cortes |
| Robotización | Robots industriales en línea | Soldadura, pintura, ensamble |

## Intercambiabilidad y Tolerancias

La **intercambiabilidad** es la capacidad de reemplazar una pieza por otra del mismo tipo sin ajustes manuales. Requiere que las piezas se fabriquen dentro de **tolerancias dimensionales** definidas.

```
DIMENSIÓN NOMINAL: 50 mm
TOLERANCIA: ±0,1 mm
RANGO ACEPTABLE: 49,9 mm a 50,1 mm

Si todas las piezas caen en ese rango, son intercambiables entre sí.
```

Sin intercambiabilidad no existe producción en serie ni mantenimiento eficiente (no se podría reponer una pieza sin ajustarla individualmente).

## Control de Calidad en Manufactura

El control de calidad verifica que los productos cumplen las especificaciones:

```
CONTROL DE CALIDAD
├── Inspección por atributos: pasa / no pasa (GO / NO-GO)
├── Inspección por variables: medición de dimensiones
├── Control Estadístico de Proceso (SPC): monitoreo continuo
└── Normas: ISO 9001 (gestión de calidad), IRAM equivalentes
```

La calidad no se inspecciona al final — se diseña en el proceso desde el principio (concepto de *quality by design*).

## Casos de Aplicación del Ingeniero Mecánico en Manufactura

- **Industria alimenticia**: diseño de máquinas de llenado, mezcla, envasado y etiquetado
- **Industria farmacéutica**: procesos de manufactura bajo normas GMP (Good Manufacturing Practices)
- **Industria automotriz**: líneas de estampado, soldadura robotizada, ensamble
- **Petróleo y gas**: fabricación de componentes para alta presión y temperatura; materiales resistentes a corrosión
- **Agricultura**: maquinaria de recolección, congeladores, hornos industriales

## Resumen

| Concepto | Descripción |
|---|---|
| Manufactura | Transformación de materia prima en producto; proceso físico |
| Producción | Organización integral del proceso productivo |
| Conformado | Cambia forma sin remover material (forja, laminado, extrusión) |
| Mecanizado | Remueve material (torneado, fresado, taladrado) |
| JIT | Producir solo lo necesario cuando se necesita |
| Intercambiabilidad | Piezas dentro de tolerancias; se reemplazan sin ajuste |
| CAD/CAM | Diseño y fabricación asistidos por computadora |

## Errores conceptuales comunes

- Confundir manufactura con producción: manufactura es el proceso físico; producción incluye toda la gestión.
- Creer que JIT elimina todo el inventario: reduce el inventario pero mantiene un mínimo operativo.
- Pensar que la impresión 3D reemplaza el mecanizado: son tecnologías complementarias para distintos contextos.

## Mapa conceptual (ASCII)

```
INGENIERÍA DE MANUFACTURA
         │
         ├── OBJETIVO ──► materia prima → producto; económico + eficiente
         │
         ├── PROCESOS ─┬── Conformado (sin remoción)
         │             ├── Mecanizado (con remoción)
         │             ├── Fundición
         │             └── Aditivos (impresión 3D)
         │
         ├── SISTEMAS ─┬── Artesanal → putting-out → fabril → serie
         │             ├── CIM (integración total)
         │             └── JIT (producción bajo demanda)
         │
         └── CALIDAD ──► tolerancias + SPC + ISO 9001
```

---
*Fuentes: 1.unidad I Ingeniería y Sociedad.pdf; HABILIDADES BÁSICAS DE LA INGENIERÍA.pdf; Ing. Mec. I - Plan de Estudio.pdf*
