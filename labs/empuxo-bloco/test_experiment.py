from fractions import Fraction as F
import unittest
from .experiment import inspect

class BuoyancyBlockTests(unittest.TestCase):
    def test_pressure_difference_on_prism(self):
        # A=0.01m², height=0.1m. Pressure forces on horizontal faces, not volume formula.
        area=F(1,100);height=F(1,10);p0=100000
        for rho in range(200,1401,100):
            for f in range(0,101,5):
                submerged_height=height*F(f,100)
                pbottom=p0+1000*10*submerged_height
                expected=(pbottom-p0)*area
                s=inspect(rho,f)
                self.assertEqual(s['buoyancy'],expected)
                self.assertEqual(s['net'],expected-F(rho,100))
                self.assertEqual(s['volume'],area*submerged_height)
        for depth in [0,1,3]:
            top=p0+1000*10*depth;bottom=p0+1000*10*(depth+height)
            self.assertEqual((bottom-top)*area,10)

    def test_equilibrium_and_current_position(self):
        self.assertTrue(inspect(400,40)['balanced'])
        self.assertGreater(inspect(400,100)['net'],0)
        self.assertLess(inspect(400,0)['net'],0)
        for rho in range(200,1001,100):
            s=inspect(rho,rho//10)
            self.assertTrue(s['balanced'])
            self.assertEqual(s['equilibrium_fraction'],F(rho,1000))
        self.assertEqual(inspect(1000,100)['regime'],'neutro')

    def test_heavy_body_and_bounds(self):
        for rho in range(1001,1401):
            s=inspect(rho,100)
            self.assertIsNone(s['equilibrium_fraction'])
            self.assertLess(s['net'],0)
        self.assertEqual(inspect(1200,100)['net'],-2)
        self.assertEqual(inspect(400,40)['mass'],F(2,5))
        self.assertEqual(inspect(400,40)['volume'],F(1,2500))

    def test_contracts(self):
        for rho in [True,199,1401,400.0,None]:
            with self.assertRaises(ValueError):inspect(rho,40)
        for f in [False,-1,101,.4,None]:
            with self.assertRaises(ValueError):inspect(400,f)
