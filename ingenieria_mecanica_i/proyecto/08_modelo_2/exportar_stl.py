# -*- coding: utf-8 -*-
"""
Salidas para imprimir y comprar, por consola:
    ~/Aplicaciones/FreeCAD.AppImage freecadcmd exportar_stl.py

  stl/NN_Pieza.stl     un archivo por pieza impresa, ya apoyado en la cama
  ficha/ficha_impresion.md   pieza, cantidad, material, relleno, soportes, notas (y su PDF)
  compras/lista_compras.md   piezas comerciales, con cantidades contadas del modelo (y su PDF)

Cada STL se vuelve a leer: tiene que ser un sólido cerrado y medir lo mismo
que la pieza. Necesita resultados.json de verificar.py (soportes y tamaños).
"""
import json, math, os, sys

CARPETA = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
sys.path.insert(0, CARPETA)

import FreeCAD as App
import Mesh
import MeshPart

import parametros as P
import piezas as Z

DENS_PLA = 1.24e-3          # [REF] g/mm³
CAUDAL = 9.0                # [SUP] mm³/s medio de la P1S con perfil estándar de 0,2 mm:
                            # la mitad del nominal, por aceleraciones y viajes
SEG_POR_CAPA = 3.0          # [SUP] cambio de capa, retracciones y limpieza
TOL_VOLUMEN = 0.01          # diferencia relativa admitida entre STL y sólido

# Orden de impresión sugerido, y criterio de cada pieza:
# (nombre en el modelo, nombre para la ficha, cantidad, relleno %, perímetros, nota)
# Las notas están escritas para quien imprime, sin contexto del repo.
IMPRESAS = [
    ("Cabezal", "Cabezal (placa)", 1, 40, 4, "primero"),
    ("Calce_9mm", "Calce de 9 mm", 1, 100, 3, "calce"),
    ("Calce_7mm", "Calce de 7 mm", 1, 100, 3, "otros_calces"),
    ("Calce_8mm", "Calce de 8 mm", 1, 100, 3, "otros_calces"),
    ("Calce_10mm", "Calce de 10 mm", 1, 100, 3, "otros_calces"),
    ("Pisador", "Pisador de la hoja", 1, 40, 3, None),
    ("Zocalo", "Zócalo de la varilla", 1, 30, 4, "zocalo"),
    ("Ojal", "Ojal", 1, 20, 3, "ojal"),
    ("Torre", "Torre del carrete", 1, 40, 4, "torre"),
    ("CarreteInferior", "Carrete, disco inferior", 1, 30, 3, "tuerca_m8"),
    ("CarreteSuperior", "Carrete, disco superior", 1, 20, 3, None),
    ("Manivela", "Manivela", 1, 40, 4, "manivela"),
    ("Mango", "Mango", 1, 15, 3, None),
    ("Lastre", "Vaso de lastre", 1, 15, 2, "lastre"),
    ("LabioExterior", "Labio exterior", 1, 40, 4, "primero"),
]
NOTAS = {
    "primero": "Imprimir antes que el resto y probar con una botella real (ver el recuadro de arriba). "
               "En el cabezal, las dos tuercas M3 se colocan desde abajo, después de imprimir.",
    "calce": "Define el ancho de la tira: 100 % de relleno, para que no se aplaste al apretarlo. Mide "
             "8,9 mm a propósito. Medirlo con calibre y anotar el valor real: el laminador puede dejarlo "
             "una décima arriba o abajo.",
    "otros_calces": "Para botellas de pared más gruesa (7 y 8 mm) o más fina (10 mm). Mismo cuidado que "
                    "el de 9 mm; cada uno mide 0,1 mm menos que su nombre.",
    "zocalo": "La tuerca M3 entra de canto por la ranura de arriba. El agujero lateral tiene forma de rombo "
              "a propósito: así se imprime sin soporte.",
    "ojal": "Revisar que la ranura de 1,5 mm quede limpia, sin hilos de plástico.",
    "torre": "Los dos rodamientos entran a presión desde arriba. Si entran muy duros o muy flojos, avisar "
             "al grupo: se ajusta la medida y se reimprime solo esta pieza.",
    "tuerca_m8": "La tuerca M8 entra desde abajo, después de imprimir.",
    "manivela": "La tuerca M8 entra desde abajo. Es la pieza que más trabaja: respetar los 4 perímetros.",
    "lastre": "Opcional: imprimir solo si el grupo lo pide, después de probar la máquina.",
}


def masa_estimada(volumen, relleno):
    """Gramos aproximados: paredes macizas y relleno según el porcentaje."""
    return volumen * DENS_PLA * (0.35 + 0.65 * relleno / 100)


def tiempo_estimado(masa, alto):
    """Minutos aproximados: plástico depositado al caudal medio, más el cambio de capa."""
    return ((masa / DENS_PLA) / CAUDAL + alto / P.CAPA * SEG_POR_CAPA) / 60


def main():
    pz = Z.conjunto(0.0)
    formas = {n: d["forma"] for n, d in pz.items() if d["tipo"] == "impresa"}
    formas.pop("Calce")
    formas.update(Z.calces_todos())
    res = json.load(open(os.path.join(CARPETA, "resultados.json"), encoding="utf-8"))
    imp = res["impresion"]
    os.makedirs(os.path.join(CARPETA, "stl"), exist_ok=True)

    filas, controles, fallas = [], [], []
    for k, (n, titulo, cant, relleno, perim, obs) in enumerate(IMPRESAS, 1):
        f = formas.pop(n).copy()
        f.Placement = Z.a_la_cama(f).multiply(f.Placement)
        malla = MeshPart.meshFromShape(Shape=f, LinearDeflection=0.02, AngularDeflection=0.15,
                                       Relative=False)
        ruta = os.path.join(CARPETA, "stl", f"{k:02d}_{n}.stl")
        malla.write(ruta)
        # relectura
        m2 = Mesh.Mesh(ruta)
        dif = abs(m2.Volume - f.Volume) / f.Volume
        cerrada = m2.isSolid() and not m2.hasNonManifolds()
        b = m2.BoundBox
        en_cama = abs(b.ZMin) < 1e-6
        ok = cerrada and dif <= TOL_VOLUMEN and en_cama
        controles.append({"stl": os.path.basename(ruta), "cerrado": cerrada,
                          "dif_volumen": float(f"{dif:.1e}"), "apoyado": en_cama, "ok": ok})
        if not ok:
            fallas.append(f"{n}: STL cerrado={cerrada}, dif={dif:.1e}, apoyado={en_cama}")
        d = imp[n]
        masa = masa_estimada(f.Volume, relleno)
        filas.append((k, n, cant, relleno, perim, d, masa, tiempo_estimado(masa, b.ZLength), obs, titulo))
    if formas:
        fallas.append(f"piezas impresas sin ficha: {sorted(formas)}")

    puente = max(v["puente_max_mm"] for v in imp.values())
    escribir_ficha(filas, puente)
    res["impresion_total"] = {"masa_g": round(sum(f[6] * f[2] for f in filas)),
                              "tiempo_h": round(sum(f[7] * f[2] for f in filas) / 60, 1),
                              "cabezal": {"masa_g": round(filas[0][6]), "tiempo_min": round(filas[0][7])}}
    escribir_compras(pz)
    res["stl"] = {"archivos": controles, "fallas": fallas}
    with open(os.path.join(CARPETA, "resultados.json"), "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=1)
    return not fallas


def coma(x, dec=0):
    return f"{x:.{dec}f}".replace(".", ",")


def escribir_ficha(filas, puente):
    """ficha/ficha_impresion.md: la lee Maty, sola, en el .md o en el PDF (make ficha_pdf)."""
    total = sum(f[6] * f[2] for f in filas)
    horas = sum(f[7] * f[2] for f in filas) / 60
    numero = {}
    for f in filas:                       # notas numeradas por orden de aparición
        if f[8] and f[8] not in numero:
            numero[f[8]] = len(numero) + 1
    lin = [
        "# Ficha de impresión",
        "",
        "<!-- solo-md -->",
        "",
        "**Cortadora PET 2.0 - Grupo 1, S1091.** 7 de noviembre de 2026. Generada desde el modelo con "
        "`make`: no editar a mano. El PDF (`build/ficha_impresion.pdf`) sale de este mismo archivo.",
        "",
        "<!-- /solo-md -->",
        "",
        "## Configuración común",
        "",
        f"- **Impresora:** Bambu Lab P1S, boquilla de {coma(P.BOQUILLA, 1)} mm, capa de {coma(P.CAPA, 1)} mm.",
        f"- **Material:** {P.MATERIAL}, en todas las piezas.",
        f"- **Sin soportes** en ninguna pieza: no hay voladizos de más de {coma(P.ANG_VOLADIZO)}° y los "
        f"puentes no pasan de {coma(puente, 1)} mm.",
        "- **Cada STL ya está orientado como va en la cama:** abrirlo y laminar, sin rotarlo.",
        "- **Tuercas:** se colocan después de imprimir, en alojamientos abiertos. No hace falta pausar la impresión.",
        "",
        "> [!TIP]",
        "> **Imprimir primero: el cabezal (01), el labio exterior (15) y el calce de 9 mm (02).** Antes de "
        "seguir, probarlos con una botella de 1,5 L lisa, con la base cortada:",
        ">",
        "> 1. Apoyar el labio exterior en su lugar sobre el cabezal, con los agujeros alineados.",
        "> 2. Pasar la pared de la botella entre los dos labios: tiene que entrar sin trabarse y sin quedar "
        "floja, y el borde tiene que llegar hasta el piso.",
        "> 3. Medir el calce con calibre: tiene que dar unos 8,9 mm.",
        ">",
        "> Si algo no va, avisar al grupo antes de imprimir el resto: se ajusta la medida y se reimprimen "
        "solo esas piezas.",
        "",
        "## Piezas",
        "",
        "| N.° | Vista en la cama | Pieza | Archivo | Cant. | Tamaño (mm) | Relleno | Perímetros | Soportes | Peso aprox. | Tiempo aprox. | Nota |",
        "|--|-----|--------|----------|--|------|---|----|----|---|---|--|",
    ]
    for k, n, cant, relleno, perim, d, masa, tmin, obs, titulo in filas:
        t = " × ".join(coma(v, 0) if abs(v - round(v)) < 0.05 else coma(v, 1) for v in d["tamano_mm"])
        sop = "Sí" if d["necesita_soportes"] else "No"
        nota = str(numero[obs]) if obs else "—"
        lin.append(f"| {k:02d} | ![](miniaturas/{n}.png){{width=1.9cm}} | {titulo} | `{k:02d}_{n}.stl` | {cant} | "
                   f"{t} | {relleno} % | {perim} | {sop} | {coma(masa)} g | {coma(tmin)} min | {nota} |")
    lin += [
        "",
        "El tamaño es ancho × profundidad × alto, tal como queda en la cama.",
        "",
        f"**Total: unos {coma(total)} g de PLA y {coma(horas, 1)} h de impresión**, sin contar purgas ni "
        "pruebas. Es una estimación hecha desde el modelo: Bambu Studio da el peso y el tiempo exactos al laminar.",
        "",
        "## Notas",
        "",
    ]
    for clave, k in numero.items():
        lin.append(f"{k}. {NOTAS[clave]}")
    lin.append("")
    os.makedirs(os.path.join(CARPETA, "ficha"), exist_ok=True)
    with open(os.path.join(CARPETA, "ficha", "ficha_impresion.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lin))


def escribir_compras(pz):
    """compras/lista_compras.md: para que el grupo se reparta qué consigue cada uno."""
    n_madera = 3 + len(P.TORNILLOS_CABEZAL) + len(P.TORNILLOS_LABIO) + 2 + 3   # zócalo, placa, labio, ojal, torre
    comprar = [
        ("Varilla lisa Ø8 mm", "1", f"{coma(P.VARILLA_L)} mm", "Eje de la botella. Es el eje liso de las impresoras 3D"),
        ("Tornillo M8 × 60, cabeza hexagonal, rosca completa", "1", "", "Eje del carrete"),
        ("Tuerca M8", "2", "", "Carrete y manivela"),
        ("Arandela M8", "2", "8,4 × 16 mm", "A cada lado de los rodamientos"),
        ("Rodamiento 608ZZ", "2", "8 × 22 × 7 mm", "Torre del carrete"),
        ("Hoja de trincheta de 18 mm", "1 + repuestos", "Segmentable", "Cuchilla"),
        ("Galga de espesores de 0,5 mm (una hoja)", "1", f"Se corta a {coma(P.CHAPITA_LARGO)} × {coma(P.CHAPITA_ANCHO, 1)} mm",
         "Apoyo metálico del borde de la botella. Sirve un segmento de trincheta"),
        ("Tornillo M3 × 25 y tuerca M3", "2 + 2", "", "Aprietan la hoja"),
        ("Tornillo M3 × 16 y tuerca M3", "1 + 1", "", "Traba la varilla"),
        ("Tornillo M5 × 70 y tuerca autoblocante M5", "1 + 1", "", "Eje del mango de la manivela"),
        ("Tornillo para madera 3,5 × 16", str(n_madera), "", "Fijan las piezas impresas a la base"),
        ("Tornillo para madera 3,5 × 45, cabeza fresada", str(len(P.TORNILLOS_TACO)), "", "Taco a la base"),
        ("Tabla de MDF de 18 mm", "1", f"{coma(P.MDF[0])} × {coma(P.MDF[1])} mm y dos recortes de "
         f"{coma(P.CAB_X[1] - P.CAB_X[0])} × {coma(P.CAB_Y[1] - P.CAB_Y[0])} mm",
         "Base y taco. En la maderera la cortan a medida"),
        ("Prensa tipo sargento", "1", "Apertura de 80 mm o más", "Fija la base a la mesa. Si alguien tiene una, no comprarla"),
    ]
    prestado = [
        ("Balanza de equipaje con gancho, o dinamómetro", "1", "", "Medir el tiro (prueba 1)"),
        ("Calibre", "1", "", "Medir la pared de la botella, la tira y el calce"),
        ("Botellas de 1,5 L lisas, con su tapa", "Varias", "", "Para probar y cortar. La tapa se perfora a 9 mm"),
        ("Tuercas o tornillos sueltos", "~100 g", "", "Lastre, solo si la botella no baja sola"),
    ]
    herramientas = [
        ("Destornillador", "1", "Phillips o el que pidan los tornillos", "Armado"),
        ("Llaves o pinza para M8 y M3", "1 juego", "", "Tuercas"),
        ("Taladro", "1", f"Mechas de 9, {coma(P.AGUJERO_TACO)} y 3 mm, y de avellanar", "Tapa, taco y guías de los tornillos"),
        ("Tijera de hojalatero", "1", "", "Cortar la galga (o doblarla hasta que se corte)"),
        ("Guantes", "1 par", "", "Cortar botellas y cambiar la hoja"),
    ]

    def tabla(filas):
        out = ["| Listo | Pieza | Cant. | Medida | Para qué | Quién lo consigue |",
               "|---|------------|-----|---------|------------|-----------|"]
        out += [f"| ☐ | {a} | {b} | {c} | {d} |  |" for a, b, c, d in filas]
        return out + [""]

    lin = [
        "# Lista de compras",
        "",
        "<!-- solo-md -->",
        "",
        "**Cortadora PET 2.0 - Grupo 1, S1091.** Generada desde el modelo con `make`: no editar a mano. "
        "El PDF (`build/lista_compras.pdf`) sale de este mismo archivo.",
        "",
        "<!-- /solo-md -->",
        "",
        "Para repartirse qué consigue cada uno: anotar el nombre en la última columna y tildar la casilla "
        "cuando ya está. Las piezas de plástico las imprime Maty y no están en esta lista.",
        "",
        "## Comprar",
        "",
    ] + tabla(comprar) + ["## Conseguir prestado o juntar", ""] + tabla(prestado) + \
        ["## Herramientas (prestadas)", ""] + tabla(herramientas)
    os.makedirs(os.path.join(CARPETA, "compras"), exist_ok=True)
    with open(os.path.join(CARPETA, "compras", "lista_compras.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lin))


codigo = 1
try:
    codigo = 0 if main() else 1
except Exception:
    import traceback
    with open(os.path.join(CARPETA, "build", "stl_error.txt"), "w") as fh:
        fh.write(traceback.format_exc())
finally:
    sys.stdout.flush()
    os._exit(codigo)
