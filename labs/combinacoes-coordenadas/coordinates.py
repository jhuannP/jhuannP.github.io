"""Exemplos 2D racionais; não é resolvedor genérico de sistemas."""
from fractions import Fraction as Q
from itertools import product

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError("Racional necessário")
    return Q(x)

def vector(v):
    a=tuple(v)
    if len(a)!=2:raise ValueError("Vetor 2D necessário")
    return tuple(rational(x) for x in a)

def combine(coefficients,vectors):
    c=tuple(rational(x) for x in coefficients);vs=tuple(vector(v) for v in vectors)
    if len(c)!=len(vs):raise ValueError("Um coeficiente por vetor")
    return tuple(sum((a*v[j] for a,v in zip(c,vs)),Q(0)) for j in range(2))

def basis_coordinates(v):
    x,y=vector(v)
    return x-y,y # Base ordenada B=((1,0),(1,1)).

def verify():
    u=(1,0);v=(1,1);w=(0,1);targets=redundant=0
    for x,y in product(range(-4,5),repeat=2):
        target=(Q(x),Q(y));a,b=basis_coordinates(target)
        assert combine((a,b),(u,v))==target
        assert combine((b,a),(v,u))==target
        assert x*x+y*y==a*a+2*a*b+2*b*b
        for t in map(Q,range(-3,4)):
            coeff=(x-t,t,y-t)
            assert combine(coeff,(u,v,w))==target
            redundant+=1
        if x==y:assert combine((x,0),((1,1),(2,2)))==target
        else:assert target[0]-target[1]!=0 # certificado de exclusão da reta.
        targets+=1
    assert combine((-1,1,-1),(u,v,w))==(0,0)
    assert combine((),())==(0,0)
    assert basis_coordinates((3,2))==(1,2)
    assert 3**2+2**2==13 and 1**2+2**2==5
    for lam in (Q(-1),Q(0),Q(1,2),Q(1),Q(2)):
        assert combine((1-lam,lam),(u,v))==(1,lam)
    # Conferência de fechamento por soma e escala para a mesma família.
    closure=0
    for a,b,s in product(range(-2,3),repeat=3):
        left=combine((a,b),(u,v));right=combine((1,-1),(u,v))
        assert combine((a+1,b-1),(u,v))==tuple(x+y for x,y in zip(left,right))
        assert combine((s*a,s*b),(u,v))==tuple(s*x for x in left)
        closure+=1
    for c,vs in (((1,),((1,0),(1,1))),((1,),((1,0,2),)),((True,),((1,0),))):
        try:combine(c,vs)
        except ValueError:pass
        else:raise AssertionError("dimensão/coeficiente")
    print(f"{targets} alvos, {redundant} representações redundantes e {closure} identidades de fechamento conferidos")
    print("(3,2): coordenadas na base B=(1,2); norma²=13, não5")

if __name__=='__main__':verify()
