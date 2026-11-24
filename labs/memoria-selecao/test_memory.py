import unittest
from itertools import product
from .memory import decoder, read, transition, TRACE


class MemoryTests(unittest.TestCase):
    def test_all_bytes_and_controls_against_indexed_reference(self):
        state = (3, 85, 170, 240)
        for address, data, we, event in product(range(4), range(256), range(2), range(2)):
            with self.subTest(address=address, data=data, we=we, event=event):
                expected = list(state)
                if we == 1 and event == 1:
                    expected[address] = data
                result = transition(state, address, data, we, event)
                self.assertEqual(result, tuple(expected))
                self.assertEqual(read(result, address), expected[address])
                self.assertEqual(state, (3, 85, 170, 240))

    def test_decoder_and_read_for_varied_states(self):
        for address in range(4):
            expected = tuple(int(j == address) for j in range(4))
            self.assertEqual(decoder(address), expected)
            self.assertEqual(sum(decoder(address)), 1)
        for state in product((0, 1, 128, 255), repeat=4):
            for address in range(4):
                self.assertEqual(read(state, address), state[address])

    def test_literal_event_trace_and_snapshots(self):
        state = (3, 85, 170, 240)
        history = [state]
        expected = [(170, 170, (3, 85, 170, 240)),
                    (170, 9, (3, 85, 9, 240)),
                    (9, 9, (3, 85, 9, 240)),
                    (85, 200, (3, 200, 9, 240)),
                    (9, 13, (3, 200, 13, 240)),
                    (13, 13, (3, 200, 13, 240))]
        for inputs, (before, after, result) in zip(TRACE, expected):
            self.assertEqual(read(state, inputs[0]), before)
            state = transition(state, *inputs)
            self.assertEqual(state, result)
            self.assertEqual(read(state, inputs[0]), after)
            history.append(state)
        self.assertEqual(history[0], (3, 85, 170, 240))
        self.assertEqual(history[2], (3, 85, 9, 240))

    def test_order_and_noninterference(self):
        state = (3, 85, 170, 240)
        for i, j in product(range(4), repeat=2):
            left = transition(transition(state, i, 17, 1, 1), j, 99, 1, 1)
            right = transition(transition(state, j, 99, 1, 1), i, 17, 1, 1)
            if i != j:
                self.assertEqual(left, right)
            else:
                self.assertNotEqual(left, right)
                self.assertEqual(left[i], 99)
                self.assertEqual(right[i], 17)
            for k in set(range(4)) - {i, j}:
                self.assertEqual(left[k], state[k])

    def test_contracts_even_with_disabled_write(self):
        good = (3, 85, 170, 240)
        for bad in [[], [0]*4, (0,)*3, (0, 0, 0, 256), (0, 0, 0, True)]:
            with self.assertRaises(ValueError): read(bad, 0)
            with self.assertRaises(ValueError): transition(bad, 0, 0, 0, 0)
        for bad in [-1, 4, 1.0, True, '1', None]:
            with self.assertRaises(ValueError): decoder(bad)
            with self.assertRaises(ValueError): read(good, bad)
        for bad in [-1, 256, 1.0, True, None]:
            with self.assertRaises(ValueError): transition(good, 0, bad, 0, 0)
        for bad in [-1, 2, 0.0, True, None]:
            with self.assertRaises(ValueError): transition(good, 0, 0, bad, 1)
            with self.assertRaises(ValueError): transition(good, 0, 0, 1, bad)
