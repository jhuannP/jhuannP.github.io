"""Quocientes racionais: exemplos finitos, não uma prova de limite."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x, bool) or not isinstance(x, (int, Q)):
        raise ValueError('Use inteiro ou Fraction para preservar a referência exata.')
    return Q(x)


def value(model, x):
    x = rational(x)
    if model == 'quadrado':
        return x*x
    if model == 'canto':
        return abs(x)
    if model == 'salto':
        return Q(0) if x == 0 else Q(1)
    if model == 'movimento':
        # t em segundos; s=3t²−2t+5 em metros.
        return 3*x*x - 2*x + 5
    raise ValueError('Modelo desconhecido.')


def quotient(model, a, h):
    a, h = rational(a), rational(h)
    if not h:
        raise ValueError('A taxa média exige h diferente de zero.')
    return (value(model, a+h)-value(model, a))/h


def symmetric(model, a, h):
    a, h = rational(a), rational(h)
    if not h:
        raise ValueError('A diferença central exige h diferente de zero.')
    return (value(model, a+h)-value(model, a-h))/(2*h)


def tangent_square(a, x):
    a, x = rational(a), rational(x)
    return a*a + 2*a*(x-a)


if __name__ == '__main__':
    for h in (Q(1,2), Q(1,10), Q(-1,10), Q(-1,100)):
        print('h=', h, 'quadrado em 2:', quotient('quadrado', 2, h),
              'canto em 0:', quotient('canto', 0, h),
              'central do canto:', symmetric('canto', 0, h))
    print('Movimento: taxa média em t=2, h=1/2:', quotient('movimento', 2, Q(1,2)), 'm/s')
    print('Velocidade exata em t=2: 10 m/s (limite algébrico).')
    print('Ter diferença central zero no canto não estabelece uma derivada.')
