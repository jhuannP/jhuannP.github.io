import unittest
from math import exp,log
from .experiment import model,RT

class CouplingTests(unittest.TestCase):
    def test_chemical_potentials_independent_route(self):
        # μ°A=0, μ°B=12, μ°D=20, μ°E=0; aA=aD=aE=1, aB=Q.
        for j in range(-3,4):
            r=model(j)
            mu=dict(A=0.,B=12+RT*log(10.**j),D=20.,E=0.)
            net=mu['B']+mu['E']-mu['A']-mu['D']
            self.assertAlmostEqual(net,r['net'],places=12)
            self.assertAlmostEqual(r['net'],RT*log(r['q']/r['equilibrium_q']),places=12)

    def test_monotonicity_and_sign(self):
        rs=[model(j) for j in range(-3,4)]
        self.assertTrue(all(a['net']<b['net'] for a,b in zip(rs,rs[1:])))
        self.assertEqual(model(0)['net'],-8)
        self.assertLess(model(1)['net'],0);self.assertGreater(model(2)['net'],0)
        for a,b in zip(rs,rs[1:]):self.assertAlmostEqual(b['net']-a['net'],RT*log(10))
        self.assertAlmostEqual(-8+RT*log(exp(8/RT)),0)

    def test_contracts(self):
        for j in (True,None,0.,'1',-4,4):
            with self.assertRaises(ValueError):model(j)
