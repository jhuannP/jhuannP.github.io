import unittest
from fractions import Fraction as Q
from .experiment import bracket,finite_sequence,absolute_bounds

class RealTests(unittest.TestCase):
    def test_nested_brackets_by_squared_order(self):
        previous=bracket(0)
        for n in range(41):
            r=bracket(n)
            self.assertLess(r['lower']**2,2)
            self.assertGreater(r['upper']**2,2)
            self.assertEqual(r['width'],Q(1,2**n))
            self.assertGreaterEqual(r['lower'],previous['lower'])
            self.assertLessEqual(r['upper'],previous['upper'])
            previous=r
        self.assertEqual(bracket(1)['upper'],Q(3,2))

    def test_finite_maximum_is_not_infinite_supremum(self):
        for n in range(1,101):
            r=finite_sequence(n)
            self.assertEqual(r['maximum'],1-Q(1,n))
            self.assertNotIn(Q(1),r['values'])
            self.assertEqual(r['gap_to_one'],Q(1,n))
        # Para qualquer M<1 racional, construir um termo maior que M.
        for M in (Q(0),Q(9,10),Q(99,100),Q(999,1000)):
            n=(1/(1-M)).numerator//(1/(1-M)).denominator+1
            self.assertGreater(1-Q(1,n),M)

    def test_triangle_and_reverse_triangle(self):
        for i in range(-12,13):
            for j in range(-12,13):
                self.assertEqual(absolute_bounds(Q(i,3),Q(j,4)),(True,True))
        self.assertEqual(abs(Q(3)+Q(-3)),0)
        self.assertNotEqual(abs(Q(3)+Q(-3)),abs(Q(3))+abs(Q(-3)))

    def test_contracts(self):
        for n in (-1,41,True,.5):
            with self.assertRaises(ValueError):bracket(n)
        for n in (0,1001,True):
            with self.assertRaises(ValueError):finite_sequence(n)
        with self.assertRaises(ValueError):absolute_bounds(.1,1)

if __name__=='__main__':unittest.main()
