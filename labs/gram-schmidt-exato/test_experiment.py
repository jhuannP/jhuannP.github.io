import unittest
from itertools import product
from fractions import Fraction as F
from .experiment import orthogonalize,model,dot

class GramTests(unittest.TestCase):
    def test_all_small_integer_pairs_span_and_rank(self):
        vectors=list(product(range(-2,3),repeat=2))
        for a,b in product(vectors,repeat=2):
            basis,_=orthogonalize([a,b]);det=a[0]*b[1]-a[1]*b[0]
            rank=2 if det else 1 if any(a+b) else 0
            self.assertEqual(len(basis),rank)
            for i,u in enumerate(basis):
                self.assertGreater(dot(u,u),0)
                for v in basis[:i]:self.assertEqual(dot(u,v),0)
            for v in (a,b):
                projected=[sum((dot(v,u)/dot(u,u)*u[j] for u in basis),F(0)) for j in range(2)]
                self.assertEqual(projected,list(v))

    def test_visual_family_and_orthonormality(self):
        for tick in range(-8,9):
            t=F(tick,4);r=model(t)
            self.assertEqual(r['residual'],(t,-t));self.assertEqual(r['norm_squared'],dot(r['residual'],r['residual']))
            self.assertEqual(r['rank'],1 if t==0 else 2)
            if t:
                self.assertAlmostEqual(dot(r['q1'],r['q2']),0)
                self.assertAlmostEqual(dot(r['q2'],r['q2']),1)
            else:self.assertIsNone(r['q2'])

    def test_order_and_zero_vectors(self):
        basis,skipped=orthogonalize([(0,0),(1,1),(2,2),(1,-1)])
        self.assertEqual(skipped,[0,2]);self.assertEqual(len(basis),2)
        left,_=orthogonalize([(1,1),(2,0)]);right,_=orthogonalize([(2,0),(1,1)])
        self.assertNotEqual(left,right)
        for basis in (left,right):self.assertEqual(dot(basis[0],basis[1]),0)
        bs,_=orthogonalize([(F(1,2),F(1,3),0),(0,0,1)])
        self.assertEqual(dot(bs[0],bs[1]),0)

    def test_contract(self):
        for vs in ([],[()],[(1,2),(1,)],[(True,0)],[(.5,1)],'bad'):
            with self.assertRaises(ValueError):orthogonalize(vs)
        for t in (True,None,.5,F(1,3),-3,3):
            with self.assertRaises(ValueError):model(t)
