import unittest
from itertools import product
from .experiment import matrix,apply,compose,snapshot,ATOMS

class C2vTests(unittest.TestCase):
    def test_group_axioms_exhaustively(self):
        for a,b,c in product(range(4),repeat=3):
            self.assertIn(compose(a,b),range(4))
            self.assertEqual(compose(compose(a,b),c),compose(a,compose(b,c)))
        for a in range(4):
            self.assertEqual(compose(a,0),a);self.assertEqual(compose(0,a),a)
            self.assertEqual(compose(a,a),0)
        self.assertEqual(compose(2,3),1)

    def test_independent_full_matrix_products(self):
        expected=[[[1,0,0],[0,1,0],[0,0,1]],[[-1,0,0],[0,-1,0],[0,0,1]],[[1,0,0],[0,-1,0],[0,0,1]],[[-1,0,0],[0,1,0],[0,0,1]]]
        for a,b in product(range(4),repeat=2):
            full=[[sum(expected[a][i][k]*expected[b][k][j] for k in range(3)) for j in range(3)] for i in range(3)]
            self.assertEqual(matrix(compose(a,b)),full)
            v=[1,2,3];first=[sum(expected[b][i][j]*v[j] for j in range(3)) for i in range(3)]
            last=[sum(expected[a][i][j]*first[j] for j in range(3)) for i in range(3)]
            self.assertEqual(snapshot(a,b)['probe'],last)

    def test_nuclear_geometry_and_nonfaithful_permutation(self):
        def d2(u,v):return sum((a-b)**2 for a,b in zip(u,v))
        for a in range(4):
            changed=[apply(a,p) for p in ATOMS]
            self.assertEqual(sorted(changed),sorted(ATOMS))
            for i,j in product(range(3),repeat=2):self.assertEqual(d2(changed[i],changed[j]),d2(ATOMS[i],ATOMS[j]))
        self.assertEqual(snapshot(0,0)['permutation'],snapshot(2,0)['permutation'])
        self.assertNotEqual(matrix(0),matrix(2));self.assertNotEqual(apply(0,(1,2,3)),apply(2,(1,2,3)))
        self.assertEqual(snapshot(1,0)['permutation'],[0,2,1])

    def test_domains_and_determinants(self):
        for k in (-1,4,1.5,'1'):
            with self.assertRaises(ValueError):matrix(k)
        with self.assertRaises(ValueError):apply(0,(1,2))
        self.assertEqual([snapshot(i,0)['determinant'] for i in range(4)],[1,1,-1,-1])

if __name__=='__main__':unittest.main()
