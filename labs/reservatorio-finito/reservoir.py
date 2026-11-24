"""Marginal microcanônica finita de sítios binários distinguíveis.
Energia total q*epsilon, epsilon>0; interação desprezada no balanço.
Distribuição estática, sem dinâmica nem atribuição de temperatura ao sistema finito.
"""
from itertools import product
from math import comb
from fractions import Fraction as Q

def geometry(total,q,m):
    if any(type(x) is not int for x in (total,q,m)):
        raise ValueError("contagens inteiras, sem bool")
    if not 1<=total<=4096 or not 0<=q<=total or not 1<=m<=min(total,8):
        raise ValueError("1<=L<=4096, 0<=q<=L, 1<=m<=min(L,8)")
    return total,q,m

def combinations(n,k):
    return comb(n,k) if 0<=k<=n else 0

def finite_patterns(total,q,m):
    total,q,m=geometry(total,q,m);den=comb(total,q)
    return {state:Q(combinations(total-m,q-sum(state)),den)
            for state in product((0,1),repeat=m)}

def canonical_patterns(p,m):
    if type(p) not in (int,Q): raise ValueError("p int ou Fraction")
    p=Q(p)
    if not 0<=p<=1 or type(m) is not int or not 1<=m<=8:
        raise ValueError("0<=p<=1, m inteiro de1 a8")
    return {state:p**sum(state)*(1-p)**(m-sum(state))
            for state in product((0,1),repeat=m)}

def total_variation(a,b):
    if a.keys()!=b.keys() or any(v<0 for d in (a,b) for v in d.values()):
        raise ValueError("mesmo suporte e probabilidades não negativas")
    if sum(a.values())!=1 or sum(b.values())!=1: raise ValueError("distribuições normalizadas")
    return sum((abs(a[k]-b[k]) for k in a),Q(0))/2

def compare_two(total,q):
    geometry(total,q,2);p=Q(q,total)
    f=finite_patterns(total,q,2);c=canonical_patterns(p,2)
    mean=sum((sum(k)*v for k,v in f.items()),Q(0))
    second=sum((sum(k)**2*v for k,v in f.items()),Q(0))
    covariance=f[(1,1)]-p*p
    return dict(p=p,finite=f,canonical=c,mean_count=mean,variance_count=second-mean*mean,
                covariance=covariance,total_variation=total_variation(f,c))
