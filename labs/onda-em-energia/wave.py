"""Solução analítica em unidades normalizadas: eps=1, mu=1/4, c=2."""
from math import cos, pi
from itertools import product
import unittest

EPS, MU, C, E0, K = 1., .25, 2., 6., 1.
OMEGA = C*K


def fields(z,t,direction=1,flip_b=False):
    if direction not in (-1,1):
        raise ValueError('Direção +1 ou -1')
    e=E0*cos(K*z-direction*OMEGA*t)
    b=direction*e/C
    if flip_b:b=-b
    return (e,0.,0.),(0.,b,0.)


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])


def energy_flux(z,t,direction=1):
    e,b=fields(z,t,direction)
    ue=EPS*sum(x*x for x in e)/2
    ub=sum(x*x for x in b)/(2*MU)
    s=tuple(x/MU for x in cross(e,b))
    return ue,ub,s


def derivative(f,x,h):
    if h<=0:raise ValueError('Passo positivo')
    return (f(x+h)-f(x-h))/(2*h)


def residuals(z,t,h,direction=1,flip_b=False):
    ex=lambda zz,tt:fields(zz,tt,direction,flip_b)[0][0]
    by=lambda zz,tt:fields(zz,tt,direction,flip_b)[1][1]
    faraday=derivative(lambda zz:ex(zz,t),z,h)+derivative(lambda tt:by(z,tt),t,h)
    ampere=-derivative(lambda zz:by(zz,t),z,h)-MU*EPS*derivative(lambda tt:ex(z,tt),t,h)
    return faraday,ampere


def conservation_residual(z,t,h,direction=1):
    u=lambda tt:sum(energy_flux(z,tt,direction)[:2])
    s=lambda zz:energy_flux(zz,t,direction)[2][2]
    return derivative(u,t,h)+derivative(s,z,h)


class Checks(unittest.TestCase):
    def test_orientation_energy_identity(self):
        self.assertAlmostEqual(C,1/(EPS*MU)**.5)
        for direction,z,t in product((-1,1),(-1.,0.,.4),(0.,.2,.7)):
            e,b=fields(z,t,direction)
            ue,ub,s=energy_flux(z,t,direction)
            self.assertAlmostEqual(ue,ub)
            self.assertAlmostEqual(s[2],direction*C*(ue+ub))
            self.assertGreaterEqual(direction*s[2],0)
            self.assertEqual(s[:2],(0.,0.))
            self.assertAlmostEqual(sum(x*y for x,y in zip(e,b)),0.)
        self.assertEqual(cross((2,0,0),(0,3,0)),(0,0,6))

    def test_period_averages(self):
        period=2*pi/OMEGA
        for n,z,direction in product((8,16,64),(.0,.37),(-1,1)):
            samples=[fields(z,period*(i+.5)/n,direction)[0][0] for i in range(n)]
            self.assertAlmostEqual(sum(samples)/n,0.,places=12)
            self.assertAlmostEqual(sum(e*e for e in samples)/n,18.,places=12)
            flux=sum(energy_flux(z,period*(i+.5)/n,direction)[2][2] for i in range(n))/n
            self.assertAlmostEqual(flux,direction*36.,places=11)
        self.assertEqual(energy_flux(0,0),(18.,18.,(0.,0.,72.)))

    def test_finite_difference_refinement(self):
        errors=[]
        for h in (.1,.05,.025):
            errors.append(max(abs(x) for z,t,d in product((.17,.43,.91),(.11,.37),(-1,1))
                              for x in (*residuals(z,t,h,d),conservation_residual(z,t,h,d))))
        self.assertLess(errors[1],errors[0]/3.8)
        self.assertLess(errors[2],errors[1]/3.8)
        print('Máximos resíduos amostrados:',errors)
        # Finite differences approximate derivatives, not the exact solution itself.

    def test_reversing_only_B_breaks_maxwell(self):
        good=max(map(abs,residuals(.37,.11,.0001)))
        bad=max(map(abs,residuals(.37,.11,.0001,flip_b=True)))
        self.assertLess(good,1e-6)
        self.assertGreater(bad,1.)
        with self.assertRaises(ValueError):derivative(cos,0,0)
        with self.assertRaises(ValueError):fields(0,0,0)


if __name__=='__main__':
    unittest.main()
