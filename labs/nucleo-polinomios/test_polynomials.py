import unittest
from fractions import Fraction as Q
from itertools import product
from .polynomials import derivative,primitive,evaluate,reconstruct

class PolynomialTests(unittest.TestCase):
    def test_basis_and_rank(self):
        images=[derivative(tuple(int(i==j) for i in range(4))) for j in range(4)]
        self.assertEqual(images,[(0,0,0),(1,0,0),(0,2,0),(0,0,3)])
        self.assertEqual(derivative((7,)),(0,))
    def test_625_exact_identities(self):
        for p in product(range(-2,3),repeat=4):
            dp=derivative(p)
            self.assertEqual(primitive(dp),(0,)+p[1:])
            self.assertEqual(derivative(primitive(dp)),dp)
            self.assertEqual(derivative((p[0]+11,)+p[1:]),dp)
            for t0 in (Q(-2),Q(1,3),Q(2)):
                self.assertEqual(reconstruct(dp,t0,evaluate(p,t0)),p)
    def test_original_example_and_affine(self):
        q=(2,-2,3)
        self.assertEqual(reconstruct(q,1,5),(3,2,-1,1))
        self.assertEqual(evaluate((3,2,-1,1),2),11)
        self.assertEqual(evaluate((0,2,-1,1),1),2)
        self.assertEqual(reconstruct((0,0,0),1,5),(5,0,0,0))
        # Fixed nonzero initial value: reconstruction does not send zero to zero.
        self.assertNotEqual(reconstruct((0,0,0),1,5),(0,0,0,0))
    def test_contracts(self):
        for p in ([],[True],[1.5],['2'],[0]*10):
            with self.assertRaises(ValueError):derivative(p)
        with self.assertRaises(ValueError):primitive([0]*9)
        with self.assertRaises(ValueError):evaluate([1],True)
        with self.assertRaises(ValueError):reconstruct([1],0,1.5)
