import unittest,math
from fractions import Fraction as Q
from .power_log import partial,derivative_partial,uniform_bound,first_sufficient

class PowerLogTests(unittest.TestCase):
    def test_reference_and_certified_count(self):
        self.assertEqual(partial(Q(1,2),3),Q(2,3))
        self.assertEqual(uniform_bound(Q(1,2),3),Q(1,32))
        self.assertEqual(uniform_bound(Q(1,2),7),Q(1,1024))
        self.assertEqual(first_sufficient(Q(1,2),Q(1,1000)),7)
        self.assertGreaterEqual(uniform_bound(Q(1,2),6),Q(1,1000))
        self.assertEqual(first_sufficient(Q(1,2),Q(1,32),False),3)
        self.assertEqual(first_sufficient(Q(1,2),Q(1,32),True),4)
    def test_finite_geometric_identity(self):
        for j in range(-8,8):
            x=Q(j,8)
            for n in range(9):
                d=derivative_partial(x,n)
                self.assertEqual((1-x)*d,1-x**n)
                # Closed form independently from summation loops.
                self.assertEqual(d,(1-x**n)/(1-x))
                if n:
                    self.assertEqual(partial(x,n)-partial(x,n-1),x**n/n)
        for n in range(1,10):
            self.assertEqual(derivative_partial(-1,n),n%2)
    def test_uniform_bound_against_independent_log(self):
        for r in (Q(1,4),Q(1,2),Q(3,4)):
            for j in range(-4,5):
                x=r*Q(j,4)
                for n in (0,1,3,7,12):
                    error=abs(-math.log1p(-float(x))-float(partial(x,n)))
                    self.assertLessEqual(error,float(uniform_bound(r,n))+2e-15)
        self.assertEqual(first_sufficient(0,Q(1,100000)),0)
    def test_remainder_by_independent_quadrature(self):
        # Simpson of the exact integral remainder, not another partial sum.
        cells=2000
        for x in (-1.0,-0.5,0.5,0.75):
            for n in (1,3,7):
                step=x/cells
                integral=0.0
                for j in range(cells+1):
                    t=j*step;weight=1 if j in (0,cells) else (4 if j%2 else 2)
                    integral+=weight*t**n/(1-t)
                integral*=step/3
                reference=-math.log1p(-x)-float(partial(Q(str(x)),n))
                self.assertAlmostEqual(integral,reference,delta=2e-12)
                if x==-1.0:
                    self.assertTrue(1/(2*(n+1))<=abs(integral)<=1/(n+1))
                    self.assertGreater(integral,0) # n odd -> (-1)^(n+1) positive.
    def test_contracts_and_search_budget(self):
        for n in (-1,513,True,1.0):
            with self.assertRaises(ValueError): partial(Q(1,2),n)
        for r in (-1,1,2,0.5,True):
            with self.assertRaises(ValueError): uniform_bound(r,3)
        for tol in (0,-1,True,0.001):
            with self.assertRaises(ValueError): first_sufficient(Q(1,2),tol)
        self.assertIsNone(first_sufficient(Q(99,100),Q(1,10**50)))
        self.assertEqual(partial(1,0),0)
