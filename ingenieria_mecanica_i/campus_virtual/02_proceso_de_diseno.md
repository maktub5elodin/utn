# Unidad II — El Proceso de Diseño

## Qué es el Diseño en Ingeniería

El **diseño en ingeniería** es el proceso creativo de definir soluciones técnicas para satisfacer necesidades humanas. No es un acto único sino un **ciclo iterativo** de etapas que va de lo abstracto (la necesidad) a lo concreto (las especificaciones del producto o sistema).

Diferencia fundamental: en contabilidad, el plan de cuentas ya existe y se aplica; en ingeniería, el "plan de cuentas" (la solución) debe crearse desde cero para cada nuevo problema.

## Las Etapas del Proceso de Diseño

```
1. RECONOCIMIENTO DE LA NECESIDAD
       │
       ▼
2. DEFINICIÓN DEL PROBLEMA
       │
       ▼
3. BÚSQUEDA Y RECOPILACIÓN DE INFORMACIÓN
       │
       ▼
4. GENERACIÓN DE ALTERNATIVAS
       │
       ▼
5. ANÁLISIS Y EVALUACIÓN DE ALTERNATIVAS
       │
       ▼
6. SELECCIÓN DE LA MEJOR SOLUCIÓN
       │
       ▼
7. ESPECIFICACIÓN Y COMUNICACIÓN (planos, documentos)
       │
       ▼
8. IMPLEMENTACIÓN (fabricación / construcción)
       │
       ▼
9. EVALUACIÓN Y RETROALIMENTACIÓN
       │
       └──── (si no cumple) ──► vuelve a etapas anteriores
```

### Etapa 1: Reconocimiento de la necesidad

Todo diseño comienza cuando alguien identifica un problema o carencia. La necesidad puede ser:
- Social: mejorar la calidad de vida
- Económica: reducir costos de producción
- Técnica: aumentar rendimiento o seguridad
- Ambiental: reducir impacto o consumo energético

### Etapa 2: Definición del problema

Traducir la necesidad en un enunciado técnico claro. Incluye:
- **Función** que debe cumplir el sistema
- **Restricciones** (presupuesto, materiales disponibles, normas, espacio)
- **Criterios de evaluación** (cómo se medirá el éxito)

Esta etapa es crítica: un problema mal definido lleva a soluciones correctas del problema equivocado.

### Etapa 3: Búsqueda de información

Recopilar datos sobre:
- Soluciones existentes (bibliografía, patentes, competencia)
- Materiales disponibles y sus propiedades
- Normas técnicas aplicables (IRAM, ISO, ASME)
- Procesos de fabricación posibles

### Etapa 4: Generación de alternativas

Fase creativa. Se proponen múltiples soluciones posibles sin descartar ninguna en un primer momento. Herramientas:
- **Brainstorming**: generar ideas sin censura
- **Analogía**: buscar soluciones en otros campos
- **SCAMPER**: Sustituir, Combinar, Adaptar, Modificar, Proponer otro uso, Eliminar, Reordenar

### Etapa 5: Análisis y evaluación

Cada alternativa se analiza con herramientas técnicas y económicas:
- Análisis de resistencia de materiales
- Simulaciones o cálculos de funcionamiento
- Estimación de costos de fabricación y operación
- Análisis de riesgo y seguridad

### Etapa 6: Selección

Se elige la alternativa que mejor satisface los criterios definidos en la etapa 2. Herramienta frecuente: **matriz de evaluación** (pondera cada criterio con un peso relativo).

```
CRITERIO         | PESO | ALT. A | ALT. B | ALT. C
─────────────────|──────|──────── |────── |───────
Costo            |  30% |  8     |  6    |  7
Rendimiento      |  40% |  7     |  9    |  6
Facilidad de mant|  20% |  9     |  7    |  8
Seguridad        |  10% |  8     |  8    |  9
─────────────────|──────|──────── |────── |───────
TOTAL            | 100% |  7.7   |  7.7  |  7.0
```

### Etapa 7: Especificación y comunicación

El diseño seleccionado se documenta en:
- **Planos de ingeniería** (vistas, secciones, detalles, cotas)
- **Memoria técnica** (justificación de decisiones de diseño)
- **Lista de materiales** (BOM — Bill of Materials)
- **Especificaciones de manufactura**

### Etapas 8–9: Implementación y evaluación

Se fabrica el prototipo o el sistema. Se evalúa su funcionamiento real comparándolo con los criterios originales. Si hay desvíos, se itera volviendo a etapas anteriores.

## Restricciones del Diseño

Todo diseño opera dentro de restricciones que limitan el espacio de soluciones posibles:

| Tipo de restricción | Ejemplos |
|---|---|
| Económicas | Presupuesto, costo de materiales, costo de fabricación |
| Técnicas | Propiedades de materiales, capacidad de equipos |
| Normativas | Normas IRAM, ISO, ASME; reglamentos de seguridad |
| Ambientales | Eficiencia energética, emisiones, residuos |
| Temporales | Plazo de entrega |
| Espaciales | Dimensiones máximas disponibles |

Analogía contable: las restricciones son como las normas contables — el contador no puede inventar el método de valuación que quiera; debe elegir dentro del marco normativo. El ingeniero no puede diseñar ignorando las propiedades de los materiales ni las normas de seguridad.

## El Diseño como Actividad Creativa y Técnica

El diseño combina:
- **Creatividad** (imaginar soluciones nuevas)
- **Análisis** (verificar que la solución funciona)
- **Síntesis** (integrar partes en un sistema coherente)
- **Optimización** (mejorar la solución dentro de las restricciones)

No hay una única solución correcta — hay soluciones mejores y peores, y el diseñador debe justificar su elección.

## Diseño Asistido por Computadora (CAD/CAM)

- **CAD** (Computer-Aided Design): software para crear planos y modelos 3D (AutoCAD, SolidWorks, CATIA)
- **CAM** (Computer-Aided Manufacturing): generación de trayectorias de herramienta para máquinas CNC a partir del modelo CAD
- **CAE** (Computer-Aided Engineering): análisis estructural, térmica, fluidodinámica (FEA, CFD)

```
NECESIDAD ──► MODELO CAD ──► ANÁLISIS CAE ──► FABRICACIÓN CAM
                    ↑                              │
                    └──────── iteración ───────────┘
```

## Resumen

| Etapa | Pregunta que responde |
|---|---|
| Reconocimiento de necesidad | ¿Qué problema existe? |
| Definición | ¿Qué debe hacer la solución exactamente? |
| Información | ¿Qué se sabe ya sobre este tipo de problema? |
| Generación de alternativas | ¿Qué soluciones son posibles? |
| Análisis | ¿Cuál funciona mejor, es más segura, más económica? |
| Selección | ¿Cuál es la mejor opción ponderando todos los criterios? |
| Especificación | ¿Cómo se documenta y comunica la solución? |
| Implementación | ¿Cómo se construye? |
| Evaluación | ¿Cumplió los objetivos? ¿Qué mejorar? |

## Errores conceptuales comunes

- Creer que el diseño termina con el plano: la evaluación post-implementación es parte del proceso.
- Ir directo a la primera solución sin generar alternativas: el sesgo de anclaje reduce la calidad del diseño.
- Ignorar las restricciones al generar alternativas: la creatividad debe operar dentro del espacio real de posibilidades.

## Mapa conceptual (ASCII)

```
NECESIDAD
    │
    ▼
DEFINICIÓN DEL PROBLEMA ──► restricciones + criterios
    │
    ▼
INFORMACIÓN ──► normas, materiales, soluciones existentes
    │
    ▼
ALTERNATIVAS ──► creatividad (brainstorming, analogías)
    │
    ▼
ANÁLISIS ──► cálculos, simulaciones, costos
    │
    ▼
SELECCIÓN ──► matriz de evaluación ponderada
    │
    ▼
ESPECIFICACIÓN ──► planos + memoria técnica + BOM
    │
    ▼
IMPLEMENTACIÓN + EVALUACIÓN ──► prototipo → ajustes
```

---
*Fuentes: 1.El Ing y su Profesión.pdf; 1.LA ING. ACTUAL UNIDAD I Y UNIDAD III.pdf; Ing. Mec. I - Plan de Estudio.pdf*
