import unittest
from fractions import Fraction as F
from itertools import product
from .binding import populations, from_pressure, drift


class BindingTests(unittest.TestCase):
    def test_integer_weights_by_explicit_labels(self):
        for x, y in product(range(7), repeat=2):
            labels = ['free'] + ['oxygen']*x + ['other']*y
            expected = tuple(F(labels.count(label), len(labels)) for label in ['free', 'oxygen', 'other'])
            self.assertEqual(populations(x, y), expected)

    def test_independent_mass_action_balances(self):
        for ao, bo, ax, bx in product([F(1, 3), F(2), F(7, 2)], repeat=4):
            probs = populations(ao/bo, ax/bx)
            free, oxygen, other = probs
            self.assertEqual(sum(probs), 1)
            self.assertEqual(ao*free, bo*oxygen)
            self.assertEqual(ax*free, bx*other)
            self.assertEqual(drift(probs, ao, bo, ax, bx), (0, 0, 0))

    def test_landmarks_and_pressure_scale(self):
        self.assertEqual(populations(3, 2), (F(1, 6), F(1, 2), F(1, 3)))
        self.assertEqual(populations(3), (F(1, 4), F(3, 4), 0))
        for y in [0, F(1, 2), 2, 7]:
            for p50 in [F(1, 10), 2, 50]:
                self.assertEqual(from_pressure(p50*(1+y), p50, y)[1], F(1, 2))
                self.assertEqual(from_pressure(3*p50, p50, y), populations(3, y))
        self.assertEqual(populations(0, 0), (1, 0, 0))

    def test_monotonicity_conservation_and_distinct_kinetics(self):
        for y in [0, 1, 3]:
            values = [populations(F(i, 2), y)[1] for i in range(21)]
            self.assertEqual(values, sorted(values))
        for x in [F(1, 2), 1, 4]:
            values = [populations(x, y)[1] for y in range(8)]
            self.assertEqual(values, sorted(values, reverse=True))
        p = populations(3, 2)
        self.assertEqual(drift(p, 3, 1, 2, 1), drift(p, 30, 10, 20, 10))
        self.assertEqual(drift((1, 0, 0), 3, 1, 2, 1), (-5, 3, 2))
        self.assertEqual(drift((1, 0, 0), 30, 10, 20, 10), (-50, 30, 20))
        for probs in [(1, 0, 0), (0, 1, 0), (0, 0, 1), p]:
            self.assertEqual(sum(drift(probs, 3, 1, 2, 1)), 0)

    def test_contracts(self):
        for bad in [-1, True, 1.0, '1', None]:
            with self.assertRaises(ValueError): populations(bad)
            with self.assertRaises(ValueError): populations(1, bad)
        for bad in [0, -1, True, 1.0]:
            with self.assertRaises(ValueError): from_pressure(1, bad)
        for bad in [(1, 1, 0), (-1, 1, 1), [1, 0, 0], (True, 0, 0)]:
            with self.assertRaises(ValueError): drift(bad, 3, 1, 2, 1)
        with self.assertRaises(ValueError): drift((1, 0, 0), 3, 0, 2, 1)
