from fractions import Fraction as Q
from itertools import product
import unittest
from .exact_lu import factor,solve,ZeroPivot

def mm(A,B):
    return tuple(tuple(sum(a*b for a,b in zip(row,col)) for col in zip(*B)) for row in A)
def mv(A,x):return tuple(sum(a*b for a,b in zip(row,x)) for row in A)

class LUTests(unittest.TestCase):
    def test_original_and_reuse(self):
        A=[[4,3],[6,3]];L,U=factor(A)
        self.assertEqual(L,((1,0),(Q(3,2),1)))
        self.assertEqual(U,((4,3),(0,Q(-3,2))))
        self.assertEqual(mm(L,U),tuple(map(tuple,A)))
        snapshot=(L,U)
        self.assertEqual(solve(L,U,[7,9]),(1,1))
        self.assertEqual(solve(L,U,[5,9]),(2,-1))
        self.assertEqual(solve(L,U,[1,0]),(Q(-1,2),1))
        self.assertEqual((L,U),snapshot);self.assertEqual(A,[[4,3],[6,3]])

    def test_generated_triangular_factors_and_rhs(self):
        for a,b,c in product((-1,0,1),repeat=3):
            want_L=((1,0,0),(a,1,0),(b,c,1))
            for q in (-1,0,2):
                want_U=((2,q,q+1),(0,-3,q-1),(0,0,4))
                A=mm(want_L,want_U);L,U=factor(A)
                self.assertEqual(L,want_L);self.assertEqual(U,want_U)
                for x in ((1,0,0),(1,-2,3),(-2,0,1)):
                    rhs=mv(A,x);actual=solve(L,U,rhs)
                    self.assertEqual(actual,x);self.assertEqual(mv(A,actual),rhs)

    def test_independent_cramer_reference(self):
        for a,b,c,d in product((-1,0,1),repeat=4):
            det=a*d-b*c
            if a==0 or det==0:continue
            L,U=factor(((a,b),(c,d)))
            for e,f in product((-1,0,1),repeat=2):
                self.assertEqual(solve(L,U,(e,f)),(Q(d*e-b*f,det),Q(a*f-c*e,det)))

    def test_permutation_requires_permuted_rhs(self):
        A=((0,1),(1,1));b=(1,2)
        with self.assertRaises(ZeroPivot):factor(A)
        PA=(A[1],A[0]);L,U=factor(PA)
        right=solve(L,U,(b[1],b[0]));wrong=solve(L,U,b)
        self.assertEqual(right,(1,1));self.assertEqual(mv(A,right),b)
        self.assertEqual(wrong,(-1,2));self.assertNotEqual(mv(A,wrong),b)

    def test_contracts_and_late_zero_pivot(self):
        for A in ([],[[1,2]],[[1],[2]],[[True]],[[.5]]):
            with self.assertRaises((ValueError,TypeError)):factor(A)
        for A in (((0,1),(1,1)),((1,2),(2,4))):
            with self.assertRaises(ZeroPivot):factor(A)
        L,U=factor([[3]])
        self.assertEqual(solve(L,U,[6]),(2,))
        for left,upper,rhs in ((((2,),),U,(6,)),(L,((0,),),(6,)),(L,U,(1,2)),(((1,1),(0,1)),((1,0),(0,1)),(1,1))):
            with self.assertRaises(ValueError):solve(left,upper,rhs)

if __name__=='__main__':unittest.main()
