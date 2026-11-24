from fractions import Fraction as Q
import unittest
from .finite import probability,dice_weights,sum_distribution

class SchoolProbabilityTests(unittest.TestCase):
    def test_sum_counts_and_moments(self):
        for n in range(1,13):
            p=sum_distribution(n)
            self.assertEqual(set(p),set(range(2,2*n+1)))
            self.assertEqual(sum(p.values()),1)
            mean=sum(s*ps for s,ps in p.items())
            self.assertEqual(mean,n+1)
            self.assertEqual(sum((s-mean)**2*ps for s,ps in p.items()),Q(n*n-1,6))
            for s,ps in p.items():
                expected=s-1 if s<=n+1 else 2*n+1-s
                self.assertEqual(ps,Q(expected,n*n))
                self.assertEqual(ps,p[2*(n+1)-s])

    def test_union_and_independence_are_different_operations(self):
        w=dice_weights();A={p for p in w if p[0]==6};B={p for p in w if p[1]==6}
        self.assertEqual(probability(w,A|B),Q(11,36))
        self.assertEqual(probability(w,A|B),probability(w,A)+probability(w,B)-probability(w,A&B))
        self.assertEqual(probability(w,A&B),probability(w,A)*probability(w,B))
        evens={p for p in w if all(v%2==0 for v in p)}
        self.assertEqual(probability(w,evens),Q(1,4))

    def test_complement_and_zero_weight_outcome(self):
        w={'a':3,'b':1,'c':0}
        self.assertEqual(probability(w,{'b'}),Q(1,4))
        self.assertEqual(probability(w,{'c'}),0)
        self.assertEqual(probability(w,{'a'})+probability(w,{'b','c'}),1)
        self.assertEqual(probability(w,set()),0)

    def test_grouping_keeps_weights_not_uniformity(self):
        w=dice_weights();p=sum_distribution()
        self.assertEqual(p[7],Q(1,6));self.assertEqual(p[2],Q(1,36))
        for total in range(2,13):
            self.assertEqual(p[total],probability(w,{x for x in w if sum(x)==total}))
        self.assertNotEqual(p[7],Q(1,11))

    def test_contracts(self):
        for n in (0,-1,True,6.,'6',None):
            with self.assertRaises(ValueError):dice_weights(n)
        for w in ({},{'a':0},{'a':-1},{'a':True},{'a':.5},None):
            with self.assertRaises(ValueError):probability(w,{'a'})
        with self.assertRaises(ValueError):probability({'a':1},{'unknown'})

if __name__=='__main__':unittest.main()
