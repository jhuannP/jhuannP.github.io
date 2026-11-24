"""Referências racionais para produto, quociente e domínio."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use inteiro ou Fraction.')
    return Q(x)


def product_derivative(x):
    x=rational(x)
    return 2*x*(x+1)+x*x


def quotient_value(x):
    x=rational(x)
    if x==-1:raise ValueError('x=-1 está fora do domínio.')
    return (x*x+1)/(x+1)


def quotient_derivative(x):
    x=rational(x)
    if x==-1:raise ValueError('x=-1 está fora do domínio.')
    return (2*x*(x+1)-(x*x+1))/(x+1)**2


def quotient_increment(x,h):
    x,h=rational(x),rational(h)
    if not h:raise ValueError('h deve ser diferente de zero.')
    return (quotient_value(x+h)-quotient_value(x))/h


def cancelled_value(x):
    x=rational(x)
    if x==1:raise ValueError('A expressão original tem um furo em x=1.')
    return (x*x-1)/(x-1)


if __name__=='__main__':
    for x in (-2,0,1,2):
        print('x=',x,'produto:',product_derivative(x),'quociente:',quotient_derivative(x))
    for h in (Q(1,10),Q(-1,10),Q(1,100)):
        print('Secante do quociente em 0:',h,quotient_increment(0,h))
    print('Derivada do quociente em 0:',quotient_derivative(0))
    print('Cancelar um fator não preenche o ponto excluído do domínio.')
