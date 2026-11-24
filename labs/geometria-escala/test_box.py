from fractions import Fraction as Q
from itertools import product,permutations
import unittest
from .box import box,scale

class BoxTests(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(box(2,3,4),dict(base_area=6,surface_area=52,volume=24))
        self.assertEqual(scale(2,3,4,2,2,2),dict(base_area=24,surface_area=208,volume=192))
        self.assertEqual(scale(2,3,4,2,1,1),dict(base_area=12,surface_area=80,volume=48))

    def test_unit_cube_oracle(self):
        neighbors=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
        for a,b,c in product(range(1,5),repeat=3):
            cubes=set(product(range(a),range(b),range(c)))
            exposed=sum((x+dx,y+dy,z+dz) not in cubes for x,y,z in cubes for dx,dy,dz in neighbors)
            actual=box(a,b,c)
            self.assertEqual(actual['volume'],len(cubes))
            self.assertEqual(actual['surface_area'],exposed)

    def test_similarity_and_unit_conversion(self):
        for a,b,c,k in product((Q(1,2),Q(2)),(Q(3,2),Q(3)),(Q(1),Q(4)),(Q(1,2),Q(2),Q(3,2))):
            original=box(a,b,c);scaled=scale(a,b,c,k,k,k)
            self.assertEqual(scaled['base_area'],original['base_area']*k*k)
            self.assertEqual(scaled['surface_area'],original['surface_area']*k*k)
            self.assertEqual(scaled['volume'],original['volume']*k**3)
        m=box(2,3,4);cm=box(200,300,400)
        self.assertEqual(cm['surface_area'],m['surface_area']*10000)
        self.assertEqual(cm['volume'],m['volume']*1000000)

    def test_permuting_dimensions_preserves_surface_and_volume(self):
        for p in permutations((2,3,4)):
            s=box(*p);self.assertEqual(s['surface_area'],52);self.assertEqual(s['volume'],24)
        self.assertNotEqual(box(2,3,4)['base_area'],box(4,3,2)['base_area'])

    def test_contracts(self):
        for i in range(3):
            for bad in (0,-1,True,1.,'1',None):
                args=[2,3,4];args[i]=bad
                with self.assertRaises(ValueError):box(*args)
        for bad in (0,-1,True,1.,'1',None):
            with self.assertRaises(ValueError):scale(2,3,4,bad,1,1)

if __name__=='__main__':unittest.main()
