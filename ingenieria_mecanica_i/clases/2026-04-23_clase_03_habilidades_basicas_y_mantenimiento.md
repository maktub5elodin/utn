# Clase 3 — Habilidades básicas del ingeniero e introducción al mantenimiento

**Fecha:** 23 de abril de 2026  
**Profesor:** Abud  
**Unidades:** UT III — La Ingeniería como Actividad Profesional / UT VII — Mantenimiento  
**Nota:** La clase 2 (16/04) estuvo dedicada al proyecto de mecánica rotacional — no se toman apuntes de clase para esa sesión.

---

## 1. Habilidades básicas del ingeniero

Abud presentó tres habilidades que todo ingeniero debe dominar independientemente de su especialidad:

```
HABILIDADES BÁSICAS
├─ Representación      ← plasmar la idea
├─ Resolución de problemas ← dar solución a una necesidad no satisfecha
└─ Optimización        ← elegir la mejor solución posible
```

---

### 1.1 Representación

Representar es **plasmar una idea de modo que otros puedan entenderla, reproducirla y construirla**. No alcanza con tener la solución en la cabeza — tiene que ser comunicable.

Abud distinguió cuatro formas de representación:

#### a) Icónica
Imágenes que **se parecen al objeto**: bosquejo, plano, mapa.  
Captura la forma, las dimensiones, la geometría visible.

```
Bosquejo rápido  ──►  Croquis  ──►  Plano técnico (normalizado)
     (idea)              (forma)          (producción)
```

#### b) Esquemática
Usa **símbolos convencionales** que no se parecen al objeto pero representan su función o su comportamiento estructural.

Abud dibujó en el pizarrón **apoyos de estabilidad** como ejemplo paradigmático de representación esquemática (los tres tipos fueron introducidos formalmente en Clase 2 — ver 16/04):

```
  APOYO DE RODILLO        APOYO ARTICULADO        EMPOTRAMIENTO
  (permite deslizar        (fijo en posición,       (fijo en posición
   en una dirección)        permite girar)            y orientación)

       ─┬─                     ─┬─                     ══╗
        │                       │                         ║
       ( )                     /▲\                        ║
      ══════                  ══════                      ║
```

Estos símbolos son la base del análisis estructural estático: el mismo viga real se representa con estos íconos abstractos para poder plantear ecuaciones de equilibrio. Conexión directa con **Sistemas de Representación**: las normas IRAM regulan exactamente estos símbolos para planos técnicos y estructurales.

#### c) Gráfica
Representación mediante **curvas, diagramas cartesianos, histogramas**: transmite relaciones funcionales entre variables (posición vs. tiempo, tensión vs. deformación, etc.). El gráfico no muestra el objeto — muestra su comportamiento.

#### d) Simulación / Prototipo
Construir o modelar el sistema antes de fabricarlo para observar su comportamiento real o virtual. El prototipo es la representación más completa — ya es casi el objeto.

#### Modelo analógico

Abud introdujo un caso especial: el **modelo analógico**.  
Un modelo analógico es comparable y equivalente al sistema real, pero **usa variables de diferente naturaleza** a las variables que se quieren estudiar.

Ejemplo clásico: un circuito eléctrico RC es un modelo analógico de un sistema térmico — la tensión representa temperatura, la corriente representa flujo de calor, la resistencia eléctrica representa resistencia térmica. Se estudia el circuito (más fácil de medir) para entender el comportamiento térmico.

```
SISTEMA REAL          MODELO ANALÓGICO        VARIABLE ANÁLOGA
─────────────────────────────────────────────────────────────
Sistema mecánico   ↔  Circuito eléctrico   Fuerza ↔ Tensión
  (masa-resorte)                            Velocidad ↔ Corriente
                                            Masa ↔ Inductancia
                                            Amortiguamiento ↔ Resistencia

Sistema térmico    ↔  Circuito RC          Temperatura ↔ Tensión
                                            Flujo de calor ↔ Corriente
```

Analogía contable: usar la variación de caja como indicador adelantado de la rentabilidad futura — son variables de diferente naturaleza que guardan una relación analógica conocida.

---

### 1.2 Resolución de problemas

Para Abud, la resolución de problemas en ingeniería apunta específicamente a **brindar una solución a un problema existente no satisfecho en la sociedad**.

El punto central es que el problema ya existe en la realidad — el ingeniero no lo inventa. Su rol es detectarlo, formularlo con precisión y proponer una solución técnicamente viable y económicamente sustentable.

```
NECESIDAD SOCIAL NO SATISFECHA
           │
           ▼
   FORMULACIÓN DEL PROBLEMA
   (definir qué hay que resolver)
           │
           ▼
   BÚSQUEDA DE SOLUCIONES
   (creatividad + base científica)
           │
           ▼
   EVALUACIÓN Y SELECCIÓN
   (optimización → ver 1.3)
           │
           ▼
   IMPLEMENTACIÓN DE LA SOLUCIÓN
```

Analogía contable: detectar que una empresa no tiene sistema de control interno (problema existente no satisfecho) y proponer el diseño e implementación del mismo — es exactamente la misma estructura.

---

### 1.3 Optimización

Optimizar es **encontrar la mejor solución posible dentro de las restricciones existentes** (costo, tiempo, materiales, normas de seguridad, condiciones del cliente).

El ingeniero no busca la solución perfecta — busca la **óptima dado el contexto**.

#### Matriz de decisión (según Abud)

Abud presentó la **matriz de decisión** como herramienta de optimización. Según él, una matriz de decisión requiere entre **15 y 20 factores** para ser válida.

Estructura de la matriz:

```
                 │ Factor 1 │ Factor 2 │ ... │ Factor N │  TOTAL
─────────────────┼──────────┼──────────┼─────┼──────────┼────────
 Solución A      │  peso×n  │  peso×n  │     │  peso×n  │   Σ
 Solución B      │  peso×n  │  peso×n  │     │  peso×n  │   Σ
 Solución C      │  peso×n  │  peso×n  │     │  peso×n  │   Σ
```

Cada factor tiene un **peso** (importancia relativa) y cada solución recibe una **nota** por factor. La solución con mayor puntaje ponderado es la óptima.

> En la práctica, esta herramienta es equivalente a un **scorecard ponderado**: se asigna peso relativo a cada criterio, se puntúan las alternativas, y se elige la de mayor score total. La terminología puede variar según el autor; lo relevante para la materia es el nombre "matriz de decisión" y la estructura de 15–20 factores que usa Abud.

Analogía contable: el análisis multicriterio para seleccionar un sistema contable (ERP) — costo, soporte, integración, curva de aprendizaje, escalabilidad, etc. — es exactamente una matriz de decisión aplicada.

---

## 2. Mantenimiento — introducción (tema dejado a medias)

Hacia el final de la clase, Abud abrió el tema de Mantenimiento, que quedó incompleto para la próxima clase.

### Definición central

> El mantenimiento es **darle al sistema la continuidad en la prestación para la cual fue creado**.

El énfasis está en la **función**: el objetivo no es que el equipo exista físicamente, sino que pueda seguir cumpliendo su rol.

### Marco conceptual

Abud marcó la importancia de definir un **marco conceptual** antes de entrar en los tipos y técnicas. Ese marco parte de una idea precisa:

> El mantenimiento es el **estado de conservación adecuado de los medios físicos involucrados** en el sistema.

```
SISTEMA
   │
   └─ medios físicos (equipos, máquinas, instalaciones)
              │
              └─ deben conservarse en estado adecuado
                        │
                        └─ para sostener la función del sistema
```

El mantenimiento no es reparar lo que se rompió — es gestionar que los medios físicos permanezcan aptos para su función.

### Gestión del mantenimiento

Abud cerró la clase mencionando que la gestión del mantenimiento incluye:

- **Políticas de reemplazo** — cuándo conviene reemplazar un componente antes de que falle vs. esperar la falla
- **Niveles de calidad** — definir qué estándar de funcionamiento es aceptable para cada equipo

#### Importancia económica

El mantenimiento tiene impacto económico directo y significativo:
- Un equipo fuera de servicio genera **lucro cesante** (producción no realizada)
- El reemplazo no planificado de piezas es más caro que el reemplazo programado
- Una política de mantenimiento bien diseñada reduce costos totales aunque aumente el gasto directo en mantenimiento

```
Costo total = Costo de mantenimiento + Costo de falla (lucro cesante + daños)
                      │                          │
              sube si mantenemos más      baja si mantenemos más
                      │                          │
                      └─────── PUNTO ÓPTIMO ─────┘
                         (minimiza la suma total)
```

Analogía contable: provisión para incobrables — gastar en auditoría y control (mantenimiento) reduce las pérdidas por deudas incobrables (fallas). Hay un punto óptimo donde el costo de control iguala el beneficio de la reducción de pérdidas.

---

## Resumen de la clase

| Habilidad | Concepto central |
|---|---|
| Representación icónica | Bosquejo, plano, mapa — se parece al objeto |
| Representación esquemática | Símbolos funcionales (ej.: apoyos de estabilidad) |
| Representación gráfica | Diagramas cartesianos, curvas de comportamiento |
| Representación por simulación | Prototipo — la representación más completa |
| Modelo analógico | Usa variables de distinta naturaleza para estudiar el sistema |
| Resolución de problemas | Solución a problema existente no satisfecho socialmente |
| Optimización | Mejor solución posible dado el contexto; herramienta: matriz de decisión (15–20 factores) |
| Mantenimiento — definición | Continuidad del sistema en la función para la cual fue creado |
| Mantenimiento — marco | Estado de conservación adecuado de los medios físicos |
| Gestión del mantenimiento | Políticas de reemplazo, niveles de calidad, importancia económica |

---
*Fuente: apuntes de clase — Prof. Abud, 23/04/2026*
