from decimal import Decimal as D, localcontext
import math
import unittest
from .model import R,log_ratio,rate_ratio,infer_ea

class ArrheniusTests(unittest.TestCase):
    def test_hand_derived_reference_case(self):
        self.assertAlmostEqual(log_ratio(6000*R,300,330),20/11,places=14)
        self.assertAlmostEqual(rate_ratio(6000*R,300,330),6.160647084304639,places=13)
        self.assertAlmostEqual(math.log(2)/(.002*rate_ratio(6000*R,300,330)),56.2560369937326,places=11)

    def test_independent_decimal_from_two_absolute_rates(self):
        # Compare with rates from A*exp(-Ea/(RT)), rather than the ratio identity.
        with localcontext() as ctx:
            ctx.prec=60
            r=D('8.314462618');a=D('1000000')
            for ea in (D('-12000'),D('0'),D('50000')):
                for t1 in (D('250'),D('300'),D('400')):
                    for t2 in (D('280'),D('330'),D('500')):
                        k1=a*(-ea/(r*t1)).exp();k2=a*(-ea/(r*t2)).exp()
                        expected=float(k2/k1)
                        self.assertAlmostEqual(rate_ratio(float(ea),float(t1),float(t2))/expected,1,places=12)
                        self.assertAlmostEqual(infer_ea(float(t1),float(k1),float(t2),float(k2)),float(ea),places=7)

    def test_inverse_composition_and_unit_invariance(self):
        ea=6000*R
        self.assertAlmostEqual(rate_ratio(ea,300,330)*rate_ratio(ea,330,300),1,places=14)
        self.assertAlmostEqual(log_ratio(ea,300,330)+log_ratio(ea,330,360),log_ratio(ea,300,360),places=14)
        k2=.002*rate_ratio(ea,300,330)
        for scale in (1/60,1,60,1000):
            self.assertAlmostEqual(infer_ea(300,.002*scale,330,k2*scale),ea,places=7)
        self.assertEqual(rate_ratio(0,300,330),1)
        self.assertEqual(rate_ratio(ea,300,300),1)
        self.assertLess(rate_ratio(-ea,300,330),1)

    def test_logarithm_preserves_extreme_comparisons(self):
        self.assertAlmostEqual(log_ratio(R*100000,100,1000),900)
        for ea in (R*100000,-R*100000):
            with self.assertRaises(ValueError):rate_ratio(ea,100,1000)
        # Ratio would overflow, but separate logarithms yield finite Ea.
        self.assertTrue(math.isfinite(infer_ea(300,1e-300,330,1e300)))

    def test_contracts(self):
        for bad in (True,'300',None):
            with self.assertRaises(TypeError):log_ratio(50000,bad,330)
        for bad in (0,-1,float('nan'),float('inf')):
            with self.assertRaises(ValueError):log_ratio(50000,bad,330)
        with self.assertRaises(ValueError):log_ratio(float('nan'),300,330)
        for bad in (0,-1,float('nan'),float('inf')):
            with self.assertRaises(ValueError):infer_ea(300,bad,330,.01)
        with self.assertRaises(ValueError):infer_ea(300,.002,300,.01)

if __name__=='__main__':unittest.main()
