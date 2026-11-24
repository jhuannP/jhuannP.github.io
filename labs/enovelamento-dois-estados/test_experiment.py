import unittest
from math import exp, log, inf, nan
from .experiment import folding, populations, R

class FoldingTests(unittest.TestCase):
    def test_midpoint_signs_and_independent_partition(self):
        for Tm in (300,330,360):
            for H in (40,120,200):
                q=folding(Tm,Tm,H)
                self.assertEqual((q['delta_g'],q['log_K'],q['folded'],q['unfolded']),(0,0,.5,.5))
                for T in (270,300,330,360,390):
                    q=folding(T,Tm,H)
                    # Cálculo independente via H-T*S e dois pesos não normalizados.
                    dg=H-T*(H/Tm)
                    k=exp(-dg/(R*T))
                    self.assertAlmostEqual(q['unfolded'],k/(1+k),places=13)
                    self.assertAlmostEqual(q['folded']+q['unfolded'],1,places=15)
                    self.assertAlmostEqual(q['log_K'],log(q['unfolded']/q['folded']),places=12)
                    self.assertEqual(q['unfolded']>.5,T>Tm)
        self.assertAlmostEqual(folding(330,300,120)['delta_g'],-12,places=12)

    def test_mixture_gibbs_minimum_and_equilibrium_force(self):
        # G(x) relativo a F: x*dG + RT[x ln x +(1-x) ln(1-x)].
        for T in (310,330,350):
            q=folding(T,330,120);x=q['unfolded'];dg=q['delta_g']
            force=dg+R*T*log(x/(1-x))
            self.assertAlmostEqual(force,0,places=12)
            energy=lambda y:y*dg+R*T*(y*log(y)+(1-y)*log(1-y))
            self.assertLess(energy(x),energy(x-.001))
            self.assertLess(energy(x),energy(x+.001))
            # Curvatura estritamente positiva no interior: mínimo único.
            self.assertGreater(R*T*(1/x+1/(1-x)),0)

    def test_monotonicity_sharpness_and_stable_extremes(self):
        for H in (40,120,200):
            values=[folding(T,330,H)['unfolded'] for T in range(260,401)]
            self.assertTrue(all(a<b for a,b in zip(values,values[1:])))
            eps=.0001
            slope=(folding(330+eps,330,H)['unfolded']-folding(330-eps,330,H)['unfolded'])/(2*eps)
            self.assertAlmostEqual(slope,H/(4*R*330**2),places=9)
        for z in (-1000,-100,-log(3),0,log(3),100,1000):
            q=populations(z);rev=populations(-z)
            self.assertAlmostEqual(q['folded'],rev['unfolded'],places=15)
            self.assertAlmostEqual(q['folded']+q['unfolded'],1,places=15)
        self.assertAlmostEqual(populations(log(3))['unfolded'],.75)
        self.assertAlmostEqual(populations(-log(3))['unfolded'],.25)

    def test_contract(self):
        for args in ((0,330,120),(300,0,120),(300,330,0),(-1,330,120),(True,330,120),(nan,330,120),(300,inf,120),('300',330,120),(5e-324,330,120)):
            with self.assertRaises(ValueError):folding(*args)
        for z in (True,inf,nan,'1'):
            with self.assertRaises(ValueError):populations(z)
