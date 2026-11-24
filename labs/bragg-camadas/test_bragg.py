import unittest
import math
from .bragg import orders, intensity


class BraggTests(unittest.TestCase):
    def test_angles_and_units(self):
        rows = orders(.30, .15)
        self.assertEqual([r[0] for r in rows], [1, 2, 3, 4])
        self.assertAlmostEqual(rows[1][1], 30)
        self.assertAlmostEqual(rows[1][2], 60)
        self.assertEqual(rows[-1][1:], (90, 180))
        for scale in (1e-9, 1, 1000):
            scaled = orders(.30 * scale, .15 * scale)
            self.assertEqual(len(rows), len(scaled))
            for a, b in zip(rows, scaled):
                for x, y in zip(a, b): self.assertAlmostEqual(x, y)
        self.assertEqual(orders(1, 3), [])

    def test_literal_parity_landmarks(self):
        for n in (1, 2, 5, 9):
            for m in (1, 2, 3, 4):
                self.assertAlmostEqual(intensity(n, m, 1), (0 if m % 2 else 4) * n*n)
                self.assertAlmostEqual(intensity(n, m, .5), (.25 if m % 2 else 2.25) * n*n)
                self.assertAlmostEqual(intensity(n, m, 0), n*n)

    def test_pairwise_real_reference(self):
        # Independent |sum a exp(i phase)|² = sum_i sum_j a_i a_j cos(phase_i-phase_j).
        for n in (1, 2, 3, 5, 7):
            for c in (.125, 1/3, .875, 1.2, 2.5):
                for b in (0, .5, 1):
                    sites = [(j, 1) for j in range(n)] + [(j+.5, b) for j in range(n)]
                    ref = math.fsum(w*v*math.cos(2*math.pi*c*(x-y))
                                    for x,w in sites for y,v in sites)
                    self.assertAlmostEqual(intensity(n,c,b), ref, places=10)

    def test_finite_width_and_period(self):
        for n in (2, 3, 5, 8):
            # N equal cells, first zero of lattice sum beside even order m=2.
            self.assertLess(intensity(n, 2+1/n), 1e-24)
            self.assertGreater(intensity(n, 2+.1/n), 0)
            for c in (.125, .33, .8):
                self.assertAlmostEqual(intensity(n,c,1), intensity(n,c+2,1), places=10)
                self.assertAlmostEqual(intensity(n,c,0), intensity(n,c+1,0), places=10)

    def test_contracts(self):
        for d,w in [(0,1),(1,-1),(True,1),(1,'a'),(float('inf'),1),(1,float('nan')),(10001,1)]:
            with self.assertRaises(ValueError): orders(d,w)
        for args in [(0,1,1),(True,1,1),(10001,1,1),(1,True,1),(1,1,True),(1,1,-.1),(1,1,1.1),(1,float('nan'),1),(1,1e7,1),(1,10**1000,1),(1,1,10**1000)]:
            with self.assertRaises(ValueError): intensity(*args)


if __name__ == '__main__': unittest.main()
