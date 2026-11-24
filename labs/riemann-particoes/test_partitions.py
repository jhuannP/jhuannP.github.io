from fractions import Fraction as Q
from itertools import combinations
import unittest
from .partitions import bounds,tagged_sum

class PartitionTests(unittest.TestCase):
    def test_uniform_closed_forms(self):
        for n in range(1,41):
            p=[Q(i,n) for i in range(n+1)];b=bounds(p)
            self.assertEqual(b['lower'],Q(1,3)-Q(1,2*n)+Q(1,6*n*n))
            self.assertEqual(b['upper'],Q(1,3)+Q(1,2*n)+Q(1,6*n*n))
            self.assertEqual(b['upper']-b['lower'],Q(1,n))
        self.assertEqual(bounds([0,Q(1,2),1])['lower'],Q(1,8))

    def test_all_eighth_grid_partitions_and_tags(self):
        grid=[Q(i,8) for i in range(1,8)]
        for k in range(8):
            for chosen in combinations(grid,k):
                p=(Q(0),)+chosen+(Q(1),);b=bounds(p)
                self.assertLessEqual(b['lower'],Q(1,3))
                self.assertGreaterEqual(b['upper'],Q(1,3))
                self.assertLessEqual(b['upper']-b['lower'],2*b['mesh'])
                for tags in (p[:-1],p[1:],tuple((a+c)/2 for a,c in zip(p,p[1:]))):
                    value=tagged_sum(p,tags)
                    self.assertTrue(b['lower']<=value<=b['upper'])
                refined=sorted(set(p)|{(a+c)/2 for a,c in zip(p,p[1:])})
                f=bounds(refined)
                self.assertGreaterEqual(f['lower'],b['lower'])
                self.assertLessEqual(f['upper'],b['upper'])

    def test_nonuniform_example(self):
        b=bounds([0,Q(1,4),Q(1,2),1])
        self.assertEqual(b,dict(lower=Q(9,64),upper=Q(37,64),mesh=Q(1,2)))
        self.assertEqual(b['upper']-b['lower'],Q(7,16))

    def test_more_points_without_mesh_refinement(self):
        for n in (1,2,4,8,16):
            p=[Q(i,2*n) for i in range(n+1)]+[Q(1)]
            b=bounds(p)
            self.assertEqual(b['mesh'],Q(1,2))
            self.assertGreaterEqual(b['upper']-b['lower'],Q(3,8))

    def test_contracts(self):
        for p in ([],[0],[1,0],[0,0,1],[0,2,1],[0,Q(1,2)],[-1,0,1],[0,True,1],[0,.5,1]):
            with self.assertRaises(ValueError):bounds(p)
        for tags in ([],[Q(1,2),2],[Q(-1),Q(3,4)],[0.,1]):
            with self.assertRaises(ValueError):tagged_sum([0,Q(1,2),1],tags)

if __name__=='__main__':unittest.main()
