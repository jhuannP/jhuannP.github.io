import unittest
from fractions import Fraction as Q
from itertools import product
from .odds import odds_update

class BayesOddsTests(unittest.TestCase):
    def test_against_enumerated_atoms(self):
        # p=i/10, s=j/10, f=k/10; 1000 objetos equiprováveis.
        for i,j,k in product(range(1,10), repeat=3):
            atoms = [(a,b,c) for a in range(10) for b in range(10) for c in range(10)]
            positive = [x for x in atoms if (x[0]<i and x[1]<j) or (x[0]>=i and x[2]<k)]
            expected = Q(sum(x[0]<i for x in positive),len(positive))
            r=odds_update(Q(i,10),Q(j,10),Q(k,10))
            self.assertEqual(r['posterior'],expected)
            self.assertEqual(r['posterior_odds'],expected/(1-expected))

    def test_half_threshold_and_direction(self):
        for s,f in product((Q(1,5),Q(1,2),Q(4,5)),repeat=2):
            threshold=f/(s+f)
            self.assertEqual(odds_update(threshold,s,f)['posterior'],Q(1,2))
            self.assertLess(odds_update(threshold/2,s,f)['posterior'],Q(1,2))
            self.assertGreater(odds_update((1+threshold)/2,s,f)['posterior'],Q(1,2))

    def test_information_and_probability_are_distinct(self):
        for p in (Q(1,100),Q(1,10),Q(1,2),Q(9,10)):
            self.assertEqual(odds_update(p,Q(1,2),Q(1,2))['posterior'],p)
            self.assertGreater(odds_update(p,Q(4,5),Q(1,5))['posterior'],p)
            self.assertLess(odds_update(p,Q(1,5),Q(4,5))['posterior'],p)
        self.assertLess(odds_update(Q(1,10),Q(4,5),Q(1,5))['posterior'],Q(1,2))

    def test_contract(self):
        for value in (0,1,-1,Q(3,2),True,.5,None,'1/2'):
            for index in range(3):
                args=[Q(1,2)]*3;args[index]=value
                with self.assertRaises(ValueError): odds_update(*args)
