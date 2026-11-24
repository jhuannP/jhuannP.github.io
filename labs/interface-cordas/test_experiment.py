import unittest
from fractions import Fraction as F
from .experiment import model,field,coefficients,A,WIDTH

def simpson(f,a,b,n=2048):
    h=(b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))

class StringInterface(unittest.TestCase):
    def test_exact_coefficients_and_matching(self):
        for ratio in range(2,9):
            q=F(ratio,4);r=(1-q)/(1+q);tau=2/(1+q)
            c=coefficients(ratio)
            self.assertAlmostEqual(c['r'],float(r));self.assertAlmostEqual(c['tau'],float(tau))
            self.assertEqual(r*r+q*tau*tau,1)
            for i in range(21):
                t=1.5+i/20;l=field('left',0,t,ratio);rr=field('right',0,t,ratio)
                for key in ['y','velocity','slope','power']:self.assertAlmostEqual(l[key],rr[key],places=12)

    def test_energy_independent_quadrature(self):
        # Integrate the full kinetic+elastic density over both physical half-lines.
        for ratio in range(2,9):
            for t in [0,1.5,1.75,2,2.25,2.5,3.5,5]:
                r=model(ratio,t)
                left=simpson(lambda x:field('left',x,t,ratio)['density'],-4,0)
                right=simpson(lambda x:field('right',x,t,ratio)['density'],0,7)
                self.assertAlmostEqual(left/r['energy0'],r['energy_left']/r['energy0'],delta=2e-7)
                self.assertAlmostEqual(right/r['energy0'],r['energy_right']/r['energy0'],delta=2e-7)
                self.assertAlmostEqual((left+right)/r['energy0'],1,delta=3e-7)
        integral=36*F(2)*(F(1,3)-F(4,5)+F(6,7)-F(4,9)+F(1,11))
        self.assertEqual(integral,F(1024,385))

    def test_pde_by_finite_differences(self):
        h=1e-4
        for ratio in range(2,9):
            for side,x,t in [('left',-.2,1.7),('left',-.2,2.1),('right',.1,2.15),('right',.3,2.4)]:
                c=coefficients(ratio);f=lambda xx,tt:field(side,xx,tt,ratio)['y']
                dtt=(f(x,t+h)-2*f(x,t)+f(x,t-h))/h**2
                dxx=(f(x+h,t)-2*f(x,t)+f(x-h,t))/h**2
                speed=c['c1'] if side=='left' else c['c2']
                self.assertAlmostEqual(dtt,speed**2*dxx,delta=2e-6)

    def test_limits_and_contracts(self):
        self.assertEqual(coefficients(4)['r'],0)
        self.assertAlmostEqual(coefficients(2)['tau'],4/3)
        self.assertAlmostEqual(coefficients(2)['transmission'],8/9)
        self.assertAlmostEqual(coefficients(8)['r'],-1/3)
        self.assertEqual(model(8,0)['energy_right'],0)
        self.assertAlmostEqual(model(8,2)['energy_right']/model(8,2)['energy0'],4/9)
        for args in [(1,2),(9,2),(True,2),(4,-1),(4,6),(4,True),(4,'x')]:
            with self.assertRaises(ValueError):model(*args)
        with self.assertRaises(ValueError):field('left',1,2)
