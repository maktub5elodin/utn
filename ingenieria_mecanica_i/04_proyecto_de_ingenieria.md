# Unidad IV — El Proyecto de Ingeniería

## Definición de Proyecto de Ingeniería

Un **proyecto de ingeniería** es una actividad temporal y única, con inicio y fin definidos, que emplea metodología racional para encontrar una solución detallada a necesidades establecidas en un estudio inicial, definiendo los recursos necesarios: máquinas y equipos, lugar de implantación, suministro de insumos, recursos humanos, obras complementarias y dispositivos de protección ambiental.

Características que distinguen un proyecto de la operación continua:
- **Temporalidad**: tiene inicio y fin
- **Unicidad**: produce un resultado único (no repetitivo como la producción en serie)
- **Progresividad**: se desarrolla por etapas con creciente nivel de detalle
- **Objetivo definido**: satisface una necesidad específica

Analogía contable: un proyecto es como una auditoría de estados financieros — tiene alcance definido, equipo asignado, presupuesto, cronograma y entregable final. La operación continua es como el ciclo contable mensual.

## Diferencia entre Diseño y Proyecto

```
DISEÑO                          PROYECTO
─────────────────────────────────────────────────────────────
Proceso creativo de definir     Proceso de planificación y
la solución técnica             ejecución de esa solución

Se pregunta: ¿Cómo debe ser?   Se pregunta: ¿Cómo se realiza?

Producto: planos, especificac.  Producto: sistema construido
                                 o instalado y funcionando

Herramienta: CAD, cálculo       Herramienta: gestión de recursos,
                                 cronogramas, presupuesto
```

En la práctica, el diseño es una **fase dentro del proyecto**.

## Etapas del Proyecto de Ingeniería

```
ETAPA 1: IDENTIFICACIÓN / PREFACTIBILIDAD
    └── ¿El proyecto es viable? Evaluación preliminar.
         Recursos estimados, mercado, tecnología disponible.

ETAPA 2: FACTIBILIDAD / ANTEPROYECTO
    └── Estudio detallado de viabilidad técnica, económica y ambiental.
         Alternativas de solución. Selección de la mejor opción.

ETAPA 3: INGENIERÍA BÁSICA (Proyecto Básico)
    └── Definición del proceso y equipos principales.
         Balance de materiales y energía. Diagramas P&ID.
         Especificaciones de equipos.

ETAPA 4: INGENIERÍA DE DETALLE
    └── Planos de construcción. Especificaciones completas.
         Lista de materiales (BOM). Documentos de licitación.

ETAPA 5: PROCURA (COMPRAS)
    └── Contratación de equipos, materiales y servicios.
         Seguimiento de entregas. Control de calidad.

ETAPA 6: CONSTRUCCIÓN / MONTAJE
    └── Ejecución física en el terreno o planta.
         Supervisión de obra. Control de avance.

ETAPA 7: PUESTA EN MARCHA
    └── Pruebas en vacío y con carga. Ajustes. Capacitación.
         Transferencia al cliente u operador.

ETAPA 8: OPERACIÓN Y CIERRE
    └── El sistema opera normalmente. El proyecto cierra.
         Documentación final (as-built). Lecciones aprendidas.
```

## El Triángulo de Restricciones del Proyecto

Todo proyecto opera con tres restricciones interrelacionadas:

```
              ALCANCE
              /      \
             /        \
            /          \
        TIEMPO ──────── COSTO

Si se modifica una, las otras se ven afectadas.
```

- **Aumentar el alcance** sin cambiar tiempo ni costo → baja calidad
- **Reducir el tiempo** sin cambiar alcance ni costo → aumenta el costo (recursos adicionales)
- **Reducir el costo** sin cambiar alcance ni tiempo → reduce el alcance o aumenta el riesgo

La gestión del proyecto consiste en equilibrar estas tres restricciones para satisfacer al cliente.

## Documentos Típicos de un Proyecto

| Documento | Contenido |
|---|---|
| EDT (Estructura de Desglose del Trabajo) | Descomposición del trabajo en paquetes manejables |
| Cronograma (Gantt / CPM) | Secuencia y duración de actividades |
| Presupuesto | Estimación de costos por actividad y total |
| Memoria descriptiva | Justificación de decisiones técnicas |
| Planos de ingeniería | Diseño detallado (civiles, mecánicos, eléctricos) |
| Especificaciones técnicas | Requisitos de materiales y equipos |
| BOM (Bill of Materials) | Lista completa de materiales con cantidades |
| Plan de calidad | Procedimientos de control e inspección |
| Plan de seguridad | Identificación de riesgos y medidas preventivas |

## Gestión del Proyecto — Roles

```
DIRECTOR DE PROYECTO (Project Manager)
       │
       ├─ Ingeniería de diseño (planos, especificaciones)
       ├─ Procura (compras, contratos)
       ├─ Construcción / montaje (ejecución en campo)
       ├─ Control de costos y cronograma
       └─ Seguridad e higiene industrial
```

El director de proyecto es responsable de coordinar todas las disciplinas para lograr el objetivo en tiempo, costo y calidad.

## Tipos de Proyectos de Ingeniería Mecánica

- **Plantas industriales**: diseño y montaje de instalaciones productivas completas
- **Ampliaciones y modificaciones**: expansión de capacidad o cambio de proceso
- **Ingeniería de procesos**: diseño de líneas de producción continua
- **Proyectos de energía**: plantas de generación (hidráulica, térmica, solar, eólica)
- **Instalaciones mecánicas**: redes de vapor, aire comprimido, agua de proceso
- **Proyectos de mantenimiento mayor**: paradas de planta programadas con gran alcance

## El Anteproyecto y la Memoria Técnica

El **anteproyecto** es el documento que sintetiza la propuesta de solución antes de comprometer los recursos de diseño de detalle. Incluye:

1. Descripción de la necesidad y el alcance del proyecto
2. Descripción de la solución propuesta
3. Estimación de recursos (equipos, personal, tiempo)
4. Evaluación económica preliminar (inversión, costos operativos, rentabilidad esperada)
5. Análisis de riesgos principales
6. Recomendación de continuidad

Analogía contable: el anteproyecto equivale al **informe de prefactibilidad** previo a una inversión; la memoria técnica equivale al **dictamen con sus bases y fundamentos**.

## Herramienta: Diagrama de Gantt

```
ACTIVIDAD          | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 |
────────────────────|────|────|────|────|────|────|────|────|
Ingeniería básica   |████|████|    |    |    |    |    |    |
Ingeniería detalle  |    |████|████|████|    |    |    |    |
Procura             |    |    |████|████|████|    |    |    |
Construcción        |    |    |    |    |████|████|████|    |
Puesta en marcha    |    |    |    |    |    |    |████|████|
```

Cada actividad tiene duración, recursos asignados y dependencias con otras actividades.

## Resumen

| Concepto | Definición |
|---|---|
| Proyecto de ingeniería | Actividad temporal y única para satisfacer una necesidad |
| Triángulo de restricciones | Alcance – Tiempo – Costo |
| Anteproyecto | Evaluación de factibilidad antes del compromiso de recursos |
| Memoria técnica | Justificación de las decisiones de diseño |
| BOM | Lista de materiales completa |
| Diagrama de Gantt | Cronograma visual de actividades |

## Errores conceptuales comunes

- Creer que el proyecto termina con la construcción: la puesta en marcha y el cierre son etapas del proyecto.
- Ignorar la interrelación alcance-tiempo-costo: cambiar uno sin ajustar los otros genera problemas.
- Confundir proyecto con operación: el proyecto produce algo nuevo y único; la operación repite un proceso.

## Mapa conceptual (ASCII)

```
NECESIDAD
    │
    ▼
PROYECTO DE INGENIERÍA
    │
    ├── ETAPAS: prefactibilidad → factibilidad → básica → detalle
    │           → procura → construcción → puesta en marcha → cierre
    │
    ├── RESTRICCIONES: ALCANCE ─── TIEMPO ─── COSTO
    │                      (triángulo: si uno cambia, cambian los demás)
    │
    └── ENTREGABLE: sistema construido, instalado y operativo
```

---
*Fuentes: 1.unidad I Ingeniería y Sociedad.pdf; 1.El Ing y su Profesión.pdf; Ing. Mec. I - Plan de Estudio.pdf*
