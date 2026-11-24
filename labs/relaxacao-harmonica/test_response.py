import unittest,json
from itertools import product
from math import exp,cos,sin,sqrt,atan,pi,log
from pathlib import Path
from numerics import simpson
from numerics4 import integrate
from .response import state

class ResponseTests(unittest.TestCase):
    def test_original_reference_and_preparation(self):
        for t in (0,.1,.7,1,3):
            s=state(t=t)
            self.assertEqual((s['a'],s['b'],s['c']),(2,3,-3))
            self.assertAlmostEqual(s['y'],2*cos(3*t)+3*sin(3*t)-3*exp(-2*t))
        s=state();self.assertEqual((s['y'],s['dy']),(-1,15))
        self.assertAlmostEqual(s['amplitude'],sqrt(13));self.assertAlmostEqual(s['phase'],atan(1.5))
        self.assertEqual(state(y0=2,t=2)['homogeneous'],0)
        self.assertAlmostEqual(state(t=log(10))['envelope'],.03)

    def test_equation_initial_and_derivative(self):
        for k,w,B,y0 in product((.5,2,4),(0,1,3),(-3,0,5),(-2,1)):
            self.assertAlmostEqual(state(k,w,B,y0,0)['y'],y0)
            for t in (.2,.7,2):
                s=state(k,w,B,y0,t)
                self.assertAlmostEqual(s['dy']+k*s['y'],B*cos(w*t),places=11)
                h=1e-5
                fd=(state(k,w,B,y0,t+h)['y']-state(k,w,B,y0,t-h)['y'])/(2*h)
                self.assertAlmostEqual(fd,s['dy'],delta=1e-7)

    def test_integrating_factor_independent_quadrature(self):
        for k,w,B,y0,t in product((.5,2),(0,3),(-3,5),(-2,1),(.3,1.2)):
            # Integrates the original forcing with decay kernel, no trig antiderivative.
            direct=y0*exp(-k*t)+simpson(lambda s:exp(-k*(t-s))*B*cos(w*s),0,t,512)
            self.assertAlmostEqual(state(k,w,B,y0,t)['y'],direct,delta=1e-9)

    def test_initial_value_numerics_and_gain(self):
        # Independent RK4 engine solves original ODE, not derivative of closed formula.
        for k,w,B,y0 in [(2,3,13,-1),(.5,0,3,1),(4,1,-2,0)]:
            tr=integrate(lambda t,y:[B*cos(w*t)-k*y[0]],0,2,[y0],512)
            self.assertAlmostEqual(tr[-1][1][0],state(k,w,B,y0,2)['y'],delta=2e-8)
        for k in (.5,2,4):
            gains=[state(k,w)['gain'] for w in (0,.5,1,2,4,10)]
            self.assertEqual(gains[0],1)
            self.assertTrue(all(a>b for a,b in zip(gains,gains[1:])))
            self.assertAlmostEqual(state(k,k)['gain'],1/sqrt(2))

    def test_old_material_and_contracts(self):
        lesson=next(l for l in json.loads((Path(__file__).resolve().parents[2]/'content/lessons.json').read_text()) if l['id']=='edo-forcada')
        exec(lesson['python'],{});exec(lesson['codingPractice']['solution'],{})
        for t in (0,.5,1,20):
            self.assertAlmostEqual(state(2,0,6,0,t)['y'],3*(1-exp(-2*t)))
        for name,v in [('k',0),('omega',-1),('B',1001),('y0',-1001),('t',101),('t',-.1)]:
            with self.assertRaises(ValueError):state(**{name:v})
        for v in (True,'2',float('nan'),float('inf')):
            with self.assertRaises(ValueError):state(k=v)
