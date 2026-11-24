from fractions import Fraction as Q
from decimal import Decimal as D,localcontext
from math import log
import unittest
from .experiment import inspect,half_life

class RateOrders(unittest.TestCase):
    def test_exact_rational_and_decimal_references(self):
        with localcontext() as ctx:
            ctx.prec=70
            for j in range(61):
                u=Q(j,20);z=inspect(float(u))
                self.assertAlmostEqual(z['concentrations'][0],float(max(1-u,0)),places=14)
                self.assertAlmostEqual(z['concentrations'][2],float(1/(1+u)),places=14)
                reference=(-D(j)/20).exp()
                self.assertAlmostEqual(z['concentrations'][1],float(reference),places=14)
                for a,p in zip(z['concentrations'],z['products']):self.assertAlmostEqual(a+p,1,places=14)
                self.assertIsNone(z['rates'][0]) if u==1 else self.assertEqual(z['rates'][0],1 if u<1 else 0)

    def test_separation_integrals_independent(self):
        # Integra du=-da/a^n por Simpson para obter o tempo a partir da fração alvo.
        for target in [.2,.4,.6,.8]:
            for order in (0,1,2):
                expected_u=1-target if order==0 else -log(target) if order==1 else 1/target-1
                if expected_u>3:continue
                N=4096;h=(1-target)/N
                integral=h/3*sum((1 if j in (0,N) else 4 if j%2 else 2)/(target+j*h)**order for j in range(N+1))
                self.assertAlmostEqual(integral,expected_u,places=10)
                self.assertAlmostEqual(inspect(expected_u)['concentrations'][order],target,places=12)

    def test_half_lives_scaling_and_zero_boundary(self):
        for A0,k in [(1,1),(2,.5),(4,2)]:
            self.assertEqual(half_life(0,2*A0,k),2*half_life(0,A0,k))
            self.assertEqual(half_life(1,2*A0,k),half_life(1,A0,k))
            self.assertEqual(half_life(2,2*A0,k),half_life(2,A0,k)/2)
        eps=1e-6
        left=(inspect(1)['concentrations'][0]-inspect(1-eps)['concentrations'][0])/eps
        right=(inspect(1+eps)['concentrations'][0]-inspect(1)['concentrations'][0])/eps
        self.assertAlmostEqual(left,-1,places=8);self.assertEqual(right,0)
        self.assertEqual(inspect(3)['concentrations'][0],0)
        self.assertGreater(inspect(3)['concentrations'][1],0)
        self.assertGreater(inspect(3)['concentrations'][2],0)

    def test_contracts(self):
        for u in [-1,4,True,float('nan'),'1']:
            with self.assertRaises(ValueError):inspect(u)
        for args in [(3,1,1),(True,1,1),(1,0,1),(1,1,0),(2,1,float('inf'))]:
            with self.assertRaises(ValueError):half_life(*args)
