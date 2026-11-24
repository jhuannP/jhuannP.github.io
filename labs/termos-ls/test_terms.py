import unittest
from math import comb
from collections import Counter
from .terms import histogram,terms,j_values2

class TermTests(unittest.TestCase):
    def test_canonical_configs(self):
        self.assertEqual(terms(2,2),((3,2),(1,2),(4,0),(2,0),(0,0)))
        self.assertEqual(set(terms(1,2)),{(1,2),(2,0),(0,0)})
        self.assertEqual(set(terms(1,3)),{(0,3),(2,1),(1,1)})
        self.assertEqual(terms(2,1),((2,1),))
        # Dois spins paralelos: 10 pares de orbitais distintos, perfil independente.
        row=histogram(2,2)
        self.assertEqual(tuple(row[m,2] for m in range(-4,5)),(0,1,1,2,2,2,1,1,0))
        self.assertEqual(tuple(row[m,0] for m in range(-4,5)),(1,2,3,4,5,4,3,2,1))

    def test_all_subshells_and_holes(self):
        for l in range(3):
            capacity=2*(2*l+1)
            for n in range(capacity+1):
                h=histogram(l,n);ts=terms(l,n)
                self.assertEqual(sum(h.values()),comb(capacity,n))
                self.assertEqual(sum((2*L+1)*(S2+1) for L,S2 in ts),comb(capacity,n))
                self.assertEqual(Counter(ts),Counter(terms(l,capacity-n)))
                for (m,s),count in h.items():
                    self.assertEqual(count,h[-m,s]);self.assertEqual(count,h[m,-s])
                reconstructed=Counter()
                for L,S2 in ts:
                    for m in range(-L,L+1):
                        for s in range(-S2,S2+1,2):reconstructed[m,s]+=1
                self.assertEqual(h,reconstructed)

    def test_j_dimensions(self):
        self.assertEqual(j_values2(3,2),(4,6,8))
        self.assertEqual(j_values2(2,1),(3,5))
        for L in range(7):
            for S2 in range(5):
                self.assertEqual(sum(j2+1 for j2 in j_values2(L,S2)),(2*L+1)*(S2+1))

    def test_contracts(self):
        for l,n in ((True,2),(3,2),(-1,2),(2,True),(2,11),(2,-1),(1,1.5)):
            with self.assertRaises(ValueError):terms(l,n)
        for L,S2 in ((True,2),(-1,2),(2,1.5)):
            with self.assertRaises(ValueError):j_values2(L,S2)
