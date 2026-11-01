# Reparto de la exposición y preparación de la defensa

## 1. Bloques de la exposición

Seis bloques continuos de 2:30, 15 minutos en total. **La asignación de integrantes a cada bloque se define en el grupo.**

| Bloque | Láminas | Tiempo | Contenido |
|---|---|---|---|
| 1 | 1-3 | 0:00 a 2:30 | Apertura, problema y objetivos |
| 2 | 4-5 | 2:30 a 5:00 | Antecedentes y principio de funcionamiento |
| 3 | 6-7 | 5:00 a 7:30 | Proceso de uso y cadena cinemática |
| 4 | 8-9 | 7:30 a 10:00 | Fricción y husillo |
| 5 | 10-11 | 10:00 a 12:30 | Ecuación de diseño y materiales |
| 6 | 12-14 | 12:30 a 15:00 | Planos, validación y conclusiones |

La lámina 15 (bibliografía) es de consulta y no se expone. Cada nota del orador indica el bloque, cuánto tiempo lleva y entre qué minutos. A 115 palabras por minuto, cada bloque da entre 2:04 y 2:18; el resto queda para señalar y para el cambio de orador. Hay que ensayarlo con reloj.

## 2. Preguntas probables

La marca **[E2]** indica que la respuesta sale de la Entrega 2. La marca **[propia]** indica que E2 no lo desarrolla y la respuesta es una propuesta a revisar por el grupo.

### ¿Por qué engranajes y no correa? **[propia]**

Los dientes fijan la relación de transmisión: el avance no pierde la sincronía con el giro por deslizamiento en esa etapa, algo que una correa plana no garantiza. Una correa dentada también sincroniza, pero no la evaluamos.

> Ojo: E2 no compara las dos opciones y el DXF tiene una cota "Unidos por correa". Si el grupo adopta correa, esta respuesta y las láminas 7 y 9 cambian.

### ¿Qué pasa si el rodillo desliza? **[E2]**

El avance del husillo deja de guardar la relación prevista con el giro de la botella, lo que afecta la regularidad del corte. Por eso la presión es regulable y se verifica en los ensayos. Los dientes no resuelven esto: la fricción sigue siendo el eslabón débil.

### ¿Cómo se calcula a? **[E2]**

Se combinan tres relaciones:

- Rodadura sin deslizamiento: `n_b = n_r · D_r / D_b`
- Engranajes: `n_h = n_r / i`
- Husillo: `v = L · n_h`

Como `a = v / n_b`, queda `a = L · D_b / (i · D_r)`. Con `L` = 8 mm, `D_b` = 88 mm, `i` = 2 y `D_r` = 50 mm, da `a` = 8 · 88 / (2 · 50) ≈ 7 mm. Esos valores son de referencia.

### ¿Por qué la cuchilla es fija? **[E2 y proyecto base]**

La botella ya tiene los dos movimientos que generan la hélice, así que la cuchilla no necesita moverse: se regula, se bloquea y queda unida a la base. El proyecto base agrega que así se reduce la complejidad mecánica y mejora la estabilidad del proceso.

### ¿Qué valida el prototipo? **[E2]**

La sujeción, la transmisión del movimiento y la continuidad y uniformidad del corte (objetivo secundario 5). Valida el principio de funcionamiento, no el dimensionamiento del dispositivo real. Los métodos de medición de la lámina 13 son una propuesta **[propia]**.

### ¿Por qué PLA? **[propia]**

Es de bajo costo y fácil de imprimir, y permite corregir piezas rápido. El prototipo valida el principio de funcionamiento, no la resistencia final. La elección todavía está en definición.

### ¿a es igual al ancho de la tira? **[propia]**

E2 lo deja a verificar. Geométricamente, la hélice tiene un ángulo muy chico: con `a` = 7 mm y `D_b` = 88 mm, `tan β = 7 / (π · 88)`, o sea `β` ≈ 1,5°. El ancho perpendicular difiere de `a` menos de un 0,1 %. Falta comprobar el efecto real de la cuchilla y de la deformación del envase.

### ¿Por qué no alcanza con una varilla M8? **[propia]**

Con `L` = 1,25 mm y sin reducción, `a` ≈ 2,2 mm para `D_b` = 88 mm, y una reducción lo achica más. Para reducir y a la vez tener un paso mayor hace falta un husillo de mayor avance por vuelta. Por eso `L` e `i` se eligen juntos.

### ¿Qué pasa con botellas de otro diámetro? **[E2]**

`a` es proporcional a `D_b`: a igual manivela, una botella mayor gira más lento y el carro avanza más por vuelta. Para compensarlo se estudian pares de engranajes intercambiables, además de piezas de sujeción y regulaciones.

### ¿Por qué se quita la base? **[E2]**

Para iniciar el corte desde el borde abierto y aprovechar la zona aproximadamente cilíndrica. El corte avanza hacia el cuello y se detiene antes de la franja del rodillo.

### ¿Cuánta fuerza requiere el corte? **[E2]**

No la tenemos todavía. E2 plantea el límite `F_t ≤ μ_s · N` y determina experimentalmente el intervalo de presión. No vamos a inventar un valor sin ensayo.

### ¿Por qué faltan planos completos? **[E2]**

Los espesores, diámetros y tolerancias se establecen con el dimensionamiento, que está en curso. Lo mostrado es un anteproyecto del conjunto del rodillo.

### ¿La imagen es el diseño real? **[E2]**

No. Es una ilustración conceptual generada con IA: ubica los componentes, pero no define dimensiones. Si preguntan por los engranajes de la imagen, hay que aclarar que muestra el chico sobre el husillo, y que el diseño prevé lo contrario.

---
*Fuentes: `03_entrega_2/Entrega_2_Reentrega_0_S1091_Grupo_1.pdf`, `01_proyecto_base/Proyecto Cortadora de Botellas PET.txt`, `04_material_grafico/Proy Mecanica.dxf`. Supuestos detallados en `contradicciones_y_supuestos.md`.*
