import unittest
from fractions import Fraction as F
from itertools import product
from .repeated import evidence, pair_table

class RepeatedEvidence(unittest.TestCase):
    def test_original_examples(self):
        for jh, jn, expected in [(F(16,25),F(1,25),F(16,25)),
                                 (F(4,5),F(1,5),F(4,13)),
                                 (F(3,5),F(0),F(1))]:
            r=evidence(F(1,10),F(4,5),F(1,5),jh,jn)
            self.assertEqual(r['after_first'],F(4,13))
            self.assertEqual(r['after_both'],expected)

    def test_integer_atom_enumeration(self):
        # Independent construction: choose subsets with prescribed cardinalities
        # among four equiprobable atoms in each group, then enumerate 16 atoms.
        for p,t,u,j,k in product(range(5),repeat=5):
            if not max(0,2*t-4)<=j<=t or not max(0,2*u-4)<=k<=u: continue
            states=[]
            for truth,weight,rate,joint in [(1,p,t,j),(0,4-p,u,k)]:
                a=set(range(rate)); b=set(range(joint))|set(range(rate,2*rate-joint))
                self.assertEqual(len(b),rate)
                for _ in range(weight):
                    states.extend((truth,int(i in a),int(i in b)) for i in range(4))
            r=evidence(F(p,4),F(t,4),F(u,4),F(j,4),F(k,4))
            for attr,selected in [('first', [s for s in states if s[1]]),
                                  ('both', [s for s in states if s[1] and s[2]])]:
                self.assertEqual(r[attr+'_mass'], F(len(selected),16))
                expected=F(sum(s[0] for s in selected),len(selected)) if selected else None
                self.assertEqual(r['after_'+attr],expected)
            self.assertEqual(sum(r['atoms'].values()),1)

    def test_copy_is_not_new_information(self):
        for p,t,u in product(range(5),repeat=3):
            r=evidence(F(p,4),F(t,4),F(u,4),F(t,4),F(u,4))
            self.assertEqual(r['after_first'],r['after_both'])

    def test_invalid_and_zero_mass(self):
        for args in [(F(1,5),F(2,5)), (F(4,5),F(1,5)), (True,0), (.5,0),(-1,0)]:
            with self.assertRaises(ValueError): pair_table(*args)
        r=evidence(0,1,0,1,0)
        self.assertIsNone(r['after_first']);self.assertIsNone(r['after_both'])
