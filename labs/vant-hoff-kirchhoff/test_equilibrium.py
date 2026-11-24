import unittest
from math import exp,log
from .equilibrium import R,log_ratio,equilibrium,integrand

def simpson(f,a,b,n=2000):
    h=(b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))

class VantHoffTests(unittest.TestCase):
    def test_original_fixture(self):
        self.assertAlmostEqual(log_ratio(400,300,1200*R),1,places=14)
        self.assertAlmostEqual(equilibrium(400,300,1200*R,logK0=log(2))['K'],2*exp(1),places=13)
        self.assertAlmostEqual(log_ratio(400,300,1200*R,4*R),1+4*(log(4/3)-.25),places=14)
        self.assertEqual(log_ratio(300,300,1200*R,4*R),0)

    def test_quadrature_and_reference_change(self):
        for T in (220.,300.,400.,700.):
            for H0 in (-10000.,0.,10000.):
                for Cp in (-20.,0.,20.):
                    f=lambda t:integrand(t,300.,H0,Cp)
                    self.assertAlmostEqual(log_ratio(T,300.,H0,Cp),simpson(f,300.,T),places=10)
                    H1=H0+Cp*(400-300)
                    self.assertAlmostEqual(log_ratio(400,300,H0,Cp)+log_ratio(T,400,H1,Cp),log_ratio(T,300,H0,Cp),places=12)

    def test_derivative_and_reverse_reaction(self):
        for T in (250.,350.,500.):
            for Cp in (-20.,0.,20.):
                h=.001;H0=10000.
                derivative=(log_ratio(T+h,300,H0,Cp)-log_ratio(T-h,300,H0,Cp))/(2*h)
                self.assertAlmostEqual(derivative,integrand(T,300,H0,Cp),places=10)
                forward=equilibrium(T,300,H0,Cp,.7)
                backward=equilibrium(T,300,-H0,-Cp,-.7)
                self.assertAlmostEqual(forward['K']*backward['K'],1,places=12)

    def test_contracts(self):
        for args in ((True,300,10000),(25,300,10000),(400,0,10000),(400,300,float('nan')),(400,300,300000)):
            with self.assertRaises(ValueError):log_ratio(*args)
        with self.assertRaises(ValueError):equilibrium(400,300,10000,logK0=101)

if __name__=='__main__':unittest.main()
