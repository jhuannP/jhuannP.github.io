"""Equilíbrio F <-> U sintético, ΔCp=0; energias em kJ/mol e T em K."""
from math import exp, isfinite

R = 8.314462618e-3  # kJ mol^-1 K^-1, constante arredondada


def finite(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not isfinite(value):
        raise ValueError('Use números finitos, sem booleanos.')
    return float(value)


def populations(log_K):
    """K=p_U/p_F; calcula o par sem exponenciar argumento positivo."""
    z = finite(log_K)
    if z <= 0:
        weight = exp(z)
        return dict(folded=1/(1+weight), unfolded=weight/(1+weight))
    weight = exp(-z)
    return dict(folded=weight/(1+weight), unfolded=1/(1+weight))


def folding(temperature=300, midpoint=330, enthalpy=120):
    T, Tm, H = map(finite, (temperature, midpoint, enthalpy))
    if min(T, Tm, H) <= 0:
        raise ValueError('Temperaturas em kelvin e entalpia de desenovelamento positivas.')
    entropy = H/Tm
    delta_g = H*(1-T/Tm)
    thermal_energy = R*T
    if thermal_energy == 0:
        raise ValueError('Escala térmica abaixo da precisão numérica.')
    log_K = -delta_g/thermal_energy
    if not all(isfinite(v) for v in (entropy, delta_g, log_K)):
        raise ValueError('Escala fora do intervalo numérico do modelo.')
    q = populations(log_K)
    return dict(delta_g=delta_g, entropy=entropy, log_K=log_K, **q)


if __name__ == '__main__':
    for T in (300, 330, 360):
        print(T, 'K:', folding(T, 330, 120))
    print('F e U são macrostados; ΔG°=G°_U-G°_F em kJ/mol.')
    print('Modelo com ΔCp=0, sem cinética, estrutura prevista ou dados reais.')
