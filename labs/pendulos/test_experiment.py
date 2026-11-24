import math
import unittest
from .experiment import period_ratio,period,physical_length

class PendulumTests(unittest.TestCase):
    def test_against_independent_quadrature(self):
        # Simpson na integral suave, sem usar AGM como referência.
        N=4096;h=(math.pi/2)/N
        for degrees in (0,1,10,30,60,90,150):
            k=math.sin(math.radians(degrees)/2)
            f=lambda u:1/math.sqrt(1-k*k*math.sin(u)**2)
            integral=h/3*(f(0)+f(math.pi/2)+sum((4 if j%2 else 2)*f(j*h) for j in range(1,N)))
            self.assertAlmostEqual(period_ratio(math.radians(degrees)),2*integral/math.pi,places=11)

    def test_scaling_and_small_amplitude(self):
        self.assertEqual(period_ratio(0),1)
        previous=1
        for degrees in range(1,151):
            ratio=period_ratio(math.radians(degrees));self.assertGreater(ratio,previous);previous=ratio
        for length in (.25,1,4):
            for g in (1,10,20):
                a=period(length,g,.5);b=period(4*length,g,.5);c=period(length,4*g,.5)
                self.assertAlmostEqual(b['nonlinear'],2*a['nonlinear'])
                self.assertAlmostEqual(c['nonlinear'],a['nonlinear']/2)
        x=.001
        self.assertAlmostEqual((period_ratio(x)-1)/x**2,1/16,places=7)

    def test_physical_rod_and_mass_cancellation(self):
        for mass in (.5,2,10):
            for length in (.5,1.5,3):
                equivalent=physical_length(mass*length**2/3,mass,length/2)
                self.assertAlmostEqual(equivalent,2*length/3)
        self.assertAlmostEqual(physical_length(1.5,2,.75),1)
        self.assertAlmostEqual(period_ratio(math.pi/2),1.1803405990160962)

    def test_invalid_inputs(self):
        for theta in (-1,math.pi,math.inf,math.nan,True,'0'):
            with self.assertRaises(ValueError):period_ratio(theta)
        for value in (0,-1,math.inf,math.nan,False):
            with self.assertRaises(ValueError):period(value,10,.1)
            with self.assertRaises(ValueError):physical_length(1,1,value)
