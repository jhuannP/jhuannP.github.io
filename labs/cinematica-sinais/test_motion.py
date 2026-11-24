import unittest
from fractions import Fraction as Q
from .motion import state,interval


class MotionTests(unittest.TestCase):
    def test_original_example(self):
        self.assertEqual(state(3),dict(x=Q(21,2),v=Q(5),a=Q(1)))
        result=interval(0,3)
        self.assertEqual(result['mean_velocity'],Q(7,2))
        self.assertEqual(result['distance'],Q(21,2))

    def test_reversal_and_repeated_position(self):
        self.assertEqual(state(3,v0=6,a=-2)['v'],0)
        self.assertEqual(state(3,v0=6,a=-2)['x'],9)
        self.assertEqual(state(2,v0=6,a=-2)['x'],8)
        self.assertEqual(state(4,v0=6,a=-2)['x'],8)
        self.assertEqual(state(2,v0=6,a=-2)['v'],2)
        self.assertEqual(state(4,v0=6,a=-2)['v'],-2)
        self.assertEqual(interval(0,6,v0=6,a=-2),dict(displacement=Q(0),distance=Q(18),mean_velocity=Q(0),mean_speed=Q(3)))

    def test_distance_against_fine_polygonal_path(self):
        # Integer v0 and |a|<=4 => any nonzero turning time is on a 1/12 s grid.
        # The fine path recovers the exact total variation without the lab's split.
        for v0 in range(-4,5):
            for a in range(-4,5):
                points=[state(Q(i,12),v0=v0,a=a)['x'] for i in range(73)]
                oracle=sum(abs(right-left) for left,right in zip(points,points[1:]))
                result=interval(0,6,v0=v0,a=a)
                self.assertEqual(result['distance'],oracle)
                self.assertGreaterEqual(oracle,abs(result['displacement']))
                v_start,v_end=Q(v0),Q(v0+6*a)
                self.assertEqual(result['mean_velocity'],(v_start+v_end)/2)

    def test_distance_additivity_and_origin(self):
        for a in [-2,0,2]:
            whole=interval(0,6,x0=17,v0=6,a=a)
            for cut in [Q(1,3),Q(3),Q(17,3)]:
                first=interval(0,cut,x0=17,v0=6,a=a)
                last=interval(cut,6,x0=17,v0=6,a=a)
                self.assertEqual(whole['distance'],first['distance']+last['distance'])
                self.assertEqual(whole['displacement'],first['displacement']+last['displacement'])
            self.assertEqual(whole,interval(0,6,x0=-23,v0=6,a=a))

    def test_velocity_squared_relation_and_units(self):
        for v0,a,t in [(6,-2,Q(4)),(-3,-1,Q(1,2)),(0,0,Q(3)),(2,3,Q(2,3))]:
            p=state(t,x0=7,v0=v0,a=a)
            self.assertEqual(p['v']**2-v0**2,2*a*(p['x']-7))
            centimeters=state(t,x0=700,v0=100*v0,a=100*a)
            self.assertEqual(centimeters['x']/100,p['x'])
            self.assertEqual(centimeters['v']/100,p['v'])
        self.assertEqual(interval(1,3,v0=0,a=0)['distance'],0)

    def test_contracts(self):
        for value in [True,1.0,'2',None]:
            with self.assertRaises(ValueError):state(value)
            with self.assertRaises(ValueError):state(1,a=value)
        with self.assertRaises(ValueError):state(-1)
        for t0,t1 in [(1,1),(2,1),(-1,3)]:
            with self.assertRaises(ValueError):interval(t0,t1)

if __name__=='__main__':unittest.main()
