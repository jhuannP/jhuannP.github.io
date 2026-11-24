import unittest
from itertools import product
from math import asin,atan2,cos,degrees,hypot,isclose,radians,sin
from .horizontal import to_horizontal

class CoordinateTests(unittest.TestCase):
    def test_meridian_and_cardinal_cases(self):
        r=to_horizontal(-30,0,0)
        self.assertAlmostEqual(r['altitude_deg'],60,places=12)
        self.assertAlmostEqual(r['azimuth_deg'],0,places=12)
        for H,az in ((-90,90),(90,270)):
            r=to_horizontal(-30,0,H)
            self.assertAlmostEqual(r['altitude_deg'],0,places=12)
            self.assertAlmostEqual(r['azimuth_deg'],az,places=12)
        r=to_horizontal(-30,0,180)
        self.assertAlmostEqual(r['altitude_deg'],-60,places=12)
        self.assertAlmostEqual(r['azimuth_deg'],180,places=12)

    def test_norm_altitude_formula_and_inverse_on_grid(self):
        for lat,dec,H in product((-60,-30,0,30,60),(-60,-30,0,30,60),(-180,-90,-30,0,30,90,180)):
            r=to_horizontal(lat,dec,H);phi,delta,h=map(radians,(lat,dec,H))
            self.assertTrue(isclose(r['east']**2+r['north']**2+r['up']**2,1,rel_tol=1e-13))
            expected=sin(phi)*sin(delta)+cos(phi)*cos(delta)*cos(h)
            self.assertAlmostEqual(r['up'],expected,places=13)
            if abs(expected)<1-1e-12:self.assertAlmostEqual(r['altitude_deg'],degrees(asin(expected)),places=11)
            # Inverse change of basis, independently reconstructing hour angle and declination.
            a=-sin(phi)*r['north']+cos(phi)*r['up'];b=r['east'];c=cos(phi)*r['north']+sin(phi)*r['up']
            recovered_dec=degrees(atan2(c,hypot(a,b)))
            recovered_H=degrees(atan2(-b,a))
            self.assertAlmostEqual(recovered_dec,dec,places=11)
            difference=(recovered_H-H+180)%360-180
            self.assertAlmostEqual(difference,0,places=11)

    def test_zenith_nadir_and_numerical_azimuth_policy(self):
        self.assertIsNone(to_horizontal(-30,-30,0)['azimuth_deg'])
        self.assertIsNone(to_horizontal(0,0,180)['azimuth_deg'])
        self.assertAlmostEqual(to_horizontal(-30,-30,0)['altitude_deg'],90,places=12)
        self.assertAlmostEqual(to_horizontal(0,0,180)['altitude_deg'],-90,places=12)
        # Near-singular value omitted by explicit numerical convention, not exact geometry.
        self.assertIsNone(to_horizontal(0,0,1e-12)['azimuth_deg'])
        self.assertIsNotNone(to_horizontal(0,0,1e-6)['azimuth_deg'])

    def test_celestial_poles_and_hour_angle_symmetry(self):
        for H in (-180,-90,0,90,180):
            r=to_horizontal(-30,-90,H)
            self.assertAlmostEqual(r['altitude_deg'],30,places=12)
            self.assertAlmostEqual(r['azimuth_deg'],180,places=12)
        for H in (15,45,90,135):
            a=to_horizontal(-30,20,H);b=to_horizontal(-30,20,-H)
            self.assertAlmostEqual(a['altitude_deg'],b['altitude_deg'],places=12)
            self.assertAlmostEqual(a['east'],-b['east'],places=12)
            self.assertAlmostEqual(a['north'],b['north'],places=12)

    def test_contracts(self):
        for value in (True,'0',None,float('nan'),float('inf'),10**400):
            for index in range(3):
                args=[-30,0,0];args[index]=value
                with self.assertRaises(ValueError):to_horizontal(*args)
        for args in ((-90,0,0),(90,0,0),(0,-91,0),(0,91,0),(0,0,-181),(0,0,181)):
            with self.assertRaises(ValueError):to_horizontal(*args)
