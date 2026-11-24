import unittest
from fractions import Fraction as Q
from itertools import product
from .analyze import matvec,candidate,characteristic,eigenspace

class EigenTests(unittest.TestCase):
    def test_known_pairs_and_noncandidates(self):
        a=((2,1),(1,2))
        self.assertEqual(candidate(a,(1,1)),3)
        self.assertEqual(candidate(a,(1,-1)),1)
        self.assertIsNone(candidate(a,(1,0)))
        self.assertEqual(characteristic(a),(1,-4,3))
        self.assertEqual(candidate(((-2,0),(0,0)),(1,0)),-2)
        self.assertEqual(candidate(((-2,0),(0,0)),(0,1)),0)
        with self.assertRaises(ValueError):candidate(a,(0,0))

    def test_basis_on_small_matrix_grid(self):
        for entries in product((-1,0,1),repeat=4):
            a=(entries[:2],entries[2:])
            for lam in (-2,-1,0,1,2):
                basis=eigenspace(a,lam)
                for v in basis:
                    self.assertNotEqual(v,(0,0))
                    self.assertEqual(matvec(a,v),tuple(lam*x for x in v))
                if len(basis)==2:
                    self.assertNotEqual(basis[0][0]*basis[1][1]-basis[0][1]*basis[1][0],0)
                    self.assertEqual(a,((lam,0),(0,lam)))
                # Enumerated candidates must belong to the returned space.
                for v in ((1,0),(0,1),(1,1),(1,-1)):
                    if matvec(a,v)!=tuple(lam*x for x in v):continue
                    self.assertTrue(basis)
                    if len(basis)==1:
                        u=basis[0]
                        self.assertEqual(u[0]*v[1]-u[1]*v[0],0)

    def test_multiplicity_examples_and_missing_real_eigenvalues(self):
        jordan=((2,1),(0,2));identity=((2,0),(0,2));rotation=((0,-1),(1,0))
        self.assertEqual(characteristic(jordan),characteristic(identity))
        self.assertEqual(len(eigenspace(jordan,2)),1)
        self.assertEqual(len(eigenspace(identity,2)),2)
        self.assertEqual(characteristic(rotation),(1,0,1))
        for lam in range(-3,4):self.assertEqual(eigenspace(rotation,lam),())

    def test_iteration_against_own_direction_decomposition(self):
        a=((2,1),(1,2))
        for x,y in product(range(-3,4),repeat=2):
            v=(Q(x),Q(y));cplus=Q(x+y,2);cminus=Q(x-y,2)
            for n in range(9):
                expected=(cplus*3**n+cminus,cplus*3**n-cminus)
                self.assertEqual(v,expected)
                v=matvec(a,v)
        for scale in (-3,Q(1,2),5):self.assertEqual(candidate(a,(scale,scale)),3)

    def test_contracts(self):
        for a in (((1,2),),(1,2),((1,2,3),(4,5,6))):
            with self.assertRaises(ValueError):characteristic(a)
        with self.assertRaises(TypeError):candidate(((2.,1),(1,2)),(1,1))
        with self.assertRaises(TypeError):eigenspace(((2,1),(1,2)),True)
        with self.assertRaises(ValueError):candidate(((2,1),(1,2)),(1,))
        self.assertEqual(candidate(((Q(1,2),0),(0,2)),(3,0)),Q(1,2))

if __name__ == "__main__":unittest.main()
