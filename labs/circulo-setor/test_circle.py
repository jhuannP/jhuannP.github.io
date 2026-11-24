import unittest
from fractions import Fraction as Q
from math import pi
from .circle import sector,annulus_area_pi,polygon_bounds

class Tests(unittest.TestCase):
    def test_fixture_and_boundary(self):
        r=sector(6,Q(1,3))
        self.assertEqual(r,{'area_pi':12,'arc_pi':4,'perimeter_plain':12})
        full=sector(6,1)
        self.assertEqual(full,{'area_pi':36,'arc_pi':12,'perimeter_plain':0})
        self.assertEqual(annulus_area_pi(5,3),16)
        self.assertNotEqual(annulus_area_pi(5,3),(5-3)**2)
    def test_partition_and_scale(self):
        for r in (Q(1,2),Q(2),Q(7,3)):
            for n in (2,3,4,7):
                part=sector(r,Q(1,n));full=sector(r,1)
                self.assertEqual(n*part['area_pi'],full['area_pi'])
                self.assertEqual(n*part['arc_pi'],full['arc_pi'])
                self.assertGreater(n*part['perimeter_plain'],full['perimeter_plain'])
            for k in (2,3):
                a=sector(r,Q(2,5));b=sector(k*r,Q(2,5))
                self.assertEqual(b['area_pi'],k*k*a['area_pi'])
                self.assertEqual(b['arc_pi'],k*a['arc_pi'])
        self.assertEqual(annulus_area_pi(7,5)+annulus_area_pi(5,2),annulus_area_pi(7,2))
    def test_polygon_containment_and_refinement(self):
        for r in (Q(1,2),Q(1),Q(3)):
            previous=(0,float('inf'))
            for n in (3,4,8,16,32,64,128,256):
                inside,outside=polygon_bounds(r,n);area=pi*float(r*r)
                self.assertLess(inside,area)
                self.assertGreater(outside,area)
                self.assertGreater(inside,previous[0]);self.assertLess(outside,previous[1])
                previous=(inside,outside)
            self.assertLess((outside-inside)/area,.001)
    def test_contracts(self):
        for bad in (True,6.,0,-1,1001):
            with self.assertRaises(ValueError):sector(bad,Q(1,3))
        for bad in (0,-1,Q(3,2),True,.5):
            with self.assertRaises(ValueError):sector(6,bad)
        for bad in (3,4,-1):
            with self.assertRaises(ValueError):annulus_area_pi(3,bad)
        for bad in (True,2,257,4.):
            with self.assertRaises(ValueError):polygon_bounds(1,bad)
