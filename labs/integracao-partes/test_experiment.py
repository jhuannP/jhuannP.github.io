from math import exp,factorial,fsum
from decimal import Decimal,localcontext
import unittest
from .experiment import inspect

class IntegrationPartsTests(unittest.TestCase):
    def test_independent_power_series(self):
        # Integrate x exp(x) term by term; not the closed antiderivative.
        with localcontext() as ctx:
            ctx.prec=70
            for q in range(-20,21):
                b=Decimal(q)/10
                reference=sum((b**(n+2)/(Decimal(factorial(n))*(n+2)) for n in range(80)),Decimal(0))
                self.assertAlmostEqual(inspect(q)['integral'],float(reference),places=12)

    def test_quadrature_with_orientation(self):
        for q in [-20,-10,-1,0,1,10,20]:
            b=q/10;n=4096;h=b/n
            value=h/3*fsum((1 if i in (0,n) else 4 if i%2 else 2)*(i*h)*exp(i*h) for i in range(n+1))
            self.assertAlmostEqual(inspect(q)['integral'],value,places=11)
            self.assertGreaterEqual(inspect(q)['integral'],0)

    def test_product_derivative_and_endpoints(self):
        F=lambda x:(x-1)*exp(x)
        for x in [-2,-1,0,.5,1,2]:
            h=1e-5
            self.assertAlmostEqual((F(x+h)-F(x-h))/(2*h),x*exp(x),places=7)
        self.assertEqual(inspect(0)['integral'],0)
        self.assertEqual(inspect(10)['integral'],1)
        self.assertAlmostEqual(inspect(-10)['integral'],1-2/exp(1),places=14)
        self.assertAlmostEqual(inspect(20)['integral'],1+exp(2),places=13)

    def test_contracts(self):
        for q in [-21,21,True,None,.5,'10']:
            with self.assertRaises(ValueError):inspect(q)
