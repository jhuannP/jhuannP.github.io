import unittest
from fractions import Fraction as Q
from math import pi,log
from cmath import exp
from .branches import principal_angle,product_defect,spiral_integral

class Tests(unittest.TestCase):
    def test_wrap_and_cuts(self):
        for n in range(-32,33):
            q=Q(n,4)
            if q.denominator==1 and q.numerator%2:
                with self.assertRaises(ValueError):principal_angle(q)
            else:
                w=principal_angle(q)
                self.assertTrue(-1<w<1)
                self.assertEqual((q-w)%2,0)
                self.assertAlmostEqual(abs(exp(1j*pi*float(q))-exp(1j*pi*float(w))),0,places=13)
        self.assertEqual(principal_angle(Q(3,2)),Q(-1,2))
    def test_product(self):
        self.assertEqual(product_defect(Q(3,4),Q(3,4)),1)
        self.assertEqual(product_defect(Q(-3,4),Q(-3,4)),-1)
        self.assertEqual(product_defect(Q(1,4),Q(1,4)),0)
        for a in (Q(-3,4),Q(-1,4),Q(1,4),Q(3,4)):
            for b in (Q(-2,3),Q(0),Q(2,3)):
                k=product_defect(a,b)
                self.assertIn(k,(-1,0,1))
                self.assertEqual(principal_angle(a)+principal_angle(b)-principal_angle(a+b),2*k)
        with self.assertRaises(ValueError):product_defect(Q(1,2),Q(1,2))
    def test_paths_independent_differences(self):
        # Reconstituir integral por incrementos log(r1/r0)+i*dtheta não envolvidos.
        for q in (Q(3,4),Q(-5,4),Q(2),Q(-4)):
            real,imag_pi=spiral_integral(1,2,q)
            self.assertAlmostEqual(real,log(2),places=14)
            for n in (64,256):
                # Quadratura de dz/z por diferenças centrais em parametrização float.
                dt=1/n;eps=1e-6;total=0j
                for j in range(n):
                    t=(j+.5)*dt
                    z=lambda s:exp((log(2)+1j*pi*float(q))*s)
                    total+=(z(t+eps)-z(t-eps))/(2*eps*z(t))*dt
                self.assertAlmostEqual(total.real,real,places=8)
                self.assertAlmostEqual(total.imag,pi*float(imag_pi),places=8)
        top=spiral_integral(1,2,Q(3,4));bottom=spiral_integral(1,2,Q(-5,4))
        self.assertEqual(top[1]-bottom[1],2)
        self.assertAlmostEqual(abs(exp((log(2)+.75j*pi))-exp(log(2)-1.25j*pi)),0,places=14)
    def test_contracts(self):
        for bad in (True,1.,'1',Q(9)):
            with self.assertRaises(ValueError):principal_angle(bad)
        for bad in (0,-1,True,17,1.):
            with self.assertRaises(ValueError):spiral_integral(bad,2,0)
        with self.assertRaises(ValueError):spiral_integral(1,2,9)
