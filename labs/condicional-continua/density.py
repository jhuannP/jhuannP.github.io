"""Modelo didático fixo f(x,y)=6/5*(x*x+y) no quadrado unitário.
Aritmética racional; não estima distribuições nem taxas de dados reais.
"""
from fractions import Fraction as Q

def rational(value):
    if isinstance(value,bool) or not isinstance(value,(int,Q)):
        raise TypeError("Use int ou Fraction; float não é entrada exata.")
    return Q(value)

def unit(value):
    value=rational(value)
    if not 0 <= value <= 1:
        raise ValueError("Valor fora de [0,1].")
    return value

def interval(a,b):
    a,b=unit(a),unit(b)
    if a>b: raise ValueError("Limites invertidos.")
    return a,b

def joint(x,y):
    x,y=rational(x),rational(y)
    return Q(6,5)*(x*x+y) if 0<=x<=1 and 0<=y<=1 else Q(0)

def marginal_x(x):
    x=rational(x)
    return Q(6,5)*(x*x+Q(1,2)) if 0<=x<=1 else Q(0)

def rectangle(a,b,c,d):
    """P(a<=X<=b,c<=Y<=d). Intervalos degenerados têm massa zero."""
    a,b=interval(a,b);c,d=interval(c,d)
    return Q(6,5)*((b**3-a**3)*(d-c)/3+(b-a)*(d*d-c*c)/2)

def point_interval(x,c,d):
    """Integral da versão contínua de f(Y|X=x); NÃO divide por P(X=x)."""
    x=unit(x);c,d=interval(c,d)
    return (x*x*(d-c)+(d*d-c*c)/2)/(x*x+Q(1,2))

def band_interval(a,b,c,d):
    """Condicionamento no evento de largura positiva; zero retorna None."""
    a,b=interval(a,b);c,d=interval(c,d)
    mass=rectangle(a,b,0,1)
    return rectangle(a,b,c,d)/mass if mass else None

def posterior_x_density(x,c,d):
    """Densidade de X após c<=Y<=d; faixa nula retorna None.

    Modelo fixo deste módulo, não um estimador de densidades.
    """
    x=rational(x);c,d=interval(c,d)
    mass=rectangle(0,1,c,d)
    if not mass: return None
    if not 0<=x<=1: return Q(0)
    return Q(6,5)*(x*x*(d-c)+(d*d-c*c)/2)/mass

def posterior_x_interval(a,b,c,d):
    """P(a<=X<=b | c<=Y<=d); evento condicionante nulo retorna None."""
    a,b=interval(a,b);c,d=interval(c,d)
    mass=rectangle(0,1,c,d)
    return rectangle(a,b,c,d)/mass if mass else None
