import math,unittest
from fractions import Fraction as F
from .experiment import value,partials,model,direction


class GradientTests(unittest.TestCase):
    def test_exact_quadratic_increment(self):
        directions=[(F(1),F(0)),(F(0),F(1)),(F(3,5),F(4,5)),(F(-5,13),F(12,13))]
        for x in map(F,(-1,0,2)):
            for y in map(F,(-1,0,2)):
                for u,v in directions:
                    self.assertEqual(u*u+v*v,1)
                    for h in (F(1),F(1,2),F(1,4),F(1,8)):
                        delta=value(0,x+h*u,y+h*v)-value(0,x,y)
                        linear=h*(2*x*u+4*y*v)
                        self.assertEqual(delta-linear,h*h*(u*u+2*v*v))
                        self.assertEqual((value(0,x+h*u,y+h*v)-value(0,x-h*u,y-h*v))/(2*h),2*x*u+4*y*v)

    def test_continuous_counterexample_with_all_directions(self):
        self.assertEqual(partials(1,0,0),(1,0))
        for u,v in ((F(1),F(0)),(F(0),F(1)),(F(3,5),F(4,5)),(F(-5,13),F(12,13))):
            for h in (F(1),F(-1),F(1,2),F(1,8)):
                self.assertEqual(value(1,h*u,h*v)/h,u**3)
                self.assertLessEqual(abs(value(1,h*u,h*v)),abs(h))
        for h in (F(1),F(1,2),F(1,4),F(1,8)):
            residual=(value(1,h*F(3,5),h*F(4,5))-h*F(3,5))/h
            self.assertEqual(residual,F(-48,125))
        self.assertEqual(value(1,F(1),F(1)),F(1,2))
        self.assertNotEqual(value(1,F(1),F(1)),value(1,F(1),F(0))+value(1,F(0),F(1)))

    def test_gradient_from_difference_and_level_normal(self):
        eps=1e-6
        for kind in (0,1):
            for x,y in ((1,2),(-1,1),(0,1),(1,0)):
                g=partials(kind,x,y)
                numeric=((value(kind,x+eps,y)-value(kind,x-eps,y))/(2*eps),
                         (value(kind,x,y+eps)-value(kind,x,y-eps))/(2*eps))
                for a,b in zip(g,numeric):self.assertAlmostEqual(a,b,delta=2e-9)
                for angle in range(0,360,15):
                    u=direction(angle)
                    self.assertLessEqual(abs(g[0]*u[0]+g[1]*u[1]),math.hypot(*g)+2e-15)
        for t in (0,.4,1,2,3):
            x,y=3*math.cos(t),3/math.sqrt(2)*math.sin(t)
            tx,ty=-3*math.sin(t),3/math.sqrt(2)*math.cos(t)
            g=partials(0,x,y)
            self.assertAlmostEqual(value(0,x,y),9,delta=4e-15)
            self.assertAlmostEqual(g[0]*tx+g[1]*ty,0,delta=4e-15)
        for k in (-1,-.5,.5,1):
            x=2*k;y=abs(x)*math.sqrt(x/k-1)
            self.assertAlmostEqual(value(1,x,y),k,delta=1e-15)

    def test_remainders_domains_and_critical_point(self):
        smooth=[model(0,1,2,45,n) for n in range(7)]
        bad=[model(1,0,0,45,n) for n in range(7)]
        for a,b in zip(smooth,smooth[1:]):
            rounding=8*math.ulp(max(abs(a['base']),abs(a['final']),abs(b['final'])))/b['h']
            self.assertAlmostEqual(a['scaled_remainder']/2,b['scaled_remainder'],delta=rounding)
        for s in bad:
            self.assertFalse(s['differentiable']);self.assertFalse(s['normal_available'])
            self.assertAlmostEqual(s['scaled_remainder'],1/(2*math.sqrt(2)),delta=3e-16)
            self.assertAlmostEqual(s['secant'],s['derivative'],delta=2e-16)
            self.assertNotEqual(s['dot'],s['derivative'])
        s=model(0,0,0)
        self.assertTrue(s['differentiable']);self.assertFalse(s['normal_available'])
        self.assertEqual(s['max_growth'],0);self.assertGreater(s['final'],0)
        s=model(1,0,1)
        self.assertTrue(s['differentiable']);self.assertFalse(s['normal_available'])
        self.assertEqual(s['g'],(0,0));self.assertEqual(s['base'],0)
        for args in ((2,), (0,3), (0,0,0,361), (0,0,0,0,7), (0,0,0,0,1.5), (0,float('nan'))):
            with self.assertRaises(ValueError):model(*args)
