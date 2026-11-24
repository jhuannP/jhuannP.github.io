import unittest
from math import pi,cos,sin,hypot
from .experiment import state

class FreeOscillatorTests(unittest.TestCase):
    def test_reference_and_equilibrium(self):
        r=state(2,8,.6,1.6,pi/4)
        self.assertAlmostEqual(r["x"],.8)
        self.assertAlmostEqual(r["v"],-1.2)
        self.assertAlmostEqual(r["energy"],4)
        self.assertAlmostEqual(r["amplitude"],1)
        self.assertAlmostEqual(r["phase"],-.9272952180016122)
        zero=state(2,8,0,0,99)
        self.assertEqual(zero["energy"],0)
        self.assertIsNone(zero["phase"])

    def test_initial_energy_derivatives_and_composition(self):
        for m,k in ((1,1),(2,8),(3,2)):
            for x0,v0 in ((1,0),(0,2),(.6,1.6),(-2,-3),(0,0)):
                z=state(m,k,x0,v0,0)
                self.assertAlmostEqual(z["x"],x0)
                self.assertAlmostEqual(z["v"],v0)
                for t in (-1,.3,2,7):
                    r=state(m,k,x0,v0,t)
                    self.assertAlmostEqual(r["energy"],(m*v0*v0+k*x0*x0)/2,places=11)
                    h=1e-5
                    left=state(m,k,x0,v0,t-h);right=state(m,k,x0,v0,t+h)
                    self.assertAlmostEqual((right["x"]-left["x"])/(2*h),r["v"],places=7)
                    self.assertAlmostEqual((right["v"]-left["v"])/(2*h),r["a"],places=7)
                    chained=state(m,k,r["x"],r["v"],.41)
                    direct=state(m,k,x0,v0,t+.41)
                    self.assertAlmostEqual(chained["x"],direct["x"],places=11)
                    self.assertAlmostEqual(chained["v"],direct["v"],places=11)
                    periodic=state(m,k,x0,v0,t+r["period"])
                    self.assertAlmostEqual(periodic["x"],r["x"],places=11)
                    self.assertAlmostEqual(r["amplitude"]*cos(r["omega"]*t+(r["phase"] or 0)),r["x"],places=11)

    def test_independent_rk4_refinement(self):
        def solve(n):
            x,v=.6,1.6;h=1.3/n
            f=lambda x,v:(v,-4*x)
            for _ in range(n):
                a,b=f(x,v);c,d=f(x+h*a/2,v+h*b/2)
                e,g=f(x+h*c/2,v+h*d/2);j,l=f(x+h*e,v+h*g)
                x+=h*(a+2*c+2*e+j)/6
                v+=h*(b+2*d+2*g+l)/6
            return x,v
        r=state(2,8,.6,1.6,1.3)
        error=lambda n:hypot(solve(n)[0]-r["x"],solve(n)[1]-r["v"])
        coarse,fine=error(20),error(40)
        self.assertLess(fine,coarse/12)
        self.assertLess(fine,1e-6)

    def test_euler_adds_energy(self):
        for m,k,x,v,h in ((2,8,.6,1.6,.1),(1,3,-1,.5,.02),(3,2,0,2,.2)):
            before=(m*v*v+k*x*x)/2
            xn,vn=x+h*v,v-h*k*x/m
            after=(m*vn*vn+k*xn*xn)/2
            self.assertAlmostEqual(after,before*(1+h*h*k/m),places=12)
            self.assertGreater(after,before)

    def test_contracts(self):
        for args in ((0,1,1,0,0),(1,-1,1,0,0),(True,1,1,0,0),
                     (1,1,float("nan"),0,0),(1,1,1,0,float("inf")),
                     (1,1,1,0,"a"),(1e-300,1e300,1,0,0)):
            with self.assertRaises(ValueError):state(*args)
