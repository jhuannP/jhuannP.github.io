import unittest
from fractions import Fraction as Q
from .experiment import model

class HydrogenTests(unittest.TestCase):
    def test_inverse_wavelength_identity(self):
        # Recorrência espectral via número de onda, sem subtrair níveis no teste.
        for n in range(3,9):
            r=model(n)
            inverse=Q(17,1550)*(Q(1,4)-Q(1,n*n))
            self.assertEqual(1/r['wavelength'],inverse)
            self.assertEqual(r['atom_change']+r['photon'],0)
            self.assertEqual(r['photon']*r['wavelength'],1240)

    def test_sequence_and_limit(self):
        rs=[model(n) for n in range(3,9)]
        self.assertTrue(all(a['photon']<b['photon'] for a,b in zip(rs,rs[1:])))
        self.assertTrue(all(a['wavelength']>b['wavelength'] for a,b in zip(rs,rs[1:])))
        for r in rs:
            self.assertLess(r['photon'],Q(17,5))
            self.assertGreater(r['wavelength'],Q(6200,17))
        self.assertEqual(model(6)['photon'],Q(136,45))
        self.assertEqual(model(6)['wavelength'],Q(6975,17))

    def test_contract(self):
        for n in (True,False,2,9,3.,None,'6'):
            with self.assertRaises(ValueError):model(n)
