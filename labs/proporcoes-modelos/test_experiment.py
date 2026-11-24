from fractions import Fraction as F
from itertools import combinations
import unittest
from .experiment import inspect

class ProportionModelsTests(unittest.TestCase):
    def test_invariants_and_doubling(self):
        for q in range(2,13):
            x=F(q,2);s=inspect(x)
            self.assertEqual(s['direta']['ratio'],4)
            self.assertEqual(s['inversa']['product'],24)
            self.assertEqual(s['direta']['doubling'],2)
            self.assertEqual(s['inversa']['doubling'],F(1,2))
            self.assertEqual(s['taxa_fixa']['doubled']-2*s['taxa_fixa']['y'],-6)
            self.assertNotEqual(s['taxa_fixa']['doubling'],2)

    def test_independent_item_counts(self):
        for x in range(1,7):
            s=inspect(x)
            self.assertEqual(s['direta']['y'],sum([4]*x))
            self.assertEqual(s['taxa_fixa']['y'],sum([6]+[4]*x))
            # Twenty-four unit tasks, each needs 1/x of a time unit with x ideal workers.
            self.assertEqual(s['inversa']['y'],sum([F(1,x)]*24))

    def test_pairs_distinguish_models(self):
        for a,b in combinations([F(q,2) for q in range(2,13)],2):
            sa=inspect(a);sb=inspect(b)
            self.assertEqual(sa['direta']['ratio'],sb['direta']['ratio'])
            self.assertEqual(sa['inversa']['product'],sb['inversa']['product'])
            self.assertNotEqual(sa['taxa_fixa']['ratio'],sb['taxa_fixa']['ratio'])
            slope=(sb['taxa_fixa']['y']-sa['taxa_fixa']['y'])/(b-a)
            self.assertEqual(slope,4) # Constant rate alone does not imply proportionality.

    def test_contracts(self):
        for x in [True,False,0,-1,7,F(4,3),float('inf'),float('nan'),None,'2']:
            with self.assertRaises(ValueError):inspect(x)
        self.assertEqual(inspect(1.5),inspect(F(3,2)))
