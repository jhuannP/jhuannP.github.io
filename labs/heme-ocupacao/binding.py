"""Sítio único e ligantes exclusivos: pesos reduzidos, não dados de proteína."""
from fractions import Fraction


def rational(value, positive=False):
    if type(value) not in (int, Fraction):
        raise ValueError('Use int ou Fraction, sem bool/float.')
    value = Fraction(value)
    if value < 0 or (positive and value == 0):
        raise ValueError('Valor fora do domínio.')
    return value


def populations(x, y=0):
    x, y = rational(x), rational(y)
    z = 1 + x + y
    return (1/z, x/z, y/z)  # livre, O, X


def from_pressure(p, p50, y=0):
    p, p50, y = rational(p), rational(p50, positive=True), rational(y)
    return populations(p/p50, y)


def drift(probs, ao, bo, ax, bx):
    """ao/ax são k_on[L] efetivos; bo/bx dissociações. Unidade comum 1/tempo."""
    if type(probs) is not tuple or len(probs) != 3:
        raise ValueError('Três populações em tupla.')
    free, oxygen, other = (rational(v) for v in probs)
    if free + oxygen + other != 1:
        raise ValueError('Populações devem somar um.')
    ao, ax = rational(ao), rational(ax)
    bo, bx = rational(bo, positive=True), rational(bx, positive=True)
    oxygen_flow = ao*free - bo*oxygen
    other_flow = ax*free - bx*other
    return (-oxygen_flow-other_flow, oxygen_flow, other_flow)


if __name__ == '__main__':
    print('x=3,y=2:', populations(3, 2))
    print('x=3,y=0:', populations(3))
    print('x=3,y=2, fluxo de equilíbrio:', drift(populations(3, 2), 3, 1, 2, 1))
    print('mesmo equilíbrio, velocidades iniciais distintas:',
          drift((1, 0, 0), 3, 1, 2, 1),
          drift((1, 0, 0), 30, 10, 20, 10))
