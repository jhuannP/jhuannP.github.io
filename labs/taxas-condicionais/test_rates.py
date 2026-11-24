import itertools
import unittest
from fractions import Fraction as Q
from .rates import audit, EXAMPLE_A, EXAMPLE_B

class Rates(unittest.TestCase):
    def test_original_example_and_individual_records(self):
        for cells, expected in ((EXAMPLE_A, Q(27,40)), (EXAMPLE_B,Q(29,40))):
            records = [(i, j<s) for i,(s,n) in enumerate(cells) for j in range(n)]
            out = audit(cells,(Q(1,2),Q(1,2)))
            self.assertEqual(out['raw'],Q(sum(ok for _,ok in records),len(records)))
            self.assertEqual(out['raw'],expected)
            for i in range(2):
                group=[ok for label,ok in records if label==i]
                self.assertEqual(out['rates'][i], Q(sum(group),len(group)))
        a,b=(audit(c,(Q(1,2),Q(1,2))) for c in (EXAMPLE_A,EXAMPLE_B))
        self.assertTrue(all(x>y for x,y in zip(a['rates'],b['rates'])))
        self.assertLess(a['raw'],b['raw'])
        self.assertEqual(a['standardized']-b['standardized'],Q(1,10))

    def test_total_against_record_count_and_permutation(self):
        cells=[(s,n) for n in range(1,7) for s in range(n+1)]
        for left,right in itertools.product(cells,repeat=2):
            out=audit((left,right),(Q(1,3),Q(2,3)))
            records=[j<s for s,n in (left,right) for j in range(n)]
            self.assertEqual(out['raw'],Q(sum(records),len(records)))
            rev=audit((right,left),(Q(2,3),Q(1,3)))
            self.assertEqual(out['standardized'],rev['standardized'])
            self.assertEqual(out['raw'],rev['raw'])
            self.assertLessEqual(min(out['rates']),out['raw'])
            self.assertLessEqual(out['raw'],max(out['rates']))

    def test_common_weights_preserve_order(self):
        rates=[Q(s,4) for s in range(5)]
        for a1,a2,b1,b2 in itertools.product(rates,repeat=4):
            if a1<b1 or a2<b2: continue
            for k in range(5):
                weights=(Q(k,4),1-Q(k,4))
                a=audit(((int(4*a1),4),(int(4*a2),4)),weights)
                b=audit(((int(4*b1),4),(int(4*b2),4)),weights)
                self.assertGreaterEqual(a['standardized'],b['standardized'])

    def test_scaling_one_stratum_changes_composition(self):
        a=audit(EXAMPLE_A,(Q(1,2),Q(1,2)))
        scaled=audit(((27,30),(18,30)),(Q(1,2),Q(1,2)))
        self.assertEqual(a['rates'],scaled['rates'])
        self.assertEqual(a['standardized'],scaled['standardized'])
        self.assertNotEqual(a['raw'],scaled['raw'])

    def test_contracts_and_extremes(self):
        for cells,weights,error in [([],[],ValueError), ([(0,0)],[1],ValueError),
                ([(2,1)],[1],ValueError), ([(True,1)],[1],TypeError),
                ([(0,1)],[],ValueError), ([(0,1)],[.5],TypeError),
                ([(0,1)],[True],TypeError), ([(0,1)],[-1],ValueError),
                ([(0,1)],[Q(1,2)],ValueError)]:
            with self.assertRaises(error): audit(cells,weights)
        self.assertEqual(audit(((0,2),(3,3)),(1,0))['standardized'],0)
        self.assertEqual(audit(((0,2),(3,3)),(0,1))['standardized'],1)
