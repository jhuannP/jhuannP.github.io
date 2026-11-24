import unittest,math
from fractions import Fraction as F
from .flux import step,weights,periodic_density


class FluxTests(unittest.TestCase):
    def test_literal_update_and_negative_counterexample(self):
        r=(4,0,0,0);args=(F(1,4),F(1,32))
        stable,_=step(r,*args,F(1,4),F(1,4))
        self.assertEqual(stable,(F(2),F(3,2),F(0),F(1,2)))
        self.assertEqual(weights(*args,F(1,4),F(1,4)),(F(1,2),F(3,8),F(1,8)))
        unstable,_=step(r,*args,1,F(1,4))
        self.assertEqual(unstable,(F(-4),F(6),F(0),F(2)))
        self.assertEqual(sum(stable)/4,1);self.assertEqual(sum(unstable)/4,1)
        reversed_out,_=step(r,F(-1,4),F(1,32),F(1,4),F(1,4))
        self.assertEqual(reversed_out,(F(2),F(1,2),F(0),F(3,2)))

    def test_convex_reference_for_periodic_impulses(self):
        for n in (3,4,5,6):
            dx=F(1,n)
            for adv in (F(0),F(1,4),F(1,2),F(1)):
                for diff in (F(0),F(1,8),F(1,4)):
                    if adv+2*diff>1:continue
                    for sign in (-1,1):
                        c=sign*adv*dx;d=diff*dx*dx
                        for cell in range(n):
                            r=[0]*n;r[cell]=n;out,_=step(r,c,d,1,dx)
                            w=weights(c,d,1,dx)
                            reference=tuple(w[0]*r[i]+w[1]*r[(i-1)%n]+w[2]*r[(i+1)%n] for i in range(n))
                            self.assertEqual(out,reference);self.assertGreaterEqual(min(out),0)
                            self.assertEqual(dx*sum(out),1)

    def test_stationary_uniform_and_telescoping(self):
        for c in (F(-1),F(0),F(1)):
            out,j=step((1,1,1,1),c,F(1,5),F(1,100),F(1,4))
            self.assertEqual(out,(F(1),)*4);self.assertEqual(j,(c,)*4)
        r=(1,2,3,2);dt=F(1,50);dx=F(1,4)
        out,j=step(r,F(1,2),F(1,10),dt,dx)
        for k in (1,2,3):self.assertEqual(dx*sum(out[:k])-dx*sum(r[:k]),dt*(j[-1]-j[k-1]))

    def test_analytic_mass_bounds_and_pde_residual(self):
        for t in (0,.1,.4):
            for a in (-1,.5,1):
                n=64;values=[periodic_density(j/n,t,.3,.05,a) for j in range(n)]
                self.assertAlmostEqual(sum(values)/n,1,places=14);self.assertGreaterEqual(min(values),0)
        for x in (.1,.3,.8):
            t=.2;c=.3;d=.05;eps=1e-4
            f=lambda xx,tt:periodic_density(xx,tt,c,d,.5)
            rt=(f(x,t+eps)-f(x,t-eps))/(2*eps)
            rx=(f(x+eps,t)-f(x-eps,t))/(2*eps)
            rxx=(f(x+eps,t)-2*f(x,t)+f(x-eps,t))/eps**2
            self.assertLess(abs(rt+c*rx-d*rxx),2e-7)
        self.assertAlmostEqual(periodic_density(.3,.2,c=0),periodic_density(.5,.2,c=1))

    def test_contracts(self):
        for r in [[],[1,1],[-1,2,0],[True,1,1],[1.,1,1]]:
            with self.assertRaises(ValueError):step(r,0,1,1,1)
        for args in [(0,-1,1,1),(0,1,-1,1),(0,1,1,0),(True,1,1,1)]:
            with self.assertRaises(ValueError):weights(*args)
        for kwargs in [dict(t=-1),dict(a=2),dict(d=-1),dict(length=0),dict(x=True),dict(x=float('nan'))]:
            base=dict(x=0,t=0);base.update(kwargs)
            with self.assertRaises(ValueError):periodic_density(**base)

if __name__=='__main__':unittest.main()
