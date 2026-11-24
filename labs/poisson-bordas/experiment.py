"""Poisson polinomial exato em [0,L], com bordas homogêneas."""
from fractions import Fraction as Q

def scalar(x):
    if type(x) not in (int,Q):
        raise ValueError("Use int ou Fraction; bool não é escalar")
    return Q(x)

def poly(coefficients):
    if type(coefficients) not in (tuple,list) or not coefficients:
        raise ValueError("Forneça coeficientes em ordem crescente, inclusive zeros")
    a=[scalar(c) for c in coefficients]
    while len(a)>1 and a[-1]==0:a.pop()
    return tuple(a)

def value(coefficients,x):
    a=poly(coefficients);x=scalar(x);y=Q(0)
    for c in reversed(a):y=y*x+c
    return y

def primitive(coefficients):
    return poly([Q(0)]+[c/Q(i+1) for i,c in enumerate(poly(coefficients))])

def derivative(coefficients):
    a=poly(coefficients)
    return poly([i*a[i] for i in range(1,len(a))] or [0])

def length(L):
    L=scalar(L)
    if L<=0:raise ValueError("L deve ser positivo")
    return L

def integral(coefficients,L=1):
    return value(primitive(coefficients),length(L))

def dirichlet(source,L=1):
    L=length(L);g=poly(source)
    u=[-c for c in primitive(primitive(g))]
    while len(u)<2:u.append(Q(0))
    u[1]-=value(u,L)/L
    return poly(u)

def neumann(source,L=1):
    L=length(L);g=poly(source)
    if integral(g,L)!=0:return None
    u=[-c for c in primitive(primitive(g))]
    u[0]-=integral(u,L)/L
    return poly(u)

if __name__=="__main__":
    assert dirichlet([1])==(Q(0),Q(1,2),Q(-1,2))
    assert neumann([1]) is None
    g=[-1,2]
    u=neumann(g)
    assert u==(Q(-1,12),Q(0),Q(1,2),Q(-1,3))
    assert integral(u)==0
    print("g=1: Dirichlet",dirichlet([1]),"; Neumann",neumann([1]))
    print("g=2x-1: Dirichlet",dirichlet(g))
    print("g=2x-1: Neumann, média zero",u)
