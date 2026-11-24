import unittest
from fractions import Fraction as Q
from math import isclose, pi
from .experiment import summary,geometric_distance_au

class ParallaxTests(unittest.TestCase):
    def test_independent_rational_endpoints(self):
        for p in (Q(1,5),Q(1),Q(8),Q(10),Q(20)):
            for s in (Q(0),p/10,p/2,p,2*p):
                q=summary(float(p),float(s))
                self.assertTrue(isclose(q['distance'],float(Q(1000)/p),rel_tol=1e-13))
                self.assertTrue(isclose(q['lower'],float(Q(1000)/(p+s)),rel_tol=1e-13))
                if s<p:
                    self.assertTrue(isclose(q['upper'],float(Q(1000)/(p-s)),rel_tol=1e-13))
                    self.assertLessEqual(q['lower'],q['distance']);self.assertGreaterEqual(q['upper'],q['distance'])
                else:self.assertIsNone(q['upper'])
        q=summary(10,2);self.assertAlmostEqual(q['linear'],20);self.assertAlmostEqual(q['upper'],125)
        self.assertGreater(q['upper']-q['distance'],q['distance']-q['lower'])

    def test_units_and_geometry_independently(self):
        self.assertAlmostEqual(summary(1000,0)['distance'],1)
        self.assertAlmostEqual(summary(20,0)['distance'],50) # deslocamento total 40 mas => p=20 mas
        self.assertAlmostEqual(geometric_distance_au(162000),1)
        self.assertAlmostEqual(geometric_distance_au(108000),3**.5)
        self.assertLess(abs(geometric_distance_au(1)/(648000/pi)-1),1e-10)

    def test_local_derivative_and_scaling(self):
        for p in (.2,1,10,20):
            h=p*1e-5
            derivative=(summary(p+h,0)['distance']-summary(p-h,0)['distance'])/(2*h)
            self.assertTrue(isclose(derivative,-1000/p**2,rel_tol=2e-9))
            self.assertAlmostEqual(summary(2*p,0)['distance'],summary(p,0)['distance']/2)
            q=summary(p,p*.001)
            self.assertLess(abs((q['upper']-q['lower'])/(2*q['linear'])-1),2e-6)

    def test_domain_and_nonfinite_inputs(self):
        for p,s in ((0,1),(-1,1),(1,-1),(float('nan'),1),(1,float('inf'))):
            with self.assertRaises(ValueError):summary(p,s)
        for p in (0,-1,324000,float('nan'),float('inf')):
            with self.assertRaises(ValueError):geometric_distance_au(p)

if __name__=='__main__':unittest.main()
