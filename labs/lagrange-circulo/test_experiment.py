import unittest
from math import hypot,sin,cos,pi
from .experiment import extrema

class LagrangeCircleTests(unittest.TestCase):
    def test_reference(self):
        r=extrema(3,4,2)
        self.assertAlmostEqual(r["maximum"]["x"],6/5)
        self.assertAlmostEqual(r["maximum"]["y"],8/5)
        self.assertAlmostEqual(r["maximum"]["value"],10)
        self.assertAlmostEqual(r["maximum"]["multiplier"],5/4)
        self.assertAlmostEqual(r["minimum"]["value"],-10)

    def test_constraint_gradient_and_parameterization(self):
        for p,q in ((3,4),(-3,4),(0,2),(2,0),(-1,-1)):
            for radius in (.5,1,3):
                for scale in (-2,.5,1,3):
                    result=extrema(p,q,radius,scale)
                    for name in ("minimum","maximum"):
                        r=result[name];x,y,lam=r["x"],r["y"],r["multiplier"]
                        self.assertAlmostEqual(x*x+y*y,radius**2,places=12)
                        self.assertAlmostEqual(p,lam*scale*2*x,places=12)
                        self.assertAlmostEqual(q,lam*scale*2*y,places=12)
                        self.assertAlmostEqual(p*x+q*y,r["value"],places=12)
                        # Tangent direction (-y,x), independently from the returned multiplier.
                        self.assertAlmostEqual(-p*y+q*x,0,places=12)
                    for i in range(48):
                        t=2*pi*i/48
                        f=radius*(p*cos(t)+q*sin(t))
                        self.assertLessEqual(f,result["maximum"]["value"]+1e-12)
                        self.assertGreaterEqual(f,result["minimum"]["value"]-1e-12)

    def test_constraint_rescaling_and_positive_objective_scale(self):
        r=extrema(3,4,2);changed=extrema(3,4,2,-3);objective=extrema(6,8,2)
        for name in ("minimum","maximum"):
            for coord in ("x","y"):
                self.assertEqual(r[name][coord],changed[name][coord])
                self.assertEqual(r[name][coord],objective[name][coord])
            self.assertAlmostEqual(changed[name]["multiplier"],r[name]["multiplier"]/-3)
            self.assertEqual(objective[name]["value"],2*r[name]["value"])

    def test_degenerate_cases_and_nonextremal_stationary_point(self):
        self.assertTrue(extrema(0,0,2)["all_points"])
        self.assertIsNone(extrema(0,0,2)["maximum"])
        r=extrema(3,4,0)
        self.assertFalse(r["regular"])
        self.assertEqual(r["maximum"]["value"],0)
        self.assertIsNone(r["maximum"]["multiplier"])
        # f=x^3 on the unit circle: (0,1) is stationary but nearby f has both signs.
        for eps in (.1,.01,.001):
            self.assertLess((-eps)**3,0)
            self.assertGreater(eps**3,0)
            self.assertAlmostEqual(eps**2+(1-eps**2),1)

    def test_contracts(self):
        for args in ((1,2,-1,1),(1,2,1,0),(True,2,1,1),(1,2,float("nan"),1),
                     (1,2,1,float("inf")),("x",2,1,1),(1e308,1e308,2,1)):
            with self.assertRaises(ValueError):extrema(*args)
