import unittest
from fractions import Fraction as Q
from decimal import Decimal, localcontext
from .grid import between,sqrt2_bracket

class DensityTests(unittest.TestCase):
    def test_examples_and_floor(self):
        self.assertEqual(between(Q(-7,5),Q(-13,10)),(11,-15,Q(-15,11)))
        self.assertEqual(between(0,1),(2,1,Q(1,2)))
        self.assertEqual(sqrt2_bracket(3),(Q(707,500),Q(283,200)))
        self.assertEqual(int(Q(-77,5)),-15) # truncamento falha como piso
        self.assertEqual(Q(-77,5).numerator//Q(-77,5).denominator,-16)

    def test_intervals_and_affine_symmetry(self):
        for i in range(-20,21):
            for width in range(1,21):
                a=Q(i,7);b=a+Q(width,70);n,m,r=between(a,b)
                self.assertLess(a,r);self.assertLess(r,b)
                self.assertGreater(n*(b-a),1)
                self.assertLessEqual(Q(m-1,n),a)
                # Inteiro deslocado mantém a mesma grade e desloca o resultado.
                self.assertEqual(between(a+3,b+3),(n,m+3*n,r+3))
                self.assertTrue(-b < -r < -a)

    def test_nested_brackets_independent_decimal(self):
        with localcontext() as ctx:
            ctx.prec=40;root=Decimal(2).sqrt();last=(Q(1),Q(2))
            for k in range(13):
                lo,hi=sqrt2_bracket(k)
                self.assertEqual(hi-lo,Q(1,10**k))
                self.assertLess(lo*lo,2);self.assertGreater(hi*hi,2)
                self.assertLessEqual(last[0],lo);self.assertGreaterEqual(last[1],hi)
                self.assertLess(Decimal(lo.numerator)/Decimal(lo.denominator),root)
                self.assertGreater(Decimal(hi.numerator)/Decimal(hi.denominator),root)
                last=lo,hi

    def test_contracts(self):
        for a,b in ((0,0),(2,1),(True,2),(0.1,1),('0',1),(0,Q(1,10**7))):
            with self.assertRaises(ValueError): between(a,b)
        for k in (-1,13,True,2.0):
            with self.assertRaises(ValueError):sqrt2_bracket(k)
