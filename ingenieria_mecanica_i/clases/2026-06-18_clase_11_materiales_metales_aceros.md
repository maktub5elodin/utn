# Clase 11 — Materiales en la ingeniería: metales, aceros y diagrama Fe-C

**Fecha:** 18 de junio de 2026  
**Profesor:** Abud  
**Nota:** Desde esta clase, el tema cambia a materiales (no es continuación de solicitaciones).  
**Alcance del parcial:** Según Abud, todo hasta esta clase (18/06) entra en el parcial del 02/07.  
**Fuente complementaria:** `abud.docx` provisto por el profesor — usado como base de la clase.

---

## 1. Los metales como materiales de ingeniería

Un **metal** es un material que:
- Conduce bien el calor y la electricidad
- Tiene alta densidad (relativa a otros materiales)
- Refleja la luz (brillo metálico)
- Es sólido a temperatura ambiente (excepción: mercurio)

Se extraen de minerales de rocas y requieren procesos de limpieza/purificación antes de usarse. En ingeniería mecánica, los materiales metálicos son la base de casi todos los componentes estructurales y de máquinas.

---

## 2. Propiedades mecánicas de los materiales

Abud repasó las propiedades fundamentales. Es importante distinguirlas entre sí:

| Propiedad | Definición |
|---|---|
| **Resiliencia** | Energía almacenada durante la deformación **elástica** — lo que el material puede devolver al soltar la carga. Se diferencia de la tenacidad en que solo cuenta la zona elástica. |
| **Tenacidad** | Energía total que el material absorbe **hasta la rotura** (zona elástica + plástica). Material tenaz = difícil de romper de golpe. |
| **Ductilidad** | Capacidad de deformarse sin romperse bajo una fuerza. Los materiales dúctiles pueden estirarse (aluminio, cobre). Lo opuesto es frágil. |
| **Fragilidad** | Se fractura con escasa o nula deformación permanente — rompe sin avisar. Lo contrario de tenaz/dúctil. |
| **Maleabilidad** | Capacidad de extenderse en láminas muy delgadas. Aumenta con el calor. Los más maleables: oro, plata, platino, cobre, estaño, plomo, zinc, hierro, níquel. |
| **Dureza** | Resistencia del material a la penetración localizada en su superficie. |
| **Plasticidad** | Capacidad de deformarse permanentemente cuando se supera el límite elástico — la deformación no se recupera al soltar la carga. |

### La dureza es siempre superficial

Abud lo marcó explícitamente: la dureza se mide siempre en la **superficie** — los ensayos de dureza (Brinell, Rockwell, Vickers) consisten en presionar un indentador contra la superficie y medir la huella. En materiales homogéneos, esa medición representa la dureza del material en todo su volumen. Pero cuando se aplican tratamientos de superficie (temple superficial, cementación), la dureza superficial puede ser muy diferente a la del núcleo.

---

## 3. Clasificación de los metales: ferrosos vs. no ferrosos

```
  METALES
  │
  ├── FERROSOS ── componente principal: HIERRO (Fe)
  │    └── Se subdividen por % de carbono:
  │         ├── Hierro forjado   (< 0,05 % C)
  │         ├── Acero            (0,05 – 2 % C)
  │         └── Fundición        (2 – 4 % C)
  │
  └── NO FERROSOS ── sin hierro como componente principal
       ├── Pesados   (densidad > 5 g/cm³): Cu, Pb, Ni, Zn
       ├── Ligeros   (densidad 2–5 g/cm³): Al, Ti
       └── Ultraligeros (densidad < 2 g/cm³): Mg
```

La distinción entre acero y fundición **no es solo cuantitativa** (% de carbono) — también hay diferencias en su **estructura cristalina** y en cómo se los puede procesar (el acero es dúctil y soldable; la fundición no lo es).

---

## 4. Metales ferrosos: el rol del carbono

El hierro puro por sí solo tiene propiedades mediocres — por eso se le agrega carbono para mejorarlas. El porcentaje de carbono es el parámetro que define todo:

### Hierro forjado (hierro dulce)
- Carbono: muy bajo (0,025 – 0,05 % C)
- Casi hierro puro
- Maleable, soldable por forja, duro pero relativamente frágil
- **Según Abud: el hierro forjado es acero** — en términos prácticos, este material con tan poco carbono ya tiene características de acero de muy bajo carbono
- Usos: estructuras, rejas, puertas, cerraduras

### Acero (0,05 – 2 % C)
- Aleación de hierro y carbono donde el carbono **no supera el 2%**
- Dúctil, tenaz, maleable, soldable, conductor térmico y eléctrico
- Mayor problema: se corroe y oxida — se le agrega cromo y/o níquel como protección
- Ej.: acero 18/10 = 18% Cr + 10% Ni (acero inoxidable)

### Fundición (2 – 4 % C)
- Carbono entre 2 y 4 %
- Muy dura, gran resistencia al desgaste, resistente a la corrosión
- **NO es dúctil ni maleable, NO se puede soldar** — solo se moldea fundiendo y dejando enfriar
- Más barata que el acero
- Usos: carcasas de motores, tapaderas de alcantarilla, soportes de máquinas

### La regla de Abud: menos carbono → más blando
A medida que baja el porcentaje de carbono en el acero, el material se vuelve más blando, más dúctil y más soldable. A mayor carbono: más duro, más resistente al desgaste, pero más frágil y difícil de soldar.

---

## 5. Aceros al carbono: clasificación por % C

| Tipo | % de Carbono | Propiedades principales | Usos típicos |
|---|---|---|---|
| **Bajo carbono** | < 0,25 % | Alta ductilidad y tenacidad, alta soldabilidad, resistencia media-baja | Estructuras, chapas, pernos de baja exigencia |
| **Medio carbono** | 0,25 – 0,55 % | Mejor combinación resistencia/tenacidad | Ejes, árboles, bulones, engranajes, resortes |
| **Alto carbono** | > 0,55 % | Alta resistencia, alta dureza, baja ductilidad, resistencia al desgaste | Rieles, resortes de alta exigencia, rodamientos, herramientas |

---

## 6. Aceros aleados

Los **aceros aleados** contienen, además del hierro y el carbono, otros elementos que mejoran propiedades específicas. Los más comunes: **cromo (Cr), níquel (Ni), molibdeno (Mo), manganeso (Mn), vanadio (V)**.

Cada aleante aporta algo diferente:
- **Cromo**: dureza, resistencia al desgaste, resistencia a la corrosión
- **Níquel**: tenacidad, resistencia al impacto y a bajas temperaturas
- **Molibdeno**: dureza a alta temperatura, resistencia al calor
- **Vanadio**: resistencia a la fatiga
- **Manganeso**: dureza, resistencia al desgaste

---

## 7. Clasificación SAE

La **SAE** (Society of Automotive Engineers) desarrolló un sistema de 4 dígitos para identificar los aceros:

```
  SAE  X  X  X  X
       │  │  └──┘
       │  │   └── % de carbono en centésimas (últimos 2 dígitos)
       │  └─── subserie / aleantes secundarios
       └─── tipo de aleación principal (primer dígito)
```

**Series principales:**

| Serie | Aleante principal |
|---|---|
| 1XXX | Aceros al carbono (sin aleantes adicionales) |
| 2XXX | Aceros al níquel |
| 3XXX | Aceros al cromo-níquel |
| 4XXX | Aceros al molibdeno |
| 5XXX | Aceros al cromo |
| 6XXX | Aceros al cromo-vanadio |
| 8XXX | Aceros al cromo-níquel-molibdeno |

**Ejemplos:**
```
  SAE 1045 → acero al carbono (1) / sin aleantes (0) / 0,45% C (45)
  SAE 4140 → acero al Cr-Mo (4) / Cr 0,9-1,1% y Mo 0,15-0,25% (1) / 0,40% C (40)
  SAE 8620 → acero al Cr-Ni-Mo (8) / 0,5%Ni – 0,5%Cr – 0,25%Mo (6) / 0,20% C (20)
```

**Ejemplos de aplicación mencionados:**
- SAE 3310 (Cr-Ni): engranajes — el cromo aumenta la resistencia al choque
- SAE 4340 (Cr-Mo): pernos de pistón — el molibdeno aporta dureza y resistencia al calor
- SAE 6160 (Cr-V): llaves de ajuste — el vanadio aporta resistencia a la fatiga

---

## 8. Metales no ferrosos: los más importantes

### Aluminio (Al)
- Extracción: mineral bauxita
- Color blanco plateado, muy abundante
- Alta resistencia a la corrosión, muy blando, maleable, dúctil, baja densidad
- Conductor eléctrico y térmico
- Usos: cables de alta tensión, aviones, automóviles, carpintería metálica, envases

### Cobre (Cu)
- Color rojizo, brillo intenso, maleable, dúctil, blando
- Se oxida fácilmente
- Aleaciones: latón (Cu + Zn), bronce (Cu + Sn)
- Usos: cables eléctricos, bobinas de motores, tuberías, radiadores

### Plomo (Pb)
- Color gris plateado, muy denso, muy blando
- Alta plasticidad, maleable, dúctil, tóxico por inhalación
- Se forja en caliente, se enfría muy rápidamente
- Usos: baterías y acumuladores

### Níquel (Ni)
- Color blanco plateado, duro, maleable, dúctil
- Se usa principalmente como recubrimiento protector de metales que se corroen
- Aleación: cuproníquel (Cu + Ni) → monedas

---

## 9. Estructura cristalina y sus efectos

Los metales tienen una **estructura cristalina** interna: sus átomos se organizan en redes regulares (retículas cristalinas). Los tipos más comunes en aceros son:

- **BCC** (Body-Centered Cubic / cúbica centrada en el cuerpo): 1 átomo en cada esquina del cubo + 1 en el centro. Menos densa.
- **FCC** (Face-Centered Cubic / cúbica centrada en las caras): 1 átomo en cada esquina + 1 en el centro de cada cara. Más densa.

**Abud vinculó la estructura cristalina con el momento de inercia**: una estructura más densa (más masa distribuida) tiene mayor momento de inercia a nivel microscópico, lo que afecta cómo el material resiste la deformación. Mayor cantidad de masas por volumen → mayor resistencia intrínseca.

La estructura cristalina puede **cambiar con la temperatura** — y cuando cambia, cambian también las propiedades mecánicas del material. A esto se llama **cambio de fase**.

---

## 10. Cambio de fase y el diagrama Fe-C

Un **cambio de fase** es la transición de un material de una estructura cristalina a otra. No es un cambio de estado (sólido → líquido); el material sigue siendo sólido, pero su red de átomos se reorganiza.

En el hierro y sus aleaciones con carbono, los cambios de fase son el fundamento de todos los tratamientos térmicos.

### El diagrama Fe-C (hierro-carbono)

El **diagrama de equilibrio Fe-C** muestra qué fase (o combinación de fases) existe para cada combinación de temperatura y porcentaje de carbono:

```
  Temperatura
  (°C)
  1538 │· hierro puro se funde aquí
       │
  1147 │─────────────────────────────────── línea eutéctica
       │   ZONA ACEROS  │  ZONA FUNDICIONES
   912 │                │
       │  AUSTENITA (γ) │
   727 │─────────────────────────────── línea eutectoide
       │  FERRITA (α) + PERLITA + CEMENTITA
       │
       └────────────────────────────────── % C
            0    0,8    2       4,3
            │    │      │
            │    │      └── máx. fundición (peor calidad sobre 4%)
            │    └── composición eutectoide (toda perlita al enfriar)
            └── acero muy bajo carbono / hierro forjado
```

### La austenita (γ)

La **austenita** es la fase del hierro que existe a alta temperatura (por encima de ~727°C). Tiene estructura **FCC** y puede disolver mucho más carbono que las fases de baja temperatura.

Al enfriar desde la zona de austenita, dependiendo de la velocidad de enfriamiento y del % de carbono, se obtienen distintas microestructuras:

| Enfriamiento | Resultado | Propiedades |
|---|---|---|
| Muy lento (recocido) | Ferrita + perlita o perlita + cementita | Blando, dúctil |
| Moderado (normalizado) | Perlita fina | Resistencia media |
| Rápido (temple) | Martensita | Muy duro, muy frágil |

> **Concepto clave:** la austenita es el punto de partida de casi todos los tratamientos térmicos — se calienta el acero hasta que forma austenita y luego se controla el enfriamiento para obtener la microestructura deseada.

---

## Resumen de la clase

| Concepto | Definición clave |
|---|---|
| Resiliencia | Energía en zona elástica — lo que el material devuelve |
| Tenacidad | Energía total hasta la rotura |
| Ductilidad | Se deforma sin romperse |
| Dureza | Resistencia superficial a la penetración (siempre superficial) |
| Maleabilidad | Se extiende en láminas |
| Ferrosos / no ferrosos | Con / sin hierro como componente principal |
| Acero | Fe + C ≤ 2% — dúctil, soldable |
| Fundición | Fe + C entre 2 y 4% — dura, no soldable |
| Hierro forjado | Fe con < 0,05% C — según Abud, es acero de muy bajo carbono |
| Bajo C / Medio C / Alto C | < 0,25% / 0,25-0,55% / > 0,55% — más C = más duro, menos dúctil |
| Aceros aleados | Contienen además Cr, Ni, Mo, V, etc. para propiedades específicas |
| Clasificación SAE | 4 dígitos: tipo de aleación + % C; ej. SAE 1045 = 0,45%C sin aleantes |
| Estructura cristalina | BCC o FCC — afecta propiedades mecánicas |
| Cambio de fase | Reorganización cristalina al cambiar temperatura — sin cambio de estado |
| Austenita (γ) | Fase FCC del hierro a alta temperatura — punto de partida de los tratamientos térmicos |

---
*Fuente: apuntes de clase — Prof. Abud, 18/06/2026. Complementado con material del docente (abud.docx).*
