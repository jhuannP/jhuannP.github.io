"""Curva original r(t)=(3t-t³,3t²), t em [0,1], e limites racionais de cordas."""
from fractions import Fraction as F
from math import isqrt

def parameter(t):
    if isinstance(t,bool) or not isinstance(t,(int,F)):
        raise TypeError('Use inteiro ou Fraction.')
    t=F(t)
    if not 0<=t<=1: raise ValueError('Parâmetro entre zero e um.')
    return t

def point(t):
    t=parameter(t)
    return (3*t-t**3,3*t*t)

def speed(t):
    t=parameter(t)
    return 3*(1+t*t)

def arc(a=0,b=1):
    a,b=parameter(a),parameter(b)
    if a>b: raise ValueError('Intervalo crescente necessário.')
    return 3*(b-a)+b**3-a**3

def sqrt_bounds(q,digits):
    """q racional não negativo; resultados são limites exatos, não floats."""
    q=F(q)
    if q<0: raise ValueError('Radicando não negativo.')
    if isinstance(digits,bool) or not isinstance(digits,int): raise TypeError('Dígitos inteiros.')
    if not 1<=digits<=12: raise ValueError('Use 1–12 dígitos.')
    scale=10**digits
    k=isqrt(q.numerator*scale*scale//q.denominator)
    lo=F(k,scale)
    hi=lo if k*k*q.denominator==q.numerator*scale*scale else F(k+1,scale)
    return lo,hi

def polygon(n,digits=9):
    if isinstance(n,bool) or not isinstance(n,int): raise TypeError('n inteiro.')
    if not 1<=n<=4096: raise ValueError('Use 1–4096 segmentos.')
    # Validate digits even before processing any chord.
    sqrt_bounds(F(0),digits)
    lower=upper=F(0)
    for i in range(n):
        a,b=point(F(i,n)),point(F(i+1,n))
        squared=sum((y-x)**2 for x,y in zip(a,b))
        lo,hi=sqrt_bounds(squared,digits)
        lower+=lo;upper+=hi
    return {'segments':n,'lower':lower,'upper':upper,'curve_length':arc()}

if __name__=='__main__':
    for n in (1,2,4,8,16):
        r=polygon(n)
        print(n,'cordas entre',float(r['lower']),float(r['upper']),'comprimento exato',r['curve_length'])
    print('Decimais acima são aproximações; lower/upper são frações exatas no retorno.')
