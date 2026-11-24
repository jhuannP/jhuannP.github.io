"""Sistema cinético sintético. Frações de metal; tempo em s e taxas em s^-1.
Solução completa versus aproximação de ordem dominante: sem ajuste a dados.
"""
from math import exp, expm1, sqrt, isfinite, ceil
import unittest


def real(x, positive=False):
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not isfinite(x):
        raise ValueError('Real finito necessário')
    if x < 0 or (positive and x == 0): raise ValueError('Valor fora do domínio')
    return float(x)


def rates(a, b, c):
    return real(a, True), real(b), real(c, True)


def full(t, a=.02, b=2., c=3.):
    t = real(t); a, b, c = rates(a, b, c)
    total = a+b+c
    # Discriminante escrito como soma não negativa.
    gap = sqrt((a-c)**2+b*b+2*b*(a+c))
    if gap == 0:
        z = a*t*exp(-a*t)
        y = -expm1(-a*t)-z
    else:
        fast = (total+gap)/2
        slow = 2*a*c/(total+gap)
        z = a*exp(-slow*t)*(-expm1(-gap*t))/gap
        y = (-fast*expm1(-slow*t)+slow*expm1(-fast*t))/gap
    return 1-z-y, z, y


def rhs(state, a, b, c):
    x, z, y = state
    return -a*x+b*z, a*x-(b+c)*z, c*z


def reduced_product(t, a=.02, b=2., c=3.):
    t=real(t); a,b,c=rates(a,b,c)
    return -expm1(-a*c/(b+c)*t)


def rk4(t, a, b, c):
    # Solução numérica das três EDOs, sem usar as taxas próprias ou fórmula fechada.
    t=real(t); a,b,c=rates(a,b,c)
    n=max(1,ceil(t*max(a+b+c,1)*20)); h=t/n
    state=(1.,0.,0.)
    advance=lambda s,k,f:tuple(x+f*h*v for x,v in zip(s,k))
    for _ in range(n):
        k1=rhs(state,a,b,c); k2=rhs(advance(state,k1,.5),a,b,c)
        k3=rhs(advance(state,k2,.5),a,b,c); k4=rhs(advance(state,k3,1),a,b,c)
        state=tuple(x+h*(p+2*q+2*r+s)/6 for x,p,q,r,s in zip(state,k1,k2,k3,k4))
    return state


class Checks(unittest.TestCase):
    def test_full_against_independent_rk4(self):
        cases=((.02,2.,3.), (1.,0.,1.), (1.,1.,1.), (.02,.2,.3))
        for a,b,c in cases:
            for t in (0.,.1,1.,10.):
                exact=full(t,a,b,c); numeric=rk4(t,a,b,c)
                for u,v in zip(exact,numeric): self.assertAlmostEqual(u,v,delta=1e-7)
                self.assertAlmostEqual(sum(numeric),1.,delta=1e-12)
                self.assertGreaterEqual(min(exact),-1e-12)

    def test_differential_equations_and_initial_layer(self):
        for t in (.1,.5,2.,10.):
            h=1e-5
            derivative=tuple((u-v)/(2*h) for u,v in zip(full(t+h),full(t-h)))
            for u,v in zip(derivative,rhs(full(t),.02,2.,3.)):
                self.assertAlmostEqual(u,v,delta=1e-9)
        self.assertEqual(full(0.),(1.,0.,0.))
        self.assertEqual(rhs(full(0.),.02,2.,3.)[2],0)
        self.assertAlmostEqual(reduced_product(1e-7)/1e-7,.012,delta=1e-9)

    def test_degenerate_and_long_time_limits(self):
        for t in (0.,.1,1.,5.):
            x,z,y=full(t,1.,0.,1.)
            self.assertAlmostEqual(x,exp(-t))
            self.assertAlmostEqual(z,t*exp(-t))
            self.assertAlmostEqual(y,1-(1+t)*exp(-t))
        x,z,y=full(10000.)
        self.assertAlmostEqual(y,1.)
        self.assertAlmostEqual(x+z,0.)

    def test_rate_competition_and_approximation(self):
        a,b,c=.02,2.,3.
        self.assertAlmostEqual(c/(b+c),3/5)
        self.assertAlmostEqual(a*c/(b+c),.012)
        self.assertAlmostEqual(a*(2*c)/(b+2*c)/(.012),5/4)
        self.assertAlmostEqual(a*c/(2*b+c),3/350)
        # Erros observados, sem elevar a amostra a cota geral de aproximação.
        for t in (1.,10.,100.):
            error=abs(full(t)[2]-reduced_product(t))
            print('t(s)=',t,'; erro absoluto no produto=',error)
            self.assertLess(error,.004)
        self.assertGreater(abs(full(.1,2.,2.,3.)[2]-reduced_product(.1,2.,2.,3.)),.05)

    def test_contracts(self):
        for t in (-1.,True,float('nan')):
            with self.assertRaises(ValueError): full(t)
        for params in ((0,2,3),(.02,-1,3),(.02,2,0)):
            with self.assertRaises(ValueError): full(1,*params)


if __name__ == '__main__':
    unittest.main()
