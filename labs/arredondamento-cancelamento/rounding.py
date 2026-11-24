"""Comparações exatas do erro em exemplos float, não aritmética universal."""
from fractions import Fraction as Q
from math import isfinite, fsum


def finite_float(value):
    if type(value) is not float or not isfinite(value):
        raise ValueError('Use float finito, excluindo bool, texto e inteiros implícitos')
    return value


def errors(approximation, reference):
    error=abs(Q.from_float(approximation)-reference)
    return dict(absolute=error, relative=error/abs(reference) if reference else None)


def compare_expression(x):
    """f(x)=(1+x)^2-1 no recorte 0 <= x <= 1/4.

    A referência trata o float recebido como racional exato. Não mede a
    diferença entre o dado pretendido pelo usuário e o float já recebido.
    """
    x=finite_float(x)
    if not 0<=x<=0.25:raise ValueError('Recorte didático: 0 <= x <= 1/4')
    q=Q.from_float(x)
    reference=2*q+q*q
    naive=(1.0+x)*(1.0+x)-1.0
    reformulated=x*(2.0+x)
    return dict(reference=reference, naive=naive, reformulated=reformulated,
                naive_error=errors(naive,reference),
                reformulated_error=errors(reformulated,reference))


def compare_sum(values):
    """Referência é a soma racional exata dos floats recebidos, inclusive vazio."""
    if not isinstance(values,(tuple,list)):raise ValueError('Use lista/tupla de floats')
    values=[finite_float(x) for x in values]
    reference=sum((Q.from_float(x) for x in values),Q(0))
    naive=0.0
    for x in values:naive+=x
    accurate=fsum(values)  # Pode falhar por overflow; isso não é corrigido aqui.
    if not isfinite(naive) or not isfinite(accurate):
        raise OverflowError('Soma excedeu o recorte finito do laboratório')
    return dict(reference=reference,naive=naive,fsum=accurate,
                naive_error=errors(naive,reference),fsum_error=errors(accurate,reference))


if __name__=='__main__':
    from sys import float_info
    print('Formato do ambiente:',float_info.radix,float_info.mant_dig)
    x=2.0**-54
    result=compare_expression(x)
    assert result['naive']==0.0 and result['reformulated']==2*x
    print('Expressão ingênua/reformulada:',result['naive'],result['reformulated'])
    print(compare_sum([1e16,1.0,-1e16]))
