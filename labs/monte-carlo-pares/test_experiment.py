import unittest
from itertools import product as tuples
from fractions import Fraction as Q
from .experiment import moments,model,sample

class AntitheticTests(unittest.TestCase):
    def test_known_moments_and_equal_cost(self):
        expected=[(Q(1,3),Q(4,45),Q(1,180),Q(-7,90)),(Q(1,12),Q(1,180),Q(1,180),Q(1,180)),(Q(1,2),Q(1,12),Q(0),Q(-1,12))]
        from .experiment import FAMILIES
        for i,c in enumerate(FAMILIES):
            a=moments(c);self.assertEqual(tuple(a[k] for k in ('mean','var','pair_var','cov')),expected[i])
            for k in range(2,11):
                s=model(i,k);self.assertEqual(s['n'],2*s['m'])
                self.assertEqual(s['var_ind'],a['var']/s['n'])
                self.assertEqual(s['var_anti'],a['pair_var']/s['m'])
        self.assertEqual(model(0)['gain'],8);self.assertEqual(model(1)['gain'],Q(1,2));self.assertIsNone(model(2)['gain'])
    def test_general_quadratics_by_independent_quadrature(self):
        n=1024;h=1/n
        def quad(f):return h*(f(0)+f(1)+4*sum(f(i*h) for i in range(1,n,2))+2*sum(f(i*h) for i in range(2,n,2)))/3
        for c in tuples((-1,0,1),repeat=3):
            s=moments(c);f=lambda u:sum(a*u**i for i,a in enumerate(c))
            mu=quad(f);self.assertAlmostEqual(float(s['mean']),mu,delta=1e-11)
            self.assertAlmostEqual(float(s['var']),quad(lambda u:(f(u)-mu)**2),delta=1e-11)
            self.assertAlmostEqual(float(s['pair_var']),quad(lambda u:((f(u)+f(1-u))/2-mu)**2),delta=1e-11)
            self.assertEqual(s['pair_var'],(s['var']+s['cov'])/2)
    def test_variance_scaling_and_seeded_experiment(self):
        for i in range(3):
            s,t=model(i,4),model(i,6)
            self.assertEqual(s['var_ind'],4*t['var_ind'])
            self.assertEqual(s['var_anti'],4*t['var_anti'])
            a=sample(i,16,42);self.assertEqual(a,sample(i,16,42));self.assertEqual(a['evaluations_each'],32)
            self.assertGreaterEqual(a['se_plain'],0);self.assertGreaterEqual(a['se_paired'],0)
        self.assertEqual(sample(2)['paired'],.5)
    def test_contracts(self):
        for family,k in [(True,4),(3,4),(0,1),(0,11),(0,4.)]:
            with self.assertRaises(ValueError):model(family,k)
        for c in [[],[True],[.5],None]:
            with self.assertRaises(ValueError):moments(c)
        for args in [(0,1,42),(0,True,42),(0,4,-1)]:
            with self.assertRaises(ValueError):sample(*args)
