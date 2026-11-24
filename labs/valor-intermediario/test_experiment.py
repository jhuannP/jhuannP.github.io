import unittest
from fractions import Fraction as Q
from .experiment import value,interval_trace,extrema,oscillation

class ExistenceTests(unittest.TestCase):
    def test_continuous_bracket_and_exact_root(self):
        for n in range(13):
            r=interval_trace(0,n)
            self.assertEqual(r['width'],Q(1,2**n))
            self.assertLess(value(0,r['a']),0);self.assertGreater(value(0,r['b']),0)
        self.assertEqual(interval_trace(0,1)['b'],Q(3,2))
        for root in (-1,0,1):self.assertEqual(value(1,root),0)
        self.assertEqual(interval_trace(1,8)['mid'],0)

    def test_jump_has_no_zero_despite_small_bracket(self):
        for n in range(13):
            r=interval_trace(2,n)
            self.assertEqual(r['width'],Q(2,2**n))
            self.assertEqual(abs(r['residual']),1)
            self.assertEqual(value(2,r['a']),-1);self.assertEqual(value(2,r['b']),1)

    def test_envelopes_and_extreme_sequences(self):
        for p in (0,1,2):
            for x in (-.25,-.1,-.01,.01,.1,.25):
                self.assertLessEqual(abs(oscillation(x,p)),abs(x)**p)
            for n in (1,2,5,10,20,100):
                r=extrema(n,p)
                self.assertAlmostEqual(oscillation(r['plus'],p),r['positive'])
                self.assertAlmostEqual(oscillation(r['minus'],p),r['negative'])
        self.assertEqual(extrema(100,0)['positive'],1)
        self.assertEqual(extrema(100,0)['negative'],-1)
        self.assertLess(extrema(20,2)['positive'],extrema(1,2)['positive'])

    def test_contracts(self):
        for n in (-1,17,True):
            with self.assertRaises(ValueError):interval_trace(0,n)
        with self.assertRaises(ValueError):value(3,0)
        with self.assertRaises(ValueError):value(0,.5)
        for x in (0,True,float('inf')):
            with self.assertRaises(ValueError):oscillation(x)
        with self.assertRaises(ValueError):extrema(0)

if __name__=='__main__':unittest.main()
