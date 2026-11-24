"""Casos racionais: furo, função afim e garantia para x² em a=1."""
from fractions import Fraction as Q


def rational(value):
    if isinstance(value,bool) or not isinstance(value,(int,Q)):
        raise ValueError('Use int ou Fraction')
    return Q(value)


def quotient(x):
    x=rational(x)
    if x==2:raise ValueError('O quociente original não está definido em 2')
    return (x*x-4)/(x-2)


def patched(x,value=9):
    x,value=rational(x),rational(value)
    return value if x==2 else x+2


def affine_delta(epsilon,slope=3):
    epsilon,slope=rational(epsilon),rational(slope)
    if epsilon<=0:raise ValueError('epsilon positivo')
    return Q(1) if slope==0 else epsilon/abs(slope)


def quadratic_delta(epsilon):
    epsilon=rational(epsilon)
    if epsilon<=0:raise ValueError('epsilon positivo')
    return min(Q(1),epsilon/3)


if __name__=='__main__':
    for k in range(1,5):
        h=Q(1,10**k)
        for x in (2-h,2+h):assert quotient(x)==x+2
        print('h=',h,'valores perto de 2:',quotient(2-h),quotient(2+h))
    assert patched(2)==9 and patched(Q(201,100))==Q(401,100)
    epsilon=Q(3,10);delta=quadratic_delta(epsilon);x=1+delta/2
    assert 0<abs(x-1)<delta and abs(x*x-1)<epsilon
    print('Garantia quadrática: delta=',delta,'erro selecionado=',abs(x*x-1))
    naive=epsilon;x=1+naive/2
    assert 0<abs(x-1)<naive and abs(x*x-1)>=epsilon
    print('Escolha ingênua delta=epsilon falha: erro=',abs(x*x-1))
