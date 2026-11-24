import unittest
from fractions import Fraction as F
from .boundary import solve,residual,quartic

class BoundaryTests(unittest.TestCase):
    def test_independent_inverse_kernel(self):
        # Inversa explícita da matriz T, sem eliminação tridiagonal.
        for n in range(2,17):
            for shift in range(3):
                b=[F((i+shift)%5-2,7) for i in range(1,n)]
                original=b.copy();U=solve(b)
                for i in range(1,n):
                    direct=sum((F(min(i,j)*(n-max(i,j)),n)*b[j-1] for j in range(1,n)),F(0))
                    self.assertEqual(U[i],direct)
                self.assertEqual(b,original)

    def test_polynomial_exactness_and_boundaries(self):
        for n in (2,3,4,8,16):
            for left,right in ((0,0),(1,2),(-2,3)):
                U=solve([F(2,n*n)]*(n-1),left,right)
                for i,value in enumerate(U):
                    x=F(i,n);self.assertEqual(value,x*(1-x)+left*(1-x)+right*x)

    def test_quartic_error_identity(self):
        for n in (2,3,4,5,8,16,32):
            xs,f,U,ref=quartic(n)
            self.assertTrue(all(v==0 for v in residual(U,f)))
            for x,a,b in zip(xs,U,ref):self.assertEqual(a-b,x*(1-x)/(n*n))
            if n%2==0:self.assertEqual(max(abs(a-b) for a,b in zip(U,ref)),F(1,4*n*n))

    def test_algebraic_residual_bound(self):
        for n in (4,8,16):
            xs,f,U,ref=quartic(n)
            # Perturbação positiva e negativa conhecida na solução do sistema.
            for sign in (-1,1):
                bad=[u+F(sign,10)*x*(1-x) for x,u in zip(xs,U)]
                r=residual(bad,f);error=max(abs(a-b) for a,b in zip(bad,U))
                self.assertEqual(error,max(map(abs,r))/8)

    def test_contracts(self):
        for b in ([],[0.5],[True]):
            with self.assertRaises(ValueError):solve(b)
        for n in (1,257,True,4.0):
            with self.assertRaises(ValueError):quartic(n)
        with self.assertRaises(ValueError):residual([0,0,0],[])
