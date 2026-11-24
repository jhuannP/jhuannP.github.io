import unittest,itertools
from fractions import Fraction as F
from .experiment import comparison

class BrakingIntervalTests(unittest.TestCase):
    def test_velocity_area_independent_of_position_formula(self):
        for v,b in itertools.product(range(1,21),range(1,6)):
            stop=F(v,b)
            for t in (F(0),stop/2,stop,stop+1,F(25)):
                m=comparison(v,b,t)
                # Área do trapézio até min(t,ts), sem usar a fórmula de posição.
                dt=min(t,stop);vf=v-b*dt
                self.assertEqual(m['position'],(F(v)+vf)*dt/2)
                self.assertEqual(m['velocity'],vf)
                self.assertEqual(m['continued_position'],(F(v)+m['continued_velocity'])*t/2)
                self.assertGreaterEqual(m['continued_distance'],abs(m['continued_position']))
    def test_join_continuity_one_sided_slopes_and_waiting(self):
        for v,b in itertools.product((1,10,20),(1,2,5)):
            ts=F(v,b);h=ts/10
            left=comparison(v,b,ts-h);middle=comparison(v,b,ts);right=comparison(v,b,ts+h)
            self.assertEqual(middle['velocity'],0);self.assertIsNone(middle['acceleration'])
            self.assertEqual((middle['velocity']-left['velocity'])/h,-b)
            self.assertEqual((right['velocity']-middle['velocity'])/h,0)
            self.assertEqual(right['position'],middle['position'])
            self.assertEqual(comparison(v,b,2*ts)['average_acceleration'],-F(b,2))
    def test_models_agree_until_stop_then_diverge(self):
        for v,b in itertools.product(range(1,21),range(1,6)):
            ts=F(v,b)
            for t in (F(0),ts/2,ts):
                m=comparison(v,b,t);self.assertEqual(m['position'],m['continued_position']);self.assertEqual(m['velocity'],m['continued_velocity'])
            later=comparison(v,b,2*ts)
            self.assertEqual(later['continued_position'],0)
            self.assertEqual(later['continued_distance'],2*later['distance'])
            self.assertEqual(later['velocity'],0);self.assertEqual(later['continued_velocity'],-v)
    def test_signs_scaling_zero_initial_and_contracts(self):
        # Aceleração negativa pode aumentar a rapidez quando v também é negativa.
        self.assertGreater(abs(F(-2)+F(-1)*2),abs(F(-2)))
        for v,b in itertools.product((1,10,20),(1,2,5)):
            a=comparison(v,b,0);twice=comparison(2*v,b,0)
            self.assertEqual(twice['stop'],2*a['stop']);self.assertEqual(twice['distance'],4*a['distance'])
            self.assertIsNone(a['average_acceleration'])
        z=comparison(0,2,0);self.assertEqual(z['phase'],'parado');self.assertEqual(z['acceleration'],0)
        for args in [(-1,2,0),(1,0,0),(1,2,-1),(True,2,0),(1,.5,0),(1,2,None)]:
            with self.assertRaises(ValueError):comparison(*args)
