import unittest,math
from .experiment import model

class NewmanTests(unittest.TestCase):
    def test_tetrahedral_bond_angles_and_rigid_rotation(self):
        dot=lambda a,b:sum(x*y for x,y in zip(a,b))
        for phi in range(0,361,10):
            s=model(phi)
            for vectors,axis in ((s['front'],(0,0,1)),(s['back'],(0,0,-1))):
                for u in vectors:
                    self.assertAlmostEqual(dot(u,u),1,places=14);self.assertAlmostEqual(dot(u,axis),-1/3,places=14)
                for i in range(3):
                    for j in range(i):self.assertAlmostEqual(dot(vectors[i],vectors[j]),-1/3,places=14)
            self.assertEqual(s['front'],model(0)['front'])
    def test_projection_matches_independent_rotation_matrix(self):
        for phi in range(0,361,15):
            s=model(phi);c=math.cos(math.radians(phi));t=math.sin(math.radians(phi))
            for initial,actual in zip(model(0)['back'],s['back']):
                x,y,z=initial;expected=(c*x-t*y,t*x+c*y,z)
                for a,b in zip(actual,expected):self.assertAlmostEqual(a,b,places=14)
            if phi<=240:
                shifted=model(phi+120)
                for j in range(3):
                    for a,b in zip(shifted['back'][j],s['back'][(j+1)%3]):self.assertAlmostEqual(a,b,places=14)
    def test_potential_extrema_periodicity_and_rad_derivative(self):
        for barrier in (0,3,12,18):
            for phi in range(361):
                s=model(phi,barrier);self.assertGreaterEqual(s['energy'],-1e-13);self.assertLessEqual(s['energy'],barrier+1e-13)
                if phi<=240:self.assertAlmostEqual(s['energy'],model(phi+120,barrier)['energy'],places=12)
            for phi in (0,120,240,360):self.assertEqual(model(phi,barrier)['kind'],'eclipsada');self.assertAlmostEqual(model(phi,barrier)['energy'],barrier)
            for phi in (60,180,300):self.assertEqual(model(phi,barrier)['kind'],'alternada');self.assertAlmostEqual(model(phi,barrier)['energy'],0)
            for phi in (15,45,90,200):
                h=1e-5;d=math.degrees(h)
                fd=(model(phi+d,barrier)['energy']-model(phi-d,barrier)['energy'])/(2*h)
                self.assertAlmostEqual(fd,model(phi,barrier)['derivative'],delta=5e-8)
    def test_domain_and_flat_profile(self):
        self.assertEqual(model(30,0)['energy'],0);self.assertEqual(model(30,0)['kind'],'intermediária')
        for args in ((-1,12),(361,12),(60,-1),(60,19),(float('nan'),12),(True,12)):
            with self.assertRaises(ValueError):model(*args)
