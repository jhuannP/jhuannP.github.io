import unittest
from fractions import Fraction as Q
from .experiment import product_derivative,quotient_derivative,quotient_increment,cancelled_value,quotient_value

class RuleTests(unittest.TestCase):
    def test_product_against_expanded_polynomial(self):
        # x²(x+1)=x³+x²: derivar coeficientes é uma referência independente.
        coefficients=[0,0,1,1]
        for numerator in range(-20,21):
            x=Q(numerator,4)
            expected=sum(i*c*x**(i-1) for i,c in enumerate(coefficients) if i)
            self.assertEqual(product_derivative(x),expected)
        self.assertEqual(product_derivative(2),16)
        self.assertNotEqual(product_derivative(2),2*Q(2))

    def test_quotient_against_division_identity(self):
        # (x²+1)/(x+1)=x−1+2/(x+1), x≠−1.
        for numerator in range(-20,21):
            x=Q(numerator,4)
            if x==-1:continue
            self.assertEqual(quotient_value(x),x-1+2/(x+1))
            self.assertEqual(quotient_derivative(x),1-2/(x+1)**2)
        self.assertEqual(quotient_derivative(0),-1)
        self.assertEqual(quotient_derivative(1),Q(1,2))

    def test_increment_exact_error_identity(self):
        for x in (Q(-2),Q(0),Q(1),Q(2)):
            for h in (Q(1,10),Q(-1,10),Q(1,100)):
                error=2*h/((x+1)**2*(x+h+1))
                self.assertEqual(quotient_increment(x,h)-quotient_derivative(x),error)
        for x in (-2,0,2,3):self.assertEqual(cancelled_value(x),x+1)

    def test_domain_and_contracts(self):
        for fn in (quotient_value,quotient_derivative):
            with self.assertRaises(ValueError):fn(-1)
        with self.assertRaises(ValueError):cancelled_value(1)
        with self.assertRaises(ValueError):quotient_increment(0,-1)
        with self.assertRaises(ValueError):quotient_increment(0,0)
        for x in (True,.1):
            with self.assertRaises(ValueError):product_derivative(x)

if __name__=='__main__':unittest.main()
