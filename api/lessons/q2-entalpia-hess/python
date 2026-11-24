"""Balanços sintéticos de entalpia; kJ/mol de reação e kJ, sem cinética."""
from fractions import Fraction as Q


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (int, Q)):
        raise ValueError('Use inteiro ou Fraction para manter aritmética exata.')
    return Q(value)


def reaction_enthalpy(nu, molar_h):
    """Soma nu_i*h_i; coeficientes assinados, h em kJ/mol de espécie."""
    if not nu or set(nu) != set(molar_h):
        raise ValueError('Mapas não vazios com as mesmas espécies.')
    return sum((rational(nu[i])*rational(molar_h[i]) for i in nu), Q(0))


def hess(b=20, c=-30, extent=1, direction=1):
    """Três formas isoméricas hipotéticas, h_A=0, h_B=b, h_C=c."""
    b, c, extent, direction = map(rational, (b, c, extent, direction))
    if extent < 0 or direction not in (-1, 1):
        raise ValueError('Extensão não negativa e sentido +1 ou -1.')
    levels = [Q(0), b, c] if direction == 1 else [c, b, Q(0)]
    first = levels[1]-levels[0]
    second = levels[2]-levels[1]
    direct = levels[2]-levels[0]
    return dict(first=first, second=second, direct=direct,
                total=extent*direct, total_first=extent*first,
                total_second=extent*second, cycle=first+second-direct,
                levels=levels)


if __name__ == '__main__':
    for direction in (1, -1):
        print('Sentido', direction, hess(20, -30, 2, direction))
    print('X2 + Y2 -> 2XY, formação sintética:',
          reaction_enthalpy({'X2': -1, 'Y2': -1, 'XY': 2},
                            {'X2': 0, 'Y2': 0, 'XY': -15}), 'kJ/mol de reação')
    print('Dados sintéticos em T e p fixos; não há previsão de rapidez ou equilíbrio.')
