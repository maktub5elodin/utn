r"""Prueba 1, medir el tiro: escribe prueba_1_tiro.md y el dibujo del armado.

Contenido del anexo A de ../00_concepto.md, armado para imprimir y usar en la
mesa de trabajo, sin haber leído nada más del proyecto. Los umbrales de la
sección final salen de ../parametros.py: si cambia el carrete o la manivela,
cambian solos.

Genera:
  - prueba_1_tiro.md
  - figuras/armado.pdf (vectorial, para el PDF) y figuras/armado.png (vista previa)
Uso: python3 generar_prueba1.py   (o `make` desde esta carpeta)
"""
import logging
import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("pgf")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle

AQUI = Path(__file__).parent
sys.path.insert(0, str(AQUI.parent))
import parametros as P  # noqa: E402

logging.getLogger("fontTools").setLevel(logging.ERROR)

# --- Umbrales: tiro máximo para no pasar F_MANO_MAX en la manivela ----------
def umbral_kg(brazo):
    return math.floor(P.F_MANO_MAX * brazo / P.R_ROLLO_FIN / P.G)


U_80 = umbral_kg(P.R_MANIVELA)
U_120 = umbral_kg(120.0)
assert (U_80, U_120) == (6, 9), (U_80, U_120)    # los del documento conceptual

# --- Dibujo -------------------------------------------------------------------
OUT = AQUI / "figuras"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({
    "pgf.texsystem": "xelatex",
    "pgf.rcfonts": False,
    "pgf.preamble": "\n".join([r"\usepackage{fontspec}", r"\setmainfont{Latin Modern Roman}"]),
    "font.family": "serif",
    "font.size": 9,
})
MADERA, HOJA, PET, TIRA, TINTA = "#d8c3a0", "#9aa3ad", "#bfe6d6", "#2e9e6e", "#22262c"


def nota(ax, texto, punto, lugar, **kw):
    """Rótulo afuera del dibujo, con una línea guía hasta lo que nombra."""
    ax.annotate(texto, xy=punto, xytext=lugar, fontsize=9, ha=kw.get("ha", "center"), va="center",
                arrowprops=dict(arrowstyle="-", lw=0.6, color=TINTA, shrinkA=2, shrinkB=0))


def costado(ax):
    """Vista de costado: tabla, calces, hoja apretada y la pared de la botella."""
    ax.add_patch(Rectangle((0, 0), 110, 10, fc=MADERA, ec=TINTA, lw=0.8))           # tabla
    ax.add_patch(Rectangle((45, 10), 60, 9, fc="#efe6d2", ec=TINTA, lw=0.8))         # calces
    ax.add_patch(Rectangle((8, 19), 97, 1.4, fc=HOJA, ec=TINTA, lw=0.8))             # hoja
    ax.add_patch(Rectangle((55, 20.4), 45, 11, fc=MADERA, ec=TINTA, lw=0.8))         # taco de arriba
    for x in (62, 93):                                                              # tornillos
        ax.add_patch(Rectangle((x - 1.2, 4), 2.4, 30, fc="#6b7280", ec=TINTA, lw=0.5))
        ax.add_patch(Rectangle((x - 3.2, 31.4), 6.4, 2.4, fc="#6b7280", ec=TINTA, lw=0.5))
    ax.add_patch(Rectangle((2, 19), 3, 40, fc=PET, ec=TINTA, lw=0.8))               # pared, arriba del filo
    ax.add_patch(Rectangle((2, 10), 3, 9, fc=TIRA, ec=TINTA, lw=0.8))               # la tira, debajo del filo
    ax.annotate("", xy=(-4, 10), xytext=(-4, 19), arrowprops=dict(arrowstyle="<->", lw=0.8, color=TINTA))
    ax.text(-7, 14.5, "w", ha="right", va="center", fontsize=10)
    nota(ax, "pared de la botella", (2, 45), (-16, 50), ha="right")
    nota(ax, "la tira (lo que se corta)", (2, 14), (-16, 32), ha="right")
    nota(ax, "hoja: el filo mira a la botella", (25, 20.4), (5, 60))
    nota(ax, "taco y tornillos que aprietan", (78, 33.8), (135, 60))
    nota(ax, "calces: unos 9 mm", (105, 15), (122, 18), ha="left")
    nota(ax, "tabla sobre la mesa", (105, 4), (122, 2), ha="left")
    ax.set_title("De costado: la botella y los calces apoyan en la tabla; la hoja queda a w (sin escala)", fontsize=10)
    ax.set_xlim(-80, 185)
    ax.set_ylim(-4, 66)


def arriba(ax):
    """Vista de arriba: la botella gira y la tira sale tangente hacia la balanza."""
    ax.add_patch(Circle((0, 0), 44, fc=PET, ec=TINTA, lw=0.8))
    ax.add_patch(Circle((0, 0), 14, fc="white", ec=TINTA, lw=0.6))
    ax.add_patch(Polygon([(-2, 32), (16, 32), (16, 95), (-2, 95)], fc=HOJA, ec=TINTA, lw=0.8))
    ax.plot([0, 140], [44, 44], color=TIRA, lw=3, solid_capstyle="butt")
    ax.add_patch(Rectangle((140, 32), 66, 24, fc="#e5e7eb", ec=TINTA, lw=0.8))
    ax.text(173, 44, "balanza", ha="center", va="center", fontsize=9)
    ax.add_patch(FancyArrowPatch((210, 44), (262, 44), arrowstyle="-|>", mutation_scale=12, lw=1.2, color=TINTA))
    ax.text(236, 62, "tirar parejo", ha="center", fontsize=9)
    ax.add_patch(FancyArrowPatch((-30, -36), (30, -36), connectionstyle="arc3,rad=0.35",
                                 arrowstyle="-|>", mutation_scale=10, lw=0.9, color=TINTA))
    nota(ax, "tapa", (0, 0), (-80, 0))
    nota(ax, "hoja", (16, 80), (55, 88))
    nota(ax, "tira", (100, 44), (100, 18))
    ax.text(0, -62, "la botella gira sola", ha="center", fontsize=9)
    ax.set_title("Desde arriba: la tira sale derecha, tangente a la botella", fontsize=10)
    ax.set_xlim(-120, 280)
    ax.set_ylim(-72, 105)


fig, (a, b) = plt.subplots(2, 1, figsize=(6.2, 3.55), gridspec_kw={"height_ratios": [1, 1.1]})
for ax in (a, b):
    ax.set_aspect("equal")
    ax.axis("off")
costado(a)
arriba(b)
fig.savefig(OUT / "armado.pdf", bbox_inches="tight")
fig.savefig(OUT / "armado.png", bbox_inches="tight", dpi=150)
plt.close(fig)

# --- Documento ------------------------------------------------------------------
MD = f"""# Prueba 1: medir el tiro

<!-- solo-md -->

**Cortadora PET 2.0 - Grupo 1, S1091.** Hoja para imprimir y usar en la mesa de trabajo. Se genera con
`make` desde `generar_prueba1.py`: no editar a mano.

<!-- /solo-md -->

**Para qué sirve:** saber cuánta fuerza hace falta para tirar de la tira de plástico mientras una cuchilla
fija corta la botella. Con ese número se confirma el carrete y la manivela de la máquina. No hace falta
imprimir nada: alcanza con una tabla, una trincheta y una balanza de equipaje. Lleva media hora y dos personas.

> [!CAUTION]
> **Seguridad:** guantes todo el tiempo. La hoja siempre bien apretada. Nadie pone la mano delante del filo.
> Al terminar, sacar la hoja y guardarla.

## Materiales

- ☐ Una botella de 1,5 L lisa, limpia y seca, **con su tapa**.
- ☐ Una trincheta con hoja nueva de 18 mm.
- ☐ Una tabla de madera de unos 30 × 15 cm y un taco chico de unos 3 cm de alto.
- ☐ Calces para levantar la hoja unos 9 mm: arandelas, palitos de helado o cartón apilados.
- ☐ Dos tornillos con arandela, o una prensa chica (sargento), para apretar la hoja.
- ☐ Una balanza de equipaje con gancho; mejor si marca el máximo.
- ☐ Regla o calibre, tijera, marcador, un lápiz y guantes.

## Armado

![](figuras/armado.png)

1. **Cortar la base de la botella** con la trincheta, donde empieza la parte lisa. Despacio y con guantes:
   el borde tiene que quedar lo más parejo posible.
2. **Armar la cuchilla.** Sobre la tabla, cerca de un borde, apilar los calces hasta unos 9 mm. Apoyar la
   hoja encima, con el filo hacia la parte libre de la tabla, sobresaliendo unos 2 cm de los calces. Apretarla
   con el taco y los tornillos, o con la prensa. **La hoja no se tiene que mover.**
3. **Medir la altura real** desde la tabla hasta el filo: ese es el ancho de la tira, `w`. Anotarlo.
4. **Arrancar la tira.** Con la tijera, cortar en la botella una lengüeta de ese mismo ancho y unos 10 cm
   de largo, desde el borde hacia arriba, con una línea apenas inclinada.
5. **Atar la punta** de la tira a un lápiz y colgar del lápiz el gancho de la balanza.

<!-- salto-pagina -->

## Medición

1. Parar la botella con el pico arriba y el borde cortado apoyado **sobre la tabla**, al lado del filo.
   Meterla de modo que **la hoja entre en el corte**: la pared pasa entre la tabla y la hoja.
2. Quien ayuda apoya **una mano suave sobre la tapa**, solo para que la botella no se caiga y pueda girar.
3. **Tirar de la balanza despacio y parejo**, en línea recta, a la altura de la tabla y tangente a la botella:
   la tira sale derecha, sin subir ni bajar. La botella gira sola.
4. Mirar la balanza mientras se tira. **Tiro medio:** el valor que más se repite con el corte andando parejo.
   **Tiro máximo:** el pico más alto, por ejemplo al arrancar o si se traba.
5. Cortar unos 50 cm, frenar y anotar. **Repetir tres veces** en la misma botella.
6. Al final, medir el **ancho de la tira** en cinco puntos y el **espesor de pared** en un pedazo. Si el
   calibre no llega a medir tan fino: doblar un pedazo de tira en cuatro, medir las cuatro capas juntas y
   dividir por cuatro.

## Qué anotar

| Dato | Medición 1 | Medición 2 | Medición 3 |
|------------|-------|-------|-------|
| Marca y tipo de botella |  |  |  |
| Diámetro de la botella (mm) |  |  |  |
| Espesor de pared (mm) |  |  |  |
| Altura del filo, `w` (mm) |  |  |  |
| Ancho de la tira en 5 puntos (mm) |  |  |  |
| Tiro medio (kg) |  |  |  |
| Tiro máximo (kg) |  |  |  |
| ¿La botella bajó sola, o hubo que empujarla? |  |  |  |
| Observaciones: se trabó, se rompió la tira, se movió la hoja… |  |  |  |

**Para pasar a newtons:** la balanza marca kilos; multiplicar por 9,8. Por ejemplo, 3 kg son unos 29 N.

## Cómo se usa el resultado

Se mira el **tiro medio**:

- **Hasta {U_80} kg:** la máquina va con el carrete movido directo por la manivela, con brazo de 80 mm.
- **Entre {U_80} y {U_120} kg:** hace falta un brazo de manivela más largo, de 120 mm.
- **Más de {U_120} kg:** antes de cambiar la máquina, revisar el filo y el ángulo de la hoja, y repetir la prueba.

La fila "¿bajó sola?" adelanta la prueba siguiente: si la botella bajó sola con la mano apoyada encima, la
idea de que avance sola va bien encaminada.
"""
(AQUI / "prueba_1_tiro.md").write_text(MD, encoding="utf-8")
print("ok: prueba_1_tiro.md y figuras/armado (.pdf + .png)")
