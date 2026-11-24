import unittest
from fractions import Fraction as F
from .response import rate, describe, COUNTS


class ResponseTests(unittest.TestCase):
    def test_literal_activity_answer(self):
        result = describe(COUNTS)
        self.assertEqual(result['rates'], {'A0': F(1, 10), 'A1': F(7, 10), 'B0': F(1, 20), 'B1': F(3, 20)})
        self.assertEqual(result['delta_a'], F(3, 5))
        self.assertEqual(result['delta_b'], F(1, 10))
        self.assertEqual(result['contrast'], F(1, 2))
        self.assertEqual(result['rates']['A1']/result['rates']['A0'], 7)
        self.assertEqual(result['rates']['B1']/result['rates']['B0'], 3)

    def test_reexpressing_same_proportions(self):
        for scale in [2, 3, 7, 11]:
            counts = {key: (k*scale, n*scale) for key, (k, n) in COUNTS.items()}
            self.assertEqual(describe(counts), describe(COUNTS))
        # Reexpressar a tabela não cria novas réplicas ou precisão experimental.
        self.assertEqual(rate(0, 20), 0)
        self.assertEqual(rate(20, 20), 1)

    def test_relabeling_signal_changes_contrast_direction(self):
        swapped = {'A0': COUNTS['A1'], 'A1': COUNTS['A0'],
                   'B0': COUNTS['B1'], 'B1': COUNTS['B0']}
        result = describe(swapped)
        self.assertEqual(result['delta_a'], F(-3, 5))
        self.assertEqual(result['delta_b'], F(-1, 10))
        self.assertEqual(result['contrast'], F(-1, 2))
        same = {'A0': (2, 20), 'A1': (14, 20), 'B0': (1, 10), 'B1': (7, 10)}
        self.assertEqual(describe(same)['contrast'], 0)

    def test_invalid_inputs(self):
        for k, n in [(-1, 20), (21, 20), (1, 0), (0, -1), (True, 20), (1, True), (1.0, 20)]:
            with self.assertRaises(ValueError): rate(k, n)
        for counts in [{}, dict(COUNTS, C0=(1, 20)), dict(COUNTS, A0=[1, 20]), dict(COUNTS, A0=(1,))]:
            with self.assertRaises(ValueError): describe(counts)
