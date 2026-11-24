"""PCA2D da aula preservada; estado congelado para aplicar em dados novos."""
from math import exp,log1p,sqrt,hypot,atan2,cos,sin,isfinite
from random import Random

def finite(x):
    if isinstance(x,bool):raise ValueError('Número real finito necessário')
    try:y=float(x)
    except (ValueError,TypeError,OverflowError):raise ValueError('Número real finito necessário') from None
    if not isfinite(y):raise ValueError('Número real finito necessário')
    return y

def pca_2d(points):
    rows=[list(p) for p in points]
    if not rows or any(len(p)!=2 for p in rows):raise ValueError('Pontos 2D necessários')
    rows=[[finite(v) for v in p] for p in rows];n=len(rows)
    mean=[sum(p[j] for p in rows)/n for j in range(2)];centered=[[p[j]-mean[j] for j in range(2)] for p in rows]
    a=sum(p[0]**2 for p in centered)/n;b=sum(p[0]*p[1] for p in centered)/n;d=sum(p[1]**2 for p in centered)/n
    angle=.5*atan2(2*b,a-d);direction=[cos(angle),sin(angle)]
    delta=hypot(a-d,2*b);values=[(a+d+delta)/2,(a+d-delta)/2]
    scores=[sum(v*w for v,w in zip(p,direction)) for p in centered]
    return dict(mean=mean,direction=direction,eigenvalues=values,scores=scores,degenerate=delta<1e-12)

from dataclasses import dataclass
from fractions import Fraction as Q

@dataclass(frozen=True)
class Model:
    mean:tuple
    direction:tuple
    eigenvalues:tuple
    degenerate:bool

def rows(points,empty=False):
    try:r=[list(p) for p in points]
    except TypeError:raise ValueError("Sequência de pontos2D necessária.") from None
    if (not r and not empty) or any(len(p)!=2 for p in r):raise ValueError("Pontos2D necessários.")
    return [[finite(v) for v in p] for p in r]

def fit(points):
    r=rows(points)
    try:result=pca_2d(r)
    except OverflowError:raise ArithmeticError("Escala fora do domínio numérico didático.") from None
    if any(not isfinite(v) for key in ('mean','direction','eigenvalues') for v in result[key]):
        raise ArithmeticError("Estatísticas não finitas; rever escala.")
    return Model(tuple(result['mean']),tuple(result['direction']),tuple(result['eigenvalues']),result['degenerate'])

def transform(model,points):
    if not isinstance(model,Model):raise TypeError("Modelo ajustado necessário.")
    return tuple(sum((p[j]-model.mean[j])*model.direction[j] for j in range(2)) for p in rows(points,empty=True))

def inverse(model,scores):
    if not isinstance(model,Model):raise TypeError("Modelo ajustado necessário.")
    return tuple(tuple(model.mean[j]+finite(t)*model.direction[j] for j in range(2)) for t in scores)

def explained_ratio(model):
    total=sum(model.eigenvalues)
    return model.eigenvalues[0]/total if total>0 else None

def exact_covariance(points):
    """Referência racional; somente int/Fraction, diferente do ajuste float."""
    if not isinstance(points,(list,tuple)) or not points or any(not isinstance(p,(list,tuple)) or len(p)!=2 for p in points):
        raise ValueError("Pontos2D necessários.")
    if any(isinstance(v,bool) or not isinstance(v,(int,Q)) for p in points for v in p):raise TypeError("Referência requer int/Fraction.")
    r=[tuple(map(Q,p)) for p in points];n=len(r)
    mu=tuple(sum(p[j] for p in r)/n for j in range(2))
    C=tuple(tuple(sum((p[i]-mu[i])*(p[j]-mu[j]) for p in r)/n for j in range(2)) for i in range(2))
    return mu,C

if __name__=='__main__':
    data=((12,22),(8,18),(11,19),(9,21));m=fit(data)
    print('média,covariância=',exact_covariance(data))
    print('modelo=',m,'fração de variância=',explained_ratio(m))
    print('novo ponto=',transform(m,[(14,20)]),'reconstrução=',inverse(m,transform(m,[(14,20)])))
