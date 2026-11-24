import unittest
from fractions import Fraction as Q
from itertools import product,combinations
from math import prod
from .binomial import pmf,independent_sum,moments

class BinomialTests(unittest.TestCase):
    def test_fixture_and_boundaries(self):
        w=pmf(4,Q(1,4));self.assertEqual(w,tuple(Q(k,256) for k in (81,108,54,12,1)))
        self.assertEqual(moments(w),(1,Q(3,4)))
        self.assertEqual(1-w[0],Q(175,256));self.assertEqual(sum(w[2:]),Q(67,256))
        self.assertEqual(pmf(0,Q(1,2)),(1,));self.assertEqual(pmf(3,0),(1,0,0,0));self.assertEqual(pmf(3,1),(0,0,0,1))

    def test_enumeration_oracle_and_moments(self):
        for n in range(9):
            for p in (Q(1,4),Q(1,2),Q(3,4)):
                counts=[Q(0)]*(n+1)
                for bits in product((0,1),repeat=n):
                    weight=prod((p if b else 1-p for b in bits),start=Q(1))
                    counts[sum(bits)]+=weight
                self.assertEqual(pmf(n,p),tuple(counts))
                self.assertEqual(independent_sum([p]*n),tuple(counts))
                self.assertEqual(moments(counts),(n*p,n*p*(1-p)))
        for ps in product((Q(1,4),Q(3,4)),repeat=5):
            oracle=[Q(0)]*6
            for bits in product((0,1),repeat=5):
                oracle[sum(bits)]+=prod((p if b else 1-p for b,p in zip(bits,ps)),start=Q(1))
            self.assertEqual(independent_sum(ps),tuple(oracle))

    def test_changed_hypotheses(self):
        hetero=independent_sum([Q(1,4),Q(3,4)])
        self.assertEqual(hetero,(Q(3,16),Q(10,16),Q(3,16)))
        self.assertEqual(moments(hetero),(1,Q(3,8)))
        correlated=(Q(1,2),Q(0),Q(1,2));self.assertEqual(moments(correlated),(1,1))
        # Duas bolas de quatro,duas marcadas,sem reposição:6 subconjuntos equiprováveis.
        counts=[0,0,0]
        for pair in combinations(range(4),2):counts[sum(i<2 for i in pair)]+=1
        hyper=tuple(Q(x,6) for x in counts)
        self.assertEqual(hyper,(Q(1,6),Q(4,6),Q(1,6)))
        self.assertEqual(moments(hyper),(1,Q(1,3)))
        self.assertNotEqual(hyper,pmf(2,Q(1,2)))

    def test_contracts(self):
        for n,p in ((True,0),(2.0,Q(1,2)),(101,0),(2,0.5),(2,-1),(2,True)):
            with self.assertRaises(ValueError):pmf(n,p)
        with self.assertRaises(ValueError):moments([Q(1,2)])
        with self.assertRaises(ValueError):independent_sum([Q(1,2)]*101)
        self.assertEqual(independent_sum([]),(1,))
