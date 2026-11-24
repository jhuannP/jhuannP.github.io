import math,unittest
from fractions import Fraction as F
from .experiment import plane,model


class TangentPlaneTests(unittest.TestCase):
    def test_exact_rational_expansion_and_bounds(self):
        for kind,sign in ((0,1),(1,-1)):
            for a,b in ((F(0),F(0)),(F(1),F(1)),(F(-2),F(3))):
                for h in (F(-1),F(0),F(1,10),F(2,3)):
                    for k in (F(-1,4),F(0),F(1,5)):
                        s=plane(kind,a,b,h,k)
                        # Independent polynomial evaluation in global coordinates.
                        z=(a+h)*(a+h)+sign*2*(b+k)*(b+k)
                        self.assertEqual(z-s['linear'],s['remainder'])
                        self.assertLessEqual(abs(s['remainder']),2*(h*h+k*k))
                        if kind==0:self.assertGreaterEqual(s['remainder'],0)

    def test_tangents_from_parametrized_curves(self):
        # Symmetric chord derivatives are exact for these quadratic graph curves.
        for kind,sign in ((0,1),(1,-1)):
            for a,b in ((0,0),(1,1),(-1,1)):
                s=plane(kind,a,b,0,0);N=s['normal'];eps=F(1,8)
                for u,v in ((1,0),(0,1),(F(3,5),F(4,5))):
                    f=lambda t:(a+t*u)**2+2*sign*(b+t*v)**2
                    tangent=(u,v,(f(eps)-f(-eps))/(2*eps))
                    self.assertEqual(sum(x*y for x,y in zip(N,tangent)),0)
                self.assertEqual(N[2],1)
                self.assertIsNone(s['scaled'])

    def test_refinement_and_integral_remainder(self):
        for kind,sign in ((0,1),(1,-1)):
            for angle in range(0,361,15):
                for n in range(6):
                    a=model(kind,0,angle,n);b=model(kind,0,angle,n+1)
                    self.assertAlmostEqual(b['remainder'],a['remainder']/4,places=14)
                    self.assertAlmostEqual(b['scaled'],a['scaled']/2,places=14)
                    # Integrate (1-t) delta^T H delta by midpoint; exact for this integrand.
                    h,k=[a['rho']*v for v in a['u']]
                    integral=sum((1-(i+.5)/100)*(2*h*h+4*sign*k*k)/100 for i in range(100))
                    self.assertAlmostEqual(integral,a['remainder'],places=13)
                    self.assertAlmostEqual(a['exact']-a['linear'],a['remainder'],places=13)

    def test_crossing_critical_points_and_domain(self):
        self.assertGreater(plane(1,1,1,1,0)['remainder'],0)
        self.assertLess(plane(1,1,1,0,1)['remainder'],0)
        self.assertAlmostEqual(plane(1,1,1,math.sqrt(2),1)['remainder'],0)
        self.assertEqual(plane(0,0,0,1,0)['normal'],(0,0,1))
        self.assertEqual(plane(0,1,1,10,0)['remainder'],100)
        for args in ((2,0,0,0),(0,3,0,0),(0,0,361,0),(0,0,0,1.2),(0,0,0,7)):
            with self.assertRaises(ValueError):model(*args)
        with self.assertRaises(ValueError):plane(0,0,0,float('nan'),1)
