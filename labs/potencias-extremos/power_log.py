"""S_N(x)=sum(x**n/n,n=1..N), com frações exatas.
A cota é uniforme em |x|<=r<1. N limitado a512 no laboratório.
Não retorna uma soma infinita exata nem decide convergência por amostragem.
"""
from fractions import Fraction as Q
MAX_N=512

def rational(x):
    if type(x) not in (int,Q): raise ValueError("use int ou Fraction, sem bool/float")
    return Q(x)

def count(n):
    if type(n) is not int or not 0<=n<=MAX_N: raise ValueError("N inteiro de0 a512")
    return n

def partial(x,n):
    x=rational(x);n=count(n);power=Q(1);total=Q(0)
    for k in range(1,n+1):
        power*=x;total+=power/k
    return total

def derivative_partial(x,n):
    x=rational(x);n=count(n);power=Q(1);total=Q(0)
    for _ in range(n):
        total+=power;power*=x
    return total

def uniform_bound(r,n):
    r=rational(r);n=count(n)
    if not 0<=r<1: raise ValueError("0<=r<1")
    return r**(n+1)/((n+1)*(1-r))

def first_sufficient(r,tolerance,strict=True):
    tolerance=rational(tolerance)
    if tolerance<=0 or type(strict) is not bool: raise ValueError("tolerância positiva e strict bool")
    # Validação antes da busca, inclusive se a primeira cota já bastar.
    uniform_bound(r,0)
    for n in range(MAX_N+1):
        b=uniform_bound(r,n)
        if b<tolerance if strict else b<=tolerance: return n
    return None # Nenhum certificado encontrado até512; não é divergência.
