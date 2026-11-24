import unittest,itertools
from fractions import Fraction as Q
try:
    from .experiment import rref,solve
except ImportError:
    from experiment import rref,solve

def multiply(A,x):return [sum(a*b for a,b in zip(row,x)) for row in A]
def rank_small(M):
    if any(M[0][i]*M[1][j]-M[0][j]*M[1][i]!=0 for i,j in itertools.combinations(range(len(M[0])),2)):return 2
    return int(any(x!=0 for row in M for x in row))

class EliminationTests(unittest.TestCase):
    def test_known_cases_and_free_variables(self):
        r=solve([[1,1],[1,-1]],[3,1]);self.assertEqual(r['particular'],[2,1]);self.assertEqual(r['status'],'unica')
        r=solve([[1,2],[2,4]],[3,6]);self.assertEqual(r['particular'],[3,0]);self.assertEqual(r['null_basis'],[[-2,1]])
        self.assertEqual(solve([[1,2],[2,4]],[3,7])['status'],'inconsistente')
        r=solve([[1,1,0],[0,1,1]],[2,3]);self.assertEqual(r['particular'],[-1,3,0]);self.assertEqual(r['null_basis'],[[1,-1,1]])
        self.assertEqual(solve([[0,0],[0,0]],[0,0])['null_basis'],[[1,0],[0,1]])

    def test_all_small_2x2_against_minors(self):
        for cells in itertools.product([-1,0,1],repeat=4):
            A=[list(cells[:2]),list(cells[2:])]
            for b in itertools.product([-1,0,1],repeat=2):
                r=solve(A,b);ra=rank_small(A);rab=rank_small([A[i]+[b[i]] for i in range(2)])
                self.assertEqual(r['rank_A'],ra);self.assertEqual(r['rank_augmented'],rab)
                expected='inconsistente' if ra!=rab else 'unica' if ra==2 else 'infinitas'
                self.assertEqual(r['status'],expected)
                if r['particular'] is not None:self.assertEqual(multiply(A,r['particular']),list(b))
                for vector in r['null_basis']:self.assertEqual(multiply(A,vector),[0,0])

    def test_row_swap_fraction_and_input_preservation(self):
        A=[[0,Q(1,2)],[1,1]];b=[1,4]
        r=solve(A,b);self.assertEqual(r['particular'],[2,2]);self.assertEqual(A,[[0,Q(1,2)],[1,1]])
        reduced,pivots=rref([[1,2,3],[2,4,6]])
        self.assertEqual(reduced,[[1,2,3],[0,0,0]]);self.assertEqual(pivots,[0])
        r=solve([[1],[2],[3]],[2,4,6]);self.assertEqual(r['particular'],[2])
        self.assertEqual(solve([[1],[2],[3]],[2,4,7])['status'],'inconsistente')

    def test_contracts(self):
        for A,b in [([],[]),([[1,2]],[1,2]),([[1],[1,2]],[1,2]),([[True]],[1]),([[.5]],[1])]:
            with self.assertRaises(ValueError):solve(A,b)
        for M in [[],[[]],[[1],[1,2]]]:
            with self.assertRaises(ValueError):rref(M)

if __name__=='__main__':unittest.main()
