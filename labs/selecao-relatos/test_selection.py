from fractions import Fraction as Q
from itertools import product
import unittest
from .selection import joint, condition

class SelectionTests(unittest.TestCase):
    def test_declared_examples(self):
        a=joint(Q(1,2),Q(3,4),Q(1,4),{(h,r):Q(1,2) if r else Q(1) for h,r in product((False,True),repeat=2)})
        b=joint(Q(1,2),Q(3,4),Q(1,4),{(h,r):Q(1,2) if h else Q(3,4) for h,r in product((False,True),repeat=2)})
        self.assertEqual([condition(a,recorded=True),condition(a,report=True,recorded=True),condition(a,recorded=False)], [Q(5,12),Q(3,4),Q(3,4)])
        self.assertEqual([condition(b,recorded=True),condition(b,report=True,recorded=True),condition(b,recorded=False)], [Q(2,5),Q(2,3),Q(2,3)])
        self.assertEqual(sum(a.values()),1); self.assertEqual(sum(b.values()),1)

    def test_independent_enumeration_of_primitive_draws(self):
        # No products of probabilities in the independent counting oracle.
        # Enumerate three independent draws (64 outcomes); all rates are multiples of 1/4.
        for prior_n in (0,1,2,3,4):
            for rates_n in ((2,2,2,2),(1,2,3,4),(0,4,0,4),(0,0,0,0),(4,4,4,4)):
                keys=list(product((False,True),repeat=2)); rates={k:Q(n,4) for k,n in zip(keys,rates_n)}
                actual=joint(Q(prior_n,4),Q(3,4),Q(1,4),rates)
                counts={k:0 for k in product((False,True),repeat=3)}
                for u,v,w in product(range(4),repeat=3):
                    h=u<prior_n; r=v<(3 if h else 1); s=w<rates_n[keys.index((h,r))]
                    counts[h,r,s]+=1
                self.assertEqual(actual,{k:Q(v,64) for k,v in counts.items()})
                for report,recorded in product((None,False,True),repeat=2):
                    good=[(k,n) for k,n in counts.items() if (report is None or k[1] is report) and (recorded is None or k[2] is recorded)]
                    denominator=sum(n for k,n in good)
                    expected=None if denominator==0 else Q(sum(n for k,n in good if k[0]),denominator)
                    self.assertEqual(condition(actual,report=report,recorded=recorded),expected)

    def test_cancellation_when_selection_depends_only_on_report(self):
        for prior,plus,minus,keep in product((Q(1,4),Q(1,2),Q(3,4)),repeat=4):
            table=joint(prior,plus,minus,{(h,r):keep if r else Q(1,3) for h,r in product((False,True),repeat=2)})
            self.assertEqual(condition(table,report=True,recorded=True),condition(table,report=True))

    def test_total_probability_and_impossible_observation(self):
        table=joint(Q(1,2),Q(3,4),Q(1,4),{k:Q(0) for k in product((False,True),repeat=2)})
        self.assertIsNone(condition(table,recorded=True))
        self.assertEqual(condition(table,recorded=False),Q(1,2))
        self.assertEqual(condition(table),Q(1,2))

    def test_contracts(self):
        rates={k:Q(1,2) for k in product((False,True),repeat=2)}
        for value in (True,0.5,float('nan'),'1/2'):
            with self.assertRaises(TypeError):joint(value,Q(3,4),Q(1,4),rates)
        for value in (-1,2):
            with self.assertRaises(ValueError):joint(value,Q(3,4),Q(1,4),rates)
        for bad in ({}, {(0,0):Q(1)}, {**rates,(True,True):Q(2)}):
            with self.assertRaises(ValueError):joint(Q(1,2),Q(3,4),Q(1,4),bad)
        with self.assertRaises(TypeError):condition(joint(Q(1,2),Q(3,4),Q(1,4),rates),recorded=1)

if __name__=='__main__':unittest.main()
