import unittest
from fractions import Fraction as Q
from itertools import product
from .independence import audit
from .weighted import condition

class ConditionalIndependenceTests(unittest.TestCase):
    def test_coins_and_condition_removal(self):
        w = dict.fromkeys(["00", "01", "10", "11"], 1)
        A, B, C = {"10", "11"}, {"01", "11"}, {"00", "11"}
        self.assertTrue(audit(w,A,B,set(w))["independent"])
        r=audit(w,A,B,C)
        self.assertEqual(r,dict(a=Q(1,2),b=Q(1,2),joint=Q(1,2),
                                product=Q(1,4),independent=False))
        self.assertEqual(condition(w,A,B&C),1)
        self.assertEqual(condition(w,A,C),Q(1,2))
        self.assertEqual(condition(w,A,B),Q(1,2))
    def test_enumerated_atoms(self):
        labels="abc"
        events=[{x for i,x in enumerate(labels) if mask&(1<<i)} for mask in range(8)]
        for ws in product(range(3),repeat=3):
            if not sum(ws):continue
            w=dict(zip(labels,ws))
            for A,B,C in product(events,repeat=3):
                atoms=[x for x in labels for _ in range(w[x]) if x in C]
                r=audit(w,A,B,C)
                if not atoms:
                    self.assertIsNone(r["independent"]);continue
                n=len(atoms);na=sum(x in A for x in atoms);nb=sum(x in B for x in atoms)
                nab=sum(x in A and x in B for x in atoms)
                self.assertEqual(r["joint"],Q(nab,n))
                self.assertEqual(r["independent"],nab*n==na*nb)
                self.assertEqual(audit(w,B,A,C),dict(a=r["b"],b=r["a"],joint=r["joint"],
                                  product=r["product"],independent=r["independent"]))
                if nb and r["independent"]:
                    self.assertEqual(condition(w,A,B&C),r["a"])
    def test_zero_mass_validation_and_no_mutation(self):
        w=dict(a=2,b=0);copy=w.copy()
        self.assertIsNone(audit(w,{"a"},{"b"},{"b"})["independent"])
        self.assertEqual(w,copy)
        for invalid in ({},dict(a=0),dict(a=-1),dict(a=True),dict(a=.5)):
            with self.assertRaises(ValueError):audit(invalid,{"a"},{"a"},{"a"})
        for A,B,C in [({"z"},{"a"},{"a"}),({"a"},{"z"},{"a"}),({"a"},{"a"},{"z"})]:
            with self.assertRaises(ValueError):audit(w,A,B,C)
