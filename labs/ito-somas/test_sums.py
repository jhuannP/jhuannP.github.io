import unittest
from fractions import Fraction as Q
from itertools import product
from .sums import quadrature,brownian_mse,predictable_example

class SumsTests(unittest.TestCase):
    def test_exact_telescoping_1875_cases(self):
        for increments in product(range(-2,3),repeat=4):
            for w0 in (-2,0,3):
                a=quadrature(increments,w0);delta=a['end']**2-w0**2
                self.assertEqual(2*a['left'],delta-a['qv'])
                self.assertEqual(2*a['right'],delta+a['qv'])
                self.assertEqual(2*a['trapezoidal'],delta)
                self.assertEqual(a['right']-a['left'],a['qv'])
    def test_fixture_and_mesh_error(self):
        a=quadrature([Q(1,2),Q(-1,4),Q(3,4)])
        self.assertEqual(a['qv'],Q(7,8));self.assertEqual(a['left'],Q(1,16))
        self.assertEqual(a['trapezoidal'],Q(1,2));self.assertEqual(a['right'],Q(15,16))
        for n in (1,2,4,8,16,32):
            self.assertEqual(brownian_mse([Q(2,n)]*n),Q(2,n))
        h=[Q(1,4),Q(1,2),Q(3,4)]
        self.assertLessEqual(brownian_mse(h),sum(h)*max(h)/2)
    def test_predictability_and_counterexample(self):
        for a,b,c in product(range(-2,3),repeat=3):
            mean,second,energy=predictable_example(a,b,c)
            self.assertEqual(mean,0);self.assertEqual(second,energy)
            self.assertEqual(energy,a*a+b*b+c*c)
        values=[first*first+first*second for first,second in product((-1,1),repeat=2)]
        self.assertEqual(sum(values)/4,1) # Antecipar destrói média zero.
    def test_contracts(self):
        for values in ([],[True],[.5],['1'],[0]*257):
            with self.assertRaises(ValueError):quadrature(values)
        for steps in ([],[0],[-1],[.5]):
            with self.assertRaises(ValueError):brownian_mse(steps)
        with self.assertRaises(ValueError):predictable_example(1,True,1)
