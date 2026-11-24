import unittest
from fractions import Fraction as Q
try:
    from .experiment import given,detector
except ImportError:
    from experiment import given,detector

class ProbabilityTests(unittest.TestCase):
    def test_dice_conditioning_and_asymmetry(self):
        self.assertEqual(given(Q(1,3),Q(1,2)),Q(2,3))
        self.assertEqual(given(Q(1,6),Q(1,3)),Q(1,2))
        self.assertEqual(given(Q(1,6),Q(1,2)),Q(1,3))
        self.assertIsNone(given(0,0))

    def test_detector_counts_reference(self):
        r=detector(Q(1,10),Q(4,5),Q(1,5));table=r['expected_table_1000']
        self.assertEqual(table,[[80,20],[180,720]])
        self.assertEqual(r['defect_given_positive'],Q(80,260))
        self.assertEqual(r['defect_given_negative'],Q(20,740))
        self.assertEqual(sum(sum(row) for row in table),1000)

    def test_all_grid_probabilities_and_normalization(self):
        grid=[Q(i,4) for i in range(5)]
        for p in grid:
            for s in grid:
                for f in grid:
                    r=detector(p,s,f);self.assertEqual(r['positive']+r['negative'],1)
                    table=r['expected_table_1000']
                    self.assertEqual(sum(table[0]),1000*p)
                    self.assertEqual(sum(table[1]),1000*(1-p))
                    self.assertEqual(table[0][0]+table[1][0],1000*r['positive'])
                    self.assertEqual(table[0][1]+table[1][1],1000*r['negative'])
                    for key in ['defect_given_positive','defect_given_negative']:
                        if r[key] is not None:self.assertTrue(0<=r[key]<=1)
                    if s==f and r['positive']>0:self.assertEqual(r['defect_given_positive'],p)
        self.assertIsNone(detector(1,0,1)['defect_given_positive'])
        self.assertEqual(detector(Q(1,10),1,0)['defect_given_positive'],1)

    def test_contracts(self):
        for bad in [True,Q(-1,2),Q(3,2),.5,'1/2']:
            with self.assertRaises(ValueError):detector(bad,1,0)
        with self.assertRaises(ValueError):given(Q(3,4),Q(1,2))

if __name__=='__main__':unittest.main()
