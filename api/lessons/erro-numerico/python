from math import isfinite, sqrt, pi, cos, sin, exp, e, fsum

def _real(value):
    try:
        if isinstance(value,bool): raise ValueError
        result=float(value)
    except (TypeError,ValueError,OverflowError):
        raise ValueError('Valor real finito necessário') from None
    if not isfinite(result): raise ValueError('Valor real finito necessário')
    return result

def erro_abs_rel(exato,aproximado):
    exato,aproximado=_real(exato),_real(aproximado)
    absoluto=abs(exato-aproximado)
    return absoluto,None if exato==0 else absoluto/abs(exato)

a,r=erro_abs_rel(2,1.98)
assert abs(a-.02)<1e-12 and abs(r-.01)<1e-12
assert erro_abs_rel(0,.1)[1] is None
print(a,r)

from fractions import Fraction as Q
reference=Q(2);approx=Q(99,50)
assert abs(reference-approx)==Q(1,50)
assert abs(reference-approx)/abs(reference)==Q(1,100)
assert erro_abs_rel(0,.0005)==(.0005,None)
print('Referência racional exata:',abs(reference-approx))
