import unittest
from itertools import combinations, product
from math import comb
from fractions import Fraction as Q
from .urn import infer
from .counts import infer_count


class CountTests(unittest.TestCase):
    def test_same_posterior_different_evidence(self):
        # Six balls: unknown red count 2 or 4, equal prior. Observe two red/one blue.
        count = infer_count(6, {2:1,4:1}, 3, 2)
        self.assertEqual(count, dict(evidence=Q(2,5), posterior={2:Q(1,4),4:Q(3,4)}, next_red=Q(1,2)))
        for seq in [(1,1,0),(1,0,1),(0,1,1)]:
            ordered = infer(6, {2:1,4:1}, seq)
            self.assertEqual(ordered['evidence'], Q(2,15))
            self.assertEqual(ordered['posterior'], count['posterior'])
            self.assertEqual(ordered['next_red'], count['next_red'])

    def test_combinations_oracle_all_counts(self):
        for n in range(1,8):
            prior = {r: Q(r+1) for r in range(n+1)}
            mass = sum(prior.values())
            for m in range(n+1):
                samples = list(combinations(range(n),m))
                total_evidence = Q(0)
                for k in range(m+1):
                    joint = {r: w/mass*Q(sum(sum(i<r for i in s)==k for s in samples),len(samples)) for r,w in prior.items()}
                    evidence = sum(joint.values())
                    expected = {r:j/evidence for r,j in joint.items()}
                    actual = infer_count(n,prior,m,k)
                    self.assertEqual(actual['evidence'], evidence)
                    self.assertEqual(actual['posterior'], expected)
                    if m<n:
                        # Expected red fraction from literal remaining-object inventories.
                        next_mass = Q(0)
                        for r,w in prior.items():
                            for s in samples:
                                if sum(i<r for i in s)==k:
                                    next_mass += w/mass * Q(sum(i<r for i in range(n) if i not in s),len(samples)*(n-m))
                        self.assertEqual(actual['next_red'], next_mass/evidence)
                    else:self.assertIsNone(actual['next_red'])
                    total_evidence += evidence
                self.assertEqual(total_evidence, 1)

    def test_order_factor_for_every_binary_sequence(self):
        for n in range(1,7):
            prior = {r: r+1 for r in range(n+1)}
            for m in range(n+1):
                for seq in product((0,1),repeat=m):
                    a = infer(n,prior,seq)
                    b = infer_count(n,prior,m,sum(seq))
                    self.assertEqual(a['evidence']*comb(m,sum(seq)),b['evidence'])
                    self.assertEqual(a['posterior'],b['posterior'])
                    self.assertEqual(a['next_red'],b['next_red'])

    def test_boundaries_and_contracts(self):
        self.assertEqual(infer_count(3,{1:1,2:1},0,0)['posterior'],{1:Q(1,2),2:Q(1,2)})
        self.assertEqual(infer_count(3,{0:1},2,1),dict(evidence=Q(0),posterior=None,next_red=None))
        self.assertEqual(infer_count(3,{1:1},3,1)['posterior'],{1:Q(1)})
        for m,k in [(True,1),(2,True),(-1,0),(4,0),(2,-1),(2,3),(1.0,0),(1,0.0)]:
            with self.subTest(m=m,k=k), self.assertRaises(ValueError):infer_count(3,{1:1},m,k)

if __name__ == '__main__':unittest.main()
