"""Ortogonalização racional; normalização somente para a família visual."""
from fractions import Fraction as F
from math import sqrt

def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))

def orthogonalize(vectors):
    if not isinstance(vectors,(list,tuple)) or not vectors or any(not isinstance(v,(list,tuple)) for v in vectors):
        raise ValueError("Família não vazia de vetores")
    dimension=len(vectors[0])
    if dimension==0 or any(len(v)!=dimension for v in vectors):raise ValueError("Dimensões incompatíveis")
    if any(type(x) not in (int,F) for v in vectors for x in v):raise ValueError("Use coordenadas int/Fraction")
    basis=[];skipped=[]
    for i,vector in enumerate(vectors):
        original=tuple(map(F,vector));residual=list(original)
        for u in basis:
            coefficient=dot(original,u)/dot(u,u)
            residual=[x-coefficient*y for x,y in zip(residual,u)]
        if any(residual):basis.append(tuple(residual))
        else:skipped.append(i)
    return basis,skipped

def model(t=1):
    if type(t) not in (int,F) or not -2<=t<=2 or (4*F(t)).denominator!=1:
        raise ValueError("t racional de -2 a 2 em quartos")
    t=F(t);v1=(F(1),F(1));v2=(1+t,1-t)
    basis,skipped=orthogonalize([v1,v2]);residual=(t,-t)
    q1=(1/sqrt(2),1/sqrt(2))
    q2=None if t==0 else (float(t)/sqrt(float(2*t*t)),-float(t)/sqrt(float(2*t*t)))
    return dict(t=t,v1=v1,v2=v2,residual=residual,norm_squared=2*t*t,
                rank=len(basis),skipped=skipped,q1=q1,q2=q2)

if __name__=='__main__':
    for t in (F(-1),F(0),F(1)):print(model(t))
