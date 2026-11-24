import unittest
from fractions import Fraction as F
from decimal import Decimal as D, localcontext
from .implicit import residual, blocks, graph_jacobian, branch_float


class ImplicitTests(unittest.TestCase):
    def test_two_roots_at_prescribed_constraint_points(self):
        for z in [F(-3), F(-2), F(-1), F(0), F(1, 2), F(1), F(2)]:
            for t in [F(-1), F(0), F(2)]:
                w, s = z-t, z*z+z-t
                self.assertEqual(residual(s, t, z, w), (0, 0))
                roots = [branch_float(float(s), float(t), sign) for sign in [-1, 1]]
                self.assertAlmostEqual(roots[0][0]+roots[1][0], -1)
                for rz, rw in roots:
                    self.assertAlmostEqual(rz*rz+rw-float(s), 0, places=11)
                    self.assertAlmostEqual(rz-rw-float(t), 0, places=11)
                self.assertTrue(any(abs(r[0]-float(z)) < 1e-11 for r in roots))
        self.assertEqual(branch_float(1, 1), (1, 0))
        self.assertEqual(branch_float(1, 1, -1), (-2, -3))

    def test_block_chain_relation(self):
        for z in [F(-3), F(-2), F(-1), F(0), F(1, 2), F(1), F(2)]:
            a, b = blocks(z)
            g = graph_jacobian(z)
            for i in range(2):
                for j in range(2):
                    self.assertEqual(a[i][j]+sum(b[i][k]*g[k][j] for k in range(2)), 0)
        self.assertEqual(graph_jacobian(1), ((F(1, 3), F(1, 3)), (F(1, 3), F(-2, 3))))

    def test_derivative_by_independent_high_precision_differences(self):
        with localcontext() as ctx:
            ctx.prec = 70
            step = D('1e-15')
            def branch(s, t):
                z = (-1+(1+4*(s+t)).sqrt())/2
                return z, z-t
            for z0 in [0, 1, 2]:
                s, t = D(z0*z0+z0-1), D(1)
                g = graph_jacobian(z0)
                for j in range(2):
                    ds, dt = (step, D(0)) if j == 0 else (D(0), step)
                    plus, minus = branch(s+ds, t+dt), branch(s-ds, t-dt)
                    for i in range(2):
                        estimate = (plus[i]-minus[i])/(2*step)
                        expected = D(g[i][j].numerator)/D(g[i][j].denominator)
                        self.assertLess(abs(estimate-expected), D('1e-27'))

    def test_exact_path_and_linear_error(self):
        for h in [F(-1, 4), F(-1, 10), F(0), F(1, 10), F(1, 2)]:
            s, t, z, w = 1+3*h+h*h, F(1), 1+h, h
            self.assertEqual(residual(s, t, z, w), (0, 0))
            ds = s-1
            self.assertEqual(h-ds/3, -h*h/3)
        self.assertEqual(F(1, 10)-F(31, 100)/3, F(-1, 300))

    def test_fold_does_not_destroy_full_constraint_rank(self):
        self.assertEqual(residual(F(-5, 4), 1, F(-1, 2), F(-3, 2)), (0, 0))
        a, b = blocks(F(-1, 2))
        self.assertEqual(b[0][0]*b[1][1]-b[0][1]*b[1][0], 0)
        self.assertEqual(a[0][0]*a[1][1]-a[0][1]*a[1][0], 1)
        with self.assertRaises(ValueError): graph_jacobian(F(-1, 2))
        with self.assertRaises(ValueError): branch_float(-1.25, 1)
        with self.assertRaises(ValueError): branch_float(-2, 1)

    def test_contracts(self):
        for bad in [True, 1.0, '1', None]:
            with self.assertRaises(ValueError): residual(bad, 1, 1, 0)
        for s, t in [(True, 1), (float('inf'), 0), (float('nan'), 0), (1e308, 1e308), (1 << 2000, 1)]:
            with self.assertRaises(ValueError): branch_float(s, t)
        for sign in [0, 2, True, 1.0, None]:
            with self.assertRaises(ValueError): branch_float(1, 1, sign)
