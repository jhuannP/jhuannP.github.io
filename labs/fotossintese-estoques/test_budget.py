import unittest
from fractions import Fraction as F
from .budget import budget

class BudgetTests(unittest.TestCase):
    def test_example_and_ties(self):
        r = budget(9,18,18)
        self.assertEqual(r['triose_mol'],2)
        self.assertEqual(r['used_mol'],(6,12,18))
        self.assertEqual(r['left_mol'],(3,6,0))
        self.assertEqual(r['limiting'],('ATP',))
        self.assertEqual(budget(3,6,9)['limiting'],('CO2','NADPH','ATP'))
        self.assertEqual(budget(1,2,3)['triose_mol'],F(1,3))

    def test_independent_feasibility_grid(self):
        # Independent candidate search in units of 1/18 mol, exact on this grid.
        for c in range(7):
            for n in range(7):
                for a in range(7):
                    feasible = [F(k,18) for k in range(37)
                                if F(k,6)<=c and F(k,3)<=n and F(k,2)<=a]
                    r = budget(c,n,a)
                    self.assertEqual(r['triose_mol'],max(feasible))
                    self.assertTrue(all(x>=0 for x in r['left_mol']))
                    self.assertEqual(tuple(u+l for u,l in zip(r['used_mol'],r['left_mol'])),(c,n,a))
                    self.assertEqual(r['fixed_carbon_mol']+r['left_mol'][0],c)
                    self.assertTrue(any(x==0 for x in r['left_mol']))

    def test_scaling_and_added_nonlimiting_stock(self):
        base = budget(9,18,18)
        for s in (F(1,7),F(3,2),F(4)):
            r = budget(9*s,18*s,18*s)
            self.assertEqual(r['triose_mol'],base['triose_mol']*s)
            self.assertEqual(r['left_mol'],tuple(x*s for x in base['left_mol']))
        self.assertEqual(budget(90,180,18)['triose_mol'],2)
        self.assertEqual(budget(9,18,27)['triose_mol'],3)
        self.assertEqual(budget(0,18,18)['triose_mol'],0)

    def test_contract(self):
        for bad in (True,1.0,'3',None):
            with self.assertRaises(TypeError): budget(bad,6,9)
        for bad in (-1,10**6+1):
            with self.assertRaises(ValueError): budget(3,bad,9)
