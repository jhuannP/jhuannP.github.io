import unittest,math
from .drag import state

class DragTests(unittest.TestCase):
    def test_reference_signs_and_terminal_solution(self):
        t=math.log(2)/2;r=state(2,4,10,t)
        self.assertEqual((r['tau'],r['terminal']),(.5,5))
        self.assertAlmostEqual(r['velocity'],2.5)
        self.assertAlmostEqual(r['acceleration'],5)
        self.assertAlmostEqual(r['position'],2.5*math.log(2)-1.25)
        for t in (0,.1,.5,2):
            r=state(2,4,10,t,5,3)
            self.assertAlmostEqual(r['velocity'],5);self.assertAlmostEqual(r['position'],3+5*t)
            self.assertAlmostEqual(r['acceleration'],0)
        r=state(2,4,10,math.log(2)/2,-5)
        self.assertAlmostEqual(r['velocity'],0,places=13)
        self.assertAlmostEqual(r['position'],2.5*(math.log(2)-1))
        self.assertGreater(state(2,4,10,0,-5)['acceleration'],10)
    def test_kinematics_and_ode_by_finite_differences(self):
        h=1e-5
        for m,b in ((2,4),(1,1),(3,2)):
            for v0 in (-5,0,8):
                for t in (.1,.5,1):
                    left=state(m,b,10,t-h,v0);right=state(m,b,10,t+h,v0);r=state(m,b,10,t,v0)
                    self.assertAlmostEqual((right['position']-left['position'])/(2*h),r['velocity'],delta=2e-8)
                    self.assertAlmostEqual((right['velocity']-left['velocity'])/(2*h),10-b*r['velocity']/m,delta=2e-8)
    def test_work_energy_by_independent_quadrature(self):
        # Simpson integrates drag power; compare with mg*dy - deltaK independently.
        n=2000
        for v0 in (-5,0,8):
            for t in (.2,1,2):
                m,b,g=2,4,10;dt=t/n;integral=0.0
                for j in range(n+1):
                    # Direct exponential velocity rather than state() integration kernels.
                    v=5+(v0-5)*math.exp(-2*j*dt)
                    weight=1 if j in (0,n) else (4 if j%2 else 2)
                    integral+=weight*b*v*v
                integral*=dt/3;r=state(m,b,g,t,v0)
                balance=m*g*r['position']-m*(r['velocity']**2-v0*v0)/2
                self.assertGreaterEqual(integral,0)
                self.assertAlmostEqual(integral,balance,delta=3e-10)
    def test_small_time_zero_drag_and_limit(self):
        for t in (1e-10,1e-8):
            r=state(2,4,10,t,-5)
            # y0=0 avoids adding a displacement below precision to a large origin.
            self.assertAlmostEqual(r['position'],-5*t+10*t*t,delta=1e-22)
            self.assertAlmostEqual(r['velocity'],-5+20*t,delta=3e-14)
        vacuum=state(2,0,10,1,3)
        self.assertEqual((vacuum['velocity'],vacuum['position']),(13,8))
        self.assertIsNone(vacuum['terminal']);self.assertIsNone(vacuum['tau'])
        weak=state(2,1e-8,10,1,3)
        self.assertAlmostEqual(weak['velocity'],13,delta=1e-6)
        self.assertAlmostEqual(weak['position'],8,delta=1e-6)
    def test_contracts_and_relaxation(self):
        for args in ((0,1,10,1),(1,-1,10,1),(1,1,-1,1),(1,1,10,-1),(True,1,10,1),(1,1,10,float('nan'))):
            with self.assertRaises(ValueError):state(*args)
        for v0 in (-5,0,8):
            for t in (.1,.5,2):
                v=state(2,4,10,t,v0)['velocity']
                self.assertTrue(min(v0,5)<=v<=max(v0,5))
