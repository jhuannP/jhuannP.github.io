"""Experimento didático original; Python padrão, sem dados medidos."""
from fractions import Fraction as Q
from math import isfinite


def finite(value):
    if type(value) not in (int, float):
        raise ValueError('Use int ou float finito, sem booleanos.')
    try:
        result = float(value)
    except OverflowError:
        raise ValueError('Valor fora da representação float.') from None
    if not isfinite(result):
        raise ValueError('Valor finito necessário.')
    return result


def central(f, x, h):
    """Diferença central em float; não estima nem certifica o erro."""
    x, h = finite(x), finite(h)
    if h <= 0:
        raise ValueError('Passo positivo necessário.')
    left, right, width = x - h, x + h, 2 * h
    if not all(isfinite(v) for v in (left, right, width)):
        raise ArithmeticError('Pontos ou denominador fora de escala.')
    if left == x or right == x:
        raise ArithmeticError('Passo não resolvido na representação de x.')
    numerator = finite(f(right)) - finite(f(left))
    if not isfinite(numerator):
        raise ArithmeticError('Diferença de valores fora de escala.')
    result = numerator / width
    if not isfinite(result):
        raise ArithmeticError('Resultado fora de escala.')
    return result


def rational(value):
    if type(value) not in (int, Q):
        raise ValueError('A referência exata aceita apenas int ou Fraction.')
    return Q(value)


def position(t, offset=0):
    """s(t)=offset+2t+t^3, valores numéricos em SI."""
    t, offset = rational(t), rational(offset)
    return offset + 2*t + t**3


def observed_velocity(h, error_plus=0, error_minus=0, offset=0):
    """Referência racional em t=1; erros absolutos de posição em metros."""
    h = rational(h)
    if h <= 0:
        raise ValueError('Passo positivo necessário.')
    return (position(1+h, offset) + rational(error_plus)
            - position(1-h, offset) - rational(error_minus)) / (2*h)


def error_bound(h, delta):
    """Limite h^2+delta/h para este cúbico, com |erros|<=delta."""
    h, delta = rational(h), rational(delta)
    if h <= 0 or delta < 0:
        raise ValueError('Exige h>0 e delta>=0.')
    return h*h + delta/h


def experiment():
    delta = Q(1, 4000)
    print('Experimento sintético: v(1)=5 m/s; delta=1/4000 m')
    print('h(s)  sem erro(m/s)  erros opostos(m/s)  limite(m/s)')
    for h in (Q(1,5), Q(1,10), Q(1,20), Q(1,40)):
        print(h, observed_velocity(h), observed_velocity(h,delta,-delta), error_bound(h,delta))
    print('\nFloat: alterar a origem não altera a derivada matemática.')
    print('h(s) |erro sem offset| |erro offset 1e8 m|')
    for k in (1,3,5,7,9):
        h = 10.0**(-k)
        values = [abs(central(lambda t: offset+2*t+t**3,1.0,h)-5.0)
                  for offset in (0.0,1e8)]
        print(h, *values)
    print('Os erros float são observações deste runtime, não uma lei monotônica.')


if __name__ == '__main__':
    experiment()
