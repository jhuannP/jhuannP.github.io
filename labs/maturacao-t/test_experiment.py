import unittest,itertools
from .experiment import phenotype, summarize

class MarkerPhenotypeTests(unittest.TestCase):
    def test_four_marker_combinations(self):
        self.assertEqual([phenotype(*x) for x in [(False,False),(True,True),(True,False),(False,True)]],
                         ['DN','DP','CD4 único','CD8 único'])
    def test_partition_and_reordering(self):
        combos=list(itertools.product((False,True),repeat=2))
        for n in range(5):
            for records in itertools.product(combos,repeat=n):
                s=summarize(records)
                self.assertEqual(sum(s.values()), n)
                self.assertEqual(s,summarize(reversed(records)))
                # Contagem por predicados, sem depender do classificador.
                self.assertEqual(s['DP'],sum(a and b for a,b in records))
                self.assertEqual(s['DN'],sum(not a and not b for a,b in records))
                self.assertEqual(s['CD4 único'],sum(a and not b for a,b in records))
                self.assertEqual(s['CD8 único'],sum(not a and b for a,b in records))
    def test_same_snapshot_does_not_encode_history(self):
        s=summarize([(True,True)]*4+[(True,False)]*2)
        self.assertEqual(s['DP'],4)
        self.assertEqual(set(s),{'DN','DP','CD4 único','CD8 único'})
        self.assertNotIn('survival_rate',s)
    def test_empty_and_invalid(self):
        self.assertTrue(all(v==0 for v in summarize([]).values()))
        for bad in [0,1,.2,'positivo',None]:
            with self.assertRaises(ValueError):phenotype(bad,False)
