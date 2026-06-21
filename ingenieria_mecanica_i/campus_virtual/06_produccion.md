# Unidad VI — Producción

## Definición de Ingeniería de Producción

La **ingeniería de producción** es la rama de la ingeniería que trata con procesos de manufactura y métodos de elaboración de productos industriales, integrando todos los factores relevantes para elaborar soluciones óptimas a problemas relacionados con la transformación de insumos económicos en productos necesarios para la sociedad.

Es multidisciplinar: adapta ciencia, tecnología, economía y administración para optimizar los sistemas de producción de bienes y servicios.

Analogía contable: si la manufactura es el registro individual de cada asiento, la producción es el diseño del sistema contable completo — el plan de cuentas, los procedimientos, el control interno, el cierre mensual.

## Diferencia entre Manufactura y Producción

| Aspecto | Manufactura | Producción |
|---|---|---|
| Enfoque | Proceso físico de transformación | Organización integral del sistema |
| Pregunta | ¿Cómo se hace? | ¿Cómo se organiza, planifica y controla? |
| Escala temporal | Operación | Gestión |
| Herramientas | Máquinas, procesos, tolerancias | Indicadores, planificación, logística |

La manufactura es **una función dentro** del sistema de producción.

## Funciones del Sistema de Producción

```
SISTEMA DE PRODUCCIÓN
│
├── PLANIFICACIÓN DE LA PRODUCCIÓN
│   ├─ Qué producir, cuánto y cuándo
│   ├─ MPS (Master Production Schedule)
│   └─ MRP (Material Requirements Planning)
│
├── CONTROL DE PRODUCCIÓN
│   ├─ Seguimiento del avance vs. plan
│   ├─ Indicadores de productividad
│   └─ Detección y corrección de desvíos
│
├── GESTIÓN DE INVENTARIO
│   ├─ Materias primas y componentes
│   ├─ Trabajo en proceso (WIP)
│   └─ Producto terminado
│
├── LOGÍSTICA INTERNA
│   └─ Transporte de materiales dentro de la planta
│
├── MANTENIMIENTO (coordinado con producción)
│   └─ Disponibilidad de equipos
│
└── CONTROL DE CALIDAD
    └─ Inspección durante y después del proceso
```

## Indicadores de Producción

### Productividad

```
Productividad = Producción obtenida / Recursos utilizados
```

Mide la eficiencia en el uso de recursos. Puede expresarse como:
- Unidades por hora de trabajo
- Toneladas por kWh de energía
- Piezas por turno

### OEE — Overall Equipment Effectiveness (Efectividad Global del Equipo)

```
OEE = Disponibilidad × Rendimiento × Calidad

Disponibilidad = Tiempo real de operación / Tiempo planificado
Rendimiento    = Producción real / Producción teórica
Calidad        = Unidades buenas / Unidades totales producidas
```

Ejemplo:
- Disponibilidad = 90% (la máquina estuvo parada 10% del tiempo)
- Rendimiento = 85% (produjo al 85% de su velocidad nominal)
- Calidad = 98% (2% de rechazo)
- OEE = 0,90 × 0,85 × 0,98 = **75%**

Un OEE de 85% se considera clase mundial.

### Takt Time

El **takt time** es el ritmo al que debe producir el sistema para satisfacer la demanda del cliente:

```
Takt time = Tiempo disponible de producción / Demanda del cliente
```

Ejemplo: si hay 450 min/turno y el cliente pide 90 unidades/turno:
- Takt time = 450 / 90 = **5 min/unidad**

Cada puesto de la línea debe completar su operación en ≤5 min para no generar cuello de botella.

## Tipos de Sistemas de Producción

### Producción por Proyecto
Una obra única y de gran escala. Ej.: puente, nave industrial, planta química.
- Alta complejidad, larga duración
- Gestión por fases (ver Unidad IV)

### Producción por Lotes
Se fabrican lotes de un mismo producto, luego se cambia a otro. Ej.: línea de pinturas industriales.
- Flexibilidad media
- Tiempo de cambio (setup) entre lotes

### Producción en Línea (Continua / Serie)
El producto fluye continuamente por puestos de trabajo secuenciales. Ej.: automotriz, embotellado.
- Alta productividad, baja flexibilidad
- El cuello de botella define la velocidad del sistema

```
LÍNEA DE PRODUCCIÓN

[PUESTO 1] → [PUESTO 2] → [PUESTO 3] → [CONTROL CALIDAD] → DESPACHO
   3 min       4 min*      2 min           1 min

* El cuello de botella (4 min) define el takt time mínimo posible
```

### Producción Continua
Proceso sin interrupciones, 24/7. Ej.: refinería, planta de cemento, siderurgia.
- Altísima productividad, nula flexibilidad
- Parar y arrancar tiene un costo enorme; el mantenimiento es crítico

## Planificación de la Producción

### MPS — Master Production Schedule

Plan de producción a mediano plazo que define qué productos se fabrican, en qué cantidades y cuándo, dentro de un horizonte de planificación (semanas/meses).

### MRP — Material Requirements Planning

A partir del MPS, calcula qué materiales se necesitan, en qué cantidades y en qué fechas, teniendo en cuenta los inventarios existentes y los tiempos de entrega de proveedores.

```
MPS (qué y cuándo producir)
       │
       ▼
MRP (qué materiales pedir y cuándo)
       │
       ▼
ÓRDENES DE COMPRA + ÓRDENES DE PRODUCCIÓN
```

Analogía contable: el MPS es el presupuesto de ventas; el MRP es el presupuesto de compras derivado. Igual que en contabilidad, se parte de los ingresos esperados para calcular los egresos necesarios.

## Gestión Tecnológica en Producción

Según la Unidad I, el ingeniero de producción debe dominar:

| Área | Aplicación |
|---|---|
| Matemática | Modelos de producción, cálculo integral, estadística |
| Física | Estado de materias primas, comportamiento de materiales |
| Estadística | Indicadores de producción, muestreo estadístico, SPC |
| Gestión ambiental (SGA) | Minimizar recursos y daño ambiental en la producción |
| Control de calidad (SGC) | Normas de certificación, mejora continua |
| Gestión tecnológica | Innovación, transferencia de tecnología |
| Automatización | CAM, robots, informatización de la producción |

## El Lean Manufacturing (Producción Ajustada)

Sistema de producción originado en Toyota. Busca eliminar todo desperdicio (*muda*) en el proceso.

Los 7 desperdicios (TIMWOOD):
1. **T**ransporte innecesario
2. **I**nventario excesivo
3. **M**ovimiento innecesario de operarios
4. **W**aiting — esperas
5. **O**verproduction — sobreproducción
6. **O**verprocessing — reprocesamiento
7. **D**efectos

```
LEAN
└── eliminar desperdicios
     └── para producir más valor con menos recursos
          └── herramientas: JIT, 5S, Kaizen, Kanban, SMED
```

## Resumen

| Concepto | Descripción |
|---|---|
| Producción | Organización integral de la transformación de insumos en productos |
| OEE | Disponibilidad × Rendimiento × Calidad |
| Takt time | Ritmo de producción requerido por la demanda |
| MPS | Plan maestro de producción |
| MRP | Planificación de requerimientos de materiales |
| Lean | Eliminar desperdicios para maximizar valor |
| Cuello de botella | El puesto más lento que limita toda la línea |

## Errores conceptuales comunes

- Confundir productividad con producción: producir más no es ser más productivo si se usaron más recursos.
- Pensar que maximizar la producción de cada puesto es óptimo: lo que importa es el flujo total; sobreproducir en un puesto crea inventario en proceso.
- Ignorar el cuello de botella: mejorar cualquier otro puesto que no sea el cuello de botella no mejora la capacidad del sistema.

## Mapa conceptual (ASCII)

```
PRODUCCIÓN
     │
     ├── SISTEMA ─┬── Planificación (MPS → MRP)
     │            ├── Control (indicadores, desvíos)
     │            ├── Inventario (materias primas, WIP, PT)
     │            └── Calidad + Mantenimiento
     │
     ├── TIPOS ─┬── Por proyecto (único)
     │          ├── Por lotes (flexible)
     │          ├── En línea (series)
     │          └── Continua (24/7)
     │
     └── INDICADORES ─┬── Productividad
                      ├── OEE
                      └── Takt time
```

---
*Fuentes: 1.unidad I Ingeniería y Sociedad.pdf; Ing. Mec. I - Plan de Estudio.pdf*
