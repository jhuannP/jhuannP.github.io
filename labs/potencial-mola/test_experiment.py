from fractions import Fraction as F
from math import cos,sin
import unittest
from .experiment import inspect

class PotentialTests(unittest.TestCase):
    def test_work_integral_and_offset(self):
        # Integral of linear F is exactly the trapezoid area; independent of U code.
        for q in range(-150,151,5):
            x=F(q,100); work=(F(0)-8*x)*x/2
            for c in range(-10,11):
                s=inspect(q,c)
                self.assertEqual(s['u']-c,-work)
                self.assertEqual(s['difference'],4+work)
                self.assertEqual(s['allowed'],abs(x)<=1)
                self.assertEqual(s['force'],-8*x)
                if s['allowed']: self.assertAlmostEqual(s['speed']**2,float(4+work),places=12)
                else: self.assertIsNone(s['speed']);self.assertIsNone(s['kinetic'])

    def test_exact_turns_and_negative_energy(self):
        for q in [-100,100]:
            s=inspect(q,-10);self.assertTrue(s['allowed']);self.assertEqual(s['speed'],0)
            self.assertNotEqual(s['force'],0)
        self.assertEqual(inspect(0,-10)['e'],-6)
        self.assertEqual(inspect(0,-10)['speed'],2)
        self.assertEqual(inspect(50)['kinetic'],3)
        self.assertFalse(inspect(101)['allowed'])

    def test_newton_trajectory_energy(self):
        # Exact solution of x''=-4x, not integration of the energy equation.
        for i in range(201):
            t=i/20;x=cos(2*t);v=-2*sin(2*t)
            self.assertAlmostEqual(v*v+4*x*x,4,places=12)
        # Both signs of v obey the same energy, including at x=0.
        for v in [-2,2]:self.assertEqual(v*v,4)

    def test_contracts(self):
        for q in [-151,151,True,1.5,None,'0']:
            with self.assertRaises(ValueError):inspect(q,0)
        for c in [-11,11,False,.5,None]:
            with self.assertRaises(ValueError):inspect(0,c)
