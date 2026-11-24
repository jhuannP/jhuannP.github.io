"""Referências racionais, perturbações e fronteiras de representação."""
import unittest
from fractions import Fraction as Q
from itertools import product
from velocity import central, observed_velocity, position, error_bound


class VelocityTests(unittest.TestCase):
    def test_polynomial_references(self):
        # Derivadas analíticas por coeficientes, não por outra diferença finita.
        for coeff in product((-2,0,3), repeat=4):
            for t,h in product((Q(-1),Q(0),Q(2)), (Q(1,4),Q(1,2))):
                def f(x): return sum(Q(a)*x**k for k,a in enumerate(coeff))
                expected = sum(k*Q(a)*t**(k-1) for k,a in enumerate(coeff) if k)
                estimate = (f(t+h)-f(t-h))/(2*h)
                self.assertEqual(estimate-expected, coeff[3]*h*h)
                # Binary-exact sample inputs give exact float results for this grid.
                self.assertEqual(central(lambda x: sum(a*x**k for k,a in enumerate(coeff)),float(t),float(h)),float(estimate))

    def test_bounded_errors(self):
        delta=Q(1,4000)
        errors=(-delta,-delta/2,Q(0),delta/2,delta)
        for h in (Q(1,5),Q(1,10),Q(1,20),Q(1,40)):
            for ep,em in product(errors,repeat=2):
                self.assertLessEqual(abs(observed_velocity(h,ep,em)-5),error_bound(h,delta))
            self.assertEqual(observed_velocity(h,delta,-delta)-5,error_bound(h,delta))
        self.assertEqual(error_bound(Q(1,20),delta),Q(3,400))
        self.assertEqual(error_bound(Q(1,40),delta),Q(17,1600))

    def test_translation_and_rate(self):
        for h in (Q(1,2),Q(1,4),Q(1,8)):
            self.assertEqual(observed_velocity(h,offset=10**8),observed_velocity(h))
            self.assertEqual((observed_velocity(h)-5)/(observed_velocity(h/2)-5),4)
        self.assertEqual(central(lambda x:x**3,1,.5),3.25)
        # Smoothness cannot be checked from a centered quotient alone.
        self.assertEqual(central(abs,0,.25),0)

    def test_float_cancellation(self):
        # f(1 +/- h) rounds to the same large value despite distinct sample times.
        h=2.0**-30
        self.assertNotEqual(0.0+h,0.0)
        self.assertEqual(central(lambda t:1e16+t,0.0,h),0.0)
        self.assertEqual(central(lambda t:t,0.0,h),1.0)
        # At t=1 the samples straddle a rounding boundary instead of both vanishing.
        self.assertEqual(central(lambda t:1e16+t,1.0,h),2.0**30)

    def test_contracts(self):
        for x,h in [(True,.1),(1,False),(1,0),(1,-.1),(float('nan'),.1),(1,float('inf')),(10**1000,.1)]:
            with self.assertRaises(ValueError): central(lambda t:t,x,h)
        for x,h in [(1e16,1),(1e308,1e308),(0,1e308)]:
            with self.assertRaises(ArithmeticError): central(lambda t:t,x,h)
        with self.assertRaises(ValueError): central(lambda t:float('inf'),1,.1)
        with self.assertRaises(ArithmeticError): central(lambda t:1e308 if t>0 else -1e308,0,1)
        for h,delta in [(0,0),(-1,0),(1,-1),(.1,0),(1,True)]:
            with self.assertRaises(ValueError): error_bound(h,delta)


if __name__ == '__main__':
    unittest.main()
