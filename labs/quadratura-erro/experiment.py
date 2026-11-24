"""Regras compostas racionais em [0,1], com referência analítica independente."""
from fractions import Fraction as F

def rules(f,n):
    if not callable(f) or type(n) is not int or n<=0 or n%2:
        raise ValueError("Comparação conjunta exige função e n positivo par")
    values=[f(F(i,n)) for i in range(n+1)]
    if any(type(v) not in (int,F) for v in values):raise ValueError("A função deve retornar int/Fraction")
    h=F(1,n);v=list(map(F,values))
    trapezoid=h*((v[0]+v[-1])/2+sum(v[1:-1],F(0)))
    simpson=h/3*(v[0]+v[-1]+4*sum(v[1:-1:2],F(0))+2*sum(v[2:-1:2],F(0)))
    return trapezoid,simpson

def model(family=0,level=2):
    if type(family) is not int or family not in (0,1) or type(level) is not int or not 1<=level<=6:
        raise ValueError("family=0 ou1; level inteiro1..6")
    n=2**level;f=(lambda x:x**4) if family==0 else (lambda x:abs(x-F(3,10)))
    integral=F(1,5) if family==0 else (F(3,10)**2+F(7,10)**2)/2
    t,s=rules(f,n)
    return dict(family=family,level=level,n=n,h=F(1,n),integral=integral,trapezoid=t,simpson=s,
                et=t-integral,es=s-integral,
                bound_t=F(1,n*n) if family==0 else None,
                bound_s=F(2,15*n**4) if family==0 else None)

if __name__=='__main__':
    for family in (0,1):
        for level in range(1,7):print(model(family,level))
