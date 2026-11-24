import unittest
from copy import deepcopy
from itertools import product, permutations
from .network import evaluate, XOR_NETWORK


class NetworkTests(unittest.TestCase):
    def test_xor_all_inputs_and_declaration_orders(self):
        original = deepcopy(XOR_NETWORK)
        for order in permutations(XOR_NETWORK):
            gates = {k: XOR_NETWORK[k] for k in order}
            for a, b in product((0, 1), repeat=2):
                inputs = {'A': a, 'B': b}
                r = evaluate(inputs, gates, ('z',))
                self.assertEqual(r['outputs'], {'z': a ^ b})
                self.assertEqual(r['gate_count'], 4)
                self.assertEqual(r['output_depth'], 3)
                self.assertEqual(r['depth'], {'A':0,'B':0,'u':1,'v':1,'w':2,'z':3})
                self.assertEqual(inputs, {'A':a,'B':b})
        self.assertEqual(XOR_NETWORK, original)

    def test_demorgan_and_counterexample(self):
        gates = {'t':('AND',('A','B')), 'left':('NOT',('t',)),
                 'na':('NOT',('A',)), 'nb':('NOT',('B',)),
                 'right':('OR',('na','nb'))}
        for a, b in product((0,1), repeat=2):
            r = evaluate({'A':a,'B':b}, gates, ('left','right'))
            self.assertEqual(r['outputs']['left'], 1-a*b)
            self.assertEqual(r['outputs']['left'], r['outputs']['right'])
        r = evaluate({'A':1,'B':1}, XOR_NETWORK, ('u','z'))
        self.assertEqual(r['outputs'], {'u':1,'z':0})

    def test_basis_fanout_and_unused_gates(self):
        primitive = evaluate({'A':1,'B':0}, {'z':('XOR',('A','B'))}, ('z',))
        self.assertEqual((primitive['gate_count'],primitive['output_depth']), (1,1))
        r = evaluate({'A':1}, {'n':('NOT',('A',)), 'q':('AND',('n','n'))}, ('A',))
        self.assertEqual(r['outputs'], {'A':1})
        self.assertEqual((r['gate_count'],r['output_depth']), (2,0))
        self.assertEqual(r['values']['q'], 0)
        self.assertEqual(evaluate({'A':0},{},('A',))['output_depth'],0)

    def test_invalid_networks(self):
        invalid = [({'A':True},{},('A',)), ({'A':0.0},{},('A',)),
                   ({'A':2},{},('A',)), ({'':0},{},('',)),
                   ({'A':0},{'A':('NOT',('A',))},('A',)),
                   ({'A':0},{'z':('NOT',('missing',))},('z',)),
                   ({'A':0},{'z':('BAD',('A',))},('z',)),
                   ({'A':0},{'z':('AND',('A',))},('z',)),
                   ({'A':0},{'z':('NOT',('z',))},('A',)),
                   ({'A':0},{'x':('NOT',('y',)), 'y':('NOT',('x',))},('x',)),
                   ({'A':0},{},('missing',)), ({'A':0},{},()),
                   ({'A':0},{'z':['NOT',('A',)]},('z',)),
                   ({str(i):0 for i in range(65)},{},('0',))]
        for args in invalid:
            with self.subTest(args=args), self.assertRaises(ValueError):
                evaluate(*args)


if __name__ == '__main__': unittest.main()
