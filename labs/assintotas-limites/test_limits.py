import unittest
from fractions import Fraction as Q
from .limits import original,error,positive_integer_cutoff,crossing,reciprocal,hole,oblique,first_derivative,second_derivative


class AsymptoteTests(unittest.TestCase):
    def test_original_and_error_identity(self):
        for x in [Q(i,7) for i in range(-100,101)]+[10**1000,-10**1000]:
            self.assertEqual(original(x)-2,-error(x))
            self.assertLess(original(x),2);self.assertEqual(original(-x),original(x))
        self.assertEqual(original(0),Q(1,3));self.assertEqual(error(10),Q(5,103))

    def test_cutoff_independent_integer_search(self):
        for eps in [Q(1,i) for i in range(1,201)]+[Q(5,3),Q(2),Q(100)]:
            expected=1
            while abs((2*expected**2+1)/Q(expected**2+3)-2)>=eps:expected+=1
            n=positive_integer_cutoff(eps);self.assertEqual(n,expected)
            for offset in (0,Q(1,10),1,100):
                self.assertLess(error(n+offset),eps);self.assertLess(error(-n-offset),eps)
        self.assertEqual(positive_integer_cutoff(Q(1,100)),23)

    def test_crossing_hole_and_poles(self):
        self.assertEqual(crossing(0),2)
        for n in range(1,21):
            self.assertLess(crossing(-n),2);self.assertGreater(crossing(n),2)
            self.assertLessEqual(abs(crossing(n)-2),Q(1,n))
            self.assertEqual(reciprocal(Q(1,n)),n);self.assertEqual(reciprocal(Q(-1,n)),-n)
            for x in (1+Q(1,n),1-Q(1,n)):
                self.assertEqual(hole(x),x+1)
        for x in [Q(i,3) for i in range(-30,31) if i!=-3]:
            self.assertEqual(oblique(x)-x,1/(x+1))

    def test_derivatives_by_polynomial_quotient(self):
        for x in [Q(i,10) for i in range(-100,101)]:
            num=2*x*x+1;den=x*x+3
            d1=(4*x*den-num*2*x)/(den*den)
            d2=(10*den**2-10*x*2*den*2*x)/den**4
            self.assertEqual(first_derivative(x),d1)
            self.assertEqual(second_derivative(x),d2)
        self.assertEqual(first_derivative(0),0)
        self.assertEqual(second_derivative(1),0);self.assertEqual(second_derivative(-1),0)
        self.assertEqual(original(1),Q(3,4))

    def test_contracts(self):
        for f in [original,error,crossing,reciprocal,hole,oblique,first_derivative,second_derivative]:
            for invalid in (True,1.0,'1'):
                with self.assertRaises(ValueError):f(invalid)
        for eps in (0,-1,True,0.01):
            with self.assertRaises(ValueError):positive_integer_cutoff(eps)
        with self.assertRaises(ValueError):reciprocal(0)
        with self.assertRaises(ValueError):hole(1)
        with self.assertRaises(ValueError):oblique(-1)
