"""Distribuição de ocupação em duas metades: modelo estático independente."""
from fractions import Fraction as F
from math import comb

def count(n,limit=512):
    if isinstance(n,bool) or not isinstance(n,int): raise TypeError('N inteiro.')
    if not 1<=n<=limit: raise ValueError('N fora do limite didático.')
    return n

def distribution(n):
    n=count(n)
    return tuple(F(comb(n,k),2**n) for k in range(n+1))

def moments(n):
    n=count(n)
    return {'mean':F(n,2),'variance':F(n,4),'fraction_variance':F(1,4*n),
            'relative_variance':F(1,n)}

def enumerate_assignments(n):
    n=count(n,16)
    totals=[0]*(n+1)
    for mask in range(2**n):
        totals[mask.bit_count()]+=1
    return tuple(totals)

def tail(n,minimum_deviation):
    n=count(n)
    if isinstance(minimum_deviation,bool) or not isinstance(minimum_deviation,(int,F)):
        raise TypeError('Desvio inteiro ou Fraction.')
    a=F(minimum_deviation)
    if a<0: raise ValueError('Desvio não negativo.')
    return sum((prob for k,prob in enumerate(distribution(n)) if abs(F(k)-F(n,2))>=a),F(0))

if __name__=='__main__':
    print('Ocupações N=8:',enumerate_assignments(8))
    p=distribution(8)
    assert p[4]==F(35,128)
    assert sum(p[2:7])==F(119,128)
    assert tail(8,3)==F(9,128)
    print('P(K=4)=',p[4],'; P(2≤K≤6)=',sum(p[2:7]))
    print('P(|K−4|≥3)=',tail(8,3),'; momentos:',moments(8))
    print('Sem tempos de espera ou simulação de dinâmica molecular.')
