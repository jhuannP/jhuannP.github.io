import unittest
from fractions import Fraction as Q
from math import exp, log
from .experiment import (uniform_cdf, uniform_interval, exponential_cdf,
                         exponential_survival, exponential_interval, exponential_quantile)

class ContinuousModelTests(unittest.TestCase):
    def test_uniform_intervals_against_exact_overlap(self):
        grid = [Q(i, 2) for i in range(-4, 9)]
        for a in (Q(-1), Q(0), Q(1)):
            for width in (Q(1, 2), Q(2), Q(3)):
                for lo in grid:
                    for hi in grid:
                        expected = max(Q(0), min(hi, a+width)-max(lo, a))/width
                        self.assertAlmostEqual(uniform_interval(float(lo), float(hi), float(a), float(width)), float(expected))
                self.assertEqual(uniform_interval(float(a), float(a+width), float(a), float(width)), 1)
                self.assertEqual(uniform_interval(float(a), float(a), float(a), float(width)), 0)

    def test_exponential_normalization_and_memoryless(self):
        for rate in (.01, .25, 1, 2, 4, 100):
            self.assertEqual(exponential_cdf(0, rate), 0)
            self.assertEqual(exponential_survival(0, rate), 1)
            self.assertEqual(exponential_cdf(-1, rate), 0)
            for t in (0, .01, .5, 2):
                self.assertAlmostEqual(exponential_cdf(t, rate)+exponential_survival(t, rate), 1)
                for s in (0, .1, .4):
                    ratio = exponential_survival(s+t, rate)/exponential_survival(s, rate)
                    self.assertAlmostEqual(ratio, exponential_survival(t, rate))
        self.assertAlmostEqual(exponential_survival(log(2)/2, 2), .5)

    def test_quantiles_intervals_and_small_probabilities(self):
        for rate in (.01, .5, 2, 100):
            for u in (0, .001, .25, .5, .9, 1-1e-10):
                t = exponential_quantile(u, rate)
                self.assertGreaterEqual(t, 0)
                self.assertAlmostEqual(exponential_cdf(t, rate), u)
            self.assertAlmostEqual(exponential_interval(.5, 1, rate), exp(-rate*.5)-exp(-rate))
            self.assertEqual(exponential_interval(1, .5, rate), 0)
        small = exponential_cdf(1e-15, 2)
        self.assertGreater(small, 0); self.assertAlmostEqual(small/2e-15, 1)
        self.assertAlmostEqual(exponential_interval(10, 10+1e-6, 2)/(exp(-20)*2e-6), 1, places=5)

    def test_contracts(self):
        for bad in (True, '2', float('inf'), float('nan')):
            with self.assertRaises(ValueError): uniform_cdf(bad)
            with self.assertRaises(ValueError): exponential_cdf(bad)
        for width in (0, -1):
            with self.assertRaises(ValueError): uniform_cdf(1, 0, width)
        with self.assertRaises(ValueError): uniform_cdf(1, 1e20, 1)
        for rate in (0, -1, .001, 101, True):
            with self.assertRaises(ValueError): exponential_cdf(1, rate)
        for u in (-.1, 1, 2):
            with self.assertRaises(ValueError): exponential_quantile(u)

if __name__ == '__main__': unittest.main()
