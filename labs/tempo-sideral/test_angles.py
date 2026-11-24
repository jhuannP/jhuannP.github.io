import cmath
import importlib
from fractions import Fraction as Q
from itertools import product
from math import isclose,pi
import unittest
from .angles import wrap24,hours_to_degrees,local_sidereal_hours,hour_angle_hours

class SiderealAngleTests(unittest.TestCase):
    def test_longitude_and_crossing_zero(self):
        self.assertEqual(local_sidereal_hours(22,30),0)
        self.assertEqual(hour_angle_hours(0,Q(47,2)),Q(1,2))
        self.assertEqual(hours_to_degrees(Q(1,2)),Q(15,2))
        self.assertEqual(local_sidereal_hours(2,-45),23)
        self.assertEqual(hour_angle_hours(23,1),-2)
        self.assertEqual(hours_to_degrees(-2),-30)

    def test_units_wrap_and_antimeridian(self):
        self.assertEqual(hours_to_degrees(24),360)
        self.assertEqual(wrap24(-Q(1,2)),Q(47,2))
        self.assertEqual(wrap24(48),0)
        self.assertEqual(hour_angle_hours(12,0),-12)
        self.assertEqual(hour_angle_hours(0,12),-12)
        self.assertEqual(local_sidereal_hours(4,180),local_sidereal_hours(4,-180))

    def test_complex_phase_reference_on_grid(self):
        hours=(Q(0),Q(6),Q(12),Q(18),Q(47,2))
        for gst,ra,lon in product(hours,hours,(-180,-45,0,30,180)):
            lst=local_sidereal_hours(gst,lon);H=hour_angle_hours(lst,ra)
            self.assertTrue(0<=lst<24 and -12<=H<12)
            # Compose three unit-circle phases independently of branch choice.
            expected=cmath.exp(2j*pi*float(gst)/24)*cmath.exp(1j*pi*lon/180)/cmath.exp(2j*pi*float(ra)/24)
            actual=cmath.exp(2j*pi*float(H)/24)
            self.assertLess(abs(actual-expected),1e-13)
            self.assertEqual(wrap24(lst-H),ra)

    def test_connection_to_geometric_coordinates(self):
        horizontal=importlib.import_module('labs.coordenadas-celestes.horizontal').to_horizontal
        for gst,lon,ra,expected_az in ((0,-90,0,90),(6,0,0,270),(22,30,0,0)):
            lst=local_sidereal_hours(gst,lon);H=hours_to_degrees(hour_angle_hours(lst,ra))
            result=horizontal(-30,0,float(H))
            self.assertTrue(isclose(result['azimuth_deg'],expected_az,abs_tol=1e-10))
        self.assertTrue(isclose(horizontal(-30,0,0)['altitude_deg'],60,abs_tol=1e-10))

    def test_contracts(self):
        for bad in (True,1.0,'1',None,float('nan')):
            with self.assertRaises(ValueError):wrap24(bad)
            with self.assertRaises(ValueError):hours_to_degrees(bad)
            with self.assertRaises(ValueError):local_sidereal_hours(bad,0)
            with self.assertRaises(ValueError):local_sidereal_hours(0,bad)
            with self.assertRaises(ValueError):hour_angle_hours(bad,0)
            with self.assertRaises(ValueError):hour_angle_hours(0,bad)
        for bad in (-1,24,25):
            with self.assertRaises(ValueError):local_sidereal_hours(bad,0)
            with self.assertRaises(ValueError):hour_angle_hours(0,bad)
        for lon in (-181,181):
            with self.assertRaises(ValueError):local_sidereal_hours(0,lon)
