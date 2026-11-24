from fractions import Fraction as Q
from itertools import product
from math import isclose,log
import unittest
from .exact import matches_integer_log,equation_candidate

class LogarithmTests(unittest.TestCase):
    def test_exact_powers_and_independent_float_reference(self):
        for base,n in product((Q(1,3),Q(1,2),Q(2),Q(3),Q(10)),range(-8,9)):
            x=base**n
            self.assertTrue(matches_integer_log(base,x,n))
            self.assertFalse(matches_integer_log(base,x,n+1))
            self.assertTrue(isclose(log(float(x))/log(float(base)),n,abs_tol=1e-12))

    def test_product_quotient_and_power(self):
        for m,n in product(range(-4,5),repeat=2):
            a=Q(2)**m;b=Q(2)**n
            self.assertTrue(matches_integer_log(2,a*b,m+n))
            self.assertTrue(matches_integer_log(2,a/b,m-n))
            self.assertTrue(matches_integer_log(2,a**3,3*m))
        # Unequal arguments avoid the accidental equality log2(2+2)=log2(2)+log2(2).
        self.assertFalse(matches_integer_log(2,6,3))

    def test_domain_before_equation(self):
        roots=[x for x in range(-10,11) if equation_candidate(x)]
        self.assertEqual(roots,[3])
        self.assertEqual((-3-1)*(-3+1),8)
        self.assertFalse(equation_candidate(-3))
        for bad in (Q(1),Q(-1),Q(0),Q(1,2)):
            self.assertFalse(equation_candidate(bad))

    def test_decreasing_base_inequality_by_powers(self):
        for n in range(-8,9):
            x=Q(1,2)**n
            self.assertEqual(n>2,0<x<Q(1,4))

    def test_contracts(self):
        for base,arg in ((0,1),(1,1),(-2,1),(2,0),(2,-1)):
            with self.assertRaises(ValueError):matches_integer_log(base,arg,0)
        for bad in (True,1.,'1',None):
            with self.assertRaises(ValueError):matches_integer_log(bad,2,1)
            with self.assertRaises(ValueError):matches_integer_log(2,bad,1)
            with self.assertRaises(ValueError):matches_integer_log(2,2,bad)
            with self.assertRaises(ValueError):equation_candidate(bad)

if __name__=='__main__':unittest.main()
