"""Pacote na reta em hbar=1,x0=0; quadratura truncada e derivada aproximada."""
from math import exp,sqrt,pi,isfinite
from cmath import exp as cexp
from itertools import product
import unittest


def real(x):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x):
        raise ValueError('Real finito necessário')
    return float(x)


def parameters(s,k,p0):
    s,k,p0=map(real,(s,k,p0))
    if s<=0:raise ValueError('s positivo')
    return s,k,p0


def psi(x,s,k,p0):
    return (2*pi*s*s)**(-.25)*exp(-x*x/(4*s*s))*cexp(1j*(p0*x+k*x*x/(4*s*s)))


def integral(f,a,b,n):
    h=(b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))


def estimate(s,k,p0,h,n=512):
    s,k,p0=parameters(s,k,p0)
    h=real(h)
    if h<=0 or isinstance(n,bool) or not isinstance(n,int) or n<2 or n%2:
        raise ValueError('Passo positivo e número par de subintervalos')
    f=lambda x:psi(x,s,k,p0)
    rho=lambda x:abs(f(x))**2
    mom=lambda x:-1j*(f(x+h)-f(x-h))/(2*h)
    integrate=lambda g:integral(g,-8*s,8*s,n)
    norm=integrate(rho)
    mx=integrate(lambda x:x*rho(x))/norm
    vx=integrate(lambda x:(x-mx)**2*rho(x))/norm
    mp=integrate(lambda x:f(x).conjugate()*mom(x))/norm
    p2=integrate(lambda x:abs(mom(x))**2)/norm
    vp=p2-mp.real**2
    return norm,mx,vx,mp,vp,sqrt(vx*vp)


class Checks(unittest.TestCase):
    def test_normalization_and_position(self):
        for s,k,p0 in product((.5,1.,2.),(0.,1.),(0.,.75)):
            norm,mx,vx,mp,vp,prod=estimate(s,k,p0,.005*s)
            self.assertAlmostEqual(norm,1.,places=11)
            self.assertAlmostEqual(mx,0.,places=11)
            self.assertAlmostEqual(vx,s*s,places=10)
            self.assertLess(abs(mp.imag),1e-10)

    def test_momentum_refinement(self):
        errors=[]
        for ratio in (.02,.01,.005):
            err=0.
            for s,k,p0 in product((.5,1.,2.),(0.,1.),(0.,.75)):
                norm,mx,vx,mp,vp,prod=estimate(s,k,p0,ratio*s)
                expected=(1+k*k)/(4*s*s)
                err=max(err,abs(mp.real-p0),abs(vp-expected))
            errors.append(err)
        self.assertLess(errors[1],errors[0]/3.8)
        self.assertLess(errors[2],errors[1]/3.8)
        self.assertLess(errors[-1],.0002)
        print('Resíduos máximos de momentos:',errors)

    def test_phase_and_analytic_examples(self):
        for s,x in product((.5,1.,2.),(-2.,-.3,0.,1.2)):
            self.assertAlmostEqual(abs(psi(x,s,0,0))**2,abs(psi(x,s,1,.75))**2,places=12)
        self.assertEqual(1/(2*2),.25)
        self.assertEqual((1+1)/(4*2**2),.125)
        minimum=estimate(2,0,0,.01)[-1]
        chirped=estimate(2,1,0,.01)[-1]
        self.assertAlmostEqual(minimum,.5,places=4)
        self.assertAlmostEqual(chirped,sqrt(2)/2,places=4)
        print('Produtos numéricos:',minimum,chirped,'versus analíticos:',.5,sqrt(2)/2)

    def test_contracts(self):
        for args in ((0,0,0),(-1,0,0),(True,0,0),(1,float('nan'),0)):
            with self.assertRaises(ValueError):estimate(*args,.01)
        for h,n in ((0,512),(.01,3),(.01,True)):
            with self.assertRaises(ValueError):estimate(1,0,0,h,n)


if __name__=='__main__':
    unittest.main()
