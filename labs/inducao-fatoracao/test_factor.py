import unittest
from math import prod
from .factor import factor

def prime_by_all_smaller(k):
    return k>=2 and all(k%d for d in range(2,k))

class FactorTests(unittest.TestCase):
    def test_known_examples(self):
        self.assertEqual(factor(72)[0],(2,2,2,3,3))
        self.assertEqual(factor(97)[0],(97,))
        self.assertEqual(factor(1000000)[0],(2,)*6+(5,)*6)

    def test_invariants_and_independent_primality(self):
        for n in range(2,1001):
            factors, trace = factor(n)
            self.assertEqual(prod(factors),n)
            self.assertEqual(tuple(sorted(factors)),factors)
            self.assertTrue(all(prime_by_all_smaller(q) for q in factors))
            last=n
            for emitted, remaining in trace:
                self.assertEqual(prod(emitted)*remaining,n)
                self.assertLess(remaining,last)
                last=remaining
            self.assertEqual(last,1)

    def test_prime_square_boundary(self):
        # <=, não <, para detectar divisores na raiz exata.
        for q in (2,3,5,7,11,31):
            self.assertEqual(factor(q*q)[0],(q,q))

    def test_contracts(self):
        for n in (True,False,0,1,-5,2.0,'72',1000001):
            with self.assertRaises(ValueError):factor(n)

if __name__=='__main__':unittest.main()
