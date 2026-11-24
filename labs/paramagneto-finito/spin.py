"""Paramagneto independente: lei exata em odds r=exp(2h/T), kB=1."""
from fractions import Fraction as Q
from math import comb

def positive(value):
    if isinstance(value, bool) or not isinstance(value, (int, Q)):
        raise TypeError("use int ou Fraction")
    value = Q(value)
    if value <= 0:
        raise ValueError("valor deve ser positivo")
    return value

def distribution(n, odds):
    """P(M=2k-n). Odds é razão de pesos, não o campo h."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n inteiro")
    if not 1 <= n <= 100:
        raise ValueError("1 <= n <= 100")
    r = positive(odds)
    return tuple((2*k-n, comb(n,k)*r**k/(1+r)**n) for k in range(n+1))

def moments(n, odds):
    law = distribution(n, odds)
    mean = sum(m*p for m,p in law)
    variance = sum((m-mean)**2*p for m,p in law)
    return mean, variance

def response(n, odds, temperature, moment=1):
    """d<mu M>/dB = mu² Var(M)/T; h=mu B, T em energia."""
    t = positive(temperature)
    mu = positive(moment)
    return mu**2 * moments(n, odds)[1] / t

if __name__ == '__main__':
    for r in (1, 3):
        print('r=',r,'lei=',distribution(4,r),'momentos=',moments(4,r),
              'resposta h=',response(4,r,2))
