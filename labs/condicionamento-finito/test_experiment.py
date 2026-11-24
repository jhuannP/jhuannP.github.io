import unittest,itertools
from fractions import Fraction as F
from .experiment import inspect

class ConditioningTests(unittest.TestCase):
    def test_enumerated_equiprobable_atoms(self):
        for counts in itertools.product(range(4),repeat=4):
            s=inspect(*counts);atoms=[(i<2,i in (0,2)) for i,n in enumerate(counts) for _ in range(n)]
            if not atoms:self.assertIsNone(s['pA']);continue
            aa=[u for u,v in atoms if u];bb=[v for u,v in atoms if v];both=sum(u and v for u,v in atoms)
            self.assertEqual(s['pA'],F(len(aa),len(atoms)))
            self.assertEqual(s['pB'],F(len(bb),len(atoms)))
            self.assertEqual(s['joint'],F(both,len(atoms)))
            self.assertEqual(s['a_given_b'],F(both,len(bb)) if bb else None)
            self.assertEqual(s['b_given_a'],F(both,len(aa)) if aa else None)
            self.assertEqual(s['independent'],s['joint']==s['pA']*s['pB'])
    def test_product_total_probability_bayes(self):
        for counts in itertools.product(range(1,4),repeat=4):
            a,b,c,d=counts;s=inspect(*counts);q=s['a_given_b']
            self.assertEqual(q*s['pB'],s['joint'])
            self.assertEqual(s['pA'],q*s['pB']+F(b,b+d)*(1-s['pB']))
            self.assertEqual(q,s['b_given_a']*s['pA']/s['pB'])
            self.assertEqual(q+F(c,a+c),1)
    def test_scaling_and_permutation(self):
        for counts in itertools.product(range(3),repeat=4):
            s=inspect(*counts);scaled=inspect(*(5*v for v in counts));swapped=inspect(counts[0],counts[2],counts[1],counts[3])
            for key in ('pA','pB','joint','a_given_b','b_given_a','independent'):self.assertEqual(s[key],scaled[key])
            self.assertEqual(s['a_given_b'],swapped['b_given_a'])
    def test_singular_independence_and_contract(self):
        self.assertIsNone(inspect(0,2,0,3)['a_given_b'])
        self.assertTrue(inspect(0,0,2,3)['independent'])
        self.assertFalse(inspect(0,2,3,0)['independent'])
        self.assertTrue(inspect(1,1,1,1)['independent'])
        self.assertNotEqual(inspect(2,1,3,4)['a_given_b'],inspect(2,1,3,4)['b_given_a'])
        for bad in (-1,True,.5,float('nan')):
            with self.assertRaises(ValueError):inspect(bad,1,1,1)
