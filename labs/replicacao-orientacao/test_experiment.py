from itertools import product
import unittest
from .experiment import complement,reverse_complement,fork,replicate

class ReplicationOrientationTests(unittest.TestCase):
    def test_all_short_sequences_and_involution(self):
        pairs={'AT','TA','CG','GC'}
        for n in range(1,7):
            for bases in product('ACGT',repeat=n):
                s=''.join(bases);c=complement(s);rc=reverse_complement(s)
                self.assertEqual(len(c),n)
                self.assertTrue(all(a+b in pairs for a,b in zip(s,c)))
                self.assertTrue(all(a+b in pairs for a,b in zip(s,reversed(rc))))
                self.assertEqual(complement(c),s)
                self.assertEqual(reverse_complement(rc),s)

    def test_parental_identity_and_antiparallel_duplexes(self):
        for n in range(1,5):
            for bases in product('ACGT',repeat=n):
                s=''.join(bases);daughters=replicate(s)
                self.assertEqual(len(daughters),2)
                origins=[]
                for duplex in daughters:
                    self.assertEqual({x['origin'] for x in duplex},{'nova','parental'})
                    self.assertEqual([x['orientation'] for x in duplex],['5→3','3→5'])
                    self.assertTrue(all(a+b in {'AT','TA','CG','GC'} for a,b in zip(duplex[0]['bases'],duplex[1]['bases'])))
                    origins.extend(x['bases'] for x in duplex if x['origin']=='parental')
                self.assertCountEqual(origins,[s,complement(s)])

    def test_fork_by_template_polarity(self):
        # A leading polymerase travels opposite to the 5→3 orientation of its template.
        template_polarity={'superior':1,'inferior':-1}
        for d in [-1,1]:
            s=fork(d)
            self.assertEqual(template_polarity[s['leading']],-d)
            self.assertEqual(s['leading_growth'],d)
            self.assertEqual(s['lagging_growth'],-d)
        self.assertEqual(reverse_complement('ACGTAACC'),'GGTTACGT')
        self.assertNotEqual(complement('ACGTAACC'),reverse_complement('ACGTAACC'))

    def test_contracts(self):
        for seq in ['',None,'acgt','ACNT','A C',123,True]:
            for f in [complement,reverse_complement,replicate]:
                with self.assertRaises(ValueError):f(seq)
        for d in [True,False,0,2,1.0,None]:
            with self.assertRaises(ValueError):fork(d)
