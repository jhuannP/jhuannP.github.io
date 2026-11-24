import unittest
from fractions import Fraction as Q
from .motion import velocity,primitive,travel

class MotionTests(unittest.TestCase):
    def test_original_and_nonlinear_reference(self):
        a=travel(0,2)
        self.assertEqual(a['changes'],(-1,1))
        self.assertEqual(a['distance'],2);self.assertEqual(a['displacement'],0)
        self.assertEqual(a['average_speed'],1)
        c=travel(0,4,'cubic')
        self.assertEqual(c['changes'],(-Q(11,12),-Q(4,3),Q(43,12)))
        self.assertEqual(c['displacement'],Q(4,3));self.assertEqual(c['distance'],Q(35,6))
        self.assertEqual(c['average_velocity'],Q(1,3));self.assertEqual(c['average_speed'],Q(35,24))

    def test_independent_simpson_integration(self):
        # Simpson é exato para cúbicas; integra |v| após separar seus zeros.
        for model in ('linear','cubic'):
            v=(lambda t:2*t-2) if model=='linear' else (lambda t:t**3-5*t*t+7*t-3)
            for ia in range(17):
                for ib in range(ia,17):
                    a,b=Q(ia,4),Q(ib,4)
                    cuts=[a]+[t for t in (Q(1),Q(3)) if a<t<b]+[b]
                    expected=Q(0);distance=Q(0)
                    for left,right in zip(cuts,cuts[1:]):
                        mid=(left+right)/2
                        expected+=(right-left)*(v(left)+4*v(mid)+v(right))/6
                        distance+=(right-left)*(abs(v(left))+4*abs(v(mid))+abs(v(right)))/6
                    result=travel(a,b,model)
                    self.assertEqual(result['displacement'],expected)
                    self.assertEqual(result['distance'],distance)

    def test_additivity_and_bound(self):
        for model in ('linear','cubic'):
            for a,b,c in ((0,1,4),(0,Q(5,2),4),(Q(1,3),Q(4,3),Q(11,3))):
                left,right,whole=travel(a,b,model),travel(b,c,model),travel(a,c,model)
                for key in ('displacement','distance'):
                    self.assertEqual(left[key]+right[key],whole[key])
                self.assertGreaterEqual(whole['distance'],abs(whole['displacement']))

    def test_touching_zero_does_not_reverse(self):
        for e in (Q(1,10),Q(1,100),Q(1,1000)):
            self.assertLess(velocity(1-e,'cubic'),0)
            self.assertLess(velocity(1+e,'cubic'),0)
            self.assertLess(velocity(3-e,'cubic'),0)
            self.assertGreater(velocity(3+e,'cubic'),0)
        self.assertEqual(velocity(1,'cubic'),0)
        self.assertEqual(velocity(3,'cubic'),0)

    def test_origin_invariance_and_axis_reversal(self):
        for model in ('linear','cubic'):
            for origin in (-7,0,11):
                self.assertEqual((origin+primitive(4,model))-(origin+primitive(0,model)),travel(0,4,model)['displacement'])
            out=travel(0,4,model)
            self.assertEqual(sum(abs(-c) for c in out['changes']),out['distance'])

    def test_contracts_and_zero_duration(self):
        for value in (True,1.0,'1'):
            with self.assertRaises(ValueError):travel(value,4)
        for a,b in ((-1,4),(3,2)):
            with self.assertRaises(ValueError):travel(a,b)
        for f in (velocity,primitive):
            with self.assertRaises(ValueError):f(1,'other')
        with self.assertRaises(ValueError):travel(0,4,'other')
        z=travel(1,1,'cubic')
        self.assertEqual(z['distance'],0);self.assertEqual(z['displacement'],0)
        self.assertIsNone(z['average_velocity']);self.assertIsNone(z['average_speed'])
