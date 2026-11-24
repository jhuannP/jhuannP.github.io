"""Três modelos adimensionais, entrada x=1..6 em meios; Python opcional."""
from fractions import Fraction as F


def inspect(x=2):
    if type(x) not in (int,float,F):
        raise ValueError('Entrada numérica, sem bool')
    try:
        x=F(x)
    except (ValueError,OverflowError):
        raise ValueError('Entrada finita') from None
    if not 1<=x<=6 or (2*x).denominator!=1:
        raise ValueError('Use x de 1 a 6, em passos de 1/2')
    values={'direta':(4*x,8*x),'inversa':(24/x,12/x),
            'taxa_fixa':(6+4*x,6+8*x)}
    return {name:dict(y=y,doubled=y2,ratio=y/x,product=x*y,doubling=y2/y)
            for name,(y,y2) in values.items()}


if __name__=='__main__':
    s=inspect(2)
    assert s['direta']['ratio']==4
    assert s['inversa']['product']==24
    assert s['taxa_fixa']['doubling']==F(11,7)
    print(s)
