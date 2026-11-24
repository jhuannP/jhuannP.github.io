import unittest
from fractions import Fraction as Q
from itertools import permutations
from .annotations import report,EXAMPLES

class AnnotationTests(unittest.TestCase):
    def test_examples_and_order(self):
        p=report(*EXAMPLES['P']);q=report(*EXAMPLES['Q']);r=report(*EXAMPLES['R'])
        self.assertEqual(p['fraction'],Q(2,3));self.assertEqual(q['fraction'],Q(8,11))
        self.assertEqual(p['covered'],120);self.assertEqual(q['covered'],160)
        self.assertEqual(p['fraction'],r['fraction']);self.assertNotEqual(p['ordered_labels'],r['ordered_labels'])
        self.assertEqual(q['ordered_labels'],['A','B','B'])
        for order in permutations(EXAMPLES['Q'][1]):self.assertEqual(report(220,order),q)
    def test_union_against_position_sets(self):
        # All pairs of intervals in an eight-residue chain,including nesting/touching.
        intervals=[(a,b) for a in range(1,9) for b in range(a,9)]
        for a,b in intervals:
            for c,d in intervals:
                out=report(8,[('A',a,b),('B',c,d)])
                expected=set(range(a,b+1))|set(range(c,d+1))
                self.assertEqual(out['covered'],len(expected))
                self.assertEqual(out['ordered_labels'] is None,bool(set(range(a,b+1))&set(range(c,d+1))))
        self.assertEqual(report(120,[('A',20,80),('B',60,100)])['covered'],81)
    def test_empty_and_duplicate_annotations(self):
        self.assertEqual(report(10,[])['fraction'],0)
        out=report(10,[('A',1,10),('A',1,10)])
        self.assertEqual(out['covered'],10);self.assertIsNone(out['ordered_labels'])
        self.assertEqual(out['annotation_counts'],{'A':2}) # Hits,not two proven biological copies.
    def test_contracts(self):
        for length,hits in [(True,[]),(0,[]),(10001,[]),(10,[('A',0,3)]),(10,[('A',3,2)]),(10,[('A',1,11)]),(10,[('A',True,3)]),(10,[('',1,3)]),(10,[('A',1.,3)])]:
            with self.assertRaises(ValueError):report(length,hits)
if __name__=='__main__':unittest.main()
