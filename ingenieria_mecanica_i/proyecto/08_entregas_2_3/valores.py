#!/usr/bin/env python3
"""Valores numéricos que cita el informe, reunidos en un solo JSON.

Ningún número del informe se escribe a mano sin respaldo: en el .md cada valor
va marcado como [13,2]{.v k="res.funcionamiento.fuerza_mano_N"}, y el filtro
del perfil tp_mecanica comprueba en cada compilación que el número escrito
coincide con el de este JSON (redondeado a los decimales escritos).

Fuentes:
  res    resultados.json del modelo digital del prototipo (última verificación)
  par    constantes numéricas de parametros.py (medidas y supuestos de diseño)
  ancho  estadística del ancho medido (anchos_medidos.py)
  tx     opciones de transmisión: F = T·r/(i·R), con T, r y R de parametros.py
  ver    resúmenes de las verificaciones (cantidades) sacados de res

  python3 valores.py salida.json
"""
import importlib.util
import json
import math
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
MODELO = AQUI.parent / "06_modelo_2"

sys.path.insert(0, str(AQUI))
from anchos_medidos import estadistica, medidos  # noqa: E402


def cargar_parametros():
    spec = importlib.util.spec_from_file_location("parametros", MODELO / "parametros.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return {k: v for k, v in vars(mod).items()
            if k.isupper() and isinstance(v, (int, float, tuple, dict))}


def transmision(p, res):
    """Fuerza en la mano y vueltas de manivela por botella para cada relación i
    = vueltas de manivela por vuelta de carrete (i < 1 multiplica la velocidad
    del carrete). Rollo lleno: caso más exigente."""
    T, R = p["T_DISENO"], p["R_MANIVELA"]
    r_fin = res["funcionamiento"]["radio_rollo_mm"][1]
    vueltas_carrete = (p["R_ROLLO_FIN"] - p["R_NUCLEO"]) / p["PARED"]
    opciones = {"multiplica": 1 / 6.6, "directo": 1.0, "reduce": 3.0}
    return {nombre: {"i": i, "fuerza_N": T * r_fin / (i * R), "vueltas_manivela": vueltas_carrete * i}
            for nombre, i in opciones.items()}


def verificaciones(res):
    pasos = res["armado"]
    imp = res["impresion"]
    return {
        "choques_inicio": len(res["choques_s0"]),
        "choques_final": len(res["choques_s180"]),
        "posiciones_manivela": res["manivela_vuelta_completa"]["posiciones"],
        "choques_manivela": len(res["manivela_vuelta_completa"]["choques"]),
        "pasos_armado": len(pasos),
        "pasos_ok": sum(p["ok"] for p in pasos),
        "piezas_impresas": len(imp),
        "piezas_sin_soportes": sum(not v["necesita_soportes"] for v in imp.values()),
        "piezas_en_cama": sum(v["entra_en_la_cama"] for v in imp.values()),
        "puente_max_mm": max(v["puente_max_mm"] for v in imp.values()),
        "fallas": len(res["fallas"]),
    }


def main(salida):
    res = json.loads((MODELO / "resultados.json").read_text(encoding="utf-8"))
    par = cargar_parametros()
    datos = {
        "res": res,
        "par": {k: (list(v) if isinstance(v, tuple) else v) for k, v in par.items()},
        "ancho": estadistica(),
        "med": medidos(),
        "tx": transmision(par, res),
        "ver": verificaciones(res),
    }
    # Derivados simples que el texto cita
    datos["par"]["ALFA_GRADOS"] = math.degrees(par["ALFA"])
    datos["par"]["RANURA"] = par["PARED"] + 2 * par["HOLG_RANURA"]
    datos["par"]["CALCE_ESPESOR_9"] = par["W"] - 0.1
    datos["par"]["D_NUCLEO"] = 2 * par["R_NUCLEO"]
    datos["par"]["FRACCION_TAPA_PCT"] = 100 * par["FRACCION_TAPA"]
    datos["par"]["FRACCION_NORMAL_PCT"] = 100 * par["FRACCION_NORMAL"]
    Path(salida).parent.mkdir(parents=True, exist_ok=True)
    Path(salida).write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
