"""Somas inteiras e contraexemplo: testar não é demonstrar indução."""
from math import isqrt


def natural(n,limit=1000):
    if isinstance(n,bool) or not isinstance(n,int) or not 0<=n<=limit:
        raise ValueError('n inteiro não negativo dentro do limite do experimento.')
    return n


def sums(n):
    n=natural(n)
    return dict(linear=sum(range(1,n+1)),odd=sum(2*k-1 for k in range(1,n+1)),
                squares=sum(k*k for k in range(1,n+1)))


def formulas(n):
    n=natural(n)
    return dict(linear=n*(n+1)//2,odd=n*n,squares=n*(n+1)*(2*n+1)//6)


def first_divisor(value):
    value=natural(value,1000000)
    if value<2:return None
    return next((d for d in range(2,isqrt(value)+1) if value%d==0),None)


def polynomial(n):
    n=natural(n,100)
    return n*n+n+41


def first_composite():
    for n in range(101):
        value=polynomial(n)
        divisor=first_divisor(value)
        if divisor is not None:return n,value,divisor
    return None


if __name__=='__main__':
    for n in (0,1,4,10):print('n=',n,'somas:',sums(n),'fórmulas:',formulas(n))
    n,value,d=first_composite()
    print('Primeiro contraexemplo testado a n²+n+41 sempre primo:',n,value,d)
    print('A base e o passo indutivo são demonstrados no texto, não inferidos desses testes.')
