# Axonometría: Isométrico vs. Caballera — posiciones y el giro que las conecta

## 1. ¿Qué problema resuelve esto?

TP 25 (Isometría) y TP 28 (Perspectiva Caballera Reducida) dibujan la **misma pieza** — un cubo con una circunferencia inscripta en sus 3 caras vistas — pero el resultado gráfico es distinto en cada uno. La pregunta que responde este documento es: *¿qué le pasa físicamente al cubo (o a un Rubik en la mano) para pasar de un dibujo al otro?*

La respuesta corta: **caballera no rota el objeto, isométrico sí**. Caballera es una técnica de proyección — el cubo queda "de frente" al observador y lo que cambia es cómo se proyecta la profundidad. Isométrico, en cambio, exige girar el cubo literalmente hasta que sus 3 ejes queden igualmente inclinados respecto al observador, y después se proyecta de forma ortogonal (sin trucos de oblicuidad).

---

## 2. Teoría — los tres sistemas de referencia

Ejes fijos respecto al observador (no al cubo):

```
        Y (vertical, "arriba")
        |
        |
        |
        +---------- X (horizontal, "derecha")
       /
      /
     /
    Z (hacia el observador, sale de la hoja)
```

El cubo tiene sus propios 3 ejes (los de sus aristas). En la **posición caballera** esos ejes coinciden exactamente con X, Y, Z. En la **posición isométrica** están rotados respecto a X, Y, Z.

### 2.1 Posición caballera (posición "cero", TP 28)

El cubo **no se rota**. Una cara queda exactamente de frente, paralela a la hoja:

```
                +--------+
               /        /|
              /  TAPA  / |
             +--------+  |
             |        |  +
             | FRENTE |  /    <- eje de fuga a 45°,
             | (real, |  /        con coeficiente
             |  1:1)  | /         de reducción
             |        |/
             +--------+
```

- La cara **FRENTE** se ve a tamaño real (0 grados de rotación, 0 deformación).
- La profundidad (eje de fuga, hacia la TAPA) se dibuja en un ángulo convencional (típicamente 45°) y **reducida** por un coeficiente — de ahí "caballera *reducida*" — para compensar que a simple vista una caballera sin reducir se percibe estirada.
- Es una **proyección oblicua**: los rayos de proyección no son perpendiculares al plano del dibujo.

### 2.2 Posición isométrica (TP 25)

Acá sí hay que **rotar el cubo**, en dos pasos, antes de proyectar:

**Paso 1 — giro azimutal de 45° sobre el eje vertical (Y).** Vista desde arriba (mirando hacia abajo, a lo largo de Y):

```
   ANTES (caballera)              DESPUÉS (girado 45° en Y)

     +--------+                         *
     |        |                        / \
     |        |                       /   \
     |        |                      *     *
     +--------+                       \   /
                                        \ /
   (cara frontal                        *
    cuadrada, de frente
    al observador)                (la arista vertical frontal
                                    ahora apunta directo
                                    al observador — el cuadrado
                                    se ve como rombo)
```

**Paso 2 — inclinación de `θ = arctan(1/√2) ≈ 35,26°` sobre el eje horizontal (X).** Vista de perfil (mirando a lo largo de X):

```
   ANTES (vertical)              DESPUÉS (inclinado θ)

      +----+                            *
      |    |                           / \
      |    |                          /   \
      |    |                         *     
      +----+                          \    
                                        \   
   (tapa de canto,                      *
    no se ve)                     (tapa ahora visible,
                                   inclinada 35,26°:
                                   arriba se "aleja")
```

Después de estos dos giros, el vértice más cercano al observador queda con sus 3 aristas formando ángulos de 120° entre sí en la proyección, y cada uno de los 3 ejes del cubo forma el mismo ángulo (`≈54,7356°`) con la dirección de vista. Por eso "isométrico" (*isos* = igual, *metron* = medida): las 3 caras quedan **igualmente** deformadas — a diferencia de caballera, donde 1 cara queda intacta y las otras 2 no.

Recién ahí se proyecta **ortogonalmente** (perpendicular a la hoja) — no hace falta ningún truco de oblicuidad como en caballera, porque la deformación ya la produjo la rotación del objeto.

- **Escala verdadera:** cada arista del cubo, al proyectarse, mide `√(2/3) ≈ 0,8165` de su longitud real.
- **Escala práctica de ingeniería:** por convención, la mayoría de los TPs (incluido TP 25) dibujan directamente a escala 1:1 sobre los ejes isométricos, ignorando ese factor — es más simple y la proporción entre piezas no cambia.

---

## 3. El giro — cómo llevar el Rubik de una posición a la otra

### 3.1 Ida: de caballera a isométrico

1. Girar 45° sobre el eje **vertical** (Y) — cualquiera de los dos sentidos sirve, por simetría.
2. Inclinar `≈35,26°` sobre el eje **horizontal** (X), de forma que la cara superior se aleje del observador y quede visible.

### 3.2 Vuelta: de isométrico a caballera

Hay que deshacer los giros **en orden inverso**, no solo con signo invertido:

1. Deshacer primero la inclinación: `-35,26°` sobre el eje horizontal (X) — el cubo vuelve a quedar "parado".
2. Deshacer después el giro azimutal: `-45°` sobre el eje vertical (Y) — la cara frontal vuelve a quedar de frente al observador.

> **Por qué importa el orden:** las rotaciones en 3D no conmutan (girar A-luego-B no es lo mismo que B-luego-A). Es como revertir asientos contables: si asentaste primero el débito y después el crédito, para volver al estado original tenés que reversar primero el crédito y después el débito — el último movimiento aplicado es el primero en deshacerse. Si invertís el orden de reversión en el cubo, no volvés a la posición caballera: terminás en una orientación distinta.

---

## 4. Ejemplo trabajado — verificación contra los `.dxf` reales

Tomando el mismo cubo con circunferencia inscripta de TP 25 y TP 28, la secuencia de arriba predice:

| Cara | En caballera (posición 0) | Después del giro completo (isométrico) |
|---|---|---|
| Frontal | círculo real, ratio eje menor/mayor = 1,0 | elipse, ratio 1/√3 ≈ 0,577 |
| Superior | elipse (ya deformada por la oblicuidad), ratio ≈ 0,310 | elipse, ratio 1/√3 ≈ 0,577 |
| Lateral | elipse, ratio ≈ 0,310 (misma que superior, por simetría del cubo) | elipse, ratio 1/√3 ≈ 0,577 |

Esto coincide con lo ya relevado en los archivos fuente:
- `tpn28.dxf` (caballera): 1 elipse con ratio ≈ 1,0 (cara frontal, sin deformar) + 2 elipses con ratio ≈ 0,310 (caras paralelas al eje de fuga).
- `tpn25.dxf` (isométrico): **las 3 elipses** con ratio idéntico = 1/√3 ≈ 0,577 — exactamente la igualdad de deformación entre las 3 caras que predice la teoría de §2.2.

Ese "las 3 caras se emparejan en el mismo ratio" es la firma geométrica de haber aplicado el giro isométrico completo (45° + 35,26°) sobre un objeto que en caballera tenía 1 cara intacta y 2 desiguales entre sí en el caso general (acá iguales por la simetría del cubo, pero no lo serían en una pieza no simétrica).

---

## 5. Tabla resumen

| Aspecto | Caballera reducida (TP 28) | Isométrico (TP 25) |
|---|---|---|
| Rotación del objeto | Ninguna — posición frontal | 45° (eje Y) + 35,26° (eje X) |
| Técnica de proyección | Oblicua | Ortogonal |
| Cara frontal | Tamaño real, sin deformar | Deformada igual que las otras 2 |
| Eje de fuga / profundidad | 45° convencional + coeficiente de reducción | No existe — los 3 ejes son simétricos |
| Círculo inscripto en el dxf | Elipse solo en las 2 caras no frontales (ratio ≈ 0,310); frontal ratio ≈ 1,0 | Elipse en las 3 caras, mismo ratio 1/√3 ≈ 0,577 |
| Escala de dibujo | 1:1 en frente, reducida en profundidad | 0,816 (verdadera) o 1:1 (práctica) |
| Giro para llegar desde la otra posición | `-35,26°` (X) luego `-45°` (Y), desde isométrico | `+45°` (Y) luego `+35,26°` (X), desde caballera |

---

## 6. Errores comunes

| Error | Por qué está mal | Corrección |
|---|---|---|
| Pensar que caballera también rota el objeto | Caballera es una técnica de proyección oblicua sobre un objeto en posición frontal, no una rotación | El objeto queda de frente; solo cambia cómo se proyecta la profundidad |
| Invertir el orden al volver de isométrico a caballera (deshacer primero el giro de 45°) | Las rotaciones 3D no conmutan — invertir el orden no devuelve a la posición original | Deshacer siempre en orden inverso: última rotación aplicada, primera en deshacerse |
| Confundir el eje de giro de 45° con el de 35,26° | Son ejes distintos: uno vertical (azimutal), otro horizontal (inclinación) | Verificar cuál eje corresponde a cada paso antes de aplicar el ángulo |
| Mezclar escala verdadera (0,816) y escala práctica (1:1) en el mismo TP | Da dimensiones inconsistentes entre piezas del mismo plano | Elegir una convención y mantenerla en todo el TP |

---

## 7. Mapa conceptual

```
AXONOMETRÍA
│
├── CABALLERA REDUCIDA (TP 28)
│   ├── Objeto: posición frontal, sin rotar
│   ├── Proyección: oblicua
│   ├── Cara frontal: tamaño real (ratio círculo = 1,0)
│   └── Profundidad: eje de fuga 45° + coeficiente de reducción
│
├── ISOMÉTRICO (TP 25)
│   ├── Objeto: rotado 45° (eje Y) + 35,26° (eje X)
│   ├── Proyección: ortogonal
│   ├── 3 caras: igualmente deformadas (ratio círculo = 1/√3 en las 3)
│   └── Escala: 0,816 (verdadera) / 1:1 (práctica de ingeniería)
│
└── GIRO QUE LAS CONECTA (no conmutativo)
    ├── Caballera → Isométrico: +45° (Y), luego +35,26° (X)
    └── Isométrico → Caballera: -35,26° (X), luego -45° (Y)
        (orden estrictamente inverso al de ida)
```

---

*Fuentes: elaboración propia a partir del análisis geométrico de `tpn25.dxf` y `tpn28.dxf` (relación de ejes de las entidades ELLIPSE, documentada en `00_expectativas_y_trabajos_practicos.md`, TP 25 y TP 28) y de convenciones estándar de dibujo técnico (proyección isométrica ISO 5456-3, perspectiva caballera/oblicua). No transcribe un enunciado ni una diapositiva de cátedra puntual — `CLASE 3.pdf` no cubre axonometría explícitamente; este documento es un desarrollo de estudio personal complementario a la carpeta, en la misma línea que `fisica_i/energia_casos_limite/`.*
