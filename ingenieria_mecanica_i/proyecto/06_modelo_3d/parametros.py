# -*- coding: utf-8 -*-
"""
Parámetros de la cortadora de botellas PET: ÚNICA fuente de verdad del modelo.

Cada valor indica su origen, para no presentar como decidido lo que no lo está:
  [E2]   lo fija la Entrega 2
  [DXF]  leído del plano; qué pieza es lo interpretó Claude
  [REF]  valor de referencia de la presentación (lámina 10), no decidido
  [SUP]  supuesto de este modelo: hacía falta un número para poder dibujar

Disposición global: X = eje de la botella (cuello hacia -X, borde abierto
hacia +X), Y = lateral, Z = arriba. Cara superior de la base en Z = 0.
Unidades: mm.
"""
import math

# ------------------------------------------------- ecuación de diseño (E2, 5.3)
D_B = 88.0            # [REF] diámetro de la botella en el contacto
D_R = 50.0            # [DXF] diámetro del rodillo
L_HUSILLO = 8.0       # [REF] avance por vuelta: T8 de 4 entradas (paso 2 mm)
ENTRADAS = 4          # [REF]
Z_1 = 20              # [SUP] engranaje conductor (eje del rodillo)
Z_2 = 40              # [SUP] engranaje conducido (husillo); i = z2/z1 > 1 [E2]
MODULO = 2.0          # [SUP] el menor que deja lugar al eje de Ø30 (ver verificar.py)
RECORRIDO = 180.0     # [REF] tramo cortado

I = Z_2 / Z_1
PASO_A = L_HUSILLO * D_B / (I * D_R)     # a = L·Db/(i·Dr), mm por vuelta de botella

# ------------------------------------------------- botella (coordenada local x)
R_B = D_B / 2
X_CUELLO_FIN = 22.0   # [SUP] largo del cuello
R_CUELLO = 14.0       # [SUP] rosca PCO, Ø28
X_HOMBRO_FIN = 85.0   # [SUP] fin del hombro, empieza la zona cilíndrica
X_FRANJA_FIN = 115.0  # [SUP] franja del rodillo, queda sin cortar [E2, 5.4]
X_BORDE = X_FRANJA_FIN + RECORRIDO      # borde abierto, sin la base [E2, 5.1]


def radio_botella(x):
    """Radio exterior de la botella en la coordenada local x."""
    if x <= X_CUELLO_FIN:
        return R_CUELLO
    if x >= X_HOMBRO_FIN:
        return R_B
    t = (x - X_CUELLO_FIN) / (X_HOMBRO_FIN - X_CUELLO_FIN)
    return R_CUELLO + (R_B - R_CUELLO) * t * t * (3 - 2 * t)


# --------------------------------------------------------------- disposición
H_EJE = 175.0                 # [SUP] altura del eje de la botella
ANG_RODILLO = math.radians(-30)  # [SUP] rodillo abajo y a un costado (+Y)
DIST_BR = (D_B + D_R) / 2     # contacto exterior [E2, 5.2]
Y_R = DIST_BR * math.cos(ANG_RODILLO)
Z_R = H_EJE + DIST_BR * math.sin(ANG_RODILLO)

DIST_EJES = MODULO * (Z_1 + Z_2) / 2
Y_H = Y_R                     # [SUP] husillo debajo del eje del rodillo
Z_H = Z_R - DIST_EJES

# --------------------------------------------------------------- eje y rodillo
D_EJE = 30.0          # [DXF] eje del rodillo
X_RODILLO = (90.0, 110.0)    # [SUP] centrado en la franja
X_EJE = (-36.0, 113.0)       # [SUP] llega hasta detrás del soporte del cuello

# ------------------------------------------------------------------- manivela
R_MANIVELA = 70.0     # [SUP] el DXF acota Ø70 sin aclarar si es este círculo
X_MANIVELA = -34.0    # [SUP] detrás del soporte del cuello
LARGO_MANGO = 60.0    # [SUP]
R_MANGO = 12.0        # [SUP]

# ------------------------------------------------------- caja de la transmisión
X_PLACA_1 = (28.0, 40.0)     # [SUP] placa que une ambos ejes
X_ENGRANAJES = (42.0, 52.0)  # [SUP] ancho de cara 10
X_PLACA_2 = (54.0, 66.0)     # [SUP]
R_PLACA_EJE = 30.0           # [SUP] rodamiento 6006 (Ø55) con pared
R_PLACA_HUSILLO = 18.0       # [SUP]

# -------------------------------------------------------------------- husillo
D_HUSILLO = 8.0       # [REF]
X_HUSILLO_INI = 24.0  # [SUP]

# ------------------------------------------------------------ soporte del cuello
X_SOPORTE = (4.0, 24.0)      # [SUP]
ANCHO_SOPORTE = 70.0  # [DXF] porta rodamientos 70 × 80
ALTO_SOPORTE = 80.0   # [DXF]
D_ROD_CUELLO = (40.0, 62.0)  # [SUP] rodamiento de 40 × 62 × 12
X_MORDAZA = (2.0, 26.0)      # [SUP] pieza de dos mitades [E2, 5.4]

# ----------------------------------------------------------------- carro y guías
X_CARRO = (-10.0, 72.0)      # [SUP]
Y_CARRO = (-75.0, 95.0)      # [SUP]
Z_CARRO = (20.0, 30.0)       # [SUP]
D_GUIA = 12.0         # [SUP]
Y_GUIAS = (-65.0, 85.0)      # [SUP] dos guías paralelas [E2, 5.1]
Z_GUIA = 12.0         # [SUP]
X_GUIAS = (-60.0, 300.0)     # [SUP]

# ---------------------------------------------------------------- piezas fijas
X_BASE = (-70.0, 310.0)      # [SUP]
Y_BASE = (-115.0, 115.0)     # [SUP]
ESPESOR_BASE = 8.0    # [SUP]
HOLGURA_TUERCA = 6.0  # [SUP] entre el carro al final del recorrido y la tuerca
X_TUERCA = (X_CARRO[1] + RECORRIDO + HOLGURA_TUERCA,
            X_CARRO[1] + RECORRIDO + HOLGURA_TUERCA + 20)
X_HUSILLO_FIN = X_TUERCA[1] + 10     # enrosca en la tuerca desde el inicio
X_CUCHILLA = X_BORDE  # la cuchilla arranca en el borde abierto [E2, 5.4]


# --------------------------------------------------------------------- cinemática
def estado(vueltas_manivela):
    """Toda la cadena a partir de una sola entrada: las vueltas de la manivela.
    Devuelve ángulos en grados con signo (positivo según +X, mano derecha)."""
    fi = vueltas_manivela * 360.0
    return {
        "s": L_HUSILLO * vueltas_manivela / I,   # avance del carro
        "rodillo": -fi,                          # gira según -X
        "botella": fi * D_R / D_B,               # contacto exterior: invierte
        "husillo": fi / I,                       # engrane exterior: invierte
    }


VUELTAS_MANIVELA_TOTAL = RECORRIDO * I / L_HUSILLO
VUELTAS_BOTELLA_TOTAL = RECORRIDO / PASO_A
LARGO_TIRA = math.pi * D_B * VUELTAS_BOTELLA_TOTAL
