import unittest
from fractions import Fraction as Q
from .contact import contact

class ContactTests(unittest.TestCase):
    def model(self,f,v):return contact(4,10,f,Q(1,2),Q(3,10),v)
    def test_rest_threshold_and_start(self):
        for f in range(-20,21):
            a=self.model(f,0)
            self.assertEqual(a['friction'],-f);self.assertEqual(a['acceleration'],0)
        self.assertEqual(self.model(24,0)['acceleration'],3)
        self.assertEqual(self.model(-24,0)['acceleration'],-3)
        self.assertEqual(self.model(20,0)['status'],'repouso admissível')
    def test_sliding_depends_on_velocity(self):
        self.assertEqual(self.model(10,1)['friction'],-12)
        self.assertEqual(self.model(10,1)['acceleration'],Q(-1,2))
        self.assertEqual(self.model(10,-1)['friction'],12)
        self.assertEqual(self.model(10,-1)['acceleration'],Q(11,2))
        self.assertEqual(self.model(0,0)['friction'],0)
        self.assertEqual(self.model(0,6)['acceleration'],-3)
        self.assertEqual(Q(6,3),2) # Frenagem só até v=0.
        self.assertEqual(Q(1,2)*4*6**2,12*6)
    def test_243_reflections_and_dissipation(self):
        for f in range(-40,41):
            for v in (-2,0,2):
                a=self.model(f,v);b=self.model(-f,-v)
                self.assertEqual(a['friction'],-b['friction'])
                self.assertEqual(a['acceleration'],-b['acceleration'])
                self.assertLessEqual(a['friction_power'],0)
                self.assertEqual(a['normal'],40)
        a=contact(4,10,0,0,0,1);self.assertEqual(a['friction'],0)
    def test_contracts(self):
        for args in [(0,10,1,1,1,0),(4,-1,1,1,1,0),(4,10,1,0,1,0),(4,10,1,1,1,True),(4,10,1,.5,0,0)]:
            with self.assertRaises(ValueError):contact(*args)
