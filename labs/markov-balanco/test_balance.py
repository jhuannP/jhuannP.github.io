from fractions import Fraction as Q
from itertools import product,permutations
from collections import Counter
import unittest
from .balance import diagnose,step,evolve

P=((Q(1,2),Q(1,2),0),(0,Q(1,2),Q(1,2)),(Q(1,2),0,Q(1,2)))
PI=(Q(1,3),)*3

class BalanceTests(unittest.TestCase):
    def test_examples_and_same_invariant_different_flows(self):
        d=diagnose(P,PI)
        self.assertTrue(d['stationary']);self.assertFalse(d['detailed_balance'])
        self.assertEqual(d['flux'][0][1],Q(1,6));self.assertEqual(d['flux'][1][0],0)
        self.assertEqual(d['current'][0][1],Q(1,6))
        R=tuple(tuple((P[i][j]+P[j][i])/2 for j in range(3)) for i in range(3))
        reverse=diagnose(R,PI)
        self.assertTrue(reverse['stationary']);self.assertTrue(reverse['detailed_balance'])
        self.assertEqual(reverse['flux'][0][1],Q(1,12))
        old=diagnose(((Q(4,5),Q(1,5)),(Q(1,10),Q(9,10))),(Q(1,3),Q(2,3)))
        self.assertTrue(old['stationary'] and old['detailed_balance'])

    def test_distribution_by_primitive_paths(self):
        for n in range(9):
            counts=Counter(sum(bits)%3 for bits in product((0,1),repeat=n))
            self.assertEqual(evolve((1,0,0),P,n)[-1],tuple(Q(counts[i],2**n) for i in range(3)))

    def test_exact_contraction_for_this_matrix(self):
        for start in ((1,0,0),(Q(1,2),Q(1,4),Q(1,4)),PI):
            initial=sum((v-Q(1,3))**2 for v in start)
            for n,p in enumerate(evolve(start,P,25)):
                self.assertEqual(sum((v-Q(1,3))**2 for v in p),initial/Q(4)**n)

    def test_conservation_and_relabeling_in_circulant_family(self):
        for a in range(5):
            for b in range(5-a):
                c=4-a-b
                base=((Q(a,4),Q(b,4),Q(c,4)),(Q(c,4),Q(a,4),Q(b,4)),(Q(b,4),Q(c,4),Q(a,4)))
                for perm in permutations(range(3)):
                    M=tuple(tuple(base[i][j] for j in perm) for i in perm)
                    d=diagnose(M,PI)
                    self.assertTrue(d['stationary']);self.assertEqual(d['detailed_balance'],b==c)
                    for start in ((1,0,0),PI,(Q(1,2),Q(1,4),Q(1,4))):
                        r=diagnose(M,start)
                        for i in range(3):
                            self.assertEqual(sum(r['current'][i]),start[i]-r['next'][i])
                            for j in range(3):self.assertEqual(r['current'][i][j],-r['current'][j][i])

    def test_periodicity_reducibility_and_contracts(self):
        flip=((0,1),(1,0))
        self.assertEqual(evolve((1,0),flip,2),((1,0),(0,1),(1,0)))
        self.assertTrue(diagnose(flip,(Q(1,2),Q(1,2)))['detailed_balance'])
        for start in ((1,0),(0,1),(Q(1,2),Q(1,2))):self.assertEqual(step(start,((1,0),(0,1))),start)
        for bad in ([],[[1,0]],[[1,1],[0,1]],[[1.0]]):
            with self.assertRaises((TypeError,ValueError)):diagnose(bad,(1,))
        with self.assertRaises(ValueError):diagnose(P,(1,1,1))
        with self.assertRaises(ValueError):evolve(PI,P,True)
        with self.assertRaises(ValueError):evolve(PI,P,1001)

if __name__=='__main__':unittest.main()
