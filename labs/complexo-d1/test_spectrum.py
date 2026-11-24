import unittest
from fractions import Fraction as Q
from itertools import product
from .spectrum import d1,parity,pair_sum,borrowed_strength,H,C

class Tests(unittest.TestCase):
    def test_energies_and_units(self):
        for gap in (1000,8000,16000,24000,50000):
            r=d1(gap)
            self.assertEqual(3*r['lower_cm']+2*r['upper_cm'],0)
            self.assertEqual(r['upper_cm']-r['lower_cm'],gap)
            wavelength_m=r['wavelength_nm']/10**9
            self.assertEqual(wavelength_m*r['frequency_hz'],C)
            self.assertEqual(r['photon_j'],H*C/wavelength_m)
        self.assertEqual(d1(16000)['wavelength_nm'],625)
        self.assertEqual(d1(24000)['wavelength_nm'],Q(1250,3))
    def test_parity_independent_pairs(self):
        # Valores de amplitudes em r e -r: formar explicitamente cada produto.
        for a,b,c in product((-1,1),repeat=3):
            explicit=sum((f*o*i+(c*f)*(b*o)*(a*i)
                          for f,o,i in ((2,3,5),(-1,2,3),(3,-4,1))),Q(0))
            self.assertEqual(pair_sum((30,-6,-12),a,b,c),explicit)
        self.assertEqual(pair_sum((2,4,8),1,-1,1),0)
        self.assertEqual(pair_sum((2,-2),1,-1,-1),0) # paridade permite, mas não garante
    def test_mixing_normalization(self):
        for k in range(-10,11):
            e=Q(k,10); s=borrowed_strength(e)
            self.assertEqual((1+e*e)*s,e*e)
            self.assertEqual(s,borrowed_strength(-e))
            self.assertTrue(0<=s<=Q(1,2))
        self.assertEqual(borrowed_strength(Q(1,5)),Q(1,26))
        self.assertEqual(borrowed_strength(Q(1,10)),Q(1,101))
        self.assertNotEqual(borrowed_strength(Q(1,10))/borrowed_strength(Q(1,5)),Q(1,4))
    def test_contracts(self):
        for bad in (True,16000.,0,999,50001,'16000'):
            with self.assertRaises(ValueError):d1(bad)
        for bad in (True,.2,Q(3,2),'x'):
            with self.assertRaises(ValueError):borrowed_strength(bad)
        for bad in (0,True,1.,Q(1)):
            with self.assertRaises(ValueError):parity(bad,-1,1)
        with self.assertRaises(ValueError):pair_sum((),1,-1,1)
