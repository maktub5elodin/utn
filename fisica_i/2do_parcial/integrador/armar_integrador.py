"""Arma Integrador_2do_Parcial.md con los ejercicios de los cuatro documentos de 2do_parcial/.

No copia resoluciones a mano: extrae cada ejercicio de su .md de origen y lo
reordena por tema (capítulos del Sears) y por dificultad. Las correcciones se
hacen en el documento de origen y se regeneran con `make`.

Controla que no se pierda nada: todo ejercicio de los documentos de origen
tiene que estar en ORDEN o en REPETIDOS; si no, se detiene.
"""

import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
SALIDA = AQUI / "Integrador_2do_Parcial.md"

# Documentos de origen: clave -> (carpeta, archivo, nombre para el origen, nivel de los títulos de ejercicio)
FUENTES = {
    "V": ("parciales_vella", "Parciales_Vella_Z1054.md", "Parciales de Vella", 3),
    "G": ("guia_extra", "Guia_Extra_2do_Parcial.md", "Guía extra", 3),
    "ET": ("examen_tipo", "Examen_Tipo_Fisica_I.md", "Examen tipo (FRBA)", 2),
    "02": ("parcial_2002", "Parcial_2002_Reconstruido.md", "Parcial 2002", 2),
}

# Evaluación de cada ejercicio de Vella, por la letra del código.
EVAL_VELLA = {
    "H": "evaluación de hidrostática, ago/2020",
    "P": "2º parcial, 1/12/2020",
    "R": "1º recuperatorio, 18/12/2020",
    "Q": "recuperatorio, 23/2/2021",
    "A": "tema A, sin fecha",
    "B": "tema B, sin fecha",
}

# Ejercicios que no se incluyen porque repiten otro: código -> código incluido.
REPETIDOS = {
    ("V", "Q1"): ("V", "R1"),
    ("V", "A1"): ("V", "H2"),
    ("V", "B4"): ("V", "P4"),
    ("G", "MAS3"): ("G", "MAS1"),
    ("G", "F5"): ("V", "P3"),
}

# Nivel: 1 = un concepto; 2 = dos etapas o ecuaciones acopladas; 3 = integra varios temas o tiene trampa.
# Prioridad: alta = tomado en una evaluación real (Vella) o en el examen tipo oficial;
# media = guía extra; baja = enunciado reconstruido o sin datos.
# Cada ejercicio: (fuente, código, nivel, prioridad, comentario breve o "").
BLOQUES = [
    (
        "Energía, cantidad de movimiento y choques",
        "Sears caps. 7 y 8",
        "Conservación de la energía con resortes y rozamiento ($W_{nc} = \\Delta E$), "
        "conservación de la cantidad de movimiento y choques. Es la base de todo lo que sigue: "
        "en los bloques de rígido se vuelve a usar el mismo balance de energía, con un término más.",
        [
            ("G", "R9", 1, "media", "choque plástico; trabajo de las fuerzas internas"),
            ("V", "B2", 1, "alta", "clasificar un choque con los datos"),
            ("ET", "2", 2, "alta", "solo cap. 7: dos pasadas por el tramo con rozamiento"),
            ("G", "R8", 2, "media", "choque y después energía; pregunta conceptual"),
            ("V", "P1", 2, "alta", "choque en el plano, por componentes, y frenado"),
            ("V", "R1", 2, "alta", "tomado dos veces; termina en una cuadrática"),
            ("02", "2", 2, "baja", "datos supuestos: practicar el método"),
            ("02", "1", 3, "baja", "deduce las fórmulas del choque elástico"),
            ("V", "A2", 3, "alta", "el más completo: péndulo, choque elástico, resorte y rozamiento"),
            ("ET", "1", 3, "alta", "suma la dinámica circular del cap. 5 (normal en D)"),
        ],
    ),
    (
        "Energía en el cuerpo rígido",
        "Sears cap. 9 y rodadura del cap. 10",
        "El mismo balance de energía del bloque anterior, ahora con energía cinética de rotación, "
        "$\\tfrac12\\,I\\,\\omega^2$, y la condición de rodadura $v_{\\text{cm}} = \\omega\\,R$. "
        "El rozamiento estático de la rodadura no trabaja.",
        [
            ("G", "R1", 1, "media", "trampa: sin rozamiento la rotación no se convierte en altura"),
            ("V", "P4", 2, "alta", "tomado dos veces: rodadura y resorte"),
            ("ET", "4", 2, "alta", "rodadura y después tiro horizontal (cap. 3)"),
            ("G", "R6", 2, "media", "el inciso a) no se puede calcular con la figura"),
            ("02", "4", 2, "baja", "datos supuestos: polea con masa y resorte"),
            ("V", "R5", 3, "alta", "resorte, polea con masa y dos partículas"),
            ("ET", "3", 3, "alta", "relación de velocidades 2:1; la clave no se reproduce"),
            ("V", "Q4", 3, "alta", "Steiner y tensión en la vertical; tiene un supuesto"),
        ],
    ),
    (
        "Dinámica de rotación: torque y rodadura",
        "Sears cap. 10",
        "Segunda ley para la rotación, $\\tau_z = I\\,\\gamma_z$, junto con la de traslación. "
        "En la rodadura hay que decidir el sentido del rozamiento estático: se supone uno y el signo lo confirma.",
        [
            ("V", "B5", 1, "alta", "eje fijo y aceleración angular constante"),
            ("V", "Q5", 2, "alta", "esfera y aro: $a = g\\,\\mathrm{sen}\\,\\alpha / (1 + c)$"),
            ("V", "A5", 2, "alta", "literal: rozamiento necesario contra $\\mu_s N$"),
            ("G", "R3", 2, "media", "eje fijo con dos masas colgantes"),
            ("02", "3", 2, "baja", "polea con inercia; rozamiento deducido"),
            ("G", "R2", 2, "media", "¿rueda o desliza? Rozamiento necesario contra el disponible"),
            ("V", "P5", 2, "alta", "cuerda en la periferia, plano inclinado"),
            ("V", "R4", 2, "alta", "agrega la energía cinética y su control por trabajo"),
            ("G", "R5", 3, "media", "fuerza horizontal sobre un plano inclinado"),
            ("V", "A4", 3, "alta", "cuerda en un tambor: el rozamiento cambia de sentido según $r$"),
            ("G", "R7", 3, "media", "disco y bloque: $a_{\\text{bloque}} = 2\\,a_{\\text{cm}}$"),
            ("G", "R4", 3, "media", "yo-yo con dos fuerzas en radios distintos"),
        ],
    ),
    (
        "Momento cinético",
        "Sears cap. 10",
        "Momento cinético respecto de un eje fijo, $L_z = I\\,\\omega_z$ para el rígido y "
        "$L_z = x\\,p_y - y\\,p_x$ para una partícula. En un choque contra un cuerpo con eje fijo "
        "no se conserva $\\vec p$ (el eje hace fuerza), pero sí $L_z$ respecto del eje.",
        [
            ("G", "MC1", 2, "media", "energía con un torque de roce y vector $\\vec L$"),
            ("G", "MC2", 3, "media", "choque plástico con eje fijo y después energía; modelo adoptado"),
            ("G", "R10", 3, "media", "choque elástico con eje fijo: $L_z$ y $K$ a la vez"),
        ],
    ),
    (
        "Movimiento periódico (MAS)",
        "Sears cap. 13",
        "Período, amplitud, energía y ecuación horaria del MAS; resorte vertical (el equilibrio se corre $m\\,g/k$), "
        "resortes en serie y péndulo físico.",
        [
            ("V", "Q2", 1, "alta", "amplitud desde el período y la fuerza máxima"),
            ("V", "B3", 1, "alta", "estiramiento de equilibrio desde el período"),
            ("G", "MAS5", 1, "media", "longitudes extremas y velocidad máxima"),
            ("G", "MAS2", 1, "media", "velocidad y aceleración en un punto"),
            ("V", "R2", 2, "alta", "fracciones de energía cinética y potencial"),
            ("V", "P2", 2, "alta", "resorte vertical: período, $v_{\\max}$ y fuerza en el techo"),
            ("G", "MC3", 2, "media", "ecuación horaria y fuerza en el techo"),
            ("G", "MAS4", 2, "media", "amplitud y fase inicial desde otra longitud"),
            ("V", "A3", 2, "alta", "resortes en serie"),
            ("G", "MAS1", 3, "media", "péndulo físico con Steiner"),
        ],
    ),
    (
        "Mecánica de fluidos",
        "Sears cap. 14",
        "Empuje (principio de Arquímedes) en equilibrio y en movimiento, continuidad y Bernoulli. "
        "Es independiente de los bloques anteriores.",
        [
            ("G", "F4", 1, "media", "empuje proporcional al volumen sumergido"),
            ("G", "F3", 1, "media", "esfera atada al fondo"),
            ("V", "H2", 1, "alta", "tomado dos veces: cuerpo entre dos líquidos"),
            ("G", "F1", 1, "media", "densidad del líquido desde la tensión"),
            ("V", "H1", 1, "alta", "el error típico: olvidar el peso del tronco"),
            ("V", "Q3", 2, "alta", "cantidad mínima de troncos"),
            ("V", "R3", 2, "alta", "resorte bajo el agua: ¿estirado o comprimido?"),
            ("V", "B1", 2, "alta", "dinámica con empuje"),
            ("G", "F2", 2, "baja", "sin datos: resuelto en forma literal"),
            ("V", "P3", 2, "alta", "continuidad y Bernoulli; también es el F5 de la guía"),
        ],
    ),
]

# Referencias a otros ejercicios dentro del texto copiado: (fuente, código, texto viejo, plantilla).
# {n:FUENTE:COD} se reemplaza por el número del ejercicio en este documento.
REFERENCIAS = [
    ("V", "A5", "como en Q5:", "como en el ejercicio {n:V:Q5}:"),
    ("G", "R5", "Como en el R2,", "Como en el ejercicio {n:G:R2},"),
    ("G", "MAS1", "El ejercicio 3 de esta sección es idéntico a este.\n\n", ""),
]

# Antes de cada ejercicio, solo en el PDF: si queda menos de un cuarto de página,
# empieza en la siguiente (evita el título y el origen solos al pie).
NO_HUERFANO = """<!-- solo-pdf
```{=latex}
\\par\\penalty-100\\begingroup\\dimen0=\\pagegoal\\advance\\dimen0 by -\\pagetotal
\\ifdim\\dimen0<14\\baselineskip\\newpage\\fi\\endgroup
```
-->"""


def leer_ejercicios(clave):
    """Devuelve {código: (título, cuerpo)} de un documento de origen."""
    carpeta, archivo, _, nivel = FUENTES[clave]
    lineas = (RAIZ / carpeta / archivo).read_text(encoding="utf-8").split("\n")
    if nivel == 3:
        patron = re.compile(r"^### (\w+)(?: — (.*))?$")
    else:
        patron = re.compile(r"^## Problema (\d) — (.*)$")
    corte = re.compile(r"^(## |### )" if nivel == 3 else r"^## ")

    ejercicios = {}
    i = 0
    while i < len(lineas):
        m = patron.match(lineas[i])
        if not m:
            i += 1
            continue
        codigo, titulo = m.group(1), (m.group(2) or "")
        j = i + 1
        while j < len(lineas) and not corte.match(lineas[j]) and lineas[j] != "<!-- solo-md -->":
            j += 1
        cuerpo = lineas[i + 1 : j]
        ejercicios[codigo] = (titulo, limpiar(cuerpo, carpeta))
        i = j
    return ejercicios


def limpiar(cuerpo, carpeta):
    salida = []
    for linea in cuerpo:
        if linea.strip() == "<!-- salto-pagina -->":
            continue
        # Subtítulos de los problemas (### 1.2 a) Velocidad en D) -> #### a) Velocidad en D
        m = re.match(r"^### \d\.\d (.*)$", linea)
        if m:
            linea = "#### " + m.group(1)
        # Figuras: rutas relativas a la carpeta de origen
        linea = linea.replace("](figuras/", f"](../{carpeta}/figuras/")
        salida.append(linea)
    texto = "\n".join(salida).strip("\n")
    texto = re.sub(r"\n+---$", "", texto).strip("\n")
    return texto


def origen(clave, codigo):
    nombre = FUENTES[clave][2]
    if clave == "V":
        texto = f"{nombre} (Z1054) — {EVAL_VELLA[codigo[0]]}, {codigo}"
    elif clave == "G":
        texto = f"{nombre} — {codigo}"
    elif clave == "ET":
        texto = f"{nombre} — problema {codigo}"
    else:
        texto = f"{nombre} (resolución de H. Cassia) — problema {codigo}, enunciado reconstruido"
    repes = [rep for rep, inc in REPETIDOS.items() if inc == (clave, codigo)]
    for rclave, rcod in repes:
        if rclave == "V":
            texto += f"; repetido como {rcod} ({EVAL_VELLA[rcod[0]]})"
        else:
            texto += f"; también es el {rcod} de la {FUENTES[rclave][2].lower()}"
    return texto


def origen_corto(clave, codigo):
    if clave == "V":
        return f"Vella {codigo}"
    if clave == "G":
        return f"Guía {codigo}"
    if clave == "ET":
        return f"Ex. tipo {codigo}"
    return f"2002 P{codigo}"


def main():
    fuentes = {clave: leer_ejercicios(clave) for clave in FUENTES}
    bloques = BLOQUES

    # Numeración global y control de que no falta ni sobra nada.
    numero = {}
    n = 0
    for _, _, _, ejercicios in bloques:
        for clave, codigo, *_ in ejercicios:
            assert codigo in fuentes[clave], f"{clave} {codigo} no existe en el documento de origen"
            assert (clave, codigo) not in numero, f"{clave} {codigo} está dos veces"
            n += 1
            numero[(clave, codigo)] = n
    todos = {(c, cod) for c, ej in fuentes.items() for cod in ej}
    faltan = todos - set(numero) - set(REPETIDOS)
    assert not faltan, f"ejercicios sin ubicar: {sorted(faltan)}"
    for rep, inc in REPETIDOS.items():
        assert rep in todos and inc in numero, (rep, inc)

    cuerpos = {k: fuentes[k[0]][k[1]][1] for k in numero}
    for clave, codigo, viejo, plantilla in REFERENCIAS:
        nuevo = re.sub(r"\{n:(\w+):(\w+)\}", lambda m: str(numero[(m.group(1), m.group(2))]), plantilla)
        assert viejo in cuerpos[(clave, codigo)], f"referencia no encontrada en {clave} {codigo}: {viejo!r}"
        cuerpos[(clave, codigo)] = cuerpos[(clave, codigo)].replace(viejo, nuevo)

    out = []
    w = out.append
    w("# Integrador del 2do parcial de Física I")
    w("")
    w("<!-- Generado por armar_integrador.py a partir de los cuatro documentos de 2do_parcial/. "
      "No editar a mano: corregir el documento de origen y correr make. -->")
    w("")
    w(f"Los {n} ejercicios distintos de los cuatro documentos de `2do_parcial/`, ordenados por tema "
      "y, dentro de cada tema, de menor a mayor dificultad. Los temas siguen el orden de los capítulos "
      "del Sears (11.ª ed. en español; en la 13.ª en inglés, fluidos es el cap. 12 y MAS el 14). "
      "Las resoluciones son las de los documentos de origen, sin cambios.")
    w("")
    w("| Documento de origen | Qué es |")
    w("|---|---|")
    w("| Parciales de Vella (`parciales_vella/`) | evaluaciones del curso Z1054, Prof. R. Vella, 2020–2021, contrastadas con sus resoluciones |")
    w("| Examen tipo (`examen_tipo/`) | examen tipo propuesto por la FRBA, con su clave |")
    w("| Guía extra (`guia_extra/`) | guía de ejercicios extra para el 2do parcial |")
    w("| Parcial 2002 (`parcial_2002/`) | parcial de 2002 del que solo queda la resolución; enunciados reconstruidos |")
    w("")
    w("**Nivel:** 1, un solo concepto; 2, dos etapas o ecuaciones acopladas; 3, integra varios temas o tiene una trampa. "
      "**Prioridad:** alta, tomado en una evaluación real (Vella) o en el examen tipo, y más si se repitió; "
      "media, guía extra; baja, enunciado reconstruido o sin datos (sirve para practicar el método, no para fijarse en los números).")
    w("")
    w("Repetidos, que aparecen una sola vez: " + "; ".join(
        f"{origen_corto(*r)} = {origen_corto(*i)} (ej. {numero[i]})" for r, i in REPETIDOS.items()) + ".")
    w("")
    w("Se usa $g = 10\\ \\text{m/s}^2$. Notación (con el término del Sears en inglés): $\\vec w$ peso (*weight*), "
      "$\\vec N$ normal, $\\vec f$ rozamiento (*friction*), $\\vec B$ empuje (*buoyant force*), $K$ energía cinética, "
      "$U$ energía potencial, $W$ trabajo (*work*), $\\mu_s$ y $\\mu_k$ coeficientes de rozamiento estático y cinético, "
      "$I$ momento de inercia, $\\tau_z$ torque, $\\vec L$ momento cinético (*angular momentum*), $\\gamma_z$ aceleración "
      "angular y $a_{\\text{rad}} = v^2/R$ aceleración radial. Rotación: eje $z$ saliente de la hoja, positivo antihorario; "
      "$\\tau_z = x\\,F_y - y\\,F_x$ y $L_z = x\\,p_y - y\\,p_x$. En las resoluciones, azul = resultado intermedio y "
      "verde = resultado final.")
    w("")
    w("> [!NOTE]")
    w("> Conviene hacer cada ejercicio sin mirar la resolución y después comparar con el resultado en verde.")

    for b, (titulo, caps, descripcion, ejercicios) in enumerate(bloques, 1):
        w("")
        w("<!-- salto-pagina -->")
        w("")
        w(f"## {b}. {titulo} ({caps})")
        w("")
        w(descripcion)
        w("")
        w("| Ej. | Origen | Nivel | Prioridad | Qué tiene |")
        w("|----|----------|-----|---------|-------------------------------------|")
        for clave, codigo, nivel, prioridad, comentario in ejercicios:
            w(f"| {numero[(clave, codigo)]} | {origen_corto(clave, codigo)} | {nivel} | {prioridad} | {comentario} |")
        for clave, codigo, nivel, prioridad, _ in ejercicios:
            titulo_ej = re.sub(r"\s*\(= \w+\)$", "", fuentes[clave][codigo][0])
            w("")
            w(NO_HUERFANO)
            w("")
            w(f"### Ejercicio {numero[(clave, codigo)]} — {titulo_ej}")
            w("")
            w(f"*Origen:* {origen(clave, codigo)}. *Nivel* {nivel}, *prioridad* {prioridad}.")
            w("")
            w(cuerpos[(clave, codigo)])

    w("")
    w("<!-- solo-md -->")
    w("")
    w("---")
    w("")
    w("**Fuentes:** los cuatro documentos de `2do_parcial/` (`parciales_vella/`, `examen_tipo/`, `guia_extra/`, "
      "`parcial_2002/`), con sus propias fuentes y la verificación numérica de cada resultado en sus scripts de figuras. "
      "Orden de temas: Sears, Zemansky, Young y Freedman, *Física universitaria*, vol. 1, 11.ª ed.")
    w("")
    w("<!-- /solo-md -->")
    w("")

    SALIDA.write_text("\n".join(out), encoding="utf-8")
    print(f"{SALIDA.name}: {n} ejercicios en {len(bloques)} bloques")


if __name__ == "__main__":
    main()
