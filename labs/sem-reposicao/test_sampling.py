from fractions import Fraction as Q
from itertools import combinations, permutations, product
from collections import Counter
import math
import unittest
from .example import distribution, path_probability

class SamplingTests(unittest.TestCase):
    def test_identifiable_subsets_and_moments(self):
        for N in range(1,9):
            for K in range(N+1):
                for n in range(N+1):
                    subsets=list(combinations(range(N),n))
                    counts=Counter(sum(x<K for x in s) for s in subsets)
                    exact=tuple(Q(counts[k],len(subsets)) for k in range(n+1))
                    self.assertEqual(distribution(N,K,n),exact)
                    self.assertEqual(sum(exact),1)
                    p=Q(K,N);mean=sum(k*q for k,q in enumerate(exact))
                    var=sum((k-mean)**2*q for k,q in enumerate(exact))
                    self.assertEqual(mean,n*p)
                    expected=Q(0) if N==1 else n*p*(1-p)*Q(N-n,N-1)
                    self.assertEqual(var,expected)
    def test_ordered_objects_color_paths_and_total(self):
        for N in range(1,7):
            for K in range(N+1):
                for n in range(N+1):
                    paths=list(permutations(range(N),n))
                    counts=Counter(tuple("V" if x<K else "A" for x in row) for row in paths)
                    masses=[Q(0)]*(n+1)
                    for colors in product("VA",repeat=n):
                        q=path_probability(N,K,colors)
                        self.assertEqual(q,Q(counts[colors],len(paths)))
                        masses[colors.count("V")]+=q
                    self.assertEqual(tuple(masses),distribution(N,K,n))
    def test_two_draw_marginals_and_negative_covariance(self):
        for N in range(2,10):
            for K in range(N+1):
                p=Q(K,N)
                vv=path_probability(N,K,"VV")
                av=path_probability(N,K,"AV")
                self.assertEqual(vv+av,p)
                self.assertEqual(vv-p*p,-p*(1-p)/Q(N-1))
        self.assertEqual(path_probability(5,3,"VV"),Q(3,10))
        self.assertEqual(path_probability(5,3,"VV")/Q(3,5),Q(1,2))
        self.assertEqual(path_probability(5,3,"AV")/Q(2,5),Q(3,4))
    def test_replacement_against_iid_color_sequences(self):
        for N in range(1,7):
            for K in range(N+1):
                for n in range(6):
                    counts=[Q(0)]*(n+1)
                    for row in product((0,1),repeat=n):
                        q=math.prod(Q(K if x else N-K,N) for x in row)
                        counts[sum(row)]+=q
                    self.assertEqual(distribution(N,K,n,True),tuple(counts))
        self.assertEqual(distribution(5,3,2,True),(Q(4,25),Q(12,25),Q(9,25)))
    def test_edges_and_contracts(self):
        self.assertEqual(distribution(1,1,1),(Q(0),Q(1)))
        self.assertEqual(distribution(5,3,0),(Q(1),))
        self.assertEqual(distribution(5,3,5),(Q(0),Q(0),Q(0),Q(1),Q(0),Q(0)))
        self.assertEqual(path_probability(5,0,"V"),0)
        self.assertEqual(path_probability(5,3,""),1)
        for args in [(0,0,0),(3,4,1),(3,-1,1),(3,1,4),(3,1,-1),(True,1,1),(3,1,.5)]:
            with self.assertRaises(ValueError):distribution(*args)
        with self.assertRaises(ValueError):distribution(3,1,1,1)
        for colors in ("X","VVVX","VAAAAA"):
            with self.assertRaises(ValueError):path_probability(5,3,colors)
