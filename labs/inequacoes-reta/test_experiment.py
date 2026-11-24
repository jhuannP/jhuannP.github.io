import unittest,itertools
from fractions import Fraction as F
from .experiment import solve,contains,OPS

class LinearInequalityTests(unittest.TestCase):
    def test_original_expression_on_independent_rational_grid(self):
        # Comparação direta da expressão original, sem isolar a variável.
        relations={'<':lambda u,v:u<v,'<=':lambda u,v:u<=v,'>':lambda u,v:u>v,'>=':lambda u,v:u>=v}
        for a,b,c,op in itertools.product(range(-3,4),range(-4,5),range(-6,7),OPS):
            s=solve(a,b,c,op)
            for k in range(-24,25):
                x=F(k,2)
                self.assertEqual(contains(s,x),relations[op](a*x+b,F(c)),(a,b,c,op,x))
    def test_boundary_and_each_side(self):
        for a,b,c,op in itertools.product((-3,-2,-1,1,2,3),(-4,0,4),(-6,0,6),OPS):
            s=solve(a,b,c,op);q=s['boundary']
            self.assertEqual(a*q+b,c)
            self.assertEqual(contains(s,q),op in ('<=','>='))
            self.assertNotEqual(contains(s,q-F(1,7)),contains(s,q+F(1,7)))
            self.assertEqual(contains(s,q+1),s['operator'] in ('>','>='))
    def test_degenerate_cases_and_nonreversible_operation(self):
        for b,c,op in itertools.product(range(-4,5),range(-6,7),OPS):
            s=solve(0,b,c,op)
            self.assertIsNone(s['boundary'])
            self.assertEqual(contains(s,F(17,3)),contains(s,F(-1000)))
        self.assertEqual(solve(0,2,2,'<=')['kind'],'all')
        self.assertEqual(solve(0,2,2,'<')['kind'],'none')
        # Multiplicar por zero não preserva equivalência nem informação de ordem.
        self.assertTrue(-1<1);self.assertFalse(0*(-1)<0*1)
        self.assertTrue(1/F(-2)<1) # ilustra por que um denominador negativo não pode ser ignorado
    def test_contract_and_rational_coefficients(self):
        s=solve(F(1,2),F(1,3),F(5,6),'<=')
        self.assertEqual(s['boundary'],1);self.assertTrue(contains(s,1))
        for bad in (True,.5,'1/2',None):
            with self.assertRaises(ValueError):solve(bad,0,1)
            with self.assertRaises(ValueError):contains(s,bad)
        for op in ('=','<>',''):
            with self.assertRaises(ValueError):solve(1,0,1,op)
