import unittest
from .alu import evaluate, signed, OPS


class ALUTests(unittest.TestCase):
    def test_all_inputs_with_independent_arithmetic_and_truth_tables(self):
        truth = {'AND': (0, 0, 0, 1), 'OR': (0, 1, 1, 1),
                 'XOR': (0, 1, 1, 0)}
        for a in range(16):
            for b in range(16):
                sa, sb = a if a < 8 else a - 16, b if b < 8 else b - 16
                for op in OPS:
                    with self.subTest(a=a, b=b, op=op):
                        d = evaluate(a, b, op)
                        if op == 'ADD':
                            expected = (a + b) % 16
                            c = int(a + b >= 16)
                            v = int(not -8 <= sa + sb <= 7)
                        else:
                            expected = sum(truth[op][2*((a//(2**i)) % 2)+((b//(2**i)) % 2)] * 2**i for i in range(4))
                            c = v = 0
                        self.assertEqual((d['result'], d['z'], d['c'], d['v']),
                                         (expected, int(expected == 0), c, v))

    def test_carry_invariant_at_every_prefix(self):
        for a in range(16):
            for b in range(16):
                d = evaluate(a, b, 'ADD')
                for i in range(5):
                    base = 2**i
                    self.assertEqual(a % base + b % base,
                                     d['result'] % base + base * d['carries'][i])

    def test_four_flag_witnesses(self):
        cases = [(7, 1, (8, 0, 0, 1)), (15, 1, (0, 1, 1, 0)),
                 (8, 8, (0, 1, 1, 1)), (2, 3, (5, 0, 0, 0))]
        for a, b, expected in cases:
            d = evaluate(a, b, 'ADD')
            self.assertEqual(tuple(d[k] for k in ['result', 'z', 'c', 'v']), expected)
        self.assertEqual(evaluate(7, 1, 'ADD')['carries'], (0, 1, 1, 1, 0))

    def test_signed_decode_and_logic_contract(self):
        self.assertEqual([signed(i) for i in range(16)], list(range(8)) + list(range(-8, 0)))
        for op in ['AND', 'OR', 'XOR']:
            self.assertEqual(evaluate(8, 8, op)['c'], 0)
            self.assertEqual(evaluate(8, 8, op)['v'], 0)
        # Carry interno calculado não é flag publicada numa operação lógica.
        self.assertEqual(evaluate(15, 1, 'OR')['carries'][4], 1)
        self.assertEqual(evaluate(15, 1, 'OR')['c'], 0)

    def test_reject_invalid_inputs(self):
        for invalid in [-1, 16, True, 1.0, '1', None]:
            for a, b in [(invalid, 0), (0, invalid)]:
                with self.assertRaises(ValueError): evaluate(a, b, 'ADD')
        for op in ['SUB', 'add', '', 0, None, []]:
            with self.assertRaises(ValueError): evaluate(1, 2, op)
