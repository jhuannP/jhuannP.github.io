import unittest
from fractions import Fraction as Q
from .experiment import doppler,beta_from_ratio,receptions

class RelativisticDopplerTests(unittest.TestCase):
    def test_known_cases_and_reciprocity(self):
        self.assertEqual(doppler(0)['ratio'],1)
        self.assertAlmostEqual(doppler(.6)['ratio'],.5)
        self.assertAlmostEqual(doppler(-.6)['ratio'],2)
        self.assertAlmostEqual(doppler(.6)['z'],1)
        self.assertAlmostEqual(doppler(-.6)['z'],-.5)
        for i in range(-18,19):
            b=i/20;q=doppler(b)
            self.assertAlmostEqual(q['ratio']*doppler(-b)['ratio'],1)
            self.assertAlmostEqual(q['ratio'],q['gamma']*(1-b))
            self.assertAlmostEqual(beta_from_ratio(q['ratio']),b)

    def test_pulse_and_lorentz_references(self):
        for b,gamma in ((Q(3,5),Q(5,4)),(Q(4,5),Q(5,3)),(Q(5,13),Q(13,12)),(Q(-3,5),Q(5,4))):
            period=1/((1-b)*gamma)
            self.assertAlmostEqual(doppler(float(b))['ratio'],float(1/period),places=13)
            q=receptions(float(b))
            self.assertAlmostEqual(q['x0'],3+float(b)*q['t0'],places=12)
            self.assertAlmostEqual(q['x1'],3+float(b)*q['t1'],places=12)
            self.assertAlmostEqual(q['dt_prime'],float(period),places=12)
            self.assertAlmostEqual(q['dx_prime'],0,places=12)
            self.assertAlmostEqual(q['dt']**2-q['dx']**2,q['dt_prime']**2,places=11)

    def test_collinear_composition_and_observables(self):
        for a in (-.6,0,.3,.8):
            for b in (-.5,0,.4):
                combined=(a+b)/(1+a*b)
                self.assertAlmostEqual(doppler(combined)['ratio'],doppler(a)['ratio']*doppler(b)['ratio'])
        for b in (-.8,-.3,0,.3,.8):
            q=doppler(b)
            self.assertAlmostEqual(q['ratio']*q['wavelength_ratio'],1)
            self.assertAlmostEqual(q['proper_period'],q['arrival_period']/q['gamma'])

    def test_invalid_inputs(self):
        for value in (True,1,-1,2,float('nan'),float('inf'),'0.6'):
            with self.assertRaises(ValueError):doppler(value)
        for value in (True,0,-1,float('nan'),float('inf'),'1'):
            with self.assertRaises(ValueError):beta_from_ratio(value)
