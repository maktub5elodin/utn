# Introducción a Álgebra y Geometría Analítica (UTN)

---

## ¿Qué es esta materia?

El nombre completo es **Álgebra y Geometría Analítica** (AyGA), y es una de las dos grandes materias matemáticas del primer año de ingeniería en UTN (junto con Análisis Matemático).

Si Análisis Matemático estudia el *cambio* (derivadas, integrales, límites), AyGA estudia la **estructura**: cómo se organizan objetos matemáticos (vectores, matrices, sistemas de ecuaciones) y qué transformaciones se les pueden aplicar.

Más concretamente, la materia tiene dos grandes ejes:

- **Álgebra Lineal:** el estudio de vectores, matrices, sistemas de ecuaciones y transformaciones entre espacios. Es la herramienta matemática más usada en ingeniería moderna.
- **Geometría Analítica:** el estudio de objetos geométricos (rectas, planos, curvas, superficies) mediante ecuaciones algebraicas. Es el puente entre la geometría visual y el cálculo.

---

## ¿Por qué la necesita un ingeniero mecánico?

El álgebra lineal no es una materia abstracta desconectada de la ingeniería. Está en todos lados:

- **Estructuras y resistencia de materiales:** el análisis de tensiones en una viga es un sistema de ecuaciones lineales.
- **Robótica y cinemática:** el movimiento de un brazo robótico se describe con matrices de transformación.
- **Vibraciones y dinámica:** los modos naturales de vibración de una estructura son exactamente los **autovectores** de una matriz.
- **Diseño asistido por computadora (CAD):** las rotaciones, traslaciones y escalados de objetos 3D son transformaciones lineales aplicadas a vectores.
- **Elementos finitos:** el método numérico más usado en simulación de ingeniería convierte un problema físico continuo en un sistema de ecuaciones matricial enorme.

> Cuando un programa de simulación como ANSYS o SolidWorks calcula tensiones, deformaciones o frecuencias naturales, por debajo está resolviendo sistemas de ecuaciones y calculando autovalores. AyGA te da el lenguaje para entender qué está haciendo la computadora.

---

## Cómo encarar la materia viniendo de Contabilidad

Hay una tensión inicial que muchos sienten: en contabilidad todo tiene unidades concretas y significado inmediato (pesos, cantidades, fechas). En álgebra lineal vas a ver objetos que a veces parecen flotando en el vacío matemático — un "espacio vectorial abstracto", una "transformación lineal", una "forma cuadrática".

La clave es que **la abstracción no es el fin, es la herramienta**. Acá van algunos puentes:

### 1. Las matrices son tablas de datos estructurados

En contabilidad manejás tablas todo el tiempo: filas son cuentas, columnas son períodos, las celdas son valores. Una matriz es exactamente eso. La diferencia es que en álgebra definimos operaciones precisas entre esas tablas (suma, producto) que tienen interpretaciones geométricas y físicas concretas.

> **Analogía:** multiplicar matrices es como aplicar una conversión de moneda compuesta. Si la matriz A convierte de pesos a dólares, y la matriz B convierte de dólares a euros, entonces el producto B·A convierte directamente de pesos a euros.

### 2. Resolver sistemas de ecuaciones = buscar el equilibrio

Cuando en contabilidad armás un balance y lo cuadrás, estás resolviendo un sistema de ecuaciones implícito. AyGA te da las herramientas para resolver sistemas de cualquier tamaño y entender cuándo tienen solución única, infinitas soluciones, o ninguna.

### 3. Los vectores son flechas con dirección y magnitud

Un vector no es solo un par de números: representa una *dirección en el espacio*. La velocidad de un objeto es un vector (tiene rapidez y sentido). La fuerza sobre una viga es un vector. Aprender a operar con ellos es aprender el idioma nativo de la física e ingeniería.

### 4. El desafío nuevo: pensar en n dimensiones

En contabilidad trabajás en el "espacio" de tus cuentas, que puede tener cientos de dimensiones (una por cuenta). El concepto abstracto de "espacio vectorial de n dimensiones" no es tan ajeno como parece: es exactamente eso, solo formalizado matemáticamente.

### Consejos prácticos

- **Dibujá siempre que puedas.** Especialmente en los primeros temas (vectores, rectas, planos), el dibujo te da intuición sobre lo que la ecuación está diciendo.
- **No memorices procedimientos, entendé el objetivo.** Gauss-Jordan no es un ritual; es un algoritmo que busca simplificar un sistema sin cambiar sus soluciones. Si entendés el *qué* y el *por qué*, el *cómo* se vuelve obvio.
- **Conectá cada concepto con su interpretación geométrica.** Un determinante es un número, sí; pero también es el *volumen* del paralelepípedo definido por los vectores fila. Esa imagen geométrica vale más que la fórmula.
- **Hacé los ejercicios del Kozak.** El libro de cátedra (Kozak-Pastorelli-Vardanega) tiene ejercicios graduados por dificultad. Es el material más calibrado para el parcial de UTN-FRBA.
- **Usá el sitio de la cátedra:** `aga.frba.utn.edu.ar` — tiene teoría, videos, applets de GeoGebra y parciales resueltos de años anteriores.

---

## Los dos grandes bloques

La materia se divide en dos partes que corresponden a los dos parciales:

### Parte A — Parcial 1 (Unidades I a V)

La primera mitad construye el lenguaje y las herramientas fundamentales:

**Unidad I — Vectores, Recta y Plano**
El punto de partida geométrico. Un vector es una flecha en el espacio. Aprendés a sumarlos, escalarlos y hacer tres tipos de productos entre ellos (escalar, vectorial, mixto), cada uno con una interpretación geométrica diferente. Luego aplicás todo esto para describir rectas y planos en 2D y 3D mediante ecuaciones.

> **¿Para qué sirve?** Para calcular ángulos entre superficies, distancias entre objetos en el espacio, y describir la geometría de cualquier pieza mecánica.

**Unidad II — Espacio Vectorial**
Acá se generaliza la idea de "vector". Un espacio vectorial es cualquier conjunto donde tiene sentido sumar elementos y escalarlos. Los polinomios, las matrices, las funciones: todos forman espacios vectoriales. Los conceptos de **base** y **dimensión** te dicen cuánta información mínima necesitás para describir cualquier elemento del espacio.

> **¿Para qué sirve?** Para entender que cualquier estado de un sistema puede describirse como combinación de estados "básicos". En vibraciones, por ejemplo, cualquier movimiento complejo es suma de modos normales.

**Unidad III — Matrices**
Las matrices son el vehículo del álgebra lineal. Aprendés las operaciones (suma, producto, transposición, inversión) y sus propiedades. El cálculo de la **matriz inversa** por Gauss-Jordan es una de las habilidades procedimentales clave del parcial.

> **¿Para qué sirve?** Para representar y manipular transformaciones de manera compacta y computacional.

**Unidad IV — Determinantes**
El determinante de una matriz es un número que "resume" propiedades críticas de la transformación que representa: si vale cero, la transformación aplasta el espacio (la matriz es singular, no invertible). Se usa para calcular inversas (método de Cramer) y para interpretar geometrías.

**Unidad V — Sistemas de Ecuaciones Lineales**
La aplicación más inmediata de todo lo anterior. Dados n ecuaciones con n incógnitas, ¿existe solución? ¿Es única? ¿Cómo se calcula? El **Teorema de Rouché-Fröbenius** da las condiciones de compatibilidad. Los métodos: Gauss-Jordan, inversión de matrices, regla de Cramer.

---

### Parte B — Parcial 2 (Unidades VI a IX)

La segunda mitad profundiza con conceptos más abstractos y geométricos:

**Unidad VI — Transformaciones Lineales**
Una transformación lineal es una función entre espacios vectoriales que "respeta la estructura". Las rotaciones, reflexiones, proyecciones: todas son transformaciones lineales. Cada una puede representarse con una matriz, y esa correspondencia es el núcleo del álgebra lineal moderno.

**Unidad VII — Cónicas**
Las cónicas (circunferencia, parábola, elipse, hipérbola) son las curvas que aparecen al cortar un cono con un plano. Tienen una ecuación general de segundo grado y se clasifican según la **excentricidad**. También se estudian en forma paramétrica.

> **¿Dónde aparecen?** La órbita de los planetas es una elipse. El foco parabólico concentra señales en antenas y reflectores. Las hipérbolas aparecen en leyes de enfriamiento y diseño de torres de enfriamiento.

**Unidad VIII — Superficies (Cuádricas)**
La generalización 3D de las cónicas. Las cuádricas (elipsoides, paraboloides, hiperboloides) son superficies descritas por ecuaciones de segundo grado en x, y, z. Se analizan por secciones paralelas a los planos coordenados.

**Unidad IX — Autovalores y Autovectores**
El concepto más importante y poderoso del curso. Un **autovector** de una matriz es un vector que solo se escala (no rota) al aplicar la transformación. El factor de escala es el **autovalor**. Permiten diagonalizar matrices, simplificar transformaciones, y calcular potencias de matrices eficientemente.

> **¿Para qué sirve?** Los modos de vibración de una estructura son autovectores de la matriz de rigidez. El análisis de componentes principales (PCA) en estadística es un cálculo de autovectores. Google PageRank es un cálculo de autovector. Es el concepto más ubicuo de toda la ingeniería computacional.

---

## Mapa general de la materia

```
Álgebra y Geometría Analítica — UTN FRBA
│
├── PARCIAL A (Unidades I–V)
│   │
│   ├── I. Vectores, Recta y Plano
│   │   ├── Operaciones vectoriales (escalar, vectorial, mixto)
│   │   ├── Rectas en R² y R³
│   │   └── Planos: ecuaciones, distancias, ángulos
│   │
│   ├── II. Espacios Vectoriales
│   │   ├── Definición y ejemplos
│   │   ├── Subespacios, combinación lineal
│   │   ├── Dependencia / independencia lineal
│   │   └── Base, dimensión, cambio de base
│   │
│   ├── III. Matrices
│   │   ├── Operaciones: suma, producto, transposición
│   │   ├── Matrices especiales (inversa, ortogonal, simétrica...)
│   │   └── Cálculo de inversa: Gauss-Jordan
│   │
│   ├── IV. Determinantes
│   │   ├── Definición y propiedades
│   │   ├── Desarrollo por Laplace
│   │   └── Matriz adjunta
│   │
│   └── V. Sistemas de Ecuaciones Lineales
│       ├── Forma matricial
│       ├── Teorema de Rouché-Fröbenius
│       └── Métodos: Gauss-Jordan, inversión, Cramer
│
└── PARCIAL B (Unidades VI–IX)
    │
    ├── VI. Transformaciones Lineales
    │   ├── Definición, núcleo e imagen
    │   ├── Representación matricial
    │   └── Matrices semejantes, cambio de base
    │
    ├── VII. Cónicas
    │   ├── Circunferencia, elipse, parábola, hipérbola
    │   ├── Clasificación por excentricidad
    │   └── Parametrización
    │
    ├── VIII. Superficies Cuádricas
    │   ├── Ecuaciones de segundo grado en R³
    │   ├── Estudio por secciones
    │   └── Coordenadas polares, cilíndricas y esféricas
    │
    └── IX. Autovalores y Autovectores
        ├── Definición y cálculo (polinomio característico)
        ├── Diagonalización de matrices
        ├── Formas cuadráticas
        └── Números complejos y aplicaciones
```

---

## Régimen de evaluación

- **1 parcial dividido en dos partes** (cuatrimestral) o **2 parciales** (anual):
  - **Parte A:** Unidades I–V
  - **Parte B:** Unidades VI–IX
- Hay **2 recuperatorios por cada parte**.
- **Promoción directa** (sin final): aprobar ambas partes en primera instancia (o una en primera recuperación) con **8 puntos mínimo** en cada una.
- **Examen final:** individual y escrito, ante un tribunal de 3 docentes. Hasta 4 oportunidades.

---

## Recursos

| Recurso | Descripción |
|---|---|
| `Kozak-Pastorelli-Vardanega` | Libro de cátedra. Cubre las 9 unidades con ejercicios graduados. |
| `aga.frba.utn.edu.ar` | Sitio oficial con teoría, videos, GeoGebra y parciales resueltos. |
| Howard Anton — *Introducción al Álgebra Lineal* | Bibliografía clásica. Clara y con muchos ejemplos. |
| Lipschutz (Schaum) — *Álgebra Lineal* | Miles de ejercicios resueltos. Ideal para practicar. |

---

## Una última reflexión

El álgebra lineal tiene fama de abstracta, y en parte lo es. Pero esa abstracción es su fortaleza: un mismo marco matemático describe el movimiento de una viga, la compresión de una imagen digital, el aprendizaje de una red neuronal, y la estabilidad de un avión. Aprender a pensar en términos de vectores, transformaciones y autovalores es aprender el idioma en que está escrita la ingeniería computacional moderna.

No te preocupes si al principio los conceptos parecen flotar sin anclaje. A medida que avanzás, empezás a ver las conexiones — y cuando llegás a autovalores y entendés que los modos de vibración *son* autovectores, todo el edificio encaja.

Bienvenido al álgebra.
