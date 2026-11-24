import unittest
from fractions import Fraction as Q
from itertools import product
from math import nextafter,inf
from .comparison import within

class ToleranceTests(unittest.TestCase):
    def test_zero_and_absolute_boundary(self):
        self.assertFalse(within(0,1e-8,rtol=1e-6,atol=0))
        self.assertTrue(within(0,1e-8,rtol=1e-6,atol=1e-7))
        self.assertTrue(within(0,.125,rtol=0,atol=.125))
        self.assertFalse(within(0,nextafter(.125,inf),rtol=0,atol=.125))
        self.assertTrue(within(3,3,rtol=0,atol=0))
        self.assertFalse(within(3,nextafter(3,inf),rtol=0,atol=0))

    def test_dyadic_grid_against_rational_inequality(self):
        values=[Q(i,8) for i in range(-8,9)]
        for a,b,r,t in product(values,values,[Q(0),Q(1,16),Q(1,4),Q(1,2)],[Q(0),Q(1,16),Q(1,4)]):
            expected=abs(a-b)<=max(t,r*max(abs(a),abs(b)))
            self.assertEqual(within(float(a),float(b),rtol=float(r),atol=float(t)),expected)
            self.assertEqual(within(float(b),float(a),rtol=float(r),atol=float(t)),expected)

    def test_unit_conversion_scales_absolute_tolerance(self):
        for a,b in product([i/8 for i in range(-8,9)],repeat=2):
            original=within(a,b,rtol=.0625,atol=.125)
            self.assertEqual(within(100*a,100*b,rtol=.0625,atol=12.5),original)
        self.assertTrue(within(1,1.0625,rtol=0,atol=.125))
        self.assertFalse(within(100,106.25,rtol=0,atol=.125))

    def test_not_transitive_and_not_a_format_comparison(self):
        self.assertTrue(within(100,101,rtol=.01,atol=0))
        self.assertTrue(within(101,102,rtol=.01,atol=0))
        self.assertFalse(within(100,102,rtol=.01,atol=0))
        a,b=1.0004,1.00049
        self.assertEqual(format(a,'.3f'),format(b,'.3f'))
        self.assertFalse(within(a,b,rtol=1e-6,atol=0))
        self.assertTrue(within(1e9,1e9+500,rtol=1e-6,atol=5))
        self.assertFalse(within(1e9,1e9+500,rtol=0,atol=5))
        self.assertFalse(within(1e308,-1e308,rtol=1e-6,atol=0))

    def test_contracts_and_conversion(self):
        for bad in (True,False,'1',None,1j,float('nan'),inf,-inf,10**400):
            for index in range(4):
                args=[1,1,1e-6,0];args[index]=bad
                with self.assertRaises(ValueError):within(args[0],args[1],rtol=args[2],atol=args[3])
        for r,t in ((-1,0),(1,0),(2,0),(0,-1)):
            with self.assertRaises(ValueError):within(1,1,rtol=r,atol=t)
        # Converting an integer to float can already round the input.
        self.assertTrue(within(2**53,2**53+1,rtol=0,atol=0))
