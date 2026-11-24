import unittest,itertools,math
from fractions import Fraction as Q
from .experiment import F,G,H,jacobians,remainder,model,matmul

class VectorChainTests(unittest.TestCase):
    def test_composition_and_direct_jacobian(self):
        for u,v in itertools.product(range(-2,3),repeat=2):
            self.assertEqual(G(*F(u,v)),H(u,v))
            A,B,C=jacobians(u,v)
            direct=[[2*u+v*v,2*u*v],[2*u*v*v,2*u*u*v-1]]
            self.assertEqual(C,direct)
            self.assertEqual((len(A),len(A[0]),len(B),len(B[0])),(3,2,2,3))
            self.assertEqual((len(matmul(A,B)),len(matmul(A,B)[0])),(3,3))
    def test_exact_fraction_remainder(self):
        for u,v in itertools.product(range(-2,3),repeat=2):
            A,B,C=jacobians(u,v)
            for w,k in itertools.product(((1,0),(0,1),(1,1)),range(1,9)):
                a,b=(Q(x,2**k) for x in w)
                actual=[x-y for x,y in zip(G(*F(u+a,v+b)),G(*F(u,v)))]
                linear=[row[0]*a+row[1]*b for row in C]
                exact=tuple(x-y for x,y in zip(actual,linear))
                self.assertEqual(exact,remainder(u,v,a,b))
    def test_uniform_bound_and_refinement(self):
        for u,v in itertools.product(range(-2,3),repeat=2):
            for direction in range(3):
                for k in range(1,9):
                    m=model(u,v,direction,k)
                    self.assertLessEqual(m['relative_remainder'],m['bound']+1e-12)
                    for x,y in zip(m['remainder'],[a-b for a,b in zip(m['actual'],m['linear'])]):self.assertAlmostEqual(x,y,places=13)
                self.assertLessEqual(model(u,v,direction,8)['relative_remainder'],model(u,v,direction,1)['relative_remainder']+1e-12)
        self.assertEqual(model()['C'],[[6,4],[8,3]])
    def test_contract_and_matrix_dimensions(self):
        for args in [(3,0,0,1),(0,0,3,1),(0,0,0,0),(True,0,0,1),(0,0,0,True),(float('nan'),0,0,1)]:
            with self.assertRaises(ValueError):model(*args)
        for A,B in [([],[[1]]),([[1,2]],[[1]]),([[1],[2,3]],[[1]])]:
            with self.assertRaises(ValueError):matmul(A,B)
