import unittest
from fractions import Fraction as Q
from .root import term,root_value,partial,tail,bound,first_bound

class Tests(unittest.TestCase):
    def test_original_fixture_and_exact_sum(self):
        self.assertEqual(term(1),Q(1,3));self.assertEqual(term(2),Q(1,4))
        self.assertEqual(partial(2),Q(7,12));self.assertEqual(tail(0),Q(17,24))
        self.assertEqual(first_bound(Q(1,100)),7)
        self.assertGreater(bound(6),Q(1,100));self.assertLess(tail(6),Q(1,100))
        self.assertEqual(tail(6),Q(1,192)+Q(1,1944))
    def test_geometric_tail_vs_independent_subtraction(self):
        total=Q(17,24)
        for n in range(129):
            self.assertEqual(tail(n),total-partial(n))
            self.assertLessEqual(tail(n),bound(n));self.assertGreater(tail(n),0)
            if n<128:
                self.assertEqual(tail(n)-tail(n+1),term(n+1))
                self.assertLess(tail(n+1),tail(n))
    def test_root_identity_parity_and_bound_search(self):
        for n in range(1,129):
            self.assertEqual(root_value(n)**n,term(n))
            self.assertLessEqual(root_value(n),Q(1,2))
        # Valores adjacentes da razão: um ramo cresce, o outro decai.
        for n in (1,3,5,7):
            self.assertEqual(term(n+1)/term(n),Q(3,2)**n/2)
        for n in (2,4,6,8):
            self.assertEqual(term(n+1)/term(n),Q(2,3)**n/3)
        for k in range(1,81):
            n=first_bound(Q(1,3*k))
            self.assertLessEqual(bound(n),Q(1,3*k))
            self.assertGreater(bound(n-1),Q(1,3*k))
    def test_contracts(self):
        for bad in (0,-1,129,True,2.,Q(2)):
            with self.assertRaises(ValueError):term(bad)
        for bad in (-1,129,True,2.):
            with self.assertRaises(ValueError):tail(bad)
        for bad in (0,1,-1,True,.01,Q(1,2**129)):
            with self.assertRaises(ValueError):first_bound(bad)
