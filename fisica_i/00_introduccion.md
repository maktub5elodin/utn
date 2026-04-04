# Introducción a la Física — Física I (UTN)

---

## ¿Qué es la Física?

La física es la ciencia que estudia la naturaleza en su nivel más fundamental: busca entender **cómo funciona el universo**, desde el movimiento de un planeta hasta el comportamiento de la luz al pasar por un vidrio.

A diferencia de otras ciencias que estudian sistemas complejos (la biología estudia seres vivos, la química estudia reacciones entre sustancias), la física busca los **principios más básicos y universales** que subyacen a todo lo demás. En ese sentido, es la ciencia más "raíz" de todas las ciencias naturales e ingenieriles.

Su herramienta principal es el **modelo**: una representación simplificada de la realidad que captura lo esencial de un fenómeno y permite hacer predicciones cuantitativas (numéricas) sobre él.

> **Analogía contable:** Así como un balance general no es "la empresa" sino un modelo que captura su situación financiera en un momento dado, un modelo físico no es "la realidad" sino una abstracción útil para predecir comportamientos.

---

## ¿Qué hace realmente un físico? ¿Y un ingeniero?

Un **físico** construye modelos. Observa un fenómeno, identifica qué variables importan, descarta lo que no importa, y formula leyes matemáticas que describen ese fenómeno. Luego verifica experimentalmente si el modelo predice correctamente la realidad.

Un **ingeniero mecánico** aplica esos modelos. Usa las leyes de la física como herramientas para diseñar puentes, motores, estructuras, mecanismos. No necesita derivar la ley desde cero; necesita entenderla lo suficientemente bien como para **saber cuándo aplicarla y cuándo no**.

La diferencia clave:
- El físico pregunta: *¿por qué funciona esto?*
- El ingeniero pregunta: *¿cómo uso esto para que funcione aquello?*

En Física I vas a estar en el medio: aprendiendo los modelos con suficiente profundidad para poder aplicarlos con criterio.

---

## Cómo encarar la materia viniendo de Contabilidad

Tu formación contable tiene más en común con la física de lo que parece. Acá van algunos puentes conceptuales:

### 1. Pensás en flujos y balances → la física también
En contabilidad, rastreás flujos de dinero: de dónde viene, adónde va, qué queda. En física hacés exactamente lo mismo con energía, cantidad de movimiento, y otras magnitudes. **El principio de conservación es el equivalente físico del balance contable**: lo que entra menos lo que sale es igual a lo que queda.

### 2. Estás acostumbrado a trabajar con modelos simplificados
Un estado de resultados no captura *todo* lo que pasa en una empresa; captura lo que importa. Igual con los modelos físicos: vamos a ignorar el roce del aire, vamos a asumir que los cuerpos son puntos sin tamaño. Eso no es hacer trampa, es modelar bien.

### 3. El desafío nuevo: la abstracción matemática
En contabilidad, los números representan cosas concretas (pesos, unidades). En física los números representan magnitudes que a veces no se pueden tocar (fuerza, campo eléctrico). El paso que tenés que dar es confiar en que las operaciones matemáticas sobre esas magnitudes tienen significado físico real.

### Consejos prácticos

- **Dibujá siempre.** Antes de escribir una ecuación, hacé un esquema del problema. Los ingenieros piensan visualmente.
- **No memorices fórmulas, entendé qué dice cada una.** Una fórmula es una oración en lenguaje matemático. Preguntate qué significa cada letra, qué pasa si esa variable crece o decrece.
- **Resolvé muchos ejercicios.** La física no se aprende leyendo, se aprende haciendo. Es como el análisis de casos en contabilidad: la teoría sola no alcanza.
- **Chequeá las unidades.** Si el resultado de un cálculo de velocidad te da en metros/segundo², algo está mal. Las unidades son tu primera línea de control de calidad.
- **Preguntate el "¿tiene sentido esto?"** después de cada resultado. Si calculás que un auto tarda 0,001 segundos en frenar desde 100 km/h, algo salió mal. El juicio de razonabilidad que usás en auditoría aplica igual acá.
- **El error no es el enemigo.** En física, equivocarse en un ejercicio y entender por qué es más valioso que copiarse la solución correcta.

---

## Los tres pilares del primer parcial

### 1. Óptica — La Física de la Luz

**¿De qué trata?**
La óptica estudia el comportamiento de la luz: cómo se propaga, cómo cambia de dirección, cómo forma imágenes.

**Conceptos clave que vas a ver:**
- **Reflexión:** la luz rebota en superficies (espejos). La ley es simple: el ángulo de entrada igual al ángulo de salida, medidos desde la perpendicular a la superficie.
- **Refracción:** la luz cambia de dirección al pasar de un medio a otro (aire → vidrio → agua). Es lo que hace que una cuchara en un vaso de agua parezca quebrada. Se describe con la **Ley de Snell**.
- **Lentes y espejos:** cómo se forman imágenes (reales o virtuales, derechas o invertidas, más grandes o más chicas).

**Intuición para construir:**
Pensá en la luz como algo que viaja en línea recta hasta que algo se lo impide. Cuando choca contra una superficie, negocia: parte de ella rebota, parte sigue pero doblada.

**Relevancia en ingeniería mecánica:**
Instrumentos de medición óptica, sensores, sistemas de iluminación en diseño de espacios y maquinaria.

---

### 2. Cinemática — El Movimiento sin Causas

**¿De qué trata?**
La cinemática describe *cómo* se mueve un objeto: su posición, velocidad y aceleración a lo largo del tiempo. No le pregunta *por qué* se mueve así, eso lo hace la dinámica.

**Conceptos clave que vas a ver:**
- **Posición, desplazamiento y distancia:** no son lo mismo. Desplazamiento es el vector de inicio a fin; distancia es el camino total recorrido.
- **Velocidad media e instantánea:** la velocidad media es el desplazamiento dividido el tiempo; la instantánea es la velocidad en un instante puntual (la derivada de la posición respecto al tiempo).
- **Aceleración:** cambio de velocidad en el tiempo.
- **Movimiento rectilíneo uniforme (MRU):** velocidad constante, sin aceleración.
- **Movimiento rectilíneo uniformemente acelerado (MRUA):** aceleración constante. Las ecuaciones de este caso son las más usadas en el parcial.
- **Movimiento en 2D y tiro parabólico:** el movimiento de proyectiles. Se resuelve separando el eje horizontal (MRU) del vertical (MRUA por la gravedad).

**Intuición para construir:**
La posición te dice dónde está el objeto. La velocidad te dice qué tan rápido cambia su posición. La aceleración te dice qué tan rápido cambia su velocidad. Son tres niveles de "rapidez de cambio" anidados.

> **Analogía contable:** Posición es como el saldo de una cuenta. Velocidad es como el flujo (cuánto entra o sale por período). Aceleración es como el cambio en ese flujo (si los ingresos están creciendo o disminuyendo).

---

### 3. Dinámica — Las Causas del Movimiento

**¿De qué trata?**
La dinámica responde la pregunta que la cinemática no hace: *¿por qué* un objeto se mueve o cambia su movimiento? La respuesta es: por las **fuerzas**.

**Conceptos clave que vas a ver:**
- **Las 3 Leyes de Newton:** el núcleo de toda la dinámica clásica.
  - *1ª Ley (Inercia):* un objeto sigue lo que está haciendo (quieto o en movimiento uniforme) a menos que una fuerza neta actúe sobre él.
  - *2ª Ley (F = m·a):* la fuerza neta sobre un objeto es igual a su masa multiplicada por su aceleración. Esta es **la** ecuación de la dinámica.
  - *3ª Ley (Acción-Reacción):* si A ejerce una fuerza sobre B, B ejerce una fuerza igual y opuesta sobre A.
- **Peso vs. masa:** la masa es la cantidad de materia (no cambia); el peso es la fuerza gravitatoria sobre esa masa (depende de dónde estás en el universo).
- **Fuerza normal, rozamiento, tensión:** las fuerzas más comunes en problemas de ingeniería.
- **Diagramas de cuerpo libre:** la herramienta fundamental para resolver problemas de dinámica. Se dibuja el objeto solo, con todas las fuerzas que actúan sobre él.

**Intuición para construir:**
La inercia es resistencia al cambio. Forzar ese cambio requiere esfuerzo (fuerza). Cuanto más masa tiene un objeto, más cuesta cambiar su estado.

> **Analogía contable:** La 2ª Ley de Newton (F = m·a) es similar en estructura a la ecuación contable básica (Activo = Pasivo + Patrimonio): relaciona tres magnitudes de manera que si sabés dos, podés calcular la tercera.

---

## Mapa general del primer cuatrimestre

```
Física I — Primer Parcial
│
├── Óptica
│   ├── Reflexión (Ley de la reflexión, espejos)
│   ├── Refracción (Ley de Snell, índice de refracción)
│   └── Lentes y formación de imágenes
│
├── Cinemática
│   ├── Movimiento en 1D (MRU, MRUA)
│   ├── Vectores y movimiento en 2D
│   └── Tiro parabólico
│
└── Dinámica
    ├── Las 3 Leyes de Newton
    ├── Fuerzas: peso, normal, rozamiento, tensión
    └── Diagramas de cuerpo libre y resolución de sistemas
```

---

## Una última reflexión

La física puede sentirse árida al principio, especialmente cuando el foco está en las matemáticas y las abstracciones. Pero en el fondo, cada fórmula es la descripción comprimida de algo que pasa en el mundo real.

Cada vez que resuelvas un ejercicio, intentá conectarlo con algo concreto: un auto frenando, una pelota lanzada, la luz doblándose en tus anteojos. Esa conexión entre la abstracción matemática y el fenómeno real es exactamente el músculo que la ingeniería te pide desarrollar.

Bienvenido a la física.
