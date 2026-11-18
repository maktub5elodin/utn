#!/usr/bin/env python3
"""Datos medidos por el grupo en el prototipo y estadística del ancho de tira.

Única fuente de los valores medidos que usa el informe: ni el promedio ni el
desvío se escriben a mano. Solo biblioteca estándar. Son las únicas
mediciones: el largo de la tira, el tiempo por botella y el tiro no se midieron.

  python3 anchos_medidos.py          imprime la tabla
  python3 anchos_medidos.py --json   imprime los valores en JSON
"""
import json
import statistics
import sys

CALCE_MM = 9.0                                  # ancho nominal (espesor del calce)
TOLERANCIA_MM = 0.5                             # criterio w ± 0,5 mm
ANCHOS_MM = [9.79, 10.79, 8.73, 9.36, 10.47]    # 5 puntos, medidos por el grupo
VARILLA_MM = 7.3                                # varilla de acero del prototipo (diseño: Ø8)


def medidos():
    return {"varilla_mm": VARILLA_MM}


def estadistica():
    n = len(ANCHOS_MM)
    media = statistics.mean(ANCHOS_MM)
    desvio = statistics.stdev(ANCHOS_MM)        # muestral (n − 1)
    lo, hi = CALCE_MM - TOLERANCIA_MM, CALCE_MM + TOLERANCIA_MM
    dentro = sum(lo <= a <= hi for a in ANCHOS_MM)
    return {
        "nominal_mm": CALCE_MM,
        "tolerancia_mm": TOLERANCIA_MM,
        "mediciones_mm": ANCHOS_MM,
        "n": n,
        "media_mm": round(media, 2),
        "desvio_mm": round(desvio, 2),
        "minimo_mm": min(ANCHOS_MM),
        "maximo_mm": max(ANCHOS_MM),
        "rango_mm": round(max(ANCHOS_MM) - min(ANCHOS_MM), 2),
        "desvio_medio_nominal_mm": round(media - CALCE_MM, 2),
        "dentro_criterio": dentro,
        "dentro_criterio_txt": f"{dentro} de {n}",
    }


def coma(x, dec=2):
    return f"{x:.{dec}f}".replace(".", ",")


if __name__ == "__main__":
    e = estadistica()
    if "--json" in sys.argv:
        print(json.dumps(e, ensure_ascii=False, indent=2))
    else:
        print("| Magnitud | Valor |")
        print("|---|---|")
        print("| Mediciones (mm) | " + "; ".join(coma(a) for a in e["mediciones_mm"]) + " |")
        print(f"| Promedio (mm) | {coma(e['media_mm'])} |")
        print(f"| Desvío estándar muestral (mm) | {coma(e['desvio_mm'])} |")
        print(f"| Mínimo / máximo (mm) | {coma(e['minimo_mm'])} / {coma(e['maximo_mm'])} |")
        print(f"| Rango (mm) | {coma(e['rango_mm'])} |")
        print(f"| Promedio − nominal (mm) | {coma(e['desvio_medio_nominal_mm'])} |")
        print(f"| Puntos dentro de 9 ± 0,5 mm | {e['dentro_criterio_txt']} |")
