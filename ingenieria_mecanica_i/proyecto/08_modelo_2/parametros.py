# -*- coding: utf-8 -*-
"""
Parámetros del modelo 2.0 de la cortadora: ÚNICA fuente de verdad del modelo.

Cada valor indica su origen, para no presentar como decidido lo que no lo está:
  [CON]  lo fija el documento conceptual (00_concepto.md)
  [REF]  valor de referencia (modelo 1, cortadoras publicadas, catálogo)
  [COM]  medida de una pieza comercial estándar
  [SUP]  supuesto de este modelo: hacía falta un número para poder dibujar
  [P1S]  dato de la impresora de Maty (Bambu Lab P1S)

Disposición global: Z hacia arriba, cara superior de la base de MDF en Z = 0.
El eje de la botella es el eje Z. La cuchilla está en el punto (0, R_B) de la
pared, y la tira sale hacia +X: vista desde arriba, la botella y el carrete
giran en sentido horario. Unidades: mm, N y kg.
"""
import math

# ------------------------------------------------------------------- botella
D_B = 88.0            # [REF] botella de 1,5 L del modelo 1; medir las reales
R_B = D_B / 2
PARED = 0.25          # [SUP] espesor de pared; se mide en la prueba 1
ALTO_BOTELLA = 295.0  # [REF] del pico al borde cortado (modelo 1, X_BORDE)
X_CUELLO_FIN = 22.0   # [REF] largo del cuello (modelo 1)
R_CUELLO = 14.0       # [COM] rosca PCO 1881, Ø28
R_CUELLO_INT = 10.85  # [COM] boca de la PCO 1881, Ø21,7
X_HOMBRO_FIN = 85.0   # [REF] fin del hombro (modelo 1)
RECORRIDO = 180.0     # [REF] tramo cilíndrico que se corta (modelo 1)
MASA_BOTELLA = 0.030  # [SUP] botella de 1,5 L vacía, sin base, en kg
DENS_PET = 1.38e-3    # [REF] g/mm³


def radio_botella(x):
    """Radio exterior a la distancia x desde la punta del pico (igual que el
    modelo 1, para comparar)."""
    if x <= X_CUELLO_FIN:
        return R_CUELLO
    if x >= X_HOMBRO_FIN:
        return R_B
    t = (x - X_CUELLO_FIN) / (X_HOMBRO_FIN - X_CUELLO_FIN)
    return R_CUELLO + (R_B - R_CUELLO) * t * t * (3 - 2 * t)


# -------------------------------------------------------------- tira y ancho
W = 9.0               # [CON] ancho para pared de 0,25 mm (tabla de Function 3D)
CALCES = (7.0, 8.0, 9.0, 10.0)   # [CON] anchos que se imprimen
W_MAX = max(CALCES)
W_MIN = min(CALCES)
TOL_ANCHO = 0.5       # [CON] criterio w ± 0,5 mm
VUELTAS_BOTELLA = RECORRIDO / W
LARGO_TIRA = math.pi * D_B * VUELTAS_BOTELLA
ALFA = math.atan(W / (math.pi * D_B))           # ángulo de la hélice

# ---------------------------------------------------------- impresión (P1S)
CAMA = 256.0          # [P1S] cama de 256 × 256 × 256 mm
MARGEN_CAMA = 6.0     # [SUP] lo que se deja libre en el borde de la cama
BOQUILLA = 0.4        # [P1S] confirmado por Maty el 07/nov/2026
MATERIAL = "PLA común"  # [P1S] confirmado por Maty el 07/nov/2026
ANG_VOLADIZO = 45.0   # [REF] más inclinado que esto, desde la vertical, pide soporte
PUENTE_MAX = 10.0     # [SUP] luz que un puente horizontal salva sin soporte en PLA

# ------------------------------------------------------ holguras de impresión
HOLG_RANURA = 0.30    # [SUP] por lado, entre la pared y cada labio
HOLG_AGUJERO = 0.40   # [SUP] diámetro de agujero = nominal + esto (tornillos, varillas)
HOLG_TUERCA = 0.30    # [SUP] entre caras del hexágono cautivo
D_608_ALOJ = 22.15    # [SUP] alojamiento del 608 a presión (22,00 nominal)

# ------------------------------------------------------- piezas comerciales
D_608, ANCHO_608 = 22.0, 7.0                  # [COM] rodamiento 608ZZ, 8 × 22 × 7
M8_EC, M8_ALTO = 13.0, 6.5                    # [COM] tuerca M8: entre caras, altura
M8_CABEZA_EC, M8_CABEZA_ALTO = 13.0, 5.3      # [COM] cabeza del tornillo M8
ARANDELA_M8 = (8.4, 16.0, 1.6)                # [COM] interior, exterior, espesor
M3_EC, M3_ALTO = 5.5, 2.4                     # [COM] tuerca M3
M3_CABEZA_D, M3_CABEZA_ALTO = 5.5, 3.0        # [COM] cabeza cilíndrica M3
M5_CABEZA_D, M5_CABEZA_ALTO = 8.5, 3.5        # [COM]
M5_TUERCA_EC, M5_TUERCA_ALTO = 8.0, 5.0       # [COM] autoblocante
MADERA_D, MADERA_CABEZA_D = 3.5, 7.0          # [COM] tornillo para madera 3,5 × 16
HOJA = (18.0, 0.5)                            # [COM] trincheta de 18 mm: ancho, espesor
LARGO_HOJA = 60.0     # [SUP] tramo de hoja que se usa (se cortan segmentos)
CHAPITA_ESP = 0.5     # [COM] hoja de galga de espesores de 0,5 mm (o segmento de trincheta)
CHAPITA_ANCHO = 12.7  # [COM] ancho de una hoja de galga (1/2")
CHAPITA_LARGO = 18.0  # [SUP] se corta con tijera de hojalatero o doblando
MDF = (345.0, 200.0, 18.0)                    # [SUP] largo, ancho, espesor
MDF_ORIGEN = (-115.0, -75.0)                  # [SUP] esquina de la base; -X deja lugar al sargento

# ------------------------------------------------------- altura de la guía
CAPA = 0.2            # [SUP] altura de capa: las cotas verticales críticas caen en múltiplos
Z_PISO = 42.0         # [SUP] piso de PLA del cabezal; lo impone la altura de la
                      # torre del carrete (ver más abajo)
TACO_ALTO = 36.0      # [COM] taco de MDF bajo el cabezal: dos recortes de 18 mm
POZO_ALTO = 3 * CAPA                      # rebaje de la chapita: tres capas, abierto arriba
Z_GUIA = Z_PISO - POZO_ALTO + CHAPITA_ESP # cara de la chapita: el borde apoya acá
RANURA_PROF = 0.3     # [SUP] canaleta bajo la pared: el borde no toca el PLA

# ---------------------------------------------------------------- cabezal
CAB_X = (-32.0, 36.0)        # [SUP] bloque del cabezal
CAB_Y = (24.0, 104.0)        # [SUP]
LABIO_ESP = 5.0              # [SUP] espesor radial del labio exterior
LABIO_INT_R0 = 40.0          # [SUP] radio interior del labio interior
ALTO_LABIO_INT = 6.0         # [SUP] < W_MIN: la hoja pasa por encima
ALTO_LABIO_EXT = 16.0        # [SUP]
TH_LABIOS = (80.0, 125.0)    # [SUP] arco del labio interior, en grados
TH_LABIO_EXT_FIN = 125.0     # [SUP] el exterior va del filo (90°) hasta acá
CHAPITA_Y0 = 43.65          # [SUP] borde interior: 0,2 mm fuera del labio interior
CHAPITA_X = (-CHAPITA_LARGO / 2, CHAPITA_LARGO / 2)       # centrada bajo el filo
CHAPITA_Y = (CHAPITA_Y0, CHAPITA_Y0 + CHAPITA_ANCHO)
HOLG_CHAPITA = 0.2           # [SUP] por lado, en el rebaje
LABIO_PIE_R = 56.0           # [SUP] pie del labio exterior, que se atornilla
LABIO_PIE_TH = (103.0, 125.0)            # [SUP] fuera del calce y del rebaje
LABIO_PIE_ESP = 3.0          # [SUP]
TORNILLOS_LABIO = ((52.0, 108.0), (52.0, 121.0))   # [SUP] radio y ángulo
TORNILLOS_TACO = ((-22.0, 70.0), (30.0, 66.0))     # [SUP] taco a la base, bajo la placa
CALCE_X = (-8.0, 26.0)       # [SUP] calce y pisador, fuera del paso de la pared
CALCE_Y = (51.0, 97.0)
PISADOR_ESP = 5.0            # [SUP]
HOJA_Y0 = 40.0               # [SUP] la punta entra 4 mm dentro de la botella
TORNILLOS_HOJA = ((-4.5, 80.0), (22.5, 80.0))   # [SUP] fuera del ancho de la hoja
PROF_TUERCA = 2.7            # [SUP] alojamientos de tuerca M3 abiertos hacia abajo
AGUJERO_TACO = 4.0           # [SUP] mecha para que los tornillos de la hoja pasen al taco
TORNILLO_HOJA_L = 25.0       # [COM] M3 × 25
TORNILLOS_CABEZAL = ((-12.0, 30.0), (12.0, 30.0), (-26.0, 96.0), (31.0, 96.0))   # [SUP] lejos de los labios
PISO_BAJO_TORNILLO = 3.0     # [SUP] material bajo la cabeza del tornillo para madera

# ----------------------------------------------------- zócalo de la varilla
ZOCALO_R, ZOCALO_ALTO = 18.0, 28.0     # [SUP]
ZOCALO_FONDO = 3.0                      # [SUP] piso bajo la varilla
HOLG_VARILLA = 0.2                      # [SUP] agujero de la varilla lisa, ajustado
Z_PRISIONERO = 14.0                     # [SUP] tornillo M3 que traba la varilla, desde -X
PRISIONERO_L = 16.0                     # [COM] M3 × 16
OREJAS_ZOCALO = (270.0, 30.0, 150.0)   # [SUP] ángulos; ninguna bajo el cabezal (90°)
OREJA_R = 26.0                          # [SUP] radio de los tornillos
VARILLA_D, VARILLA_L = 8.0, 400.0       # [COM] varilla lisa Ø8 (eje lineal de impresora 3D)

# -------------------------------------------------------------------- ojal
X_OJAL = 70.0          # [SUP] fuera del barrido de la manivela
OJAL_LARGO = 10.0      # [SUP] a lo largo de la tira
OJAL_PARED = 4.0       # [SUP]
OJAL_HUECO = 1.5       # [SUP] ancho de la ranura: tira de 0,25 mm más juego

# ----------------------------------------------------------------- carrete
R_NUCLEO = 16.0        # [SUP] núcleo de Ø32
R_ROLLO_FIN = math.sqrt(R_NUCLEO ** 2 + LARGO_TIRA * PARED / math.pi)
R_ROLLO_MAX = max(math.sqrt(R_NUCLEO ** 2 + math.pi * D_B * RECORRIDO / w * t / math.pi)
                  for w, t in ((10, .20), (9, .25), (8, .30), (7, .35)))
R_DISCO = R_ROLLO_MAX + 4.0             # [SUP] discos laterales
DISCO_ESP = 3.0        # [SUP]
X_CARRETE = 180.0      # [SUP] lo fija el lugar para la mano (ver verificar.py)
Y_CARRETE = R_B - (R_NUCLEO + R_ROLLO_FIN) / 2   # la tira llega tangente a mitad del rollo
ALTO_NUCLEO = W_MAX + 3.0               # [SUP] la tira más ancha, con juego

# ------------------------------------------------- torre y eje del carrete
TORRE_R = D_608_ALOJ / 2 + 6.0          # [SUP] pared de 6 mm
TORRE_ALTO = 36.0      # [SUP] dos 608 separados 12 mm
TORRE_BRIDA = (30.0, 5.0)               # [SUP] radio y espesor de la brida
TORRE_CAVIDAD = (10.0, 10.0)            # [SUP] radio y alto: cabeza del tornillo M8
TORRE_TORNILLOS_R = 24.0                # [SUP]
EJE_CARRETE_L = 60.0   # [COM] tornillo M8 × 60, rosca completa

# ---------------------------------------------------------------- manivela
R_MANIVELA = 80.0      # [CON] brazo elegido en 4.1
MANIVELA_ESP = 8.0     # [SUP] espesor del brazo
MANIVELA_ANCHO = 16.0  # [SUP]
CUBO_R, CUBO_ALTO = 11.0, 12.0          # [SUP]
MANGO_R, MANGO_L = 11.0, 55.0           # [SUP]
TORNILLO_MANGO_L = 70.0                 # [COM] M5 × 70
LUZ_MANO = 40.0        # [SUP] espacio mínimo entre el mango y la botella

# ----------------------------------------------------------------- sargento
SARGENTO_XY = (-92.0, 15.0)             # [SUP] centro de la mordaza, sobre el MDF
SARGENTO_PAD_R = 16.0                   # [COM] mordaza de un sargento chico

# ------------------------------------------------------------ vaso de lastre
LASTRE_R, LASTRE_ALTO, LASTRE_PARED = 25.0, 30.0, 2.0   # [SUP]
DENS_TUERCAS = 3.5e-3  # [SUP] g/mm³ de tuercas sueltas apiladas (acero con huecos)

# ---------------------------------------------------- cuentas de funcionamiento
T_DISENO = 40.0        # [CON] supuesto hasta la prueba 1 (anexo A)
F_MANO_MAX = 20.0      # [CON] criterio de fuerza en la mano
SIGMA_PET = 55.0       # [REF] MPa, PET sin orientar: cota baja
MU_PLA_PET = 0.35      # [SUP] rozamiento PLA-PET, sin lubricar
MU_TAPA = 0.30         # [SUP] tapa de PE/PP sobre acero liso: valor de diseño, del lado seguro
MU_PE_ACERO = {"seca": 0.20, "con grasa": 0.20}   # [REF] Engineering Toolbox, polietileno-acero:
                       # la grasa no lo cambia; no hay dato de polipropileno
FRACCION_TAPA = 0.10   # [SUP] carga de la tapa sobre la varilla, como fracción del tiro
FRACCION_NORMAL = 0.5  # [SUP] carga de los labios como fracción del tiro: el
                       # tiro y la reacción de la hoja actúan casi en el mismo
                       # punto y casi se anulan, así que queda del lado seguro
G = 9.81

# ---------------------------------------------------------------- derivados
Z_CORE0 = TORRE_ALTO + ARANDELA_M8[2] + DISCO_ESP   # base del núcleo
Z_CORE1 = Z_CORE0 + ALTO_NUCLEO
Z_MANIVELA = Z_CORE1 + DISCO_ESP                     # base del cubo de la manivela


def z_superior_botella(s):
    """Punta del pico cuando ya se cortaron s mm: el borde sigue en la guía."""
    return Z_GUIA + ALTO_BOTELLA - s
