import unittest
from fractions import Fraction as Q
from itertools import permutations, product
from .urn import infer


class BayesUrnTests(unittest.TestCase):
    def test_examples_and_protocol(self):
        prior = {1: 1, 2: 1}
        self.assertEqual(infer(3, prior)['next_red'], Q(1,2))
        one = infer(3, prior, (1,))
        self.assertEqual(one['posterior'], {1: Q(1,3), 2: Q(2,3)})
        self.assertEqual(one['next_red'], Q(1,3))
        two = infer(3, prior, (1,1))
        self.assertEqual(two['evidence'], Q(1,6))
        self.assertEqual(two['posterior'][2], 1)
        self.assertEqual(two['next_red'], 0)
        mixed = infer(3, prior, (1,0))
        self.assertEqual(mixed['posterior'][2], Q(1,2))
        self.assertEqual(mixed['next_red'], Q(1,2))
        replaced = infer(3, prior, (1,1), replacement=True)
        self.assertEqual(replaced['evidence'], Q(5,18))
        self.assertEqual(replaced['posterior'][2], Q(4,5))
        self.assertEqual(replaced['next_red'], Q(3,5))
        self.assertEqual(prior, {1:1, 2:1})

    def test_object_enumeration_independent_oracle(self):
        # Enumerate identifiable balls, rather than reusing sequential likelihoods.
        for n in range(1, 6):
            for replacement in (False, True):
                for k in range(min(3, n)+1):
                    seqs = list(product(range(n), repeat=k) if replacement else permutations(range(n), k))
                    for obs in product((0,1), repeat=k):
                        prior = {r: Q(r+1) for r in range(n+1)}
                        mass = sum(prior.values())
                        joints = {}
                        red_joint = Q(0)
                        for r, w in prior.items():
                            compatible = [s for s in seqs if tuple(int(i < r) for i in s) == obs]
                            joints[r] = w/mass * Q(len(compatible), len(seqs))
                            if replacement or k<n:
                                # Count next-ball possibilities among each compatible prefix.
                                hits = sum(sum(i<r for i in range(n) if replacement or i not in s) for s in compatible)
                                red_joint += w/mass * Q(hits, len(seqs)*(n if replacement else n-k))
                        evidence = sum(joints.values())
                        actual = infer(n, prior, obs, replacement=replacement)
                        self.assertEqual(actual['evidence'], evidence)
                        self.assertEqual(actual['posterior'], {r:j/evidence for r,j in joints.items()} if evidence else None)
                        self.assertEqual(actual['next_red'], red_joint/evidence if evidence and (replacement or k<n) else None)

    def test_sequence_order_and_weight_scale(self):
        for replacement in (False, True):
            a = infer(5, {0:0, 1:2, 3:5, 5:1}, (1,0,1), replacement=replacement)
            b = infer(5, {0:0, 1:6, 3:15, 5:3}, (0,1,1), replacement=replacement)
            self.assertEqual(a, b)

    def test_impossible_and_empty_inventory_are_distinct(self):
        self.assertEqual(infer(2, {0:1}, (1,)), dict(evidence=Q(0), posterior=None, next_red=None))
        full = infer(2, {1:1}, (1,0))
        self.assertEqual(full['posterior'], {1: Q(1)})
        self.assertIsNone(full['next_red'])
        self.assertEqual(infer(2, {0:0, 1:1}, (1,))['posterior'][0], 0)

    def test_contracts(self):
        for args, kwargs in [((True,{1:1}),{}), ((0,{0:1}),{}), ((2,{}),{}), ((2,{3:1}),{}),
                ((2,{1:True}),{}), ((2,{1:0}),{}), ((2,{1:-1}),{}), ((2,{1:0.5}),{}),
                ((2,{True:1}),{}), ((2,{1:1},[True]),{}), ((2,{1:1},'1'),{}),
                ((2,{1:1},[2]),{}), ((2,{1:1},[0,1,0]),{}), ((2,{1:1}),{'replacement':1})]:
            with self.subTest(args=args, kwargs=kwargs), self.assertRaises(ValueError):
                infer(*args, **kwargs)

if __name__ == '__main__':
    unittest.main()
