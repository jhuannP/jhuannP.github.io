"""Família (a*x+b)/(x*(x+1)**2), com domínio original preservado."""
from fractions import Fraction as Q

def rational(x):
    if type(x) not in (int,Q):raise ValueError("Use int ou Fraction")
    return Q(x)

def coefficients(a,b):
    a,b=rational(a),rational(b)
    return b,-b,a-b

def original(x,a=2,b=3):
    x,a,b=map(rational,(x,a,b))
    if x in (0,-1):raise ValueError("Ponto fora do domínio original")
    return (a*x+b)/(x*(x+1)**2)

def decomposed(x,a=2,b=3):
    x=rational(x)
    if x in (0,-1):raise ValueError("Ponto fora do domínio original")
    A,B,C=coefficients(a,b)
    return A/x+B/(x+1)+C/(x+1)**2

def proper_interval(left,right):
    left,right=rational(left),rational(right)
    low,high=sorted((left,right))
    return not any(low<=pole<=high for pole in (-1,0))

if __name__ == "__main__":
    print("A,B,C:",coefficients(2,3))
    for x in (-2,Q(-1,2),1,2):
        assert original(x)==decomposed(x)
        print(x,original(x))
    print("[1,2] próprio:",proper_interval(1,2))
    print("[-1/2,1/2] próprio:",proper_interval(Q(-1,2),Q(1,2)))
