# Comparativa: potencia humana en casos límite

## La tabla

Todas las cifras están redondeadas a dos-tres cifras significativas — son **muestras** (*samples*), no mediciones de laboratorio propias, así que el objetivo es el orden de magnitud y la comparación relativa, no la precisión al vatio.

| Actividad | Potencia | Duración del esfuerzo | Tipo |
|---|---|---|---|
| Empuje casero, 1 kg 1 m en 0.1 s (`02`) | ≈ 2 000 W | ~0.1 s | estimación propia, calculada |
| Jabalina, salida varones (`04`) | ≈ 3 400 W | ~0.1 s | estimación (v y m reales, t supuesto) |
| Usain Bolt, pico saliendo de los tacos (100 m WR, Berlín 2009) | ≈ 2 620 W | <1 s, instantáneo | medido |
| Bala, salida varones (`03`) | ≈ 4 800 W | ~0.15 s | estimación (v y m reales, t supuesto) |
| Halterofilia olímpica, arranque de 56 kg | ≈ 2 140 W | fracción de s | medido |
| Halterofilia olímpica, arranque de 110 kg | ≈ 4 790 W | fracción de s | medido |
| Halterofilia, 2ª tirada (*2nd pull*), atleta ~100 kg | hasta ≈ 5 500 W | fracción de s | medido |
| Ciclismo de ruta, esfuerzo sostenido (Tour de France) | ≈ 500 W | horas | medido, promedio |
| Ciclismo, sprint final | ≈ 1 500 W | segundos | medido, pico |

## Lo que se repite

**Los esfuerzos explosivos de fracción de segundo — lanzar, saltar, arrancar una carrera, la segunda tirada de una arrancada olímpica — convergen todos en el mismo orden de magnitud: 2 000 a 6 000 W**, sin importar si el objeto en movimiento es el propio cuerpo del atleta (Bolt, el levantador) o un objeto externo (la bala, la jabalina). Y **los esfuerzos sostenidos en el tiempo caen un orden de magnitud entero**, a los ~500 W del ciclismo de ruta. No es casualidad: es el mismo patrón de `02` — la potencia escala con `1/t³` para un desplazamiento fijo, así que comprimir el tiempo de aplicación de la fuerza es, matemáticamente, la palanca más fuerte que existe para elevar la potencia. El cuerpo humano no tiene una "potencia máxima" única: tiene una potencia que depende fuertemente de cuánto tiempo se le pide que la sostenga (la misma lógica de una curva de descarga de una batería: más corriente pico, menos tiempo sostenible).

## Sobre la masa del atleta (tu propia pregunta)

La progresión de halterofilia de la tabla — 2 140 W en la categoría de 56 kg contra 4 790 W en la de 110 kg, más del doble — confirma directamente la intuición del planteo original: la masa del atleta importa, y no es un detalle menor. Por `F = m·a` (cap. 4), más masa corporal (más músculo) permite generar más fuerza absoluta, y por `P = F·v`, más fuerza a igual velocidad es más potencia. Es la misma razón física por la que los lanzadores de bala de elite suelen ser considerablemente más pesados que los lanzadores de jabalina: la técnica de bala premia la fuerza bruta aplicada en un recorrido corto (el círculo mide 2.135 m), mientras que la de jabalina premia más la velocidad de todo el cuerpo acumulada en una carrera larga y transferida con precisión.

## Lo que falta para cerrar el círculo (capítulos pendientes)

Esta comparación se queda corta en dos lugares, ambos capítulos que todavía no llegué a estudiar:

```
  Cap. 7 — Potential Energy and Energy Conservation
    → analizar el vuelo de la jabalina como intercambio K ⇄ U:
      en el punto más alto de la trayectoria, toda la energía
      cinética "horizontal" persiste pero la vertical se convirtió
      en energía potencial gravitatoria — hoy en 03/04 el vuelo se
      trató solo como cinemática de proyectil (cap. 3), sin
      contabilizar la energía en cada punto de la trayectoria.

  Cap. 8 — Momentum, Impulse, and Collisions
    → la fase final de cada lanzamiento (lo que en 03/04 estimé
      como "t de aceleración") es, en el lenguaje del cap. 8, un
      problema de impulso: F·Δt = Δp. Con el impulso se podría
      estimar la fuerza promedio real que aplica el atleta sin
      tener que inventar un tiempo — usando el cambio de momentum
      del objeto, que sí es dato conocido (m y Δv).
```

Cuando lleguen esos dos capítulos, esta carpeta suma `06_energia_en_vuelo.md` y `07_impulso_y_la_fuerza_real.md` sobre la misma base de datos ya construida acá — compound knowledge, literal.

---
**Fuentes:** potencia de Usain Bolt (análisis biomecánico del récord mundial de 100 m, Berlín 2009); potencias de halterofilia olímpica (estudios de producción de potencia en levantadores olímpicos, por categoría de peso); potencia de ciclismo de ruta (datos públicos de potenciómetro, Tour de France). Estimaciones propias de `02`, `03` y `04` recalculadas acá para comparación directa.
