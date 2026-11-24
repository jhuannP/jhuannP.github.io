import unittest
from math import sqrt, hypot
try:
    from .experiment import binary, integrate, diagnostics, acceleration, position_error
except ImportError:
    from experiment import binary, integrate, diagnostics, acceleration, position_error

class GravityTests(unittest.TestCase):
    def test_reference(self):
        m,r,v=binary(); d=diagnostics(m,r,v)
        self.assertAlmostEqual(d['energy'],-.5)
        self.assertEqual(d['momentum'],[0,0]);self.assertEqual(d['center'],[0,0])
        self.assertAlmostEqual(d['angular'],1/sqrt(2))
        self.assertEqual(acceleration(m,r),[[1,0],[-1,0]])

    def test_force_potential_gradient(self):
        m=[2.,3.,4.];r=[[-1,.2],[.8,.6],[.1,-1.2]];v=[[0,0]]*3;a=acceleration(m,r);eps=1e-6
        for i in range(3):
            for k in range(2):
                plus=[row[:] for row in r];minus=[row[:] for row in r]
                plus[i][k]+=eps;minus[i][k]-=eps
                grad=(diagnostics(m,plus,v)['energy']-diagnostics(m,minus,v)['energy'])/(2*eps)
                self.assertAlmostEqual(m[i]*a[i][k],-grad,places=7)
        for k in range(2):self.assertAlmostEqual(sum(m[i]*a[i][k] for i in range(3)),0,places=13)

    def test_convergence(self):
        for method,lo,hi in [('cromer',1.8,2.2),('verlet',3.8,4.2)]:
            errors=[position_error(integrate(*binary(),.7,n,method)) for n in (40,80,160)]
            for a,b in zip(errors,errors[1:]):self.assertTrue(lo<a/b<hi,(method,errors))

    def test_momentum_center_and_angular(self):
        m=[2,3,1];r=[[-1,0],[1,0],[0,2]];v=[[.1,.3],[-.2,0],[.4,-.6]]
        for method in ['cromer','verlet']:
            trace=integrate(m,r,v,.2,100,method);initial=trace[0]
            for row in trace:
                for k in range(2):
                    self.assertAlmostEqual(row['momentum'][k],initial['momentum'][k],places=12)
                    self.assertAlmostEqual(row['center'][k],initial['center'][k]+row['time']*initial['momentum'][k]/sum(m),places=12)
                self.assertAlmostEqual(row['angular'],initial['angular'],places=12)
            self.assertEqual(r,[[-1,0],[1,0],[0,2]])

    def test_contracts(self):
        for time,steps,method in [(0,10,'verlet'),(1,True,'verlet'),(1,10001,'verlet'),(1,1,'unknown')]:
            with self.assertRaises(ValueError):integrate(*binary(),time,steps,method)
        for masses in [[0,1],[True,1],[float('nan'),1],[1]]:
            with self.assertRaises(ValueError):integrate(masses,[[-.5,0],[.5,0]],[[0,0],[0,0]],1,10)
        with self.assertRaises(ValueError):integrate([1,1],[[0,0],[0,0]],[[0,0],[0,0]],1,10)

if __name__=='__main__':unittest.main()
