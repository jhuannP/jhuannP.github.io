from fractions import Fraction as Q
from itertools import product
import unittest
from .kinetic import energy_moments

def raw_uniform_moment(lo,hi,power):
    if lo==hi:return lo**power
    return (hi**(power+1)-lo**(power+1))/((power+1)*(hi-lo))

class NonlinearTests(unittest.TestCase):
    def test_example(self):
        s=energy_moments(2,2,Q(1,5))
        self.assertEqual(s['plug_in'],4)
        self.assertEqual(s['mean'],Q(301,75))
        self.assertEqual(s['input_variance'],Q(1,75))
        self.assertEqual(s['linear_variance'],Q(16,75))
        self.assertEqual(s['curvature_variance'],Q(4,28125))
        self.assertEqual(s['exact_variance'],Q(6004,28125))
        self.assertEqual(s['extra_over_linear'],Q(1,1500))

    def test_against_direct_polynomial_integration(self):
        for m,v,a in product((Q(1,2),Q(2),Q(5)),(Q(-3),Q(-1,5),Q(0),Q(1,5),Q(2)),(Q(0),Q(1,10),Q(1,5),Q(2))):
            mean=m*raw_uniform_moment(v-a,v+a,2)/2
            second=m*m*raw_uniform_moment(v-a,v+a,4)/4
            s=energy_moments(m,v,a)
            self.assertEqual(s['mean'],mean)
            self.assertEqual(s['exact_variance'],second-mean*mean)
            self.assertGreaterEqual(s['exact_variance'],s['linear_variance'])

    def test_zero_derivative_is_not_zero_variance(self):
        s=energy_moments(2,0,Q(1,5))
        self.assertEqual(s['linear_variance'],0)
        self.assertEqual(s['mean'],Q(1,75))
        self.assertEqual(s['exact_variance'],Q(4,28125))
        self.assertIsNone(s['extra_over_linear'])
        constant=energy_moments(2,2,0)
        self.assertEqual(constant['exact_variance'],0)
        self.assertEqual(constant['mean'],constant['plug_in'])

    def test_sign_mass_and_width_scaling(self):
        base=energy_moments(2,2,Q(1,5))
        self.assertEqual(energy_moments(2,-2,Q(1,5)),base)
        heavier=energy_moments(4,2,Q(1,5))
        self.assertEqual(heavier['mean'],2*base['mean'])
        self.assertEqual(heavier['exact_variance'],4*base['exact_variance'])
        narrower=energy_moments(2,2,Q(1,10))
        self.assertEqual(narrower['linear_variance'],base['linear_variance']/4)
        self.assertEqual(narrower['curvature_variance'],base['curvature_variance']/16)

    def test_contracts(self):
        for i in range(3):
            for bad in (True,0.,'0',None):
                args=[2,2,Q(1,5)];args[i]=bad
                with self.assertRaises(ValueError):energy_moments(*args)
        for m,a in ((0,1),(-1,1),(2,-1)):
            with self.assertRaises(ValueError):energy_moments(m,0,a)

if __name__=='__main__':unittest.main()
