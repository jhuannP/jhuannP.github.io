from fractions import Fraction as Q
import unittest
from .examples import value,satisfies

class RationalInequalities(unittest.TestCase):
    def test_solution_sets_against_expression(self):
        for x in (Q(i,7) for i in range(-500,501)):
            self.assertEqual(satisfies(value(x)),x<-2 or x>=1)
            self.assertEqual(satisfies(value(x),True),x<-2 or x>1)
            self.assertEqual(satisfies(value(x,'hole')),x>=-1 and x!=2)
            self.assertEqual(satisfies(value(x,'double'),True),x>-2 and x!=1)

    def test_boundaries_without_rounding(self):
        for power in (1,10,30,100):
            eps=Q(1,10**power)
            self.assertGreater(value(-2-eps),0);self.assertLess(value(-2+eps),0)
            self.assertLess(value(1-eps),0);self.assertGreater(value(1+eps),0)
            self.assertGreater(value(1-eps,'double'),0);self.assertGreater(value(1+eps,'double'),0)
        self.assertIsNone(value(-2));self.assertEqual(value(1),0)
        self.assertTrue(satisfies(value(1)));self.assertFalse(satisfies(value(1),True))
        self.assertFalse(satisfies(value(-2)))

    def test_cancellation_preserves_domain(self):
        self.assertIsNone(value(2,'hole'));self.assertEqual(2+1,3)
        for x in (Q(i,9) for i in range(-50,51)):
            if x!=2:self.assertEqual(value(x,'hole'),x+1)
        self.assertTrue(satisfies(value(-1,'hole')))
        self.assertFalse(satisfies(value(2,'hole')))

    def test_positive_square_equivalence_and_counterexample(self):
        for x in (Q(i,5) for i in range(-100,101)):
            if x!=-2:
                self.assertEqual(value(x)*(x+2)**2,(x-1)*(x+2))
                self.assertEqual(satisfies(value(x)),(x-1)*(x+2)>=0)
        self.assertGreater(value(-3),0);self.assertFalse(-3>=1)
        # Product inequality alone includes the prohibited pole: keep domain.
        self.assertEqual((-2-1)*(-2+2),0);self.assertFalse(satisfies(value(-2)))

    def test_contracts_and_extremes(self):
        for bad in (True,.5,'1/2',None):
            with self.assertRaises(TypeError):value(bad)
        with self.assertRaises(ValueError):value(0,'unknown')
        with self.assertRaises(TypeError):satisfies(Q(1),1)
        for x in (-10**100,10**100):self.assertGreater(value(x),0)
        self.assertFalse(satisfies(None));self.assertFalse(satisfies(None,True))

if __name__=='__main__':unittest.main()
