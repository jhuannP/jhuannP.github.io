import unittest
from fractions import Fraction as Q
from .experiment import project,integral,residual,square_integral,sampled_quadratic

class ContinuousLeastSquaresTests(unittest.TestCase):
    def test_exact_projection_and_orthogonality(self):
        a,b,J=project([0,0,1])
        self.assertEqual((a,b,J),(Q(-1,6),Q(1),Q(1,180)))
        r=residual([0,0,1],a,b)
        self.assertEqual(integral(r),0);self.assertEqual(integral([0]+r),0)
        # Integração independente da expansão explícita do quadrado.
        self.assertEqual(Q(1,5)-Q(1,2)+Q(4,9)-Q(1,6)+Q(1,36),J)

    def test_pythagorean_identity_and_unique_minimum(self):
        for i in range(-3,4):
            for j in range(9):
                a=Q(i,6);b=Q(j,4);da=a+Q(1,6);db=b-1
                value=square_integral(residual([0,0,1],a,b))
                self.assertEqual(value,Q(1,180)+da*da+da*db+db*db/3)
                self.assertGreaterEqual(value,Q(1,180))
                self.assertEqual(value==Q(1,180),(a,b)==(Q(-1,6),Q(1)))

    def test_reproduction_and_generic_moments(self):
        for a in (Q(-1,2),0,2):
            for b in (0,Q(1,3),3):self.assertEqual(project([a,b]),(a,b,0))
        for coefficients in ([1,2,3,4],[0,0,0,1],[2,Q(-1,3),0,0,5]):
            a,b,J=project(coefficients);r=residual(coefficients,a,b)
            self.assertEqual(integral(r),0);self.assertEqual(integral([0]+r),0)
            self.assertGreaterEqual(J,0)

    def test_samples_converge_under_declared_design(self):
        for n in (1,2,4,8,16,32):
            a,b=sampled_quadratic(n)
            self.assertEqual(a,-Q(n-1,6*n));self.assertEqual(b,1)
            J=square_integral(residual([0,0,1],a,b))
            self.assertEqual(J-Q(1,180),Q(1,36*n*n))
        self.assertEqual(sampled_quadratic(1),(0,1))
        for n in (0,-1,True,Q(3,2)):
            with self.assertRaises(ValueError):sampled_quadratic(n)
        for c in ([],[True],[.5]):
            with self.assertRaises(ValueError):project(c)
