import unittest
from itertools import product
from fractions import Fraction as Q
from experiment import central, combine, extrapolate, perturbed, position


class RichardsonTests(unittest.TestCase):
    def test_polynomial_exactness(self):
        # Reference derivatives from coefficients, not from a finer grid.
        for a in product((-1,0,2),repeat=5):
            f=lambda x:sum(c*x**k for k,c in enumerate(a))
            for x,h in product((Q(-1),Q(0),Q(2)),(Q(1,4),Q(1,2))):
                derivative=sum(k*c*x**(k-1) for k,c in enumerate(a) if k)
                self.assertEqual(extrapolate(f,x,h),derivative)

    def test_fifth_degree_remainder(self):
        for h in (Q(1,2),Q(1,4),Q(1,8)):
            self.assertEqual(central(position,1,h),10+11*h*h+h**4)
            self.assertEqual(extrapolate(position,1,h)-10,-h**4/4)
            self.assertEqual((extrapolate(position,1,h)-10)/(extrapolate(position,1,h/2)-10),16)
        self.assertEqual(extrapolate(position,1,Q(1,2)),Q(639,64))

    def test_perturbation_bound(self):
        delta=Q(1,4000)
        for h in (Q(1,2),Q(1,4),Q(1,20)):
            ideal=extrapolate(position,1,h)
            for errors in product((-delta,Q(0),delta),repeat=4):
                result=perturbed(h,errors)
                self.assertLessEqual(abs(result-ideal),3*delta/h)
                self.assertLessEqual(abs(result-10),h**4/4+3*delta/h)
            self.assertEqual(perturbed(h,(delta,-delta,delta,-delta))-ideal,3*delta/h)
            self.assertEqual(perturbed(h,(-delta,delta,-delta,delta))-10,-h**4/4-3*delta/h)

    def test_order_and_contracts(self):
        self.assertEqual(combine(Q(13,4),Q(49,16)),3)
        self.assertEqual(combine(Q(13,4),Q(49,16),1),Q(23,8))
        for p in (True,0,-1,2.0,21):
            with self.assertRaises(ValueError): combine(1,2,p)
        for h in (0,-1,True,.1):
            with self.assertRaises(ValueError): central(position,1,h)
        with self.assertRaises(ValueError): combine(1.0,2)
        with self.assertRaises(ValueError): perturbed(Q(1,2),(0,0,0))


if __name__=='__main__': unittest.main()
