import unittest
from fractions import Fraction
from .experiment import grow,summary,INITIAL

class ClonalSelectionTests(unittest.TestCase):
    def test_exact_counts_and_fractions(self):
        q=summary(0,3,1)
        self.assertEqual(q['final'],[80,10,80,10,10]);self.assertEqual(q['total'],190);self.assertEqual(q['added'],140)
        self.assertEqual(Fraction(sum(n for n,r in zip(q['final'],q['recognized']) if r),q['total']),Fraction(16,19))
        self.assertAlmostEqual(q['selected_fraction'],16/19)
        self.assertEqual(summary(1,3,1)['final'],[10,80,10,10,10])
        for t in range(3):
            for g in range(7):
                for signal in (0,1):
                    q=summary(t,g,signal);self.assertTrue(all(n>=10 for n in q['final']))
                    self.assertEqual(q['total'],sum(q['final']));self.assertTrue(0<=q['selected_fraction']<=1)

    def test_recognition_does_not_require_activation(self):
        for t in range(3):
            a,b=summary(t,6,0),summary(t,6,1)
            self.assertEqual(a['recognized'],b['recognized']);self.assertEqual(a['final'],list(INITIAL))
            self.assertFalse(any(a['active']));self.assertTrue(any(b['active']))
            self.assertEqual(summary(t,0,1)['final'],list(INITIAL))
            for i,r in enumerate(b['recognized']):
                if not r:self.assertEqual(b['final'][i],INITIAL[i])

    def test_semigroup_scaling_and_no_new_lineage(self):
        for t in range(3):
            base=[0,2,3,5,7];saved=base[:]
            twice=grow(grow(base,t,2,1),t,3,1)
            self.assertEqual(twice,grow(base,t,5,1));self.assertEqual(base,saved)
            self.assertEqual(grow(base,t,5,1)[0],0)
            self.assertEqual(grow([3*n for n in base],t,4,1),[3*n for n in grow(base,t,4,1)])

    def test_domains(self):
        for initial,t,g,s in [([10]*4,0,1,1),([0]*5,0,1,1),([-1,2,3,4,5],0,1,1),([10]*5,3,1,1),([10]*5,0,-1,1),([10]*5,0,1.5,1),([10]*5,0,1,2)]:
            with self.assertRaises(ValueError):grow(initial,t,g,s)

if __name__=='__main__':unittest.main()
