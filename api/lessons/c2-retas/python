"""Retas em R³ com coordenadas racionais exatas."""
from fractions import Fraction as Q


def scalar(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError('Use inteiro ou Fraction.')
    return Q(x)


def vector(values):
    if not isinstance(values,(list,tuple)) or len(values)!=3:
        raise ValueError('Vetor com três coordenadas.')
    return tuple(map(scalar,values))


def direction(values):
    v=vector(values)
    if not any(v):raise ValueError('Direção nula não define uma reta.')
    return v


def point_at(P,v,t):
    P,v,t=vector(P),direction(v),scalar(t)
    return tuple(p+t*d for p,d in zip(P,v))


def parameter(P,v,R):
    P,v,R=vector(P),direction(v),vector(R)
    pivot=next(i for i,d in enumerate(v) if d)
    t=(R[pivot]-P[pivot])/v[pivot]
    return t if point_at(P,v,t)==R else None


def through(A,B):
    A,B=vector(A),vector(B)
    return A,direction(tuple(b-a for a,b in zip(A,B)))


if __name__=='__main__':
    P=(1,2,-1);v=(2,-1,2)
    for t in (-1,0,2):
        R=point_at(P,v,t)
        print('t=',t,'ponto=',R,'parâmetro recuperado=',parameter(P,v,R))
    print('Fora da reta:',parameter(P,v,(5,0,4)))
    print('Com direção vertical, só z varia:',point_at(P,(0,0,1),2))
    print('A projeção xy sozinha não verifica pertencimento em R³.')
