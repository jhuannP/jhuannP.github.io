"""Vetores racionais 2D em uma base cartesiana ortonormal.

Componentes numéricas apenas: a consistência das unidades cabe ao chamador.
"""
from fractions import Fraction as Q


def vector(value):
    if not isinstance(value, (tuple, list)) or len(value) != 2:
        raise ValueError('Vetor deve ser lista/tupla com duas componentes')
    if any(type(x) not in (int, Q) for x in value):
        raise ValueError('Componentes inteiras ou Fraction; bool/float excluídos')
    return tuple(Q(x) for x in value)


def add(a, b):
    a, b = vector(a), vector(b)
    return tuple(x+y for x,y in zip(a,b))


def scale(s, a):
    if type(s) not in (int, Q):
        raise ValueError('Escalar inteiro ou Fraction')
    return tuple(s*x for x in vector(a))


def dot(a, b):
    return sum((x*y for x,y in zip(vector(a),vector(b))), Q(0))


def norm_squared(a):
    return dot(a, a)


def quarter_turn_axes(a):
    """Mesma grandeza; eixos giram +90°: novas componentes são (y,-x)."""
    x,y = vector(a)
    return y,-x


def project(a, direction):
    """Projeção vetorial sobre a reta na direção não nula fornecida."""
    a, direction = vector(a), vector(direction)
    denominator = norm_squared(direction)
    if not denominator:
        raise ValueError('Não existe direção definida pelo vetor zero')
    return scale(dot(a,direction)/denominator, direction)


if __name__ == '__main__':
    force, displacement = (2,-1), (3,4)
    assert dot(force,displacement) == 2
    assert norm_squared(displacement) == 25
    assert project(force,displacement) == (Q(6,25),Q(8,25))
    assert dot(quarter_turn_axes(force),quarter_turn_axes(displacement)) == 2
    print('Trabalho: 2 J, se força em N e deslocamento em m.')
