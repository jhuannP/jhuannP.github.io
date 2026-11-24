"""Velocidades divididas por c; boosts passivos ao longo de x.
Laboratório racional: o caso plano exige gamma racional (restrição do código).
"""
from fractions import Fraction as Q
from itertools import product
from math import isqrt
import unittest


def rational(x):
    if isinstance(x, bool) or not isinstance(x, (int, Q)):
        raise TypeError('Use int ou Fraction, sem conversão implícita de float')
    return Q(x)


def frame(b):
    b = rational(b)
    if abs(b) >= 1: raise ValueError('Boost precisa satisfazer |b|<1')
    return b


def collinear(a, b):
    a, b = rational(a), frame(b)
    if abs(a) > 1: raise ValueError('Estado causal necessário: |a|≤1')
    return (a-b)/(1-a*b)


def exact_gamma(b):
    b = frame(b)
    z = 1/(1-b*b)
    n, d = isqrt(z.numerator), isqrt(z.denominator)
    if n*n != z.numerator or d*d != z.denominator:
        raise ValueError('Este laboratório exato restringe o boost a gamma racional')
    return Q(n, d)


def planar(ax, ay, b):
    ax, ay, b = rational(ax), rational(ay), frame(b)
    if ax*ax+ay*ay > 1: raise ValueError('Estado fora do disco causal')
    denominator = 1-b*ax
    return (ax-b)/denominator, ay/(exact_gamma(b)*denominator)


class Checks(unittest.TestCase):
    def test_collinear_identity_and_inverse(self):
        for a, b in product((Q(i, 10) for i in range(-10, 11)),
                             (Q(i, 10) for i in range(-8, 9))):
            ap = collinear(a, b)
            self.assertEqual(collinear(ap, -b), a)
            self.assertEqual(1-ap*ap, (1-a*a)*(1-b*b)/(1-a*b)**2)
            if abs(a) < 1: self.assertLess(abs(ap), 1)
            else: self.assertEqual(ap, a)

    def test_planar_lorentz_events(self):
        boosts = (Q(0), Q(3, 5), Q(-3, 5), Q(4, 5), Q(-4, 5), Q(5, 13), Q(-5, 13))
        states = [(Q(i, 5), Q(j, 5)) for i, j in product(range(-5, 6), repeat=2) if i*i+j*j <= 25]
        for (ax, ay), b in product(states, boosts):
            actual = planar(ax, ay, b)
            g = exact_gamma(b)
            # Vetor de deslocamentos (c Δt, Δx, Δy) em unidades compatíveis.
            # Matriz de Lorentz aplicada antes de formar razões de componentes.
            event = (Q(5), 5*ax, 5*ay)
            matrix = ((g, -g*b, Q(0)), (-g*b, g, Q(0)), (Q(0), Q(0), Q(1)))
            transformed = tuple(sum(m*x for m, x in zip(row, event)) for row in matrix)
            self.assertGreater(transformed[0], 0)
            self.assertEqual(actual, (transformed[1]/transformed[0], transformed[2]/transformed[0]))
            self.assertEqual(planar(*actual, -b), (ax, ay))
            self.assertEqual(1-sum(x*x for x in actual), (1-b*b)*(1-ax*ax-ay*ay)/(1-b*ax)**2)
        print('Estados planos × boosts:', len(states)*len(boosts))

    def test_collinear_composition(self):
        vals = (Q(-4, 5), Q(-1, 2), Q(0), Q(1, 2), Q(4, 5))
        add = lambda a, b: collinear(a, -b)
        for a, b, c in product(vals, repeat=3):
            self.assertEqual(add(add(a, b), c), add(a, add(b, c)))
            self.assertEqual(add(a, b), add(b, a))
        # Exemplo original, sinal e taxa de aproximação em um único S.
        self.assertEqual(add(Q(1, 2), Q(1, 2)), Q(4, 5))
        self.assertEqual(collinear(Q(3, 5), Q(4, 5)), Q(-5, 13))
        self.assertEqual(Q(4, 5)-Q(-4, 5), Q(8, 5))
        self.assertEqual(collinear(Q(-4, 5), Q(4, 5)), Q(-40, 41))

    def test_low_speed_error_and_examples(self):
        for a, b in product((Q(i, 100) for i in range(-4, 5)), repeat=2):
            transformed = collinear(a, -b)
            galilean = a+b
            if transformed:
                self.assertEqual(abs(galilean-transformed)/abs(transformed), abs(a*b))
            else:
                self.assertEqual(galilean, 0)
        self.assertEqual(collinear(Q(1, 100), Q(-2, 100)), Q(150, 5001))
        self.assertEqual(planar(0, Q(3, 5), Q(3, 5)), (Q(-3, 5), Q(12, 25)))
        self.assertEqual(planar(0, 1, Q(3, 5)), (Q(-3, 5), Q(4, 5)))

    def test_contracts(self):
        for b in (-1, 1, Q(11, 10)):
            with self.assertRaises(ValueError): collinear(0, b)
        with self.assertRaises(ValueError): collinear(2, 0)
        with self.assertRaises(ValueError): planar(1, 1, 0)
        with self.assertRaises(ValueError): planar(0, 0, Q(1, 2))
        for a in (True, .5, float('nan'), '1/2'):
            with self.assertRaises(TypeError): collinear(a, 0)


if __name__ == '__main__':
    print('Partícula ultrapassada:', collinear(Q(3, 5), Q(4, 5)))
    print('Luz transversal:', planar(0, 1, Q(3, 5)))
    unittest.main()
