import unittest,itertools
from fractions import Fraction as F
from .experiment import model

class HydrostaticWallTests(unittest.TestCase):
    def test_pressure_reference_and_gradient(self):
        for rho,h,p0,probe in itertools.product((500,1000,1500),(0,1,4),(80,100,120),(0,.5,1)):
            s=model(rho,h,1,p0,probe);z=F(str(probe))*h
            self.assertEqual(s['dp'],float(F(rho)*10*z));self.assertEqual(s['absolute']-s['dp'],1000*p0)
            if h:
                a=model(rho,h,1,p0,.25);b=model(rho,h,1,p0,.75)
                self.assertAlmostEqual((b['dp']-a['dp'])/(b['z']-a['z']),10*rho)
    def test_force_and_moment_by_exact_strip_quadrature(self):
        # Simpson integra pressão linear e momento quadrático exatamente.
        for rho,h,w,p0 in itertools.product((500,1000,1500),(1,2,4),(.5,1,3),(80,120)):
            s=model(rho,h,w,p0);a=F(str(w));H=F(h);p=lambda z:F(rho)*10*z
            force=a*H/6*(p(0)+4*p(H/2)+p(H));moment=a*H/6*(0+4*(H/2)*p(H/2)+H*p(H))
            self.assertAlmostEqual(s['net'],float(force));self.assertAlmostEqual(s['center'],float(moment/force))
            self.assertAlmostEqual(s['one_side']-1000*p0*w*h,s['net'])
    def test_width_height_reference_and_query_invariants(self):
        s=model();self.assertEqual(model(width=2)['dp'],s['dp']);self.assertEqual(model(width=2)['net'],2*s['net'])
        self.assertEqual(model(height=4)['net'],4*s['net'])
        self.assertEqual(model(p0=120)['net'],s['net']);self.assertEqual(model(probe=0)['net'],s['net'])
        self.assertEqual(model(probe=0)['dp'],0)
    def test_zero_height_and_domain(self):
        s=model(height=0);self.assertEqual(s['area'],0);self.assertEqual(s['net'],0);self.assertEqual(s['one_side'],0);self.assertIsNone(s['center'])
        for args in ((0,2,1,100,1),(1000,-1,1,100,1),(1000,2,0,100,1),(1000,2,1,0,1),(1000,2,1,100,2),(1000,float('nan'),1,100,1)):
            with self.assertRaises(ValueError):model(*args)
