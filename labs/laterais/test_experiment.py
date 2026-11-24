import unittest
from fractions import Fraction as Q
from itertools import product
from .experiment import piece,classify,hole_extension

class OneSidedTests(unittest.TestCase):
    def test_branch_approach_and_center(self):
        for left,right,value in product((-2,0,2),repeat=3):
            for h in (Q(1,10),Q(1,100),Q(1,1000)):
                self.assertEqual(piece(-h,left,right,value)-left,-h)
                self.assertEqual(piece(h,left,right,value)-right,-h)
            self.assertEqual(piece(0,left,right,value),value)

    def test_all_classifications(self):
        counts=dict(salto=0,continua=0,removivel=0)
        for left,right,value in product((-2,0,2),repeat=3):
            r=classify(left,right,value);counts[r['category']]+=1
            if left!=right:self.assertIsNone(r['bilateral'])
            else:self.assertEqual(r['bilateral'],left)
        self.assertEqual(counts,dict(salto=18,continua=3,removivel=6))

    def test_continuity_does_not_imply_derivative_and_extension(self):
        self.assertEqual(classify(0,0,0)['category'],'continua')
        for h in (Q(1,10),Q(1,100),Q(1,1000)):
            self.assertEqual((piece(-h,0,0,0)-piece(0,0,0,0))/(-h),1)
            self.assertEqual((piece(h,0,0,0)-piece(0,0,0,0))/h,-1)
            for value in (-3,4,9):
                self.assertEqual(hole_extension(2-h,value),4-h)
                self.assertEqual(hole_extension(2+h,value),4+h)
        self.assertEqual(hole_extension(2),4)

    def test_contracts(self):
        for bad in (True,.5,'1/2'):
            with self.assertRaises(ValueError):piece(bad)
            with self.assertRaises(ValueError):classify(bad)

if __name__=='__main__':unittest.main()
