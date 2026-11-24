import unittest
from fractions import Fraction as Q
from .experiment import REACTIONS,combine,ledger

class GlycolysisLedgerTests(unittest.TestCase):
    def test_each_reaction_preserves_selected_inventories(self):
        # Carbon map follows only the glucose-derived skeleton, not carbon inside ATP/NAD.
        carbon=dict(glucose=6,G6P=6,F6P=6,FBP=6,DHAP=3,GAP=3,BPG=3,PG3=3,PG2=3,PEP=3,pyruvate=3)
        phosphate=dict(ATP=3,ADP=2,Pi=1,G6P=1,F6P=1,FBP=2,DHAP=1,GAP=1,BPG=2,PG3=1,PG2=1,PEP=1)
        for r in REACTIONS:
            self.assertEqual(sum(v*carbon.get(s,0) for s,v in r.items()),0)
            self.assertEqual(sum(v*phosphate.get(s,0) for s,v in r.items()),0)
            self.assertEqual(r.get("ATP",0)+r.get("ADP",0),0)
            self.assertEqual(r.get("NAD+",0)+r.get("NADH",0),0)

    def test_net_inventory_and_fractional_moles(self):
        expected={"glucose":-1,"ATP":2,"ADP":-2,"Pi":-2,"NAD+":-2,"NADH":2,"pyruvate":2,"water":2}
        for amount in (Q(0),Q(1,2),Q(1),Q(3),Q(10)):
            r=ledger(amount)
            for species,value in r["net"].items():
                self.assertEqual(value,amount*expected.get(species,0))
            self.assertEqual((r["atp_used"],r["atp_made"],r["atp_net"]),(2*amount,4*amount,2*amount))
            self.assertEqual(6*amount,3*r["net"]["pyruvate"])

    def test_missing_branch_multiplicity_leaves_intermediate(self):
        wrong=combine((1,)*10)
        self.assertEqual(wrong["GAP"],1)
        self.assertEqual(wrong["pyruvate"],1)
        self.assertEqual(wrong["ATP"],0)
        self.assertEqual(ledger(1)["net"]["GAP"],0)

    def test_prefix_investment_and_gross_accounting(self):
        prefix=combine((1,1,1,1,1,0,0,0,0,0))
        self.assertEqual(prefix["ATP"],-2)
        self.assertEqual(prefix["GAP"],2)
        self.assertEqual(ledger(1)["atp_made"],2+2)
        self.assertEqual(ledger(1)["atp_net"],-1-1+2+2)

    def test_contracts(self):
        for amount in (-1,True,.5,"1"):
            with self.assertRaises(ValueError):ledger(amount)
        for extents in ([],[1]*9,[1]*11,[1]*9+[-1],[1]*9+[True],[1]*9+[.5]):
            with self.assertRaises(ValueError):combine(extents)
