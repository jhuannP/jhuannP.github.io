"""Modelo didático original; probabilidades racionais, sem dados reais."""
from fractions import Fraction as Q
from itertools import product
import unittest


def probability(value):
    if isinstance(value, bool) or not isinstance(value, (int, Q)) or not 0 <= value <= 1:
        raise ValueError('Use int ou Fraction em [0,1]')
    return Q(value)


def record(bits):
    for i, bit in enumerate(bits):
        if bit == 1:
            return '0' * i + '1'
    return '0' * len(bits)


def table(prior=Q(1, 2), high=Q(3, 4), low=Q(1, 4)):
    """Conjuntas sobre hipótese e registro, somando oito sequências potenciais."""
    prior, high, low = map(probability, (prior, high, low))
    result = {r: [Q(0), Q(0)] for r in ('1', '01', '001', '000')}
    for h, base, rate in ((0, prior, high), (1, 1-prior, low)):
        for bits in product((0, 1), repeat=3):
            weight = base
            for bit in bits:
                weight *= rate if bit else 1-rate
            result[record(bits)][h] += weight
    return result


def posterior(masses):
    total = sum(masses)
    return masses[0] / total if total else None


class Checks(unittest.TestCase):
    def test_example(self):
        t = table()
        self.assertEqual(sum(t['001']), Q(3, 32))
        self.assertEqual(posterior(t['001']), Q(1, 4))
        success = [sum(t[r][h] for r in ('1', '01', '001')) for h in (0, 1)]
        self.assertEqual(sum(success), Q(25, 32))
        self.assertEqual(posterior(success), Q(63, 100))
        self.assertEqual(posterior(t['000']), Q(1, 28))

    def test_enumeration_against_prefix_formula(self):
        # Independent geometric-prefix expressions, including degenerate rates.
        for prior, a, b in product((Q(0), Q(1,4), Q(1,2), Q(3,4), Q(1)), repeat=3):
            t = table(prior, a, b)
            for h, base, rate in ((0, prior, a), (1, 1-prior, b)):
                for n in (1, 2, 3):
                    self.assertEqual(t['0'*(n-1)+'1'][h], base*(1-rate)**(n-1)*rate)
                self.assertEqual(t['000'][h], base*(1-rate)**3)
            self.assertEqual(sum(map(sum, t.values())), 1)
            # Average posterior over possible records recovers the prior.
            self.assertEqual(sum(sum(m)*posterior(m) for m in t.values() if sum(m)), prior)

    def test_fixed_protocol_and_coarsening(self):
        t = table()
        fixed = [sum(Q(1,2)*rate**sum(bits)*(1-rate)**(2-sum(bits))
                     for bits in product((0,1), repeat=2) if bits == (0,1))
                 for rate in (Q(3,4), Q(1,4))]
        self.assertEqual(fixed, t['01'])
        self.assertEqual(sum(fixed), Q(3,16))
        self.assertEqual(posterior(fixed), Q(1,2))
        count = [2*x for x in fixed]
        self.assertEqual(sum(count), Q(3,8))
        self.assertEqual(posterior(count), Q(1,2))

    def test_zero_evidence_and_contract(self):
        self.assertIsNone(posterior(table(high=1, low=1)['000']))
        self.assertIsNone(posterior(table(high=0, low=0)['1']))
        for invalid in (True, .5, Q(-1), Q(2), '1/2'):
            with self.assertRaises(ValueError):
                table(prior=invalid)


if __name__ == '__main__':
    for key, masses in table().items():
        print(key, 'conjuntas:', masses, 'posterior H:', posterior(masses))
    unittest.main()
