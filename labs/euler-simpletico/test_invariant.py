import unittest
from fractions import Fraction as Q
from math import asin,pi
from .invariant import trace,energy,invariant

class InvariantTests(unittest.TestCase):
    def test_exact_invariant_and_bounds(self):
        for eta in [Q(1,10),Q(1,2),Q(1),Q(3,2),Q(19,10)]:
            for q0,p0 in [(1,0),(0,1),(-2,1),(1,-3)]:
                inv0=invariant(q0,p0,eta);e0=energy(q0,p0)
                for q,p in trace(q0,p0,eta,40):
                    self.assertEqual(invariant(q,p,eta),inv0)
                    self.assertGreaterEqual(energy(q,p)/e0,(1-eta/2)/(1+eta/2))
                    self.assertLessEqual(energy(q,p)/e0,(1+eta/2)/(1-eta/2))
    def test_cycle_and_boundary(self):
        self.assertEqual(trace(),[(1,0),(0,-1),(-1,-1),(-1,0),(0,1),(1,1),(1,0)])
        for n,(q,p) in enumerate(trace(eta=Q(2),n=30)):
            self.assertEqual((q,p),((-1)**n*(1+2*n),(-1)**n*2*n))
            self.assertEqual(invariant(q,p,Q(2)),Q(1,2))
        self.assertEqual(energy(*trace(eta=Q(2),n=3)[-1]),Q(85,2))
    def test_structure_phase_and_unstable_example(self):
        for eta in [Q(1,10),Q(1),Q(2),Q(5,2)]:
            a,b,c,d=1-eta*eta,eta,-eta,Q(1)
            self.assertEqual(a*d-b*c,1)
        theta=2*asin(.5);self.assertAlmostEqual(theta,pi/3)
        self.assertAlmostEqual(6*(theta-1),2*pi-6)
        self.assertGreater(energy(*trace(eta=Q(5,2),n=10)[-1]),1000)
    def test_contracts(self):
        for kwargs in [dict(eta=0),dict(eta=-1),dict(eta=4),dict(eta=.1),dict(q=True),dict(n=True),dict(n=201),dict(n=-1)]:
            with self.assertRaises(ValueError):trace(**kwargs)
if __name__=='__main__':unittest.main()
