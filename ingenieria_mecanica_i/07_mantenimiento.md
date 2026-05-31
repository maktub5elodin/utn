# Unidad VII — Mantenimiento

## Definición

El **mantenimiento** es el conjunto de actividades técnicas y administrativas cuyo objetivo es conservar un bien o restablecerlo a un estado en que pueda realizar la función requerida, con el nivel de disponibilidad y confiabilidad esperados, al menor costo posible.

Analogía contable: el mantenimiento equivale a la **auditoría interna continua** de una empresa. No se espera a que aparezca un error grave en el balance (falla catastrófica); se revisan periódicamente los registros (equipos) para detectar desvíos antes de que escalen.

## Objetivos del Mantenimiento

- **Disponibilidad**: que el equipo esté operativo cuando se lo necesita
- **Confiabilidad**: que funcione correctamente durante su operación
- **Seguridad**: que no genere riesgos para personas ni instalaciones
- **Vida útil**: prolongar el ciclo de vida del equipo
- **Costo óptimo**: mínimo costo total (mantenimiento + fallas + lucro cesante)

```
OBJETIVO CENTRAL:
MAX (Disponibilidad × Confiabilidad)
con
MIN (Costo total de mantenimiento)
```

## Tipos de Mantenimiento

### 1. Mantenimiento Correctivo

Intervención **después** de que ocurre la falla. El equipo se repara para restablecer su función.

```
EQUIPO OPERA → FALLA → DETECCIÓN → DIAGNÓSTICO → REPARACIÓN → OPERA
```

- **Correctivo no planificado** (emergencia): la falla es inesperada; alta urgencia, mayor costo.
- **Correctivo planificado** (diferido): la falla se detecta pero se acepta seguir operando hasta la próxima parada programada.

Cuándo usarlo: equipos de bajo costo, duplicados, o donde la falla no afecta la seguridad ni la producción crítica.

### 2. Mantenimiento Preventivo

Intervención **antes** de que ocurra la falla, según un plan fijo de tiempo o uso.

```
PLAN (calendario / horas de uso)
       │
       ▼
INTERVENCIÓN PROGRAMADA (inspección, lubricación, reemplazo de piezas)
       │
       ▼
EQUIPO OPERA (en estado controlado)
```

Tipos de intervalos:
- **Tiempo fijo**: cada 30 días, cada 6 meses, etc.
- **Uso acumulado**: cada 500 horas de funcionamiento, cada 10.000 km.

Ventaja: evita fallas imprevistas y sus consecuencias.
Limitación: puede reemplazar piezas que aún tienen vida útil (desperdicio) o no detectar fallas que se desarrollan entre inspecciones.

### 3. Mantenimiento Predictivo

Monitoreo **continuo o periódico** del estado real del equipo para intervenir solo cuando los parámetros se acercan a valores críticos.

```
MONITOREO CONTINUO DE PARÁMETROS
(vibración, temperatura, presión, ruido, análisis de aceite)
       │
       ▼
¿PARÁMETRO FUERA DE RANGO?
   NO → sigue operando
   SÍ → programar intervención antes de la falla
```

Técnicas de diagnóstico:
- **Análisis de vibraciones**: detecta desbalanceo, desalineación, desgaste de rodamientos
- **Termografía infrarroja**: puntos calientes en conexiones eléctricas, fricciones
- **Análisis de aceite**: partículas metálicas indican desgaste interno
- **Ultrasonido**: fugas, fisuras, rodamientos

Ventaja: máximo aprovechamiento de la vida útil, mínimas intervenciones innecesarias.
Limitación: requiere instrumentación y personal especializado.

### 4. Mantenimiento Mejorativo (Proactivo)

Modifica el diseño del equipo o el proceso para eliminar la causa raíz de fallas recurrentes. No solo repara — **mejora**.

Ejemplo: si una bomba falla repetidamente por cavitación, el correctivo la repara; el mejorativo rediseña el sistema hidráulico para que no cavite.

## Comparación entre Tipos

| Criterio | Correctivo | Preventivo | Predictivo | Mejorativo |
|---|---|---|---|---|
| Cuándo actúa | Después de la falla | Según plan fijo | Según estado real | Modifica el sistema |
| Planificación | Nula (emergencia) o baja | Alta | Alta | Alta |
| Costo de intervención | Alto (urgencia) | Medio | Medio-alto (instrumental) | Alto (rediseño) |
| Riesgo de falla | Alto | Medio | Bajo | Muy bajo |
| Aprovechamiento de vida útil | 100% (hasta rotura) | Bajo | Alto | Variable |
| Aplicación típica | Equipos de bajo impacto | Equipos estándar | Equipos críticos | Fallas recurrentes |

Analogía contable: correctivo = registrar el error cuando ya cerró el ejercicio; preventivo = conciliación mensual; predictivo = software de alerta de inconsistencias en tiempo real; mejorativo = rediseñar el plan de cuentas para que el error no pueda ocurrir.

## Indicadores de Mantenimiento

### MTBF — Tiempo Medio Entre Fallas

```
MTBF = Tiempo total de operación / Número de fallas
```

Mide la **confiabilidad**. Mayor MTBF = equipo más confiable.

Ejemplo: una bomba operó 2.000 h y falló 4 veces → MTBF = 500 h.

### MTTR — Tiempo Medio de Reparación

```
MTTR = Tiempo total de reparación / Número de fallas
```

Mide la **mantenibilidad**. Menor MTTR = reparación más rápida.

### Disponibilidad

```
Disponibilidad = MTBF / (MTBF + MTTR)
```

Expresa qué porcentaje del tiempo el equipo está operativo.

Ejemplo:
- MTBF = 500 h, MTTR = 20 h
- Disponibilidad = 500 / (500 + 20) = 0,962 = 96,2%

```
MTBF grande  ──►  POCAS fallas  ──►  ALTA confiabilidad
MTTR pequeño ──►  REPARACIÓN rápida ──►  ALTA disponibilidad
```

### Costo Total de Mantenimiento

```
Costo total = Costo directo + Costo de falla
            = (mano de obra + repuestos + instrumentación)
            + (lucro cesante + daños secundarios + seguridad)
```

El objetivo es minimizar el costo total, no solo el costo de mantenimiento. Gastar más en preventivo/predictivo puede reducir drásticamente el lucro cesante.

## Organización del Mantenimiento

### Estructura centralizada

Un departamento único de mantenimiento atiende toda la planta.

```
GERENCIA DE PLANTA
       │
DEPARTAMENTO DE MANTENIMIENTO
   ├─ Mecánico
   ├─ Eléctrico
   └─ Instrumentación
```

Ventaja: especialización y uso eficiente de recursos.
Limitación: puede ser lento para responder a emergencias en áreas remotas.

### Estructura descentralizada

Cada sector productivo tiene su propio equipo de mantenimiento.

Ventaja: respuesta rápida, conocimiento profundo del sector.
Limitación: duplicación de recursos; menor especialización técnica.

### Estructura mixta

Mantenimiento especializado centralizado + operadores capacitados para tareas básicas en cada sector.

## Estrategia TPM (Mantenimiento Productivo Total)

El Mantenimiento Productivo Total involucra a todos los empleados, no solo al personal de mantenimiento. Los operadores realizan mantenimiento autónomo básico (limpieza, lubricación, ajustes menores) y detectan anomalías temprano.

```
PILARES DEL TPM
├─ Mantenimiento autónomo (operadores)
├─ Mantenimiento planificado (mantenimiento)
├─ Mejora enfocada (ingeniería)
├─ Mantenimiento de la calidad
└─ Formación y capacitación
```

## Mantenimiento en la Industria Petrolera (caso Argentina)

Una planta de refinación opera 365 días al año sin parar. El ingeniero mecánico tiene rol clave:
- Cuidado de equipos bajo alta presión y temperatura
- Mantenimiento de equipos en contacto con líquidos corrosivos e inflamables
- Cualquier falla puede derivar en riesgo de seguridad personal o consecuencias ambientales
- La demora en una reparación puede generar desabastecimiento nacional

## Resumen

| Concepto | Definición |
|---|---|
| Mantenimiento correctivo | Intervención post-falla |
| Mantenimiento preventivo | Intervención según plan fijo (tiempo/uso) |
| Mantenimiento predictivo | Intervención según estado real (monitoreo) |
| Mantenimiento mejorativo | Modifica el sistema para eliminar la causa raíz |
| MTBF | Tiempo medio entre fallas (confiabilidad) |
| MTTR | Tiempo medio de reparación (mantenibilidad) |
| Disponibilidad | MTBF / (MTBF + MTTR) |

## Errores conceptuales comunes

- Creer que más mantenimiento preventivo siempre es mejor: hay un punto óptimo donde el costo total es mínimo.
- Confundir disponibilidad con confiabilidad: disponibilidad incluye la velocidad de reparación; confiabilidad solo mide cada cuánto falla.
- Pensar que el predictivo reemplaza al preventivo: son complementarios; el predictivo reduce intervenciones innecesarias, no las elimina todas.

## Mapa conceptual (ASCII)

```
MANTENIMIENTO
      │
      ├── OBJETIVOS ──► disponibilidad + confiabilidad + seguridad + costo óptimo
      │
      ├── TIPOS ─┬── Correctivo (post-falla)
      │          ├── Preventivo (plan fijo)
      │          ├── Predictivo (monitoreo de estado)
      │          └── Mejorativo (elimina causa raíz)
      │
      ├── INDICADORES ─┬── MTBF (confiabilidad)
      │                ├── MTTR (mantenibilidad)
      │                └── Disponibilidad = MTBF/(MTBF+MTTR)
      │
      └── ORGANIZACIÓN ─┬── Centralizada
                        ├── Descentralizada
                        └── Mixta / TPM
```

---
*Fuentes: Mantenimiento[1].pdf; 1.unidad I Ingeniería y Sociedad.pdf (contexto industria)*
