import unittest
from fractions import Fraction as Q
from itertools import product
from .experiment import sequence

class ExponentialStagesTests(unittest.TestCase):
    def test_independent_repeated_updates_and_telescoping(self):
        for initial,factor,n in product((Q(0),Q(3),Q(80)),(Q(1,2),Q(3,4),Q(1),Q(3,2),Q(2)),(0,1,3,8)):
            rows=sequence(initial,factor,n)
            current=initial
            for i,row in enumerate(rows):
                self.assertEqual(row["value"],current)
                if i:
                    self.assertEqual(row["delta"],(factor-1)*rows[i-1]["value"])
                current*=factor
            self.assertEqual(sum((r["delta"] for r in rows[1:]),Q(0)),rows[-1]["value"]-initial)

    def test_composition_and_change_of_interval(self):
        for factor in (Q(1,2),Q(1),Q(3,2)):
            direct=sequence(80,factor,12)
            grouped=sequence(80,factor**3,4)
            for j,row in enumerate(grouped):self.assertEqual(row["value"],direct[3*j]["value"])
            restart=sequence(direct[5]["value"],factor,7)
            self.assertEqual(restart[-1]["value"],direct[-1]["value"])
            scaled=sequence(80*1000,factor,12)
            self.assertEqual(scaled[-1]["value"],1000*direct[-1]["value"])

    def test_examples_and_constant_case(self):
        self.assertEqual([r["value"] for r in sequence(80,Q(3,2),3)],[80,120,180,270])
        self.assertEqual([r["delta"] for r in sequence(80,Q(3,2),3)],[None,40,60,90])
        self.assertEqual([r["value"] for r in sequence(80,Q(1,2),3)],[80,40,20,10])
        self.assertEqual([r["value"] for r in sequence(12,1,3)],[12]*4)
        # A 50% increase followed by a 50% reduction is not the same factor repeated.
        self.assertEqual(Q(80)*Q(3,2)*Q(1,2),60)

    def test_contracts(self):
        for args in ((-1,2,3),(1,0,3),(1,-1,3),(True,2,3),(1,.5,3),
                     (1,2,-1),(1,2,2.5),(1,2,True),(1,2,257)):
            with self.assertRaises(ValueError):sequence(*args)
