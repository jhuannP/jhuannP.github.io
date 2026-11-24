import unittest
from fractions import Fraction as Q
from .experiment import motion,floor_normal

class FrameTests(unittest.TestCase):
    def test_coordinate_and_force_identities(self):
        for m in (1,2,4):
            for F in (-4,0,4):
                for A in (-2,0,2):
                    for t in (0,Q(1,2),2):
                        r=motion(m,F,A,t,x0=3,v0=-1,X0=2,V0=1)
                        self.assertEqual(r['relative_x'],r['x']-r['X'])
                        self.assertEqual(r['relative_a'],Q(F,m)-A)
                        self.assertEqual(m*r['relative_a'],r['effective_force'])
                        self.assertEqual(r['effective_force'],F+r['inertial_force'])
        r=motion(2,6,1,2)
        self.assertEqual((r['x'],r['X'],r['relative_x']),(6,2,4))

    def test_acceleration_from_exact_second_difference(self):
        for A in (-2,0,2):
            for F in (-3,0,3):
                h=Q(1,10);t=Q(1)
                left=motion(2,F,A,t-h)['relative_x']
                mid=motion(2,F,A,t)['relative_x']
                right=motion(2,F,A,t+h)['relative_x']
                self.assertEqual((right-2*mid+left)/(h*h),Q(F,2)-A)
        self.assertEqual(motion(2,0,1,2)['relative_x'],-2)
        self.assertEqual(motion(2,2,1,2)['relative_x'],0)

    def test_inertial_translation_and_floor_contact(self):
        r=motion(2,4,0,3,v0=2,V0=7)
        self.assertEqual(r['relative_a'],r['a'])
        self.assertEqual(r['relative_v'],r['v']-7)
        self.assertEqual(r['inertial_force'],0)
        self.assertEqual(floor_normal(2,10,2),24)
        self.assertEqual(floor_normal(2,10,-2),16)
        self.assertEqual(floor_normal(2,10,-10),0)

    def test_contracts(self):
        for args in ((0,1,1,1),(-1,1,1,1),(1,1,1,-1),(True,1,1,1),(1,.5,1,1)):
            with self.assertRaises(ValueError):motion(*args)
        with self.assertRaises(ValueError):floor_normal(2,10,-11)
        with self.assertRaises(ValueError):floor_normal(2,0,1)

if __name__=='__main__':unittest.main()
