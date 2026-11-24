import unittest
from math import tanh,sqrt
from .response import response

class ResponseTests(unittest.TestCase):
    def test_zero_field_and_two_levels(self):
        for n in range(21):
            a=response(n,2,0)
            self.assertAlmostEqual(a['moment'],0)
            self.assertAlmostEqual(a['slope'],a['curie_slope'])
            self.assertAlmostEqual(a['effective']**2,3*a['slope'])
        for x in (-10,-1,-.01,0,.01,1,10):
            self.assertAlmostEqual(response(1,2,x)['moment'],tanh(x))
        self.assertAlmostEqual(response(4,2,0)['effective'],sqrt(24))
        self.assertEqual(response(4,2,0)['saturation'],4)
    def test_525_normalized_bounded_odd_cases(self):
        for n in range(21):
            for i in range(-12,13):
                x=i/4;a=response(n,1.7,x);b=response(n,1.7,-x)
                self.assertAlmostEqual(sum(a['probabilities']),1)
                self.assertTrue(all(0<=p<=1 for p in a['probabilities']))
                self.assertLessEqual(abs(a['moment']),a['saturation']+1e-12)
                self.assertAlmostEqual(a['moment'],-b['moment'])
                self.assertGreaterEqual(a['slope'],0)
    def test_fluctuation_slope_and_limits(self):
        for n in (1,2,4,9):
            for x in (-1,-.1,0,.1,1):
                h=1e-5
                diff=(response(n,2,x+h)['moment']-response(n,2,x-h)['moment'])/(2*h)
                self.assertAlmostEqual(diff,response(n,2,x)['slope'],places=7)
        self.assertAlmostEqual(response(4,2,1000)['moment'],4)
        self.assertAlmostEqual(response(4,2,-1000)['moment'],-4)
        self.assertEqual(response(0,2,1000)['moment'],0)
        self.assertGreater(abs(response(4,2,1)['moment']-8),4)
    def test_contracts(self):
        for args in [(True,2,0),(-1,2,0),(21,2,0),(1.5,2,0),(4,0,0),(4,2,float('nan')),(4,2,1001),(4,True,0)]:
            with self.assertRaises(ValueError):response(*args)
