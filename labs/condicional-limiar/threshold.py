"""Modelo sintético X~U[0,1], Y=max(0,X-a). Aritmética racional.
Versão condicional: U[0,a] em y=0; delta_(a+y) em 0<y<1-a.
O extremo y=1-a é marginalmente nulo e fica sem especificação.
Não é calibração de um sensor nem ajuste a dados.
"""
from fractions import Fraction as Q

def rational(x):
    if type(x) not in (int,Q):
        raise ValueError("use int ou Fraction, sem bool/float")
    return Q(x)

def threshold(a):
    a=rational(a)
    if not 0<a<1: raise ValueError("0<a<1")
    return a

def readout(x,a):
    a=threshold(a);x=rational(x)
    if not 0<=x<=1: raise ValueError("0<=x<=1")
    return max(Q(0),x-a)

def cdf(y,a):
    a=threshold(a);y=rational(y)
    if y<0: return Q(0)
    return min(Q(1),a+y)

def posterior(y,a):
    a=threshold(a);y=rational(y)
    if y<0 or y>1-a: raise ValueError("leitura fora do suporte")
    if y==0:
        return dict(kind="uniform",lower=Q(0),upper=a,mean=a/2,variance=a*a/12)
    if y==1-a: return None
    return dict(kind="point",lower=a+y,upper=a+y,mean=a+y,variance=Q(0))

def bin_posterior(b,a,include_zero=True):
    a=threshold(a);b=rational(b)
    if type(include_zero) is not bool: raise ValueError("include_zero deve ser bool")
    if not 0<b<=1-a: raise ValueError("0<b<=1-a")
    low=Q(0) if include_zero else a
    high=a+b;width=high-low
    return dict(evidence=width,lower=low,upper=high,mean=(low+high)/2,variance=width*width/12)

def decomposition(a):
    a=threshold(a)
    residual=a**3/12
    return dict(mean=Q(1,2),variance=Q(1,12),residual=residual,explained=Q(1,12)-residual)
