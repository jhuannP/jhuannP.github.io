import unittest
from math import sqrt,pi,exp
from numerics import simpson
from .speed import component_density,speed_density,tails,scales,physical_speed_density


class MaxwellTests(unittest.TestCase):
    def test_reference_scales(self):
        r=scales(2,1)
        self.assertAlmostEqual(r['mode'],2);self.assertAlmostEqual(r['mean'],4/sqrt(pi));self.assertAlmostEqual(r['rms'],sqrt(6));self.assertEqual(r['mean_square'],6)
        self.assertLess(r['mode'],r['mean']);self.assertLess(r['mean'],r['rms'])
        self.assertEqual(speed_density(0),0)
        self.assertAlmostEqual(component_density(0),1/sqrt(2*pi))

    def test_independent_integrals_and_moments(self):
        mass=simpson(speed_density,0,8,4000)
        first=simpson(lambda u:u*speed_density(u),0,10,4000)
        second=simpson(lambda u:u*u*speed_density(u),0,8,4000)
        self.assertAlmostEqual(mass+tails(8)['probability'],1,places=11)
        self.assertAlmostEqual(first,sqrt(8/pi),places=10)
        self.assertAlmostEqual(second+tails(8)['second_moment'],3,places=10)
        self.assertAlmostEqual(simpson(component_density,-8,8,4000),1,places=11)
        self.assertAlmostEqual(simpson(lambda x:x*component_density(x),-8,8,4000),0,places=12)

    def test_tail_integration_and_geometry(self):
        for u in (1,2,4,8):
            prob=simpson(speed_density,u,12,6000)
            second=simpson(lambda z:z*z*speed_density(z),u,12,6000)
            self.assertAlmostEqual(prob,tails(u)['probability'],delta=2e-11)
            self.assertAlmostEqual(second,tails(u)['second_moment'],delta=2e-10)
            # Joint vector density from product of THREE independent component densities.
            joint=component_density(u)*component_density(0)**2
            self.assertAlmostEqual(4*pi*u*u*joint,speed_density(u),places=13)
        self.assertLess(tails(8)['probability'],1e-12)
        self.assertLess(tails(8)['second_moment'],1e-9)
        self.assertEqual(tails(0),dict(probability=1.,second_moment=3.))

    def test_scaling_and_mode(self):
        for theta,mass in ((1,1),(2,1),(.5,4),(10,3)):
            old=scales(theta,mass);hot=scales(4*theta,mass);heavy=scales(theta,4*mass)
            self.assertAlmostEqual(hot['mean'],2*old['mean'])
            self.assertAlmostEqual(heavy['mean'],old['mean']/2)
            for u in (.5,1,2,3):
                v=u*old['s']
                self.assertAlmostEqual(physical_speed_density(2*v,4*theta,mass),physical_speed_density(v,theta,mass)/2)
        h=1e-5;u=sqrt(2)
        derivative=(speed_density(u+h)-speed_density(u-h))/(2*h)
        self.assertAlmostEqual(derivative,0,places=8)
        self.assertGreater(speed_density(u),speed_density(u-.01));self.assertGreater(speed_density(u),speed_density(u+.01))

    def test_previous_challenge_and_contracts(self):
        T,m=1,1;mode=sqrt(2*T/m);mean=sqrt(8*T/(pi*m));rms=sqrt(3*T/m)
        self.assertTrue(mode<mean<rms)
        f=lambda v:4*pi*(1/(2*pi))**1.5*v*v*exp(-v*v/2)
        N=4000;h=8/N
        mass=h*sum(f((i+.5)*h) for i in range(N))
        second=h*sum(((i+.5)*h)**2*f((i+.5)*h) for i in range(N))
        self.assertLess(abs(mass-1),1e-9);self.assertLess(abs(second-3),1e-9)
        for x in (-1,33,True,float('nan'),'1'):
            with self.assertRaises(ValueError):speed_density(x)
        for theta,m in [(0,1),(1,-1),(1e5,1)]:
            with self.assertRaises(ValueError):scales(theta,m)
