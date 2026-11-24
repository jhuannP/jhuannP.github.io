import itertools
import unittest
from fractions import Fraction as F
from .throttle import state,throttle,entropy_change

class ThrottleTests(unittest.TestCase):
    def test_landmarks(self):
        for d,t2 in ((-1,F(59,60)),(0,F(1)),(1,F(61,60))):
            a,b=throttle(1,F(1,10),F(1,20),d)
            self.assertEqual(b['tau'],t2);self.assertEqual(a['h'],b['h'])
            self.assertGreater(entropy_change(a,b),0)

    def test_independent_flow_work(self):
        # Balanço por u e trabalho de fluxo, sem reutilizar h para montar o oráculo.
        for t,p1,ratio,d,c in itertools.product((F(1),F(2)),(F(1,10),F(1,5)),(F(1,2),F(1,3)),(-1,0,1),(F(2),F(3))):
            p2=p1*ratio;a,b=throttle(t,p1,p2,d,c)
            U1=(c-1)*t;V1=t/p1+d
            U2=(c-1)*b['tau'];V2=b['tau']/p2+d
            self.assertEqual(U2-U1,p1*V1-p2*V2)
            self.assertGreater(entropy_change(a,b),0)

    def test_derivatives_and_path_composition(self):
        h=F(1,1000)
        for d in (-1,0,1):
            a,b=throttle(1,F(1,5),F(1,10),d)
            _,end=throttle(b['tau'],b['pi'],F(1,20),d)
            _,direct=throttle(1,F(1,5),F(1,20),d)
            self.assertEqual(end,direct)
            # Deriva v em tau por diferença exata e verifica a identidade termodinâmica.
            dv=(state(1+h,F(1,5),d)['v']-state(1-h,F(1,5),d)['v'])/(2*h)
            self.assertEqual((dv-a['v'])/a['c'],a['mu'])

    def test_free_expansion_is_not_throttling(self):
        for d in (-1,0,1):
            a=state(1,F(1,10),d);b=state(1,F(1,20),d)
            self.assertEqual(a['u'],b['u'])
            self.assertEqual(b['h']-a['h'],F(d)*F(-1,20))

    def test_contracts(self):
        for args in ((0,F(1,10),0,3),(1,0,0,3),(1,F(1,10),0,1),(1,1,-2,3)):
            with self.assertRaises(ValueError):state(*args)
        for t in (True,1.0,'1'):
            with self.assertRaises(ValueError):state(t,F(1,10),0)
        with self.assertRaises(ValueError):throttle(1,F(1,10),F(1,5),0)
