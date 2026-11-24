import unittest
from fractions import Fraction as Q
from .nmr import chemical_shift,offset_hz,rectangle,integrate,fractions,counts


class NMRTests(unittest.TestCase):
    def test_scales_and_round_trip(self):
        self.assertEqual(chemical_shift(400000800,400000000),2)
        self.assertEqual(offset_hz(2,400),800);self.assertEqual(offset_hz(2,600),1200)
        for ref in (100,200,400,600,800):
            for shift in (Q(-5),Q(-1,2),Q(0),Q(1),Q(2),Q(3),Q(10)):
                sample=ref*10**6+offset_hz(shift,ref)
                self.assertEqual(chemical_shift(sample,ref*10**6),shift)

    def test_area_oracle_by_disjoint_bins(self):
        signal=[(3,Q(2,5),3),(1,Q(4,5),2)]
        # Independent midpoint sum on 0.1-ppm bins: all edges align.
        values=[]
        for i in range(40):
            x=Q(2*i+1,20)
            height=Q(15,2) if Q(14,5)<x<Q(16,5) else Q(5,2) if Q(3,5)<x<Q(7,5) else Q(0)
            values.append(height/Q(10))
        self.assertEqual(sum(values),5)
        self.assertEqual(integrate(signal,0,2),sum(values[:20]))
        self.assertEqual(integrate(signal,2,4),sum(values[20:]))
        self.assertEqual(integrate(signal,0,4),5)
        self.assertEqual(rectangle(3,Q(2,5),3)[2]/rectangle(1,Q(4,5),2)[2],3)

    def test_additivity_overlap_and_transformations(self):
        signal=[(3,Q(2,5),3),(1,Q(4,5),2)]
        for cut in [Q(i,10) for i in range(41)]:
            self.assertEqual(integrate(signal,0,cut)+integrate(signal,cut,4),5)
        self.assertEqual(integrate([(1,2,4),(1,2,6)],0,2),10)
        wider=[(c,2*w,a) for c,w,a in signal]
        self.assertEqual(integrate(wider,-2,6),5)
        self.assertEqual(integrate(list(reversed(signal)),0,4),5)
        shifted=[(c+10,w,a) for c,w,a in signal]
        self.assertEqual(integrate(shifted,10,14),5)
        self.assertEqual(integrate(signal,0,0),0)

    def test_relative_counts_and_no_rounding(self):
        self.assertEqual(fractions((3,2)),(Q(3,5),Q(2,5)))
        self.assertEqual(fractions((30,20)),fractions((3,2)))
        self.assertEqual(counts((3,2),5),(3,2));self.assertEqual(counts((3,2),10),(6,4))
        self.assertEqual(counts((3,2),6),(Q(18,5),Q(12,5)))
        self.assertEqual(fractions((0,2)),(0,1))

    def test_contracts(self):
        for args in [(0,1),(1,0),(True,1),(1.0,1)]:
            with self.assertRaises(ValueError):chemical_shift(*args)
        for args in [(1,0),(1,True)]:
            with self.assertRaises(ValueError):offset_hz(*args)
        for args in [(0,0,1),(0,1,-1),(0,True,1)]:
            with self.assertRaises(ValueError):rectangle(*args)
        with self.assertRaises(ValueError):integrate([(0,1,1)],2,1)
        with self.assertRaises(ValueError):integrate([(0,1)],0,1)
        for areas in [[],[0,0],[-1,2],[True,2]]:
            with self.assertRaises(ValueError):fractions(areas)
        with self.assertRaises(ValueError):counts((3,2),True)
