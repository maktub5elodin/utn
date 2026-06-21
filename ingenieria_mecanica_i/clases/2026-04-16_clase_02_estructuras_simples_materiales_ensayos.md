# Clase 2 — Estructuras simples, grados de libertad y ensayos de materiales

**Fecha:** 16 de abril de 2026  
**Profesor:** Abud  
**Unidades:** UT I — La Ingeniería y la Tecnología / UT II — Proceso de Diseño  
**Continuación de:** Clase 1 (09/04) — sistemas mecánicos, modelo resorte-masa

---

## 1. Retoma: sistemas mecánicos

Abud comenzó recordando el sistema resorte-masa de la clase anterior y planteó la extensión natural: pasar de un sistema con un resorte y una masa a **estructuras simples**, que son la forma más básica de sistema mecánico real.

La pregunta que organiza la clase:  
> ¿Cómo describimos matemáticamente el comportamiento de una estructura?

La respuesta: identificando las **variables** que determinan su respuesta ante una carga.

---

## 2. Descripción matemática de una estructura simple: la viga

### La curva de deflexión

Cuando se aplica una fuerza sobre una viga, esta se deforma: adopta una curva. Esa curva se llama **función de deflexión** y es la variable de salida del sistema. Para poder describirla matemáticamente, hay que identificar qué variables de entrada la determinan.

```
                     F (fuerza aplicada)
                          │
                          ▼
  ══════════════════════════════════════════╗
  ══════════════════════════════════════════╣ ← viga
  ══════════════════════════════════════════╝
                         │
                         ▼  deflexión δ (curva de deformación)
```

### Variables que afectan la deflexión

Abud enumeró cuatro factores:

| Variable | Qué define |
|---|---|
| **Forma de la sección transversal** | Distribución de material alrededor del eje neutro (ej.: sección circular, rectangular, en I) |
| **Tipo de material** | Módulo de elasticidad E — qué tan resistente es a deformarse |
| **Punto de acción de la fuerza** | Dónde se aplica la carga sobre la viga |
| **Forma de fijación o apoyo** | Cómo está restringida la viga en sus extremos |

---

## 3. Formas de fijación o apoyo de una viga

Los apoyos son el **vínculo entre la estructura y el entorno**. Definen qué movimientos están permitidos y cuáles están impedidos. Son uno de los temas centrales de la estática estructural.

Abud utilizó estos apoyos como ejemplo de **representación esquemática** (ver Clase 3): sus símbolos no se parecen al apoyo real, pero representan exactamente su comportamiento mecánico.

### Apoyo de rodillo (o deslizante)

Impide el desplazamiento en una sola dirección (perpendicular a la superficie de apoyo). Permite deslizar en la dirección paralela y permite girar.

```
      ─────── viga ───────
              │
             ( ) ← rueda / rodillo
           ══════
```

Reacción: solo una fuerza perpendicular a la superficie.

### Apoyo articulado (o de pasador)

Impide el desplazamiento en cualquier dirección (vertical y horizontal). Permite girar.

```
      ─────── viga ───────
                  │
                 /│\
                / │ \
               /  ▲  \
             ══════════
```

Reacciones: una fuerza horizontal y una fuerza vertical.

### Empotramiento (apoyo fijo)

Impide absolutamente todo movimiento: ni desplazamiento ni giro.

```
      ══╗
        ║ ─────────────── viga
        ║
      ══╝
```

Reacciones: fuerza horizontal, fuerza vertical y un momento flector.

### Resumen de apoyos

```
TIPO DE APOYO     │ Despl. ⊥ │ Despl. ∥ │ Giro │ Reacciones
──────────────────┼───────────┼───────────┼──────┼───────────
Rodillo           │ IMPEDIDO  │ LIBRE     │ LIBRE│ 1 (fuerza ⊥)
Articulado        │ IMPEDIDO  │ IMPEDIDO  │ LIBRE│ 2 (H + V)
Empotramiento     │ IMPEDIDO  │ IMPEDIDO  │IMPED.│ 3 (H + V + M)
```

---

## 4. Plano de simetría

Un **plano de simetría** es un plano imaginario que divide al sistema en dos mitades especulares. Interpretación teórica: si el sistema, los apoyos y las cargas son todos simétricos respecto a ese plano, la deformación también lo será.

Esto es importante porque permite **simplificar el análisis**: si existe simetría, basta con estudiar la mitad del sistema y extrapolar al otro lado.

```
          F/2          F/2
           │            │
    ───────┼────────────┼───────
           │            │
           │  SIMETRÍA  │
           └────── ║ ───┘
                plano de
                simetría
```

---

## 5. Grados de libertad

Los **grados de libertad (GDL)** son la cantidad de movimientos independientes que puede realizar un cuerpo.

### En el plano (2D)

Un cuerpo libre en el plano puede moverse de tres maneras independientes:

```
         ↑ traslación en Y
         │
    ─────┼─────► traslación en X
         │
       ↺     rotación en Z

GDL en el plano = 3
```

### En el espacio (3D)

Un cuerpo libre en el espacio tiene seis grados de libertad:

```
TRASLACIONES          ROTACIONES
  en X (derecha/izq.)    alrededor de X (cabeceo)
  en Y (arriba/abajo)    alrededor de Y (guiñada)
  en Z (adelante/atrás)  alrededor de Z (balanceo)

GDL en 3D = 6
```

### Relación entre GDL y apoyos: isostático e hiperestático

Cada apoyo **elimina** uno o más grados de libertad (los restringe). La cantidad de restricciones que impone un apoyo coincide con la cantidad de reacciones que genera:

| Apoyo | Restricciones |
|---|---|
| Rodillo | 1 |
| Articulado | 2 |
| Empotramiento | 3 |

**Sistema isostático (estáticamente determinado):**  
Restricciones = GDL → el sistema queda en equilibrio con exactamente la cantidad de apoyos necesaria. La solución de las reacciones es única y se puede calcular con las ecuaciones de equilibrio estático.

```
GDL = 3   →   3 restricciones necesarias (ejemplo: 1 articulado + 1 rodillo)
```

**Sistema hiperestático (estáticamente indeterminado):**  
Restricciones > GDL → hay más apoyos de los estrictamente necesarios. Las ecuaciones de equilibrio solas no alcanzan para determinar todas las reacciones; se necesita incorporar las ecuaciones de deformación del material.

```
GDL = 3   →   4 o más restricciones → hiperestático
```

**Consecuencia sobre el material:**  
Isostático e hiperestático influyen en **cómo se va a deformar el material a través del tiempo**. En un sistema hiperestático, los vínculos redundantes generan esfuerzos internos adicionales incluso sin carga externa (por ejemplo, ante variaciones de temperatura o asientos diferenciales de los apoyos). Esta es una razón central para elegir uno u otro tipo de estructura según la aplicación.

Analogía contable: un sistema isostático es como un asiento contable con exactamente un débito y un crédito — equilibrado y determinado. Uno hiperestático es como tener múltiples partidas que suman al mismo total — hay más de una forma de distribuirlas y hay que usar información adicional (ecuaciones de deformación) para resolver la distribución real.

---

## 6. Simbología y representación

Los símbolos de los apoyos que Abud dibujó en el pizarrón son un ejemplo de **simbología**: convenciones gráficas que representan una parte del sistema. No son el objeto real — son su abstracción funcional.

Este mismo principio aplica a todos los planos técnicos: el plano no es la pieza, **representa** la pieza. Primero se aprende el símbolo y su significado; luego, cuando se ve el símbolo en un plano real, se sabe exactamente qué tipo de vínculo físico representa.

---

## 7. Importancia de los materiales

¿Por qué se estudian los materiales? Porque el comportamiento de la estructura depende de ellos. El ingeniero necesita saber:

- **Resistencia** — cuánta carga soporta antes de fallar
- **Teoría matemática de la elasticidad** — cómo se deforma bajo carga y cómo recupera su forma al retirarla

> Esta materia es estrictamente teórica en este nivel — no se hacen cálculos numéricos; se comprenden los conceptos y las relaciones.

### Lo empírico según Abud

En la clase anterior se estableció la diferencia entre empírico (comprobado) y racional (deducido). Abud agrega aquí una precisión fundamental:

> **Lo empírico tiene que buscar reproducir las condiciones requeridas.**

Es decir: un ensayo experimental no vale si las condiciones del ensayo no representan fielmente las condiciones reales de uso. La validez de lo empírico depende de la fidelidad de la reproducción.

---

## 8. Ensayos de materiales

Para caracterizar un material experimentalmente, se realizan **ensayos** bajo condiciones controladas. Las **solicitaciones** del ingeniero sobre el material son las cargas que este puede aplicar al sistema.

### Solicitación axial (o axil)

La más básica: se aplica una fuerza a lo largo del eje longitudinal de una barra. Puede ser:
- **Tracción** — la fuerza estira la barra (aleja los extremos)
- **Compresión** — la fuerza aplasta la barra (acerca los extremos)

```
TRACCIÓN:
   ←─── F          barra          F ───►
        │══════════════════════════│

COMPRESIÓN:
   ───► F          barra          F ◄───
        │══════════════════════════│
```

### La probeta para ensayo de tracción

Para asegurarse de que la barra **falle mecánicamente en la sección central** (y no en las mordazas de la máquina), la probeta tiene una geometría especial: **los extremos son más gruesos que la parte central**.

```
  ╔═════╗                         ╔═════╗
  ║ (M) ║══─────────────────────══║ (M) ║
  ╚═════╝  ← sección reducida →  ╚═════╝
  mordaza                         mordaza
```

- La sección central es más delgada → mayor esfuerzo con la misma fuerza → falla ahí
- Los extremos gruesos tienen menor esfuerzo → no fallan → la mordaza no daña el resultado

La máquina **muerde** los extremos y **estira** la probeta a velocidad controlada mientras mide la fuerza y el alargamiento.

> Cuando se observa un comportamiento que no tiene explicación racional —por ejemplo, un alargamiento inesperado antes de la fractura— Abud lo llama **fenómeno**: algo que se mide y se registra aunque la teoría aún no lo explique completamente.

---

## 9. Diagrama de tracción

El resultado del ensayo se grafica en un **diagrama tensión-deformación** (o diagrama de tracción):

- **Eje vertical:** tensión `σ = F / A` (fuerza dividida por el área de la sección transversal) — representa la "presión" interna del material
- **Eje horizontal:** deformación unitaria `ε = ΔL / L₀` (incremento de longitud dividido por la longitud original)

```
  σ (tensión)
   │                  x fractura
   │           x (resistencia máxima)
   │        x
   │    ────── zona plástica
   │   /
   │  /  ← zona elástica (PROPORCIONAL)
   │ /      σ = E · ε    (ley de Hooke)
   │/
   └──────────────────────────── ε (deformación)
```

### Concepto clave: proporcionalidad

En la zona inicial del diagrama, la relación entre tensión y deformación es **lineal y proporcional**: al duplicar la fuerza, se duplica el alargamiento. Esta zona se llama **zona elástica** y responde a la Ley de Hooke:

`σ = E · ε`

donde `E` es el **módulo de elasticidad** del material (constante propia de cada material).

Abud destacó este concepto de proporcionalidad como el más importante de la clase: es el fundamento sobre el cual se construye toda la teoría matemática de la elasticidad.

Analogía contable: la zona proporcional es como la relación lineal entre ventas e impuesto a las ventas — mientras la alícuota es constante, duplicar las ventas duplica el impuesto. La proporcionalidad es la condición que permite hacer proyecciones simples. Cuando la relación deja de ser lineal (zona plástica), ya no alcanza con saber la alícuota — hay que conocer la curva completa.

---

## Resumen de la clase

| Concepto | Idea central |
|---|---|
| Curva de deflexión | Respuesta de la viga ante carga; depende de sección, material, punto de carga y apoyo |
| Apoyo de rodillo | 1 restricción; permite deslizar y girar |
| Apoyo articulado | 2 restricciones; permite girar |
| Empotramiento | 3 restricciones; impide todo movimiento |
| Plano de simetría | Simplifica el análisis: basta estudiar la mitad |
| GDL en el plano | 3 (traslación X, traslación Y, rotación Z) |
| GDL en el espacio | 6 (3 traslaciones + 3 rotaciones) |
| Isostático | Restricciones = GDL → solución determinada |
| Hiperestático | Restricciones > GDL → requiere ecuaciones de deformación |
| Lo empírico | Debe reproducir las condiciones reales del sistema |
| Probeta de tracción | Extremos gruesos → falla garantizada en la sección central |
| Diagrama de tracción | Curva tensión vs. deformación del material |
| Proporcionalidad | Zona elástica: `σ = E·ε`; base de la teoría de la elasticidad |

---
*Fuente: apuntes de clase — Prof. Abud, 16/04/2026*
