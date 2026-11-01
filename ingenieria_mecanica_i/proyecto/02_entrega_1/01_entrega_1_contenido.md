# Entrega 1 — TP Final: Cortadora de Botellas PET (Grupo 1)

> Contenido redactado a partir de `Proyecto Cortadora de Botellas PET.txt` (proyecto completo ya desarrollado por el grupo), reestructurado para cumplir exactamente los requisitos de la Entrega 1 detallados en `00_diseno_entrega_1.md`. El contenido original fue condensado/reordenado donde el profesor exige límites (p. ej. Introducción ≤500 palabras); no se alteraron los conceptos técnicos, decisiones de diseño ni el sentido del proyecto.
>
> Este documento está pensado para pasarse tal cual a un asistente con acceso a internet, que debe completar la sección 3 (Estado del arte) siguiendo las instrucciones de búsqueda incluidas al final de esa sección.

**Título de archivo final:** `Entrega_1_Rev_0_S1091_Grupo_1`
**Formato de texto:** Times New Roman 12, justificado, interlineado 1,15 (aplicar recién en el documento final, no en este markdown).

**Carátula:**

| Campo | Valor |
|---|---|
| Universidad | Universidad Tecnológica Nacional — Buenos Aires |
| Trabajo | Trabajo Práctico Final — Ingeniería Mecánica I |
| Grupo | 1 |
| Curso | S1091 |
| Entrega N° | 1 |
| Revisión N° | 0 |
| Profesor | Abud, Moisés Rolando |
| ATP | Cáceres Guido, Jerónimo |
| Alumnos | Burelli, Angelo (Leg. [COMPLETAR]) · Fernandez, Lautaro (Leg. [COMPLETAR]) · Franco Solignac, Matias (Leg. [COMPLETAR]) · Kainer, Martin (Leg. [COMPLETAR]) · Ledesma Blanco, Camila Cecilia (Leg. [COMPLETAR]) · Paredes, Sergio Gastón (Leg. 260.861-3) |

---

## 1. Introducción

*(439 palabras — límite: 500)*

El incremento sostenido en el consumo de envases plásticos descartables ha generado una creciente acumulación de residuos fabricados en Polietileno Tereftalato (PET), material ampliamente utilizado en la industria alimenticia y de bebidas por su bajo peso, resistencia mecánica y bajo costo de producción.

Si bien el PET es reciclable, una gran proporción de estos envases no recibe un tratamiento adecuado tras su uso. Una de las alternativas de reutilización más difundidas consiste en transformar las botellas en tiras plásticas continuas, empleadas luego en aplicaciones artesanales, domésticas, educativas y semi industriales. Sin embargo, ¿cómo puede obtenerse una tira continua y de ancho uniforme a partir de una botella PET sin depender exclusivamente de la habilidad manual del operador? Los procedimientos manuales existentes presentan limitaciones importantes: la geometría cilíndrica del envase tiende a desplazarse, deformarse o perder alineación respecto de la herramienta de corte, lo que genera tiras de ancho irregular, discontinuidades y un riesgo elevado para el operador, que debe sostener simultáneamente la botella y el elemento cortante.

Para abordar este problema, el presente trabajo desarrolla el diseño conceptual de un dispositivo mecánico de accionamiento manual capaz de generar un corte helicoidal controlado sobre la botella, coordinando su rotación y su desplazamiento longitudinal mediante sistemas de sujeción, guiado y transmisión de movimiento. El enfoque adoptado combina el desarrollo conceptual del mecanismo —fundamentado en principios de cinemática, transmisión de potencia y estabilidad estructural— con la construcción posterior de un prototipo experimental que permita validar el principio de funcionamiento propuesto y analizar el comportamiento de sus componentes.

La originalidad del trabajo radica en integrar, dentro de una misma arquitectura de bajo costo y accionamiento completamente manual, un sistema de sujeción axial (esfera de apoyo y contrapunta regulable), un sistema de guiado longitudinal y un sistema de transmisión mecánica (rodillo motriz por fricción, engranajes reductores y husillo roscado) que coordinan automáticamente la rotación y el avance de la botella — a diferencia de los dispositivos artesanales existentes, en los que ambos movimientos dependen enteramente del operador.

El trabajo resulta relevante porque aplica de manera integrada conceptos fundamentales de ingeniería mecánica —restricción de grados de libertad, fricción, transmisión y conversión de movimiento, estabilidad dinámica— a un problema concreto de reutilización de residuos plásticos, aportando una alternativa tecnológica accesible que favorece la economía circular y sienta bases conceptuales para una eventual evolución industrial del dispositivo.

El presente informe se estructura en una introducción a la problemática, los objetivos del proyecto, un estado del arte sobre antecedentes de dispositivos y soluciones similares, y un marco teórico que describe los principios de ingeniería y la metodología de desarrollo a aplicar en las etapas siguientes del trabajo.

---

## 2. Objetivos

**Principal:**

Desarrollar un dispositivo mecánico de accionamiento manual capaz de transformar botellas de Polietileno Tereftalato (PET) en tiras plásticas continuas mediante un proceso de corte helicoidal controlado, integrando sistemas de sujeción, guiado y transmisión de movimiento.

**Secundarios:**

1. Diseñar un sistema de sujeción axial (esfera de apoyo y contrapunta regulable) que mantenga alineado el eje de rotación de la botella durante el proceso de corte.
2. Diseñar un sistema de guiado longitudinal que controle el desplazamiento axial del envase y garantice un ancho de tira relativamente uniforme.
3. Desarrollar un sistema de accionamiento manual (manivela y rodillo motriz por fricción) junto con un sistema de transmisión mecánica (engranajes reductores y husillo roscado) que coordinen la rotación y el avance longitudinal de la botella.
4. Construir un prototipo experimental que valide el principio de funcionamiento del sistema y permita evaluar el comportamiento real de sus componentes.
5. Analizar la viabilidad de una futura fabricación industrial del dispositivo, considerando materiales y procesos de manufactura compatibles con una escala mayor de producción.

---

## 3. Estado del arte

> **PENDIENTE DE COMPLETAR** — requiere búsqueda bibliográfica con acceso a internet (no realizada en esta sesión). Ver instrucciones de búsqueda al final de esta sección.

*[Espacio para el desarrollo: aquí deben incorporarse 1–2 párrafos que describan qué se sabe sobre el tema a partir de los trabajos citados, vinculándolos explícitamente con el problema y la solución de este proyecto — no alcanza con listar las referencias sueltas, deben citarse dentro del cuerpo del texto en formato *(Apellido, año)*, con la referencia completa en APA al pie o al final.]*

### Instrucciones de búsqueda (para quien complete esta sección con acceso a internet)

**Contexto del proyecto** (ver Introducción y Objetivos de este mismo documento): dispositivo mecánico de accionamiento manual que transforma botellas PET en tiras plásticas continuas mediante corte helicoidal, usando sujeción axial (esfera + contrapunta regulable), guiado longitudinal por carro y guías, transmisión por fricción (manivela + rodillo motriz) y avance sincronizado por engranajes reductores + husillo roscado.

**Qué buscar:** trabajos de investigación (papers, tesis, actas de congreso) publicados **después de 2016**, relacionados con alguno de estos ejes — de mayor a menor afinidad con el proyecto:

1. Dispositivos o máquinas de bajo costo para cortar botellas PET en tiras/hilo plástico continuo (buscar en español e inglés: "cortadora de botellas PET", "plastic bottle cutter", "plastic bottle rope/strip cutting machine", "PET bottle strip cutting device").
2. Reciclaje mecánico y reutilización artesanal/educativa de botellas PET orientada a economía circular ("PET bottle recycling low cost device", "reutilización de PET reciclaje mecánico").
3. Mecanismos de sujeción entre puntos (esfera–contrapunta) o de guiado de piezas cilíndricas flexibles, análogos a los usados en tornos ("center-driven cylindrical workholding", "sujeción entre puntos mecanizado").
4. Transmisión de movimiento por fricción rodillo–superficie cilíndrica ("friction drive roller mechanism").
5. Conversión de movimiento rotacional en lineal mediante husillo roscado/tornillo sin fin en dispositivos de bajo costo o fabricación académica ("screw-driven linear motion low-cost mechanism", "lead screw mechanism design").

**Cómo buscar:** usar [Google Scholar](https://scholar.google.com/) (o buscadores académicos equivalentes), filtrar por año ≥ 2017, y usar el botón "Citar" de Google Scholar para obtener cada referencia ya formateada en **Normas APA**.

**Qué entregar:** mínimo 2 citas en APA (pueden ser más si aportan), integradas en un texto breve — no una simple lista de referencias — que sintetice el estado del conocimiento sobre el tema y lo conecte explícitamente con el enfoque de este proyecto.

---

## 4. Marco teórico

El desarrollo del proyecto se apoya en conceptos fundamentales de ingeniería mecánica vinculados al análisis del movimiento, la transmisión de fuerzas, la estabilidad estructural y el comportamiento de materiales, aplicados de manera integrada durante las etapas de diseño conceptual y construcción del prototipo experimental.

**Restricción de grados de libertad y sistema de guiado.** Se aplican principios de restricción cinemática para limitar los grados de libertad de la botella —cuerpo cilíndrico libre, con múltiples posibilidades de traslación y rotación— permitiendo únicamente la rotación alrededor de su eje longitudinal y el desplazamiento axial controlado necesario para generar la trayectoria helicoidal de corte.

**Transmisión de movimiento por fricción.** El accionamiento manual (manivela + rodillo motriz) se dimensiona en función de las relaciones entre coeficiente de fricción, fuerza normal de contacto y geometría superficial, buscando transmitir el giro a la botella sin deslizamiento ni deformación local del material plástico.

**Conversión y transmisión de energía.** Se utilizan relaciones de transmisión mecánica (engranajes reductores y husillo roscado) para transformar el movimiento rotacional de la manivela en un avance axial controlado, considerando relación de transmisión, torque disponible y velocidad de rotación como variables de diseño.

**Estabilidad dinámica y vibraciones mecánicas.** Se consideran criterios de rigidez estructural, alineación geométrica y distribución de masas para minimizar vibraciones y oscilaciones que puedan afectar la precisión y continuidad del corte.

**Resistencia mecánica y comportamiento del PET.** Se analiza el comportamiento del material frente a esfuerzos de tracción, tensiones locales y fuerzas tangenciales generadas durante la rotación, considerando el espesor de pared y las irregularidades geométricas propias de cada botella.

**Diseño modular, materiales y procesos de manufactura.** El dispositivo se desarrolla bajo un criterio modular que permite analizar, fabricar, ajustar o reemplazar cada subsistema de manera independiente. Se evalúan materiales estructurales (acero, aluminio), materiales de bajo coeficiente de fricción para el sistema de guiado (nylon, PTFE), aceros para herramienta en el sistema de corte, y procesos de manufactura convencionales (mecanizado, plegado de chapa, soldadura), compatibles con una eventual escala industrial.

**Ergonomía y seguridad operativa.** Se aplican criterios básicos de ergonomía orientados a reducir el esfuerzo físico y los riesgos de la manipulación manual de herramientas de corte, disminuyendo la intervención directa del operador sobre el envase y la cuchilla.

**Metodología de desarrollo.** El proyecto se desarrolla en dos etapas. En la primera se completa el diseño conceptual del dispositivo: definición de subsistemas, dimensionamiento preliminar, selección de materiales y verificación cualitativa de los principios mecánicos aplicados (fricción, transmisión, estabilidad). En la segunda etapa se construye un prototipo experimental adaptado a los recursos disponibles en el ámbito académico, con el objetivo de validar el principio de funcionamiento del sistema, verificar la interacción real entre subsistemas y evaluar su desempeño bajo condiciones representativas de uso.

---
*Fuente del contenido técnico: `Proyecto Cortadora de Botellas PET.txt` (secciones 1 "Introducción", 2 "Problemática", 3 "Objetivos" y 7 "Fundamentos de ingeniería aplicados al diseño" del proyecto completo). Reestructurado según `00_diseno_entrega_1.md`.*
