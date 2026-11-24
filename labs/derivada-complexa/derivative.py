"""Quocientes complexos exatos em quatro exemplos didáticos.
Complexos são pares (real, imag), ambos int ou Fraction, sem float/bool.
A amostragem confere identidades; não decide limites nem analiticidade.
"""
from fractions import Fraction as Q

def pair(z):
    if not isinstance(z,(tuple,list)) or len(z)!=2:
        raise ValueError("use par (real, imag)")
    if any(type(t) not in (int,Q) for t in z):
        raise ValueError("componentes int ou Fraction, sem bool/float")
    return tuple(Q(t) for t in z)

def add(z,w):
    a,b=pair(z);c,d=pair(w)
    return a+c,b+d

def subtract(z,w):
    a,b=pair(z);c,d=pair(w)
    return a-c,b-d

def multiply(z,w):
    a,b=pair(z);c,d=pair(w)
    return a*c-b*d,a*d+b*c

def divide(z,w):
    a,b=pair(z);c,d=pair(w);r=c*c+d*d
    if r==0: raise ValueError("denominador complexo zero")
    return (a*c+b*d)/r,(b*c-a*d)/r

def conjugate(z):
    a,b=pair(z)
    return a,-b

def value(model,z):
    z=pair(z);x,y=z
    if model=='square': return multiply(z,z)
    if model=='conjugate': return conjugate(z)
    if model=='radial': return x*x+y*y,Q(0)
    if model=='trap':
        if z==(0,0): return Q(0),Q(0)
        c=conjugate(z)
        return divide(multiply(c,c),z)
    raise ValueError("modelo desconhecido")

def quotient(model,z,h):
    z=pair(z);h=pair(h)
    if h==(0,0): raise ValueError("incremento precisa ser não nulo")
    return divide(subtract(value(model,add(z,h)),value(model,z)),h)

def squared_norm(z):
    x,y=pair(z)
    return x*x+y*y
