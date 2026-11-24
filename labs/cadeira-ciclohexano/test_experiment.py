import unittest,itertools,math
from .experiment import model

def sub(a,b):return [x-y for x,y in zip(a,b)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))

class ChairTests(unittest.TestCase):
    def test_closed_ring_and_tetrahedral_geometry(self):
        for chair in (0,1):
            m=model(chair)
            for i,p in enumerate(m['carbons']):
                bonds=[sub(m['carbons'][(i-1)%6],p),sub(m['carbons'][(i+1)%6],p),m['axial'][i],m['equatorial'][i]]
                for v in bonds:self.assertAlmostEqual(dot(v,v),1)
                for j,k in itertools.combinations(range(4),2):self.assertAlmostEqual(dot(bonds[j],bonds[k]),-1/3)
                self.assertTrue(all(abs(sum(v[k] for v in bonds))<1e-12 for k in range(3)))
    def test_face_preserved_and_type_swapped(self):
        for chair,site,up in itertools.product((0,1),range(1,7),(0,1)):
            a=model(chair,site,up);b=model(1-chair,site,up)
            self.assertEqual((a['site'],a['up']),(b['site'],b['up']))
            self.assertNotEqual(a['kind'],b['kind'])
            self.assertEqual(a['kind'],model(1-b['chair'],site,up)['kind'])
            self.assertEqual(a['direction'][2]>0,bool(up));self.assertEqual(b['direction'][2]>0,bool(up))
            self.assertAlmostEqual(abs(a['direction'][2]),1 if a['kind']=='axial' else 1/3)
    def test_axial_alternation_and_counts(self):
        self.assertEqual(model(0)['axial_up'],[1,3,5]);self.assertEqual(model(1)['axial_up'],[2,4,6])
        for chair in (0,1):
            a=model(chair)
            self.assertEqual(sum(v[2]>0 for v in a['axial']),3)
            self.assertEqual(sum(v[2]>0 for v in a['equatorial']),3)
            for i in range(6):self.assertLess(a['axial'][i][2]*a['equatorial'][i][2],0)
    def test_contract(self):
        for args in [(2,1,1),(0,0,1),(0,7,1),(0,1,2),(True,1,1),(0,1,False),(0,1.0,1)]:
            with self.assertRaises(ValueError):model(*args)
