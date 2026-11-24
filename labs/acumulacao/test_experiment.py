import unittest
from fractions import Fraction
try:
    from .experiment import integral,accumulation,rate,boundaries
except ImportError:
    from experiment import integral,accumulation,rate,boundaries

class AccumulationTests(unittest.TestCase):
    def test_orientation_and_additivity(self):
        for a in [-2,0,1,2]:
            for b in [-1,0,2]:
                self.assertEqual(integral(a,b),-integral(b,a))
                for c in [-3,0,3]:self.assertEqual(integral(a,b)+integral(b,c),integral(a,c))
        self.assertEqual(integral(-1,0),-.5)
        self.assertEqual(integral(0,-1),.5)

    def test_reference_and_chain(self):
        for x in [-2,-1,0,1,2]:
            self.assertEqual(accumulation(0,x),x*x/2);self.assertEqual(rate(0,x),x)
            self.assertEqual(accumulation(1,x),x**4/2);self.assertEqual(rate(1,x),2*x**3)
            self.assertEqual(accumulation(2,x),1.5*x*x);self.assertEqual(rate(2,x),3*x)

    def test_exact_incremental_quotients(self):
        for mode in range(3):
            for x in [Fraction(-1),Fraction(0),Fraction(1),Fraction(2)]:
                h=Fraction(1,10)
                central=(accumulation(mode,x+h)-accumulation(mode,x-h))/(2*h)
                error=2*x*h*h if mode==1 else 0
                self.assertEqual(central-rate(mode,x),error)

    def test_invalid_mode(self):
        for mode in [True,3,-1,'1']:
            with self.assertRaises(ValueError):boundaries(mode,1)

if __name__=='__main__':unittest.main()
