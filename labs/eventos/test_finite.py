import unittest
from fractions import Fraction as Q
from itertools import combinations
from .finite import distribution, event_probability, analyze, binary_table

class FiniteProbabilityTests(unittest.TestCase):
    def test_all_die_event_pairs_by_indicator_count(self):
        space = tuple(range(1, 7)); weights = {x: Q(1, 6) for x in space}
        subsets = [set(c) for n in range(7) for c in combinations(space, n)]
        for a in subsets:
            for b in subsets:
                r = analyze(weights, a, b)
                union = Q(sum(x in a or x in b for x in space), 6)
                joint = Q(sum(x in a and x in b for x in space), 6)
                self.assertEqual(r['union'], union)
                self.assertEqual(r['intersection'], joint)
                self.assertEqual(r['union'], r['a'] + r['b'] - joint)
                self.assertEqual(r['complement_a'] + r['a'], 1)
        biased = {1: Q(1, 10), 2: Q(2, 10), 3: Q(7, 10)}
        self.assertEqual(event_probability(biased, {1, 2}), Q(3, 10))
        self.assertEqual(event_probability(biased, [1, 1, 2]), Q(3, 10))

    def test_binary_tables_marginals_and_extremes(self):
        grid = [Q(i, 4) for i in range(5)]
        a, b = {(1, 0), (1, 1)}, {(0, 1), (1, 1)}
        for p in grid:
            for q in grid:
                for position in grid:
                    w = binary_table(p, q, position); r = analyze(w, a, b)
                    self.assertEqual(sum(w.values()), 1)
                    self.assertTrue(all(0 <= v <= 1 for v in w.values()))
                    self.assertEqual(r['a'], p); self.assertEqual(r['b'], q)
                    self.assertLessEqual(r['intersection'], min(p, q))
                    self.assertGreaterEqual(r['intersection'], max(0, p + q - 1))
                    if q == 0: self.assertIsNone(r['a_given_b'])
                    else: self.assertEqual(r['a_given_b'] * q, r['intersection'])
        half = Q(1, 2)
        self.assertFalse(analyze(binary_table(half, half, 0), a, b)['independent'])
        self.assertTrue(analyze(binary_table(half, half, half), a, b)['independent'])
        self.assertFalse(analyze(binary_table(half, half, 1), a, b)['independent'])

    def test_pairwise_not_mutual_and_zero_covariance(self):
        w = {(a, b): Q(1, 4) for a in (0, 1) for b in (0, 1)}
        a = {x for x in w if x[0]}; b = {x for x in w if x[1]}
        c = {x for x in w if x[0] == x[1]}
        for x, y in [(a, b), (a, c), (b, c)]: self.assertTrue(analyze(w, x, y)['independent'])
        self.assertEqual(event_probability(w, a & b & c), Q(1, 4))
        self.assertNotEqual(event_probability(w, a & b & c), Q(1, 8))
        ex = sum(Q(x, 3) for x in (-1, 0, 1))
        ey = sum(Q(x*x, 3) for x in (-1, 0, 1))
        exy = sum(Q(x*x*x, 3) for x in (-1, 0, 1))
        self.assertEqual(exy - ex*ey, 0)
        wxy = {(x, x*x): Q(1, 3) for x in (-1, 0, 1)}
        zero_x = {pair for pair in wxy if pair[0] == 0}
        zero_y = {pair for pair in wxy if pair[1] == 0}
        r = analyze(wxy, zero_x, zero_y)
        self.assertEqual(r['intersection'], Q(1, 3))
        self.assertEqual(r['a'] * r['b'], Q(1, 9))
        self.assertFalse(r['independent'])

    def test_contracts_and_null_events(self):
        for w in [{}, {1: Q(1, 2)}, {1: True}, {1: .5, 2: .5}, {1: Q(-1, 2), 2: Q(3, 2)}]:
            with self.assertRaises(ValueError): distribution(w)
        with self.assertRaises(ValueError): event_probability({1: Q(1)}, {2})
        for bad in [True, .5, Q(-1, 4), Q(5, 4)]:
            with self.assertRaises(ValueError): binary_table(bad, 1, 1)
        r = analyze({1: Q(1), 2: Q(0)}, {2}, {1})
        self.assertTrue(r['independent']); self.assertEqual(r['a_given_b'], 0)
        r = analyze({1: Q(1), 2: Q(0)}, {1}, {2})
        self.assertIsNone(r['a_given_b']); self.assertTrue(r['independent'])

if __name__ == '__main__': unittest.main()
