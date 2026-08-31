# Energía en casos límite

## Por qué esta carpeta es distinta a las demás de `fisica_i/`

`00_introduccion.md`, `01_optica.md` y `02_cinematica.md` en la carpeta padre son **resúmenes de clase**: condensan lo que la cátedra dio, en el orden en que lo dio. Esta carpeta es otra cosa. Es lunes 31 de agosto de 2026, y el parcial es pasado mañana, **miércoles 2 de septiembre**. Para esta instancia ya leí — por mi cuenta, del *Physics* de Sears, Young, Freedman y Zemansky (ediciones 12ª y 13ª) — los capítulos 1 a 6. No necesito otro resumen de esos capítulos: los tengo. Lo que quiero es *usarlos* para pensar algo que no está en el libro: cuánta potencia puede generar realmente un cuerpo humano, llevado a sus casos límite — el lanzamiento de bala y el lanzamiento de jabalina en el deporte de alto rendimiento.

Esto es **compound knowledge**: cada capítulo nuevo no reemplaza al anterior, se apoya en él. Es la misma lógica que el interés compuesto en contabilidad — el capital de este período incluye los intereses ya devengados del período anterior, no arranca de cero. Acá, la ecuación de trabajo-energía del capítulo 6 no es un tema nuevo aislado: es álgebra directa sobre las dos ecuaciones de cinemática del capítulo 2 que ya tenías incorporadas. Esa derivación te la enseñó el libro — no la inventaste vos, y vale la pena tenerlo claro para no engañarte con la propia curva de aprendizaje —, pero la hiciste tuya al punto de encontrarle un uso concreto y disfrutarla, y es el punto de partida del archivo `01`.

## Dónde estoy parado en el temario (Mecánica, Sears caps. 1–9)

```
 [x] Cap 1  Units, Physical Quantities, and Vectors
 [x] Cap 2  Motion Along a Straight Line
 [x] Cap 3  Motion in Two or Three Dimensions      (acá vive projectile motion — se usa en 03 y 04)
 [x] Cap 4  Newton's Laws of Motion                (F = m·a, w = m·g)
 [x] Cap 5  Applying Newton's Laws                 (fricción: mu_s, mu_k — mencionado, no explotado aún)
 [x] Cap 6  Work and Kinetic Energy                ← hasta acá llegué de teoría nueva
 [ ] Cap 7  Potential Energy and Energy Conservation
 [ ] Cap 8  Momentum, Impulse, and Collisions
 [ ] Cap 9  Rotation of Rigid Bodies
                                                     parcial: miércoles 02/sep/2026
```

Todo lo que sigue en esta carpeta usa **solo** herramientas de los capítulos 1 a 6. Cuando en el camino aparece una tentación de usar energía potencial (cap. 7) o impulso (cap. 8) — y va a aparecer, porque un lanzamiento es un caso de libro para esos temas — lo marco explícitamente como "adelanto" y lo dejo pendiente de desarrollar cuando llegue a esos capítulos. La carpeta va a seguir creciendo con esos archivos más adelante.

## Convención de vocabulario: inglés donde ayuda

Vengo notando que aprendo física mejor en inglés que en español — probablemente porque es el idioma en el que está escrito el Sears, que es mi fuente principal. Uso español para el día a día y para el resto de la carrera, pero en esta carpeta en particular voy a citar siempre el término original en inglés junto al símbolo, porque ahí es donde vive la lógica de la notación:

| Símbolo | Inglés | Español | Nota |
|---|---|---|---|
| `h` | height | altura | — |
| `w` | weight | peso | **minúscula** — es una fuerza, en N: `w = m·g` |
| `W` | Work | trabajo | **mayúscula** — en J. No confundir con `w` (peso) |
| `K` | Kinetic Energy | energía cinética | `K = ½·m·v²`, en J |
| `U` | Potential Energy | energía potencial | cap. 7, pendiente |
| `P` | Power | potencia | en W = J/s |
| `F` | Force | fuerza | en N |
| `m` | mass | masa | en kg |
| `a` | acceleration | aceleración | en m/s² |
| `v`, `v₀` | velocity, initial velocity | velocidad, velocidad inicial | en m/s |
| `t` | time | tiempo | en s |
| `μs`, `μk` | coefficient of static/kinetic friction | coeficiente de fricción estática/cinética | adimensional; "s" de *static*, "k" de *kinetic* |
| `x`, `Δx` | displacement | desplazamiento | en m |

La distinción `w` vs `W` es la que más vale la pena tener clavada: el libro las usa una al lado de la otra todo el tiempo (`w = mg` es una fuerza vertical; `W = F·d·cosθ` es un escalar que puede valer cero aunque haya fuerza, si no hay desplazamiento, o aunque haya desplazamiento, si la fuerza es perpendicular a él).

## Convención de método: vectores primero

Cuando un problema admite resolverse por descomposición vectorial (componentes, vector resultante, producto escalar o producto vectorial, matrices/determinantes) y también por un atajo trigonométrico "de memoria" (ángulos de referencia, simetrías), en esta carpeta priorizo la vía vectorial. No es purismo: el atajo es más rápido una vez que se domina, pero abre la puerta a errores de signo silenciosos — el ejemplo real es descomponer una fuerza en el 4to cuadrante usando `cos 300°` en vez de `sin 30°` (o viceversa) sin ajustar el signo según el cuadrante en el que realmente cae el ángulo. El método de componentes, con el ángulo medido siempre desde el eje `+x` en sentido antihorario (la convención estándar), no tiene esa ambigüedad: los signos de `cos θ` y `sin θ` salen solos al evaluarlos en el ángulo real — no hace falta "recordarlos" caso por caso.

Por eso en `01` el trabajo (*Work*) no se presenta solo como la fórmula memorizada `W = F·d·cosθ`, sino primero como el producto escalar entre el vector fuerza y el vector desplazamiento, `W = F⃗ · Δr⃗`, del cual `cos θ` sale como consecuencia de la definición geométrica del producto escalar, no como un factor aparte para memorizar. A medida que aparezcan fuerzas no colineales con el desplazamiento (por ejemplo, en una trayectoria curva) se van a descomponer en componentes `x`/`y` en vez de tirar de un ángulo de referencia memorizado — y cuando el capítulo 9 (rotación) entre en juego, el producto vectorial (`×`) va a tener su lugar para torque y momento angular.

## Mapa de esta carpeta

```
00_introduccion.md                         → este archivo: por qué, dónde estoy, vocabulario
01_de_la_cinematica_al_trabajo_energia.md  → la derivación del libro (cap. 2→6), formalizada + Work como producto escalar
02_calibracion_personal_el_joule_humano.md → "¿puedo mover 1 kg, 1 m, en 1 s?" — con números
03_lanzamiento_de_bala_shot_put.md         → primer caso límite: masa grande, velocidad menor
04_lanzamiento_de_jabalina_javelin.md      → segundo caso límite: masa chica, velocidad enorme
05_comparativa_potencia_humana.md          → los dos casos + otros deportes, en una sola tabla
```

Cada archivo de `03` en adelante cita sus fuentes al pie — récords mundiales, especificaciones reglamentarias y estudios de biomecánica son datos reales, buscados para esta carpeta, no inventados. Las estimaciones de tiempo (cuánto dura la fase final de aceleración de un lanzamiento) sí son supuestos razonados, no mediciones — están marcadas como tales en cada caso: la idea es tener un orden de magnitud confiable, no un dato de laboratorio.

## Un último apunte antes de arrancar

El miércoles rendís hasta donde da el capítulo 6. Esta carpeta no es para ese parcial — es para el después. Pero si en el medio de armar el caso del lanzamiento de bala se termina de fijar el teorema trabajo-energía mejor de lo que lo dejó el resumen de clase, mejor todavía.
