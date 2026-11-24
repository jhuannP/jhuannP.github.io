"""Mola ideal 1D, m=2 kg, k=8 N/m, amplitude=1 m. Posição candidata, não trajetória."""
from fractions import Fraction as F
from math import sqrt


def inspect(q=0, c=0):
    if isinstance(q, bool) or not isinstance(q, int) or not -150 <= q <= 150:
        raise ValueError('Posição inteira em centésimos, de -150 a 150')
    if isinstance(c, bool) or not isinstance(c, int) or not -10 <= c <= 10:
        raise ValueError('Constante inteira em joules, de -10 a 10')
    x=F(q,100); u=4*x*x+c; e=F(4+c); difference=e-u
    allowed=difference>=0
    return dict(x=x,u=u,e=e,difference=difference,allowed=allowed,
                kinetic=difference if allowed else None,
                speed=sqrt(float(difference)) if allowed else None,force=-8*x)


if __name__ == '__main__':
    assert inspect(0,-10)['kinetic']==4
    assert inspect(100)['speed']==0
    assert inspect(125)['kinetic'] is None
    print(inspect(50,-10))
