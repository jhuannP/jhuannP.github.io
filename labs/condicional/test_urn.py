"""Oráculo por pares de objetos, sem simulação ou dependências externas."""
import unittest
from fractions import Fraction as Q
from itertools import permutations, product
from .weighted import condition

class UrnTests(unittest.TestCase):
    def test_three_red_two_blue(self):
        weights = {p: 1 for p in permutations(range(5), 2)}
        A = {p for p in weights if p[0] < 3}
        B = {p for p in weights if p[1] < 3}
        self.assertEqual(len(weights), 20)
        self.assertEqual(condition(weights, B, A), Q(1, 2))
        self.assertEqual(condition(weights, A & B, weights), Q(3, 10))
        self.assertEqual(condition(weights, B, weights), Q(3, 5))
        self.assertEqual(condition(weights, A, B), Q(1, 2))
        Ac = set(weights) - A
        self.assertEqual(condition(weights, B, A)*condition(weights, A, weights)
                         + condition(weights, B, Ac)*condition(weights, Ac, weights), Q(3, 5))

    def test_general_formula_against_enumeration(self):
        for n in range(2, 13):
            for r in range(n + 1):
                with self.subTest(n=n, r=r):
                    w = {p: 1 for p in permutations(range(n), 2)}
                    A = {p for p in w if p[0] < r}
                    B = {p for p in w if p[1] < r}
                    self.assertEqual(condition(w, A, w), Q(r, n))
                    self.assertEqual(condition(w, B, w), Q(r, n))
                    self.assertEqual(condition(w, A & B, w), Q(r*(r-1), n*(n-1)))
                    self.assertEqual(condition(w, B, A), Q(r-1, n-1) if r else None)

    def test_replacement_requires_another_space(self):
        w = {p: 1 for p in product(range(5), repeat=2)}
        A = {p for p in w if p[0] < 3}
        B = {p for p in w if p[1] < 3}
        self.assertEqual(len(w), 25)
        self.assertEqual(condition(w, B, A), Q(3, 5))
        self.assertEqual(condition(w, A & B, w), Q(9, 25))

if __name__ == '__main__':
    unittest.main()
