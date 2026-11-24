import unittest
from math import exp,pi,isclose,log
from decimal import Decimal,localcontext
from .experiment import fraction,disk,half_light_ratio

class ExponentialDiskTests(unittest.TestCase):
    def test_independent_simpson_and_tiny_decimal(self):
        for x in (.1,1,2,4,8):
            n=4000;step=x/n
            integral=step/3*(x*exp(-x)+sum((4 if k%2 else 2)*(k*step)*exp(-k*step) for k in range(1,n)))
            self.assertLess(abs(fraction(x)-integral),1e-11)
        with localcontext() as ctx:
            ctx.prec=70
            for text in ['0.000000000001','0.00000001','0.001']:
                x=Decimal(text);expected=1-(1+x)*(-x).exp()
                self.assertTrue(isclose(fraction(float(x)),float(expected),rel_tol=1e-13))

    def test_units_scaling_and_aperture(self):
        q=disk(2,3,6);self.assertAlmostEqual(q['total'],36*pi)
        self.assertAlmostEqual(q['fraction'],1-3*exp(-2))
        for I,h,R in [(1,.5,0),(2,3,6),(5,4,16)]:
            q=disk(I,h,R);scaled=disk(I,2*h,2*R)
            self.assertAlmostEqual(scaled['total'],4*q['total']);self.assertAlmostEqual(scaled['fraction'],q['fraction'])
            self.assertAlmostEqual(disk(2*I,h,R)['enclosed'],2*q['enclosed'])
        # Converter densidade por pc² e comprimentos em kpc: fator de área 10^6.
        self.assertAlmostEqual(disk(2*10**6,3,6)['total'],disk(2,3000,6000)['total'])

    def test_monotonicity_derivative_half_light(self):
        xs=[i/10 for i in range(101)];fs=[fraction(x) for x in xs]
        self.assertEqual(fs[0],0);self.assertTrue(all(a<b for a,b in zip(fs,fs[1:])))
        self.assertLess(fs[-1],1);self.assertAlmostEqual(fraction(100),1)
        for x in (.1,1,2,4):
            h=1e-5;d=(fraction(x+h)-fraction(x-h))/(2*h)
            self.assertTrue(isclose(d,x*exp(-x),rel_tol=1e-8))
        r=half_light_ratio();self.assertLess(abs(fraction(r)-.5),1e-14)
        self.assertTrue(1.67834<r<1.67835)
        self.assertNotAlmostEqual(fraction(log(2)),.5)

    def test_domain(self):
        for args in [(0,1,1),(1,0,1),(1,1,-1),(1,float('inf'),1),(float('nan'),1,1)]:
            with self.assertRaises(ValueError):disk(*args)
        for x in (-1,float('nan'),float('inf')):
            with self.assertRaises(ValueError):fraction(x)

if __name__=='__main__':unittest.main()
