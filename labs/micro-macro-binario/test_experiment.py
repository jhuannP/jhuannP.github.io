import unittest
from fractions import Fraction as Q
from itertools import product
from math import comb
from .experiment import macro_distribution, enumerate_distribution, moments

class BinaryStatesTests(unittest.TestCase):
    def test_enumeration_against_combinatorics(self):
        for n in range(10):
            for p in (Q(0), Q(1,4), Q(1,2), Q(2,3), Q(1)):
                with self.subTest(n=n, p=p):
                    result = macro_distribution(n, p)
                    self.assertEqual(result, enumerate_distribution(n, p))
                    self.assertEqual(sum(result), 1)
                    self.assertTrue(all(w >= 0 for w in result))

    def test_counts_partition_configurations(self):
        for n in range(10):
            counts = [0]*(n+1)
            for state in product((0,1), repeat=n):
                counts[sum(state)] += 1
            self.assertEqual(counts, [comb(n,m) for m in range(n+1)])
            self.assertEqual(sum(counts), 2**n)
            self.assertEqual(counts, counts[::-1])

    def test_moments_and_reflection(self):
        for n in range(10):
            for p in (Q(0), Q(1,4), Q(1,2), Q(2,3), Q(1)):
                d = macro_distribution(n,p)
                self.assertEqual(moments(d), (n*p, n*p*(1-p)))
                self.assertEqual(d, macro_distribution(n,1-p)[::-1])

    def test_lesson_numbers_and_mode_vs_band(self):
        d = macro_distribution(8)
        self.assertEqual(d[4], Q(35,128))
        self.assertEqual(sum(d[3:6]), Q(91,128))
        self.assertGreater(sum(d[3:6]), Q(1,2))
        self.assertLess(d[4], Q(1,2))
        self.assertEqual(macro_distribution(4, Q(1,4))[2], Q(27,128))
        self.assertEqual(macro_distribution(4)[2], Q(3,8))

    def test_contract_and_empty_configuration(self):
        self.assertEqual(macro_distribution(0), (Q(1),))
        self.assertEqual(enumerate_distribution(0), (Q(1),))
        for n,p in [(-1,Q(1,2)),(17,Q(1,2)),(True,Q(1,2)),(2.0,Q(1,2)),(4,.5),(4,True),(4,Q(-1)),(4,Q(2))]:
            for fn in (macro_distribution, enumerate_distribution):
                with self.assertRaises(ValueError): fn(n,p)
