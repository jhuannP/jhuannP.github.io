import unittest
from fractions import Fraction as Q
from .shoot import shoot,integrate

class ShootingTests(unittest.TestCase):
    def test_fixture_two_residuals(self):
        s,tr=shoot(10)
        self.assertEqual(s,Q(18,25));self.assertEqual(tr[-1][1],0)
        self.assertEqual(s-1,-Q(7,25));self.assertEqual(tr[5][1],Q(3,10))
        self.assertEqual(Q(3,8)-tr[5][1],Q(3,40))

    def test_exact_sum_oracle(self):
        for c in range(1,7):
            for n in range(2,31):
                for s in (-2,Q(1,3),2):
                    tr=integrate(s,n,c)
                    for k,(x,u,v) in enumerate(tr):
                        # Somas fechadas independentes da recorrência.
                        self.assertEqual(v,s-Q(c*k*(k-1),2*n*n))
                        self.assertEqual(u,Q(s)*x-Q(c*k*(k-1)*(k-2),6*n**3))
                slope,tr=shoot(n,c)
                self.assertEqual(slope,Q(c*(n-1)*(n-2),6*n*n))

    def test_mesh_refinement_and_affine_map(self):
        for n in range(2,51,2):
            s,tr=shoot(n);ss,tt=shoot(2*n)
            err=Q(3,8)-tr[n//2][1];err2=Q(3,8)-tt[n][1]
            self.assertEqual(err,2*err2);self.assertEqual(err,Q(3,4*n))
            for a,b in ((-1,1),(0,2),(Q(1,3),Q(7,5))):
                fa=integrate(a,n)[-1][1];fb=integrate(b,n)[-1][1]
                self.assertEqual(fb-fa,b-a)
                self.assertEqual(a-fa*(b-a)/(fb-fa),s)

    def test_contracts(self):
        for n in (0,1,201,True,2.0):
            with self.assertRaises(ValueError):shoot(n)
        for c in (0,-1,13,True,0.5):
            with self.assertRaises(ValueError):shoot(10,c)
        for s in (True,1.0,101):
            with self.assertRaises(ValueError):integrate(s,10)
