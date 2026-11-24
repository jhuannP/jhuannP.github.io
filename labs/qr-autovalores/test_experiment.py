import importlib.util
import itertools
import math
import unittest
from fractions import Fraction as F
from pathlib import Path
spec=importlib.util.spec_from_file_location('qrlesson',Path(__file__).with_name('experiment.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class QRTests(unittest.TestCase):
    def test_qr_on_integer_and_singular_matrices(self):
        ident=[[1.,0.],[0.,1.]]
        for values in itertools.product([-2,0,1],repeat=4):
            a=[list(values[:2]),list(values[2:])];q,r=m.qr2(a)
            self.assertLess(m.norm(m.diff(m.mm(q,r),a)),2e-15)
            self.assertLess(m.norm(m.diff(m.mm(m.trans(q),q),ident)),1e-15)
            self.assertEqual(r[1][0],0)

    def test_exact_symmetric_formula(self):
        # Coluna da iteração ortogonal proporcional a A^k e1;
        # expressão racional independente da fatoração numérica.
        for k in range(21):
            r=m.experiment(0,k);p=9**k
            expected=[[float(F(3*p+1,p+1)),float(F(2*3**k,p+1))],
                      [float(F(2*3**k,p+1)),float(F(p+3,p+1))]]
            self.assertLess(m.norm(m.diff(r['a'],expected)),2e-14)

    def test_invariants_and_nonconvergent_cases(self):
        expected=[(4,3),(0,-1),(0,1),(3,2)]
        for case,k in itertools.product(range(4),range(21)):
            r=m.experiment(case,k);trace,det=expected[case]
            self.assertAlmostEqual(r['trace'],trace,delta=2e-14)
            self.assertAlmostEqual(r['determinant'],det,delta=2e-14)
            self.assertLess(r['similarity'],3e-15)
            self.assertLess(r['orthogonality'],3e-15)
            self.assertLess(r['qr_error'],2e-15)
            self.assertAlmostEqual(m.norm(r['a']),m.norm(r['original']),delta=2e-14)
            if case==1:
                self.assertEqual(r['a'],[[0.,(-1.)**k],[(-1.)**k,0.]])
            if case==2:self.assertEqual(r['a'],m.CASES[2])
            if case==3:
                self.assertEqual(r['lower'],0)
                self.assertGreater(r['vector_residual'],.9)

    def test_domain_and_zero_first_column(self):
        a=[[0.,2.],[0.,3.]];q,r=m.qr2(a)
        self.assertEqual(q,[[1.,0.],[0.,1.]])
        self.assertEqual(r,a)
        for a in [[],[[1]],[[1,2],[3,float('nan')]]]:
            with self.assertRaises(ValueError):m.qr2(a)
        with self.assertRaises(ValueError):m.experiment(4,2)
        with self.assertRaises(ValueError):m.experiment(0,21)

if __name__=='__main__':unittest.main()
