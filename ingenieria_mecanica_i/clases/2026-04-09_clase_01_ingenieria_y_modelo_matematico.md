# Clase 1 — Ingeniería interdisciplinaria y modelo matemático de un sistema

**Fecha:** 9 de abril de 2026  
**Profesor:** Abud  
**Unidad:** UT I — La Ingeniería y la Tecnología

---

## 1. La ingeniería es interdisciplinaria

La ingeniería no pertenece a una sola disciplina: toma conocimientos y habilidades de matemática, física, química, ciencias de materiales, economía y ciencias sociales, y los integra para resolver problemas concretos.

Punto central que marcó Abud: **la ingeniería NO es ciencia pura**. Nace en la ciencia — la usa como base — pero la adapta. La ciencia busca entender cómo funciona el mundo; la ingeniería toma ese entendimiento y lo convierte en algo útil, fabricable, económicamente viable.

```
CIENCIA PURA          INGENIERÍA
──────────────────────────────────────────────────
Describe la realidad   Transforma la realidad
Busca la verdad        Busca la solución
Resultados teóricos    Resultados aplicados
Laboratorio / papers   Diseño / producto / sistema
Libre de restricciones Sujeta a costos y normas
```

Analogía contable: la contabilidad pura (teoría contable) describe cómo debería registrarse la realidad económica; la contaduría en ejercicio profesional adapta esa teoría al marco normativo, al cliente y a las restricciones prácticas. Misma relación entre ciencia e ingeniería.

---

## 2. Formulación del modelo matemático de un sistema

Para analizar cualquier sistema mecánico, el ingeniero primero construye un **modelo matemático** que lo represente. Abud describió tres pasos para formular ese modelo:

### Paso 1 — Identificar variables y parámetros

Las **variables** son las magnitudes que cambian con el tiempo (posición, velocidad, temperatura).  
Los **parámetros** son las constantes propias del sistema (masa, rigidez del resorte, coeficiente de amortiguamiento).

```
PARÁMETROS (fijos del sistema)
    masa m
    rigidez k
    amortiguamiento c
          │
          ▼
SISTEMA  ──►  VARIABLES (evolucionan en el tiempo)
                  posición x(t)
                  velocidad ẋ(t)
                  aceleración ẍ(t)
```

### Paso 2 — Establecer hipótesis (suposiciones razonables)

No se puede modelar la realidad con exactitud total. Se asumen condiciones que simplifican el análisis sin perder lo esencial:

- El resorte se comporta linealmente (Ley de Hooke: `F = k·x`)
- La masa es rígida (no se deforma)
- El sistema es homogéneo y continuo

Las hipótesis **no son invenciones arbitrarias**: incluyen las **leyes empíricas** que aplican al sistema — leyes que ya fueron verificadas experimentalmente para ese tipo de fenómeno.

### Paso 3 — Distinción empírico vs. racional

Abud marcó esta diferencia:

| Tipo de ley | Origen | Validez |
|---|---|---|
| **Empírica** | Observación y experimento | Comprobada — se sabe que funciona porque se midió |
| **Racional** | Deducción lógica desde primeros principios | Lógica — se deduce que debe funcionar porque se razona |

Una ley empírica (ej.: `F = k·x` de Hooke) es *comprobada*: surgió de medir resortes reales.  
Una ley racional (ej.: Segunda Ley de Newton `F = m·a`) es *lógica*: se puede deducir desde principios más fundamentales.

En la práctica, el modelo matemático mezcla ambas: parte de relaciones deducidas (racionales) y las complementa con constantes obtenidas experimentalmente (empíricas).

---

## 3. Ejemplo: sistema mecánico resorte-masa

### ¿Qué es un sistema?

Un solo elemento aislado — por ejemplo, **solo el resorte** — no constituye un sistema por sí mismo: es simplemente un componente.  
**Dos o más elementos en interacción ya forman un sistema.**  
El ejemplo de clase: resorte (k) + masa (m) → sistema resorte-masa.

```
     techo
      |||
       │
     [===] ← resorte (rigidez k)
       │
      [█] ← masa m
       │
       ▼ x(t): desplazamiento desde la posición de equilibrio
```

### Ecuación de movimiento

Aplicando la Segunda Ley de Newton:

`F = m·a`  →  `F = m·ẍ`

Sumando las fuerzas que actúan sobre la masa:
- Fuerza del resorte: `-k·x` (restauradora, opuesta al desplazamiento)
- Fuerza de amortiguamiento: `-c·ẋ` (opuesta a la velocidad)
- Fuerza externa: `F(t)` (excitación del sistema)

La ecuación diferencial del sistema es:

`m·ẍ + c·ẋ + k·x = F(t)`

La solución de esta ecuación —sin fuerza externa (`F(t) = 0`)— es una **función sinusoidal amortiguada**: la masa oscila y esa oscilación se va atenuando con el tiempo.

### Los tres casos de amortiguamiento

El comportamiento depende de la relación entre el amortiguamiento real `c` y el amortiguamiento crítico `c_c`:

```
  x(t)
   │
   │  SUBAMORTIGUADO (c < c_c)
   │  ╭─╮   ╭─╮
   │ ╭╯  ╰─╯  ╰─╮          oscila y se atenúa
   │─────────────────── t
   │
   │  CRÍTICAMENTE AMORTIGUADO (c = c_c)
   │  ╭╮
   │ ╭╯ ╰──────────────     vuelve al equilibrio lo más rápido
   │─────────────────── t   posible sin oscilar
   │
   │  SOBREAMORTIGUADO (c > c_c)
   │  ╭╮
   │ ╭╯   ╰──────────────   vuelve al equilibrio lentamente
   │─────────────────── t   sin oscilar
```

| Caso | Condición | Respuesta |
|---|---|---|
| **Subamortiguado** | `c < c_c` | Oscila con amplitud decreciente — resorte de puerta que rebota |
| **Críticamente amortiguado** | `c = c_c` | Retorno más rápido sin oscilación — amortiguador de puerta de hospital |
| **Sobreamortiguado** | `c > c_c` | Retorno lento sin oscilación — puerta con pistón muy pesado |

Analogía contable: los tres casos son como tres políticas de cobranza ante una deuda. El subamortiguado es el cliente que paga en cuotas con rebotes (oscila). El críticamente amortiguado es el que salda exactamente al vencimiento. El sobreamortiguado es el que paga, pero lleva mucho tiempo.

---

## Resumen de la clase

| Concepto | Idea central |
|---|---|
| Ingeniería | Interdisciplinaria; nace en la ciencia pero la adapta — no es ciencia pura |
| Modelo matemático | Variables + hipótesis + leyes empíricas |
| Empírico vs. racional | Comprobado por experimento vs. deducido por lógica |
| Sistema | 2 o más elementos en interacción; 1 elemento solo no es sistema |
| Resorte-masa | `m·ẍ + c·ẋ + k·x = F(t)` → respuesta sinusoidal |
| Amortiguamiento | Tres regímenes: sub / crítico / sobre |

> **Continúa en Clase 2 (16/04):** el sistema resorte-masa se extiende a estructuras simples (vigas). Se introducen los tipos de apoyo, los grados de libertad, isostático/hiperestático y el diagrama de tracción de materiales.

---
*Fuente: apuntes de clase — Prof. Abud, 09/04/2026*
