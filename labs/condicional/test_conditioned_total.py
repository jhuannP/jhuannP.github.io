"""Identidades sob informação adicional, sem supor independência."""
import unittest
from fractions import Fraction as Q
from itertools import product
from .weighted import condition

class ConditionedTotalTests(unittest.TestCase):
    def test_all_two_group_partitions_with_zero_cells(self):
        labels = "abc"
        events = [{x for i,x in enumerate(labels) if mask & (1<<i)} for mask in range(8)]
        for ws in product(range(3),repeat=3):
            if not sum(ws): continue
            weights = dict(zip(labels,ws))
            atoms = [x for x,w in weights.items() for _ in range(w)]
            for A,C,B in product(events,repeat=3):
                selected = [x for x in atoms if x in C]
                if not selected: continue
                expected = Q(sum(x in A for x in selected),len(selected))
                total = Q(0)
                for group in (B,set(labels)-B):
                    within = [x for x in selected if x in group]
                    if within:
                        total += condition(weights,A,group&C)*condition(weights,group,C)
                    else:
                        self.assertIsNone(condition(weights,A,group&C))
                self.assertEqual(total,expected)
                self.assertEqual(condition(weights,A,C),expected)

    def test_die_changes_both_weights_and_rates(self):
        weights = {n:1 for n in range(1,7)}
        A,E,O,C = {2,3,5},{2,4,6},{1,3,5},{2,3,4,5,6}
        self.assertEqual(condition(weights,O,C),Q(2,5))
        self.assertEqual(condition(weights,A,O&C),1)
        correct = sum(condition(weights,A,B&C)*condition(weights,B,C) for B in (E,O))
        wrong = sum(condition(weights,A,B)*condition(weights,B,C) for B in (E,O))
        self.assertEqual(correct,Q(3,5))
        self.assertEqual(wrong,Q(7,15))
        self.assertNotEqual(correct,wrong)

    def test_conditioned_measure_normalization_and_complement(self):
        w = dict(a=1,b=2,c=3,d=0)
        C = {"b","c"}
        space = set(w)
        self.assertEqual(condition(w,space,C),1)
        self.assertEqual(condition(w,set(),C),0)
        for mask in range(16):
            A = {x for i,x in enumerate(w) if mask & (1<<i)}
            self.assertEqual(condition(w,A,C)+condition(w,space-A,C),1)
