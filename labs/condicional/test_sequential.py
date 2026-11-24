import unittest
from fractions import Fraction as Q
from itertools import product
from .sequential import update

class SequentialConditionalTests(unittest.TestCase):
    def test_all_event_triples_against_distinct_atoms(self):
        labels = "abc"
        events = [{x for i,x in enumerate(labels) if mask & (1 << i)} for mask in range(8)]
        for ws in product(range(3), repeat=3):
            if not sum(ws): continue
            weights = dict(zip(labels,ws))
            atoms = [(x,k) for x,w in weights.items() for k in range(w)]
            for A,B,C in product(events, repeat=3):
                r = update(weights,A,B,C)
                selected = [x for x,k in atoms if x in B and x in C]
                expected = None if not selected else Q(sum(x in A for x in selected),len(selected))
                self.assertEqual(r["final"],expected)
                self.assertEqual(r["staged"],expected)
                self.assertEqual(update(weights,A,C,B)["final"],expected)
                self.assertEqual(update(weights,A,B,B)["final"],r["initial"])
    def test_example_and_chain_rule(self):
        w=dict(a=1,b=2,c=3,d=4,e=5)
        r=update(w,set("ce"),set("abcd"),set("bce"))
        self.assertEqual(r,dict(initial=Q(3,10),second_given_first=Q(1,2),
                               joint_given_first=Q(3,10),staged=Q(3,5),final=Q(3,5)))
        self.assertEqual(Q(2,3)*r["second_given_first"]*r["final"],Q(1,5))
    def test_zero_mass_and_contracts(self):
        self.assertIsNone(update(dict(a=1,b=0),{"a"},{"a"},{"b"})["final"])
        self.assertIsNone(update(dict(a=1,b=0),{"a"},{"b"},{"a"})["staged"])
        for weights in ({},dict(a=0),dict(a=-1),dict(a=True),dict(a=.5)):
            with self.assertRaises(ValueError): update(weights,{"a"},{"a"},{"a"})
        for A,B,C in [({"z"},{"a"},{"a"}),({"a"},{"z"},{"a"}),({"a"},{"a"},{"z"})]:
            with self.assertRaises(ValueError): update(dict(a=1),A,B,C)
