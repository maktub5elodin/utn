# -*- coding: utf-8 -*-
"""
Salidas para imprimir y comprar, por consola:
    ~/Aplicaciones/FreeCAD.AppImage freecadcmd exportar_stl.py

  stl/NN_Pieza.stl     un archivo por pieza impresa, ya apoyado en la cama
  ficha_impresion.md   pieza, cantidad, material, relleno, soportes, observaciones
  lista_compras.md     piezas comerciales, con cantidades contadas del modelo

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
# (nombre, cantidad, relleno %, perímetros, observaciones)
IMPRESAS = [
    ("Cabezal", 1, 40, 4,
     "Placa de 6 mm con el labio interior; va sobre un taco de MDF. Imprimir primero, junto con el "
     "labio exterior (15), y probar con la botella real: la pared tiene que pasar entre los labios "
     "sin trabarse. Las dos tuercas M3 entran desde abajo"),
    ("Calce_9mm", 1, 100, 3,
     "Define el ancho de la tira: macizo, para que no se aplaste al apretar. Mide 0,1 mm menos "
     "que el ancho, porque apoya en el piso de PLA y la chapita queda 0,1 mm más abajo. Medirlo con "
     "calibre: el laminador puede dejarlo 0,1 mm arriba o abajo"),
    ("Calce_7mm", 1, 100, 3, "Para pared de 0,35 mm"),
    ("Calce_8mm", 1, 100, 3, "Para pared de 0,30 mm"),
    ("Calce_10mm", 1, 100, 3, "Para pared de 0,20 mm"),
    ("Pisador", 1, 40, 3, "Aprieta la hoja; caras planas"),
    ("Zocalo", 1, 30, 4, "La varilla lisa entra a presión suave; la traba un tornillo M3 cuya tuerca "
     "entra de canto por la ranura de arriba. El agujero del tornillo es un rombo: así se imprime sin soporte"),
    ("Ojal", 1, 20, 3, "Revisar que la ranura de 1,5 mm quede limpia"),
    ("Torre", 1, 40, 4,
     "Los 608ZZ entran a presión desde arriba. Si entran muy duros o flojos, ajustar D_608_ALOJ "
     "en parametros.py"),
    ("CarreteInferior", 1, 30, 3, "La tuerca M8 entra por abajo. La punta de la tira se engancha en la ranura del núcleo"),
    ("CarreteSuperior", 1, 20, 3, "Disco suelto: lo aprieta la manivela"),
    ("Manivela", 1, 40, 4, "La tuerca M8 entra por abajo. Es la pieza más cargada en flexión"),
    ("Mango", 1, 15, 3, "Gira sobre el tornillo M5"),
    ("Lastre", 1, 15, 2, "Opcional: solo si la botella no baja sola (prueba 2). Se carga con tuercas o "
     "tornillos sueltos, no con arena: hacen falta unos 100 g"),
    ("LabioExterior", 1, 40, 4, "Retiene la chapita; se atornilla al taco con 2 tornillos para madera"),
]


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
    for k, (n, cant, relleno, perim, obs) in enumerate(IMPRESAS, 1):
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
        filas.append((k, n, cant, relleno, perim, d, masa, tiempo_estimado(masa, b.ZLength), obs))
    if formas:
        fallas.append(f"piezas impresas sin ficha: {sorted(formas)}")

    escribir_ficha(filas)
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


def escribir_ficha(filas):
    total = sum(m * c for _, _, c, _, _, _, m, _, _ in filas)
    horas = sum(tm * c for _, _, c, _, _, _, _, tm, _ in filas) / 60
    lin = [
        "# Ficha de impresión: cortadora 2.0",
        "",
        "> Generada por `exportar_stl.py` a partir del modelo: no editar a mano. Para Maty.",
        "",
        "**Configuración común:** PLA, boquilla de 0,4 mm, capa de 0,2 mm, Bambu Lab P1S con placa "
        "texturada o lisa. **Ninguna pieza lleva soportes:** todas se comprobaron sin voladizos de más "
        "de 45° y con puentes de 5,8 mm como máximo. **Cada STL ya está orientado como se imprime:** "
        "abrirlo y laminar, sin rotarlo.",
        "",
        "Las tuercas cautivas se colocan después de imprimir: todos los alojamientos quedan abiertos hacia "
        "abajo o de costado. No hace falta pausar la impresión.",
        "",
        "| N.° | Archivo | Cant. | Tamaño en la cama (mm) | Relleno | Perímetros | Soportes | Peso aprox. | Tiempo aprox. | Observaciones |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for k, n, cant, relleno, perim, d, masa, tmin, obs in filas:
        t = " × ".join(coma(v, 0) if abs(v - round(v)) < 0.05 else coma(v, 1) for v in d["tamano_mm"])
        sop = "Sí" if d["necesita_soportes"] else "No"
        lin.append(f"| {k} | `stl/{k:02d}_{n}.stl` | {cant} | {t} | {relleno} % | {perim} | {sop} | "
                   f"{coma(masa)} g | {coma(tmin)} min | {obs} |")
    lin += [
        "",
        f"**Total aproximado: {coma(total)} g de PLA y {coma(horas, 1)} h de impresión**, sin contar purgas "
        "ni pruebas. Son estimaciones: el peso supone paredes macizas más el relleno indicado, y el tiempo, "
        f"un caudal medio de {coma(CAUDAL)} mm³/s más {coma(SEG_POR_CAPA)} s por capa. Bambu Studio da "
        "los valores exactos al laminar.",
        "",
        "## Antes de imprimir todo",
        "",
        "1. **Primero el cabezal (1), el labio exterior (15) y el calce de 9 mm (2).** Con la botella "
        "real: la pared tiene que entrar entre los labios y el borde tiene que apoyar en la chapita. Si "
        "la pared no entra, aumentar `HOLG_RANURA` en `parametros.py` y volver a correr `make`.",
        "2. **Después la torre (9):** probar el ajuste de los 608ZZ antes de imprimir el carrete.",
        "3. El resto, en cualquier orden.",
        "",
        "## Con la boquilla de 0,2 mm",
        "",
        "La captura de Bambu Studio que mandó Maty usa boquilla de 0,2 mm y capa de 0,10 mm. Con esa "
        "boquilla, estas piezas también se pueden imprimir, pero tardan bastante más; las holguras "
        "se calcularon para 0,4 mm.",
        "",
    ]
    with open(os.path.join(CARPETA, "ficha_impresion.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lin))


def escribir_compras(pz):
    n_madera = 3 + len(P.TORNILLOS_CABEZAL) + len(P.TORNILLOS_LABIO) + 2 + 3   # zócalo, placa, labio, ojal, torre
    filas = [
        ("Varilla lisa Ø8 mm", "1", f"{coma(P.VARILLA_L)} mm", "Eje vertical de la botella. Es el eje lineal de "
         "las impresoras 3D (acero rectificado): la tapa baja y gira sobre una superficie lisa"),
        ("Tornillo M3 × 16 y tuerca M3", "1 + 1", "", "Prisionero que traba la varilla en el zócalo"),
        ("Tornillo M8 × 60, cabeza hexagonal, rosca completa", "1", "DIN 933", "Eje del carrete"),
        ("Tuerca M8", "2", "", "Cautivas en el carrete y en la manivela"),
        ("Arandela M8", "2", "8,4 × 16 × 1,6", "A cada lado de los rodamientos"),
        ("Rodamiento 608ZZ", "2", "8 × 22 × 7 mm", "Torre del carrete"),
        ("Hoja de trincheta de 18 mm", "1 + repuestos", "Segmentable", f"Cuchilla: se usa un tramo de {coma(P.LARGO_HOJA)} mm"),
        ("Galga de espesores de 0,5 mm (una hoja)", "1", f"Se corta a {coma(P.CHAPITA_LARGO)} × "
         f"{coma(P.CHAPITA_ANCHO, 1)} mm", "Chapita: piso de la guía bajo el filo. Sirve también un segmento "
         "de trincheta de 0,5 mm, con el filo hacia afuera de la ranura"),
        ("Tornillo M3 × 25, cabeza cilíndrica, y tuerca M3", "2 + 2", "", "Pisador de la hoja"),
        ("Tornillo M5 × 70", "1", "", "Eje del mango"),
        ("Tuerca autoblocante M5", "1", "", "Bajo el brazo de la manivela"),
        ("Tornillo para madera 3,5 × 16", str(n_madera), "", "Zócalo, placa del cabezal, labio exterior, ojal y torre"),
        ("Tornillo para madera 3,5 × 45, cabeza fresada", str(len(P.TORNILLOS_TACO)), "", "Taco a la base, con la cabeza al ras"),
        ("Tabla de MDF de 18 mm", "1", f"{coma(P.MDF[0])} × {coma(P.MDF[1])} mm, más dos recortes de "
         f"{coma(P.CAB_X[1] - P.CAB_X[0])} × {coma(P.CAB_Y[1] - P.CAB_Y[0])} mm", "Base y taco del cabezal (los dos recortes, encolados o atornillados)"),
        ("Prensa tipo sargento", "1", "Apertura de 80 mm o más", "Fija la base a la mesa, en el extremo libre del lado de la botella"),
        ("Botella de 1,5 L lisa, con su tapa", "Las que se corten", "", "La tapa se perfora a 9 mm"),
        ("Lastre: tuercas o tornillos sueltos", "~100 g", "Opcional", "En el vaso de lastre, si la botella no baja sola"),
        ("Balanza de equipaje o dinamómetro", "1, prestado", "", "Pruebas 1 y 2"),
    ]
    lin = [
        "# Lista de compras: cortadora 2.0",
        "",
        "> Generada por `exportar_stl.py` a partir del modelo: no editar a mano.",
        "",
        "| Pieza | Cantidad | Medida | Para qué |",
        "|---|---|---|---|",
    ] + [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in filas] + [
        "",
        "**Herramientas:** destornillador, llave o pinza para M8 y M3, tijera de hojalatero (o doblar la galga hasta "
        f"cortarla), taladro con mecha de 9 mm para la tapa y de {coma(P.AGUJERO_TACO)} mm para el taco (dos agujeros "
        "bajo los tornillos de la hoja, usando el cabezal de plantilla), mecha de avellanar y mecha fina para guiar "
        "los tornillos en el MDF.",
        "",
    ]
    with open(os.path.join(CARPETA, "lista_compras.md"), "w", encoding="utf-8") as fh:
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
