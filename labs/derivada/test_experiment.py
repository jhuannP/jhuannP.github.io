import unittest
from fractions import Fraction as Q
from .experiment import value, quotient, symmetric, tangent_square

class DerivativeTests(unittest.TestCase):
    def test_quadratic_expansion_and_exact_remainder(self):
        for a in range(-3,4):
            for h in (Q(1,2),Q(-1,2),Q(1,100),Q(-1,100)):
                self.assertEqual(quotient('quadrado',a,h),2*a+h)
                self.assertEqual(value('quadrado',a+h)-tangent_square(a,a+h),h*h)
                self.assertEqual(symmetric('quadrado',a,h),2*a)

    def test_cusp_refutes_symmetric_shortcut(self):
        for n in range(1,21):
            h=Q(1,n)
            self.assertEqual(quotient('canto',0,h),1)
            self.assertEqual(quotient('canto',0,-h),-1)
            self.assertEqual(symmetric('canto',0,h),0)
            self.assertEqual(quotient('salto',0,h),n)
            self.assertEqual(quotient('salto',0,-h),-n)

    def test_motion_units_reference(self):
        for t in range(6):
            for h in (Q(1,2),Q(-1,10)):
                self.assertEqual(quotient('movimento',t,h),6*t-2+3*h)
        self.assertEqual(quotient('movimento',2,Q(1,2)),Q(23,2))
        self.assertEqual(value('movimento',2),13)

    def test_contracts(self):
        for func in (quotient,symmetric):
            with self.assertRaises(ValueError):func('quadrado',0,0)
            with self.assertRaises(ValueError):func('quadrado',0,True)
            with self.assertRaises(ValueError):func('quadrado',0,.1)
        with self.assertRaises(ValueError):value('inexistente',0)

if __name__=='__main__':unittest.main()
