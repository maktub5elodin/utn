r"""Instructivo de armado: escribe instructivo_armado.md y la plantilla de perforación.

Lo lee alguien del grupo que no conoce el proyecto, con las piezas sobre la mesa.
Sigue la secuencia de ../armado.py, la misma que comprueba ../verificar.py. Todos
los números salen de ../parametros.py, del modelo (../build/armado.json, que escribe
../vistas_armado.py) y de ../resultados.json (ficha, compras y cuentas): si cambia
una medida, el instructivo se regenera solo.

Genera:
  - instructivo_armado.md          (el PDF A4 sale de acá, con el pipeline del repo)
  - build/plantilla_base_A3.pdf    plantilla 1:1 en A3 apaisado
  - pasos/plantilla.png            vista reducida de la plantilla, para el .md y el PDF
Uso: python3 generar_instructivo.py   (o `make` desde esta carpeta)
"""
import json
import logging
import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("pgf")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle

AQUI = Path(__file__).parent
MODELO = AQUI.parent
sys.path.insert(0, str(MODELO))
import armado as A  # noqa: E402
import parametros as P  # noqa: E402

logging.getLogger("fontTools").setLevel(logging.ERROR)

RES = json.loads((MODELO / "resultados.json").read_text(encoding="utf-8"))
DAT = json.loads((MODELO / "build" / "armado.json").read_text(encoding="utf-8"))
M = DAT["medidas"]
FUNC = RES["funcionamiento"]


def c(x, dec=None):
    """Número con coma decimal; sin decimales si es entero."""
    if dec is None:
        dec = 0 if abs(x - round(x)) < 0.05 else 1
    return f"{x:.{dec}f}".replace(".", ",")


# ------------------------------------------------------------- piezas y tornillos
FICHA = {f["pieza"]: f for f in RES["ficha"]}


def pz(nombre, cual=None):
    """Pieza impresa con su número de la ficha de impresión."""
    f = FICHA[nombre]
    t = (cual or f["titulo"]).replace(" (", ", ").replace(")", "")    # «Cabezal (placa)» → «cabezal, placa»
    return f"{t[0].lower() + t[1:]} (n.° {f['n']:02d})"


W = P.W
CALCE = DAT["calces"][str(int(W))]
MAD = f"tornillo para madera de {c(P.MADERA_D)} × {c(P.MADERA_L)}"
MAD_TACO = f"tornillo para madera de {c(P.MADERA_D)} × {c(P.TORNILLO_TACO_L)}, cabeza fresada"
GUIA = c(P.MECHA_GUIA)
PASANTE = c(P.MECHA_PASANTE)
X0, Y0 = DAT["base"]["origen"]
AGUJ = DAT["agujeros"]
N_ZOC = sum(a["pieza"] == "Zocalo" for a in AGUJ)
N_OJAL = sum(a["pieza"] == "Ojal" for a in AGUJ)
N_TORRE = sum(a["pieza"] == "Torre" for a in AGUJ)
N_TACO = sum(a["pieza"] == "Taco" for a in AGUJ)
N_PLACA, N_LABIO, N_HOJA = len(P.TORNILLOS_CABEZAL), len(P.TORNILLOS_LABIO), len(P.TORNILLOS_HOJA)
PLACA = P.Z_PISO - P.TACO_ALTO
PROF_GUIA_BASE = max(P.MADERA_L - a["espesor_pieza"] for a in AGUJ if a["espesor_pieza"]) + 1
PROF_TACO_DESDE_ABAJO = P.TORNILLO_TACO_L
PROF_PLACA = P.MADERA_L - P.PISO_BAJO_TORNILLO + 2
PROF_LABIO = P.MADERA_L - P.LABIO_PIE_ESP - PLACA + 2
LENGUETA = math.ceil(M["hoja_a_carrete"] / 50) * 5      # cm, redondeado hacia arriba a 5 cm

# Instrucciones de cada paso de armado.PASOS, por clave:
#   titulo, usa (piezas y tornillería), texto (pasos numerados), comprobar
INSTR = {
    "zocalo": dict(
        titulo="Zócalo",
        usa=[pz("Zocalo"), f"{N_ZOC} × {MAD}"],
        texto=[f"Apoyar el zócalo sobre la base, con sus {N_ZOC} orejas sobre los agujeros guía que se hicieron "
               "con la plantilla. El agujero en forma de rombo del costado mira a la izquierda, hacia el lado del "
               "sargento.",
               f"Atornillar las {N_ZOC} orejas, de a poco y en cruz. Parar cuando la cabeza apoya."],
        comprobar="empujar el zócalo de costado con la mano: no se mueve. El agujero en rombo mira a la izquierda."),
    "tuerca_prisionero": dict(
        titulo="Tuerca del prisionero",
        usa=["1 × tuerca M3"],
        texto=["Meter la tuerca de canto por la ranura de arriba del zócalo, con un vértice hacia abajo, y "
               "empujarla con la punta de un destornillador hasta el fondo."],
        comprobar="mirando por el agujero en rombo se ve el agujero de la tuerca, centrado. Un tornillo M3 "
                  "entra a mano dos vueltas; después sacarlo."),
    "varilla": dict(
        titulo="Varilla",
        usa=[f"1 × varilla lisa Ø{c(P.VARILLA_D)} × {c(P.VARILLA_L)} mm"],
        texto=[f"Limpiar la varilla y meterla desde arriba en el agujero del zócalo, hasta el fondo: entra "
               f"{c(M['varilla_en_zocalo'])} mm."],
        comprobar=f"con una escuadra apoyada en la base, la varilla queda pegada a la escuadra mirando de frente "
                  f"y de costado: está vertical. La punta queda a {c(M['varilla_arriba_de_la_base'])} mm de la base."),
    "prisionero": dict(
        titulo="Prisionero",
        usa=[f"1 × tornillo M3 × {c(P.PRISIONERO_L)}"],
        texto=["Pasar el tornillo por el agujero en rombo, desde la izquierda, y enroscarlo en la tuerca hasta "
               "que apriete la varilla. Firme con los dedos y un cuarto de vuelta más con el destornillador: "
               "no más, el zócalo es de plástico."],
        comprobar="tirar de la varilla hacia arriba y tratar de girarla: no se mueve."),
    "taco": dict(
        titulo="Taco de madera",
        usa=[f"los 2 recortes de MDF de {c(P.CAB_X[1] - P.CAB_X[0])} × {c(P.CAB_Y[1] - P.CAB_Y[0])} mm",
             f"{N_TACO} × {MAD_TACO}", "el sargento, para sostener mientras se atornilla"],
        texto=["Apilar los dos recortes con los cantos parejos y apoyarlos sobre el rectángulo del taco marcado "
               "en la base.",
               "Apretar el taco contra la base con el sargento. Correr la base hasta que el taco quede afuera "
               "del borde de la mesa, para llegar a los agujeros por debajo.",
               f"Por debajo, con mecha de {GUIA} mm, seguir los {N_TACO} agujeros pasantes de la base dentro del taco: "
               f"{c(PROF_TACO_DESDE_ABAJO)} mm de profundidad en total, contando la base (marcar la mecha con cinta).",
               f"Atornillar los {N_TACO} tornillos de cabeza fresada desde abajo."],
        comprobar="los cantos del taco siguen sobre las líneas marcadas. La cabeza de los tornillos queda al ras o "
                  "hundida: apoyada en la mesa, la base no baila."),
    "tuercas_cabezal": dict(
        titulo="Tuercas de la placa",
        usa=[pz("Cabezal", "Cabezal (placa)"), f"{N_HOJA} × tuerca M3"],
        texto=["Dar vuelta la placa: los dos hexágonos están en la cara de abajo, la que apoyó en la cama de la "
               "impresora.",
               "Meter una tuerca en cada hexágono, como se explica en «Cuidados con el plástico»."],
        comprobar=f"las tuercas quedan {c(M['tuerca_m3_hundida'])} mm hundidas: apoyada en la mesa, la placa no "
                  "baila, y al darla vuelta las tuercas no se caen."),
    "cabezal": dict(
        titulo="Placa sobre el taco",
        usa=[pz("Cabezal", "Cabezal (placa)"), f"{N_PLACA} × {MAD}"],
        texto=["Apoyar la placa sobre el taco, con las tuercas abajo y los cantos al ras de los del taco. El labio "
               "curvo queda del lado de la varilla.",
               f"Marcar con el punzón el centro de los {N_PLACA + N_LABIO + N_HOJA} agujeros de la placa y sacarla.",
               f"Agujerear el taco: los {N_PLACA} de las esquinas con mecha de {GUIA} mm y {c(PROF_PLACA)} mm de "
               f"profundidad; los {N_LABIO} del lado de la varilla, para el labio, con mecha de {GUIA} mm y "
               f"{c(PROF_LABIO)} mm; y los {N_HOJA} de las tuercas, donde entran las puntas de los tornillos de la "
               f"hoja, con mecha de {c(P.AGUJERO_TACO)} mm y {c(P.AGUJERO_TACO_PROF)} mm.",
               f"Volver a poner la placa y atornillar los {N_PLACA} tornillos de las esquinas, en cruz."],
        comprobar=f"de la base a la cara de arriba de la placa hay {c(M['placa_arriba_de_la_base'])} mm. Los "
                  "cantos de la placa quedan al ras de los del taco."),
    "chapita": dict(
        titulo="Chapita",
        usa=[f"1 × chapita de galga de {c(P.CHAPITA_ESP)} mm, cortada a {c(P.CHAPITA_LARGO)} × "
             f"{c(P.CHAPITA_ANCHO)} mm"],
        texto=[f"Cortar la galga a {c(P.CHAPITA_LARGO)} mm de largo y repasar los cantos con una lima, sin dejar "
               "rebabas.",
               f"Apoyarla en el rebaje de la placa, junto al labio curvo, con el lado de {c(P.CHAPITA_LARGO)} mm de "
               f"izquierda a derecha. El rebaje tiene {c(M['pozo_chapita'])} mm de profundidad."],
        comprobar=f"una regla apoyada de canto sobre la placa, cruzando la chapita, toca el plástico de los dos "
                  f"lados: la chapita queda {c(M['chapita_bajo_el_piso'])} mm abajo del piso y no sobresale."),
    "labio": dict(
        titulo="Labio exterior",
        usa=[pz("LabioExterior"), f"{N_LABIO} × {MAD}"],
        texto=["Apoyar el labio sobre la placa, con su pie encima de la chapita y los agujeros alineados con los "
               "que se hicieron en el taco.",
               f"Atornillar los {N_LABIO} tornillos, sin pasarse: el pie tiene {c(P.LABIO_PIE_ESP)} mm."],
        comprobar=f"un recorte de pared de botella (sirve un pedazo de la base que se corta) entra entre los dos "
                  f"labios sin trabarse y sin quedar flojo: la ranura mide {c(M['ranura_labios'], 2)} mm. La "
                  "chapita no se puede sacar."),
    "calce": dict(
        titulo="Calce",
        usa=[pz(f"Calce_{int(W)}mm")],
        texto=[f"Medir el calce con calibre: tiene que dar {c(CALCE)} mm. Anotar el valor real.",
               "Apoyarlo sobre la placa, con sus dos agujeros sobre los de las tuercas."],
        comprobar=f"el calce mide {c(CALCE)} mm con calibre. Por sus agujeros se ven las tuercas de la placa."),
    "ojal": dict(
        titulo="Ojal",
        usa=[pz("Ojal"), f"{N_OJAL} × {MAD}"],
        texto=["Apoyar el ojal sobre sus agujeros guía, con la ranura de izquierda a derecha, en línea con la "
               "pared de la botella.",
               f"Atornillar los {N_OJAL} tornillos."],
        comprobar=f"mirando desde el ojal hacia la placa, la ranura apunta al hueco entre los dos labios. Una tira "
                  f"de botella pasa por la ranura de {c(M['ojal_ranura'])} mm sin engancharse."),
    "rodamientos": dict(
        titulo="Rodamientos en la torre",
        usa=[pz("Torre"), "2 × rodamiento 608ZZ", "el caño de PVC de 20 mm"],
        texto=["Se arma en la mano, fuera de la base.",
               "Meter el primer rodamiento por arriba de la torre y llevarlo hasta el escalón del fondo, empujando "
               "con el caño de PVC apoyado en el aro de afuera, como se explica en «Cuidados con el plástico».",
               "Meter el segundo hasta que quede al ras de la cara de arriba, empujando con un taco de madera plano."],
        comprobar=f"el de arriba queda al ras. Entre los dos quedan {c(M['rodamientos_separacion'])} mm. Cada uno "
                  "gira libre al empujarlo con un dedo."),
    "eje_carrete": dict(
        titulo="Eje del carrete",
        usa=[f"1 × tornillo M8 × {c(P.EJE_CARRETE_L)}", "1 × arandela M8"],
        texto=["Poner la arandela en el tornillo y meterlo desde abajo de la torre, por los dos rodamientos. La "
               "cabeza queda dentro del hueco de abajo."],
        comprobar=f"el tornillo asoma {c(M['tornillo_m8_sobre_torre'])} mm arriba de la torre y gira libre con los "
                  "dedos."),
    "torre": dict(
        titulo="Torre sobre la base",
        usa=["la torre con los rodamientos y el tornillo", f"{N_TORRE} × {MAD}"],
        texto=["Apoyar la torre sobre sus agujeros guía, sin que se caiga el tornillo, y atornillar la brida con "
               f"los {N_TORRE} tornillos."],
        comprobar=f"el tornillo sigue girando libre: la cabeza queda {c(M['cabeza_m8_sobre_base'])} mm arriba de "
                  "la base, sin rozarla."),
    "arandela": dict(
        titulo="Arandela de arriba",
        usa=["1 × arandela M8"],
        texto=["Pasar la arandela por el tornillo hasta que apoye en el rodamiento de arriba."],
        comprobar="la arandela apoya en el aro de adentro del rodamiento, no en la torre."),
    "carrete_inferior": dict(
        titulo="Carrete, disco inferior",
        usa=[pz("CarreteInferior"), "1 × tuerca M8"],
        texto=["Meter la tuerca M8 en el hexágono de la cara de abajo del disco (la que apoyó en la cama).",
               "Sostener la punta del tornillo con los dedos y enroscar el disco hasta que apoye en la arandela."],
        comprobar="el disco no toca la torre: entre los dos pasa una hoja de papel. La ranura del núcleo queda "
                  "limpia, sin hilos de plástico."),
    "carrete_superior": dict(
        titulo="Carrete, disco superior",
        usa=[pz("CarreteSuperior")],
        texto=["Pasarlo por el tornillo hasta que apoye en el núcleo."],
        comprobar=f"apoya plano. Entre los dos discos quedan {c(P.ALTO_NUCLEO)} mm, lugar para la tira más ancha."),
    "manivela": dict(
        titulo="Manivela",
        usa=[pz("Manivela"), "1 × tuerca M8"],
        texto=["Meter la tuerca M8 en el hexágono de la cara de abajo de la manivela.",
               "Enroscarla en el tornillo hasta que apoye en el disco superior.",
               "Sostener el carrete con una mano y apretar la manivela girándola en sentido horario, visto desde "
               "arriba: firme con la mano, sin herramientas."],
        comprobar="la manivela y el carrete giran juntos, suaves, sin juego hacia arriba ni hacia abajo."),
    "mango": dict(
        titulo="Mango",
        usa=[pz("Mango"), f"1 × tornillo M5 × {c(P.TORNILLO_MANGO_L)}"],
        texto=["Pasar el tornillo por el mango y por el agujero de la punta de la manivela, desde arriba."],
        comprobar="la cabeza del tornillo apoya en el mango y la rosca asoma por debajo de la manivela."),
    "tuerca_mango": dict(
        titulo="Tuerca del mango",
        usa=["1 × tuerca autoblocante M5"],
        texto=["Enroscar la tuerca por debajo de la manivela hasta que el mango no tenga juego hacia arriba ni "
               f"hacia abajo, pero siga girando libre: entre el mango y la manivela quedan {c(M['mango_juego'])} mm. "
               "La tuerca autoblocante no se afloja sola."],
        comprobar=f"girar la manivela una vuelta completa en sentido horario visto desde arriba: no toca nada. El "
                  f"mango gira libre en la mano y pasa a {c(M['manivela_a_botella'])} mm del lugar de la botella."),
    "botella": dict(
        titulo="Botella",
        usa=["una botella preparada, con su tapa perforada (ver «Primer uso», 1)"],
        texto=["Pasar la varilla por el agujero de la tapa y bajar la botella hasta que el borde cortado apoye "
               "en la chapita, con la pared entre los dos labios.",
               "Girar la botella con la mano hasta que el comienzo de la lengüeta quede donde termina el labio de "
               "afuera, junto al calce, con la lengüeta saliendo hacia la derecha, hacia el ojal."],
        comprobar="la botella gira con la mano sin trabarse y su borde apoya en la chapita, no en el plástico."),
    "hoja": dict(
        titulo="Hoja",
        usa=[f"1 × hoja de trincheta de {c(P.HOJA[0])} mm, de unos {c(P.LARGO_HOJA)} mm de largo", "guantes"],
        texto=["Con guantes. Deslizar la hoja desde atrás, apoyada plana sobre el calce, con el filo mirando a la "
               "izquierda: la pared de la botella llega desde ese lado.",
               f"La punta entra en el comienzo del corte de la lengüeta, {c(M['punta_hoja_dentro'])} mm hacia "
               "adentro de la pared."],
        comprobar=f"la lengüeta queda debajo de la hoja y la botella, arriba. Atrás, la hoja sobresale unos "
                  f"{c(M['hoja_sobresale_afuera'])} mm del calce."),
    "pisador": dict(
        titulo="Pisador",
        usa=[pz("Pisador")],
        texto=["Apoyarlo sobre la hoja, con los agujeros sobre los del calce."],
        comprobar="el pisador y el calce coinciden en sus cuatro cantos."),
    "tornillos_hoja": dict(
        titulo="Tornillos de la hoja",
        usa=[f"{N_HOJA} × tornillo M3 × {c(P.TORNILLO_HOJA_L)}"],
        texto=["Pasar los tornillos por el pisador y el calce, a los costados de la hoja, y enroscarlos en las "
               "tuercas de la placa.",
               "Apretar de a poco, alternando entre los dos, hasta que la hoja no se mueva. Firme, pero sin "
               f"forzar: la punta entra {c(M['tornillo_hoja_en_taco'])} mm en el taco."],
        comprobar="empujar la hoja con la punta de un destornillador, con guantes: no se mueve. El pisador apoya "
                  "parejo, sin luz de un lado."),
    "lastre": dict(
        titulo="Vaso de lastre (solo si hace falta)",
        usa=[pz("Lastre"), f"unos {c(FUNC['agregar_al_vaso_g'])} g de tuercas o tornillos sueltos"],
        texto=["Se pone solo si la botella no baja sola al cortar (ver «Primer uso», 4).",
               f"Pasar el vaso por la varilla hasta que apoye en la tapa y cargarlo con unos "
               f"{c(FUNC['agregar_al_vaso_g'])} g: con el vaso, son unos {c(FUNC['lastre_total_g'])} g sobre la botella."],
        comprobar="el vaso baja por la varilla sin trabarse y queda apoyado en la tapa."),
    "sargento": dict(
        titulo="Sargento a la mesa",
        usa=["1 × sargento"],
        texto=["Poner la base con el extremo izquierdo al borde de la mesa y apretar el sargento sobre el círculo "
               "marcado, con el arco por fuera de la base."],
        comprobar="empujar la base hacia cualquier lado: no se mueve. La manivela gira sin tocar la mesa."),
}
assert list(INSTR) == [p["clave"] for p in A.PASOS], "INSTR tiene que seguir armado.PASOS, en el mismo orden"


# ------------------------------------------------------------------ plantilla A3
PAG = (420.0, 297.0)
MX = (PAG[0] - DAT["base"]["largo"]) / 2
MY = PAG[1] - 15.0 - DAT["base"]["ancho"]
TINTA = "#1f2328"
GRIS = "#6b7280"
NOMBRES = {"Zocalo": "zócalo", "Taco": "taco", "Ojal": "ojal", "Torre": "torre", "Sargento": "sargento"}


def hoja_xy(x, y):
    """Coordenadas del modelo → milímetros en la hoja."""
    return x - X0 + MX, y - Y0 + MY


def area(pts):
    return abs(sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(pts, pts[1:] + pts[:1]))) / 2


def numerar_agujeros():
    """Numera de izquierda a derecha, y de adelante hacia atrás."""
    return sorted(AGUJ, key=lambda a: (round(a["x"] - X0), a["y"]))


def control(ax, x, y, vertical=False):
    """Línea de 100 mm con marcas cada 10 mm."""
    dx, dy = (0, 1) if vertical else (1, 0)
    ax.plot([x, x + 100 * dx], [y, y + 100 * dy], color=TINTA, lw=0.6, solid_capstyle="butt")
    for k in range(11):
        t = 2.5 if k in (0, 5, 10) else 1.5
        px, py = x + 10 * k * dx, y + 10 * k * dy
        ax.plot([px - t * dy, px + t * dy], [py - t * dx, py + t * dx], color=TINTA, lw=0.4)


def plantilla(agujeros):
    plt.rcParams.update({
        "pgf.texsystem": "xelatex", "pgf.rcfonts": False,
        "pgf.preamble": "\n".join([r"\usepackage{fontspec}", r"\setmainfont{Latin Modern Roman}"]),
        "font.family": "serif", "font.size": 9,
    })
    fig = plt.figure(figsize=(PAG[0] / 25.4, PAG[1] / 25.4))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, PAG[0])
    ax.set_ylim(0, PAG[1])
    ax.set_aspect("equal")
    ax.axis("off")
    largo, ancho = DAT["base"]["largo"], DAT["base"]["ancho"]
    ax.add_patch(Rectangle((MX, MY), largo, ancho, fill=False, ec=TINTA, lw=0.9))
    ax.text(MX - 2, MY - 2, "A", ha="right", va="top", fontsize=14, fontweight="bold")
    for dx, dy, t in ((1, 0, "X"), (0, 1, "Y")):          # sentido de las cotas
        ax.annotate("", xy=(MX + 4 + 22 * dx, MY + 4 + 22 * dy), xytext=(MX + 4, MY + 4),
                    arrowprops=dict(arrowstyle="-|>", lw=0.6, color=TINTA))
        ax.text(MX + 4 + 25 * dx + 1.5 * dy, MY + 4 + 25 * dy, t, ha="center", va="center", fontsize=9)
    ax.text(MX + largo / 2, MY + ancho - 4, f"ATRÁS   ·   base de {c(largo)} × {c(ancho)} mm, vista desde arriba",
            ha="center", va="top", fontsize=9, color=GRIS)
    ax.text(MX + largo / 2, MY - 3, "ADELANTE", ha="center", va="top", fontsize=9, color=GRIS)
    ax.text(MX + 4, MY + ancho / 2, "IZQUIERDA", rotation=90, ha="left", va="center", fontsize=9, color=GRIS)
    ax.text(MX + largo - 4, MY + ancho / 2, "DERECHA", rotation=90, ha="right", va="center", fontsize=9, color=GRIS)

    # contornos de las piezas (el de mayor área de cada una)
    for n, wires in DAT["contornos"].items():
        if not wires:
            continue
        w = max(wires, key=lambda pts: area([tuple(p) for p in pts]))
        pts = [hoja_xy(*p) for p in w]
        estilo = "-." if n == "Sargento" else "--"
        ax.add_patch(Polygon(pts, closed=True, fill=False, ec=GRIS, lw=0.6, ls=estilo))
        cx = sum(p[0] for p in pts) / len(pts)
        ymax = max(p[1] for p in pts)
        rot = {"Sargento": "sargento: apretar acá"}.get(n, NOMBRES[n])
        if n == "Zocalo":                                  # adentro: arriba lo toca el taco
            vx, vy = hoja_xy(*DAT["varilla_xy"])
            ax.text(vx, vy + 8, rot, ha="center", va="bottom", fontsize=8, color=GRIS)
        else:
            ax.text(cx, ymax + 1.5, rot, ha="center", va="bottom", fontsize=8, color=GRIS)
        if n == "Taco":                                    # esquinas, para marcar con punzón
            for x, y in [(min(p[0] for p in pts), min(p[1] for p in pts)), (max(p[0] for p in pts), min(p[1] for p in pts)),
                         (min(p[0] for p in pts), max(p[1] for p in pts)), (max(p[0] for p in pts), max(p[1] for p in pts))]:
                ax.add_patch(Circle((x, y), 0.8, fc=TINTA, ec="none"))

    # eje de la varilla
    vx, vy = hoja_xy(*DAT["varilla_xy"])
    for dx, dy in ((1, 0), (0, 1)):
        ax.plot([vx - 6 * dx, vx + 6 * dx], [vy - 6 * dy, vy + 6 * dy], color=GRIS, lw=0.4)
    ax.text(vx, vy - 7, "eje de la varilla", ha="center", va="top", fontsize=7, color=GRIS)

    # agujeros numerados
    for k, a in enumerate(agujeros, 1):
        x, y = hoja_xy(a["x"], a["y"])
        d = P.MECHA_GUIA if a["desde"] == "arriba" else P.MECHA_PASANTE
        ax.add_patch(Circle((x, y), d / 2, fill=False, ec=TINTA, lw=0.5))
        if a["desde"] == "abajo":
            ax.add_patch(Circle((x, y), P.MADERA_CABEZA_D / 2 + 0.5, fill=False, ec=TINTA, lw=0.5, ls=":"))
        for dx, dy in ((1, 0), (0, 1)):
            ax.plot([x - 4 * dx, x + 4 * dx], [y - 4 * dy, y + 4 * dy], color=TINTA, lw=0.3)
        ax.text(x + 3.5, y + 3.5, str(k), fontsize=8, fontweight="bold", ha="left", va="bottom")

    # franja de abajo: control de escala, leyenda y cotas
    ax.text(MX, MY - 12, "Plantilla de perforación de la base - escala 1:1", fontsize=12, fontweight="bold",
            va="top")
    ax.text(MX, MY - 19, "Imprimir en A3 apaisado, al 100 %, sin ajustar a la página. Antes de usarla, medir las dos "
            "líneas de control: tienen que dar 100 mm justos.", fontsize=8.5, va="top")
    control(ax, MX, 30)
    ax.text(MX + 50, 33.5, "control: 100 mm", ha="center", va="bottom", fontsize=8)
    control(ax, MX - 14, MY + ancho - 100, vertical=True)
    ax.text(MX - 18, MY + ancho - 50, "control: 100 mm", rotation=90, ha="right", va="center", fontsize=8)
    ley_y = 22
    ax.add_patch(Circle((MX + 2, ley_y), P.MECHA_GUIA / 2, fill=False, ec=TINTA, lw=0.5))
    ax.text(MX + 6, ley_y, f"guía Ø{GUIA} mm, {c(PROF_GUIA_BASE)} mm de profundidad (zócalo, ojal y torre)",
            fontsize=8, va="center")
    ley_y -= 7
    ax.add_patch(Circle((MX + 2, ley_y), P.MECHA_PASANTE / 2, fill=False, ec=TINTA, lw=0.5))
    ax.add_patch(Circle((MX + 2, ley_y), P.MADERA_CABEZA_D / 2 + 0.5, fill=False, ec=TINTA, lw=0.5, ls=":"))
    ax.text(MX + 7, ley_y, f"pasante Ø{PASANTE} mm, avellanado por abajo (taco)", fontsize=8, va="center")
    ley_y -= 7
    ax.add_patch(Circle((MX + 2, ley_y), 0.8, fc=TINTA, ec="none"))
    ax.text(MX + 6, ley_y, "esquinas del taco: marcarlas y unirlas con lápiz", fontsize=8, va="center")

    # tabla de cotas desde la esquina A
    tx, ty = 250.0, MY - 12
    cols = [(0, "N.°"), (12, "pieza"), (42, "X desde A"), (66, "Y desde A"), (90, "agujero")]
    for dx, t in cols:
        ax.text(tx + dx, ty, t, fontsize=8, fontweight="bold", va="top")
    for k, a in enumerate(agujeros, 1):
        y = ty - 5 - 5 * k
        tipo = f"guía Ø{GUIA}" if a["desde"] == "arriba" else f"pasante Ø{PASANTE}"
        vals = [str(k), NOMBRES[a["pieza"]], f"{c(a['x'] - X0, 1)} mm", f"{c(a['y'] - Y0, 1)} mm", tipo]
        for (dx, _), t in zip(cols, vals):
            ax.text(tx + dx, y, t, fontsize=8, va="top")
    (AQUI / "build").mkdir(exist_ok=True)
    fig.savefig(AQUI / "build" / "plantilla_base_A3.pdf")
    fig.savefig(AQUI / "pasos" / "plantilla.png", dpi=60)
    plt.close(fig)


# ------------------------------------------------------------------ documento
def tabla(encabezado, filas):
    out = ["| " + " | ".join(encabezado) + " |", "|" + "|".join("-" * max(3, len(h)) for h in encabezado) + "|"]
    out += ["| " + " | ".join(f) + " |" for f in filas]
    return "\n".join(out)


def documento(agujeros):
    compras = RES["compras"]
    celdas = [[f"{f['n']:02d}", f["titulo"] + (f" (× {f['cant']})" if f["cant"] > 1 else ""),
               f"![](../ficha/miniaturas/{f['pieza']}.png){{width=1.3cm}}"] for f in RES["ficha"]]
    mitad = math.ceil(len(celdas) / 2)                  # en dos columnas, para que entre en una página
    impresas = tabla(["N.°", "Pieza", "Vista"] * 2,
                     [celdas[k] + (celdas[k + mitad] if k + mitad < len(celdas) else ["", "", ""])
                      for k in range(mitad)])
    comerciales = tabla(["Pieza", "Cant.", "Medida"], [[p, n, m or "—"] for p, n, m, _ in compras["comprar"]])
    herr = [f"- {h}" + (f": {m}" if m else "") + "." for h, _, m, _ in compras["herramientas"]]
    herr += [f"- {h}." for h, _, _, _ in compras["prestado"] if h.startswith("Calibre")]
    cotas = tabla(["N.°", "Pieza", "X desde A", "Y desde A", "Agujero"],
                  [[str(k), {"Zocalo": "Zócalo", "Taco": "Taco", "Ojal": "Ojal", "Torre": "Torre"}[a["pieza"]],
                    f"{c(a['x'] - X0, 1)} mm", f"{c(a['y'] - Y0, 1)} mm",
                    f"guía Ø{GUIA}" if a["desde"] == "arriba" else f"pasante Ø{PASANTE}, avellanar abajo"]
                   for k, a in enumerate(agujeros, 1)])
    anchos = tabla(["Espesor de pared", "Ancho de tira", "Calce", "El calce mide"],
                   [[f"{c(t, 2)} mm", f"{c(w)} mm", pz(f"Calce_{int(w)}mm", f"Calce de {c(w)} mm"),
                     f"{c(DAT['calces'][str(int(w))])} mm"] for t, w in P.ANCHO_SEGUN_PARED])

    L = []
    a = L.append
    a("# Instructivo de armado")
    a("")
    a("<!-- solo-md -->")
    a("")
    a("**Cortadora PET 2.0 - Grupo 1, S1091.** 8 de noviembre de 2026. *Versión preliminar: las medidas se "
      "confirman con las piezas de prueba.* Se genera desde el modelo con `make armado_pdf`: no editar a mano. "
      "El PDF (`build/instructivo_armado.pdf`) y la plantilla A3 (`build/plantilla_base_A3.pdf`) salen de "
      "`generar_instructivo.py`.")
    a("")
    a("![](pasos/portada.png)")
    a("")
    a("<!-- /solo-md -->")
    a("")
    a("## 1. Antes de empezar")
    a("")
    a("### Piezas impresas")
    a("")
    a("El número es el de la ficha de impresión y el de cada archivo. Los calces van uno por vez: el de "
      f"{c(W)} mm es el de la botella común.")
    a("")
    a(impresas)
    a("")
    a("### Piezas compradas")
    a("")
    a(comerciales)
    a("")
    a("### Herramientas")
    a("")
    L.extend(herr)
    a("")
    a("### Seguridad")
    a("")
    a("> [!CAUTION]")
    a("> **La hoja de trincheta corta mucho.** Guantes cada vez que se toca la hoja o se corta una botella. La hoja "
      "va siempre apretada por sus dos tornillos; si se afloja, parar. Nadie pone la mano delante del filo. Para "
      "partir un segmento gastado, usar una pinza, nunca los dedos. Al guardar la máquina, sacar la hoja.")
    a("")
    a("### Cuidados con el plástico")
    a("")
    a("- **No sobreapretar.** Las piezas son de plástico: los tornillos para madera se aprietan hasta que la cabeza "
      "apoya y nada más; los M3, firmes con los dedos y un cuarto de vuelta con el destornillador. Si una rosca "
      "gira en falso, avisar al grupo: no seguir apretando.")
    a("- **Tuercas cautivas** (M3 de la placa, M8 del carrete y de la manivela). Van en hexágonos abiertos de la "
      "cara de abajo. Alinear las caras de la tuerca con las del hexágono y empujarla con el pulgar. Si no entra, "
      "pasar un tornillo de la misma medida desde el otro lado, enroscarlo en la tuerca y apretarlo: la tuerca "
      "entra sola. Después, sacar el tornillo. No martillar.")
    a("- **Rodamientos 608ZZ.** Entran a presión en la torre, siempre empujando el aro de afuera, nunca el de "
      "adentro ni la tapita. Ponerlos derechos, empujar con el pulgar y terminar con el sargento entre dos tacos "
      "de madera, o con golpes suaves sobre un taco. Para el de abajo, empujar con el caño de PVC de 20 mm. Si "
      "entran muy duros o quedan flojos, avisar al grupo: no limar la torre.")
    a("")
    a("### Cómo se nombran los lados")
    a("")
    a("Con la base vista desde arriba y la **esquina A** (marcada en la plantilla) adelante a la izquierda: el "
      "sargento va a la **izquierda**, el carrete a la **derecha**, y la placa de la cuchilla queda **atrás** de la "
      "botella.")
    a("")
    a("## 2. Preparación de la base")
    a("")
    a("### Cortar la madera")
    a("")
    a(f"- **Base:** MDF de {c(P.MDF[2])} mm, {c(P.MDF[0])} × {c(P.MDF[1])} mm.")
    a(f"- **Taco:** dos recortes del mismo MDF, de {c(P.CAB_X[1] - P.CAB_X[0])} × {c(P.CAB_Y[1] - P.CAB_Y[0])} mm. "
      f"Apilados miden {c(P.TACO_ALTO)} mm.")
    a("")
    a("En la maderera los cortan a medida. Los cantos tienen que quedar a escuadra.")
    a("")
    a("### Plantilla de perforación")
    a("")
    a("La plantilla es una hoja A3 aparte: **imprimirla al 100 %, sin ajustar a la página** (en el diálogo de "
      "impresión: «tamaño real»). Si no hay impresora A3, la imprime cualquier fotocopiadora.")
    a("")
    a("1. **Controlar la escala:** medir con regla las dos líneas de control de 100 mm. Si no dan 100 mm justos, "
      "la impresora escaló la hoja: volver a imprimir.")
    a("2. **Pegarla** sobre la cara de arriba de la base con cinta de papel, con el rectángulo de la base sobre los "
      "bordes de la madera y la esquina A sobre la esquina de adelante a la izquierda.")
    a("3. **Marcar con punzón** el centro de cada agujero, las cuatro esquinas del taco y el centro del círculo del "
      "sargento. Sacar la plantilla y unir las esquinas del taco con lápiz.")
    a(f"4. **Agujerear:** los guía, con mecha de {GUIA} mm y {c(PROF_GUIA_BASE)} mm de profundidad (marcar la mecha "
      f"con cinta). Los {N_TACO} del taco, pasantes con mecha de {PASANTE} mm; después, dar vuelta la base y "
      "avellanarlos por abajo hasta que la cabeza del tornillo quede al ras.")
    a("")
    a("<!-- solo-pdf")
    a("\\needspace{6cm}")
    a("-->")
    a("")
    a("Las mismas cotas, para marcar con regla y escuadra si no se pudo imprimir la plantilla:")
    a("")
    a(cotas)
    a("")
    a("![](pasos/plantilla.png){width=13cm}")
    a("")
    a("*Plantilla reducida: no sirve para marcar.*")
    a("")
    a("<!-- salto-pagina -->")
    a("")
    a("## 3. Armado paso a paso")
    a("")
    a("Cada paso tiene una vista: en gris, lo que ya está armado; en naranja, la pieza nueva; la flecha roja "
      "indica por dónde entra. Las vistas de una misma etapa están tomadas desde el mismo lugar.")
    etapa = None
    for i, paso in enumerate(A.PASOS, 1):
        ins = INSTR[paso["clave"]]
        a("")
        a("<!-- solo-pdf")
        a("\\needspace{9cm}")
        a("-->")
        if paso["etapa"] != etapa:
            etapa = paso["etapa"]
            a("")
            a(f"### Etapa {etapa + 1}: {A.ETAPAS[etapa]}")
        a("")
        a(f"#### Paso {i}. {ins['titulo']}")
        a("")
        a(f"![](pasos/paso_{i:02d}.png){{width=8.5cm}}")
        a("")
        a("**Usa:** " + "; ".join(ins["usa"]) + ".")
        a("")
        for k, t in enumerate(ins["texto"], 1):
            a(f"{k}. {t}")
        a("")
        a("> [!TIP]")
        a(f"> **Comprobar:** {ins['comprobar']}")
    a("")
    a("## 4. Primer uso")
    a("")
    a("### 1. Preparar la botella")
    a("")
    a("Botella de 1,5 L lisa, limpia y seca, con su tapa. Con guantes:")
    a("")
    a("1. **Cortar la base** con la trincheta, donde empieza la parte lisa. El borde tiene que quedar parejo: es lo "
      "que apoya en la chapita.")
    a(f"2. **Arrancar la tira:** con tijera, cortar desde el borde una lengüeta de {c(W)} mm de ancho y unos "
      f"{c(LENGUETA)} cm de largo, en espiral, siguiendo el borde con una línea apenas inclinada. Es lo que llega "
      "hasta el carrete.")
    a(f"3. **Perforar la tapa** en el centro, con mecha de {c(P.TAPA_AGUJERO)} mm, apoyada sobre un taco. La varilla "
      f"pasa con {c(M['tapa_a_la_varilla'])} mm de juego.")
    a("")
    a("### 2. Montarla")
    a("")
    a("1. Si la hoja está puesta, aflojar sus dos tornillos y sacar el pisador y la hoja.")
    a(f"2. Montar la botella y la hoja como en los pasos {_n('botella')} a {_n('tornillos_hoja')}.")
    a("3. Pasar la lengüeta por la ranura del ojal, desde arriba.")
    a(f"4. Meter la punta de la lengüeta en la ranura del núcleo del carrete, entre los dos discos: entra "
      f"{c(M['ranura_nucleo'])} mm. Girar la manivela una vuelta, despacio, para que la tira se enrolle sobre su "
      "punta y quede tomada.")
    a("")
    a("### 3. Cortar")
    a("")
    a(f"Girar la manivela **en sentido horario, visto desde arriba**, a ritmo parejo. Una botella son unas "
      f"{c(FUNC['vueltas_manivela'])} vueltas de manivela y unos {c(FUNC['largo_tira_m'], 1)} m de tira. La "
      f"botella gira y baja sola, {c(W)} mm por vuelta.")
    a("")
    a("### 4. Si algo no anda")
    a("")
    a("- **Se traba o cuesta mucho:** parar, no forzar. Girar un poco hacia atrás para aflojar la tira y revisar: "
      "que la tira siga en el ojal, que el borde de la botella siga apoyado en la chapita y que la botella no "
      "tenga restos de etiqueta o de pegamento. Si la hoja no corta parejo, cambiar el segmento (ver "
      "«Mantenimiento»).")
    a(f"- **La botella no baja:** el corte sube por la pared y la tira sale más angosta. Poner el vaso de lastre "
      f"(paso {_n('lastre')}) con unos {c(FUNC['agregar_al_vaso_g'])} g de tuercas. Si sigue sin bajar, avisar al "
      "grupo.")
    a(f"- **La tira sale de otro ancho:** medirla con calibre en varios puntos; tiene que dar {c(W)} ± "
      f"{c(P.TOL_ANCHO)} mm. Si no, revisar el calce y la chapita.")
    a("")
    a("### 5. Al terminar")
    a("")
    a("1. Aflojar los tornillos de la hoja, sacar el pisador y la hoja, y levantar lo que quedó de la botella.")
    a("2. Para sacar el rollo: aflojar la manivela girándola en sentido antihorario mientras se sostiene el carrete, "
      "sacarla junto con el disco superior y deslizar el rollo hacia arriba.")
    a("")
    a("## 5. Mantenimiento")
    a("")
    a("### Cambiar la hoja")
    a("")
    a(f"Con guantes. Aflojar los dos tornillos, sacar el pisador y deslizar la hoja hacia atrás. Partir el segmento "
      f"gastado con una pinza, en la marca, o poner una hoja nueva. Volver a montarla como en los pasos "
      f"{_n('hoja')} a {_n('tornillos_hoja')}.")
    a("")
    a("### Cambiar el calce para otro ancho")
    a("")
    a("El ancho de la tira depende del espesor de la pared de la botella. Para medirla, doblar un pedazo en cuatro, "
      "medir las cuatro capas juntas con calibre y dividir por cuatro.")
    a("")
    a(anchos)
    a("")
    a(f"Sacar los tornillos de la hoja, el pisador y la hoja, cambiar el calce y volver a montar todo como en los "
      f"pasos {_n('hoja')} a {_n('tornillos_hoja')}. Medir los primeros centímetros de tira.")
    a("")
    a("### Revisar la chapita")
    a("")
    a("El borde de la botella apoya y roza sobre la chapita. De vez en cuando, y siempre que la tira salga "
      "despareja, sacar el calce y el labio exterior y mirarla: si tiene un surco que se siente con la uña, darla "
      f"vuelta o cortar una nueva de {c(P.CHAPITA_LARGO)} × {c(P.CHAPITA_ANCHO)} mm.")
    a("")
    return "\n".join(L)


def _n(clave):
    return next(i for i, p in enumerate(A.PASOS, 1) if p["clave"] == clave)


if __name__ == "__main__":
    ags = numerar_agujeros()
    (AQUI / "pasos").mkdir(exist_ok=True)
    plantilla(ags)
    (AQUI / "instructivo_armado.md").write_text(documento(ags), encoding="utf-8")
    print("ok: instructivo_armado.md, build/plantilla_base_A3.pdf y pasos/plantilla.png")
