import unittest
from fractions import Fraction as Q
from itertools import product
from .experiment import state,landing_time

class ProjectileHeightTests(unittest.TestCase):
    def test_lesson_events(self):
        self.assertEqual((state(0)['y'],state(0)['vy']),(15,10))
        self.assertEqual((state(1)['x'],state(1)['y'],state(1)['vy']),(8,20,0))
        self.assertEqual((state(2)['x'],state(2)['y'],state(2)['vy']),(16,15,-10))
        self.assertEqual((state(3)['x'],state(3)['y'],state(3)['vy']),(24,0,-20))
        self.assertEqual(landing_time(),3)

    def test_energy_and_velocity_position_identities(self):
        for y0,vx,vy,g in product((0,3,15),(-4,0,8),(-3,0,10),(1,10)):
            e0=state(0,0,y0,vx,vy,g)['specific_energy']
            for t in (Q(0),Q(1,4),Q(1),Q(3)):
                s=state(t,0,y0,vx,vy,g)
                self.assertEqual(s['specific_energy'],e0)
                self.assertEqual(s['vy']**2,vy**2-2*g*(s['y']-y0))
                h=Q(1,10)
                a=state(t+h,0,y0,vx,vy,g)
                self.assertEqual((a['x']-s['x'])/h,vx)
                self.assertEqual((a['y']-s['y'])/h,s['vy']-g*h/2)

    def test_manufactured_ground_events(self):
        for g,T,vy in product((1,2,10),(1,2,3),(-10,0,1)):
            y0=Q(g*T*T,2)-vy*T
            if y0<=0:continue
            self.assertEqual(state(T,0,y0,4,vy,g)['y'],0)
            self.assertAlmostEqual(landing_time(y0,vy,g),T,places=12)
        self.assertEqual(landing_time(0,4,10),.8)
        self.assertEqual(landing_time(0,0,10),0)
        self.assertEqual(landing_time(0,-4,10),0)

    def test_translation_and_horizontal_reversal(self):
        for t in (0,1,2,3):
            a=state(t);b=state(t,7,15,-8,10,10)
            self.assertEqual(b['x'],7-a['x'])
            for key in ('y','vy','specific_energy'):self.assertEqual(a[key],b[key])

    def test_contract(self):
        for args in [(-1,), (True,), (1.,), (0,0,-1), (0,0,15,8,10,0)]:
            with self.assertRaises(ValueError):state(*args)
        for args in [(-1,1,10),(1,1,0),(1.,1,10)]:
            with self.assertRaises(ValueError):landing_time(*args)
