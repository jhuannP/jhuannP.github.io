from fractions import Fraction as F
import unittest
from .experiment import inspect

class LeverRuleTests(unittest.TestCase):
    def test_by_counting_component_packets(self):
        # Each alpha packet: four A and one B; beta packet: one A and four B.
        for a in range(7):
            for b in range(7):
                if a+b==0:continue
                atoms=['A']*(4*a)+['B']*a+['A']*b+['B']*(4*b)
                z=100*F(atoms.count('B'),len(atoms))
                if z.denominator!=1:continue
                s=inspect(int(z),1)
                self.assertEqual(s['fa'],F(a,a+b));self.assertEqual(s['fb'],F(b,a+b))
                self.assertEqual(s['b_total'],F(atoms.count('B'),len(atoms)))

    def test_balance_scaling_and_bounds(self):
        for z in range(20,81):
            first=inspect(z,1)
            for n in range(1,6):
                s=inspect(z,n)
                self.assertEqual(s['fa']+s['fb'],1)
                self.assertEqual(s['n_alpha']+s['n_beta'],n)
                self.assertEqual(s['b_alpha']+s['b_beta'],s['b_total'])
                a_alpha=s['n_alpha']-s['b_alpha'];a_beta=s['n_beta']-s['b_beta']
                self.assertEqual(a_alpha+a_beta,n-s['b_total'])
                self.assertEqual(s['fa'],first['fa'])
                self.assertTrue(0<=s['fa']<=1)
        self.assertEqual(inspect(20)['fb'],0);self.assertFalse(inspect(20)['two_present'])
        self.assertEqual(inspect(80)['fa'],0);self.assertTrue(inspect(50)['two_present'])

    def test_outside_is_not_extrapolated(self):
        for z in list(range(20))+list(range(81,101)):
            s=inspect(z)
            self.assertFalse(s['inside'])
            for k in ['fa','fb','n_alpha','n_beta','b_alpha','b_beta']:self.assertIsNone(s[k])
            self.assertEqual(s['b_total'],F(z,100))

    def test_contracts(self):
        for z in [True,False,None,.5,-1,101,'50']:
            with self.assertRaises(ValueError):inspect(z)
        for n in [True,0,6,1.0,None]:
            with self.assertRaises(ValueError):inspect(50,n)
