import unittest
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from .reports import MODES, likelihood, update

# Independent oracle: enumerate primitive uniform draws, not Bayes formulas.
def atoms(mode):
    counts = Counter()
    for h in (False, True):
        threshold = 3 if h else 1
        for u, v in product(range(4), repeat=2):
            if mode == "independente":
                reports = [(u < threshold, v < threshold)]
            elif mode == "copia":
                reports = [(u < threshold, u < threshold)]
            else:
                # Equiprobable latent switch, independent of h and draws.
                reports = [(u < threshold, v < threshold),
                           (u < threshold, u < threshold)]
            for r1, r2 in reports:
                counts[h, r1, r2] += 1
    return counts

class ReportsTests(unittest.TestCase):
    def test_every_cell_against_uniform_draws(self):
        for mode in MODES:
            c = atoms(mode)
            total = sum(c.values())
            for h, a, b in product((False, True), repeat=3):
                self.assertEqual(Q(c[h, a, b], total),
                                 Q(1, 2)*likelihood(h, a, b, mode))
            for a, b in product((False, True), repeat=2):
                mass = c[True, a, b] + c[False, a, b]
                evidence, posterior = update(a, b, mode)
                self.assertEqual(evidence, Q(mass, total))
                expected = Q(c[True, a, b], mass) if mass else None
                self.assertEqual(posterior, expected)

    def test_same_single_report_marginals_different_joint(self):
        for mode in MODES:
            for h in (False, True):
                expected = Q(3, 4) if h else Q(1, 4)
                self.assertEqual(sum(likelihood(h, True, b, mode)
                                     for b in (False, True)), expected)
                self.assertEqual(sum(likelihood(h, a, True, mode)
                                     for a in (False, True)), expected)
        self.assertEqual([update(True, True, m)[1] for m in MODES],
                         [Q(9,10), Q(3,4), Q(21,26)])

    def test_unconditional_dependence_and_sequential_update(self):
        evidence, posterior = update(True, True, "independente")
        self.assertEqual(evidence, Q(5,16))
        self.assertNotEqual(evidence, Q(1,2)**2)
        # Under conditional independence, after first + the posterior is 3/4.
        stage2 = Q(3,4)*Q(3,4) / (Q(3,4)*Q(3,4)+Q(1,4)*Q(1,4))
        self.assertEqual(stage2, posterior)
        self.assertEqual(update(True, False, "independente")[1], Q(1,2))

    def test_prior_grid_symmetry_and_impossible_report(self):
        for i in range(21):
            prior = Q(i,20)
            for mode in MODES:
                self.assertEqual(sum(update(a,b,mode,prior)[0]
                                     for a,b in product((False,True),repeat=2)), 1)
                for a,b in product((False,True),repeat=2):
                    e,p = update(a,b,mode,prior)
                    e2,p2 = update(not a,not b,mode,1-prior)
                    self.assertEqual(e,e2)
                    self.assertEqual(p2, 1-p if p is not None else None)
        self.assertEqual(update(True, False, "copia"), (0,None))

    def test_contracts(self):
        for invalid in (-1, Q(3,2)):
            with self.assertRaises(ValueError): update(True,True,"copia",invalid)
        for invalid in (True, .5, "1/2", None):
            with self.assertRaises(TypeError): update(True,True,"copia",invalid)
        with self.assertRaises(ValueError): update(True,True,"unknown")
        with self.assertRaises(TypeError): update(1,True,"copia")
        with self.assertRaises(TypeError): likelihood(True,False,None,"misto")

if __name__ == "__main__": unittest.main()
