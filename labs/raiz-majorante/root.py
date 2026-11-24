"""Família de série positiva e majorante; não decide limites a partir de amostra."""
from fractions import Fraction as Q

def index(n,allow_zero=False):
    if isinstance(n,bool) or not isinstance(n,int) or not (0 if allow_zero else 1)<=n<=128:
        raise ValueError('Índice inteiro no contrato0..128 ou1..128 necessário')
    return n

def term(n):
    n=index(n)
    return Q(1,(2 if n%2==0 else 3)**n)

def root_value(n):
    n=index(n)
    return Q(1,2 if n%2==0 else 3)

def partial(n):
    n=index(n,True)
    return sum((term(j) for j in range(1,n+1)),Q(0))

def tail(n):
    n=index(n,True)
    # Primeiro índice ímpar e primeiro par estritamente DEPOIS de n.
    odd=n+1 if n%2==0 else n+2
    even=n+2 if n%2==0 else n+1
    return Q(1,3**odd)/Q(8,9)+Q(1,2**even)/Q(3,4)

def bound(n):
    return Q(1,2**index(n,True))

def first_bound(tolerance):
    if isinstance(tolerance,bool) or not isinstance(tolerance,(int,Q)):
        raise ValueError('Tolerância int/Fraction necessária')
    tolerance=Q(tolerance)
    if not 0<tolerance<1:raise ValueError('0<tolerância<1 necessária')
    for n in range(129):
        if bound(n)<=tolerance:return n
    raise ValueError('A cota requer mais de128 termos no contrato')

if __name__=='__main__':
    print('Soma exata:',partial(0)+tail(0))
    n=first_bound(Q(1,100))
    print('Primeiro N para a cota<=1/100:',n)
    print('R_6=',tail(6),'cota_6=',bound(6))
    assert partial(7)+tail(7)==Q(17,24)
