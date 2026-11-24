"""Intervalo de ocorrência num modelo hipotético; não há dados observados.
Tempos inteiros exatos em dias; versão por densidade avaliada em float.
"""
from fractions import Fraction as Q
from itertools import product
from math import exp, log, expm1, isfinite
import unittest
from mixture import parameters, day, simpson, posterior


def occurrence(a, b, p=Q(1, 2), q=(Q(1, 2), Q(1, 4))):
    p, q = parameters(p, q)
    day(a); day(b)
    if b <= a:
        raise ValueError('Intervalo precisa ter largura positiva')
    masses = tuple(w*(v**a-v**b) for w, v in zip((p, 1-p), q))
    evidence = sum(masses)
    return evidence, tuple(m/evidence for m in masses)


def point_version(t):
    if isinstance(t, bool) or not isinstance(t, (int, float)) or not isfinite(t) or t < 0:
        raise ValueError('Tempo real finito e não negativo')
    # Forma estável: razão das densidades normalizada, não probabilidades pontuais.
    w = 1/(1+2*exp(-log(2)*t))
    return w, 1-w


class Checks(unittest.TestCase):
    def test_joint_cells(self):
        count = 0
        for p, q in product((Q(0), Q(1, 5), Q(1, 2), Q(1)),
                            ((Q(1, 2), Q(1, 4)), (Q(3, 4), Q(1, 3)), (Q(1, 3), Q(1, 3)))):
            table = [(i, k, w*v**k*(1-v)) for i, (w, v) in enumerate(zip((p, 1-p), q)) for k in range(9)]
            for a in range(5):
                for b in range(a+1, 9):
                    cells = [sum(m for i, k, m in table if i == j and a <= k < b) for j in (0, 1)]
                    e, w = occurrence(a, b, p, q)
                    self.assertEqual(e, sum(cells))
                    self.assertEqual(w, tuple(m/sum(cells) for m in cells))
                    # Atualização por sobreviver até a e ocorrer no intervalo novo.
                    e2, w2 = occurrence(0, b-a, posterior(a, p, q)[0], q)
                    self.assertEqual(w2, w)
                    count += 1
        self.assertEqual(count, 360)

    def test_density_integral(self):
        rates = (log(2), 2*log(2))
        for a, b in ((0, 1), (1, 2), (1, 4), (3, 7)):
            values = [simpson(lambda u: .5*r*exp(-r*(a+u)), hi=b-a, n=1024) for r in rates]
            e, w = occurrence(a, b)
            self.assertAlmostEqual(sum(values), float(e), delta=1e-10)
            self.assertAlmostEqual(values[0]/sum(values), float(w[0]), delta=1e-10)

    def test_shrinking_intervals(self):
        rates = (log(2), 2*log(2))
        for t in (.25, 1, 2, 5):
            errors = []
            for width in (.1, .01, .001, .0001):
                masses = [.5*exp(-r*t)*(-expm1(-r*width)) for r in rates]
                errors.append(abs(masses[0]/sum(masses)-point_version(t)[0]))
            self.assertTrue(all(y < x for x, y in zip(errors, errors[1:])))
            self.assertLess(errors[-1], 1e-5)
        self.assertAlmostEqual(point_version(2)[0], 2/3)
        self.assertNotAlmostEqual(point_version(2)[0], float(occurrence(1, 2)[1][0]))

    def test_examples_and_contracts(self):
        self.assertEqual(occurrence(1, 2), (Q(7, 32), (Q(4, 7), Q(3, 7))))
        self.assertEqual(occurrence(0, 1, Q(2, 3))[0], Q(7, 12))
        for a, b in ((1, 1), (2, 1), (-1, 2), (True, 2), (0, .5)):
            with self.assertRaises(ValueError): occurrence(a, b)
        for t in (-1, float('inf'), float('nan'), True):
            with self.assertRaises(ValueError): point_version(t)


if __name__ == '__main__':
    print('Registro 1<T≤2:', occurrence(1, 2), '; versão t=2:', point_version(2))
    unittest.main()
