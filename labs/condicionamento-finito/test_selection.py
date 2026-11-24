import itertools
import unittest
from fractions import Fraction as F
from .selection import selected_table

class SelectionTests(unittest.TestCase):
    def test_enumerated_atoms_and_masks(self):
        for weights in itertools.product(range(3), repeat=4):
            if not sum(weights):
                continue
            atoms = [state for state, w in zip(itertools.product(range(2), repeat=2), weights) for _ in range(w)]
            for mask in itertools.product((False, True), repeat=4):
                kept = [s for s in atoms if mask[2*s[0]+s[1]]]
                result = selected_table(weights, mask)
                if not kept:
                    self.assertIsNone(result)
                    continue
                pa = F(sum(a for a,b in kept), len(kept))
                pb = F(sum(b for a,b in kept), len(kept))
                joint = F(sum(a*b for a,b in kept), len(kept))
                self.assertEqual((result['a'],result['b'],result['joint']), (pa,pb,joint))
                self.assertEqual(result['independent'], joint == pa*pb)
                self.assertEqual(result['selection'], F(len(kept),len(atoms)))
                self.assertEqual(sum(result['cells']), 1)
                self.assertEqual(result['a_given_b'], None if pb == 0 else joint/pb)
    def test_counterexample_and_complement(self):
        weights = (1,1,1,1)
        self.assertTrue(selected_table(weights,(True,True,True,True))['independent'])
        r=selected_table(weights,(False,True,True,True))
        self.assertEqual((r['a'],r['b'],r['joint']), (F(2,3),F(2,3),F(1,3)))
        self.assertFalse(r['independent'])
        # No complemento só (0,0) resta; ambos os eventos têm massa zero e são independentes.
        self.assertTrue(selected_table(weights,(True,False,False,False))['independent'])
    def test_scale_invariance(self):
        for mask in itertools.product((False,True), repeat=4):
            self.assertEqual(selected_table((1,2,3,4),mask),selected_table((7,14,21,28),mask))
    def test_contract_and_zero_condition(self):
        self.assertIsNone(selected_table((1,0,0,0),(False,True,True,True)))
        self.assertIsNone(selected_table((1,1,0,0),(True,False,False,False))['a_given_b'])
        for w,m in [((0,0,0,0),(True,)*4),((True,1,1,1),(True,)*4),((-1,1,1,1),(True,)*4),((1.0,1,1,1),(True,)*4),((1,1),(True,)*4),((1,1,1,1),(1,1,1,1))]:
            with self.assertRaises(ValueError): selected_table(w,m)
