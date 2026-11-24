import unittest,itertools
from fractions import Fraction as F
from .experiment import model

class ForceBalanceTests(unittest.TestCase):
    def test_exact_constant_acceleration_reference(self):
        for m,r,l,v0,t in itertools.product((1,3,6),(0,6,12),(0,6,12),(-4,0,4),(0,1,3)):
            s=model(m,r,l,v0,t);a=F(r-l,m);v=F(v0)+a*t;x=F(v0)*t+a*t*t/2
            for key,ref in (('force',r-l),('a',a),('v',v),('x',x)):
                self.assertAlmostEqual(s[key],float(ref),delta=1e-12)
            self.assertEqual(s['normal']-s['weight'],0)
    def test_impulse_and_work_energy(self):
        for m,r,l,v0,t in itertools.product((1,3,6),(0,6,12),(0,6,12),(-4,0,4),(0,1,3)):
            s=model(m,r,l,v0,t)
            self.assertAlmostEqual(s['impulse'],m*(s['v']-v0),delta=1e-11)
            self.assertAlmostEqual(s['work'],s['delta_k'],delta=1e-11)
            self.assertAlmostEqual(model(m,r,l,0,t)['a'],s['a'])
    def test_turn_is_not_a_permanent_stop(self):
        s=model(3,12,6,-2,1);self.assertEqual(s['v'],0);self.assertEqual(s['a'],2);self.assertEqual(s['turn'],1)
        self.assertEqual(model()['v'],2);self.assertEqual(model()['x'],0)
        for v in (-4,0,4):
            s=model(3,6,6,v,3);self.assertEqual(s['v'],v);self.assertEqual(s['x'],3*v);self.assertIsNone(s['turn'])
        self.assertEqual(model(3,6,12,2,3)['a'],-2)
    def test_domains(self):
        for args in ((0,1,1,0,0),(1,-1,1,0,0),(1,1,-1,0,0),(1,1,1,0,-1),(True,1,1,0,0),(1,1,1,float('nan'),0)):
            with self.assertRaises(ValueError):model(*args)
