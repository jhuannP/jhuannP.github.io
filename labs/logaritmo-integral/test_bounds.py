from fractions import Fraction as Q
from math import log
from itertools import product
import unittest
from .bounds import log_bounds

class LogIntegralTests(unittest.TestCase):
    def test_example(self):
        b=log_bounds(2,4)
        self.assertEqual(b['lower'],Q(533,840))
        self.assertEqual(b['upper'],Q(319,420))
        self.assertEqual(b['midpoint'],Q(1171,1680))
        self.assertEqual(b['max_midpoint_error'],Q(1,16))

    def test_reference_and_telescoping_width(self):
        for x,n in product((Q(1,8),Q(1,2),Q(1),Q(3,2),Q(2),Q(4)),(1,2,4,8,16)):
            b=log_bounds(x,n);a,c=min(Q(1),x),max(Q(1),x)
            self.assertEqual(b['upper']-b['lower'],(c-a)**2/(n*a*c))
            self.assertLessEqual(float(b['lower']),log(float(x))+1e-14)
            self.assertGreaterEqual(float(b['upper']),log(float(x))-1e-14)
            self.assertLessEqual(abs(float(b['midpoint'])-log(float(x))),float(b['max_midpoint_error'])+1e-14)

    def test_refinement_nested_and_oriented_integral(self):
        for x in (Q(1,8),Q(1,2),Q(2),Q(4)):
            for n in (1,2,4,8):
                a=log_bounds(x,n);b=log_bounds(x,2*n)
                self.assertGreaterEqual(b['lower'],a['lower'])
                self.assertLessEqual(b['upper'],a['upper'])
                self.assertEqual(b['upper']-b['lower'],(a['upper']-a['lower'])/2)
        z=log_bounds(1,5)
        self.assertEqual(set(z.values()),{Q(0)})
        self.assertLess(log_bounds(Q(1,2),4)['upper'],0)

    def test_first_sum_direct_rectangle_oracle(self):
        # For one strip the bounds depend only on endpoint heights.
        for x in (Q(1,4),Q(3,4),Q(2),Q(5)):
            b=log_bounds(x,1)
            endpoints=((x-1)/x,x-1)
            self.assertEqual(b['lower'],min(endpoints))
            self.assertEqual(b['upper'],max(endpoints))

    def test_contracts(self):
        for bad in (0,-1,True,1.,'1',None):
            with self.assertRaises(ValueError):log_bounds(bad,4)
        for bad in (0,-1,True,4.,'4',None):
            with self.assertRaises(ValueError):log_bounds(2,bad)

if __name__=='__main__':unittest.main()
