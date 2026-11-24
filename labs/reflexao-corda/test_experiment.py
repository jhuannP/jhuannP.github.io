import unittest
from math import sqrt
from .experiment import pulse,pulse_prime,evaluate,total_energy,A,WIDTH,MU

def simpson(fn,a,b,n=4000):
    h=(b-a)/n
    return h/3*(fn(a)+fn(b)+4*sum(fn(a+i*h) for i in range(1,n,2))+2*sum(fn(a+i*h) for i in range(2,n,2)))

class StringReflectionTests(unittest.TestCase):
    def test_profile_direction_initial_data_and_pde(self):
        self.assertEqual(pulse(0),A)
        for x in (-2,-1,0):
            r=evaluate(0,x,0)
            self.assertEqual(r['reflected'],0)
            self.assertEqual(r['total'],pulse(x+2))
            self.assertEqual(r['velocity'],-pulse_prime(x+2))
        for c in (1,sqrt(2),2):
            x,t,h=-.23,2/c,1e-5
            for end in (0,1):
                f=lambda x,t:evaluate(end,x,t,c)['total']
                dtt=(f(x,t+h)-2*f(x,t)+f(x,t-h))/h**2
                dxx=(f(x+h,t)-2*f(x,t)+f(x-h,t))/h**2
                self.assertAlmostEqual(dtt,c*c*dxx,delta=5e-6)
        h=1e-6
        self.assertAlmostEqual((pulse(.13+h)-pulse(.13-h))/(2*h),pulse_prime(.13),places=9)

    def test_boundary_conditions_and_signed_reflection(self):
        for c in (1,sqrt(2),2):
            for t in (0,1/c,1.75/c,2/c,2.25/c,3/c):
                fixed=evaluate(0,0,t,c);free=evaluate(1,0,t,c)
                self.assertAlmostEqual(fixed['total'],0,places=14)
                self.assertAlmostEqual(fixed['velocity'],0,places=14)
                self.assertAlmostEqual(free['slope'],0,places=14)
                self.assertAlmostEqual(fixed['power'],0,places=14)
                self.assertAlmostEqual(free['power'],0,places=14)
            self.assertAlmostEqual(evaluate(1,0,2/c,c)['total'],2*A)
            self.assertAlmostEqual(evaluate(0,-1,3/c,c)['total'],-A)
            self.assertAlmostEqual(evaluate(1,-1,3/c,c)['total'],A)

    def test_energy_from_independent_quadrature(self):
        for c in (1,2):
            expected=total_energy(c)
            for end in (0,1):
                for t in (0,1.75/c,2/c,2.25/c,4/c):
                    measured=simpson(lambda x:evaluate(end,x,t,c)['density'],-8,0)
                    self.assertAlmostEqual(measured,expected,delta=1e-11)
        # Em colisão fixa, deslocamento zero não implica ausência de energia.
        self.assertEqual(evaluate(0,-.25,2)['total'],0)
        self.assertGreater(evaluate(0,-.25,2)['density'],0)

    def test_support_timing_and_domain(self):
        for c in (1,2):
            self.assertEqual(evaluate(0,0,1.4/c,c)['incident'],0)
            self.assertGreater(evaluate(0,0,1.75/c,c)['incident'],0)
        self.assertEqual(pulse(WIDTH),0);self.assertEqual(pulse_prime(WIDTH),0)
        self.assertAlmostEqual(total_energy(2),4*total_energy(1))
        for args in [(2,0,0,1),(0,.1,0,1),(0,0,-1,1),(0,0,1,0),(0,0,1,float('nan'))]:
            with self.assertRaises(ValueError):evaluate(*args)

if __name__=='__main__':unittest.main()
