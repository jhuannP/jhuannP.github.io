"""Teste unilateral superior em lei binomial finita. Só biblioteca padrão."""
from fractions import Fraction as Q
from math import comb
from itertools import product

def rational(p):
    if type(p) not in (int,Q) or not 0<=p<=1:raise ValueError('probabilidade racional em0..1 necessária')
    return Q(p)
def pmf(n,p):
    if type(n) is not int or not 1<=n<=100:raise ValueError('n inteiro1..100 necessário')
    p=rational(p)
    return [comb(n,k)*p**k*(1-p)**(n-k) for k in range(n+1)]
def tail(n,s,p):
    law=pmf(n,p)
    if type(s) is not int or not 0<=s<=n:raise ValueError('s inteiro0..n necessário')
    return sum(law[s:],Q(0))
def rejection(n,p0,alpha):
    law=pmf(n,p0)
    alpha=rational(alpha)
    if not 0<alpha<1:raise ValueError('alpha entre zero e um necessário')
    return [s for s in range(n+1) if sum(law[s:],Q(0))<=alpha]

if __name__=='__main__':
    tails=0
    for n in range(1,9):
        for p in (Q(1,4),Q(1,2),Q(3,4)):
            counts=[Q(0)]*(n+1)
            for bits in product((0,1),repeat=n):
                weight=Q(1)
                for bit in bits:weight*=p if bit else 1-p
                counts[sum(bits)]+=weight
            assert counts==pmf(n,p) and sum(counts)==1
            for s in range(n+1):
                assert tail(n,s,p)==sum(counts[s:])
                tails+=1
    procedures=0
    for n in range(1,13):
        for p in (Q(1,4),Q(1,2),Q(3,4)):
            law=pmf(n,p)
            previous=Q(1)
            for s in range(n+1):
                value=tail(n,s,p)
                assert 0<=value<=previous<=1
                previous=value
            for alpha in (Q(1,100),Q(1,20),Q(1,10),Q(1,4)):
                region=rejection(n,p,alpha)
                assert sum(law[s] for s in region)<=alpha
                procedures+=1
    region=rejection(6,Q(1,2),Q(1,20));assert region==[6]
    assert tail(6,5,Q(1,2))==Q(7,64)
    assert pmf(6,Q(4,5))[6]==Q(4096,15625)
    assert 1-Q(63,64)**2==Q(127,4096)
    assert 1-Q(63,64)**10>Q(1,20)
    for n,s,p in [(True,1,Q(1,2)),(0,0,Q(1,2)),(6,7,Q(1,2)),(6,1,.5),(6,True,Q(1,2))]:
        try:tail(n,s,p)
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    print('24 leis enumeradas;',tails,'caudas;',procedures,'procedimentos; tamanho/poder/blocos e contratos aprovados.')
