"""Protocolo de observação: eventos distintos em um espaço ampliado."""
import unittest
from fractions import Fraction as Q
from itertools import product
from .weighted import condition

class ObservationTests(unittest.TestCase):
    def test_uniform_pairs_against_expanded_space(self):
        pairs = list(product((0, 1), repeat=2))
        weights = {(pair, j): 1 for pair in pairs for j in range(2)}
        both = {x for x in weights if x[0] == (1, 1)}
        exists = {x for x in weights if any(x[0])}
        observed = {x for x in weights if x[0][x[1]] == 1}
        self.assertEqual((len(exists), len(observed), len(both)), (6, 4, 2))
        self.assertEqual(condition(weights, both, exists), Q(1, 3))
        self.assertEqual(condition(weights, both, observed), Q(1, 2))
        self.assertEqual([condition(weights, {x for x in weights if x[0] == pair}, observed)
                          for pair in pairs], [Q(0), Q(1,4), Q(1,4), Q(1,2)])

    def test_bayes_with_nonuniform_pair_weights(self):
        pairs = list(product((0, 1), repeat=2))
        for masses in product(range(3), repeat=4):
            if not sum(masses):
                continue
            # Each position is chosen with probability 1/2 independently of the pair.
            weights = {(pair, j): m for pair, m in zip(pairs, masses) for j in range(2)}
            both = {x for x in weights if x[0] == (1, 1)}
            observed = {x for x in weights if x[0][x[1]] == 1}
            denominator = masses[1] + masses[2] + 2*masses[3]
            expected = Q(2*masses[3], denominator) if denominator else None
            self.assertEqual(condition(weights, both, observed), expected)

    def test_always_observing_first_position(self):
        weights = {pair: 1 for pair in product((0, 1), repeat=2)}
        first_on = {pair for pair in weights if pair[0] == 1}
        both = {(1, 1)}
        self.assertEqual(condition(weights, both, first_on), Q(1, 2))
        # Same numerical answer does not make the observation events identical.
        self.assertEqual(first_on, {(1, 0), (1, 1)})
