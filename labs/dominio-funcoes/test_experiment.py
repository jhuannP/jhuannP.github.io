import unittest,math,itertools
from fractions import Fraction as F
from .experiment import model

class FunctionDomainTests(unittest.TestCase):
    def test_constraints_and_values_by_independent_formulas(self):
        for a,x in itertools.product((-2,-1,0,1,2),range(-4,7)):
            s=model(0,a,x);valid=x>=a and x!=a+1
            self.assertEqual(s['defined'],valid)
            if valid:self.assertAlmostEqual(s['value'],math.sqrt(x-a)/(x-a-1))
            else:self.assertIsNone(s['value'])
            s=model(1,a,x)
            if x!=a:self.assertEqual(F(s['value']),F(x*x-a*a,x-a))
            else:self.assertIsNone(s['value']);self.assertEqual(s['candidate'],2*a)
            s=model(2,a,x);self.assertEqual(s['value']**2,(x-a)**2);self.assertGreaterEqual(s['value'],0)
            self.assertEqual(s['value']==s['candidate'],x>=a)
    def test_boundaries_and_neighbours_without_epsilon_exclusion(self):
        for a in (-2.,-1.,0.,1.,2.):
            self.assertTrue(model(0,a,a)['defined']);self.assertEqual(model(0,a,a)['value'],0)
            for point in (a+1,):
                self.assertFalse(model(0,a,point)['defined'])
                for direction in (-math.inf,math.inf):self.assertTrue(model(0,a,math.nextafter(point,direction))['defined'])
            for direction in (-math.inf,math.inf):self.assertTrue(model(1,a,math.nextafter(a,direction))['defined'])
    def test_cancellation_extension_and_absolute_counterexample(self):
        for a in (-2,-1,0,1,2):
            s=model(1,a,a);self.assertFalse(s['defined']);self.assertIsNotNone(s['candidate'])
            self.assertNotEqual(model(2,a,a-1)['value'],model(2,a,a-1)['candidate'])
        self.assertEqual(model(0,1,5)['reason'],'válido');self.assertEqual(model(0,1,0)['reason'],'radicando negativo');self.assertEqual(model(0,1,2)['reason'],'denominador zero')
    def test_domain_contract(self):
        for args in ((3,1,1),(True,1,1),(0,3,1),(0,1,7),(0,1,float('nan')),(0,float('inf'),1)):
            with self.assertRaises(ValueError):model(*args)
