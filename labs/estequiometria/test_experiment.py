import unittest
from fractions import Fraction as Q
from .experiment import reaction,balanced

class StoichiometryTests(unittest.TestCase):
    def test_atoms_nonnegative_and_maximum_extent(self):
        for h in range(21):
            for o in range(21):
                q=reaction(Q(h,2),Q(o,2));f=q['final']
                self.assertEqual(q['H_atoms_initial'],q['H_atoms_final'])
                self.assertEqual(q['O_atoms_initial'],q['O_atoms_final'])
                self.assertTrue(all(v>=0 for v in f.values()))
                self.assertTrue(f['H2']==0 or f['O2']==0)
                # Qualquer avanço positivo adicional violaria não negatividade.
                extra=Q(1,100)
                self.assertTrue(f['H2']-2*extra<0 or f['O2']-extra<0)
                # Massas molares aproximadas 2,32,18 são consistentes com a contagem.
                self.assertEqual(2*q['initial']['H2']+32*q['initial']['O2'],2*f['H2']+32*f['O2']+18*f['H2O'])

    def test_limiting_tie_zero_and_scaling(self):
        self.assertEqual(reaction(3,2)['final'],{'H2':0,'O2':Q(1,2),'H2O':3})
        self.assertEqual(reaction(4,2)['exhausted'],['H2','O2'])
        self.assertEqual(reaction(0,2)['extent'],0)
        for scale in (Q(1,2),2,5):
            a=reaction(3,2);b=reaction(3*scale,2*scale)
            for name in a['final']:self.assertEqual(b['final'][name],scale*a['final'][name])

    def test_balance_counts_not_subscripts(self):
        for scale in range(1,10):self.assertTrue(balanced(2*scale,scale,2*scale))
        for coefficients in ((1,1,1),(2,1,1),(1,2,1),(2,2,2)):self.assertFalse(balanced(*coefficients))

    def test_contract(self):
        for value in (-1,True,'1',1.5,float('nan')):
            with self.assertRaises(ValueError):reaction(value,2)
        for coefficients in ((0,1,1),(2,True,2),(2,1,Q(1,2))):
            with self.assertRaises(ValueError):balanced(*coefficients)
