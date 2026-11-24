import unittest
from fractions import Fraction as F
from math import comb
from .waves import coefficients,mean_power,pulse,field,wall


class WaveTests(unittest.TestCase):
    def test_literal_coefficients_and_powers(self):
        self.assertEqual(coefficients(2,6),dict(r=F(-1,2),tau=F(1,2),R=F(1,4),transmission=F(3,4)))
        self.assertEqual(coefficients(6,2)['tau'],F(3,2))
        self.assertEqual(mean_power(2,4,F(1,100)),F(1,625))
        self.assertEqual(mean_power(2,4,F(1,200)),F(1,2500))
        self.assertEqual(mean_power(6,4,F(1,200)),F(3,2500))

    def test_interface_conditions(self):
        for z1 in [1,2,3,6]:
            for z2 in [1,2,3,6]:
                c=coefficients(z1,z2)
                self.assertEqual(1+c['r'],c['tau'])
                self.assertEqual(z1*(1-c['r']),z2*c['tau'])
                self.assertEqual(c['R']+c['transmission'],1)
                self.assertTrue(0<=c['R']<=1 and 0<=c['transmission']<=1)
                self.assertEqual(coefficients(z2,z1)['R'],c['R'])
        self.assertEqual(coefficients(2,2)['r'],0)

    def test_boundaries_and_instantaneous_flux(self):
        for z1,z2 in [(2,6),(6,2),(2,2)]:
            for i in range(17):
                t=F(1,3)+F(i-8,160)
                a=field('left',0,t,z1,z2);b=field('right',0,t,z1,z2)
                self.assertEqual(a['y'],b['y']);self.assertEqual(a['yt'],b['yt'])
                self.assertEqual(18*a['yx'],18*b['yx'])
                self.assertEqual(a['flux'],b['flux'])
                self.assertEqual(wall('fixed',t)['y'],0)
                self.assertEqual(wall('fixed',t)['yt'],0)
                self.assertEqual(wall('free',t)['yx'],0)
        self.assertEqual(wall('free',F(1,3))['y'],F(1,50))

    def test_pulse_derivative(self):
        width=F(1,20);h=F(1,10**8)
        for u in [F(-3,4),F(-1,2),0,F(1,4),F(3,4)]:
            t=u*width;value,d=pulse(t,width)
            finite_difference=(pulse(t+h,width)[0]-pulse(t-h,width)[0])/(2*h)
            self.assertLess(abs(d-finite_difference),F(1,10**8))
            self.assertGreaterEqual(value,0)
        for u in [-2,-1,1,2]:self.assertEqual(pulse(u*width,width),(0,0))

    def test_separated_pulse_energy(self):
        # Independent integral of [d(1-u^2)^3/du]^2 as an expanded polynomial.
        C=36*sum((F(2*(-1)**j*comb(4,j),2*j+3) for j in range(5)),F(0))
        incident_energy=2*F(1,100)**2*C/F(1,20)
        # Independent spatial quadrature of actual kinetic+elastic energy densities.
        # At t=0 incident support [-3.45,-2.55]; at 2/3 reflected there, transmitted [.85,1.15].
        def integrate(side,t,lo,hi,n=128):
            h=(hi-lo)/n
            return h/3*(field(side,lo,t)['density']+field(side,hi,t)['density']+
                        sum((4 if i%2 else 2)*field(side,lo+i*h,t)['density'] for i in range(1,n)))
        inc=integrate('left',0,F(-69,20),F(-51,20))
        ref=integrate('left',F(2,3),F(-69,20),F(-51,20))
        trans=integrate('right',F(2,3),F(17,20),F(23,20))
        self.assertLess(abs(inc-incident_energy),F(1,10**8))
        self.assertLess(abs(ref-incident_energy/4),F(1,10**8))
        self.assertLess(abs(trans-3*incident_energy/4),F(1,10**8))
        self.assertLess(abs(inc-ref-trans),F(1,10**8))

    def test_contracts(self):
        for a,b in [(0,2),(-1,2),(True,2),(2,6.0)]:
            with self.assertRaises(ValueError):coefficients(a,b)
        for kwargs in [dict(tension=0),dict(width=0),dict(amplitude=-1)]:
            with self.assertRaises(ValueError):field('left',0,0,**kwargs)
        with self.assertRaises(ValueError):field('left',1,0)
        with self.assertRaises(ValueError):field('right',-1,0)
        with self.assertRaises(ValueError):wall('unknown',0)

if __name__=='__main__':unittest.main()
