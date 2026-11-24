import math
import unittest
from fractions import Fraction as F
from .angular import fraction, isotropic_fraction, relative_power

class AngularTests(unittest.TestCase):
    def test_examples_and_full_sphere(self):
        self.assertEqual(fraction(-1,1),1)
        self.assertEqual(fraction(0,1),F(1,2))
        self.assertEqual(fraction(F(1,2),1),F(5,32))
        self.assertEqual(fraction(F(-1,2),F(1,2)),F(11,16))
        self.assertEqual(isotropic_fraction(F(1,2),1),F(1,4))
        self.assertEqual(fraction(1,1),0)

    def test_partitions_reflection_and_order(self):
        # 231 intervals; partition sums and north/south reflection.
        points=[F(i,10) for i in range(-10,11)]
        for i, a in enumerate(points):
            for b in points[i:]:
                v=fraction(a,b)
                self.assertEqual(v,fraction(-b,-a))
                self.assertGreaterEqual(v,0);self.assertLessEqual(v,1)
                mid=(a+b)/2
                self.assertEqual(v,fraction(a,mid)+fraction(mid,b))
        self.assertEqual(sum(fraction(a,b) for a,b in zip(points,points[1:])),1)

    def test_independent_theta_quadrature_and_scaling(self):
        # Independent theta-space integration includes sin(theta) area factor.
        for low, high in [(0,math.pi/3),(math.pi/3,2*math.pi/3),(0,math.pi)]:
            n=10000;step=(high-low)/n
            value=math.fsum(.75*math.sin(low+(i+.5)*step)**3*step for i in range(n))
            expected=F(5,32) if low==0 and high<math.pi else F(11,16) if low>0 else F(1)
            self.assertAlmostEqual(value,float(expected),delta=1e-8)
        self.assertEqual(relative_power(2,1),4)
        self.assertEqual(relative_power(1,2),16)
        self.assertEqual(relative_power(F(1,2),2),4)
        for a in (F(1,2),F(1),F(3)):
            for w in (F(1,2),F(1),F(2)):
                self.assertEqual(relative_power(a,w)*relative_power(1/a,1/w),1)

    def test_contracts(self):
        for args in [(True,1),(0,.5),('0',1)]:
            with self.assertRaises(TypeError): fraction(*args)
        for args in [(-2,0),(0,2),(1,-1)]:
            with self.assertRaises(ValueError): fraction(*args)
        for args in [(-1,1),(1,0),(1,-1)]:
            with self.assertRaises(ValueError): relative_power(*args)
        self.assertEqual(relative_power(0,1),0)

if __name__=='__main__': unittest.main()
