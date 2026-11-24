import math
import unittest
from .principal import inverse,direction_angle

class PrincipalTests(unittest.TestCase):
    def test_inverse_composition_and_branches(self):
        for i in range(-20,21):
            x=i/20
            a=inverse('asin',x);c=inverse('acos',x)
            self.assertTrue(-math.pi/2<=a<=math.pi/2)
            self.assertTrue(0<=c<=math.pi)
            self.assertAlmostEqual(math.sin(a),x,places=14)
            self.assertAlmostEqual(math.cos(c),x,places=14)
        for x in (-100,-3,-1,0,1,3,100):
            self.assertAlmostEqual(math.tan(inverse('atan',x)),x,places=10)
        self.assertAlmostEqual(inverse('asin',math.sin(5*math.pi/6)),math.pi/6)
        self.assertAlmostEqual(inverse('atan',math.tan(3*math.pi/4)),-math.pi/4)

    def test_four_quadrants_against_normalized_coordinates(self):
        for x in range(-4,5):
            for y in range(-4,5):
                if not (x or y):continue
                a=direction_angle(x,y);r=math.hypot(x,y)
                self.assertTrue(-math.pi<=a<math.pi)
                self.assertAlmostEqual(math.cos(a),x/r,places=14)
                self.assertAlmostEqual(math.sin(a),y/r,places=14)
                self.assertAlmostEqual(direction_angle(7*x,7*y),a,places=14)
        self.assertAlmostEqual(direction_angle(-1,1)-inverse('atan',-1),math.pi)

    def test_axes_signed_zero_and_branch_cut(self):
        for x,y,expected in ((1,0,0),(0,1,math.pi/2),(-1,0,-math.pi),(0,-1,-math.pi/2),(-1,-0.,-math.pi)):
            self.assertEqual(direction_angle(x,y),expected)
        self.assertGreater(direction_angle(-1,1e-6),0)
        self.assertLess(direction_angle(-1,-1e-6),0)
        self.assertEqual(math.copysign(1,direction_angle(1,-0.)),1)
        with self.assertRaises(ValueError):direction_angle(0,-0.)

    def test_strict_domain_endpoints_and_rounding(self):
        for kind in ('asin','acos'):
            for x in (-1,1):self.assertTrue(math.isfinite(inverse(kind,x)))
            for x in (math.nextafter(1,math.inf),math.nextafter(-1,-math.inf)):
                with self.assertRaises(ValueError):inverse(kind,x)
        # A finite float can round atan's mathematically open endpoint to pi/2.
        self.assertEqual(inverse('atan',1e300),math.pi/2)

    def test_contracts(self):
        for bad in (True,'0',None,math.inf,math.nan,10**1000):
            with self.assertRaises(ValueError):inverse('atan',bad)
            with self.assertRaises(ValueError):direction_angle(bad,1)
            with self.assertRaises(ValueError):direction_angle(1,bad)
        with self.assertRaises(ValueError):inverse('sin',0)

if __name__=='__main__':unittest.main()
