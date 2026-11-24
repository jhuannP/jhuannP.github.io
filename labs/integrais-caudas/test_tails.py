import unittest
from fractions import Fraction as Q
from .tails import tail, partial, cutoff, finite_bracket

class TailTests(unittest.TestCase):
    def test_known_values_and_boundary(self):
        self.assertEqual((partial(2,10),tail(2,10)), (Q(9,10),Q(1,10)))
        self.assertEqual((partial(3,10),tail(3,10)), (Q(99,200),Q(1,200)))
        self.assertEqual(tail(2,Q(3,2)),Q(2,3))
        for p in range(2,8):
            self.assertEqual(partial(p,1),0)
            self.assertEqual(tail(p,1),Q(1,p-1))

    def test_scale_law_and_monotonicity(self):
        for p in range(2,7):
            previous = tail(p,1)
            for b in range(2,21):
                remaining = tail(p,b)
                self.assertLess(remaining,previous)
                self.assertEqual(tail(p,2*b)*2**(p-1), remaining)
                self.assertEqual(partial(p,b)+remaining,Q(1,p-1))
                previous=remaining

    def test_strict_cutoff_against_linear_search(self):
        self.assertEqual(cutoff(2,Q(1,100)),101)
        self.assertEqual(cutoff(3,Q(1,1000)),23)
        for p in range(2,6):
            for d in range(1,81):
                epsilon=Q(1,d)
                expected=next(b for b in range(1,83) if tail(p,b)<epsilon)
                self.assertEqual(cutoff(p,epsilon),expected)
            for b in range(1,15):
                self.assertEqual(cutoff(p,tail(p,b)),b+1)
        self.assertEqual(cutoff(2,2),1)

    def test_analytic_integral_inside_rectangle_bounds(self):
        # Rectangle bounds independently sample the decreasing integrand.
        # Dyadic refinement should tighten the brackets without losing the integral.
        for p in range(2,6):
            for b in (1,Q(3,2),2,4,10):
                exact=partial(p,b)
                outer=None
                for n in (2,4,8,16):
                    lo,hi=finite_bracket(p,b,n)
                    self.assertLessEqual(lo,exact)
                    self.assertLessEqual(exact,hi)
                    self.assertLessEqual(lo+tail(p,b),Q(1,p-1))
                    self.assertLessEqual(Q(1,p-1),hi+tail(p,b))
                    if outer:
                        self.assertGreaterEqual(lo,outer[0])
                        self.assertLessEqual(hi,outer[1])
                    # Independent telescoping identity for left/right gap.
                    self.assertEqual(hi-lo,(Q(b)-1)/n*(1-Q(b)**(-p)))
                    outer=lo,hi

    def test_contracts(self):
        for p in (True,2.,Q(2),"2"):
            with self.assertRaises(TypeError):tail(p,10)
        for p in (-1,0,1):
            with self.assertRaises(ValueError):tail(p,10)
        for b in (True,1.,float('nan'),float('inf'),None):
            with self.assertRaises(TypeError):partial(2,b)
        for b in (0,Q(1,2)):
            with self.assertRaises(ValueError):tail(2,b)
        for eps in (0,-1):
            with self.assertRaises(ValueError):cutoff(2,eps)
        with self.assertRaises(TypeError):cutoff(2,.01)
        with self.assertRaises(TypeError):finite_bracket(2,10,True)
        with self.assertRaises(ValueError):finite_bracket(2,10,0)

if __name__ == "__main__":unittest.main()
