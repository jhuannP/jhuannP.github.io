import unittest
from fractions import Fraction as Q
from itertools import product
from .weighted import condition

class WeightedConditionalTests(unittest.TestCase):
    def test_against_distinct_equiprobable_atoms(self):
        # Enumeração independente: cada rótulo expande em w objetos distintos.
        labels = tuple("abcd")
        events = [{labels[i] for i in range(4) if mask & (1 << i)} for mask in range(16)]
        for ws in product(range(3), repeat=4):
            if not sum(ws): continue
            weights = dict(zip(labels, ws))
            atoms = [(label, i) for label, w in weights.items() for i in range(w)]
            for A in events:
                for B in events:
                    selected = [x for x in atoms if x[0] in B]
                    expected = Q(sum(x[0] in A for x in selected), len(selected)) if selected else None
                    self.assertEqual(condition(weights, A, B), expected)

    def test_scale_and_rational_weights(self):
        w = dict(a=1,b=2,c=3,d=4); A={"a","c"}; B={"b","c"}
        self.assertEqual(condition(w,A,B), Q(3,5))
        self.assertEqual(condition(w,B,A), Q(3,4))
        for scale in (Q(1,10), Q(7,3), 100):
            self.assertEqual(condition({k:v*scale for k,v in w.items()},A,B),Q(3,5))
        self.assertEqual(condition(w,A,B)+condition(w,set(w)-A,B),1)

    def test_zero_mass_and_invalid_models(self):
        self.assertIsNone(condition(dict(a=1,b=0),{"a"},{"b"}))
        for w in ({},dict(a=0),dict(a=-1),dict(a=True),dict(a=.5)):
            with self.assertRaises(ValueError): condition(w,set(),set())
        with self.assertRaises(ValueError): condition(dict(a=1),{"x"},{"a"})
