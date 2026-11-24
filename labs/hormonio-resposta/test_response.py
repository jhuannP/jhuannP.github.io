from fractions import Fraction as F
from decimal import Decimal,localcontext
import unittest
from .response import equilibrium,drift,transient


class ResponseTests(unittest.TestCase):
    def test_literal_landmarks(self):
        a=equilibrium(2,2,4,1);b=equilibrium(2,2,1,4)
        self.assertEqual((a['u'],a['x'],a['maximum'],a['half_concentration']),
                         (F(1,2),F(2,3),F(4,5),F(2,5)))
        self.assertEqual((b['u'],b['x'],b['maximum'],b['half_concentration']),
                         (F(1,2),F(1,9),F(1,5),F(8,5)))
        self.assertEqual(equilibrium(F(2,5),2,4,1)['x'],F(2,5))
        self.assertEqual(equilibrium(1,2,0,1)['half_concentration'],None)

    def test_balance_and_fraction_invariant(self):
        for h in (0,F(1,5),1,2,20):
            for a in (0,1,4):
                for b in (1,2,4):
                    e=equilibrium(h,2,a,b)
                    self.assertEqual(drift(e['x'],h,2,a,b),0)
                    self.assertGreaterEqual(drift(0,h,2,a,b),0)
                    self.assertLess(drift(1,h,2,a,b),0)
                    self.assertTrue(0<=e['x']<=e['maximum']<=1)
                    self.assertEqual(e['x'],F(a)*h/((a+b)*h+2*b))

    def test_half_response_and_scaling(self):
        for kd in (1,2,5):
            for a,b in ((1,1),(4,1),(1,4)):
                e=equilibrium(0,kd,a,b);h=e['half_concentration']
                self.assertEqual(equilibrium(h,kd,a,b)['x'],e['maximum']/2)
                original=equilibrium(2,kd,a,b);fast=equilibrium(2,kd,10*a,10*b)
                self.assertEqual(original['x'],fast['x'])
                self.assertEqual(original['half_concentration'],fast['half_concentration'])
                self.assertEqual(fast['rate'],10*original['rate'])

    def test_time_against_decimal_and_rate_scaling(self):
        for h in (0,2):
            for initial in (F(0),F(1,3),F(1)):
                for t in (F(0),F(1,10),F(1),F(3)):
                    e=equilibrium(h,2,4,1)
                    with localcontext() as ctx:
                        ctx.prec=65
                        def dec(v):return Decimal(v.numerator)/Decimal(v.denominator)
                        ref=dec(e['x'])+(dec(initial)-dec(e['x']))*(-dec(e['rate'])*dec(t)).exp()
                    self.assertAlmostEqual(transient(h,2,4,1,initial,t),float(ref),places=14)
                    self.assertTrue(0<=transient(h,2,4,1,initial,t)<=1)
        self.assertEqual(transient(2,2,4,1,F(2,3),20),float(F(2,3)))
        # Stationary initial condition, boundary and common rate scaling.
        self.assertEqual(transient(0,2,4,1,0,2),0)
        self.assertGreater(transient(2,2,4,1,0,F(1,10)),0)
        self.assertAlmostEqual(transient(2,2,40,10,0,F(1,10)),transient(2,2,4,1,0,1))

    def test_contracts(self):
        for args in [(-1,2,4,1),(1,0,4,1),(1,2,-1,1),(1,2,4,0),(True,2,4,1),(1.,2,4,1)]:
            with self.assertRaises(ValueError):equilibrium(*args)
        for initial,t in [(2,1),(-1,1),(0,-1),(True,1),(0,10**1000)]:
            with self.assertRaises(ValueError):transient(2,2,4,1,initial,t)

if __name__=='__main__':unittest.main()
