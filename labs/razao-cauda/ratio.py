"""Termos fatoriais e cota geométrica do resto; frações exatas."""
from fractions import Fraction as Q
from math import factorial

def count(n):
    if isinstance(n,bool) or not isinstance(n,int) or n<0:raise ValueError("Índice inteiro não negativo")
    return n

def positive(v):
    if isinstance(v,bool) or not isinstance(v,(int,Q)) or v<=0:raise ValueError("Racional positivo")
    return Q(v)

def term(c,n):
    c=positive(c);n=count(n)
    return c**n/factorial(n)

def tail_bound(c,N):
    c=positive(c);N=count(N);q=c/(N+2)
    if q>=1:raise ValueError("Ainda não há majorante com q<1 nesta escolha")
    return term(c,N+1)/(1-q)

def choose_N(c,tolerance,maxN=100):
    c=positive(c);tolerance=positive(tolerance);maxN=count(maxN)
    for N in range(maxN+1):
        if c/(N+2)<1 and tail_bound(c,N)<tolerance:return N
    return None # orçamento insuficiente não significa série divergente

def verify():
    cases=0;comparisons=0
    for c in (Q(1,2),Q(1),Q(3),Q(5)):
        for N in range(15):
            if c/(N+2)>=1:continue
            q=c/(N+2);first=term(c,N+1)
            finite=Q(0)
            for j in range(40):
                a=term(c,N+1+j)
                assert a<=first*q**j
                assert term(c,N+2+j)/a==c/(N+2+j)
                finite+=a;comparisons+=1
            assert first<=finite<tail_bound(c,N)
            cases+=1
    assert term(1,4)/term(1,3)==Q(1,4)
    assert term(3,9)==Q(243,4480)
    assert tail_bound(3,8)==Q(243,3136)
    N=choose_N(3,Q(1,1000));assert N==12
    assert tail_bound(3,N)<Q(1,1000)<=tail_bound(3,N-1)
    assert choose_N(3,Q(1,1000),maxN=11) is None
    # Conferência finita das comparações usadas nas provas do caso L=1.
    for n in range(2,101):assert Q(1,n*n)<=Q(1,n-1)-Q(1,n)
    for k in range(8):
        block=sum((Q(1,n) for n in range(2**k+1,2**(k+1)+1)),Q(0))
        assert block>=Q(1,2)
    for bad in (-1,True,Q(1,2)):
        try:count(bad)
        except ValueError:pass
        else:raise AssertionError("índice")
    try:tail_bound(5,0)
    except ValueError:pass
    else:raise AssertionError("majorante inválida")
    print(f"{cases} cotas e {comparisons} comparações de termos/razões conferidas")
    print("c=3,N=8: resto <=",tail_bound(3,8))
    print("Primeiro N com esta cota <0,001:",N,"; cota:",tail_bound(3,N))

if __name__=='__main__':verify()
