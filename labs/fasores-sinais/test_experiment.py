import math
import unittest
from itertools import product
from .experiment import signal, derivative, polar

class PhasorTests(unittest.TestCase):
    def test_superposition_and_interference_identity(self):
        values=[complex(a,b) for a,b in product((-3,0,2),repeat=2)]
        for z,w in product(values,repeat=2):
            expected=abs(z)**2+abs(w)**2+2*(z*w.conjugate()).real
            self.assertAlmostEqual(abs(z+w)**2,expected,places=10)
            for t in (-1,0,.3,2):
                self.assertAlmostEqual(signal(z+w,2,t),signal(z,2,t)+signal(w,2,t),places=11)

    def test_coordinates_polar_and_zero(self):
        for a,b in product((-4,-1,0,3),repeat=2):
            z=complex(a,b);amplitude,phase=polar(z)
            self.assertAlmostEqual(amplitude**2,a*a+b*b,places=11)
            if z:
                self.assertAlmostEqual(amplitude*math.cos(phase),a,places=11)
                self.assertAlmostEqual(amplitude*math.sin(phase),b,places=11)
            else:self.assertIsNone(phase)
        self.assertEqual(polar(0),(0,None))
        self.assertIsNotNone(polar(1e-12j)[1])

    def test_sign_derivative_and_time_origin(self):
        z=3+4j
        self.assertEqual(signal(z,2,0),3)
        self.assertEqual(derivative(z,2,0),-8)
        self.assertAlmostEqual(signal(z,2,math.pi/4),-4,places=12)
        for t in (-.5,0,.7):
            h=1e-5
            diff=(signal(z,2,t+h)-signal(z,2,t-h))/(2*h)
            self.assertAlmostEqual(diff,derivative(z,2,t),places=7)
            shift=.3;angle=2*shift
            shifted=z*complex(math.cos(angle),math.sin(angle))
            self.assertAlmostEqual(signal(shifted,2,t),signal(z,2,t+shift),places=12)

    def test_lesson_sum_and_distinct_frequencies(self):
        z=(3+4j)+(-3+4j)
        self.assertEqual(z,8j)
        self.assertEqual(polar(z),(8,math.pi/2))
        self.assertEqual(derivative(z,2,0),-16)
        actual=signal(1,1,math.pi)+signal(1,2,math.pi)
        wrong=signal(2,1,math.pi)
        self.assertAlmostEqual(actual,0,places=12)
        self.assertAlmostEqual(wrong,-2,places=12)

    def test_contract(self):
        for z,omega,t in [(True,2,0),(complex(float('nan'),0),2,0),(1,0,0),(1,-1,0),(1,True,0),(1,2,float('inf')),(1,1e308,1e308)]:
            with self.assertRaises(ValueError):signal(z,omega,t)
        with self.assertRaises(ValueError):polar(float('inf'))
