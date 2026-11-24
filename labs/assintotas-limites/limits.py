"""Funções racionais exatas; amostras não substituem as provas de limite."""
from fractions import Fraction as Q
from math import isqrt


def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int/Fraction, sem bool/float')
    return Q(x)


def original(x):
    x=rational(x);return (2*x*x+1)/(x*x+3)


def error(x):
    x=rational(x);return Q(5)/(x*x+3)


def positive_integer_cutoff(epsilon):
    """Menor inteiro POSITIVO N com |x|>=N => |f(x)-2|<epsilon.

    Resolva x²>5/epsilon-3 exatamente; não usa log/sqrt de float.
    """
    epsilon=rational(epsilon)
    if epsilon<=0:raise ValueError('epsilon positivo')
    threshold=max(Q(0),5/epsilon-3)
    return isqrt(threshold.numerator//threshold.denominator)+1


def crossing(x):
    x=rational(x);return 2+x/(x*x+1)


def reciprocal(x):
    x=rational(x)
    if not x:raise ValueError('x=0 excluído')
    return 1/x


def hole(x):
    x=rational(x)
    if x==1:raise ValueError('x=1 continua excluído após cancelamento')
    return (x*x-1)/(x-1)


def oblique(x):
    x=rational(x)
    if x==-1:raise ValueError('x=-1 excluído')
    return (x*x+x+1)/(x+1)


def first_derivative(x):
    x=rational(x);return 10*x/(x*x+3)**2


def second_derivative(x):
    x=rational(x);return 30*(1-x*x)/(x*x+3)**3


if __name__=='__main__':
    assert positive_integer_cutoff(Q(1,100))==23
    assert error(23)<Q(1,100)<=error(22)
    assert original(1)==Q(3,4) and crossing(0)==2
    print('N para erro<0,01:',positive_integer_cutoff(Q(1,100)))
