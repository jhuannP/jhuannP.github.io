import unittest
from fractions import Fraction as Q
from .slices import section,riemann,exact_volume_factor

class VolumeTests(unittest.TestCase):
    def test_geometry_for_three_axes(self):
        for k in range(33):
            x=Q(k,16)
            r0,r1,area=section(x,0)
            self.assertEqual(area,abs(4-4*x))
            self.assertGreaterEqual(r0,r1);self.assertGreaterEqual(r1,0)
            outer,inner,area=section(x,1)
            self.assertEqual(inner,0);self.assertEqual(outer,abs(1-x))
            self.assertEqual(area,(1-x)**2)
            self.assertEqual(section(x,3)[2],8*abs(1-x))
        self.assertEqual(section(Q(1,2),0),(Q(3,2),Q(1,2),Q(2)))

    def test_integrals_by_independent_simpson(self):
        # Simpson exato aqui, áreas polinomiais de grau <=2 em cada metade.
        def integrate(a,b,axis):
            f=lambda x:section(x,axis)[2]
            return (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6
        for axis in (0,1,3):
            first=integrate(Q(0),Q(1),axis)
            second=integrate(Q(1),Q(2),axis)
            self.assertEqual(first,exact_volume_factor(axis))
            self.assertEqual(first+second,exact_volume_factor(axis,2))
        self.assertEqual(exact_volume_factor(0),2)
        self.assertEqual(exact_volume_factor(1),Q(1,3))
        self.assertEqual(exact_volume_factor(3),4)

    def test_riemann_bounds_and_midpoint(self):
        for n in [1,2,3,4,8,16,32,64]:
            for axis in (0,1,3):
                lo=riemann(n,'right',axis);hi=riemann(n,'left',axis)
                target=exact_volume_factor(axis)
                self.assertLessEqual(lo,target);self.assertLessEqual(target,hi)
                gap={0:Q(4),1:Q(1),3:Q(8)}[axis]/n
                self.assertEqual(hi-lo,gap)
                mid=riemann(n,'mid',axis)
                self.assertEqual(target-mid,Q(1,12*n*n) if axis==1 else Q(0))

    def test_counterexamples_and_symmetry(self):
        # Espessura quadrada: integral de (2−2x)^2 =4/3, não volume/pi=2.
        self.assertNotEqual(Q(4,3),exact_volume_factor())
        # Fórmula assinada sem trocar raios em [0,2] daria zero.
        self.assertNotEqual(0,exact_volume_factor(0,2))
        for i in range(17):
            x=Q(i,8)
            for axis in (0,1,3):self.assertEqual(section(x,axis),section(2-x,axis))
        self.assertEqual(section(1,0)[2],0)
        self.assertEqual(section(Q(1,2),1)[2],Q(1,4))

    def test_contracts(self):
        for x in [-1,Q(21,10)]:
            with self.assertRaises(ValueError):section(x)
        for x in [True,.5,'1']:
            with self.assertRaises(TypeError):section(x)
        for n in [0,-1,True,1.5,4097]:
            with self.assertRaises(ValueError):riemann(n)
        with self.assertRaises(ValueError):section(0,2)
        with self.assertRaises(ValueError):riemann(2,'invalid')
        with self.assertRaises(ValueError):exact_volume_factor(stop=3)

if __name__=='__main__':unittest.main()
