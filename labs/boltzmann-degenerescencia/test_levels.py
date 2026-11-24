import unittest
from fractions import Fraction as Q
from math import exp,log,isfinite
from .levels import probabilities,thermodynamics

class BoltzmannTests(unittest.TestCase):
    def test_rational_microstate_enumeration(self):
        for g0 in (1,2,3):
            for g1 in (1,2,3):
                for w in (Q(0),Q(1,3),Q(1)):
                    weights=[Q(1)]*g0+[w]*g1
                    micro=[v/sum(weights) for v in weights]
                    self.assertEqual(probabilities(w,g0,g1),(sum(micro[:g0]),sum(micro[g0:])))
    def test_independent_entropy_energy_fluctuation(self):
        for x in (0.1,log(3),2,10):
            for g0 in (1,2):
                for g1 in (1,3):
                    weights=[1.0]*g0+[exp(-x)]*g1;z=sum(weights)
                    ps=[w/z for w in weights];energies=[0]*g0+[x]*g1
                    energy=sum(p*e for p,e in zip(ps,energies))
                    variance=sum(p*(e-energy)**2 for p,e in zip(ps,energies))
                    entropy=-sum(p*log(p) for p in ps)
                    stats=thermodynamics(x,g0,g1)
                    self.assertAlmostEqual(stats['p_exc'],sum(ps[g0:]),places=13)
                    self.assertAlmostEqual(stats['s_over_k'],entropy,places=12)
                    self.assertAlmostEqual(stats['c_over_k'],variance,places=12)
                    self.assertAlmostEqual(stats['f_over_kt'],energy-entropy,places=12)
    def test_landmarks(self):
        self.assertEqual(probabilities(Q(1,3),1,3),(Q(1,2),Q(1,2)))
        self.assertEqual(probabilities(Q(1,3)),(Q(3,4),Q(1,4)))
        stats=thermodynamics(log(3),1,3)
        self.assertAlmostEqual(stats['p_exc'],0.5,places=14)
        self.assertAlmostEqual(stats['s_over_k'],log(2)+log(3)/2,places=14)
        self.assertAlmostEqual(stats['c_over_k'],log(3)**2/4,places=14)
        self.assertAlmostEqual(thermodynamics(1000,2,3)['s_over_k'],log(2),places=14)
    def test_extremes_and_monotonicity(self):
        for gs in ((1,1),(1,3)):
            previous=1
            for x in (1e-10,1,100,1000):
                stats=thermodynamics(x,*gs)
                self.assertTrue(all(isfinite(v) for v in stats.values()))
                self.assertGreaterEqual(stats['p_exc'],0);self.assertLessEqual(stats['p_exc'],previous)
                self.assertGreaterEqual(stats['c_over_k'],0);previous=stats['p_exc']
    def test_contracts(self):
        for x in (0,-1,True,float('nan'),float('inf')):
            with self.assertRaises(ValueError):thermodynamics(x)
        for gs in ((0,1),(1,-1),(True,1),(1,1.5)):
            with self.assertRaises(ValueError):probabilities(Q(1,3),*gs)
        with self.assertRaises(ValueError):probabilities(0.5)

if __name__=='__main__':unittest.main()
