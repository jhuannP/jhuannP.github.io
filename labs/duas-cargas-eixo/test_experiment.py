import unittest
from fractions import Fraction as F
from .experiment import axial

class TwoChargeTests(unittest.TestCase):
    def test_gradient_independent_route(self):
        h=F(1,100000)
        for s in (-1,1):
            for x in (F(-3),F(-2),F(-1,2),F(0),F(1,2),F(2),F(3)):
                derivative=-(axial(x+h,s)['potential']-axial(x-h,s)['potential'])/(2*h)
                self.assertLess(abs(float(derivative-axial(x,s)['field'])),1e-6)

    def test_parities_and_middle(self):
        for x in (F(0),F(1,4),F(1,2),F(2),F(3)):
            for s in (-1,1):
                a,b=axial(x,s),axial(-x,s)
                self.assertEqual(a['field'],(-1 if s==1 else 1)*b['field'])
                self.assertEqual(a['potential'],(1 if s==1 else -1)*b['potential'])
        self.assertEqual((axial(0,1)['field'],axial(0,1)['potential']),(0,18))
        self.assertEqual((axial(0,-1)['field'],axial(0,-1)['potential']),(18,0))
        self.assertEqual((axial(2,-1)['field'],axial(2,-1)['potential']),(-8,-6))

    def test_work_integral_avoids_sources(self):
        n=2048
        for s in (-1,1):
            for a,b in ((F(-3),F(-2)),(F(-1,2),F(1,2)),(F(2),F(3))):
                h=(b-a)/n
                integral=float(h)/3*sum((1 if j in (0,n) else 4 if j%2 else 2)*float(axial(a+j*h,s)['field']) for j in range(n+1))
                difference=float(axial(a,s)['potential']-axial(b,s)['potential'])
                self.assertAlmostEqual(integral,difference,places=9)

    def test_singularities_and_contract(self):
        for x in (-1,1):
            for s in (-1,1):
                r=axial(x,s);self.assertTrue(r['singular']);self.assertIsNone(r['field']);self.assertIsNone(r['potential'])
                self.assertEqual(sum(v is None for v in r['fields']),1)
        for x in (True,None,.5,'0'):
            with self.assertRaises(ValueError):axial(x)
        for s in (True,None,0,2,-1.):
            with self.assertRaises(ValueError):axial(0,s)
