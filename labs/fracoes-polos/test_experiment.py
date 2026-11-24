import unittest
from fractions import Fraction as Q
from itertools import product
from .experiment import coefficients,original,decomposed,proper_interval

class PartialFractionsTests(unittest.TestCase):
    def test_polynomial_identity_all_coefficients(self):
        for a,b in product(range(-5,6),repeat=2):
            A,B,C=coefficients(a,b)
            # Numerador após recombinar: A(x+1)^2+B*x*(x+1)+C*x.
            self.assertEqual((A,2*A+B+C,A+B),(b,a,0))

    def test_exact_rational_values(self):
        for a,b in product(range(-3,4),repeat=2):
            for k in range(-12,13):
                x=Q(k,4)
                if x not in (0,-1):self.assertEqual(original(x,a,b),decomposed(x,a,b))

    def test_lesson_and_missing_repeated_factor(self):
        self.assertEqual(coefficients(2,3),(3,-3,-1))
        self.assertEqual(original(1),Q(5,4))
        self.assertNotEqual(original(1),Q(3)-Q(3,2))
        self.assertEqual(decomposed(Q(-1,2)),-16)

    def test_domains_and_oriented_intervals(self):
        for pole in (0,-1):
            for fn in (original,decomposed):
                with self.assertRaises(ValueError):fn(pole)
                with self.assertRaises(ValueError):fn(pole,0,0)
        for a,b in [(1,2),(-3,-2),(Q(-3,4),Q(-1,4))]:
            self.assertTrue(proper_interval(a,b));self.assertTrue(proper_interval(b,a))
        for a,b in [(-2,2),(-1,2),(Q(-1,2),Q(1,2)),(-2,-1),(0,0)]:
            self.assertFalse(proper_interval(a,b));self.assertFalse(proper_interval(b,a))

    def test_contract(self):
        for x in (True,1.,None,"1"):
            with self.assertRaises(ValueError):coefficients(x,3)
            with self.assertRaises(ValueError):original(x)
            with self.assertRaises(ValueError):decomposed(x)
            with self.assertRaises(ValueError):proper_interval(x,2)
