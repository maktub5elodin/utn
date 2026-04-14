# Sistemas de Representación — Materiales y Normas IRAM

## 1. ¿Qué es IRAM?

IRAM (Instituto de Racionalización Argentina de Materiales) es el organismo argentino de normalización, equivalente a ISO en el plano internacional. Sus normas de dibujo técnico adaptan la ISO al contexto local.

> **Analogía contable:** Las normas IRAM en dibujo técnico cumplen el mismo rol que las NCP (Normas Contables Profesionales) en contabilidad: establecen un lenguaje universal que garantiza que todos interpreten el mismo plano de la misma manera.

En esta materia se aplican principalmente:
- **IRAM 4502** — Tipos de líneas y sus aplicaciones
- **IRAM 4503** — Caligrafía técnica
- **IRAM 4504** — Acotación

---

## 2. Materiales requeridos

### Para láminas (hoja lisa)

| Material | Especificación |
|---|---|
| Hoja A4 lisa | 210 × 297 mm, blanca |
| Lápiz duro | HB o H — para trazos finos (0,25 mm) |
| Lápiz blando | B o 2B — para trazos gruesos (0,5 mm) |
| Regla graduada | 30 cm mínimo |
| Escuadra 45° | par de escuadras |
| Escuadra 60°/30° | par de escuadras |
| Compás | con porta-lápiz |
| Curvigrafo (opcional) | para trazos curvos en TP 07 |
| Borrador | suave, que no manche |
| Portaminas (opcional) | 0,5 mm y 0,3 mm como alternativa a lápiz |

### Para croquis (hoja cuadriculada)

| Material | Especificación |
|---|---|
| Hoja A4 cuadriculada | cuadrícula 5 mm recomendada |
| Lápiz duro | trazos finos a mano alzada |
| Lápiz blando | trazos gruesos a mano alzada |
| Regla | solo para el rótulo |

### Observación sobre los lápices

La diferencia entre trazo grueso y fino no es de presión, sino de lápiz:
- **Trazo grueso (0,5 mm):** lápiz blando (B, 2B)
- **Trazo fino (0,25 mm):** lápiz duro (H, 2H)

Intentar hacer ambos con el mismo lápiz cambiando la presión produce resultados inconsistentes y es causa de desaprobación.

---

## 3. Tipos de líneas IRAM (norma IRAM 4502)

### 3.1 Tabla de tipos

| Tipo IRAM | Denominación | Descripción | Grosores disponibles |
|---|---|---|---|
| **01** | Continua | Línea ininterrumpida | Gruesa (0,5 mm) y Fina (0,25 mm) |
| **02** | Discontinua corta | Segmentos 6 mm, espacios 1,5 mm | Gruesa y Fina |
| **03** | Discontinua larga | Segmentos largos, espacios más largos | Gruesa y Fina |
| **04** | Raya larga y punto | Raya 12 mm, punto/espacio 1,5 mm | Gruesa y Fina |
| **05** | Raya larga y doble punto | Igual que 04 pero con dos puntos | Gruesa y Fina |
| **06** | Raya larga y triple punto | Igual que 04 pero con tres puntos | Gruesa y Fina |

**En esta materia se usan:** tipos 01, 02 y 04.

### 3.2 Representación esquemática

```
Tipo 01 gruesa: ─────────────────────────────────────  (0,5 mm)
Tipo 01 fina:   ─────────────────────────────────────  (0,25 mm)

Tipo 02 gruesa: ──────  ──────  ──────  ──────  ──────  (seg 6mm, esp 1,5mm)
Tipo 02 fina:   ──────  ──────  ──────  ──────  ──────

Tipo 04 gruesa: ────────── · ────────── · ──────────    (raya 12mm, pto 1,5mm)
Tipo 04 fina:   ────────── · ────────── · ──────────
```

### 3.3 Aplicaciones de cada línea (IRAM 4502-30 y 4502-40)

#### Línea fina continua (01.1) — 0,25 mm

Se usa para todo lo que "acompaña" al dibujo pero no es el objeto en sí:

- Líneas de cota
- Líneas auxiliares de cota
- Indicaciones y referencias
- Rayado de secciones y cortes
- Eje corto de circunferencias de centro
- Núcleo del filete de rosca
- Diagonales en vistas de superficies planas
- Terminaciones de vistas parciales (zigzag a mano alzada)

#### Línea gruesa continua (01.2) — 0,5 mm

Las aristas y contornos que se ven directamente:

- Aristas visibles del objeto
- Contornos visibles del objeto
- Cresta del filete de rosca
- Límite de zona roscada
- Flechas indicadoras de cortes y secciones

#### Línea fina discontinua (02.1) — 0,25 mm

Lo que existe pero no se ve desde el punto de vista elegido:

- Aristas ocultas (detrás de otra cara)
- Contornos ocultos
- (Referencia normativa: IRAM 4502-30)

#### Línea fina raya-punto (04.1) — 0,25 mm

Elementos de referencia geométrica, no físicos:

- Ejes de simetría
- Ejes de revolución
- Circunferencia primitiva de engranajes
- Circunferencia de centros de agujeros dispuestos en círculo

#### Línea gruesa raya-punto (04.2) — 0,5 mm

Indicaciones especiales de proceso o posición:

- Zonas de tratamiento superficial especial
- Posición de los planos de corte (IRAM 4502-40)

### 3.4 Tabla resumen de aplicaciones

| Línea | Tipo | Grosor | Uso principal |
|---|---|---|---|
| Contorno visible | 01.2 | Gruesa | Aristas y superficies visibles |
| Cota y auxiliar | 01.1 | Fina | Acotación completa |
| Oculta | 02.1 | Fina | Aristas no visibles |
| Eje / simetría | 04.1 | Fina | Geometría de referencia |
| Tratamiento / corte | 04.2 | Gruesa | Indicaciones de proceso |

---

## 4. Caligrafía técnica IRAM tipo A

### 4.1 Concepto

La caligrafía técnica normalizada garantiza que los números y letras en un plano sean legibles y reproducibles. La norma IRAM 4503 define el **tipo A** como caligrafía vertical (sin inclinación) con parámetros proporcionales a la altura de letra `h`.

> **Analogía contable:** Como la tipografía en un balance oficial — no es un tema estético, es una norma de comunicación. Un plano con caligrafía libre puede generar lecturas ambiguas (¿es un 1 o un 7?), igual que cifras mal escritas en un libro contable.

### 4.2 Tabla 1 — Medidas de las letras tipo A (en milímetros)

| Característica | Símbolo | Múltiplo de h | h=1,8 | h=2,5 | h=3,5 | **h=5** | h=7 | h=10 | h=14 | h=20 |
|---|---|---|---|---|---|---|---|---|---|---|
| Altura de letra | h | (14/14)h | 1,8 | 2,5 | 3,5 | **5** | 7 | 10 | 14 | 20 |
| Altura de minúscula | c₁ | (10/14)h | 1,3 | 1,8 | 2,5 | **3,5** | 5 | 7 | 10 | 14 |
| Saliente inferior de minúscula | c₂ | (4/14)h | 0,52 | 0,72 | 1 | **1,4** | 2 | 2,8 | 4 | 5,6 |
| Prolongación superior de minúscula | c₃ | (4/14)h | 0,52 | 0,72 | 1 | **1,4** | 2 | 2,8 | 4 | 5,6 |
| Banda para signos diacríticos | f | (5/14)h | 0,65 | 0,9 | 1,25 | **1,75** | 2,5 | 3,5 | 5 | 7 |
| Separación entre letras | a | (2/14)h | 0,26 | 0,36 | 0,5 | **0,7** | 1 | 1,4 | 2 | 2,8 |
| Espacio mínimo entre líneas (con diacríticos) | b₁ | (25/14)h | 3,25 | 4,5 | 6,25 | **8,75** | 12,5 | 17,5 | 25 | 35 |
| Espacio mínimo entre líneas (sin diacríticos) | b₂ | (21/14)h | 2,73 | 3,78 | 5,25 | **7,35** | 10,5 | 14,7 | 21 | 29,4 |
| Espacio mínimo entre líneas (solo mayúsculas) | b₃ | (17/14)h | 2,21 | 3,06 | 4,25 | **5,95** | 8,5 | 11,9 | 17 | 23,8 |
| Separación entre palabras | e | (6/14)h | 0,78 | 1,08 | 1,5 | **2,1** | 3 | 4,2 | 6 | 8,4 |
| Espesor del trazo | d | (1/14)h | 0,13 | 0,18 | 0,25 | **0,35** | <0,5 | 0,7 | 1 | 1,4 |

Notas:
1. b₁: letras mayúsculas y minúsculas con signos diacríticos
2. b₂: letras mayúsculas y minúsculas sin signos diacríticos
3. b₃: mayúsculas solamente
4. Los valores de d marcados con superíndice son redondeados

### 4.3 Parámetros para h = 5 mm (el usado en los TPs)

```
┌──────────────────────────────────────────────────┐
│  PARÁMETRO    VALOR      DESCRIPCIÓN             │
│  h = 5        5,00 mm    Altura total de mayúsc. │
│  c₁= 3,5      3,50 mm    Altura de minúscula     │
│  c₂= 1,4      1,40 mm    Saliente inf. (g,p,q,y) │
│  c₃= 1,4      1,40 mm    Prolong. sup. (b,d,f,h) │
│  f = 1,75     1,75 mm    Banda diacríticos (á,é) │
│  a = 0,7      0,70 mm    Separación entre letras │
│  b₁= 8,75     8,75 mm    Interlineado (con tilde)│
│  b₂= 7,35     7,35 mm    Interlineado normal     │
│  b₃= 5,95     5,95 mm    Interlineado mayúsculas │
│  e = 2,1      2,10 mm    Separación entre palabras│
│  d = 0,35     0,35 mm    Espesor del trazo       │
└──────────────────────────────────────────────────┘
```

### 4.4 Diagrama de referencia

```
            h=5mm
  ┌─────────────────────────────────────────────┐
  │  IRAM  91  g                                │
  │  ↑  ↑          ↑         ↑d ↑δ ↑           │
  │  h  c₁        b₁        ───── f            │
  │              ↓                    É         │
  │  (base line 1)                              │
  │  ←a→    ←──e──→ ←d→                        │
  │                                             │
  │  (base line 2 = b₁ más abajo)              │
  └─────────────────────────────────────────────┘

Donde:
  h  = altura total (mayúsculas)
  c₁ = altura de minúscula (cuerpo central)
  b₁ = distancia entre líneas de base (con diacríticos)
  a  = separación entre letras
  e  = separación entre palabras
  d  = espesor del trazo
  f  = banda para diacríticos (tildes, diéresis)
```

---

## 5. Acotación (IRAM 4504)

### 5.1 ¿Qué es una cota?

Una cota es la expresión numérica del valor de una medida, indicada en el dibujo. Será paralela a la medida que se acota y de igual longitud.

> **Analogía contable:** La cota es como el importe en una factura — sin él, el dibujo está incompleto. Una pieza sin cotas no puede fabricarse, como una factura sin importe no puede pagarse.

### 5.2 Elementos de una cota

```
                      NÚMERO DE COTA
                           ↓
           ←───────────── 75 ────────────→
           │                              │
    ───────┤                              ├───────
    (línea auxiliar)            (línea auxiliar)
```

| Elemento | Línea IRAM | Descripción |
|---|---|---|
| Línea de cota | 01.1 (fina continua) | Paralela a la dimensión acotada |
| Línea auxiliar de cota | 01.1 (fina continua) | Perpendicular, sale del contorno del objeto |
| Número de cota | Caligrafía tipo A | Valor numérico de la medida |
| Flecha | — | Termina cada extremo de la línea de cota |

### 5.3 Línea auxiliar de cota

Se usa cuando la línea de cota se traza por fuera del contorno de una vista. Tanto la línea de cota como la auxiliar de cota se trazan con **línea fina continua (01.1)**.

```
     ┌─────────────────┐
     │                 │  ← contorno (01.2 gruesa)
     │                 │
     └─────────────────┘
     ↑                 ↑
 línea aux.        línea aux.     ← 01.1 fina, sobresalen del contorno
 ←─────── 100 mm ──────→         ← línea de cota con número
```

### 5.4 La flecha

Los extremos de la línea de cota se terminan con flechas formadas por un **triángulo isósceles ennegrecido**. Relación base:altura ≈ **4:1**.

```
    ◄────  Relación: largo ≈ 4 × ancho
         ↕ 1
    ←────────────────→
           4
```

- Las flechas se dibujan ennegrecidas (rellenas), no huecas
- Siempre apuntan hacia la línea auxiliar (hacia adentro de la cota)

### 5.5 Métodos de acotación de diámetros

Cuando se acota una pieza cilíndrica vista de frente (sin el círculo visible), hay dos métodos equivalentes:

**Método 1** — La línea de cota lleva el símbolo `φ` (phi) antes del número:
```
    ←── φ30 ──→     ←── φ40 ──→
    (el símbolo indica que es diámetro)
```

**Método 2** — La línea de cota sale de la vista circular con `φ` también:
```
    φ30    φ40    φ50
    (los diámetros se indican directamente sobre las vistas)
```

Ambos métodos son correctos según IRAM. El docente puede especificar cuál usar en cada TP.

### 5.6 Acotación en espacios reducidos

Cuando no hay espacio para colocar el número entre las flechas, se permiten estas variantes:

```
Espacio muy reducido — flechas hacia afuera:
    →|    10    |←         → número adentro, flechas afuera

Espacio mínimo — número afuera:
    →|          |← 6,5     → flechas adentro, número afuera

Espacio mínimo múltiple — marcas en vez de flechas:
    ─||──── 18 ────||──── 6 ────||──── 24 ────||─
              2,5    2           (marcas tipo tick)
```

---

## 6. Errores comunes

| Error | Consecuencia | Corrección |
|---|---|---|
| Usar el mismo lápiz para grueso y fino | Líneas indiferenciables | Un lápiz blando para grueso, uno duro para fino |
| Tipo 02 con segmentos irregulares | No cumple IRAM | Segmentos exactamente 6 mm, espacios 1,5 mm |
| Tipo 04 con puntos en vez de raya-punto | No cumple IRAM | Raya 12 mm, luego punto/espacio 1,5 mm |
| Caligrafía libre en el rótulo | No normalizado | Usar tabla IRAM tipo A, h = 5 mm |
| Línea de cota gruesa | No cumple IRAM 4504 | Cota y auxiliar siempre línea fina (01.1) |
| Flecha hueca (sin rellenar) | No cumple IRAM | Triángulo isósceles ennegrecido, relación 4:1 |
| Número de cota en ángulo | Difícil de leer | El número siempre paralelo a la línea de cota |

---

## 7. Mapa conceptual

```
NORMAS IRAM — SISTEMAS DE REPRESENTACIÓN
│
├── Líneas (IRAM 4502)
│   ├── 01.2 gruesa continua → contornos visibles
│   ├── 01.1 fina continua   → cotas, auxiliares, ejes cortos
│   ├── 02.1 fina discontinua → ocultos
│   ├── 04.1 fina raya-punto  → ejes, simetrías
│   └── 04.2 gruesa raya-punto → tratamientos, planos de corte
│
├── Caligrafía (IRAM 4503)
│   ├── Tipo A — proporcional a h
│   ├── h = 5 mm en los TPs
│   └── d = 0,35 mm (espesor de trazo)
│
└── Acotación (IRAM 4504)
    ├── Cota = expresión numérica de una medida
    ├── Línea de cota + auxiliar = 01.1 (fina)
    ├── Flechas = triángulo isósceles negro, 4:1
    └── Espacios reducidos = flechas/número afuera
```
