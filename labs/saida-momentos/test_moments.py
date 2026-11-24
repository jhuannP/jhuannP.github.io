import unittest
from fractions import Fraction as Q
from .moments import moments,continuous

class MomentTests(unittest.TestCase):
    def test_fixture_counterexample(self):
        c=continuous(1,2,Q(1,2));self.assertEqual(c['mean'],1);self.assertEqual(c['variance'],Q(2,3))
        for m,v in ((2,0),(4,Q(1,2)),(8,Q(5,8))):
            a=moments(2,Q(1,2),m);self.assertEqual(a['mean'][m//2],1);self.assertEqual(a['variance'][m//2],v)
        self.assertEqual(moments(2,Q(1,2),2)['dt'],1)
    def test_closed_forms_and_recurrences(self):
        for length in (1,2,3):
            for D in (Q(1,2),1,2):
                for m in range(2,21):
                    a=moments(length,D,m);dt=a['dt']
                    for i in range(1,m):
                        c=continuous(Q(i*length,m),length,D);t=a['mean'][i];s=a['second'][i]
                        self.assertEqual(t,c['mean']);self.assertEqual(a['right'][i],c['right'])
                        self.assertEqual(t,dt+(a['mean'][i-1]+a['mean'][i+1])/2)
                        self.assertEqual(s,dt*dt+dt*(a['mean'][i-1]+a['mean'][i+1])+(a['second'][i-1]+a['second'][i+1])/2)
                        self.assertEqual(s,c['second']-Q(2,3)*dt*t)
                        self.assertGreaterEqual(a['variance'][i],0)
    def test_scaling(self):
        a=moments(2,1,6);b=moments(4,1,6);c=moments(2,2,6)
        for i in range(7):
            self.assertEqual(b['mean'][i],4*a['mean'][i]);self.assertEqual(b['variance'][i],16*a['variance'][i])
            self.assertEqual(c['mean'][i],a['mean'][i]/2);self.assertEqual(c['variance'][i],a['variance'][i]/4)
    def test_contracts(self):
        for args in [(0,1,4),(2,0,4),(True,1,4),(2,1,True),(2,1,1),(2,1,41),(2.0,1,4)]:
            with self.assertRaises(ValueError):moments(*args)
        with self.assertRaises(ValueError):continuous(3,2,1)
