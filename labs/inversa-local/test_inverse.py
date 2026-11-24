import unittest
from fractions import Fraction as F
from decimal import Decimal, localcontext
from .inverse import forward, jacobian, inverse_jacobian, inverse_float


class InverseTests(unittest.TestCase):
    def test_chain_and_independent_symmetric_differences(self):
        for x in [F(-3), F(-1, 2), F(1, 10), F(1, 2), F(2), F(7)]:
            a, b = jacobian(x), inverse_jacobian(x)
            for left, right in [(a, b), (b, a)]:
                product = tuple(tuple(sum(left[i][k]*right[k][j] for k in range(2)) for j in range(2)) for i in range(2))
                self.assertEqual(product, ((1, 0), (0, 1)))
            step = F(1, 37)
            for j in range(2):
                delta = (step, 0) if j == 0 else (0, step)
                plus = forward(x+delta[0], 1+delta[1])
                minus = forward(x-delta[0], 1-delta[1])
                self.assertEqual(tuple((plus[i]-minus[i])/(2*step) for i in range(2)),
                                 tuple(a[i][j] for i in range(2)))

    def test_explicit_quadratic_remainder(self):
        for h in [F(-1, 2), F(-1, 10), F(0), F(1, 10), F(1, 2)]:
            for k in [F(-1, 3), F(0), F(2, 7)]:
                u, v = forward(2+h, 1+k)
                self.assertEqual((u-5-(4*h+k), v-1-k), (h*h, 0))
                predicted_dx = ((u-5)-(v-1))/4
                self.assertEqual(h-predicted_dx, -h*h/4)

    def test_two_branches_with_decimal_reference(self):
        for x in [F(1, 10), F(1, 2), F(2), F(7, 2)]:
            for y in [F(-2), F(0), F(3)]:
                u, v = forward(x, y)
                self.assertEqual(forward(-x, y), (u, v))
                for sign in [-1, 1]:
                    result = inverse_float(float(u), float(v), sign)
                    self.assertAlmostEqual(result[0], float(sign*x), places=12)
                    self.assertEqual(result[1], float(v))
        with localcontext() as ctx:
            ctx.prec = 70
            for w in ['0.00000001', '0.001', '2', '4', '10', '100']:
                expected = Decimal(w).sqrt()
                value = inverse_float(float(w), 0)[0]
                relative = abs(Decimal(str(value))-expected)/expected
                self.assertLess(relative, Decimal('3e-16'))

    def test_landmarks_and_determinant_not_condition(self):
        self.assertEqual(forward(2, 1), (5, 1))
        self.assertEqual(inverse_jacobian(2), ((F(1, 4), F(-1, 4)), (0, 1)))
        self.assertEqual(F(1, 10)-(F(541, 100)-5)/4, F(-1, 400))
        for lam in [F(1, 1000), F(1, 10), F(1), F(10), F(1000)]:
            self.assertEqual(lam*(1/lam), 1)
            gain = max(lam, 1/lam)
            self.assertGreaterEqual(gain, 1)
        self.assertEqual(max(F(1000), F(1, 1000)), 1000)

    def test_contracts_and_branch_boundary(self):
        for x in [True, 1.0, '1', None]:
            with self.assertRaises(ValueError): forward(x, 0)
        with self.assertRaises(ValueError): inverse_jacobian(0)
        for u, v in [(0, 0), (1, 2), (float('inf'), 0), (float('nan'), 0), (1e308, -1e308), (True, 0), (1 << 2000, 0)]:
            with self.assertRaises(ValueError): inverse_float(u, v)
        for sign in [0, 2, True, 1.0, None]:
            with self.assertRaises(ValueError): inverse_float(5, 1, sign)
