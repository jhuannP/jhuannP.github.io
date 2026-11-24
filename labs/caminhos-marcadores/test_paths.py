import unittest
from fractions import Fraction as Q
from .paths import amplitudes,probabilities,marker,norm2

class PathsTests(unittest.TestCase):
    def test_fixtures(self):
        self.assertEqual(marker(Q(1,3)),(Q(4,5),Q(3,5)))
        self.assertEqual(probabilities(Q(1,3)),(Q(9,10),Q(1,10)))
        self.assertEqual(probabilities(Q(1,3),(-1,0)),(Q(1,10),Q(9,10)))
        self.assertEqual(probabilities(0),(1,0));self.assertEqual(probabilities(1),(Q(1,2),Q(1,2)))

    def test_marginals_and_visibility(self):
        for i in range(21):
            t=Q(i,20);g,h=marker(t)
            self.assertEqual(g*g+h*h,1)
            for c,s in ((1,0),(0,1),(-1,0),(0,-1),(Q(3,5),Q(4,5))):
                plus,minus=probabilities(t,(c,s))
                self.assertEqual(plus,(1+g*c)/2)
                self.assertEqual(minus,(1-g*c)/2)
                self.assertTrue(0<=plus<=1 and 0<=minus<=1)
            high=probabilities(t)[0];low=probabilities(t,(-1,0))[0]
            self.assertEqual((high-low)/(high+low),g)

    def test_global_phase_and_orthogonal_marker(self):
        # Rotação complexa global não muda probabilidades conjuntas.
        c,s=Q(3,5),Q(4,5)
        for t in (0,Q(1,3),1):
            for a,b in amplitudes(t,(Q(3,5),Q(4,5))):
                self.assertEqual(norm2((c*a-s*b,s*a+c*b)),a*a+b*b)
        for phase in ((1,0),(0,1),(-1,0),(Q(3,5),Q(4,5))):
            a=amplitudes(1,phase)
            self.assertEqual(tuple(norm2(z) for z in a),(Q(1,4),)*4)

    def test_contracts(self):
        for t in (True,0.5,-1,2):
            with self.assertRaises(ValueError):probabilities(t)
        for phase in ((0,0),(1,1),(True,0),(1.0,0),(1,)):
            with self.assertRaises(ValueError):probabilities(0,phase)
