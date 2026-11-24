import itertools
import unittest
from fractions import Fraction as Q
from .experiment import interface

class DielectricTests(unittest.TestCase):
    def test_exact_boundary_identities(self):
        for k1,k2,n,t,sigma in itertools.product((1,2,4),(1,2,4),(-2,0,1),(-1,0,2),(-1,0,2)):
            q=interface(k1,k2,n,t,sigma)
            self.assertEqual(q['D2n']-q['D1n'],sigma)
            self.assertEqual(q['E2t'],q['E1t'])
            # Gauss de E conta carga total, não apenas a livre.
            self.assertEqual(q['E2n']-q['E1n'],q['sigma_total'])
            self.assertEqual(q['sigma_bound'],q['P1n']-q['P2n'])

    def test_normal_reversal_and_medium_swap(self):
        for k1,k2,sigma in itertools.product((1,2,4),(1,2,4),(-1,0,2)):
            q=interface(k1,k2,1,2,sigma)
            reverse=interface(k2,k1,-q['E2n'],2,sigma)
            self.assertEqual(reverse['E2n'],-q['E1n'])
            self.assertEqual(reverse['sigma_bound'],q['sigma_bound'])
            self.assertEqual(reverse['sigma_total'],q['sigma_total'])

    def test_vacuum_equal_media_and_distinct_components(self):
        q=interface(1,1,2,1,3)
        self.assertEqual(q['sigma_bound'],0);self.assertEqual(q['E2n'],5)
        q=interface(2,4,1,1,0)
        self.assertEqual(q['E2n'],Q(1,2));self.assertEqual(q['sigma_bound'],Q(-1,2))
        self.assertNotEqual(q['E2n'],q['E1n']);self.assertEqual(q['D1n'],q['D2n'])
        for k in (1,2,4):
            q=interface(k,k,2,1,0);self.assertEqual(q['E1n'],q['E2n']);self.assertEqual(q['sigma_bound'],0)

    def test_contracts(self):
        for k in (0,-1,True,'2',float('nan')):
            with self.assertRaises(ValueError):interface(k,2,1,1,0)
        with self.assertRaises(ValueError):interface(1,1,1.5,0,0)
