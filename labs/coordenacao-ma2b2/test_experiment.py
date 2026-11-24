import unittest
from itertools import combinations
from .experiment import POINTS,PAIRS,apply,determinant,model,orbit,rotations

class CoordinationGeometry(unittest.TestCase):
    def test_spatial_groups_and_composition(self):
        for g,n in [(0,8),(1,12)]:
            group=rotations(g); perms={p for p,_ in group}
            self.assertEqual(len(perms),n)
            for p,m in group:
                self.assertEqual(determinant(m),1)
                self.assertEqual(tuple(apply(m,v) for v in POINTS[g]),tuple(POINTS[g][i] for i in p))
                for q,_ in group:self.assertIn(tuple(p[q[i]] for i in range(4)),perms)

    def test_invariant_and_classes(self):
        # Distances independently partition all six pairs; compare complete orbits.
        for g,expected in [(0,[2,4]),(1,[6])]:
            classes={orbit(g,p) for p in PAIRS}
            self.assertEqual(sorted(map(len,classes)),expected)
            def distance(pair):
                a,b=(POINTS[g][i] for i in pair)
                return sum((x-y)**2 for x,y in zip(a,b))
            for pair in PAIRS:
                self.assertEqual(set(orbit(g,pair)),{q for q in PAIRS if distance(q)==distance(pair)})

    def test_burnside_fixed_pairs(self):
        for g,expected in [(0,2),(1,1)]:
            group=rotations(g)
            fixed=sum(tuple(sorted(p[i] for i in pair))==pair for p,_ in group for pair in PAIRS)
            self.assertEqual(fixed,expected*len(group))
            for k in range(6):
                r=model(g,k)
                stabilizer=sum(tuple(sorted(p[i] for i in PAIRS[k]))==PAIRS[k] for p,_ in group)
                self.assertEqual(r['stabilizer'],stabilizer)
                self.assertEqual(r['orbit_size']*stabilizer,len(group))

    def test_view_and_contracts(self):
        for g in (0,1):
            for k in range(6):
                base=model(g,k)
                for rot in range(12):
                    r=model(g,k,rot)
                    self.assertIn(r['moved_pair'],r['orbit'])
                    self.assertEqual(r['cosine'],base['cosine'])
                    self.assertEqual(r['label'],base['label'])
        for args in [(2,0,0),(0,6,0),(1,0,12),(True,0,0),(0,0,.5)]:
            with self.assertRaises(ValueError):model(*args)
        self.assertAlmostEqual(model(1)['angle'],109.47122063449069)
        self.assertEqual(model(0,1)['angle'],180)
