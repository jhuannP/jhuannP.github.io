import unittest
from itertools import product
from fractions import Fraction as Q
from .inheritance import cross,viable,any_independent,observed,binomial

class Tests(unittest.TestCase):
    def test_gamete_enumeration(self):
        for a,b in product(range(3),repeat=2):
            ga=(1,)*a+(0,)*(2-a);gb=(1,)*b+(0,)*(2-b)
            counts=[0,0,0]
            for x,y in product(ga,gb):counts[x+y]+=1
            self.assertEqual(cross(a,b),tuple(Q(v,4)for v in counts))
        self.assertEqual(cross(1,1),(Q(1,4),Q(1,2),Q(1,4)))
        self.assertEqual(viable(cross(1,1),(1,1,0)),(Q(1,3),Q(2,3),0))
    def test_loci_and_observation(self):
        for ps in ((Q(1,2),),(Q(1,2),Q(1,2)),(Q(1,4),Q(2,3),Q(1,2))):
            present=Q(0)
            for bits in product((0,1),repeat=len(ps)):
                weight=Q(1)
                for bit,p in zip(bits,ps):weight*=p if bit else 1-p
                if any(bits):present+=weight
            self.assertEqual(any_independent(ps),present)
        # Dois sítios em ligação completa cis: 00/11, cada um 1/2, não 3/4.
        linked={(0,0):Q(1,2),(1,1):Q(1,2)}
        self.assertEqual(sum(v for bits,v in linked.items()if any(bits)),Q(1,2))
        self.assertEqual(observed(Q(1,2),Q(3,4)),Q(3,8))
        self.assertEqual(observed(Q(1,2),Q(3,4),Q(1,8)),Q(7,16))
    def test_independent_offspring(self):
        for p in (Q(1,2),Q(3,8)):
            counts=[Q(0)for _ in range(9)]
            for bits in product((0,1),repeat=8):
                w=Q(1)
                for bit in bits:w*=p if bit else 1-p
                counts[sum(bits)]+=w
            self.assertEqual(tuple(counts),tuple(binomial(8,k,p)for k in range(9)))
            self.assertEqual(sum(counts),1)
            self.assertEqual(sum(k*v for k,v in enumerate(counts)),8*p)
        self.assertEqual(binomial(8,6,Q(1,2)),Q(7,64))
    def test_contracts(self):
        for bad in (True,1.,-1,3):
            with self.assertRaises(ValueError):cross(bad,0)
        for bad in (True,.5,Q(3,2),-1):
            with self.assertRaises(ValueError):observed(bad,1)
        with self.assertRaises(ValueError):viable(cross(1,1),(0,0,0))
        with self.assertRaises(ValueError):viable((Q(1,4),)*3,(1,1,1))
        with self.assertRaises(ValueError):any_independent(())
        with self.assertRaises(ValueError):binomial(21,1,Q(1,2))
        with self.assertRaises(ValueError):binomial(8,True,Q(1,2))
