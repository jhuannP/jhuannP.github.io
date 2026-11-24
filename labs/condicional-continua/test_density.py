from fractions import Fraction as Q
import unittest
from .density import joint,marginal_x,rectangle,point_interval,band_interval

def simpson(f,a,b,n=20):
    # Quadratura separada das primitivas usadas no módulo; graus <=2.
    h=(b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))

class DensityTests(unittest.TestCase):
    def test_rectangle_against_independent_quadrature(self):
        grid=[Q(i,4) for i in range(5)]
        intervals=[(a,b) for a in grid for b in grid if a<=b]
        for a,b in intervals:
            for c,d in intervals:
                numeric=simpson(lambda x:simpson(lambda y:float(joint(Q(x),Q(y))),float(c),float(d)),float(a),float(b))
                self.assertAlmostEqual(float(rectangle(a,b,c,d)),numeric,places=12)
        self.assertEqual(rectangle(0,1,0,1),1)
        self.assertEqual(rectangle(Q(1,2),Q(1,2),0,1),0)

    def test_normalization_partitions_and_total_probability(self):
        for i in range(11):
            x=Q(i,10)
            self.assertEqual(point_interval(x,0,1),1)
            self.assertAlmostEqual(float(marginal_x(x)),simpson(lambda y:float(joint(x,Q(y))),0,1),places=12)
            for j in range(11):
                t=Q(j,10)
                self.assertEqual(point_interval(x,0,t)+point_interval(x,t,1),1)
                total=simpson(lambda z:float(point_interval(Q(z),t,1)*marginal_x(Q(z))),0,1)
                self.assertAlmostEqual(total,float(rectangle(0,1,t,1)),places=12)
        for split in (Q(1,4),Q(1,2),Q(3,4)):
            total=sum(rectangle(a,b,0,1)*band_interval(a,b,Q(1,2),1) for a,b in ((0,split),(split,1)))
            self.assertEqual(total,Q(13,20))

    def test_bands_limit_and_error_identity(self):
        target=Q(2,3);previous=Q(1)
        for k in range(1,12):
            h=Q(1,2**k)
            actual=band_interval(Q(1,2)-h,Q(1,2)+h,Q(1,2),1)
            self.assertEqual(actual,(Q(1,2)+h*h/6)/(Q(3,4)+h*h/3))
            error=target-actual
            self.assertEqual(error,(h*h/18)/(Q(3,4)+h*h/3))
            self.assertGreater(error,0);self.assertLess(error,previous);previous=error
        self.assertEqual(band_interval(0,1,Q(1,2),1),Q(13,20))
        self.assertEqual(band_interval(Q(1,4),Q(3,4),Q(1,2),1),Q(49,74))
        self.assertEqual(band_interval(Q(3,8),Q(5,8),Q(1,2),1),Q(193,290))

    def test_density_not_mass_and_dependence(self):
        self.assertEqual(joint(1,1),Q(12,5))
        self.assertEqual(point_interval(Q(1,2),Q(1,2),1),Q(2,3))
        self.assertEqual(point_interval(0,Q(1,2),1),Q(3,4))
        self.assertEqual(point_interval(1,Q(1,2),1),Q(7,12))
        self.assertEqual(point_interval(Q(1,2),Q(1,2),Q(1,2)),0)
        self.assertEqual(rectangle(0,1,Q(1,2),1),Q(13,20))
        self.assertIsNone(band_interval(Q(1,2),Q(1,2),0,1))

    def test_contracts_and_outside_support(self):
        self.assertEqual(joint(-1,0),0);self.assertEqual(joint(0,2),0)
        self.assertEqual(marginal_x(2),0)
        for bad in (.5,True,'1/2',None):
            with self.assertRaises(TypeError):point_interval(bad,0,1)
        for args in ((-1,0,1),(2,0,1),(0,Q(3,4),Q(1,4))):
            with self.assertRaises(ValueError):point_interval(*args)
        for args in ((1,0,0,1),(0,1,-1,1)):
            with self.assertRaises(ValueError):rectangle(*args)

if __name__=='__main__':unittest.main()
