import unittest
from math import sqrt,pi,isclose
from .experiment import geometry,normal,simpson_area

class SurfaceTests(unittest.TestCase):
    def test_planar_limit_and_independent_antiderivative(self):
        for R in (.5,1,2):
            self.assertAlmostEqual(geometry(0,R)['area'],pi*R*R)
            self.assertAlmostEqual(geometry(1e-9,R)['area'],pi*R*R)
            for a in (.25,1,2):
                ref=2*pi*((1+a*a*R*R)**1.5-1)/(3*a*a)
                self.assertAlmostEqual(geometry(a,R)['area'],ref,places=11)
                self.assertAlmostEqual(simpson_area(a,R,512),ref,places=8)
                self.assertGreater(geometry(a,R)['area'],geometry(a,R)['projected'])

    def test_normal_and_flux_integrand(self):
        for a in (0,.5,2):
            for u,v in ((0,0),(.5,.25),(1,0)):
                for sign in (-1,1):
                    n=normal(a,u,v,sign)
                    self.assertAlmostEqual(sum(x*x for x in n),1)
                    self.assertAlmostEqual(n[0]+a*u*n[2],0)
                    self.assertAlmostEqual(n[1]+a*v*n[2],0)
                    jac=sqrt(1+a*a*(u*u+v*v))
                    self.assertAlmostEqual(n[2]*jac,sign)

    def test_scaling_and_orientation(self):
        for a in (0,.5,2):
            g=geometry(a,1)
            h=geometry(a,1,-1)
            self.assertEqual(g['area'],h['area']);self.assertEqual(g['mass'],h['mass'])
            self.assertEqual(g['flux'],-h['flux'])
            for scale in (.5,2,3):
                q=geometry(a/scale,scale)
                self.assertAlmostEqual(q['area'],scale**2*g['area'])
                self.assertAlmostEqual(q['height'],scale*g['height'])

    def test_quadrature_convergence_and_contracts(self):
        exact=geometry(1,1)['area']
        errors=[abs(simpson_area(1,1,n)-exact) for n in (8,16,32)]
        self.assertTrue(errors[0]>errors[1]>errors[2])
        self.assertGreater(errors[0]/errors[1],10)
        for args in ((-1,1),(0,0),(True,1),(0,float('inf')),(1,1,0),(1,1,True)):
            with self.assertRaises(ValueError):geometry(*args)
        for n in (0,3,True):
            with self.assertRaises(ValueError):simpson_area(1,1,n)
