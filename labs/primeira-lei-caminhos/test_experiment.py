from math import fsum,log
from fractions import Fraction as F
import unittest
from .experiment import inspect

class FirstLawPathsTests(unittest.TestCase):
    def test_independent_pressure_integrals(self):
        for q in range(1,7):
            r=F(q,2);s=inspect(r);a=3.;b=float(3*r);n=4096;h=(b-a)/n
            value=h/3*fsum((1 if i in (0,n) else 4 if i%2 else 2)*300/(a+i*h) for i in range(n+1))
            self.assertAlmostEqual(s['isothermal'],value,places=8)
            # Constant-pressure rectangles; vertical segments have dV=0.
            self.assertEqual(s['pressure_first'],(b-a)*float(100/r))
            self.assertEqual(s['volume_first'],(b-a)*100)

    def test_endpoints_and_intermediate_temperatures(self):
        for q in range(1,7):
            r=F(q,2);s=inspect(r)
            self.assertEqual(s['v2']*s['p2'],300)
            self.assertEqual(s['t1'],s['t2'])
            self.assertEqual(s['intermediate_pressure_first'],3*s['p2'])
            self.assertEqual(s['intermediate_volume_first'],100*s['v2'])
            self.assertEqual(s['delta_u'],0)
        self.assertEqual(inspect(1)['isothermal'],0)
        self.assertEqual(inspect(1)['pressure_first'],0)
        self.assertEqual(inspect(1)['volume_first'],0)

    def test_order_and_signs(self):
        for q in [1,3,4,5,6]:
            r=F(q,2);s=inspect(r)
            self.assertLess(float(s['pressure_first']),s['isothermal'])
            self.assertLess(s['isothermal'],float(s['volume_first']))
            for key in ['isothermal','pressure_first','volume_first']:
                self.assertEqual(s[key]>0,r>1)
        self.assertAlmostEqual(inspect(F(1,2))['isothermal'],-inspect(2)['isothermal'],places=12)
        self.assertEqual(inspect(F(1,2))['pressure_first'],-inspect(2)['volume_first'])

    def test_contracts(self):
        for r in [True,False,0,-1,F(1,3),F(3,4),4,None,'2',float('inf'),float('nan')]:
            with self.assertRaises(ValueError):inspect(r)
