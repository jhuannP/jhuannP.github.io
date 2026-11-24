import unittest
from fractions import Fraction as F
from .experiment import rules,model

class QuadratureErrorTests(unittest.TestCase):
    def test_polynomial_exactness(self):
        for degree in range(4):
            for n in range(2,34,2):
                t,s=rules(lambda x:x**degree,n)
                self.assertEqual(s,F(1,degree+1))
                if degree<=1:self.assertEqual(t,F(1,degree+1))

    def test_quartic_error_identity_and_bounds(self):
        for n in range(2,66,2):
            t,s=rules(lambda x:x**4,n)
            et=F(1,3*n*n)-F(1,30*n**4)
            es=F(2,15*n**4)
            self.assertEqual(t-F(1,5),et)
            self.assertEqual(s-F(1,5),es)
            self.assertLessEqual(abs(et),F(1,n*n))
        for k in range(1,6):
            self.assertEqual(model(0,k)['es']/model(0,k+1)['es'],16)

    def test_corner_counterexample(self):
        integral=(F(3,10)**2+F(7,10)**2)/2
        self.assertEqual(integral,F(29,100))
        self.assertEqual(model(1,1)['es'],F(1,100))
        self.assertEqual(model(1,2)['es'],-F(1,150))
        for k in range(1,7):
            r=model(1,k);self.assertEqual(r['integral'],integral)
            self.assertIsNone(r['bound_t']);self.assertIsNone(r['bound_s'])

    def test_contract(self):
        for n in (True,0,-2,3,2.,None):
            with self.assertRaises(ValueError):rules(lambda x:x,n)
        with self.assertRaises(ValueError):rules(lambda x:.5,2)
        for family,level in ((True,2),(2,2),(0,True),(0,0),(0,7),(0,2.)):
            with self.assertRaises(ValueError):model(family,level)
