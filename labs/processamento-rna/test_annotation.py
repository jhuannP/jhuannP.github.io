import unittest
from .annotation import PRECURSOR,ISOFORM_A,ISOFORM_B,splice

class AnnotationTests(unittest.TestCase):
    def test_two_supplied_isoforms(self):
        self.assertEqual(len(PRECURSOR),17)
        a,pa=splice(PRECURSOR,ISOFORM_A)
        b,pb=splice(PRECURSOR,ISOFORM_B)
        self.assertEqual(a,'AUGGAAUAG')
        self.assertEqual(b,'AUGUAG')
        self.assertEqual(pa,(0,1,2,7,8,9,14,15,16))
        self.assertEqual(pb,(0,1,2,14,15,16))
        self.assertEqual([i for i in range(1,len(pa)) if pa[i]!=pa[i-1]+1],[3,6])
        self.assertEqual([i for i in range(1,len(pb)) if pb[i]!=pb[i-1]+1],[3])

    def test_all_small_ordered_interval_pairs(self):
        rna='ACGUAC'
        spans=[(a,b) for a in range(len(rna)) for b in range(a+1,len(rna)+1)]
        for first in spans:
            for second in spans:
                if first[1]>second[0]:continue
                sequence,positions=splice(rna,(first,second))
                # Independent membership selection at each original position.
                selected=tuple(i for i in range(len(rna))
                               if any(a<=i<b for a,b in (first,second)))
                self.assertEqual(positions,selected)
                self.assertEqual(sequence,''.join(rna[i] for i in selected))
                self.assertEqual(len(sequence),sum(b-a for a,b in (first,second)))
                self.assertEqual(len(set(positions)),len(positions))

    def test_half_open_boundaries_and_no_added_tail(self):
        self.assertEqual(splice('ACGU',[(0,4)]),('ACGU',(0,1,2,3)))
        self.assertEqual(splice('ACGU',[(0,2),(2,4)]),('ACGU',(0,1,2,3)))
        self.assertEqual(splice('ACGU',[(2,3)]),('G',(2,)))
        self.assertNotIn('A',splice('CCGG',[(0,4)])[0])

    def test_inputs_preserved_and_representation_equivalent(self):
        intervals=[[0,3],[14,17]]
        before=[x.copy() for x in intervals]
        result=splice(PRECURSOR,intervals)
        self.assertEqual(intervals,before)
        self.assertEqual(result,splice(PRECURSOR,ISOFORM_B))
        self.assertEqual(PRECURSOR,'AUGGUAGGAAGUAGUAG')

    def test_contracts(self):
        for rna in ('','acgu','ACGT','ACGN','AC GU'):
            with self.assertRaises(ValueError):splice(rna,[(0,1)])
        for rna in (None,True,['A']):
            with self.assertRaises(TypeError):splice(rna,[(0,1)])
        for intervals in ([],[(0,0)],[(-1,2)],[(0,18)],[(7,10),(0,3)],[(0,3),(2,4)],[(0,3,4)]):
            with self.assertRaises(ValueError):splice(PRECURSOR,intervals)
        for intervals in ([(True,3)],[(0,3.)]):
            with self.assertRaises(TypeError):splice(PRECURSOR,intervals)
        with self.assertRaises(TypeError):splice(PRECURSOR,'0:3')

if __name__ == "__main__":unittest.main()
