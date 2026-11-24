"""Média de lista: contrato explícito, sem leitura ou impressão na função."""
import math
from fractions import Fraction


def _racionais(valores):
    if type(valores) is not list or not valores:
        raise ValueError('Use uma lista não vazia')
    result=[]
    for x in valores:
        if type(x) not in (int,float):
            raise ValueError('Use int ou float; bool não é aceito')
        try:
            finite=math.isfinite(float(x))
        except OverflowError:
            finite=False
        if not finite:
            raise ValueError('Cada valor deve ser representável como float finito')
        result.append(Fraction(x))
    return result


def media(valores):
    """Float da média exata dos valores recebidos; não modifica a lista."""
    values=_racionais(valores)
    return float(sum(values,Fraction(0))/len(values))


if __name__=='__main__':
    assert math.isclose(media([0.1,0.2,0.3]),0.2,rel_tol=1e-12,abs_tol=1e-15)
    assert media([7])==7
    print(media([2,4,6]))
