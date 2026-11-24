import unittest,itertools
from fractions import Fraction as Q
from .trace import trace

class TraceTests(unittest.TestCase):
    def test_fixture_censoring(self):
        a=trace(3,[('G',10),('S',4),('G',5)])
        self.assertEqual(a['points'],[(0,3),(10,5),(14,3),(19,4)])
        self.assertEqual(a['catastrophe_rate'],Q(1,15));self.assertEqual(a['rescue_rate'],Q(1,4))
        self.assertEqual(a['catastrophes'],1);self.assertEqual(a['rescues'],1)
        b=trace(3,[('G',10)])
        self.assertEqual(b['catastrophes'],0);self.assertEqual(b['catastrophe_rate'],0)
        self.assertIsNone(b['rescue_rate'])
    def test_enumeration_and_units(self):
        for durations in itertools.product((1,2,3),repeat=3):
            for first in ('G','S'):
                states=[first,'S' if first=='G' else 'G',first]
                segments=list(zip(states,durations));a=trace(10,segments)
                direct=Q(10)+sum((Q(1,5) if s=='G' else -Q(1,2))*t for s,t in segments)
                self.assertEqual(a['points'][-1],(sum(durations),direct))
                self.assertEqual(sum(a['exposure'].values()),sum(durations))
                self.assertEqual(a['catastrophes']+a['rescues'],2)
                # Reexpressar tempo em unidade 2x mais fina: duração dobra e velocidade divide por2.
                b=trace(10,[(s,2*t) for s,t in segments],Q(1,10),Q(1,4))
                self.assertEqual(a['points'][-1][1],b['points'][-1][1])
                for key in ('catastrophe_rate','rescue_rate'):
                    self.assertEqual(b[key],a[key]/2)
    def test_boundary(self):
        self.assertEqual(trace(1,[('S',2)])['points'][-1][1],0)
        for seg in [[('S',3)],[('S',2),('G',1)]]:
            with self.assertRaises(ValueError):trace(1,seg)
    def test_contracts(self):
        for initial,seg in [(0,[('G',1)]),(True,[('G',1)]),(3,[]),(3,[('X',1)]),(3,[('G',0)]),(3,[('G',1.0)]),(3,[('G',1),('G',2)])]:
            with self.assertRaises(ValueError):trace(initial,seg)
