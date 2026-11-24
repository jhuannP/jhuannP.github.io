"""Duas restrições polinomiais: F=(z²+w−s,z−w−t)."""
from fractions import Fraction
from math import isfinite, sqrt


def rational(value):
    if type(value) not in (int, Fraction):
        raise ValueError('Use int/Fraction, sem bool/float.')
    return Fraction(value)


def residual(s, t, z, w):
    s, t, z, w = map(rational, (s, t, z, w))
    return z*z+w-s, z-w-t


def blocks(z):
    z = rational(z)
    return ((-1, 0), (0, -1)), ((2*z, 1), (1, -1))


def graph_jacobian(z):
    z = rational(z)
    d = 2*z+1
    if d == 0:
        raise ValueError('Bloco das incógnitas singular.')
    return ((1/d, 1/d), (1/d, -2*z/d))


def branch_float(s, t, sign=1):
    if type(sign) is not int or sign not in (-1, 1):
        raise ValueError('sign deve ser int±1.')
    if type(s) not in (int, float) or type(t) not in (int, float):
        raise ValueError('Parâmetros float/int finitos.')
    try:
        s, t = float(s), float(t)
    except OverflowError as exc:
        raise ValueError('Fora da faixa float.') from exc
    d = 1+4*(s+t)
    if not isfinite(s) or not isfinite(t) or not isfinite(d) or d <= 0:
        raise ValueError('Ramos C1 requerem 1+4(s+t)>0 finito.')
    z = (-1+sign*sqrt(d))/2
    return z, z-t


if __name__ == '__main__':
    print('ramos em s=t=1:', branch_float(1, 1), branch_float(1, 1, -1))
    print('Dg no ramo z=1:', graph_jacobian(1))
    h = Fraction(1, 10)
    ds = 3*h+h*h
    print('delta s=', ds, 'delta z linear=', ds/3,
          'delta real=', h, 'real-linear=', h-ds/3)
