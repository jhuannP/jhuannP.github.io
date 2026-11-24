import math,unittest
from .experiment import state,response

class ForcedOscillatorTests(unittest.TestCase):
    def test_initial_conditions_ode_and_energy_identity(self):
        for z in (0,.1,.5,.9):
            for r in (.5,1,1.5):
                for initial in range(3):
                    s=state(z,r,initial,0)
                    if initial!=1:self.assertAlmostEqual(s['q'],float(initial==2),places=13);self.assertAlmostEqual(s['v'],0,places=13)
                    else:self.assertAlmostEqual(s['homogeneous'],0,places=13)
                    for t in (0,.3,2,9,20):
                        s=state(z,r,initial,t)
                        self.assertAlmostEqual(s['acc']+2*z*s['v']+s['q'],math.cos(r*t),places=12)
                        self.assertAlmostEqual(s['v']*(s['acc']+s['q']),s['energy_rate'],places=12)
                        self.assertLessEqual(abs(s['homogeneous']),s['envelope']+1e-14)

    def test_independent_rk4_state_and_accumulated_work_refinement(self):
        def integrate(z,r,initial,h):
            # Integra a EDO e o balanço de trabalho diretamente, sem usar a solução.
            y=[float(initial==2),0.,0.];t=0.
            def f(t,y):return[y[1],math.cos(r*t)-2*z*y[1]-y[0],math.cos(r*t)*y[1]-2*z*y[1]**2]
            for _ in range(round(4/h)):
                a=f(t,y);b=f(t+h/2,[v+h*k/2 for v,k in zip(y,a)]);c=f(t+h/2,[v+h*k/2 for v,k in zip(y,b)]);d=f(t+h,[v+h*k for v,k in zip(y,c)])
                y=[v+h*(j+2*k+2*l+m)/6 for v,j,k,l,m in zip(y,a,b,c,d)];t+=h
            return y
        for z in (0,.2,.8):
            for r in (.7,1.,1.4):
                for initial in (0,2):
                    target=state(z,r,initial,4)
                    errors=[]
                    for h in (.05,.025):
                        y=integrate(z,r,initial,h)
                        errors.append(max(abs(y[0]-target['q']),abs(y[1]-target['v'])))
                        self.assertAlmostEqual(y[2],target['energy']-float(initial==2)/2,delta=2e-6)
                    self.assertLess(errors[1],errors[0]*.08+1e-13)

    def test_steady_power_average_and_peak_locations(self):
        for z in (.1,.5,.8):
            for r in (.5,1.,1.5):
                n=1024;period=2*math.pi/r
                samples=[state(z,r,1,period*j/n) for j in range(n)]
                expected=response(z,r)['power']
                self.assertAlmostEqual(sum(s['power_in'] for s in samples)/n,expected,places=12)
                self.assertAlmostEqual(sum(s['loss'] for s in samples)/n,expected,places=12)
            self.assertAlmostEqual(response(z,1)['power'],1/(4*z),places=13)
            for r in (.6,.9,1.1,1.4):self.assertLess(response(z,r)['power'],response(z,1)['power'])
            peak=response(z,1)['peak']
            if peak:
                for r in (peak-.01,peak+.01):self.assertLess(response(z,r)['amplitude'],response(z,peak)['amplitude'])
            else:self.assertGreater(response(z,0)['amplitude'],response(z,.1)['amplitude'])

    def test_undamped_resonance_and_contract(self):
        for t in (0,1,math.pi/2,7):
            s=state(0,1,0,t);self.assertAlmostEqual(s['q'],t*math.sin(t)/2)
            self.assertIsNone(s['amplitude']);self.assertIsNone(s['power']);self.assertEqual(s['loss'],0)
        self.assertAlmostEqual(response(.25,1)['amplitude']*.25,.5)
        for args in ((-1,1,0,1),(1,1,0,1),(.5,-1,0,1),(.5,1,3,1),(.5,1,0,-1)):
            with self.assertRaises(ValueError):state(*args)
