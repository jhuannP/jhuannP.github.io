"""Bayes na medida restrita, conferido por contagem independente."""
import unittest
from fractions import Fraction as Q
from itertools import product
from .weighted import condition

class BayesConditionedTests(unittest.TestCase):
    def test_all_finite_events_and_zero_cells(self):
        labels = "abc"
        events = [{x for i, x in enumerate(labels) if mask & (1 << i)} for mask in range(8)]
        for values in product(range(3), repeat=3):
            if not sum(values):
                continue
            weights = dict(zip(labels, values))
            atoms = [x for x, w in weights.items() for _ in range(w)]
            for A, B, C in product(events, repeat=3):
                observed = [x for x in atoms if x in A and x in C]
                if not observed:
                    self.assertIsNone(condition(weights, B, A & C))
                    continue
                expected = Q(sum(x in B for x in observed), len(observed))
                self.assertEqual(condition(weights, B, A & C), expected)
                if condition(weights, B, C) == 0:
                    self.assertIsNone(condition(weights, A, B & C))
                    self.assertEqual(expected, 0)
                else:
                    actual = condition(weights, A, B & C) * condition(weights, B, C) / condition(weights, A, C)
                    self.assertEqual(actual, expected)

    def test_die_posterior_and_inconsistent_factors(self):
        w = {i: 1 for i in range(1, 7)}
        A, O, C = {2, 3, 5}, {1, 3, 5}, {2, 3, 4, 5, 6}
        self.assertEqual(condition(w, O, C), Q(2, 5))
        self.assertEqual(condition(w, O, A & C), Q(2, 3))
        wrong = condition(w, A, O) * condition(w, O, C) / condition(w, A, C)
        self.assertEqual(wrong, Q(4, 9))
        self.assertNotEqual(wrong, condition(w, O, A & C))

    def test_dropping_C_can_change_the_answer(self):
        w = dict(a=1, b=2, c=3, d=4)
        A, B, C = {"a", "b", "c"}, {"b", "c"}, {"a", "c", "d"}
        self.assertEqual(condition(w, B, A), Q(5, 6))
        self.assertEqual(condition(w, B, A & C), Q(3, 4))
        self.assertNotEqual(condition(w, B, A), condition(w, B, A & C))
