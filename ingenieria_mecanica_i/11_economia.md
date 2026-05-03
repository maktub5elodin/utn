# Unidad XI — Economía para Ingenieros

## Por qué Economía en Ingeniería

El ingeniero no solo diseña sistemas que funcionen — diseña sistemas que sean **económicamente viables**. Una máquina técnicamente perfecta que cuesta el doble de lo que puede pagarse es una solución fallida.

La definición misma de ingeniería lo confirma: "transformar recursos naturales en formas útiles para el uso del hombre **de manera económica y óptima**". Lo económico es parte constitutiva de la profesión.

Analogía directa: economía es el puente más obvio entre contabilidad e ingeniería. El análisis costo-beneficio, la evaluación de inversiones y el flujo de fondos son herramientas comunes a ambas disciplinas.

## Conceptos Económicos Básicos

### Costo vs. Precio vs. Valor

```
COSTO  = lo que se gasta para producir algo (insumos + mano de obra + overhead)
PRECIO = lo que se cobra al mercado (costo + ganancia esperada)
VALOR  = lo que el cliente percibe que vale (subjetivo, depende del beneficio que obtiene)
```

El ingeniero gestiona el **costo**; la empresa fija el **precio**; el mercado determina el **valor**.

### Costos Fijos y Variables

| Tipo | Descripción | Ejemplo |
|---|---|---|
| **Fijo** | No varía con el volumen de producción | Alquiler de planta, depreciación de equipos, salarios fijos |
| **Variable** | Varía proporcionalmente con la producción | Materia prima, energía, salarios por pieza |
| **Semivariable** | Fijo hasta cierto volumen, luego escala | Supervisión, mantenimiento |

```
Costo Total = Costos Fijos + (Costo Variable Unitario × Unidades Producidas)
```

### Punto de Equilibrio (Break-Even)

El **punto de equilibrio** es el volumen de producción/ventas donde los ingresos igualan a los costos totales (ni ganancia ni pérdida).

```
Ingresos = Precio × Q
Costos = CF + CV × Q

Punto de equilibrio: Precio × Q* = CF + CV × Q*
                     Q* = CF / (Precio - CV)
```

```
INGRESOS ─────────────────────────────────── /
                                        /
                               PUNTO /
                            EQUILIBRIO
                               /
COSTOS TOTALES ───────────────/──────────────
              CF + CV×Q     /
                           /
COSTOS FIJOS ─────────────────────────────── CF
                     │
              Q* (Volumen)
```

Analogía contable: el punto de equilibrio es el equivalente operativo al balance en cero — identifica cuándo la actividad "se paga a sí misma".

## Evaluación Económica de Proyectos

### Flujo de Fondos (Cash Flow)

El flujo de fondos representa los ingresos y egresos de dinero a lo largo del tiempo de vida del proyecto:

```
Período  | 0 (inv.) | 1  | 2  | 3  | 4  | 5  |
─────────|──────────|────|────|────|────|────|
Ingresos |   0      | 500| 500| 500| 500| 500|
Egresos  | -2.000   |-200|-200|-200|-200|-200|
─────────|──────────|────|────|────|────|────|
NETO     | -2.000   | 300| 300| 300| 300| 300|
```

### Valor Actual Neto (VAN / NPV)

El **VAN** descuenta todos los flujos futuros a la tasa de interés de referencia (costo del capital) y los suma:

```
VAN = -Inversión + FN₁/(1+i)¹ + FN₂/(1+i)² + ... + FNₙ/(1+i)ⁿ
```

- **VAN > 0**: el proyecto genera valor; conviene realizarlo.
- **VAN = 0**: el proyecto recupera la inversión con la rentabilidad mínima requerida.
- **VAN < 0**: el proyecto destruye valor; no conviene.

### Tasa Interna de Retorno (TIR / IRR)

La **TIR** es la tasa de descuento que hace que el VAN sea igual a cero. Indica la rentabilidad intrínseca del proyecto.

- Si **TIR > tasa de corte**: el proyecto es rentable.
- Si **TIR < tasa de corte**: no lo es.

### Período de Repago (Payback)

Tiempo necesario para recuperar la inversión inicial:

```
Payback = Inversión / Flujo neto anual (si es constante)
```

Ejemplo: inversión de $2.000, flujo neto anual de $400 → Payback = 5 años.

## Depreciación y Vida Útil

La **depreciación** distribuye el costo de un activo fijo a lo largo de su vida útil. Para el ingeniero es relevante porque:
- Afecta el costo unitario de producción
- Determina cuándo conviene renovar el equipo
- Tiene impacto impositivo

Método lineal (el más simple):
```
Depreciación anual = (Valor inicial - Valor residual) / Vida útil (años)
```

La **vida útil técnica** (cuánto puede funcionar) puede diferir de la **vida útil económica** (cuándo conviene reemplazarlo). El ingeniero evalúa ambas.

## Economía de la Empresa Industrial

### Costos de Producción

```
COSTO DE PRODUCCIÓN
├── Materia prima (MP)
├── Mano de obra directa (MOD)
├── Costos indirectos de fabricación (CIF)
│   ├── Mano de obra indirecta
│   ├── Energía
│   ├── Mantenimiento
│   ├── Depreciación de equipos
│   └── Otros gastos de fábrica
└── COSTO DE MANUFACTURA = MP + MOD + CIF
```

### Precio de Venta

```
Precio de venta = Costo de manufactura + Gastos comerciales + Administración + Ganancia
```

## Análisis de Alternativas de Inversión

El ingeniero frecuentemente debe comparar alternativas de inversión:

| Criterio | Equipo A | Equipo B |
|---|---|---|
| Inversión inicial | $100.000 | $150.000 |
| Costo operativo anual | $20.000 | $12.000 |
| Vida útil | 5 años | 8 años |
| Valor residual | $10.000 | $20.000 |

No alcanza con comparar la inversión inicial — hay que evaluar el costo total durante la vida útil (Costo Anual Equivalente o Valor Actual de Costos).

## La Economía del Mantenimiento

La decisión de mantener vs. reemplazar un equipo es económica:

```
MANTENER si:
  Costo de reparación < Diferencia de valor presente entre continuar y reemplazar

REEMPLAZAR si:
  Costo de mantenimiento creciente supera el beneficio de continuar
```

La **curva de la bañera** muestra la tasa de falla de un equipo a lo largo del tiempo:

```
TASA DE FALLA
    │
    │\                                         /│
    │ \                                       / │
    │  \    FALLAS ALEATORIAS               /  │
    │   \   (desgaste mínimo)              /   │
    │    ───────────────────────────────────    │
    │
   RODAJE      VIDA ÚTIL           ENVEJECIMIENTO
(fallas por    (tasa baja          (fallas por
 defectos)     y constante)         desgaste)
```

## Formación Empresarial del Ingeniero

El plan de estudios de Ingeniería Mecánica incluye materias de formación empresarial porque el ingeniero frecuentemente:
- Gestiona presupuestos de proyectos
- Evalúa la viabilidad económica de inversiones en equipos
- Decide entre alternativas de compra, alquiler o fabricación propia (make or buy)
- Negocia contratos con proveedores y clientes
- Conduce equipos y debe justificar sus decisiones en términos económicos

## Resumen

| Concepto | Fórmula / Descripción |
|---|---|
| Costo total | CF + CV × Q |
| Punto de equilibrio | Q* = CF / (P - CV) |
| VAN | Suma de flujos descontados − Inversión |
| TIR | Tasa donde VAN = 0 |
| Payback | Inversión / Flujo neto anual |
| Depreciación lineal | (Valor inicial − Valor residual) / Vida útil |

## Errores conceptuales comunes

- Elegir la alternativa de menor inversión inicial sin evaluar el costo total de vida útil.
- Confundir costo con precio: el ingeniero controla el costo; el precio lo fija el mercado.
- Ignorar el valor del dinero en el tiempo: $1 hoy vale más que $1 en un año (concepto del VAN).

## Mapa conceptual (ASCII)

```
ECONOMÍA PARA INGENIEROS
         │
         ├── COSTOS ─┬── Fijos / Variables
         │           └── Punto de equilibrio
         │
         ├── EVALUACIÓN DE PROYECTOS ─┬── Flujo de fondos
         │                            ├── VAN
         │                            ├── TIR
         │                            └── Payback
         │
         ├── ACTIVOS FIJOS ──► Depreciación (lineal / acelerada)
         │
         └── DECISIÓN MAKE OR BUY ──► comparar costo propio vs. tercerizar
```

---
*Fuentes: 1.El Ing y su Profesión.pdf; 1.unidad I Ingeniería y Sociedad.pdf; Ing. Mec. I - Plan de Estudio.pdf*
