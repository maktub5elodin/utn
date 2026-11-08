# -*- coding: utf-8 -*-
"""
Secuencia de armado del modelo 2.0: una sola lista, que usan verificar.py
(cada pieza llega a su lugar sin atravesar lo ya armado) y el instructivo de
armado (instructivo/), que la sigue paso por paso. Sin FreeCAD: se importa
también desde el python del sistema.

Cada paso:
  clave      nombre corto, para enlazar las instrucciones del instructivo
  nombre     descripción del control en verificar.py
  etapa      índice en ETAPAS
  mueven     piezas que entran juntas
  direc      dirección en que entran (llegan desde -direc)
  recorrido  mm que se barren antes de llegar
  contra     None: contra todo lo ya armado; si no, solo esas piezas
             (subconjuntos que se arman aparte, fuera de la base)
"""

ETAPAS = [
    "Eje de la botella",
    "Cabezal",
    "Ojal",
    "Carrete y manivela",
    "Botella",
    "Cuchilla",
    "Lastre y sujeción a la mesa",
]


def _p(clave, nombre, etapa, mueven, direc, recorrido, contra=None):
    return {"clave": clave, "nombre": nombre, "etapa": etapa, "mueven": mueven,
            "direc": direc, "recorrido": recorrido, "contra": contra}


ABAJO, ARRIBA = (0, 0, -1), (0, 0, 1)
PASOS = [
    _p("zocalo", "Zócalo sobre la base", 0, ["Zocalo"], ABAJO, 40),
    _p("tuerca_prisionero", "Tuerca M3 del prisionero, por su ranura", 0, ["TuercaPrisionero"], ABAJO, 20),
    _p("varilla", "Varilla lisa en el zócalo, desde arriba", 0, ["Varilla"], ABAJO, 60),
    _p("prisionero", "Prisionero, desde afuera", 0, ["Prisionero"], (1, 0, 0), 20),
    _p("taco", "Taco de MDF sobre la base", 1, ["Taco"], ABAJO, 60),
    _p("tuercas_cabezal", "Tuercas M3 al cabezal, desde abajo", 1, ["TuercasHoja"], ARRIBA, 20, ["Cabezal"]),
    _p("cabezal", "Cabezal sobre el taco", 1, ["Cabezal", "TuercasHoja"], ABAJO, 40),
    _p("chapita", "Chapita en su rebaje, desde arriba", 1, ["Chapita"], ABAJO, 20),
    _p("labio", "Labio exterior, sobre la chapita", 1, ["LabioExterior"], ABAJO, 30),
    _p("calce", "Calce", 1, ["Calce"], ABAJO, 30),
    _p("ojal", "Ojal", 2, ["Ojal"], ABAJO, 60),
    _p("rodamientos", "Rodamientos a la torre, desde arriba", 3, ["Rodamientos"], ABAJO, 40, ["Torre"]),
    _p("eje_carrete", "Tornillo M8 a la torre, desde abajo", 3, ["EjeCarrete"], ARRIBA, 70,
       ["Torre", "Rodamientos"]),
    _p("torre", "Torre sobre la base", 3, ["Torre", "Rodamientos", "EjeCarrete"], ABAJO, 60),
    _p("arandela", "Arandela sobre el rodamiento", 3, ["ArandelaCarrete"], ABAJO, 40),
    _p("carrete_inferior", "Carrete inferior con su tuerca, enroscado", 3, ["CarreteInferior", "TuercaCarrete"],
       ABAJO, 40),
    _p("carrete_superior", "Disco superior del carrete", 3, ["CarreteSuperior"], ABAJO, 30),
    _p("manivela", "Manivela con su tuerca, enroscada", 3, ["Manivela", "TuercaManivela"], ABAJO, 40),
    _p("mango", "Mango y su tornillo, desde arriba", 3, ["Mango", "TornilloMango"], ABAJO, 80),
    _p("tuerca_mango", "Tuerca del mango, desde abajo", 3, ["TuercaMango"], ARRIBA, 20),
    _p("botella", "Botella con su tapa, bajando por la varilla", 4, ["Botella", "Tapa"], ABAJO, 400),
    _p("hoja", "Hoja, deslizada desde afuera por la lengüeta", 5, ["Hoja"], (0, -1, 0), 70),
    _p("pisador", "Pisador", 5, ["Pisador"], ABAJO, 30),
    _p("tornillos_hoja", "Tornillos de la hoja", 5, ["TornillosHoja"], ABAJO, 40),
    _p("lastre", "Vaso de lastre, opcional", 6, ["Lastre"], ABAJO, 60),
    _p("sargento", "Sargento a la mesa", 6, ["Sargento"], ABAJO, 40),
]
