import itertools
import unittest
from .experiment import model,audit,enumerate_octets


class ResonanceTests(unittest.TestCase):
    def test_independent_enumeration(self):
        # Enumerate all order-1/2 assignments and 0..3 lone pairs on the two terminals.
        # Constraints written directly from CH3-C-X-Y, not by selecting model presets.
        for family in (0,1):
            candidates=[]
            valence_last=6 if family==0 else 5
            h_last=0 if family==0 else 2
            required_charge=-1 if family==0 else 0
            for o1,o2,l1,l2 in itertools.product((1,2),(1,2),range(4),range(4)):
                if 2*(1+o1+o2)!=8 or 2*(o1+l1)!=8 or 2*(h_last+o2+l2)!=8:continue
                fc=[4-(1+o1+o2),6-2*l1-o1,valence_last-2*l2-h_last-o2]
                e=2*(1+o1+o2+3+h_last+l1+l2)
                if sum(fc)==required_charge and e==24:candidates.append((o1,o2,l1,l2))
            expected={(2,1,2,3),(1,2,3,2)} if family==0 else {(2,1,2,1),(1,2,3,0)}
            self.assertEqual(set(candidates),expected)
            self.assertEqual(set(enumerate_octets(family)),expected)
            actual={(model(family,f)['bonds'][1][2],model(family,f)['bonds'][2][2],*model(family,f)['pairs'][2:]) for f in (0,1)}
            self.assertEqual(actual,expected)

    def test_explicit_charges_and_inventory(self):
        expected={(0,0):[0,0,0,-1],(0,1):[0,0,-1,0],(0,2):[0,-1,0,0],
                  (1,0):[0,0,0,0],(1,1):[0,0,-1,1],(1,2):[0,-1,0,1]}
        for (family,form),formal in expected.items():
            s=model(family,form)
            self.assertEqual(s['formal'],formal)
            self.assertEqual(s['electrons'],24);self.assertEqual(s['target'],24)
            self.assertTrue(s['electron_ok']);self.assertTrue(s['charge_ok'])
            self.assertEqual(s['local'],[8,10 if form==2 else 8,8,8])
            self.assertEqual(s['octet_ok'],form!=2)

    def test_connectivity_and_two_arrows(self):
        for family in (0,1):
            a,b,bad=[model(family,f) for f in (0,1,2)]
            self.assertEqual(a['atoms'],b['atoms']);self.assertEqual(a['hydrogens'],b['hydrogens'])
            self.assertEqual([v[:2] for v in a['bonds']],[v[:2] for v in b['bonds']])
            # Pair on terminal 4 becomes a pi pair; old pi pair becomes lone pair on O3.
            self.assertEqual(b['pairs'][3],a['pairs'][3]-1)
            self.assertEqual(b['pairs'][2],a['pairs'][2]+1)
            self.assertEqual([v[2] for v in b['bonds']],[1,1,2])
            self.assertTrue(bad['electron_ok']) # Conserving electrons is not sufficient.
            self.assertFalse(bad['octet_ok'])
        # Renaming equivalent acetate oxygens maps one contributor onto the other.
        a,b=model(0,0),model(0,1)
        self.assertEqual(a['formal'][2:],list(reversed(b['formal'][2:])))
        # Amide endpoints are different elements, so the same permutation is not a symmetry.
        self.assertNotEqual(model(1,0)['atoms'][2],model(1,0)['atoms'][3])

    def test_errors_and_bookkeeping_identity(self):
        for family,form in ((2,0),(0,3),(-1,0),(0,-1)):
            with self.assertRaises(ValueError):model(family,form)
        for atoms,H,bonds,lp,q in ((['S'],[0],[],[0],0),(['O'],[-1],[],[0],0),(['C','O'],[0,0],[[0,1,1],[1,0,1]],[0,0],0)):
            with self.assertRaises(ValueError):audit(atoms,H,bonds,lp,q)
        for H,L,B in itertools.product(range(3),range(4),(1,2,3)):
            s=audit(['C','N'],[H,1],[[0,1,B]],[L,1],0)
            # Sum formal charges = neutral valence count minus actual electron count.
            self.assertEqual(s['total_charge'],4+5+H+1-s['electrons'])
        # Missing a pair changes the inventory even if geometry is untouched.
        a=model(0,0); s=audit(a['atoms'],a['hydrogens'],a['bonds'],[0,0,2,2],-1)
        self.assertFalse(s['electron_ok']);self.assertFalse(s['charge_ok'])
