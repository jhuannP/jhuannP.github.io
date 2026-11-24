import unittest
from fractions import Fraction as Q
from .events import arrival, frequency

class DopplerTests(unittest.TestCase):
    def test_event_geometry(self):
        # Direct worldline position of the crest vs observer, 75 events.
        for us in (-90,-30,0,30,90):
            for uo in (-90,-30,0,30,90):
                for n in (0,1,5):
                    te=Q(n,20);ta=arrival(n,300,20,120,us,uo)
                    crest=us*te+300*(ta-te)
                    receiver=120+uo*ta
                    self.assertEqual(crest,receiver)
                    self.assertGreater(ta,te)
                    self.assertEqual(1/(arrival(n+1,300,20,120,us,uo)-ta),frequency(300,20,us,uo))
    def test_independent_crest_spacing(self):
        # At time t=1, positions of crests 0,1,2 give wavelength directly.
        for us in (-60,0,60):
            positions=[us*Q(n,20)+300*(1-Q(n,20)) for n in range(3)]
            spacing=positions[0]-positions[1]
            self.assertEqual(positions[1]-positions[2],spacing)
            for uo in (-30,0,30):
                self.assertEqual(frequency(300,20,us,uo),(300-uo)/spacing)
    def test_landmarks(self):
        self.assertEqual([arrival(n,300,20,120,60,-30) for n in range(3)],[Q(4,11),Q(2,5),Q(24,55)])
        self.assertEqual(frequency(300,20,60,-30),Q(55,2))
        self.assertEqual(frequency(300,20,90,0),Q(200,7))
        self.assertNotEqual(frequency(300,20,60,-30),frequency(300,20,90,0))
        for u in (-60,0,60): self.assertEqual(frequency(300,20,u,u),20)
    def test_distance_not_period(self):
        for distance in (60,120,240):
            a=arrival(0,300,20,distance,60,-30)
            b=arrival(1,300,20,distance,60,-30)
            self.assertEqual(b-a,Q(2,55))
            self.assertEqual(a,Q(distance,330))
    def test_contracts(self):
        for args in [(0,20),(300,0),(300,20,300,0),(300,20,0,-300),(300.0,20),(True,20)]:
            with self.assertRaises(ValueError): frequency(*args)
        for args in [(-1,300,20,120),(True,300,20,120),(1,300,20,0),(10,300,20,1,60,-30)]:
            with self.assertRaises(ValueError): arrival(*args)

if __name__=='__main__': unittest.main()
