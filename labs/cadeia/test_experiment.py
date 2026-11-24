import unittest
from fractions import Fraction
try:
    from .experiment import factors,central
except ImportError:
    from experiment import factors,central

class ChainTests(unittest.TestCase):
    def test_reference_and_constant(self):
        self.assertEqual(factors(1,2)['derivative'],54)
        self.assertEqual(factors(-.5,2)['derivative'],0)
        self.assertEqual(factors(1,-2)['derivative'],-6)
        for x in [-1,0,1,2]:self.assertEqual(factors(x,0)['derivative'],0)

    def test_expanded_polynomial_reference(self):
        # Expansão independente: 1+3bx+3b²x²+b³x³.
        for x in [-1,-.5,0,1,2]:
            for b in [-2,-.5,0,.5,2]:
                expected=3*b+6*b*b*x+3*b**3*x*x
                self.assertAlmostEqual(factors(x,b)['derivative'],expected,places=12)

    def test_exact_central_error_formula(self):
        for x in [-1,0,1,2]:
            for b in [-2,0,2]:
                for h in [Fraction(1,10),Fraction(1,20)]:
                    f=lambda t:(1+b*t)**3
                    delta=(f(Fraction(x)+h)-f(Fraction(x)-h))/(2*h)
                    d=3*b*(1+b*x)**2
                    self.assertEqual(delta-d,b**3*h*h)
                    self.assertAlmostEqual(central(x,b,float(h)),float(delta),places=10)

    def test_contracts(self):
        for bad in [True,float('nan'),float('inf'),'1']:
            with self.assertRaises(ValueError):factors(bad,2)
        for h in [0,-1,True]:
            with self.assertRaises(ValueError):central(1,2,h)

if __name__=='__main__':unittest.main()
