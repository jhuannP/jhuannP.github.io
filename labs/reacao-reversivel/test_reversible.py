import unittest,math,itertools
from .reversible import state,relative_time

class ReversibleTests(unittest.TestCase):
    def test_reference_and_dynamic_equilibrium(self):
        r=state(.3,.1,1,0,math.log(2)/.4)
        for key,value in [('a_eq',.25),('b_eq',.75),('a',.625),('b',.375),('forward',.1875),('backward',.0375)]:self.assertAlmostEqual(r[key],value,places=14)
        r=state(.3,.1,.25,.75,10)
        self.assertAlmostEqual(r['forward'],.075);self.assertAlmostEqual(r['backward'],.075)
        self.assertAlmostEqual(r['da_dt'],0)
        r=state(.3,.1,1,0,math.log(3)/.4)
        self.assertAlmostEqual(r['a'],.5)
    def test_invariants_initial_and_differential_equation(self):
        for kf,kb,a,b in itertools.product([.1,.3,1],[.2,.5],[0,.2],[.4,1]):
            r0=state(kf,kb,a,b,0)
            self.assertEqual(r0['a'],a);self.assertEqual(r0['b'],b)
            for t in [.1,1,3]:
                r=state(kf,kb,a,b,t);h=1e-5
                left=state(kf,kb,a,b,t-h);right=state(kf,kb,a,b,t+h)
                self.assertAlmostEqual(r['a']+r['b'],a+b,places=13)
                self.assertGreaterEqual(r['a'],0);self.assertGreaterEqual(r['b'],0)
                self.assertAlmostEqual((right['a']-left['a'])/(2*h),r['da_dt'],delta=2e-10)
                self.assertAlmostEqual(r['db_dt'],-r['da_dt'])
    def test_independent_rk4_and_refinement(self):
        def integrate(n):
            h=2/n;a,b=1.,0.
            def rhs(a,b):return -.3*a+.1*b,.3*a-.1*b
            for _ in range(n):
                u=rhs(a,b);v=rhs(a+h*u[0]/2,b+h*u[1]/2)
                w=rhs(a+h*v[0]/2,b+h*v[1]/2);q=rhs(a+h*w[0],b+h*w[1])
                a+=h*(u[0]+2*v[0]+2*w[0]+q[0])/6
                b+=h*(u[1]+2*v[1]+2*w[1]+q[1])/6
            return a,b
        ref=state(.3,.1,1,0,2);errors=[]
        for n in [4,8,16]:
            a,b=integrate(n);self.assertAlmostEqual(a+b,1,places=14)
            errors.append(abs(a-ref['a']))
        self.assertGreater(errors[0]/errors[1],15)
        self.assertGreater(errors[1]/errors[2],15)
        self.assertLess(errors[-1],2e-8)
    def test_scaling_and_relaxation(self):
        for t in [0,.2,1,10]:
            base=state(.3,.1,1,0,t);fast=state(1.5,.5,1,0,t/5)
            self.assertAlmostEqual(base['a_eq'],fast['a_eq'])
            self.assertAlmostEqual(base['a'],fast['a'])
            self.assertAlmostEqual(base['forward']*5,fast['forward'])
        for epsilon in [.9,.5,.01,1e-8]:
            t=relative_time(.3,.1,epsilon);r=state(.3,.1,1,0,t)
            self.assertAlmostEqual((r['a']-.25)/.75,epsilon,places=14)
        self.assertEqual(relative_time(.3,.1,1),0)
    def test_direction_and_contracts(self):
        # Q/K and net rate have opposite signs; not a thermodynamic fit.
        for a in [.1,.25,.5,.9]:
            b=1-a;r=state(.3,.1,a,b,0)
            self.assertLessEqual(r['db_dt']*math.log((b/a)/3),1e-15)
        for args in [(0,.1,1,0,1),(.1,0,1,0,1),(.1,.1,-1,2,1),(.1,.1,0,0,1),(.1,.1,1,0,-1),(.1,.1,1,0,float('nan')),(True,.1,1,0,1)]:
            with self.assertRaises(ValueError):state(*args)
        for epsilon in [0,-1,1.1,float('inf')]:
            with self.assertRaises(ValueError):relative_time(.3,.1,epsilon)
