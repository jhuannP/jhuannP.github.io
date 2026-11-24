"""Fator nodal e exemplo exato x⁴; não é interpolador geral novo."""
from fractions import Fraction as Q
from importlib import import_module
base=import_module('labs.lagrange-bases.interpolation')

def coefficients(n):
    if isinstance(n,bool) or not isinstance(n,int) or not 0<=n<=16:
        raise ValueError('0<=n<=16 inteiro')
    if n==0:return (Q(1),)
    previous=[Q(1)]; current=[Q(0),Q(1)]
    for k in range(1,n):
        nxt=[Q(0)]+[2*v for v in current]
        for j,v in enumerate(previous):nxt[j]-=v
        previous,current=current,nxt
    return tuple(current)

def monic(n):
    c=coefficients(n)
    return tuple(v/c[-1] for v in c)

def evaluate(coeffs,x):
    x=base.rational(x); value=Q(0)
    for c in reversed(coeffs):value=value*x+c
    return value

def fixture(family):
    if family=='uniform':return ((Q(-1),Q(-1,3),Q(1,3),Q(1)),(Q(1,9),0,Q(-10,9),0,1))
    if family=='lobatto':return ((Q(-1),Q(-1,2),Q(1,2),Q(1)),(Q(1,4),0,Q(-5,4),0,1))
    if family=='roots':return (None,monic(4))
    raise ValueError('uniform,lobatto ou roots')

def error(x,family):
    return evaluate(fixture(family)[1],x)

def interpolant(x,family):
    x=base.rational(x)
    return x**4-error(x,family)

def sup_error(family):
    # Quartico par x⁴+c2*x²+c0; y=x² percorre[0,1].
    _,c=fixture(family); c0,c2=Q(c[0]),Q(c[2])
    ys=[Q(0),Q(1)]; critical=-c2/2
    if 0<=critical<=1:ys.append(critical)
    return max(abs(y*y+c2*y+c0) for y in ys)

def mapped_error(x,family,left,right):
    x,left,right=map(base.rational,(x,left,right))
    if left>=right:raise ValueError('intervalo crescente')
    h=(right-left)/2;center=(right+left)/2
    return h**4*error((x-center)/h,family)

if __name__=='__main__':
    for family in ('uniform','lobatto','roots'):
        print(family,'coeficientes=',fixture(family)[1], 'p(0)=',interpolant(0,family),'norma=',sup_error(family))
