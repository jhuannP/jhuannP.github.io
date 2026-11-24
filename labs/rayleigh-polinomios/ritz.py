"""Rayleigh em polinômios racionais de Dirichlet, intervalo unitário."""
from fractions import Fraction as Q
from math import sqrt

def rational(v):
    if isinstance(v,bool) or not isinstance(v,(int,Q)):raise TypeError("Use int ou Fraction.")
    return Q(v)

def polynomial(p):
    if not isinstance(p,(tuple,list)) or not p:raise ValueError("Lista não vazia de coeficientes crescentes.")
    return tuple(map(rational,p))

def derivative(p):
    p=polynomial(p)
    return tuple(j*p[j] for j in range(1,len(p))) or (Q(0),)

def evaluate(p,x):
    p=polynomial(p);x=rational(x);v=Q(0)
    for a in reversed(p):v=v*x+a
    return v

def inner(p,q):
    p,q=polynomial(p),polynomial(q)
    return sum((a*b/Q(i+j+1) for i,a in enumerate(p) for j,b in enumerate(q)),Q(0))

def rayleigh(p):
    p=polynomial(p)
    if evaluate(p,0)!=0 or evaluate(p,1)!=0:raise ValueError("Dirichlet exige u(0)=u(1)=0.")
    mass=inner(p,p)
    if mass==0:raise ValueError("Função tentativa precisa ser não nula.")
    dp=derivative(p)
    return inner(dp,dp)/mass

F=(0,1,-1)
G=(0,0,1,-2,1)

def trial(a,b):
    a,b=rational(a),rational(b)
    return tuple(a*(F[j] if j<len(F) else 0)+b*G[j] for j in range(5))

def matrices():
    basis=(F,G)
    H=tuple(tuple(inner(derivative(u),derivative(v)) for v in basis) for u in basis)
    M=tuple(tuple(inner(u,v) for v in basis) for u in basis)
    return H,M

def normalized_characteristic():
    H,M=matrices();h,k,l=H[0][0],H[0][1],H[1][1];a,b,c=M[0][0],M[0][1],M[1][1]
    detm=a*c-b*b
    return ((h*l-k*k)/detm,(-h*c-l*a+2*k*b)/detm,Q(1))

def ritz_values():
    # Apenas o problema 2x2 desta base; aproximação float de raízes algébricas exatas.
    c,b,a=normalized_characteristic();delta=float(b*b-4*a*c)
    return ((-float(b)-sqrt(delta))/(2*float(a)),(-float(b)+sqrt(delta))/(2*float(a)))

if __name__=='__main__':
    print('R[f]=',rayleigh(F),'R[f+g]=',rayleigh(trial(1,1)))
    print('H,M=',matrices())
    print('Ritz=',ritz_values())
