import unittest
from fractions import Fraction as Q
from .experiment import square,reciprocal,nonquadratic,curvature_bound

class LinearizationTests(unittest.TestCase):
    def test_square_exact_remainder_and_scaling(self):
        for a in range(-4,5):
            for h in (Q(-1,2),Q(1,2),Q(1,10),Q(-1,10)):
                r=square(a,h)
                self.assertEqual(r['error'],h*h)
                self.assertEqual(square(a,h/2)['absolute'],r['absolute']/4)
                self.assertEqual(curvature_bound(2,h),r['absolute'])
        self.assertEqual(square(2,Q(1,10))['linear'],Q(22,5))
        self.assertIsNone(square(1,-1)['relative'])
        self.assertEqual(square(0,Q(1,100))['relative'],1)

    def test_reciprocal_against_algebraic_identity(self):
        for a in (Q(-2),Q(-1),Q(1),Q(2)):
            for h in (Q(-1,10),Q(1,10),Q(1,2)):
                r=reciprocal(a,h)
                self.assertEqual(r['error'],h*h/(a*a*(a+h)))
        self.assertEqual(reciprocal(1,Q(1,10))['linear'],Q(9,10))
        self.assertEqual(reciprocal(1,Q(1,10))['error'],Q(1,110))
        # Sur [0,9;1,1], |f″|≤2/(0,9³).
        for h in (Q(-1,10),Q(1,10)):
            self.assertLessEqual(abs(reciprocal(1,h)['error']),curvature_bound(Q(2)/Q(9,10)**3,h))

    def test_differentiability_does_not_supply_quadratic_remainder(self):
        for n in range(1,31):
            r=nonquadratic(Q(1,n))
            self.assertEqual(r['remainder']/r['h'],Q(1,n))
            self.assertEqual(r['remainder']/r['h']**2,n)
        self.assertGreater(nonquadratic(Q(1,100))['over_h_squared'],nonquadratic(Q(1,10))['over_h_squared'])

    def test_contracts(self):
        for a,h in ((0,1),(1,-1)):
            with self.assertRaises(ValueError):reciprocal(a,h)
        with self.assertRaises(ValueError):nonquadratic(0)
        with self.assertRaises(ValueError):curvature_bound(-1,1)
        for h in (True,.1):
            with self.assertRaises(ValueError):square(2,h)

if __name__=='__main__':unittest.main()
