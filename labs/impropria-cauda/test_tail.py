import unittest
from fractions import Fraction as Q
from decimal import Decimal,localcontext
from numerics import trapezio,simpson
from .tail import cutoff,minimum_cutoff,regularized,first_transform_at_square,finite_comparison,RULES


class ImproperTests(unittest.TestCase):
    def test_cutoffs_and_budget(self):
        self.assertEqual(cutoff(10),dict(R=100,tail=Q(23,100),partial=Q(477,100)))
        self.assertEqual(cutoff(20)['tail'],Q(43,400))
        info=minimum_cutoff(Q(1,100));self.assertEqual((info['n'],info['R']),(202,40804))
        self.assertLessEqual(info['tail'],Q(1,100));self.assertGreater(cutoff(201)['tail'],Q(1,100))
        for n in (1,2,5,10,50,100,10000):
            self.assertEqual(cutoff(n)['partial']+cutoff(n)['tail'],5)

    def test_antiderivative_decimal(self):
        # Independent primitive -2/sqrt(x)-3/x, at square integer endpoints.
        with localcontext() as ctx:
            ctx.prec=60
            for n in (1,2,3,7,10,20,57,100):
                R=Decimal(n*n);primitive=-2/R.sqrt()-3/R
                expected=primitive+5
                actual=cutoff(n)['partial'];target=Decimal(actual.numerator)/Decimal(actual.denominator)
                self.assertLess(abs(expected-target),Decimal('1e-55'))

    def test_jacobian_and_regular_endpoint(self):
        for denominator in range(1,25):
            t=Q(1,denominator)
            self.assertEqual(first_transform_at_square(t)*2*t,regularized(t))
        self.assertEqual(regularized(0),2)
        with self.assertRaises(ValueError):first_transform_at_square(0)
        for panels in (2,4,8,16,32):
            self.assertEqual(RULES.rules(regularized,panels),(5,5))
        self.assertNotEqual(Q(1,4)+Q(3,5),5)  # Omitting dx/dt would integrate t³+3t⁴.

    def test_signed_error_decomposition(self):
        for panels in (10,100,1000):
            r=finite_comparison(10,panels)
            self.assertAlmostEqual(r['signed_total_error'],r['tail']-r['quadrature_error'],places=12)
            self.assertGreater(r['quadrature_error'],0)  # Positive convex integrand, trapezoid overestimate.
        self.assertLess(finite_comparison(10,10)['signed_total_error'],0)
        self.assertGreater(finite_comparison(10,1000)['signed_total_error'],0)
        # More panels alter finite quadrature error, never the fixed R100 tail.
        self.assertEqual(finite_comparison(10,10)['tail'],finite_comparison(10,1000)['tail'])

    def test_old_material_and_contracts(self):
        R=10;cut=trapezio(lambda x:1/x**2,1,R,1000);transformed=simpson(lambda t:1,0,1,2)
        self.assertLess(abs(cut-.9),1e-4);self.assertEqual(transformed,1)
        self.assertEqual((1/10,1/20),(.1,.05))
        for n in (0,10001,True,2.):
            with self.assertRaises(ValueError):cutoff(n)
        for eps in (0,-1,Q(1,10**8)):
            with self.assertRaises(ValueError):minimum_cutoff(eps)
        with self.assertRaises(TypeError):minimum_cutoff(.01)
        with self.assertRaises(ValueError):regularized(-1)
        with self.assertRaises(ValueError):finite_comparison(1,10)
