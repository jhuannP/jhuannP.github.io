"""F(x,y)=(x²+y,y): ramos explícitos e derivadas locais, não inversor geral."""
from fractions import Fraction
from math import isfinite, sqrt


def rational(value):
    if type(value) not in (int, Fraction):
        raise ValueError('Use int/Fraction, sem bool/float.')
    return Fraction(value)


def forward(x, y):
    x, y = rational(x), rational(y)
    return x*x+y, y


def jacobian(x):
    x = rational(x)
    return ((2*x, Fraction(1)), (Fraction(0), Fraction(1)))


def inverse_jacobian(x):
    x = rational(x)
    if x == 0:
        raise ValueError('Derivada singular em x=0.')
    return ((1/(2*x), -1/(2*x)), (Fraction(0), Fraction(1)))


def inverse_float(u, v, sign=1):
    if type(sign) is not int or sign not in (-1, 1):
        raise ValueError('Ramo: sign=1 ou -1.')
    if type(u) not in (int, float) or type(v) not in (int, float):
        raise ValueError('Coordenadas float/int finitas.')
    try:
        u, v = float(u), float(v)
    except OverflowError as exc:
        raise ValueError("Coordenadas fora da faixa float.") from exc
    w = u-v
    if not isfinite(u) or not isfinite(v) or not isfinite(w) or w <= 0:
        raise ValueError('Domínio do ramo: u>v e diferença finita.')
    return sign*sqrt(w), v


if __name__ == '__main__':
    print('F(2,1)=', forward(2, 1), '=F(-2,1)=', forward(-2, 1))
    print('Dg em F(2,1):', inverse_jacobian(2))
    h = Fraction(1, 10)
    u, v = forward(2+h, 1)
    predicted_dx = (u-5)/4
    print('h=', h, 'predição linear=', predicted_dx,
          'erro=', h-predicted_dx)
    print('ramos em (5,1):', inverse_float(5, 1), inverse_float(5, 1, -1))
