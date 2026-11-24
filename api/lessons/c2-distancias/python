"""Projeções euclidianas em R³; quadrados de distâncias racionais exatos."""
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


def plane_projection(R,n,d):
    R,n,d=vector(R),nonzero(n),scalar(d)
    residual=dot(n,R)-d
    factor=residual/dot(n,n)
    H=tuple(r-factor*c for r,c in zip(R,n))
    return dict(foot=H,residual=residual,squared_distance=residual**2/dot(n,n))


def line_projection(R,P,v):
    R,P,v=vector(R),vector(P),nonzero(v)
    w=tuple(r-p for r,p in zip(R,P))
    t=dot(w,v)/dot(v,v)
    H=tuple(p+t*c for p,c in zip(P,v))
    residual=tuple(r-h for r,h in zip(R,H))
    return dict(foot=H,parameter=t,residual=residual,squared_distance=dot(residual,residual))


if __name__=='__main__':
    print('Projeção de (1,1,1) no plano x+y+z=1:',plane_projection((1,1,1),(1,1,1),1))
    print('Normal reescalada:',plane_projection((1,1,1),(3,3,3),3))
    print('Projeção de (3,4,0) no eixo x:',line_projection((3,4,0),(0,0,0),(1,0,0)))
    print('As distâncias ao quadrado são exatas; a raiz pode ser irracional.')
