"""Eletrostática em uma reta. SI; k arredondado, demais números racionais exatos."""
from fractions import Fraction as Q
from itertools import product
import unittest
K = Q(9_000_000_000)  # N m²/C², arredondamento didático, não valor físico exato.
NC = Q(1, 10**9)
MICRO_N = Q(1, 10**6)


def rational(v):
    if isinstance(v, bool) or not isinstance(v, (int, Q)):
        raise TypeError('Use int ou Fraction; não há conversão silenciosa de float')
    return Q(v)


def contribution(x, charge, position):
    x, charge, position = map(rational, (x, charge, position))
    if charge == 0: return Q(0)  # Fonte ausente não cria singularidade artificial.
    dx = x-position
    if dx == 0: raise ValueError('Ponto sobre uma fonte puntiforme não nula')
    return K*charge*dx/abs(dx)**3  # Componente assinada em N/C, não módulo.


def field(x, sources):
    x = rational(x); value = Q(0)
    for source in sources:
        if len(source) != 2: raise ValueError('Cada fonte tem carga e posição')
        charge, position = source
        value += contribution(x, charge, position)
    return value


def force(test_charge, x, sources):
    return rational(test_charge)*field(x, sources)  # N; campo externo, sem auto-interação.


class Checks(unittest.TestCase):
    def test_examples_and_units(self):
        sources = ((2*NC, 0), (-2*NC, Q(2, 5)))
        x = Q(1, 5)
        self.assertEqual(contribution(x, 2*NC, 0), 450)
        self.assertEqual(contribution(x, -2*NC, Q(2, 5)), 450)
        self.assertEqual(field(x, sources), 900)
        self.assertEqual(force(-NC, x, sources)/MICRO_N, Q(-9, 10))
        self.assertEqual(abs(force(3*NC, 0, ((-4*NC, Q(1, 5)),)))/MICRO_N, Q(27, 10))
        self.assertEqual(abs(force(2*NC, 0, ((2*NC, Q(2, 5)),)))/MICRO_N, Q(9, 40))
        self.assertEqual((3*NC)/Q(1, 10**6), Q(3, 1000))

    def test_newton_pair_forces(self):
        count = 0
        for a, b, x, distance in product((-3, -1, 0, 1, 3), (-3, -1, 0, 1, 3),
                                         (Q(-1), Q(0), Q(1, 2)), (Q(1, 4), Q(1, 2), Q(2))):
            q1, q2, y = a*NC, b*NC, x+distance
            f1 = force(q1, x, ((q2, y),)); f2 = force(q2, y, ((q1, x),))
            self.assertEqual(f1, -f2)
            self.assertEqual(abs(f1), K*abs(q1*q2)/distance**2)
            if a*b > 0: self.assertLess(f1, 0)  # Esquerda: repulsão da carga da direita.
            if a*b < 0: self.assertGreater(f1, 0)
            count += 1
        self.assertEqual(count, 225)

    def test_translation_and_distance_scaling(self):
        sources = ((2*NC, Q(0)), (-2*NC, Q(2, 5)))
        count = 0
        for x, shift, scale in product((Q(-2, 5), Q(-1, 5), Q(1, 10), Q(1, 5), Q(3, 10), Q(3, 5), Q(4, 5)),
                                        (Q(-2), Q(0), Q(1)), (Q(1, 2), Q(2), Q(3))):
            transformed = tuple((q, scale*p+shift) for q, p in sources)
            self.assertEqual(field(scale*x+shift, transformed), field(x, sources)/scale**2)
            count += 1
        self.assertEqual(count, 63)
        self.assertEqual(contribution(Q(2, 5), 2*NC, 0)/contribution(Q(1, 5), 2*NC, 0), Q(1, 4))

    def test_superposition_and_charge_scaling(self):
        a, b = (2*NC, 0), (-2*NC, Q(2, 5))
        for x in (Q(-1), Q(1, 10), Q(1, 5), Q(3, 5), Q(1)):
            total = field(x, (a, b))
            self.assertEqual(total, field(x, (a,))+field(x, (b,)))
            self.assertEqual(field(x, ((-a[0], a[1]), (-b[0], b[1]))), -total)
            self.assertEqual(field(x, ((2*a[0], a[1]), (2*b[0], b[1]))), 2*total)

    def test_field_zero_and_force_zero(self):
        x = Q(1, 5)
        self.assertEqual(field(x, ((2*NC, 0), (2*NC, Q(2, 5)))), 0)
        self.assertEqual(field(x, ((2*NC, 0), (-2*NC, Q(2, 5)))), 900)
        self.assertEqual(force(0, x, ((2*NC, 0), (-2*NC, Q(2, 5)))), 0)
        self.assertEqual(field(x, ()), 0)
        self.assertEqual(contribution(0, 0, 0), 0)

    def test_contracts(self):
        with self.assertRaises(ValueError): contribution(0, NC, 0)
        with self.assertRaises(ValueError): field(1, ((NC, 0, 2),))
        for x in (.2, True, float('nan')):
            with self.assertRaises(TypeError): field(x, ((NC, 0),))
        with self.assertRaises(TypeError): contribution(1, .1, 0)


if __name__ == '__main__':
    sources = ((2*NC, 0), (-2*NC, Q(2, 5)))
    print('Campo no ponto médio:', field(Q(1, 5), sources), 'N/C')
    print('Força sobre -1nC:', force(-NC, Q(1, 5), sources)/MICRO_N, 'microN')
    unittest.main()
