import unittest,itertools,math
from fractions import Fraction as F
from .experiment import model

class FractionUnitsTests(unittest.TestCase):
    def test_fraction_reference_all_panel_states(self):
        for p,q,r,s in itertools.product(range(7),range(1,7),range(7),range(1,7)):
            a=model(p,q,r,s);ref=F(p,q)+F(r,s)
            self.assertEqual((a['numerator'],a['denominator']),(ref.numerator,ref.denominator))
            self.assertEqual(F(a['a'],a['common']),F(p,q));self.assertEqual(F(a['b'],a['common']),F(r,s))
            self.assertGreaterEqual(a['extent'],ref);self.assertLess(a['extent']-ref,1) if ref else self.assertEqual(a['extent'],1)
    def test_least_common_multiple_by_search(self):
        for q,s in itertools.product(range(1,7),repeat=2):
            a=model(1,q,1,s);expected=next(x for x in range(1,q*s+1) if x%q==0 and x%s==0)
            self.assertEqual(a['common'],expected)
            self.assertEqual(math.gcd(a['numerator'],a['denominator']),1)
    def test_exchange_equivalence_zero_and_improper(self):
        for p,q,r,s in itertools.product(range(7),range(1,7),range(7),range(1,7)):
            a=model(p,q,r,s);b=model(r,s,p,q)
            self.assertEqual((a['numerator'],a['denominator']),(b['numerator'],b['denominator']))
        self.assertEqual(model(0,3,0,4)['denominator'],1)
        self.assertEqual(model(6,1,6,1)['extent'],12)
        self.assertEqual(model(2,6,2,4)['numerator'],5)
        self.assertEqual(model(2,6,2,4)['denominator'],6)
    def test_domains(self):
        for args in ((1,0,1,4),(1,-1,1,4),(7,1,1,1),(True,1,1,1),(1,2.0,1,4),(1,3,-1,4)):
            with self.assertRaises(ValueError):model(*args)
