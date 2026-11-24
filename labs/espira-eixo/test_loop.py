import unittest
from math import sqrt
from fractions import Fraction as F
from .loop import profile,integrate_axis,dipole_profile

class LoopTests(unittest.TestCase):
    def test_exact_geometric_references(self):
        self.assertEqual(profile(0),1)
        self.assertAlmostEqual(profile(.75),float(F(64,125)),places=14)
        self.assertAlmostEqual(profile(1),1/(2*sqrt(2)),places=14)
        # a=4,z=3 => distance=5; B/B0=(4/5)^3.
        self.assertEqual(F(4,5)**3,F(64,125))

    def test_vector_sum_and_symmetry(self):
        for u in (-10.,-3.,-.75,0.,.75,3.,10.):
            for n in (4,5,8,31,64):
                bx,by,bz=integrate_axis(u,n)
                self.assertAlmostEqual(bx,0,places=14)
                self.assertAlmostEqual(by,0,places=14)
                self.assertAlmostEqual(bz,profile(u),places=14)
            self.assertEqual(profile(u),profile(-u))
        self.assertTrue(all(profile(i/10)>profile((i+1)/10) for i in range(40)))

    def test_far_field_error(self):
        errors=[dipole_profile(u)/profile(u)-1 for u in (2.,5.,10.,20.)]
        self.assertTrue(all(x>y>0 for x,y in zip(errors,errors[1:])))
        self.assertAlmostEqual(errors[2],(1+.01)**1.5-1,places=14)
        self.assertLess(errors[2],.016)

    def test_contracts(self):
        for u in (True,'0',float('nan'),float('inf'),1001):
            with self.assertRaises(ValueError):profile(u)
        for n in (True,3,4097,8.):
            with self.assertRaises(ValueError):integrate_axis(1,n)
        with self.assertRaises(ValueError):dipole_profile(0)

if __name__=='__main__':unittest.main()
