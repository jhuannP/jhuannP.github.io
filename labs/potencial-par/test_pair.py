import unittest
from fractions import Fraction as Q
from decimal import Decimal,localcontext
from .pair import potential,force,curvature,minimum_bracket,work


class PairPotential(unittest.TestCase):
    def test_landmarks_and_force_sign(self):
        self.assertEqual((potential(1),force(1)),(0,24))
        self.assertEqual((potential(2),force(2)),(Q(-63,1024),Q(-93,512)))
        self.assertEqual((potential(Q(1,2)),force(Q(1,2))),(16128,390144))
        self.assertLess(potential(Q(11,10)),0)
        self.assertGreater(force(Q(11,10)),0)
        self.assertLess(force(Q(6,5)),0)

    def test_units_scales_and_offset_invariance(self):
        for epsilon in [1,2,5]:
            for sigma in [1,3]:
                for s in [Q(1,2),1,Q(3,2),2]:
                    self.assertEqual(potential(s*sigma,epsilon,sigma),epsilon*potential(s))
                    self.assertEqual(force(s*sigma,epsilon,sigma),Q(epsilon,sigma)*force(s))
                    self.assertEqual(curvature(s*sigma,epsilon,sigma),Q(epsilon,sigma*sigma)*curvature(s))
        for C in [-3,0,7]:
            self.assertEqual((potential(1)+C)-(potential(2)+C),Q(63,1024))

    def test_derivatives_by_independent_differences(self):
        for r in [Q(3,4),1,Q(9,8),Q(3,2),2]:
            errors=[]
            for h in [Q(1,1024),Q(1,2048),Q(1,4096)]:
                numeric=-(potential(r+h)-potential(r-h))/(2*h)
                errors.append(abs(numeric-force(r)))
            for a,b in zip(errors,errors[1:]):self.assertTrue(Q(39,10)<a/b<Q(41,10))
            h=Q(1,10000)
            numeric=-(force(r+h)-force(r-h))/(2*h)
            self.assertLess(abs(float((numeric-curvature(r))/curvature(r))),1e-5)

    def test_certified_root_bracket_and_stability(self):
        with localcontext() as ctx:
            ctx.prec=70
            reference=(Decimal(2).ln()/6).exp()
            prev=(Q(1),Q(3,2))
            for steps in [16,32,60]:
                lo,hi=minimum_bracket(steps)
                self.assertLess(lo**6,2);self.assertGreater(hi**6,2)
                self.assertEqual(hi-lo,Q(1,2**(steps+1)))
                self.assertTrue(prev[0]<=lo<hi<=prev[1]);prev=(lo,hi)
                decimal=lambda q:Decimal(q.numerator)/Decimal(q.denominator)
                self.assertTrue(decimal(lo)<reference<decimal(hi))
                self.assertGreater(force(lo),0);self.assertLess(force(hi),0)
                self.assertGreater(curvature(lo),0);self.assertGreater(curvature(hi),0)
            mid=sum(prev)/2
            self.assertLess(abs(float(potential(mid)+1)),1e-30)
            self.assertLess(abs(float(curvature(mid)-72/mid**2)),1e-12)

    def test_force_work_matches_energy_with_refinement(self):
        exact=Q(63,1024);errors=[]
        for N in [32,64,128]:
            approx=work(1,2,panels=N)
            errors.append(abs(approx-exact))
        for a,b in zip(errors,errors[1:]):self.assertTrue(15<a/b<17)
        self.assertLess(float(errors[-1]),1e-5)
        self.assertGreater(exact,0)

    def test_contracts(self):
        for fn in [potential,force,curvature]:
            for i in range(3):
                for bad in [0,-1,True,1.0,'1']:
                    args=[1,1,1];args[i]=bad
                    with self.assertRaises(ValueError):fn(*args)
        for steps in [0,129,True,1.0]:
            with self.assertRaises(ValueError):minimum_bracket(steps)
        for N in [0,3,514,True,2.0]:
            with self.assertRaises(ValueError):work(1,2,panels=N)
        with self.assertRaises(ValueError):work(2,1)
