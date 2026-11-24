from fractions import Fraction as Q
from itertools import product
import unittest
from .spin import distribution, moments, response

class SpinTests(unittest.TestCase):
    def test_reference(self):
        self.assertEqual(distribution(4,1), tuple(zip((-4,-2,0,2,4),map(Q,[Q(1,16),Q(1,4),Q(3,8),Q(1,4),Q(1,16)]))))
        self.assertEqual(moments(4,1),(0,4))
        self.assertEqual(moments(4,3),(2,3))
        self.assertEqual(response(4,3,2),Q(3,2))
    def test_ordered_microstates(self):
        # Enumeração independente, sem comb: peso-produto por sequência.
        for n in range(1,7):
            for r in (Q(1,3),Q(1),Q(3)):
                p = r/(1+r)
                law={m:Q(0) for m,_ in distribution(n,r)}
                for spins in product((-1,1),repeat=n):
                    weight=Q(1)
                    for spin in spins:
                        weight *= p if spin==1 else 1-p
                    law[sum(spins)]+=weight
                self.assertEqual(dict(distribution(n,r)),law)
                self.assertEqual(sum(law.values()),1)
                self.assertEqual(moments(n,r),(n*(2*p-1),4*n*p*(1-p)))
    def test_reflection_and_response(self):
        for n in range(1,9):
            for r in (Q(1,5),Q(1),Q(3)):
                self.assertEqual(dict(distribution(n,1/r)),{-m:p for m,p in distribution(n,r)})
                # Derivada analítica da média via dr/dh=2r/T.
                expected = Q(2*n)/(1+r)**2 * 2*r/2
                self.assertEqual(response(n,r,2),expected)
    def test_units_and_old_material(self):
        self.assertEqual(response(4,1,2),2)
        self.assertEqual(response(4,1,2,3),18)
        self.assertEqual(response(4,3,4),response(4,3,2)/2)
        from math import tanh
        self.assertEqual(4/2,2)
        self.assertLess(abs(tanh(-.7)+tanh(.7)),1e-12)
    def test_contracts(self):
        for n in (0,101):
            with self.assertRaises(ValueError): distribution(n,1)
        for n in (True,1.0):
            with self.assertRaises(TypeError): distribution(n,1)
        for r in (0,-1):
            with self.assertRaises(ValueError): distribution(4,r)
        for r in (True,1.0,'3'):
            with self.assertRaises(TypeError): distribution(4,r)
        for t in (0,-2):
            with self.assertRaises(ValueError): response(4,1,t)
if __name__=='__main__': unittest.main()
