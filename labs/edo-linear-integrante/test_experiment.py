import unittest
from fractions import Fraction as Q
from itertools import product
from copy import deepcopy
from .experiment import solve

class IntegratingFactorTests(unittest.TestCase):
    def test_reference_and_singularity(self):
        s=solve(2,[3],1,2)
        self.assertEqual(s.value(Q(1,2)),Q(9,2))
        self.assertEqual(s.value(2),Q(9,4))
        self.assertEqual(s.derivative(2),Q(3,4))
        self.assertEqual(s.derivative(Q(1,2)),-15)
        for t in (0,-1):
            with self.assertRaises(ValueError):s.value(t)
        removable=solve(2,[3],1,1) # formula t, but equation still excludes zero
        self.assertEqual(removable.constant,0)
        with self.assertRaises(ValueError):removable.value(0)
    def test_grid_initial_conditions_and_residuals(self):
        for m,q,t0,y0 in product((1,2,3),product((-1,0,1),repeat=3),(-2,-1,1,2),(-2,0,3)):
            s=solve(m,q,t0,y0);self.assertEqual(s.value(t0),y0)
            for mag in (Q(1,2),1,2,3):
                t=mag if t0>0 else -mag
                forcing=sum(Q(a)*t**j for j,a in enumerate(q))
                self.assertEqual(s.derivative(t)+Q(m,t)*s.value(t),forcing)
    def test_derivative_by_independent_centered_difference(self):
        h=Q(1,1000000)
        for m,q,t0,y0 in product((1,2,3),((3,),(1,-2,1)),(-1,1),(-2,2)):
            s=solve(m,q,t0,y0)
            for magnitude in (Q(1,2),1,2):
                t=magnitude if t0>0 else -magnitude
                numerical=(s.value(t+h)-s.value(t-h))/(2*h)
                self.assertLess(abs(numerical-s.derivative(t)),Q(1,1000000))
    def test_homogeneous_difference_and_input_preservation(self):
        q=[1,-2,3];old=deepcopy(q)
        a=solve(3,q,2,1);b=solve(3,q,2,4)
        for t in (Q(1,2),1,2,3):
            self.assertEqual((b.value(t)-a.value(t))*t**3,24)
        self.assertEqual(q,old)
        negative=solve(2,[3],-1,2)
        self.assertEqual(negative.value(-1),2)
        with self.assertRaises(ValueError):negative.value(1)
    def test_contracts(self):
        for args in [(0,[1],1,1),(True,[1],1,1),(1,[],1,1),(1,[True],1,1),
                     (1,[1.0],1,1),(1,[1],0,1),(1,[1],1,False)]:
            with self.assertRaises(ValueError):solve(*args)
        s=solve(1,[0],1,0)
        self.assertEqual(s.value(2),0)
        for t in (True,1.0):
            with self.assertRaises(ValueError):s.derivative(t)
