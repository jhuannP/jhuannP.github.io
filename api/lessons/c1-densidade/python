"""Construções exatas finitas; não representa todo real como entrada."""
from fractions import Fraction as Q
from math import isqrt

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use int/Fraction, não float')
    x=Q(x)
    if abs(x.numerator)>10**12 or x.denominator>10**12:
        raise ValueError('Numerador/denominador excede 10**12')
    return x

def between(a,b):
    """Ponto estritamente interno na grade 1/n, inclusive a<0."""
    a=rational(a);b=rational(b)
    if not a<b: raise ValueError('Intervalo crescente necessário')
    n=1+(1/(b-a)).numerator//(1/(b-a)).denominator
    if n>10**6: raise ValueError('Grade excede orçamento de 10**6')
    na=n*a;m=na.numerator//na.denominator+1
    r=Q(m,n)
    assert a<r<b
    return n,m,r

def sqrt2_bracket(k):
    if isinstance(k,bool) or not isinstance(k,int) or not 0<=k<=12:
        raise ValueError('Precisão decimal inteira de 0 a 12')
    n=10**k;m=isqrt(2*n*n)
    lo,hi=Q(m,n),Q(m+1,n)
    assert lo*lo<2<hi*hi
    return lo,hi

if __name__=='__main__':
    print(between(Q(-7,5),Q(-13,10)))
    lo,hi=sqrt2_bracket(3)
    print('sqrt(2) entre',lo,'e',hi,'largura',hi-lo)
