import unittest,itertools
from .experiment import trace,inspect

def words(limit):
    return [''.join(w) for n in range(limit+1) for w in itertools.product('01',repeat=n)]

class ParityDFATests(unittest.TestCase):
    def test_all_words_to_ten_and_every_prefix_invariant(self):
        cases=words(10);self.assertEqual(len(cases),2047)
        for w in cases:
            s=trace(w);self.assertEqual(s['accepted'],w.count('1')%2==0)
            for k,q in enumerate(s['states']):self.assertEqual(q,w[:k].count('1')%2)
            self.assertEqual(len(s['rows']),len(w))
    def test_concatenation_and_zero_invariance(self):
        for u in words(4):
            self.assertEqual(trace(u+'0')['accepted'],trace(u)['accepted'])
            self.assertNotEqual(trace(u+'1')['accepted'],trace(u)['accepted'])
            for v in words(4):
                self.assertEqual(trace(u+v)['states'][-1],(u.count('1')+v.count('1'))%2)
    def test_panel_prefix_and_final_acceptance(self):
        accepted=0
        for word in range(16):
            w=format(word,'04b');accepted+=trace(w)['accepted']
            for step in range(5):
                s=inspect(word,step);self.assertEqual(s['prefix']+s['suffix'],w)
                self.assertEqual(s['state'],w[:step].count('1')%2)
                self.assertEqual(s['accepted'],w.count('1')%2==0);self.assertEqual(s['complete'],step==4)
        self.assertEqual(accepted,8)
        self.assertEqual(inspect(11,3)['state'],0);self.assertFalse(inspect(11,3)['accepted'])
    def test_empty_witnesses_and_invalid_domain(self):
        self.assertEqual(trace('')['states'],[0]);self.assertTrue(trace('')['accepted']);self.assertFalse(trace('1')['accepted'])
        for w in ('2','10a','０1',None,12):
            with self.assertRaises(ValueError):trace(w)
        for args in ((16,0),(-1,0),(0,5),(0,-1),(True,0),(0,.5)):
            with self.assertRaises(ValueError):inspect(*args)
