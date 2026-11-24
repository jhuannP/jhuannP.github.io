"""Distribuições de um modelo de linhagem; não simula tecido real."""
from fractions import Fraction as Q
from math import comb
from itertools import product

def distribution(p,n):
    if isinstance(p,bool) or not isinstance(p,(int,Q)) or not 0<=p<=1:
        raise ValueError('p racional entre zero e um necessário')
    if type(n) is not int or not 0<=n<=7:raise ValueError('rodadas inteiras 0..7 necessárias')
    p=Q(p); law={1:Q(1)}
    for _ in range(n):
        nxt={}
        for s,w in law.items():
            for k in range(2*s+1):
                mass=w*comb(2*s,k)*p**k*(1-p)**(2*s-k)
                if mass:nxt[k]=nxt.get(k,Q(0))+mass
        law=nxt
    return law

if __name__=='__main__':
    for p in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)):
        for n in range(7):
            law=distribution(p,n)
            assert sum(law.values())==1
            assert sum(k*v for k,v in law.items())==(2*p)**n
            if p==Q(1,2):
                variance=sum((k-1)**2*v for k,v in law.items())
                assert variance==Q(n,2)
    expected={0:Q(25,64),1:Q(20,64),2:Q(14,64),3:Q(4,64),4:Q(1,64)}
    assert distribution(Q(1,2),2)==expected
    # Six independent fair daughter choices: two at first generation,
    # four possible daughters at second generation, including unused positions.
    counts={k:0 for k in range(5)}
    for bits in product((0,1),repeat=6):
        total=bits[0]*(bits[2]+bits[3])+bits[1]*(bits[4]+bits[5])
        counts[total]+=1
    assert {k:Q(v,64) for k,v in counts.items()}==expected
    for n in range(1,7):
        assert distribution(0,n)=={0:Q(1)}
        assert distribution(1,n)=={2**n:Q(1)}
    q=Q(0)
    for n in range(7):
        assert distribution(Q(1,2),n).get(0,0)==q
        q=((1+q)/2)**2
    for p,n in [(True,1),(.5,1),(Q(-1,2),1),(Q(3,2),1),(Q(1,2),True),(Q(1,2),8)]:
        try:distribution(p,n)
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    print('35 leis: normalização/média; variância crítica, extremos, recorrência de extinção e 64 configurações independentes aprovados.')
