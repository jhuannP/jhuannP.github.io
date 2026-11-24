"""Envelope nominal ideal de uma espécie, dois isótopos por sítio."""
from fractions import Fraction as Q
from math import comb

def exact(v):
    if isinstance(v,bool) or not isinstance(v,(int,Q)):raise TypeError("Use int ou Fraction.")
    return Q(v)

def cluster(n,p,m0=100,z=1):
    if isinstance(n,bool) or not isinstance(n,int) or not 0<=n<=12:
        raise ValueError("Número de sítios entre0 e12 necessário.")
    if isinstance(z,bool) or not isinstance(z,int) or z<1:raise ValueError("Carga positiva inteira necessária.")
    p,m0=exact(p),exact(m0)
    if not 0<=p<=1 or m0<=0:raise ValueError("Probabilidade ou massa inválida.")
    masses=[Q(comb(n,k))*p**k*(1-p)**(n-k) for k in range(n+1)]
    maximum=max(masses)
    return tuple(dict(heavy=k,mz=(m0+2*k)/z,probability=q,relative=100*q/maximum) for k,q in enumerate(masses))
