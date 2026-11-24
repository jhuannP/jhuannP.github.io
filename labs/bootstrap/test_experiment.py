import unittest
from fractions import Fraction as Q
from itertools import product
from .experiment import exact_bootstrap, monte_carlo, percentile, PRESETS

class BootstrapTests(unittest.TestCase):
    def test_two_point_distribution_and_replacement(self):
        r=exact_bootstrap([0,2])
        self.assertEqual(r['masses'],{0:Q(1,4),1:Q(1,2),2:Q(1,4)})
        self.assertEqual(r['variance'],Q(1,2));self.assertEqual(r['bias'],0)
        self.assertEqual((r['lower'],r['upper']),(0,2))
        self.assertEqual(exact_bootstrap([5])['variance'],0)

    def test_mean_identity_and_affine_transform(self):
        for n in range(1,5):
            for data in product((-1,0,2),repeat=n):
                r=exact_bootstrap(data);mean=Q(sum(data),n)
                v=sum((Q(x)-mean)**2 for x in data)/n
                self.assertEqual(r['mean'],mean);self.assertEqual(r['variance'],v/n)
                self.assertEqual(sum(r['masses'].values()),1)
        for data in PRESETS:
            r=exact_bootstrap(data);moved=exact_bootstrap([-2*x+3 for x in data])
            self.assertEqual(moved['mean'],-2*r['mean']+3)
            self.assertEqual(moved['variance'],4*r['variance'])

    def test_duplicates_median_and_percentile_convention(self):
        r=exact_bootstrap([0,0,2],'median')
        self.assertEqual(r['masses'],{0:Q(20,27),2:Q(7,27)})
        self.assertEqual(r['bias'],Q(14,27));self.assertEqual(r['variance'],Q(560,729))
        values=[0,1,1,2]
        self.assertEqual(percentile(values,Q(1,4)),0)
        self.assertEqual(percentile(values,Q(1,2)),1)
        self.assertEqual(percentile(values,1),2)
        r=exact_bootstrap([2,2,2]);self.assertEqual(r['variance'],0)
        self.assertEqual((r['lower'],r['upper']),(2,2))

    def test_deterministic_monte_carlo_and_valid_support(self):
        for data in PRESETS:
            for kind in ('mean','median'):
                exact=exact_bootstrap(data,kind);r=monte_carlo(data,200,42,kind)
                self.assertEqual(r,monte_carlo(data,200,42,kind))
                self.assertTrue(set(r['masses'])<=set(exact['masses']))
                self.assertEqual(sum(r['masses'].values()),1)
                self.assertEqual(r['sample_variance'],r['variance']*Q(200,199))
        self.assertNotEqual(monte_carlo([0,2],200,42)['masses'],monte_carlo([0,2],200,1)['masses'])

    def test_contracts(self):
        for data in ([],[0]*6,[True,2],[.5,2]):
            with self.assertRaises(ValueError):exact_bootstrap(data)
        with self.assertRaises(ValueError):exact_bootstrap([0,2],'maximum')
        for b in (1,10001,True):
            with self.assertRaises(ValueError):monte_carlo([0,2],b)
        for seed in (-1,2**32,True):
            with self.assertRaises(ValueError):monte_carlo([0,2],200,seed)
        with self.assertRaises(ValueError):percentile([0,2],Q(3,2))

if __name__=='__main__':unittest.main()
