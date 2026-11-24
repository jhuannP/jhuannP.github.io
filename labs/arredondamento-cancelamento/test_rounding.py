import unittest
from fractions import Fraction as Q
from math import ulp,nextafter,inf
from sys import float_info
from itertools import permutations
from .rounding import compare_expression,compare_sum


class RoundingTests(unittest.TestCase):
    def test_binary_format_and_lost_increment(self):
        self.assertEqual((float_info.radix,float_info.mant_dig),(2,53))
        self.assertEqual(ulp(1.0),2.0**-52)
        self.assertEqual(nextafter(1.0,inf)-1,2.0**-52)
        x=2.0**-54;q=Q(1,2**54)
        r=compare_expression(x)
        self.assertEqual(1.0+x,1.0)
        self.assertEqual(r['naive'],0.0)
        self.assertEqual(r['naive_error']['relative'],1)
        self.assertEqual(r['reformulated'],2*x)
        self.assertEqual(r['reformulated_error']['relative'],q/(2+q))

    def test_rational_reference_and_small_scale_grid(self):
        # Independent reference via expanded exact square, not rounded (1+x).
        samples=[2.0**-k for k in range(2,1001)]+[0.0,nextafter(0.0,1.0),nextafter(.25,0.0)]
        for x in samples:
            q=Q.from_float(x);r=compare_expression(x)
            self.assertEqual(r['reference'],(1+q)**2-1)
            if x:
                self.assertLessEqual(r['reformulated_error']['relative'],Q(1,2**51))
            else:self.assertIsNone(r['reformulated_error']['relative'])

    def test_exactly_representable_cases(self):
        for x in [.25,.125,.0625]:
            r=compare_expression(x)
            self.assertEqual(r['naive_error']['absolute'],0)
            self.assertEqual(r['reformulated_error']['absolute'],0)

    def test_sum_orders_and_input_information(self):
        seen=set()
        for values in permutations([1e16,1.0,-1e16]):
            r=compare_sum(values)
            self.assertEqual(r['reference'],1)
            self.assertEqual(r['fsum'],1)
            seen.add(r['naive'])
        self.assertEqual(seen,{0,1})
        rounded=1e16+1.0
        self.assertEqual(compare_sum([rounded,-1e16])['reference'],0)
        self.assertEqual(compare_sum([rounded,-1e16])['fsum'],0)
        self.assertEqual(Q.from_float(.1)-Q(1,10),Q(1,180143985094819840))

    def test_zero_reference_and_contracts(self):
        r=compare_sum([1.,-1.]);self.assertEqual(r['reference'],0)
        self.assertIsNone(r['fsum_error']['relative'])
        self.assertEqual(compare_sum([])['fsum'],0)
        for value in [True,1,'0.1',Q(1,10),float('nan'),inf,-.1,nextafter(.25,inf)]:
            with self.subTest(value=value),self.assertRaises(ValueError):compare_expression(value)
        for value in [[1],[True],['1'],[inf],None]:
            with self.assertRaises(ValueError):compare_sum(value)
        with self.assertRaises(OverflowError):compare_sum([1e308,1e308])

if __name__=='__main__':unittest.main()
