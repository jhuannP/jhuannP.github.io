"""Bases e interpolação racional; não certifica a rotina float do painel."""
from fractions import Fraction as Q
from math import prod

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError("Use int/Fraction.")
    return Q(x)

def nodes(xs):
    xs=tuple(map(rational,xs))
    if not xs or len(set(xs))!=len(xs):raise ValueError("Nós distintos não vazios necessários.")
    return xs

def basis(xs,x):
    xs=nodes(xs);x=rational(x)
    return tuple(prod(((x-xj)/(xi-xj) for j,xj in enumerate(xs) if i!=j),start=Q(1)) for i,xi in enumerate(xs))

def weights(xs):
    xs=nodes(xs)
    return tuple(1/prod((xi-xj for j,xj in enumerate(xs) if i!=j),start=Q(1)) for i,xi in enumerate(xs))

def data(xs,ys):
    xs=nodes(xs);ys=tuple(map(rational,ys))
    if len(xs)!=len(ys):raise ValueError("Tamanhos iguais necessários.")
    return xs,ys

def lagrange(xs,ys,x):
    xs,ys=data(xs,ys)
    return sum((y*l for y,l in zip(ys,basis(xs,x))),Q(0))

def barycentric(xs,ys,x):
    xs,ys=data(xs,ys);x=rational(x)
    if x in xs:return ys[xs.index(x)]
    terms=tuple(w/(x-xi) for xi,w in zip(xs,weights(xs)))
    return sum((a*y for a,y in zip(terms,ys)),Q(0))/sum(terms,Q(0))

def amplification(xs,x):return sum(map(abs,basis(xs,x)),Q(0))

if __name__=='__main__':
    print(basis([0,1,2],Q(3,2)))
    print(lagrange([0,1,2],[0,1,4],Q(3,2)))
    print(amplification([0,1,2],Q(3,2)),amplification([0,1,2],3))
