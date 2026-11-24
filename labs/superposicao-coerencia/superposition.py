"""Poço infinito: posição u e tempo tau normalizados; duas componentes."""
from math import sin,cos,sqrt,pi,isfinite
from cmath import exp
from itertools import product
import unittest


def validate(w):
    if isinstance(w,bool) or not isinstance(w,(int,float)) or not isfinite(w) or not 0<=w<=1:
        raise ValueError('Peso finito entre0 e1')


def phi(n,u):
    return sqrt(2)*sin(n*pi*u)


def amplitude(w,tau,u,relative_phase=0.):
    validate(w)
    return sqrt(w)*phi(1,u)*exp(-1j*tau)+sqrt(1-w)*phi(2,u)*exp(-4j*tau+1j*relative_phase)


def expanded(w,tau,u):
    validate(w)
    a,b=phi(1,u),phi(2,u)
    return w*a*a+(1-w)*b*b+2*sqrt(w*(1-w))*a*b*cos(3*tau)


def mixture(w,u):
    validate(w)
    return w*phi(1,u)**2+(1-w)*phi(2,u)**2


def integrate(f,a=0.,b=1.,n=256):
    if isinstance(n,bool) or not isinstance(n,int) or n<=0 or n%2:
        raise ValueError('Número par positivo de subintervalos')
    h=(b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if k%2 else 2)*f(a+k*h) for k in range(1,n)))


def left_probability(w,tau):
    validate(w)
    return .5+2*sqrt(w*(1-w))*4/(3*pi)*cos(3*tau)


class Checks(unittest.TestCase):
    def test_complex_vs_expanded(self):
        for w,t,u in product((0.,.25,.5,.75,1.),(0.,pi/9,pi/3,2*pi/3,1.2),
                             (k/100 for k in range(101))):
            density=abs(amplitude(w,t,u))**2
            self.assertGreaterEqual(density,0.)
            self.assertAlmostEqual(density,expanded(w,t,u),places=12)

    def test_integrals_and_energy(self):
        for w,t in product((0.,.25,.5,.75,1.),(0.,pi/9,pi/3,2*pi/3,1.2)):
            rho=lambda u:abs(amplitude(w,t,u))**2
            self.assertAlmostEqual(integrate(rho),1.,places=10)
            self.assertAlmostEqual(integrate(rho,b=.5),left_probability(w,t),places=8)
            # H/E1 multiplies basis amplitudes by1 and4 independently.
            hpsi=lambda u:sqrt(w)*phi(1,u)*exp(-1j*t)+4*sqrt(1-w)*phi(2,u)*exp(-4j*t)
            expectation=integrate(lambda u:amplitude(w,t,u).conjugate()*hpsi(u))
            self.assertAlmostEqual(expectation.real,4-3*w,places=10)
            self.assertAlmostEqual(expectation.imag,0.,places=10)
        self.assertAlmostEqual(left_probability(.5,0),.9244131815783876)
        self.assertAlmostEqual(left_probability(.5,pi/3),.0755868184216124)

    def test_global_phase_mixture_and_boundaries(self):
        for u,t,w in product((.13,.25,.73),(0.,.7),(0.,.5,1.)):
            psi=amplitude(w,t,u)
            self.assertAlmostEqual(abs(psi*exp(.37j))**2,abs(psi)**2,places=12)
            mean=sum(abs(amplitude(w,0,u,2*pi*k/16))**2 for k in range(16))/16
            self.assertAlmostEqual(mean,mixture(w,u),places=12)
            if w in (0.,1.):self.assertAlmostEqual(expanded(w,t,u),mixture(w,u),places=12)
        for u in (0.,1.):self.assertLess(abs(amplitude(.5,.7,u)),1e-14)

    def test_contracts(self):
        for w in (-.1,1.1,True,float('nan'),float('inf')):
            with self.assertRaises(ValueError):amplitude(w,0,.5)
        for n in (0,3,True,2.5):
            with self.assertRaises(ValueError):integrate(lambda x:x,n=n)


if __name__=='__main__':
    print('P esquerda coerente:',left_probability(.5,0),left_probability(.5,pi/3))
    print('P esquerda mistura:',integrate(lambda u:mixture(.5,u),b=.5))
    unittest.main()
