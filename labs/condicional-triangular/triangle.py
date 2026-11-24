"""Modelo sintético f(x,y)=3x em 0<=y<=x<=1. Aritmética racional exata."""
from fractions import Fraction as Q

def rational(v):
    if isinstance(v, bool) or not isinstance(v, (int,Q)):
        raise TypeError("Use int ou Fraction; bool e float não são aceitos.")
    return Q(v)

def interval(a,b):
    a,b=rational(a),rational(b)
    if not 0<=a<=b<=1: raise ValueError("Intervalo ordenado dentro de [0,1].")
    return a,b

def marginal_x(x):
    x=rational(x)
    return 3*x*x if 0<=x<=1 else Q(0)

def marginal_y(y):
    y=rational(y)
    return Q(3,2)*(1-y*y) if 0<=y<=1 else Q(0)

def rectangle(a,b,c,d):
    """P(a<=X<=b,c<=Y<=d), sem estender o suporte ao quadrado."""
    a,b=interval(a,b);c,d=interval(c,d)
    lo,hi=max(a,c),min(b,d)
    mass=Q(0)
    if lo<hi:
        primitive=lambda x:x**3-Q(3,2)*c*x*x
        mass+=primitive(hi)-primitive(lo)
    lo=max(a,d)
    if lo<b: mass+=Q(3,2)*(d-c)*(b*b-lo*lo)
    return mass

def given_x(x,c,d):
    """Massa em [c,d] na versão uniforme em [0,x]; x=0 -> None."""
    x=rational(x);c,d=interval(c,d)
    if not 0<=x<=1: raise ValueError("x fora do suporte marginal.")
    if x==0: return None
    return max(Q(0),min(d,x)-c)/x

def given_y(y,a,b):
    """Massa em [a,b] na versão 2x/(1-y²), y<=x<=1; y=1 -> None."""
    y=rational(y);a,b=interval(a,b)
    if not 0<=y<=1: raise ValueError("y fora do suporte marginal.")
    if y==1:return None
    lo=max(a,y)
    return (b*b-lo*lo)/(1-y*y) if lo<b else Q(0)

def band_x(a,b,c,d):
    """Razão por uma faixa de X; condição de massa zero -> None."""
    numerator=rectangle(a,b,c,d)
    denominator=rectangle(a,b,0,1)
    return numerator/denominator if denominator else None

if __name__=='__main__':
    assert rectangle(0,1,Q(1,2),1)==Q(5,16)
    assert given_x(Q(1,2),Q(1,4),1)==Q(1,2)
    assert given_y(Q(1,2),Q(3,4),1)==Q(7,12)
    print("P(Y>1/2)=5/16; P(Y>1/4|X=1/2)=1/2; P(X>3/4|Y=1/2)=7/12")
