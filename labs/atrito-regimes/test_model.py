import unittest
from fractions import Fraction as Q
from .model import state,coast

class FrictionTests(unittest.TestCase):
    def test_start_force_grid_and_threshold(self):
        for m in range(1,5):
            for F in range(-20,21):
                r=state(0,F,m=m)
                self.assertEqual(r['normal'],10*m)
                if abs(F)<=5*m:
                    self.assertEqual(r['friction'],-F);self.assertEqual(r['acceleration'],0)
                else:
                    self.assertEqual(abs(r['friction']),3*m)
                    self.assertGreater(r['acceleration']*F,0)
                self.assertEqual(m*r['acceleration'],F+r['friction'])
        self.assertEqual(state(0,10)['regime'],'estático')
        self.assertEqual(state(0,-10)['regime'],'estático')

    def test_relative_velocity_sets_direction(self):
        self.assertEqual(state(-3,6)['friction'],6)
        self.assertEqual(state(-3,6)['acceleration'],6)
        self.assertEqual(state(3,6)['acceleration'],0)
        for v in (-4,-1,1,4):
            for F in range(-12,13):
                r=state(v,F)
                self.assertLessEqual(r['friction']*v,0)
                self.assertEqual(r['friction'],-6 if v>0 else 6)

    def test_stop_event_and_rest(self):
        for dt,expected_v,expected_x in ((Q(1,2),Q(3,2),Q(9,8)),(1,0,Q(3,2)),(2,0,Q(3,2))):
            r=coast(3,dt);self.assertEqual(r['stop_time'],1)
            self.assertEqual(r['velocity'],expected_v);self.assertEqual(r['displacement'],expected_x)
        self.assertEqual(coast(0,2)['distance'],0)

    def test_semigroup_across_stop(self):
        for v in (-3,3):
            for a,b in ((Q(1,4),Q(1,4)),(Q(1,2),1),(2,1)):
                first=coast(v,a);second=coast(first['velocity'],b);whole=coast(v,a+b)
                self.assertEqual(first['displacement']+second['displacement'],whole['displacement'])
                self.assertEqual(first['distance']+second['distance'],whole['distance'])
                self.assertEqual(second['velocity'],whole['velocity'])

    def test_energy_reflection_and_zero_friction(self):
        for v in range(-3,4):
            for dt in (0,Q(1,4),Q(1,2),1,2):
                r=coast(v,dt);opposite=coast(-v,dt)
                self.assertEqual(r['delta_k'],r['work'])
                self.assertEqual(r['displacement'],-opposite['displacement'])
                self.assertEqual(r['distance'],opposite['distance'])
        r=coast(3,2,mk=0);self.assertIsNone(r['stop_time'])
        self.assertEqual(r['velocity'],3);self.assertEqual(r['distance'],6)

    def test_contracts(self):
        for invalid in (True,1.,'1'):
            with self.assertRaises(ValueError):state(invalid,1)
        for kwargs in ({'m':0},{'g':0},{'ms':-1},{'mk':1}):
            with self.assertRaises(ValueError):state(0,1,**kwargs)
        with self.assertRaises(ValueError):coast(1,-1)
