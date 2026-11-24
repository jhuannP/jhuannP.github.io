"""Reta 1D: SSE+lambda*w*w, intercepto livre, aritmética racional.
Não implementa Ridge multivariado nem escolhe lambda por validação.
"""
from fractions import Fraction as Q
from dataclasses import dataclass


def rational(v):
    if isinstance(v,bool) or not isinstance(v,(int,Q)):
        raise TypeError("Use int ou Fraction; float/bool não são entradas exatas.")
    return Q(v)


def penalty(lam):
    lam=rational(lam)
    if lam<0:raise ValueError("lambda deve ser não negativo.")
    return lam


def paired(x,y):
    if not isinstance(x,(list,tuple)) or not isinstance(y,(list,tuple)):
        raise TypeError("Use listas ou tuplas de números exatos.")
    if not x or len(x)!=len(y):raise ValueError("Dados não vazios, de mesmo tamanho.")
    return tuple(map(rational,x)),tuple(map(rational,y))


@dataclass(frozen=True)
class Fit:
    w: Q
    b: Q
    def __post_init__(self):
        object.__setattr__(self,"w",rational(self.w))
        object.__setattr__(self,"b",rational(self.b))


def fit_ridge(x,y,lam=0):
    x,y=paired(x,y);lam=penalty(lam)
    mx=sum(x)/len(x);my=sum(y)/len(y)
    sxx=sum((v-mx)**2 for v in x)
    sxy=sum((u-mx)*(v-my) for u,v in zip(x,y))
    if sxx+lam==0:
        raise ArithmeticError("Mínimos não únicos; esta rotina não escolhe um deles.")
    w=sxy/(sxx+lam)
    return Fit(w,my-w*mx)


def predict(model,x):
    if not isinstance(model,Fit):raise TypeError("Modelo deve ser Fit.")
    return model.w*rational(x)+model.b


def sse(x,y,model):
    x,y=paired(x,y)
    return sum(((predict(model,u)-v)**2 for u,v in zip(x,y)),Q(0))


def objective(x,y,model,lam=0):
    lam=penalty(lam)
    return sse(x,y,model)+lam*model.w**2


if __name__=="__main__":
    x=[-1,0,1];y=[-2,0,2]
    for lam in (0,2,6):
        fitted=fit_ridge(x,y,lam)
        print("lambda",lam,fitted,"SSE",sse(x,y,fitted),"objetivo",objective(x,y,fitted,lam))
