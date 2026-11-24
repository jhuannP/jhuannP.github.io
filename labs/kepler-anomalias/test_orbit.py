import unittest
from math import pi,sqrt,sin,cos,hypot
from decimal import Decimal as Q,localcontext
from .orbit import solve,state

def dsin(x):
    term=total=x
    for k in range(1,110):
        term *= -x*x/Q((2*k)*(2*k+1));total+=term
    return total

def reference(m,e):
    # Decimal60: série de seno e bisseção; nenhum sin float na referência.
    with localcontext() as ctx:
        ctx.prec=60;m=Q.from_float(m);e=Q.from_float(e)
        lo=Q(0);hi=Q(7)
        for _ in range(210):
            mid=(lo+hi)/2
            if mid-e*dsin(mid)<m:lo=mid
            else:hi=mid
        return float((lo+hi)/2)

class OrbitTests(unittest.TestCase):
    def test_literal_landmarks_and_quadrants(self):
        e=.6;E=pi/2;m=pi/2-.6
        self.assertAlmostEqual(solve(m,e)['E'],E,places=13)
        s=state(E,e,a=2,mu=8)
        for k,v in {'x':-1.2,'y':1.6,'r':2.,'vx':-2.,'vy':0.,'n':1.,'nu':2.214297435588181}.items():
            self.assertAlmostEqual(s[k],v,places=12)
        self.assertAlmostEqual(s['area'],1.6*m,places=12)
        self.assertGreater(s['nu'],pi/2) # E e ν NÃO precisam estar no mesmo quadrante.
        s=state(3*pi/2,e)
        self.assertTrue(pi<s['nu']<3*pi/2)
        for E in [0,pi,2*pi]:
            self.assertAlmostEqual(solve(E,e)['E'],E,places=13)

    def test_decimal_reference_and_manufactured_roots(self):
        for e in [0,.2,.6,.9,.99]:
            for E in [.001,.1,pi/2,2.3,4.5,6.2]:
                with self.subTest(e=e,E=E):
                    result=solve(E-e*sin(E),e)
                    self.assertAlmostEqual(result['E'],E,delta=9e-13)
                    self.assertLessEqual(abs(result['residual']),3e-14)
        for e,m in [(.99,1e-5),(.99,.1),(.99,5.9),(.6,pi/2-.6),(.2,4.),(.9,3.)]:
            self.assertAlmostEqual(solve(m,e)['E'],reference(m,e),delta=8e-14)

    def test_energy_momentum_geometry(self):
        for a,mu in [(1.,1.),(2.,8.),(.3,20.)]:
            for e in [0,.2,.6,.99]:
                for E in [.1,.6,1.8,3.5,5.5]:
                    s=state(E,e,a,mu)
                    self.assertAlmostEqual(hypot(s['x'],s['y']),s['r'],places=12)
                    self.assertAlmostEqual((s['x']/a+e)**2+(s['y']/(a*sqrt(1-e*e)))**2,1,places=12)
                    self.assertAlmostEqual((s['vx']**2+s['vy']**2)/2-mu/s['r'],-mu/(2*a),places=10)
                    self.assertAlmostEqual(s['x']*s['vy']-s['y']*s['vx'],sqrt(mu*a*(1-e*e)),places=11)

    def test_area_by_polygon_quadrature(self):
        # Área via produto vetorial de posições, sem integrar a fórmula da área.
        for e,E in [(.2,1.),(.6,pi/2),(.9,5.)]:
            N=12000;prev=state(0,e);area=0.
            for i in range(1,N+1):
                cur=state(E*i/N,e)
                area+=(prev['x']*cur['y']-prev['y']*cur['x'])/2;prev=cur
            self.assertAlmostEqual(area,state(E,e)['area'],delta=2e-7)

    def test_limits_sensitivity_and_scaling(self):
        for M in [0,.1,1.,pi,5.,2*pi]:
            self.assertEqual(solve(M,0)['E'],M)
        # Sensibilidade local no periastro; diferença finita, sem divisão em M=0.
        small=1e-8
        self.assertAlmostEqual(solve(small,.99)['E']/small,100,delta=.0001)
        for E in [.3,1.,4.]:
            u=state(E,.6,1,1);v=state(E,.6,2,8)
            self.assertAlmostEqual(u['period'],v['period'])
            self.assertAlmostEqual(v['x'],2*u['x'])
            self.assertAlmostEqual(v['area'],4*u['area'])

    def test_contracts(self):
        for args in [(-1,.3),(7,.3),(1,1),(1,-.1),(1,.999),(float('nan'),.2)]:
            with self.assertRaises(ValueError):solve(*args)
        for args in [(True,.1),(1,False),('1',.1)]:
            with self.assertRaises(TypeError):solve(*args)
        for args in [(1,.3,0,1),(1,.3,1,0),(1,.3,1e9,1),(1,.3,1,float('inf'))]:
            with self.assertRaises(ValueError):state(*args)
