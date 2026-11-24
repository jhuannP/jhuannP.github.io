import importlib.util
import itertools
import unittest
from fractions import Fraction as F
from pathlib import Path
spec=importlib.util.spec_from_file_location('eqsteps',Path(__file__).with_name('experiment.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class EquationTests(unittest.TestCase):
    def test_exact_classification_and_substitution(self):
        expected=[('unique',4),('unique',7),('none',None),('all',None),('unique',2.5)]
        for case,step in itertools.product(range(5),range(4)):
            text,a,b,c,d=m.CASES[case][step]
            a,b,c,d=map(F,[a,b,c,d])
            kind,root=m.classify(a,b,c,d)
            self.assertEqual((kind,None if root is None else float(root)),expected[case])
            if kind=='unique':self.assertEqual(a*root+b,c*root+d)

    def test_solution_membership_invariant_over_steps(self):
        for case,candidate in itertools.product(range(5),[i/4 for i in range(-8,33)]):
            states=[m.model(case,step,candidate) for step in range(4)]
            self.assertTrue(all(r['satisfies']==states[0]['satisfies'] for r in states))
            for r in states:
                a,b,c,d=map(F,r['coefficients']);x=F(candidate)
                self.assertEqual(F(r['left']),a*x+b)
                self.assertEqual(F(r['right']),c*x+d)

    def test_allowed_operations_and_bad_cancellation(self):
        for a,b,c,d,x in itertools.product(range(-2,3),repeat=5):
            before=(a*x+b)==(c*x+d)
            for factor in [-3,-1,1,2]:
                self.assertEqual(before,factor*(a*x+b)==factor*(c*x+d))
            self.assertEqual(before,(a*x+b+2*x-7)==(c*x+d+2*x-7))
        # Dividir x(x−1)=0 por x perde a solução zero.
        self.assertEqual(0*(0-1),0)
        self.assertNotEqual(0-1,0)
        # Multiplicar por zero transforma a contradição 1=3 numa identidade.
        self.assertNotEqual(1,3);self.assertEqual(0*1,0*3)

    def test_domain_and_non_integer_root(self):
        self.assertEqual(m.model(4,3,2.5)['root'],2.5)
        self.assertTrue(m.model(3,0,-2)['satisfies'])
        self.assertFalse(m.model(2,3,8)['satisfies'])
        for args in [(5,0,4),(0,4,4),(0,0,float('nan')),(0,0,9)]:
            with self.assertRaises(ValueError):m.model(*args)

if __name__=='__main__':unittest.main()
