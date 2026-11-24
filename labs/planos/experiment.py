"""Planos e incidência de retas em R³, com aritmética racional."""
from fractions import Fraction as Q


def scalar(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError('Use inteiro ou Fraction.')
    return Q(x)


def vector(values):
    if not isinstance(values,(list,tuple)) or len(values)!=3:raise ValueError('Três coordenadas necessárias.')
    return tuple(map(scalar,values))


def nonzero(values):
    v=vector(values)
    if not any(v):raise ValueError('Vetor não nulo necessário.')
    return v


def dot(a,b):return sum(x*y for x,y in zip(a,b))


def plane_from_points(A,B,C):
    A,B,C=map(vector,(A,B,C))
    u=tuple(b-a for a,b in zip(A,B));v=tuple(c-a for a,c in zip(A,C))
    n=nonzero((u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]))
    return n,dot(n,A)


def residual(n,d,R):
    return dot(nonzero(n),vector(R))-scalar(d)


def intersect(n,d,P,v):
    n,d,P,v=nonzero(n),scalar(d),vector(P),nonzero(v)
    denominator=dot(n,v)
    numerator=d-dot(n,P)
    if not denominator:
        return dict(kind='contained' if not numerator else 'parallel',parameter=None,point=None)
    t=numerator/denominator
    return dict(kind='unique',parameter=t,point=tuple(p+t*u for p,u in zip(P,v)))


if __name__=='__main__':
    n=(1,2,-1);d=3
    for P,v in (((0,0,0),(1,0,0)),((0,0,0),(2,-1,0)),((3,0,0),(2,-1,0))):
        print('Reta:',P,v,'incidência:',intersect(n,d,P,v))
    print('Plano por três pontos:',plane_from_points((1,0,0),(0,1,0),(0,0,1)))
    print('Resíduo não normalizado não é distância geométrica.')
