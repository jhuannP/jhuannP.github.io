"""Variação quadrática: identidades finitas, momentos e malhas acopladas.
A enumeração finita confere os quatro primeiros momentos; não é lei browniana.
"""
from fractions import Fraction as Q
from itertools import product
from math import sqrt, isfinite, fsum
from random import Random

def qv(increments):
    return sum(x*x for x in increments)

def coarsen(increments):
    if not increments or len(increments)%2:
        raise ValueError("Quantidade positiva e par de incrementos")
    return [increments[i]+increments[i+1] for i in range(0,len(increments),2)]

def theory(steps):
    if not steps or any(isinstance(h,bool) or not isinstance(h,(int,Q)) or h<=0 for h in steps):
        raise ValueError("Passos racionais positivos")
    T=sum(steps)
    return T,2*sum(h*h for h in steps)

def coupled(n,T=1,seed=42):
    if isinstance(n,bool) or not isinstance(n,int) or n<2 or n%2:
        raise ValueError("n precisa ser inteiro positivo par")
    if isinstance(T,bool): raise ValueError("T real positivo finito")
    try: T=float(T)
    except (TypeError,ValueError,OverflowError): raise ValueError("T real positivo finito") from None
    if not isfinite(T) or T<=0: raise ValueError("T real positivo finito")
    rng=Random(seed);dw=[sqrt(T/n)*rng.gauss(0,1) for _ in range(n)]
    return dw,coarsen(dw)

def verify():
    cases=0;atoms=0
    # Z em {-1,0,1} com pesos 1/6,2/3,1/6. Delta=s Z tem
    # E[Delta²]=s²/3 e E[Delta⁴]=s⁴/3=3h², como a gaussiana.
    nodes=((-1,Q(1,6)),(0,Q(2,3)),(1,Q(1,6)))
    for n in range(1,7):
        for scales in ([Q(1)]*n,[Q(i+1,2) for i in range(n)]):
            mean=second=mass=Q(0)
            for state in product(nodes,repeat=n):
                prob=Q(1);inc=[]
                for scale,(z,w) in zip(scales,state):prob*=w;inc.append(scale*z)
                v=qv(inc);mass+=prob;mean+=prob*v;second+=prob*v*v;atoms+=1
            target,var=theory([s*s/3 for s in scales])
            assert mass==1 and mean==target and second-mean*mean==var
            assert var<=2*target*max(s*s/3 for s in scales)
            cases+=1
    paths=0
    for inc in product((Q(-1,2),Q(0),Q(1,2)),repeat=6):
        coarse=coarsen(inc)
        assert qv(coarse)-qv(inc)==2*sum(inc[i]*inc[i+1] for i in range(0,6,2))
        w=Q(0);left=Q(0)
        for delta in inc:left+=w*delta;w+=delta
        assert 2*left==w*w-qv(inc)
        paths+=1
    # Refinar a interpolação linear de uma série fixa fabrica Q/r ->0.
    inc=[Q(1,4),Q(-1,4),Q(1,2),Q(-1,8)]
    for r in (1,2,4,16):
        refined=[x/r for x in inc for _ in range(r)]
        assert qv(refined)==qv(inc)/r
    assert theory([Q(1,100)]*100)==(1,Q(1,50))
    assert theory([Q(1,4),Q(3,4)])==(1,Q(5,4))
    assert qv([Q(1),Q(-1)])==2 and qv(coarsen([1,-1]))==0
    assert qv([Q(1),Q(1)])==2 and qv(coarsen([1,1]))==4
    fine,coarse=coupled(1024)
    assert all(isfinite(x) for x in fine) and len(coarse)==512
    assert abs(fsum(fine)-fsum(coarse))<1e-12
    for n,T in ((1,1),(3,1),(True,1),(4,0),(4,float('nan')),(4,True)):
        try:coupled(n,T)
        except ValueError:pass
        else:raise AssertionError("contrato")
    print(f"{cases} leis de momentos ({atoms} átomos), {paths} identidades de trajetórias e interpolação conferidos")
    print("Amostra gaussiana acoplada, não prova de convergência:",qv(fine),qv(coarse))

if __name__=='__main__':verify()
