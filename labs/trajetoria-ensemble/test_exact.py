import unittest
from itertools import product
from fractions import Fraction as Q
from .exact import averages,variance_of_mean

class EnsembleTests(unittest.TestCase):
    def test_axes_and_preserved_example(self):
        self.assertEqual(averages([[0,2,0],[0,0,0]]),((0,1,0),(Q(2,3),0)))
        self.assertEqual(averages([[-1]*4,[1]*4]),((0,0,0,0),(-1,1)))
        a,b=averages([[1,2,4],[3,6,8]])
        self.assertEqual(sum(a)/3,sum(b)/2)
        self.assertEqual(a,(2,4,6))

    def test_constant_sign_does_not_average_away(self):
        for N in range(1,41):
            ensemble,temporal=averages([[-1]*N,[1]*N])
            self.assertEqual(ensemble,(0,)*N)
            self.assertEqual(temporal,(-1,1))
            self.assertEqual(sum(x*x for x in temporal)/2,1)
            self.assertEqual(variance_of_mean([[1]*N for _ in range(N)]),1)

    def test_independent_realizations_by_exhaustive_enumeration(self):
        for M in range(1,10):
            means=[sum((Q(x) for x in signs),Q(0))/M for signs in product((-1,1),repeat=M)]
            self.assertEqual(sum(means)/len(means),0)
            self.assertEqual(sum(x*x for x in means)/len(means),Q(1,M))
            self.assertEqual(variance_of_mean([[int(i==j) for j in range(M)] for i in range(M)]),Q(1,M))

    def test_alternating_sign_correlations(self):
        for N in range(1,31):
            rows=[[z*(-1)**n for n in range(N)] for z in (-1,1)]
            ensemble,temporal=averages(rows)
            self.assertEqual(ensemble,(0,)*N)
            variance=sum((x*x for x in temporal),Q(0))/2
            expected=Q(0) if N%2==0 else Q(1,N*N)
            self.assertEqual(variance,expected)
            C=[[(-1)**(i-j) if i>=j else (-1)**(j-i) for j in range(N)] for i in range(N)]
            self.assertEqual(variance_of_mean(C),expected)

    def test_contracts(self):
        for paths in ([],[[]],[[1],[1,2]],[[True]],[[.5]]):
            with self.assertRaises(ValueError):averages(paths)
        for C in ([],[[1,0]],[[1,1],[0,1]],[[True]],[[.5]]):
            with self.assertRaises(ValueError):variance_of_mean(C)
