import math
import unittest
from .experiment import potential, simpson, coulomb_shell


class PotentialTests(unittest.TestCase):
    def test_gradient_and_boundary(self):
        h=1e-5
        for profile in (0,1):
            for q in (-2,0,1.5):
                for r in (.1,.5,.9,1.1,2,4):
                    v=lambda x: potential(profile,q,x)['value']
                    numeric=-(v(r+h)-v(r-h))/(2*h)
                    self.assertAlmostEqual(numeric,potential(profile,q,r)['field'],delta=3e-10)
                center=potential(profile,q,0)
                self.assertEqual(center['field'],0)
                edge=potential(profile,q,1)
                self.assertAlmostEqual(potential(profile,q,1-h)['value'],edge['value'],delta=1e-5)
                self.assertAlmostEqual(potential(profile,q,1+h)['value'],edge['value'],delta=1e-5)
                left=-(edge['value']-potential(profile,q,1-h)['value'])/h
                right=-(potential(profile,q,1+h)['value']-edge['value'])/h
                self.assertAlmostEqual(left,edge['inner_field'],delta=2e-6)
                self.assertAlmostEqual(right,edge['outer_field'],delta=2e-6)
                self.assertEqual(edge['field'] is None,profile==1 and q!=0)

    def test_independent_coulomb_integral(self):
        for q in (-2,0,1.5):
            for r in (0,.3,.8,1,1.2,2,4):
                self.assertAlmostEqual(coulomb_shell(r,q),potential(1,q,r)['base'],delta=2e-11)
        # Integrate spherical layers: dQ=3Q*a² da. The split at a=r avoids a kink.
        for q in (-1,2):
            for r in (0,.3,.8,1,2):
                if r==0:
                    v=simpson(lambda a:3*q*a,0,1)/(4*math.pi)
                else:
                    v=(simpson(lambda a:3*q*a*a/r,0,min(r,1))+(simpson(lambda a:3*q*a,r,1) if r<1 else 0))/(4*math.pi)
                self.assertAlmostEqual(v,potential(0,q,r)['base'],delta=1e-12)

    def test_work_line_integral_and_gauge(self):
        for profile in (0,1):
            for Q in (-2,0,1):
                for r in (0,.5,1,2,4):
                    # Independent radial integral of the Gauss fields; split at r=1.
                    lo,hi=sorted((r,2)); points=sorted({lo,hi}|({1} if lo<1<hi else set()))
                    integral=0
                    for a,b in zip(points,points[1:]):
                        if (a+b)/2<1:
                            fn=(lambda x:Q*x/(4*math.pi)) if profile==0 else (lambda x:0)
                        else:
                            fn=lambda x:Q/(4*math.pi*x*x)
                        integral+=simpson(fn,a,b)
                    expected=-integral*(1 if r>=2 else -1)
                    for q in (-1,0,1):
                        for shift in (-1,0,1):
                            s=potential(profile,Q,r,q,shift)
                            self.assertAlmostEqual(s['delta'],expected,delta=2e-12)
                            self.assertAlmostEqual(s['value']-s['start'],s['delta'],delta=1e-15)
                            self.assertAlmostEqual(s['energy'],q*expected,delta=2e-12)
                            self.assertEqual(s['energy']+s['work'],0)
                            self.assertEqual(s['field'],potential(profile,Q,r,q,0)['field'])

    def test_domain_and_counterexamples(self):
        for args in ((3,1,1),(0,1,-1),(0,float('nan'),1),(0,1,1,-1,float('inf'))):
            with self.assertRaises(ValueError): potential(*args)
        self.assertNotEqual(potential(1,1,.5)['value'],0)  # E=0 does not imply V=0.
        self.assertNotEqual(potential(0,1,0)['base'],potential(1,1,0)['base'])
        self.assertEqual(potential(0,1,2)['base'],potential(1,1,2)['base'])
        # V(0)=0 for opposite point charges at +/-1; Ex(0)=-2 in k=Q=1 units.
        v=lambda x:1/abs(x-1)-1/abs(x+1)
        self.assertEqual(v(0),0)
        h=1e-5
        self.assertAlmostEqual(-(v(h)-v(-h))/(2*h),-2,delta=3e-10)
