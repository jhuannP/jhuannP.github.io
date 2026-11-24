"""Órbita circular sintética; código opcional de aprofundamento."""
from math import sqrt, pi, hypot, sin, cos, isfinite
import unittest


def real(x, positive=False):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x):
        raise ValueError('Real finito necessário')
    if x<0 or (positive and x==0):raise ValueError('Valor fora do domínio')
    return float(x)


def circular(mu, radius, altitude, mass):
    mu=real(mu,True);radius=real(radius,True)
    altitude=real(altitude);mass=real(mass,True)
    try:
        r=radius+altitude
        g=mu/r**2;v=sqrt(mu/r);period=2*pi*r/v
        result={'r':r,'g':g,'force':mass*g,'v':v,'period':period}
    except (OverflowError,ZeroDivisionError):
        raise ValueError('Fora da faixa numérica deste cálculo') from None
    if not all(isfinite(x) and x>0 for x in result.values()):
        raise ValueError('Fora da faixa numérica deste cálculo')
    return result


def rhs(s):
    # Sistema normalizado μ=1; teste orbital restrito a r≈1,sem superfície/colisão.
    x,y,vx,vy=s;r=hypot(x,y)
    if r==0:raise ValueError('Campo pontual singular no centro')
    return vx,vy,-x/r**3,-y/r**3


def integrate(n):
    if type(n) is not int or n<16:raise ValueError('Pelo menos16 passos por volta')
    h=2*pi/n;s=(1.,0.,0.,1.)
    maximum=0.
    for _ in range(n):
        k1=rhs(s);k2=rhs(tuple(x+h*k/2 for x,k in zip(s,k1)))
        k3=rhs(tuple(x+h*k/2 for x,k in zip(s,k2)))
        k4=rhs(tuple(x+h*k for x,k in zip(s,k3)))
        s=tuple(x+h*(a+2*b+2*c+d)/6 for x,a,b,c,d in zip(s,k1,k2,k3,k4))
        maximum=max(maximum,abs(hypot(s[0],s[1])-1))
    return s,maximum


class Checks(unittest.TestCase):
    def test_example_and_units(self):
        e=circular(4e14,6e6,4e6,500)
        self.assertEqual(e['r'],1e7);self.assertEqual(e['g'],4.)
        self.assertEqual(e['force'],2000.)
        self.assertAlmostEqual(e['v']/1000,sqrt(40))
        self.assertAlmostEqual(e['period'],9934.588265796102)

    def test_scaling_and_period(self):
        for r in range(1,9):
            for m in (1,2,10):
                a=circular(64.,1.,r-1,m)
                b=circular(64.,1.,2*r-1,m)
                heavy=circular(64.,1.,r-1,2*m)
                self.assertAlmostEqual(b['g']/a['g'],.25)
                self.assertAlmostEqual(b['v']/a['v'],1/sqrt(2))
                self.assertAlmostEqual(b['period']/a['period'],2*sqrt(2))
                self.assertEqual(heavy['g'],a['g'])
                self.assertAlmostEqual(heavy['force'],2*a['force'])
                self.assertAlmostEqual(a['v']**2/a['r'],a['g'])
                self.assertAlmostEqual(a['period']**2/a['r']**3,4*pi*pi/64)

    def test_numerical_orbit_against_circle(self):
        errors=[]
        for n in (96,192,384):
            state,drift=integrate(n)
            # Referência analítica em t=2π: (cos t,sin t,-sin t,cos t).
            reference=(cos(2*pi),sin(2*pi),-sin(2*pi),cos(2*pi))
            error=sqrt(sum((x-y)**2 for x,y in zip(state,reference)))
            errors.append(error)
            self.assertLess(drift,2e-5)
            print('Passos:',n,';erro de estado:',error,';máximo desvio radial:',drift)
        self.assertTrue(errors[2]<errors[1]<errors[0])
        for a,b in zip(errors,errors[1:]):self.assertGreater(a/b,12)

    def test_direction_and_finite_state(self):
        dx,dy,ax,ay=rhs((1.,0.,0.,1.))
        self.assertEqual((dx,dy),(0.,1.))
        self.assertEqual((ax,ay),(-1.,0.))
        self.assertEqual(ax*dx+ay*dy,0.)
        with self.assertRaises(ValueError):rhs((0.,0.,0.,0.))

    def test_contracts(self):
        for values in ((0,1,1,1),(1,0,1,1),(1,1,-1,1),(1,1,1,0),(True,1,1,1),(float('inf'),1,1,1)):
            with self.assertRaises(ValueError):circular(*values)
        for n in (0,15,True,16.5):
            with self.assertRaises(ValueError):integrate(n)


if __name__=='__main__':
    unittest.main()
