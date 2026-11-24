import unittest
from .experiment import audit,BEFORE,AFTER,LP_BEFORE,LP_AFTER,ATOMS,VALENCE

class SN2LewisTests(unittest.TestCase):
    def test_selected_structures_and_valence_inventory(self):
        a,b=audit(BEFORE,LP_BEFORE),audit(AFTER,LP_AFTER)
        self.assertEqual(a['formula'],{'C':1,'S':1,'Cl':1,'H':4})
        self.assertEqual(a['formula'],b['formula']) # identidade dos átomos preservada por construção
        for s in (a,b):
            self.assertEqual(s['electrons'],22);self.assertEqual(s['total_charge'],-1)
            self.assertEqual(s['electrons'],sum(VALENCE[x] for x in ATOMS.values())-s['total_charge'])
            self.assertTrue(s['closed_shell'])
        self.assertEqual((a['charge']['C'],a['charge']['S'],a['charge']['Cl']),(0,-1,0))
        self.assertEqual((b['charge']['C'],b['charge']['S'],b['charge']['Cl']),(0,0,-1))
    def test_conserved_total_does_not_make_five_single_bonds_valid(self):
        bonds=BEFORE+(('C','S'),);lp=dict(LP_BEFORE);lp['S']=2
        bad=audit(bonds,lp)
        self.assertEqual(bad['electrons'],22);self.assertEqual(bad['total_charge'],-1)
        self.assertEqual(bad['shells']['C'],10);self.assertFalse(bad['closed_shell'])
    def test_missing_leaving_pair_and_bond_order_independence(self):
        bad=dict(LP_AFTER);bad['Cl']=3
        a=audit(AFTER,bad);self.assertEqual(a['electrons'],20);self.assertFalse(a['closed_shell'])
        self.assertEqual(audit(tuple((b,a) for a,b in reversed(AFTER)),LP_AFTER),audit(AFTER,LP_AFTER))
    def test_contracts(self):
        for bonds in [(('C','C'),),(('C','X'),),BEFORE+(('Cl','C'),),(('C',),)]:
            with self.assertRaises(ValueError):audit(bonds,LP_BEFORE)
        for lp in ({},dict(LP_BEFORE,C=True),dict(LP_BEFORE,S=-1)):
            with self.assertRaises(ValueError):audit(BEFORE,lp)
