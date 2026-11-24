import unittest
from itertools import combinations, permutations, product
from fractions import Fraction as Q
from geometry import classify, dot, weighted_sum, TETRA, PLANAR, LINEAR


class GeometryTests(unittest.TestCase):
    def test_gram_and_cancellation(self):
        # Geometry verified by Gram products, independently of VSEPR labels.
        for vectors,length2,pairdot in [(TETRA,3,-1),(PLANAR,2,-1),(LINEAR,1,-1)]:
            self.assertTrue(all(dot(v,v)==length2 for v in vectors))
            for u,v in combinations(vectors,2): self.assertEqual(dot(u,v),pairdot)
            self.assertEqual(weighted_sum(vectors,[1]*len(vectors)),(0,0,0))
        self.assertEqual(dot(TETRA[0],TETRA[1])/3,Q(-1,3))

    def test_change_weights_and_remove_directions(self):
        for index in range(4):
            weights=[1]*4;weights[index]=2
            self.assertEqual(weighted_sum(TETRA,weights),TETRA[index])
            weights[index]=0
            self.assertEqual(weighted_sum(TETRA,weights),tuple(-v for v in TETRA[index]))
        self.assertEqual(weighted_sum(LINEAR,[1,2]),(-1,0,0))
        # Bent synthetic 90-degree case, not coordinates of a water molecule.
        self.assertEqual(weighted_sum([(1,0,0),(0,1,0)],[1,1]),(1,1,0))

    def test_coordinate_changes(self):
        # Signed permutations are 48 exact orthogonal coordinate transforms.
        for order,signs in product(permutations(range(3)),product((-1,1),repeat=3)):
            transformed=[tuple(signs[k]*v[order[k]] for k in range(3)) for v in TETRA]
            self.assertEqual(weighted_sum(transformed,[1]*4),(0,0,0))
            for i,j in combinations(range(4),2):
                self.assertEqual(dot(transformed[i],transformed[j]),-1)

    def test_counts_and_contracts(self):
        # Same domain count can give different molecular shapes.
        a,b=classify(4,0),classify(2,2)
        self.assertEqual(a['regions'],b['regions'])
        self.assertNotEqual(a['molecular'],b['molecular'])
        for args in [(True,0),(2,False),(2.0,0),(5,0),(0,0),(2,-1)]:
            with self.assertRaises(ValueError): classify(*args)
        for vectors,weights in [([],[]),([(1,2)],[1]),([(1,2,3)],[]),([(1,2,3)],[True]),([(1,2,3)],[1.0])]:
            with self.assertRaises(ValueError): weighted_sum(vectors,weights)


if __name__=='__main__': unittest.main()
