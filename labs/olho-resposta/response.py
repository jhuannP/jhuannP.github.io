"""Contrastes descritivos em quatro condições sintéticas; sem inferência causal."""
from fractions import Fraction


COUNTS = {'A0': (2, 20), 'A1': (14, 20), 'B0': (1, 20), 'B1': (3, 20)}


def rate(k, n):
    if type(k) is not int or type(n) is not int or n <= 0 or not 0 <= k <= n:
        raise ValueError('Contagens int, n>0 e 0≤k≤n, sem bool.')
    return Fraction(k, n)


def describe(counts):
    if type(counts) is not dict or set(counts) != {'A0', 'A1', 'B0', 'B1'}:
        raise ValueError('Exatamente A0,A1,B0,B1.')
    for pair in counts.values():
        if type(pair) is not tuple or len(pair) != 2:
            raise ValueError('Cada condição recebe tupla (positivas,total).')
    rates = {key: rate(*pair) for key, pair in counts.items()}
    da, db = rates['A1']-rates['A0'], rates['B1']-rates['B0']
    return {'rates': rates, 'delta_a': da, 'delta_b': db, 'contrast': da-db}


if __name__ == '__main__':
    print(describe(COUNTS))
    print('Valores fixos fictícios de marcador M; não dados de cristalino ou BMP4.')
