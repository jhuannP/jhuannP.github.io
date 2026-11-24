import unittest
from fractions import Fraction as Q
from .moments import evolve,stationary,euler

class OUTests(unittest.TestCase):
    def test_independent_noise_weights(self):
        # Sum independent innovation variances, rather than repeating recurrence.
        for r in (Q(-1,2),Q(0),Q(1,2),Q(3,4)):
            for noise in (Q(0),Q(1,4),Q(1)):
                for n in (0,1,2,8):
                    m,v=evolve(r,noise,2,Q(1,3),n)
                    expected=r**(2*n)*Q(1,3)+sum((noise*r**(2*j) for j in range(n)),Q(0))
                    self.assertEqual(m,2*r**n);self.assertEqual(v,expected)
    def test_composition(self):
        for r in (Q(-1,2),Q(1,2),Q(3,4)):
            for first in (0,1,3):
                for second in (0,2,4):
                    m,v=evolve(r,Q(3,4),2,0,first)
                    self.assertEqual(evolve(r,Q(3,4),m,v,second),evolve(r,Q(3,4),2,0,first+second))
    def test_invariant_exact_kernels(self):
        for rho in (Q(1,4),Q(1,2),Q(3,4)):
            for variance in (Q(1),Q(9,4),Q(4)):
                noise=variance*(1-rho*rho)
                self.assertEqual(stationary(rho,noise),variance)
                self.assertEqual(evolve(rho,noise,0,variance,7),(0,variance))
    def test_euler_bias_and_boundary(self):
        for h,expected in [(Q(1,2),Q(4,3)),(Q(1),Q(2)),(Q(3,2),Q(4))]:
            r,noise=euler(1,2,h)
            self.assertEqual(stationary(r,noise),expected)
        r,noise=euler(1,2,2)
        self.assertEqual(evolve(r,noise,0,0,3),(0,12))
        with self.assertRaises(ValueError):stationary(r,noise)
        self.assertEqual(evolve(Q(1,2),Q(3,4),2,0,2),(Q(1,2),Q(15,16)))
    def test_contracts(self):
        for args in [(1,-1,Q(1,2)),(0,1,1),(1,1,0)]:
            with self.assertRaises(ValueError):euler(*args)
        for args in [(Q(1,2),-1,0,0,1),(Q(1,2),1,0,-1,1),(Q(1,2),1,0,0,True)]:
            with self.assertRaises(ValueError):evolve(*args)
        with self.assertRaises(ValueError):stationary(0.5,1)

if __name__=='__main__':unittest.main()
