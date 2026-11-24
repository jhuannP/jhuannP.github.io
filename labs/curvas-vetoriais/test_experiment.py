import unittest
from fractions import Fraction as Q
from .experiment import state

class CurveTests(unittest.TestCase):
    def test_against_polynomial_coefficients(self):
        polynomials={0:([0,1],[0,0,1]),1:([0,0,0,1],[0,0,0,0,0,0,1]),2:([0,-1],[0,0,1])}
        def evaluate(c,t):return sum(Q(v)*t**i for i,v in enumerate(c))
        def derivative(c):return [i*v for i,v in enumerate(c)][1:]
        for mode,coordinates in polynomials.items():
            for t in (Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1)):
                r=state(mode,t)
                for i,c in enumerate(coordinates):
                    self.assertEqual(r['position'][i],evaluate(c,t))
                    self.assertEqual(r['velocity'][i],evaluate(derivative(c),t))
                    self.assertEqual(r['acceleration'][i],evaluate(derivative(derivative(c)),t))

    def test_same_image_and_chain_factor(self):
        for t in (Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1)):
            original=state(0,t**3);cube=state(1,t)
            self.assertEqual(cube['position'],original['position'])
            self.assertEqual(cube['velocity'],tuple(3*t*t*v for v in original['velocity']))
            reverse=state(2,-t);base=state(0,t)
            self.assertEqual(reverse['position'],base['position'])
            self.assertEqual(reverse['velocity'],tuple(-v for v in base['velocity']))

    def test_regular_and_stationary_parameter(self):
        self.assertTrue(state(0,0)['regular'])
        self.assertFalse(state(1,0)['regular'])
        self.assertEqual(state(1,0)['speed_squared'],0)
        for mode in range(3):
            for t in (Q(-1),Q(1,2),Q(1)):
                r=state(mode,t)
                self.assertTrue(r['regular'])
                self.assertEqual(r['position'][1],r['position'][0]**2)
                self.assertEqual(r['position'][2],0)
                self.assertGreater(r['speed_squared'],0)
        self.assertEqual(state(0,Q(1,2))['speed_squared'],2)

    def test_contracts(self):
        for mode in (True,3,-1):
            with self.assertRaises(ValueError):state(mode,0)
        for t in (True,.5,float('nan')):
            with self.assertRaises(ValueError):state(0,t)

if __name__=='__main__':unittest.main()
