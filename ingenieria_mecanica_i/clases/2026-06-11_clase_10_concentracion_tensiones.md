# Clase 10 — Concentración de tensiones

**Fecha:** 11 de junio de 2026  
**Profesor:** Abud  
**Nota:** Última clase sobre solicitaciones. La clase del 18/06 cambia de tema.  
**Nota de apunte:** Clase con baja concentración — contenido reconstruido combinando notas fragmentadas con el desarrollo estándar del tema.

---

## 1. Conexión con fatiga (clase anterior)

En la clase 9 vimos que la fatiga ocurre porque los ciclos de tensión van erosionando el material desde dentro, iniciando microfisuras en puntos de irregularidad. Hoy Abud desarrolla exactamente ese mecanismo: ¿por qué las irregularidades son tan peligrosas? La respuesta es la **concentración de tensiones**.

---

## 2. El fenómeno: tensión nominal vs. tensión máxima real

Cuando calculamos la tensión en una barra usando las fórmulas que vimos (σ = N/A para axial, σ = M·c/I para flexión), obtenemos la **tensión nominal** — la tensión "promedio" que habría si la sección fuera uniforme y sin perturbaciones.

Pero si la barra tiene una irregularidad geométrica — un cambio brusco de sección, una ranura, un agujero, una entalla — la tensión real en esa zona es **significativamente mayor** que la nominal.

> **Observación central de Abud:** cuando hay irregularidades, el valor de la tensión máxima es superior al valor de la tensión nominal.

```
  BARRA UNIFORME                   BARRA CON ENTALLA

  →→→→→→→→→→→→→→→→→→→→→→          →→→→→→→→→ ─┐  ┌─ →→→→→→→→→
  (flujo de tensiones              (el flujo se "aprieta"
   uniforme y paralelo)             al pasar por la entalla)
                                         →→→→→─┘  └─→→→→
                                         →→→→→→→→→→→→→→→
                                         →→→→→─┐  ┌─→→→→
                                   σ_max ┤  │  │  │  ├ σ_max
                                         (mucho mayor que σ_nom)
```

El "flujo" de tensiones tiene que pasar por una sección reducida — se concentra ahí, como el agua en un caño angosto.

---

## 3. Lugares donde aparece concentración de tensiones

Abud enumeró los casos típicos:

| Tipo de irregularidad | Ejemplos |
|---|---|
| Cambios angulares de sección | Escalones sin redondeo, esquinas vivas |
| Entrantes y ranuras | Ranuras de chaveta, canales, surcos |
| Orificios | Agujeros para tornillos, ventanas en perfiles |
| Cambios de sección suaves pero bruscos | Reducciones sin radio de transición suficiente |
| Zonas de contacto entre piezas | Ajustes a presión, rodamientos sobre ejes |

---

## 4. El coeficiente teórico de concentración de tensiones — K_t

Para cuantificar cuánto se amplifica la tensión en una irregularidad, se define el **coeficiente teórico de concentración de tensiones** K_t:

```
        σ_max
  K_t = ───────
        σ_nom
```

- `σ_max` = tensión máxima real en la zona de la irregularidad
- `σ_nom` = tensión nominal calculada con las fórmulas clásicas en la sección neta
- K_t ≥ 1 siempre (la tensión real nunca es menor que la nominal)
- K_t = 1 significa sección perfectamente uniforme, sin perturbación

K_t es un **factor puramente geométrico**: depende de la forma de la irregularidad, no del material. Se obtiene de tablas y gráficas experimentales (no hay fórmula cerrada general).

### El radio de acuerdo — r

El **radio de acuerdo** (también llamado radio de entalla o radio de filete) es el radio de curvatura en la transición entre dos secciones de distinto tamaño:

```
  Sección grande          Sección pequeña
  ───────────────╮                       ← radio de acuerdo r
                  ╰────────────────────
                  ↑
                  r (radio de la curvatura de transición)
```

- Radio grande (r grande) → transición suave → K_t pequeño (poca concentración)
- Radio pequeño (r → 0, esquina viva) → K_t muy grande (concentración severa)

Por eso las normas de diseño exigen radios de acuerdo mínimos en todos los cambios de sección de piezas sometidas a fatiga.

---

## 5. De K_t a K_f: la sensibilidad del material a las entallas

K_t es teórico y geométrico. Pero experimentalmente se observó que no todos los materiales responden igual a la misma entalla bajo carga cíclica — aquí aparece la parte **empírica** (sin explicación racional, como marcó Abud).

Se define el **factor de concentración de tensiones para fatiga** K_f:

```
  K_f = 1 + q · (K_t − 1)
```

Aquí aparece el `(K_t − 1)` que el usuario anotó: ese "menos 1" es específico de la formulación para **cargas cíclicas** — en carga estática no aparece de esta forma.

Donde `q` es el **factor de sensibilidad a la entalla** (0 ≤ q ≤ 1):

| Valor de q | Significado |
|---|---|
| q = 0 | Material insensible a la entalla bajo ciclos — K_f = 1 (como si no hubiera concentración) |
| q = 1 | Material totalmente sensible — K_f = K_t (la concentración teórica se transfiere completa) |
| 0 < q < 1 | Caso real: sensibilidad parcial |

q depende del material y del radio de acuerdo. Se obtiene de gráficas empíricas.

---

## 6. El acabado superficial — coeficiente de calidad β

La superficie de la pieza también afecta la fatiga, independientemente de la geometría de sección. Una superficie rugosa contiene microirregularidades que actúan como concentradores de tensión propios.

Se define un **coeficiente de calidad superficial** β (beta, siempre ≤ 1):

| Acabado superficial | Valor de β (aprox.) |
|---|---|
| Pulido de espejo (probeta de laboratorio) | β = 1,0 |
| Rectificado | β ≈ 0,9 |
| Torneado fino | β ≈ 0,8 |
| Torneado común | β ≈ 0,7 |
| Forjado / laminado | β ≈ 0,5 – 0,6 |
| Herrumbroso / corrroído | β < 0,5 |

A peor acabado → menor β → menor límite de fatiga de la pieza real.

---

## 7. σ₋₁: el límite de fatiga y cómo se degrada

### La notación σ₋₁

El subíndice −1 en σ₋₁ indica el **ciclo simétrico** (R = σ_min/σ_max = −1), el mismo del eje de ferrocarril que vimos en clase 9. Es el caso de referencia más usado en los ensayos de fatiga.

`σ₋₁` es el **límite de tensión de fatiga del material** — obtenido sobre probeta pulida, sin entallas, en laboratorio. Es el valor máximo teórico.

### El límite de fatiga de la pieza real

Una pieza real tiene entallas (K_f > 1) y acabado superficial imperfecto (β < 1). Su límite de fatiga efectivo `σ'₋₁` es:

```
       σ₋₁ · β
  σ'₋₁ = ─────────
             K_f
```

Esta es la tensión máxima que puede soportar la pieza real en ciclo simétrico sin fallar por fatiga.

El proceso que Abud enumeró queda así:

```
  σ₋₁                → límite de fatiga del material (laboratorio)
       ↓ aplicar β
  σ₋₁ · β            → corregido por acabado superficial
       ↓ dividir por K_f
  σ'₋₁ = σ₋₁·β/K_f  → límite de fatiga de la pieza que se analiza
       ↓
  Diseño: σ_max en servicio ≤ σ'₋₁
```

### Caracterizar el fenómeno

Abud dijo "caracterizar el fenómeno: darle una identidad, buscar relaciones que me ayuden a construir una especie de comportamiento." Esto describe exactamente el proceso:
- Primero identificar qué tipo de irregularidad hay y su geometría → K_t
- Luego considerar el material y su sensibilidad → q → K_f  
- Luego considerar el acabado → β
- Finalmente: σ'₋₁ = σ₋₁·β/K_f

---

## 8. Caso de momento torsor con concentración

La misma lógica aplica cuando la solicitación es torsional en lugar de flexional. En ese caso:

- `τ_nom` = tensión tangencial nominal en la sección neta: `τ = M_t·ρ/J`
- `K_ts` = coeficiente teórico de concentración para torsión (mismo concepto que K_t, específico para τ)
- `τ_max = K_ts · τ_nom`

El comportamiento empírico — que la concentración bajo carga cíclica no sigue ninguna ley racional — se mantiene: sigue siendo un fenómeno sin explicación teórica completa, manejado con factores empíricos.

---

## 9. Resumen visual: la cadena de degradación del límite de fatiga

```
  MATERIAL PURO
  σ₋₁ (laboratorio, probeta pulida, sin entallas)
       │
       │  × β (acabado superficial < 1)
       ▼
  σ₋₁ · β
       │
       │  ÷ K_f  (donde K_f = 1 + q·(K_t − 1), K_f ≥ 1)
       ▼
  σ'₋₁ = σ₋₁ · β / K_f   ← límite de fatiga de la pieza real
       │
       │  comparar con σ_max en servicio
       ▼
  σ_max ≤ σ'₋₁  →  DISEÑO ACEPTABLE
  σ_max > σ'₋₁  →  FALLA POR FATIGA (en número finito de ciclos)
```

---

## Resumen de la clase

| Concepto | Definición |
|---|---|
| Concentración de tensiones | Amplificación local de la tensión cerca de irregularidades geométricas |
| σ_nom | Tensión calculada con fórmulas clásicas (sin considerar irregularidades) |
| σ_max = K_t · σ_nom | La tensión real en la irregularidad supera siempre a la nominal |
| K_t | Coeficiente teórico de concentración — factor geométrico puro |
| Radio de acuerdo r | Radio de transición entre secciones — mayor r → menor K_t |
| q | Factor de sensibilidad a la entalla (0 a 1) — empírico por material |
| K_f = 1 + q·(K_t − 1) | Factor de concentración para fatiga — el (K_t − 1) aplica solo en carga cíclica |
| β | Coeficiente de calidad superficial — acaba superficial mejor → β más cercano a 1 |
| σ₋₁ | Límite de fatiga del material en ciclo simétrico (R = −1) |
| σ'₋₁ = σ₋₁·β/K_f | Límite de fatiga de la pieza real (degradado por geometría y acabado) |

---
*Fuente: apuntes de clase — Prof. Abud, 11/06/2026. Clase con apunte fragmentado; contenido completado con desarrollo estándar del tema.*
