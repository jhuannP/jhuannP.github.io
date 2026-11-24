"""Somas geométricas racionais pequenas; precisão exata, sem dados medidos."""
from fractions import Fraction as Q

def number(v):
    if type(v) not in (int,Q):raise ValueError('use int/Fraction sem bool')
    return Q(v)

def count(n):
    if type(n) is not int or not 0<=n<=1000:raise ValueError('N inteiro0..1000')
    return n

def partial(a,r,n):
    a,r=number(a),number(r);n=count(n);total=Q(0);term=a
    for _ in range(n):total+=term;term*=r
    return total

def remainder(a,r,n):
    a,r=number(a),number(r);n=count(n)
    if abs(r)>=1:raise ValueError('o resto usa |r|<1')
    return a*r**n/(1-r)

def first_terms(a,r,tolerance,budget=100):
    a,r,tolerance=map(number,(a,r,tolerance));budget=count(budget)
    if abs(r)>=1 or tolerance<=0:raise ValueError('|r|<1 e tolerância positiva')
    for n in range(budget+1):
        if abs(remainder(a,r,n))<tolerance:return n
    return None

if __name__=='__main__':
    for a in (Q(-2),Q(0),Q(3,2)):
        for r in (Q(-2),Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1),Q(2)):
            for n in range(21):
                s=partial(a,r,n)
                closed=a*n if r==1 else a*(1-r**n)/(1-r)
                assert s==closed
                if abs(r)<1:assert s+remainder(a,r,n)==a/(1-r)
    assert partial(1,Q(1,2),4)==Q(15,8)
    assert remainder(1,Q(-1,2),3)==Q(-1,12)
    assert first_terms(1,Q(1,2),Q(1,1000),100)==11
    assert first_terms(1,Q(9,10),Q(1,1000),2) is None
    assert first_terms(0,Q(1,2),Q(1,1000))==0
    for bad in (True,1.5,-1,1001):
        try:partial(1,Q(1,2),bad)
        except ValueError:pass
        else:raise AssertionError('aceitou N inválido')
    print('441 somas por recorrência conferidas contra identidade finita.')
    print('r=1/2: primeiro N com erro<1/1000:',first_terms(1,Q(1,2),Q(1,1000)))
    print('r=-1/2: S3=',partial(1,Q(-1,2),3),'resto=',remainder(1,Q(-1,2),3))
