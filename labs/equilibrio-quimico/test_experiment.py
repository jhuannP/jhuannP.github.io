import itertools
import unittest
from fractions import Fraction as Q
from .experiment import equilibrium

class EquilibriumTests(unittest.TestCase):
    def test_mass_balance_quotient_and_feasible_extent(self):
        for a,b,K in itertools.product(range(5),range(5),(Q(1,4),Q(1),Q(4))):
            if a+b==0:continue
            q=equilibrium(a,b,K)
            self.assertEqual(q['A']+q['B'],a+b)
            self.assertGreater(q['A'],0);self.assertGreater(q['B'],0)
            self.assertEqual(q['B']/q['A'],K)
            self.assertEqual(q['A'],a-q['extent']);self.assertEqual(q['B'],b+q['extent'])
            self.assertGreater(q['extent'],-b);self.assertLess(q['extent'],a)

    def test_reverse_reaction_and_scale(self):
        for a,b in ((3,1),(0,4),(4,0),(2,2)):
            for K in (Q(1,4),Q(1),Q(4)):
                q=equilibrium(a,b,K);reverse=equilibrium(b,a,1/K)
                self.assertEqual(q['A'],reverse['B']);self.assertEqual(q['B'],reverse['A'])
                self.assertEqual(q['extent'],-reverse['extent'])
                for factor in (Q(1,2),3):
                    scaled=equilibrium(a*factor,b*factor,K)
                    self.assertEqual(scaled['A'],factor*q['A']);self.assertEqual(scaled['fraction_B'],q['fraction_B'])

    def test_direction_limits_and_equal_rates_not_equal_amounts(self):
        self.assertEqual(equilibrium(3,1,1)['direction'],'direta')
        self.assertEqual(equilibrium(0,4,1)['direction'],'inversa')
        self.assertIsNone(equilibrium(0,4,1)['Qinitial'])
        self.assertEqual(equilibrium(1,0,1)['Qinitial'],0)
        self.assertEqual(equilibrium(2,2,1)['direction'],'já em equilíbrio')
        self.assertEqual(equilibrium(1,0,4)['fraction_B'],Q(4,5))

    def test_contract(self):
        for args in ((0,0,1),(-1,2,1),(1,1,0),(1,1,-1),(True,1,1),(1.,1,1)):
            with self.assertRaises(ValueError):equilibrium(*args)
