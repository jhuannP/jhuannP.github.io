import unittest
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from math import comb
from .reservoir import finite_patterns,canonical_patterns,compare_two,total_variation

class ReservoirTests(unittest.TestCase):
    def test_original_and_two_probes_reference(self):
        one=finite_patterns(11,3,1)
        self.assertEqual(one[(1,)],Q(3,11))
        self.assertEqual({s:v*165 for s,v in one.items()},{(0,):120,(1,):45})
        r=compare_two(11,3)
        self.assertEqual([r['finite'][s]*165 for s in ((0,0),(0,1),(1,0),(1,1))],[84,36,36,9])
        self.assertEqual(r['covariance'],Q(-12,605))
        self.assertEqual(r['total_variation'],Q(24,605))
        self.assertEqual(r['mean_count'],Q(6,11))
        self.assertNotEqual(r['finite'][(1,1)],r['p']**2)
    def test_distribution_against_independent_enumeration(self):
        for total in range(2,10):
            states=list(product((0,1),repeat=total))
            for q in range(total+1):
                accessible=[s for s in states if sum(s)==q]
                for m in range(1,min(3,total)+1):
                    counts=Counter(s[:m] for s in accessible)
                    expected={s:Q(counts[s],len(accessible)) for s in product((0,1),repeat=m)}
                    self.assertEqual(finite_patterns(total,q,m),expected)
    def test_pattern_probabilities_by_sequential_draws(self):
        # Independent construction as sampling without replacement, not combinations.
        for total in range(2,13):
            for q in range(total+1):
                for m in range(1,min(4,total)+1):
                    exact=finite_patterns(total,q,m)
                    for state,prob in exact.items():
                        remaining=q;chance=Q(1)
                        for i,bit in enumerate(state):
                            numerator=remaining if bit else total-i-remaining
                            if numerator<=0: chance=Q(0);break
                            chance*=Q(numerator,total-i)
                            remaining-=bit
                        self.assertEqual(prob,chance)
    def test_matching_marginals_finite_covariance_and_limit(self):
        distances=[]
        for total,q in ((11,3),(22,6),(44,12),(88,24)):
            r=compare_two(total,q);p=r['p']
            for i in (0,1):
                self.assertEqual(sum(v for state,v in r['finite'].items() if state[i]),p)
                self.assertEqual(sum(v for state,v in r['canonical'].items() if state[i]),p)
            self.assertEqual(r['covariance'],-p*(1-p)/(total-1))
            self.assertEqual(r['total_variation'],2*p*(1-p)/(total-1))
            self.assertEqual(r['variance_count'],2*p*(1-p)*(total-2)/(total-1))
            distances.append(r['total_variation'])
        self.assertTrue(all(a>b for a,b in zip(distances,distances[1:])))
        for total,q in ((8,0),(8,8)):
            self.assertEqual(compare_two(total,q)['total_variation'],0)
    def test_contracts_and_normalization(self):
        for args in ((0,0,1),(10,-1,2),(10,11,2),(10,2,9),(2,1,3),(True,1,1)):
            with self.assertRaises(ValueError): finite_patterns(*args)
        for p in (Q(-1),Q(2),True,0.5):
            with self.assertRaises(ValueError): canonical_patterns(p,2)
        for q in range(6):
            f=finite_patterns(5,q,3);self.assertEqual(sum(f.values()),1)
        with self.assertRaises(ValueError): total_variation({0:Q(1,2)},{0:Q(1)})
