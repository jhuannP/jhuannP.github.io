import unittest
from copy import deepcopy
from .addition import paths,audit,key

class AdditionTests(unittest.TestCase):
    def test_both_paths_conserve_atoms_charge_electrons(self):
        for site in ['C1','C2']:
            states,_=paths(site)
            for state in states:
                out=audit(state)
                self.assertEqual(out['composition'],{'C':3,'H':7,'Cl':1})
                self.assertEqual(out['electrons'],26);self.assertEqual(out['charge'],0)
    def test_protonation_and_capture_edits(self):
        for site in ['C1','C2']:
            (a,b,c),cation=paths(site)
            self.assertEqual(b['bonds'][key('C1','C2')],1)
            self.assertNotIn(key('Ha','Cl'),b['bonds'])
            self.assertEqual(b['bonds'][key(site,'Ha')],1)
            self.assertEqual(c['bonds'][key(cation,'Cl')],1)
            self.assertEqual(b['pairs']['Cl'],4);self.assertEqual(c['pairs']['Cl'],3)
            self.assertEqual(len(b['bonds']),len(a['bonds']))
            self.assertEqual(len(c['bonds']),len(b['bonds'])+1)
    def test_local_charges_and_shells(self):
        for site in ['C1','C2']:
            (a,b,c),cation=paths(site);mid=audit(b);out=audit(c)
            self.assertEqual(mid['charges'][cation],1);self.assertEqual(mid['charges']['Cl'],-1)
            self.assertEqual(mid['shell'][cation],6)
            self.assertTrue(all(q==0 for q in out['charges'].values()))
            for atom,shell in out['shell'].items():self.assertEqual(shell,2 if c['atoms'][atom]=='H' else 8)
    def test_contracts_and_counterexample(self):
        with self.assertRaises(ValueError):paths('C3')
        original=paths()[0][0]
        for mutate in [lambda s:s['bonds'].__setitem__(key('C1','H1'),True),lambda s:s['pairs'].__setitem__('Cl',4),lambda s:s['atoms'].__setitem__('X','C')]:
            broken=deepcopy(original);mutate(broken)
            with self.assertRaises(ValueError):audit(broken)
        # Conservation alone does not identify the final C–Cl connectivity.
        product1=paths('C1')[0][2];product2=paths('C2')[0][2]
        self.assertNotEqual(product1['bonds'],product2['bonds'])
        self.assertEqual(audit(product1)['electrons'],audit(product2)['electrons'])
if __name__=='__main__':unittest.main()
