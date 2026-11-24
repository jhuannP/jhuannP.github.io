import unittest
from fractions import Fraction as Q
from .experiment import geometry

class CellGeometryTests(unittest.TestCase):
    def test_volume_conservation_and_surface_scaling(self):
        for r in (Q(1,2),1,2,5,10):
            for k in range(1,11):
                g=geometry(r,k)
                self.assertEqual(g['total_volume_pi'],g['volume_pi'])
                self.assertEqual(g['total_area_pi'],k*g['single_area_pi'])
                self.assertEqual(g['total_area_pi']/g['total_volume_pi'],g['total_ratio'])
                self.assertEqual(g['count']*g['small_radius']**3,Q(r)**3)

    def test_change_of_length_scale(self):
        for factor in (Q(1,10),2,10):
            a=geometry(2,3);b=geometry(2*factor,3)
            self.assertEqual(b['total_area_pi'],factor**2*a['total_area_pi'])
            self.assertEqual(b['total_volume_pi'],factor**3*a['total_volume_pi'])
            self.assertEqual(b['total_ratio'],a['total_ratio']/factor)

    def test_independent_known_spheres(self):
        q=geometry(2,2)
        self.assertEqual(q['count'],8);self.assertEqual(q['small_radius'],1)
        self.assertEqual(q['single_area_pi'],16);self.assertEqual(q['total_area_pi'],32)
        self.assertEqual(q['volume_pi'],Q(32,3));self.assertEqual(q['total_ratio'],3)
        self.assertEqual(geometry(4,1)['single_ratio'],Q(3,4))

    def test_contract(self):
        for radius in (0,-1,True,1.5,'2'):
            with self.assertRaises(ValueError):geometry(radius)
        for k in (0,-1,11,True,Q(1,2)):
            with self.assertRaises(ValueError):geometry(1,k)
