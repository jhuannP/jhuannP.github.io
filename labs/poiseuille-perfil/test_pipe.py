import unittest
from fractions import Fraction as F
from itertools import product
from .pipe import flow,speed

class PipeTests(unittest.TestCase):
    def test_fixture(self):
        a=F(1,1000);r=flow(a,1,F(1,10),1000,1000)
        self.assertEqual(r['peak'],F(1,400));self.assertEqual(r['mean'],F(1,800))
        self.assertEqual(r['q_over_pi'],F(1,800000000));self.assertEqual(r['reynolds'],F(1,40))
        self.assertEqual(r['wall_stress_magnitude'],F(1,2))
        self.assertEqual(speed(a,1,F(1,10),1000,a/2),F(3,1600))

    def test_integral_and_boundary(self):
        for a,L,eta,drop in product((1,2,3),repeat=4):
            result=flow(a,L,eta,drop,1)
            self.assertEqual(speed(a,L,eta,drop,a),0)
            self.assertEqual(speed(a,L,eta,drop,0),result['peak'])
            # Simpson é exato para o integrando cúbico 2r*v(r).
            def f(r):return 2*r*speed(a,L,eta,drop,r)
            integral=F(a,6)*(f(0)+4*f(F(a,2))+f(a))
            self.assertEqual(integral,result['q_over_pi'])
            self.assertEqual(result['power_over_pi'],drop*integral)
            self.assertGreaterEqual(result['power_over_pi'],0)
            def diss(r):return F(eta)*L*(F(drop)*r/(2*eta*L))**2*2*r
            dissipation=F(a,6)*(diss(0)+4*diss(F(a,2))+diss(a))
            self.assertEqual(dissipation,result['power_over_pi'])

    def test_scaling_and_reversal(self):
        base=flow(1,2,3,4,5)
        radius=flow(2,2,3,4,5);pressure=flow(2,2,3,F(1,4),5)
        self.assertEqual(radius['q_over_pi'],16*base['q_over_pi'])
        self.assertEqual(radius['mean'],4*base['mean']);self.assertEqual(radius['reynolds'],8*base['reynolds'])
        self.assertEqual(pressure['q_over_pi'],base['q_over_pi'])
        reverse=flow(1,2,3,-4,5)
        for key in ('peak','mean','q_over_pi'):self.assertEqual(reverse[key],-base[key])
        for key in ('power_over_pi','reynolds','wall_stress_magnitude'):self.assertEqual(reverse[key],base[key])
        self.assertEqual(flow(1,2,3,0,5)['q_over_pi'],0)

    def test_contracts(self):
        for args in ((0,1,1,1,1),(1,-1,1,1,1),(1,1,0,1,1),(True,1,1,1,1),(1,1,1,1,0),(1.,1,1,1,1)):
            with self.assertRaises(ValueError):flow(*args)
        for r in (-1,2):
            with self.assertRaises(ValueError):speed(1,1,1,1,r)
