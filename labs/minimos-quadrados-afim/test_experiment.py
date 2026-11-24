from fractions import Fraction as Q
from itertools import product
from copy import deepcopy
import unittest
from .experiment import fit

class AffineLeastSquaresTests(unittest.TestCase):
    def test_exact_example(self):
        r=fit((0,1,2),(1,2,2))
        self.assertEqual((r["intercept"],r["slope"]),(Q(7,6),Q(1,2)))
        self.assertEqual(r["fitted"],(Q(7,6),Q(5,3),Q(13,6)))
        self.assertEqual(r["residual"],(Q(1,6),Q(-1,3),Q(1,6)))
        self.assertEqual(r["sse"],Q(1,6))
    def test_exhaustive_normal_equations_and_pythagorean_identity(self):
        # 819 datasets of length 1..3; coefficients independently solved by sums.
        for n in (1,2,3):
            for xs,ys in product(product((0,1,2),repeat=n),product((-1,0,1),repeat=n)):
                r=fit(xs,ys)
                self.assertEqual(r["normal_residual"],(0,0))
                sx=sum(xs);sy=sum(ys);sxx=sum(v*v for v in xs);sxy=sum(u*v for u,v in zip(xs,ys))
                det=n*sxx-sx*sx
                if det:
                    slope=Q(n*sxy-sx*sy,det);intercept=Q(sy-slope*sx,n)
                    self.assertEqual((r["intercept"],r["slope"]),(intercept,slope))
                for da,db in product((-1,0,1),repeat=2):
                    candidate=sum((r["intercept"]+da+(r["slope"]+db)*u-v)**2 for u,v in zip(xs,ys))
                    increment=sum((da+db*u)**2 for u in xs)
                    self.assertEqual(candidate-r["sse"],increment)
                    self.assertGreaterEqual(candidate,r["sse"])
    def test_rank_deficiency_and_nonunique_coefficients(self):
        xs=(1,1,1);ys=(1,2,2);r=fit(xs,ys)
        self.assertEqual(r["rank"],1);self.assertEqual(r["null_direction"],(-1,1))
        self.assertEqual(r["fitted"],(Q(5,3),)*3);self.assertEqual(r["sse"],Q(2,3))
        for slope in (-3,0,2,Q(1,2)):
            intercept=Q(5,3)-slope
            self.assertEqual(tuple(intercept+slope*x for x in xs),r["fitted"])
        self.assertEqual(fit((2,),(7,))["fitted"],(7,))
    def test_affine_coordinates_shift_and_preservation(self):
        xs=[0,1,2];ys=[1,2,2];old=deepcopy((xs,ys));r=fit(xs,ys)
        changed=fit([2*x+3 for x in xs],ys)
        self.assertEqual(changed["fitted"],r["fitted"])
        self.assertEqual(changed["slope"],r["slope"]/2)
        self.assertEqual(changed["intercept"],r["intercept"]-3*r["slope"]/2)
        shifted=fit(xs,[v+5 for v in ys])
        self.assertEqual(shifted["sse"],r["sse"])
        self.assertEqual(shifted["intercept"],r["intercept"]+5)
        self.assertEqual((xs,ys),old)
    def test_contracts_and_exact_fit(self):
        for x,y in [([],[]),([1],[1,2]),([True],[1]),([1],[False]),([1.],[1]),([1],[float("nan")])]:
            with self.assertRaises(ValueError):fit(x,y)
        self.assertEqual(fit((0,1,2),(2,5,8))["sse"],0)
