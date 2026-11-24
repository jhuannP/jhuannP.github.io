import math
import unittest
from decimal import Decimal, localcontext
from .scales import log_ratio, coordinates, secants

class ScalesTests(unittest.TestCase):
    def test_independent_decimal_logs(self):
        with localcontext() as c:
            c.prec=60
            for v in (0.125,0.5,1,3,16,69):
                for ref in (0.25,1,8):
                    for base in (2,10):
                        exact=(Decimal(str(v))/Decimal(str(ref))).ln()/Decimal(base).ln()
                        self.assertAlmostEqual(log_ratio(v,ref,base),float(exact),places=12)

    def test_exponential_power_and_units(self):
        for A in (1,3,64):
            for n in (-2,-1,1,2,3):
                xs=(1,2,4,8)
                pts=[(x,A*x**n) for x in xs]
                for base in (2,10,math.e):
                    for slope in secants(coordinates(pts,"dilog",base=base)):
                        self.assertAlmostEqual(slope,n,places=12)
                    # Changing both numerical units and their references preserves log coordinates.
                    changed=[(100*x,1000*y) for x,y in pts]
                    for a,b in zip(coordinates(pts,"dilog",base=base),coordinates(changed,"dilog",100,1000,base)):
                        for p,q in zip(a,b): self.assertAlmostEqual(p,q,places=12)
        pts=[(t,64*2**(-t/2)) for t in (0,2,4,6)]
        for s in secants(coordinates(pts,"monolog",base=2)): self.assertAlmostEqual(s,-0.5)

    def test_offset_and_residuals(self):
        pts=[(t,5+64*2**(-t/2)) for t in (0,2,4,6)]
        slopes=secants(coordinates(pts,"monolog",base=2))
        self.assertTrue(slopes[0]<slopes[1]<slopes[2]<0)
        corrected=[(x,y-5) for x,y in pts]
        for s in secants(coordinates(corrected,"monolog",base=2)): self.assertAlmostEqual(s,-0.5)
        self.assertEqual((2-1)**2,(11-10)**2)
        self.assertGreater(log_ratio(2,1)**2,log_ratio(11,10)**2)

    def test_domains_and_zero(self):
        self.assertEqual(coordinates([(0,-1),(1,0)],"linear"),[(0,-1),(1,0)])
        self.assertEqual(coordinates([(0,1)],"monolog"),[(0,0)])
        for v in (0,-1,True,float("nan"),float("inf"),"2"):
            with self.assertRaises(ValueError): log_ratio(v)
        for base in (0,-2,1):
            with self.assertRaises(ValueError): log_ratio(2,base=base)
        with self.assertRaises(ValueError): coordinates([(0,1)],"dilog")
        with self.assertRaises(ValueError): coordinates([(1,0)],"monolog")
        with self.assertRaises(ValueError): coordinates([(1,1)],"log")
        with self.assertRaises(ValueError): secants([(1,1),(1,2)])
