import unittest,math,itertools
from fractions import Fraction as F
from .experiment import model

class VesicleLeafletTests(unittest.TestCase):
    def test_independent_surface_integral_and_volumes(self):
        # Integral de faixa esférica: 2πR² integral_0^π sinθ dθ =4πR².
        for r,d in itertools.product(range(10,101,10),(2,4,6)):
            m=model(r,d)
            for radius,key in ((r,'inner_area'),(r+d,'outer_area')):
                n=2000;h=math.pi/n
                integral=h*sum(math.sin((k+.5)*h) for k in range(n))
                area=2*math.pi*radius**2*integral
                self.assertLess(abs(area/m[key]-1),2e-7)
            self.assertAlmostEqual(m['lumen_volume']+m['shell_volume'],4*math.pi*(r+d)**3/3,places=7)
    def test_exact_ratios_and_conditional_molecule_fraction(self):
        for r,d in itertools.product(range(10,101,10),(2,4,6)):
            m=model(r,d);ratio=F((r+d)**2,r*r)
            self.assertEqual(m['ratio'],float(ratio))
            self.assertEqual(m['relative_excess'],float(2*F(d,r)+F(d,r)**2))
            self.assertEqual(m['outer_fraction'],float(ratio/(1+ratio)))
        self.assertEqual(model(10,4)['ratio'],1.96)
        self.assertEqual(model(20,4)['ratio'],1.44)
    def test_refinement_and_common_scale(self):
        for d in (2,4,6):
            values=[model(r,d)['ratio'] for r in range(10,101,10)]
            self.assertTrue(all(a>b for a,b in zip(values,values[1:])))
        a=model(10,2);b=model(20,4)
        self.assertEqual(a['ratio'],b['ratio'])
        self.assertAlmostEqual(b['inner_area']/a['inner_area'],4)
        self.assertAlmostEqual(b['lumen_volume']/a['lumen_volume'],8)
    def test_domain_and_universal_geometric_inequalities(self):
        for r,d in itertools.product(range(10,101,10),(2,4,6)):
            m=model(r,d);self.assertGreater(m['outer_area'],m['inner_area'])
            self.assertTrue(.5<m['outer_fraction']<1)
        for args in [(0,4),(15,4),(110,4),(20,0),(20,3),(True,4),(20,False),(20.0,4)]:
            with self.assertRaises(ValueError):model(*args)
