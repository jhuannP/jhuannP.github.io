import unittest
from fractions import Fraction as Q
from itertools import product
from .experiment import moments, binomial

class MomentTests(unittest.TestCase):
    def test_known_moments_and_affine_transform(self):
        r = moments(range(1, 7), [Q(1, 6)]*6)
        self.assertEqual(r['mean'], Q(7, 2)); self.assertEqual(r['variance'], Q(35, 12))
        for origin in (-3, 0, 10**8):
            for scale in (-2, 0, 3):
                s = moments([scale*x+origin for x in range(1, 7)], [Q(1, 6)]*6)
                self.assertEqual(s['mean'], scale*r['mean']+origin)
                self.assertEqual(s['variance'], scale**2*r['variance'])
        self.assertEqual(moments([10**8-1, 10**8+1], [Q(1, 2)]*2)['variance'], 1)

    def test_two_point_reference_and_second_identity(self):
        for a in (-3, 0, 3):
            for d in (0, 2, 6):
                for p in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
                    r = moments([a, a+d], [1-p, p])
                    self.assertEqual(r['mean'], a+d*p)
                    self.assertEqual(r['variance'], d*d*p*(1-p))
                    self.assertEqual(r['variance'], r['second']-r['mean']**2)
                    self.assertGreaterEqual(r['variance'], 0)

    def test_binomial_against_enumerated_sequences(self):
        for n in range(9):
            for p in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
                observed = [Q(0)]*(n+1)
                for seq in product((0, 1), repeat=n):
                    weight = Q(1)
                    for bit in seq: weight *= p if bit else 1-p
                    observed[sum(seq)] += weight
                result = binomial(n, p)
                self.assertEqual(result, observed); self.assertEqual(sum(result), 1)
                r = moments(range(n+1), result)
                self.assertEqual(r['mean'], n*p); self.assertEqual(r['variance'], n*p*(1-p))
        for n in (20, 100):
            r = binomial(n, Q(1, 3)); self.assertEqual(sum(r), 1)
            self.assertEqual(moments(range(n+1), r)['mean'], Q(n, 3))

    def test_contracts(self):
        for values, weights in [([], []), ([1], []), ([1], [Q(1, 2)]), ([1, 2], [Q(-1), Q(2)]), ([True], [1]), ([.5], [1])]:
            with self.assertRaises(ValueError): moments(values, weights)
        for n, p in [(True, 0), (-1, 0), (101, 0), (1.5, 0), (1, True), (1, .5), (1, Q(-1, 2)), (1, Q(3, 2))]:
            with self.assertRaises(ValueError): binomial(n, p)

if __name__ == '__main__': unittest.main()
