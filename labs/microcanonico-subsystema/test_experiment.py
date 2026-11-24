from itertools import product, combinations
from collections import Counter
from fractions import Fraction as Q
from math import log
import unittest
from .experiment import subsystem,pattern_probability

class MicrocanonicalSubsystemTests(unittest.TestCase):
    def test_example_and_fluctuations(self):
        r=subsystem(8,3,3)
        self.assertEqual(r,dict(omega=56,counts=(10,30,15,1),
            probabilities=(Q(5,28),Q(15,28),Q(15,56),Q(1,56))))
        p=r["probabilities"]
        mean=sum(k*pk for k,pk in enumerate(p))
        variance=sum((k-mean)**2*pk for k,pk in enumerate(p))
        self.assertEqual(mean,Q(9,8));self.assertEqual(variance,Q(225,448))
        self.assertEqual(pattern_probability(8,3,[0,0,0]),Q(5,28))
        self.assertEqual(pattern_probability(8,3,[1,0,0]),Q(5,28))
        self.assertEqual(pattern_probability(8,3,[1,1,1]),Q(1,56))
    def test_binary_enumeration_and_prefix_patterns(self):
        for N in range(1,10):
            states=list(product((0,1),repeat=N))
            for q in range(N+1):
                allowed=[s for s in states if sum(s)==q]
                for a in range(N+1):
                    r=subsystem(N,q,a)
                    counts=Counter(sum(s[:a]) for s in allowed)
                    self.assertEqual(r["omega"],len(allowed))
                    self.assertEqual(r["counts"],tuple(counts[k] for k in range(a+1)))
                    self.assertEqual(sum(r["probabilities"]),1)
                    patterns=Counter(s[:a] for s in allowed)
                    for bits in product((0,1),repeat=a):
                        self.assertEqual(pattern_probability(N,q,bits),Q(patterns[bits],len(allowed)))
    def test_arbitrary_site_subsets_and_energy_anticorrelation(self):
        N,q=6,2
        allowed=[s for s in product((0,1),repeat=N) if sum(s)==q]
        for a in range(N+1):
            r=subsystem(N,q,a)
            for selected in combinations(range(N),a):
                xs=[sum(s[i] for i in selected) for s in allowed]
                counts=Counter(xs)
                self.assertEqual(tuple(Q(counts[k],len(xs)) for k in range(a+1)),r["probabilities"])
                mean=Q(sum(xs),len(xs));ys=[q-x for x in xs]
                mean_y=Q(sum(ys),len(ys))
                variance=sum((x-mean)**2 for x in xs)/len(xs)
                covariance=sum((x-mean)*(y-mean_y) for x,y in zip(xs,ys))/len(xs)
                self.assertEqual(covariance,-variance)
    def test_symmetry_and_degenerate_limits(self):
        for N in range(1,10):
            for q in range(N+1):
                for a in range(N+1):
                    p=subsystem(N,q,a)["probabilities"]
                    self.assertEqual(tuple(reversed(p)),subsystem(N,N-q,a)["probabilities"])
                    self.assertEqual(sum(k*pk for k,pk in enumerate(p)),Q(a*q,N))
            self.assertEqual(log(subsystem(N,0,0)["omega"]),0)
            self.assertEqual(subsystem(N,N,0)["probabilities"],(Q(1),))
            p=subsystem(N,N//2,N)["probabilities"]
            self.assertEqual(p[N//2],1)
    def test_contracts_and_forbidden_patterns(self):
        for args in [(0,0,0),(3,4,1),(3,-1,1),(3,1,4),(3,1,-1),(True,0,0),(3,1,.5)]:
            with self.assertRaises(ValueError):subsystem(*args)
        for bits in ([True],[2],["1"]):
            with self.assertRaises(ValueError):pattern_probability(3,1,bits)
        self.assertEqual(pattern_probability(3,1,[1,1]),0)
        self.assertEqual(pattern_probability(3,1,[]),1)
