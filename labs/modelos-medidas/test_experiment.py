import unittest,itertools
from fractions import Fraction as F
from .experiment import model

class PredictionComparisonTests(unittest.TestCase):
    def test_independent_fraction_reference(self):
        for a,b,B in itertools.product((0,1,2,3,4),(-20,0,20),(0,2,4,20)):
            m=model(a,b,B)
            for i,r in enumerate(m['rows']):
                t=F(i,2); noise=(F(0),F(1,50),F(-1,50),F(1,50),F(-1,50))[i]
                observed=F(1,2)+F(1,2)*t+t*t+noise+F(b,100)
                predicted=F(1,2)+F(1,2)*t+F(a,2)*t*t
                self.assertAlmostEqual(r['residual'],float(observed-predicted),places=13)
                self.assertEqual(r['within'],abs(observed-predicted)<=F(B,100))
    def test_exact_boundary_and_reference(self):
        self.assertEqual(model(2,0,2)['inside'],5)
        self.assertEqual(model(2,0,0)['inside'],1)
        self.assertEqual(model(0,0,4)['inside'],1)
        self.assertEqual(model(0,0,4)['rows'][-1]['residual'],3.98)
        self.assertEqual(model(2,10,4)['inside'],0)
    def test_bias_acceleration_and_bound_roles(self):
        for a in range(5):
            base=model(a,0,4)
            shifted=model(a,10,4)
            broader=model(a,0,20)
            for r,s,b in zip(base['rows'],shifted['rows'],broader['rows']):
                self.assertAlmostEqual(s['residual']-r['residual'],.1)
                self.assertEqual(r['observed'],b['observed'])
                self.assertEqual(r['predicted'],b['predicted'])
                self.assertEqual(r['residual'],b['residual'])
            self.assertGreaterEqual(broader['inside'],base['inside'])
        for u,v in zip(model(1)['rows'],model(2)['rows']):
            self.assertAlmostEqual(u['residual']-v['residual'],.5*u['time']**2)
    def test_domain(self):
        for args in [(True,0,4),(2.,0,4),(-1,0,4),(5,0,4),(2,21,4),(2,0,-1),(2,0,21)]:
            with self.assertRaises(ValueError):model(*args)
