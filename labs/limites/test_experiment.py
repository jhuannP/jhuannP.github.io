import unittest
from fractions import Fraction as Q
from .experiment import quotient,patched,affine_delta,quadratic_delta

class LimitTests(unittest.TestCase):
    def test_factorization_and_point_change(self):
        for numerator in range(-30,31):
            x=Q(numerator,10)
            if x!=2:
                self.assertEqual(quotient(x),x+2)
                for value in (-3,4,9):self.assertEqual(patched(x,value),quotient(x))
        self.assertEqual(patched(2,9),9)
        with self.assertRaises(ValueError):quotient(2)

    def test_affine_bound_with_negative_and_zero_slopes(self):
        for epsilon in (Q(1,10),Q(3,10),Q(1),Q(4)):
            for slope in (Q(-3),Q(-1,2),Q(0),Q(1,2),Q(3)):
                delta=affine_delta(epsilon,slope)
                for ratio in (Q(-9,10),Q(-1,2),Q(1,2),Q(9,10)):
                    h=ratio*delta
                    self.assertTrue(0<abs(h)<delta)
                    self.assertLess(abs(slope*h),epsilon)

    def test_quadratic_bound_and_naive_counterexample(self):
        for epsilon in (Q(1,10),Q(3,10),Q(1),Q(3),Q(4)):
            delta=quadratic_delta(epsilon)
            for ratio in (Q(-9,10),Q(-1,2),Q(1,2),Q(9,10)):
                x=1+ratio*delta
                self.assertTrue(0<abs(x-1)<delta)
                self.assertLess(abs(x*x-1),epsilon)
        epsilon=Q(3,10);x=1+epsilon/2
        self.assertLess(abs(x-1),epsilon)
        self.assertGreaterEqual(abs(x*x-1),epsilon)
        self.assertEqual(abs(x*x-1),Q(129,400))

    def test_contracts(self):
        for bad in (True,.3,'1/2'):
            with self.assertRaises(ValueError):quadratic_delta(bad)
        for bad in (0,-1):
            with self.assertRaises(ValueError):affine_delta(bad)
            with self.assertRaises(ValueError):quadratic_delta(bad)

if __name__=='__main__':unittest.main()
