"""Família racional A_eta = diag_retangular(3,eta) V^T, 0<=eta<=3.
V1=(3/5,4/5), V2=(-4/5,3/5); imagem no plano das duas primeiras saídas.
Decomposição conhecida analiticamente; não é algoritmo geral de SVD.
"""
from fractions import Fraction as Q
V1=(Q(3,5),Q(4,5));V2=(Q(-4,5),Q(3,5))

def rational(x):
    if type(x) not in (int,Q): raise ValueError("int ou Fraction, sem bool/float")
    return Q(x)

def parameter(eta):
    eta=rational(eta)
    if not 0<=eta<=3: raise ValueError("0<=eta<=3")
    return eta

def vector(x,n):
    if not isinstance(x,(tuple,list)) or len(x)!=n: raise ValueError("dimensão incompatível")
    return tuple(rational(t) for t in x)

def norm_squared(x):
    return sum((rational(t)**2 for t in x),Q(0))

def matrix(eta,rank_one=False):
    eta=parameter(eta)
    if type(rank_one) is not bool: raise ValueError("rank_one bool")
    e=Q(0) if rank_one else eta
    return ((3*V1[0],3*V1[1]),(e*V2[0],e*V2[1]),(Q(0),Q(0)))

def apply(eta,x):
    x=vector(x,2)
    return tuple(sum((a*b for a,b in zip(row,x)),Q(0)) for row in matrix(eta))

def pseudoinverse(eta):
    eta=parameter(eta)
    second=tuple(t/eta for t in V2) if eta else (Q(0),Q(0))
    return tuple((V1[i]/3,second[i],Q(0)) for i in range(2))

def fit(eta,b,truncate=False):
    eta=parameter(eta);b=vector(b,3)
    if type(truncate) is not bool: raise ValueError("truncate bool")
    a=b[0]/3;c=b[1]/eta if eta and not truncate else Q(0)
    x=tuple(a*u+c*v for u,v in zip(V1,V2));prediction=apply(eta,x)
    residual=tuple(t-y for t,y in zip(b,prediction))
    return dict(x=x,prediction=prediction,residual=residual,residual_squared=norm_squared(residual),
                norm_squared=norm_squared(x),rank=2 if eta else 1,
                condition=3/eta if eta else None)
