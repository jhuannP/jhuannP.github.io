import unittest
from fractions import Fraction as Q
from math import sqrt
from statistics import NormalDist
from .experiment import normal_cdf, normal_survival, mean_bernoulli

class LimitProbabilityTests(unittest.TestCase):
    def test_normal_reference_symmetry_and_scaling(self):
        for mu in (-3, 0, 10):
            for sd in (.25, 1, 2, 3):
                reference = NormalDist(mu, sd)
                for z in (-3, -1, 0, 1, 3):
                    x = mu+sd*z
                    self.assertAlmostEqual(normal_cdf(x, mu, sd), reference.cdf(x))
                    self.assertAlmostEqual(normal_cdf(x, mu, sd)+normal_survival(x, mu, sd), 1)
                    self.assertAlmostEqual(normal_cdf(x, mu, sd), normal_cdf(z))
        self.assertGreater(normal_survival(8), 0)
        self.assertAlmostEqual(normal_survival(8)/6.220960574271784e-16, 1)

    def test_exact_binomial_mean_variance_tail_and_bound(self):
        for n in (1, 2, 4, 10, 16, 40, 64, 100):
            for p in (Q(1, 10), Q(1, 4), Q(1, 2), Q(3, 4), Q(9, 10)):
                r = mean_bernoulli(n, p)
                self.assertEqual(sum(r['masses']), 1)
                self.assertEqual(r['mean'], p)
                self.assertEqual(r['variance'], p*(1-p)/n)
                self.assertLessEqual(r['tail'], r['chebyshev'])
        r = mean_bernoulli(4, Q(1, 2))
        self.assertEqual(r['tail'], Q(5, 8))
        self.assertEqual(r['chebyshev'], 1)

    def test_dependence_changes_variance_and_fourfold_sample_size(self):
        p = Q(1, 2)
        for n in (1, 4, 16, 64):
            repeated_outcomes = [(Q(0), 1-p), (Q(1), p)]
            repeated_mean = sum(x*w for x, w in repeated_outcomes)
            repeated_var = sum((x-repeated_mean)**2*w for x, w in repeated_outcomes)
            self.assertEqual(repeated_var, Q(1, 4))
            self.assertEqual(mean_bernoulli(n, p)['variance'], repeated_var/n)
        se16 = sqrt(float(mean_bernoulli(16, p)['variance']))
        se64 = sqrt(float(mean_bernoulli(64, p)['variance']))
        self.assertEqual(se64, se16/2)

    def test_contracts(self):
        for bad in (True, '1', float('inf'), float('nan')):
            with self.assertRaises(ValueError): normal_cdf(bad)
        for sd in (0, -1):
            with self.assertRaises(ValueError): normal_cdf(0, 0, sd)
        for n, p in [(0, Q(1, 2)), (101, Q(1, 2)), (True, Q(1, 2)), (2, 0), (2, 1), (2, .5)]:
            with self.assertRaises(ValueError): mean_bernoulli(n, p)
        with self.assertRaises(ValueError): mean_bernoulli(4, Q(1, 2), 0)

if __name__ == '__main__': unittest.main()
