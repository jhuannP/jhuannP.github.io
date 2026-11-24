import itertools
import unittest
from fractions import Fraction as F
from .sequential import sequence_probability as probability

class SequentialConditioningTests(unittest.TestCase):
    def test_labeled_objects_independent_count(self):
        # Enumera identidades distintas, sem usar a regra do produto por cores.
        for n in range(1, 9):
            for red in range(n + 1):
                for k in range(min(3, n) + 1):
                    outcomes = list(itertools.permutations(range(n), k))
                    for chars in itertools.product('RB', repeat=k):
                        pattern = ''.join(chars)
                        count = sum(all(('R' if obj < red else 'B') == color
                                        for obj, color in zip(outcome, pattern))
                                    for outcome in outcomes)
                        self.assertEqual(probability(red, n-red, pattern), F(count, len(outcomes)))
    def test_partition_and_color_symmetry(self):
        for red, blue in itertools.product(range(5), repeat=2):
            for k in range(min(red+blue, 3)+1):
                patterns = [''.join(c) for c in itertools.product('RB', repeat=k)]
                self.assertEqual(sum(probability(red, blue, s) for s in patterns), 1)
                for s in patterns:
                    self.assertEqual(probability(red, blue, s), probability(blue, red, s.translate(str.maketrans('RB','BR'))))
    def test_condition_and_dependence(self):
        for red in range(1, 6):
            for blue in range(1, 6):
                p1 = probability(red, blue, 'R')
                joint = probability(red, blue, 'RR')
                self.assertEqual(joint/p1, F(red-1, red+blue-1))
                self.assertLess(joint, p1*p1)
        self.assertEqual(probability(3,2,'RR'), F(3,10))
        self.assertEqual(probability(3,2,'RB') + probability(3,2,'BR'), F(3,5))
    def test_contract_and_impossible_paths(self):
        self.assertEqual(probability(0,0,''), 1)
        self.assertEqual(probability(1,2,'RRB'), 0)
        self.assertEqual(probability(0,3,'R'), 0)
        for red,blue,pattern in [(-1,2,'R'),(True,2,'R'),(1.5,2,'R'),(1,2,'X'),(1,2,[]),(1,1,'RRR')]:
            with self.assertRaises(ValueError): probability(red,blue,pattern)
