# Caso límite 2 — Lanzamiento de jabalina (javelin)

## El objeto y la pista

```
   Masa oficial de la jabalina:
     Varones:  800 g
     Damas:    600 g

   Pista de carrera (runway):
     |←──────────── 30 a 36.5 m ────────────→|  ancho mínimo 4 m
     ───────────────────────────────────────┬──   ← línea de falta (foul line)
      carrera: 6-10 zancadas + 2-3 cruzadas  │
                                              ╲   sector de caída
                                               ╲  (ángulo ≈ 28.96° desde
                                                ╲  los extremos del arco)
```

Acá sí es una carrera en línea recta — al revés que la bala (`03`), que gira dentro de un círculo de 2.135 m. La jabalina se beneficia de una pista larga porque parte de su velocidad final viene de la carrera; la bala no tiene ese recurso porque el reglamento la confina a un círculo.

## Los números de elite

| | Varones | Damas |
|---|---|---|
| Récord mundial | Jan Železný — 98.48 m (1996) | Barbora Špotáková — 72.28 m (2008) |
| Masa del objeto | 800 g | 600 g |
| Velocidad de salida (elite) | ≈ 28–30 m/s | ≈ 20–25 m/s |

Un dato que vale la pena remarcar: la velocidad máxima de carrera de un lanzador de elite en la aproximación es de solo **5–6 m/s** — pero la jabalina sale disparada a **28–30 m/s**. La carrera no es lo que le da la velocidad final al objeto: le da *ritmo y momentum al cuerpo*, que después se transfiere y se multiplica en la acción final de brazo y muñeca (las últimas dos zancadas cruzadas + el "latigazo" final). Es el mismo principio que "ponele el cuerpo al golpe" en boxeo: la fuerza no sale del brazo solo, sale de una cadena cinética que empieza en las piernas, pasa por el tronco, y termina concentrada en el segmento final (puño, o en este caso, jabalina) que se mueve mucho más rápido que cualquier segmento anterior de la cadena.

## Energía cinética en el instante de la suelta

Usando el punto medio del rango de velocidad de elite (varones: 29 m/s):

```
   K = ½ · 0.8 kg · (29 m/s)²
   K = ½ · 0.8 · 841
   K ≈ 336.4 J
```

Damas (punto medio 22.5 m/s):

```
   K = ½ · 0.6 kg · (22.5 m/s)²
   K = ½ · 0.6 · 506.25
   K ≈ 151.9 J
```

## El dato que no cierra a primera vista

La jabalina masculina llega a **98.48 m** con apenas **336 J** de energía cinética de salida. La bala masculina (`03`) llega a solo **23.56 m** con **724 J** — más del doble de energía, para una **cuarta parte** de la distancia. ¿Cómo puede ser que "menos energía" produzca "más del cuádruple de alcance"?

La respuesta no está en la energía, está en **cómo se convierte esa energía en distancia**: la bala es, aerodinámicamente, casi una esfera lisa — vuela como un proyectil de cap. 3 sin más ayuda que su propia inercia, perdiendo energía contra el arrastre del aire (*drag*) sin ganar nada a cambio. La jabalina, en cambio, tiene una forma diseñada para generar **sustentación aerodinámica** (*aerodynamic lift*) mientras vuela: el aire que pasa por su superficie inclinada la empuja hacia arriba, igual que el ala de un avión, extendiendo el tiempo que pasa en el aire y con eso el alcance — muy por encima de lo que predeciría la parábola simple de cap. 3. Es la misma razón por la que el ángulo óptimo de salida de la jabalina es **32°–36°**, más bajo incluso que el de la bala (37°–38°): un ángulo de ataque demasiado alto hace que la jabalina entre en pérdida (*stall*, se frena bruscamente al perder sustentación), igual que le pasaría a un avión que intenta subir con un ángulo demasiado empinado.

En números: la bala convierte su energía en distancia con más "pérdida" (arrastre puro, sin compensación); la jabalina convierte menos energía en más distancia porque parte del trabajo de mantenerla en el aire lo hace el propio aire, no el atleta. Es la misma familia de fenómenos que hace que un frisbee vuele mucho más lejos que una pelota de tenis lanzada con la misma energía.

## Estimación de potencia

Igual que en `03`: masa y velocidad de salida son datos reales (o su punto medio documentado); la duración de la fase final de aceleración (el "latigazo" del brazo, más rápido que la extensión de brazo+tronco de la bala) se estima, no se mide acá, en un rango de **0.08 a 0.15 s**:

| t supuesto (s) | P = K/t, varones (W) |
|---|---|
| 0.08 | ≈ 4 205 W |
| 0.10 | ≈ 3 364 W |
| 0.15 | ≈ 2 243 W |

Estimación central (~0.10 s): **≈ 3.4 kW**. Del mismo orden de magnitud que la bala (`03`, ≈4.8 kW) y que el pico de potencia de Usain Bolt saliendo de los tacos (`05`, ≈2.6 kW) — a pesar de que el objeto, la técnica y la cancha son completamente distintos. Esa convergencia de orden de magnitud entre deportes tan distintos es exactamente el patrón que se explora en `05`.

---
**Fuentes:** World Athletics (récords y especificaciones oficiales de la jabalina y la pista); rango de velocidad de salida y de carrera de lanzadores de elite (biomecánica del lanzamiento de jabalina, revisiones publicadas sobre parámetros de salida); explicación aerodinámica del ángulo de ataque óptimo (32°–36°) por sustentación y pérdida (*stall*).
