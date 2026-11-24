import unittest,copy
from fractions import Fraction as Q
from itertools import product
from .factor import cholesky,solve_factor,relative_factor_residual

def gram(L):
    n=len(L)
    return [[sum(Q(L[i][k])*Q(L[j][k]) for k in range(n)) for j in range(n)] for i in range(n)]

def exact_gauss(A,b):
    # Referência racional por eliminação de Gauss; não usa raiz quadrada.
    m=[list(map(Q,row))+[Q(v)] for row,v in zip(A,b)];n=len(m)
    for j in range(n):
        pivot=next(i for i in range(j,n) if m[i][j]);m[j],m[pivot]=m[pivot],m[j]
        for i in range(j+1,n):
            t=m[i][j]/m[j][j]
            for k in range(j,n+1):m[i][k]-=t*m[j][k]
    x=[Q(0)]*n
    for i in range(n-1,-1,-1):x[i]=(m[i][-1]-sum(m[i][j]*x[j] for j in range(i+1,n)))/m[i][i]
    return x

class CholeskyTests(unittest.TestCase):
    def test_constructed_positive_matrices(self):
        # 216 fatores de diagonal positiva -> 648 sistemas com referência exata.
        for diag in product((1,2),repeat=3):
            for u,v,w in product((-1,0,1),repeat=3):
                known=[[diag[0],0,0],[u,diag[1],0],[v,w,diag[2]]]
                A=gram(known);snapshot=copy.deepcopy(A);L=cholesky(A)
                self.assertLess(relative_factor_residual(A,L),2e-15)
                for i in range(3):
                    for j in range(3):self.assertAlmostEqual(L[i][j],known[i][j],places=13)
                for b in [(1,0,0),(0,1,0),(-2,-1,3)]:
                    got=solve_factor(L,b);want=exact_gauss(A,b)
                    for x,y in zip(got,want):self.assertAlmostEqual(x,float(y),places=12)
                self.assertEqual(A,snapshot)

    def test_original_and_new_example(self):
        A=[[4,2],[2,3]];L=cholesky(A)
        self.assertAlmostEqual(L[1][1]**2,2,places=14)
        for b in [(1,0),(0,1),(1,1)]:
            for x,y in zip(solve_factor(L,b),exact_gauss(A,b)):self.assertAlmostEqual(x,float(y),places=14)
        self.assertEqual(solve_factor(cholesky([[4,2,-2],[2,5,1],[-2,1,3]]),[-2,-1,3]),[1,-1,2])
        self.assertEqual(solve_factor(cholesky([[9]]),[6]),[2/3])

    def test_scaling_and_reuse(self):
        A=[[4,2],[2,3]];b=[1,2];base=solve_factor(cholesky(A),b)
        for scale in [2**-20,2**20]:
            scaled=[[scale*v for v in row] for row in A]
            L=cholesky(scaled);snapshot=copy.deepcopy(L)
            got=solve_factor(L,[scale*v for v in b])
            for x,y in zip(got,base):self.assertAlmostEqual(x,y,places=13)
            solve_factor(L,[1,0]);self.assertEqual(L,snapshot)
            self.assertLess(relative_factor_residual(scaled,L),2e-15)

    def test_nonpositive_and_rounding(self):
        for A in [[[1,0],[0,-1]],[[1,1],[1,1]],[[0,0],[0,1]]]:
            with self.assertRaises(ArithmeticError):cholesky(A)
        delta=Q(1,2**54);exact=[[Q(1),Q(1)],[Q(1),1+delta]]
        self.assertGreater(exact[0][0]*exact[1][1]-exact[0][1]**2,0)
        self.assertEqual(float(1+delta),1.0)
        with self.assertRaises(ArithmeticError):cholesky(exact)
        self.assertGreater(cholesky([[1,1],[1,1+2**-20]])[1][1],0)

    def test_contracts(self):
        for A in [[],[[1,2]],[[1,2],[0,1]],[[True]],[[float('nan')]],[[float('inf')]]]:
            with self.assertRaises(ValueError):cholesky(A)
        with self.assertRaises(ValueError):solve_factor([[1,1],[0,1]],[1,2])
        with self.assertRaises(ValueError):solve_factor([[1]],[1,2])
        with self.assertRaises(ArithmeticError):solve_factor([[0]],[1])
        with self.assertRaises(ValueError):relative_factor_residual([[0]],[[0]])

if __name__=='__main__':unittest.main()
