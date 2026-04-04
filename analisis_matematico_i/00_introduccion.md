# Introducción a Análisis Matemático I (UTN)

---

## ¿Qué es esta materia?

**Análisis Matemático I** (AM1) es la materia de cálculo del primer año de ingeniería. Si AyGA estudia la *estructura* (vectores, matrices, espacios), AM1 estudia el **cambio**: cómo varían las funciones, qué tan rápido cambian, cuánto acumulan.

Más concretamente, AM1 construye dos herramientas fundamentales:

- **La derivada:** mide la *tasa de cambio instantánea* de una función. ¿Qué tan rápido crece la temperatura? ¿Con qué velocidad se deforma una pieza bajo carga?
- **La integral:** mide la *acumulación*. ¿Cuánto calor se transfirió en total? ¿Qué área ocupa una sección transversal?

Hacia el final de la materia aparecen también las **series**, que permiten aproximar funciones complicadas con sumas infinitas de términos simples — la base de cómo las computadoras calculan senos, exponenciales y logaritmos.

La materia es **anual**, una clase por semana los lunes, con dos parciales: uno en agosto y otro en noviembre.

---

## ¿Por qué la necesita un ingeniero mecánico?

El cálculo no es un ejercicio académico. Está en el núcleo de casi todo lo que hace un ingeniero mecánico:

- **Cinemática y dinámica:** la velocidad es la derivada de la posición; la aceleración es la derivada de la velocidad. Sin derivadas no hay física newtoniana.
- **Termodinámica:** el calor transferido es una integral de la potencia en el tiempo. Los ciclos termodinámicos se calculan como áreas bajo curvas.
- **Resistencia de materiales:** la deformación de una viga bajo carga distribuida se obtiene integrando dos veces la ecuación de la elástica.
- **Diseño de máquinas:** encontrar el punto de mínima tensión, máximo rendimiento o menor peso es un problema de optimización — derivadas igualadas a cero.
- **Vibraciones y control:** el comportamiento de sistemas mecánicos se describe con ecuaciones diferenciales, que aparecen en la segunda parte de la materia.
- **Manufactura y CAM:** las trayectorias de herramientas en mecanizado CNC se calculan con curvas paramétricas y sus derivadas.

> El cálculo es el idioma en que están escritas las leyes de la física. Sin él, solo podés usar las fórmulas; con él, podés entender de dónde vienen y adaptarlas a situaciones nuevas.

---

## Cómo encarar la materia viniendo de Contabilidad

AM1 es probablemente la materia que más contrasta con la formación contable, porque trabaja con el concepto de *infinito* (límites, sumas infinitas) y con objetos que no se pueden "ver" directamente (la derivada en un punto, el área bajo una curva).

Pero hay puentes útiles:

### 1. La derivada es una tasa de variación — como cualquier indicador de gestión

En contabilidad calculás tasas todo el tiempo: variación porcentual de ventas, tasa de crecimiento de costos, rentabilidad mensual. La derivada es exactamente eso, pero *en un instante* en lugar de en un período. Es la versión matemática de preguntarse: "¿a qué velocidad está cambiando esto *ahora mismo*?"

> **Analogía:** la variación de ventas entre enero y febrero es una tasa media (como el cociente incremental). La derivada es el límite de esa tasa cuando el período se hace infinitamente pequeño — la velocidad instantánea del cambio.

### 2. La integral es una acumulación — como un flujo de caja integrado

Si la derivada descompone el cambio, la integral lo reensambla. Sumar infinitos pedacitos pequeños para obtener un total es exactamente lo que hace una integral — y es análogo a sumar todos los flujos diarios para obtener el flujo acumulado del año.

> **Analogía:** si sabés cuánto entra por día (una función), la integral te dice cuánto acumulaste en el mes. El Teorema Fundamental del Cálculo dice que derivar e integrar son operaciones inversas — como el debe y el haber.

### 3. Los límites son el rigor detrás de la intuición

Antes de derivadas e integrales viene el concepto de **límite**: qué valor se acerca una función cuando la variable se acerca a algún punto. Es la formalización de "qué pasa cuando me acerco mucho pero no llego". Puede sentirse abstracto al principio, pero es el cimiento que hace que todo lo demás sea matemáticamente válido.

### Consejos prácticos

- **Dominá las funciones elementales antes de empezar.** Seno, coseno, exponencial, logaritmo — sus gráficas, sus propiedades, sus comportamientos límite. Si las funciones básicas te resultan extrañas, los temas que vienen encima son mucho más difíciles.
- **No salteés los límites aunque parezcan abstractos.** Son el 30% del primer parcial y el fundamento de todo lo demás. Una comprensión débil de límites produce errores en derivadas e integrales.
- **En derivadas, memorizá las reglas pero entendé qué significan.** La regla de la cadena, del producto, del cociente — cada una tiene una interpretación. Si la entendés, la recordás; si solo la memorizás, la confundís bajo presión.
- **Dibujá funciones antes de calcular.** Antes de derivar o integrar, hacé un bosquejo de la función. Te da intuición sobre el resultado esperado y te avisa cuando el cálculo salió mal.
- **Las series al final son más difíciles conceptualmente.** Requieren pensar en procesos infinitos. Dales tiempo extra y muchos ejemplos.

---

## Los dos grandes bloques

### Bloque 1 — Primer Parcial (marzo a agosto)

El primer parcial cubre el análisis de funciones reales de una variable: cómo se comportan, cómo cambian, y cómo se optimizan.

---

**Funciones**
El punto de partida: dominio, imagen, gráfica, funciones elementales (polinómicas, racionales, trigonométricas, exponenciales, logarítmicas). Las funciones son el objeto de estudio de toda la materia.

---

**Topología**
Conceptos de vecindad, intervalos abiertos y cerrados, puntos de acumulación. Es el lenguaje formal para hablar de "cercanía" en la recta real — necesario para definir límites con precisión.

---

**Límites**
El concepto central de todo el cálculo. El límite de `f(x)` cuando `x → a` es el valor al que se acerca la función, independientemente de lo que valga *en* `a`. Se estudian:
- Límites laterales (por izquierda y por derecha).
- Límites en el infinito y límites infinitos.
- **Límites indeterminados** (formas `0/0`, `∞/∞`, `0·∞`, etc.) — se resuelven con factorización, racionalización, o la **Regla de L'Hôpital**.

---

**Asíntotas y Continuidad**
Las asíntotas (verticales, horizontales, oblicuas) describen el comportamiento de la función "en los extremos". La continuidad formaliza la intuición de "poder dibujar la curva sin levantar el lápiz".

Los **teoremas de funciones continuas** (Bolzano, Valor Intermedio, Weierstrass) son resultados poderosos que garantizan la existencia de ceros, máximos y mínimos bajo ciertas condiciones.

---

**Derivadas**
La derivada de `f` en `x` es el límite del cociente incremental:

```
f'(x) = lim [f(x+h) - f(x)] / h   cuando h → 0
```

Geométricamente, es la **pendiente de la recta tangente** a la curva en ese punto. Se estudian:
- Reglas de derivación: suma, producto, cociente, composición (regla de la cadena).
- Derivadas de funciones elementales.
- Derivadas sucesivas (segunda derivada, tercera derivada...).
- **Diferenciabilidad:** condición más fuerte que continuidad.

---

**Teoremas de funciones derivables**
- **Rolle:** si `f(a) = f(b)`, existe un punto interior donde `f'(c) = 0`.
- **Valor Medio (Lagrange):** existe un punto donde la derivada iguala la tasa de variación media.
- **Regla de L'Hôpital:** para resolver indeterminaciones usando derivadas.

---

**Estudio de funciones y Optimización**
La derivada permite analizar completamente una función:
- Intervalos de crecimiento y decrecimiento (signo de `f'`).
- Máximos y mínimos locales (donde `f' = 0` o no existe).
- Concavidad y puntos de inflexión (signo de `f''`).
- Construcción del gráfico completo.

La **optimización** aplica todo esto a problemas reales: encontrar la dimensión que minimiza el costo, el ángulo que maximiza el alcance, la velocidad que minimiza el consumo.

---

### Bloque 2 — Segundo Parcial (agosto a noviembre)

El segundo parcial extiende el cálculo hacia la acumulación (integrales) y las aproximaciones (series).

---

**Fórmula de Taylor**
Cualquier función "suave" puede aproximarse localmente mediante un polinomio. La **serie de Taylor** en `x = a` es:

```
f(x) ≈ f(a) + f'(a)(x-a) + f''(a)(x-a)²/2! + f'''(a)(x-a)³/3! + ...
```

Sirve para aproximar funciones complicadas, calcular límites indeterminados, y estimar errores de aproximación.

---

**Integrales indefinidas y métodos de integración**
La integral indefinida es la operación inversa de derivar — la **antiderivada**:

```
∫ f(x) dx = F(x) + C    tal que F'(x) = f(x)
```

Métodos de integración:
- **Integración directa** (reconocimiento de antiderivadas inmediatas).
- **Sustitución (cambio de variable):** simplificar el integrando con una sustitución.
- **Integración por partes:** para productos de funciones (`∫ u dv = uv - ∫ v du`).
- **Fracciones parciales:** para integrar funciones racionales.

---

**Ecuaciones diferenciales**
Una ecuación diferencial relaciona una función con sus derivadas. Las más simples son de variables separables:

```
dy/dx = f(x)·g(y)   →   ∫ dy/g(y) = ∫ f(x) dx
```

Aparecen en todo: enfriamiento de piezas, crecimiento de presión, circuitos, vibraciones.

---

**Integrales definidas y Teorema Fundamental del Cálculo**
La integral definida `∫[a,b] f(x) dx` es el **área con signo** bajo la curva entre `a` y `b`.

El **Teorema Fundamental del Cálculo** conecta todo:
```
∫[a,b] f(x) dx = F(b) - F(a)
```
Donde `F` es cualquier antiderivada de `f`. Derivar e integrar son operaciones inversas.

---

**Integrales impropias**
Integrales con límites infinitos (`∫[1,∞)`) o con discontinuidades en el intervalo. Se evalúan como límites de integrales ordinarias — y pueden converger (dar un número finito) o divergir.

---

**Sucesiones y Series**
Una **sucesión** es una lista infinita de números `a₁, a₂, a₃, ...`. Una **serie** es la suma de todos esos términos. La pregunta central: ¿la suma infinita converge a un número finito, o diverge?

Se estudian criterios de convergencia:
- Criterio de la razón (d'Alembert).
- Criterio de la integral.
- Criterio de comparación.
- **Series alternadas** (criterio de Leibniz).
- **Series de potencias:** `Σ aₙ(x-a)ⁿ` — generalizan Taylor y convergen en un intervalo.

---

## Mapa general y cronograma 2026

```
Análisis Matemático I — A1191 (Anual 2026, lunes)
│
├── PARCIAL 1 (24-ago-2026)
│   │
│   ├── Funciones                         [30-mar]
│   ├── Topología                         [6-abr]
│   ├── Límites                           [13-abr / 20-abr]
│   ├── Límites indeterminados            [27-abr / 4-may]
│   ├── Asíntotas. Continuidad            [11-may]
│   ├── Teoremas de funciones continuas   [18-may]
│   ├── Derivadas                         [1-jun / 8-jun / 22-jun]
│   ├── Derivadas sucesivas               [29-jun]
│   ├── Teoremas. Estudio de funciones    [6-jul]
│   └── Optimización                      [3-ago]
│
└── PARCIAL 2 (30-nov-2026)
    │
    ├── Fórmula de Taylor                 [31-ago]
    ├── Integrales indefinidas            [7-sept]
    ├── Métodos de integración +
    │   Ecuaciones diferenciales          [14-sept]
    ├── Integrales definidas              [28-sept]
    ├── T.F.C. + Integrales impropias     [5-oct / 12-oct]
    ├── Sucesiones. Series                [19-oct / 26-oct]
    └── Series alternadas y de potencias  [2-nov / 9-nov]
```

---

## Régimen de evaluación

- **2 parciales** a lo largo del año:
  - **1er Parcial:** lunes 24 de agosto de 2026
  - **2do Parcial:** lunes 30 de noviembre de 2026
- **Recuperatorios** (2 instancias por cada parcial):
  - 1er Parcial: 14/12/2026 y 15/2/2027
  - 2do Parcial: 21/12/2026 y 22/2/2027
- Hay también instancias **complementarias** junto con los primeros recuperatorios (para quien aprobó uno pero necesita subir nota).

---

## Una última reflexión

El cálculo tiene fama de difícil, y parte de esa fama es merecida: exige un tipo de pensamiento que probablemente no habías ejercitado — razonar sobre lo que ocurre "en el límite", visualizar áreas bajo curvas, trabajar con sumas de infinitos términos.

Pero también hay una recompensa concreta: después de AM1, las leyes de la física dejan de ser fórmulas que aceptás por fe y se convierten en relaciones que podés derivar, analizar y extender. Un ingeniero que entiende cálculo no memoriza fórmulas; las construye.

El primer mes (funciones, topología, límites) es denso y conceptual. No te desesperes si parece lento. Todo ese andamiaje se justifica cuando llegás a derivadas y las piezas encajan.

Bienvenido al cálculo.
