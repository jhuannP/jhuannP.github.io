"""Pressão osmótica ideal: soluto neutro retido, solvente permeável.
Concentração em mol/L, T em K e pressão em Pa. Sem dinâmica de fluxo.
"""
from math import isfinite

R = 8.314462618  # J mol^-1 K^-1; valor arredondado para o laboratório

def pressure(concentration, temperature):
    for value in (concentration, temperature):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not isfinite(value):
            raise ValueError('Entrada numérica finita, sem booleanos.')
    if concentration < 0 or temperature <= 0:
        raise ValueError('Concentração não negativa e temperatura absoluta positiva.')
    # 1 mol/L = 1000 mol/m³; J/m³ = Pa.
    return 1000 * concentration * R * temperature

if __name__ == '__main__':
    for c in (0, .01, .02):
        print(f'{c} mol/L, 300 K: {pressure(c,300)/1000:.6f} kPa')
    print('É uma pressão de equilíbrio ideal, não vazão nem medição.')
