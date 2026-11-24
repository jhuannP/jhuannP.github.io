import unittest
from itertools import combinations_with_replacement
from bisect import bisect_left
from .experiment import trace,lower_bound,busca_binaria,DATASETS

class BinaryLimits(unittest.TestCase):
    def test_enumerated_sorted_lists(self):
        for n in range(9):
            for a in combinations_with_replacement(range(-1,3),n):
                for target in range(-2,5):
                    expected=sum(x<target for x in a)
                    r=trace(a,target)
                    self.assertEqual(lower_bound(a,target),expected)
                    self.assertEqual(r['position'],bisect_left(a,target))
                    self.assertEqual(r['found'],a.index(target) if target in a else -1)
                    self.assertLessEqual(r['ordered_comparisons'],n.bit_length())
                    any_index=busca_binaria(a,target)
                    self.assertEqual(any_index>=0,target in a)
                    if any_index>=0:self.assertEqual(a[any_index],target)

    def test_trace_invariants_and_progress(self):
        for a in DATASETS:
            for target in range(17):
                r=trace(a,target);position=sum(x<target for x in a)
                for row in r['rows']:
                    lo,hi=row['low'],row['high']
                    self.assertTrue(0<=lo<=hi<=len(a))
                    self.assertTrue(all(x<target for x in a[:lo]))
                    self.assertTrue(all(x>=target for x in a[hi:]))
                    self.assertTrue(lo<=position<=hi)  # position is a boundary, not always an element
                    if row['mid'] is not None:
                        self.assertTrue(lo<=row['mid']<hi)
                        self.assertLess(row['next_high']-row['next_low'],hi-lo)
                        self.assertLessEqual(row['next_high']-row['next_low'],(hi-lo)//2)
                self.assertEqual(r['rows'][-1]['low'],r['rows'][-1]['high'])

    def test_worst_case_and_instrumentation(self):
        for n in range(129):
            a=list(range(n));cases=[trace(a,t) for t in range(-1,n+1)]
            self.assertEqual(max(x['ordered_comparisons'] for x in cases),n.bit_length())
            for r in cases:
                self.assertEqual(r['equality_comparisons'],int(r['position']<n))
                self.assertEqual(r['total_key_comparisons'],r['ordered_comparisons']+r['equality_comparisons'])
        self.assertEqual(busca_binaria(DATASETS[1],3),3)
        self.assertEqual(trace(DATASETS[1],3)['found'],1)
        self.assertEqual(trace([],3)['total_key_comparisons'],0)

    def test_contracts_and_original_example(self):
        self.assertEqual(busca_binaria(DATASETS[0],11),5)
        self.assertEqual(busca_binaria(DATASETS[0],2),-1)
        self.assertEqual(busca_binaria([],7),-1)
        self.assertEqual(lower_bound([9,1,3],9),3)  # intentional counterexample, order precondition false
        for a,t in [([2,1],1),([True],1),([1],True),([1.5],1),('abc',1),([1],'1')]:
            with self.assertRaises(ValueError):trace(a,t)
