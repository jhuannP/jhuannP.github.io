"""Comprimentos racionais exatos: não classifica incerteza de medidas reais."""
from fractions import Fraction as Q
from math import isqrt

def positive(v):
    if type(v) not in (int,Q) or v<=0:raise ValueError('int/Fraction positivo sem bool')
    return Q(v)

def root_if_rational(square):
    a,b=isqrt(square.numerator),isqrt(square.denominator)
    return Q(a,b) if a*a==square.numerator and b*b==square.denominator else None

def hypotenuse(a,b):
    a,b=positive(a),positive(b);square=a*a+b*b
    return dict(square=square,exact_root=root_if_rational(square))

def missing_leg(c,a):
    c,a=positive(c),positive(a)
    if c<=a:raise ValueError('hipotenusa deve ser maior que cateto')
    square=c*c-a*a
    return dict(square=square,exact_root=root_if_rational(square))

def classify(sides):
    if not isinstance(sides,(list,tuple)) or len(sides)!=3:raise ValueError('três lados')
    a,b,c=sorted(positive(v) for v in sides)
    if a+b<=c:return 'não forma triângulo'
    return 'retângulo' if a*a+b*b==c*c else 'não retângulo'

if __name__=='__main__':
    from itertools import permutations
    assert hypotenuse(6,8)==dict(square=Q(100),exact_root=Q(10))
    assert missing_leg(10,6)['exact_root']==8
    assert hypotenuse(2,3)==dict(square=Q(13),exact_root=None)
    # Generate triples independently from integer m,n; confirm exact relation and missing sides.
    for m in range(2,10):
        for n in range(1,m):
            a,b,c=m*m-n*n,2*m*n,m*m+n*n
            assert hypotenuse(a,b)['exact_root']==c
            assert missing_leg(c,a)['exact_root']==b
            for perm in permutations((a,b,c)):assert classify(perm)=='retângulo'
            for k in (Q(1,10),Q(3),Q(5,2)):
                assert hypotenuse(k*a,k*b)['square']==k*k*c*c
    assert classify([1,2,3])=='não forma triângulo'
    assert classify([5,5,8])=='não retângulo'
    assert classify([5,12,13])=='retângulo'
    for call in (lambda:hypotenuse(True,8),lambda:missing_leg(6,10),lambda:classify([1,2]),lambda:hypotenuse(0,2)):
        try:call()
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    print('6,8:',hypotenuse(6,8),'2,3:',hypotenuse(2,3))
    print('36 triplas parametrizadas, permutações e escalas racionais conferidas.')
