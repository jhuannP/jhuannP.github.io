import unittest
from fractions import Fraction as F
from .inventory import inventory,atp_equivalents

class BetaTests(unittest.TestCase):
    def test_c14_fixture(self):
        v=inventory(14)
        self.assertEqual((v['cycles'],v['acetyl'],v['beta_nadh'],v['beta_etf_pairs']),(6,7,6,6))
        self.assertEqual((v['total_nadh'],v['total_q_pairs'],v['gtp']),(27,13,7))
        self.assertEqual(atp_equivalents(14),dict(gross=F(94),activation=2,net=F(92)))
        self.assertEqual(atp_equivalents(14,free_acid=False)['net'],94)

    def test_stepwise_carbon_and_closed_form(self):
        for n in range(4,41,2):
            v=inventory(n)
            self.assertEqual(v['cycles'],n//2-1);self.assertEqual(v['acetyl'],n//2)
            self.assertEqual(v['trace'][-1]['released'],2)
            self.assertEqual(v['trace'][-1]['remaining'],0)
            for row in v['trace']:
                self.assertEqual(2*row['acetyl']+row['remaining'],n)
            self.assertEqual(atp_equivalents(n)['net'],7*n-6)
        v=inventory(14)['trace'][2]
        self.assertEqual((v['remaining'],v['acetyl']),(8,3))

    def test_yield_assumptions_are_parameters(self):
        for n in (4,12,14,18):
            low=atp_equivalents(n,F(2),F(1))['net']
            standard=atp_equivalents(n)['net']
            self.assertLess(low,standard)
            self.assertEqual(atp_equivalents(n,free_acid=False)['net']-standard,2)
        self.assertEqual(atp_equivalents(14,F(0),F(0))['net'],5)

    def test_contracts(self):
        for n in (True,2,3,5,42,-4,14.,'14'):
            with self.assertRaises(ValueError):inventory(n)
        for x in (2.5,F(-1),True):
            with self.assertRaises(ValueError):atp_equivalents(14,p_nadh=x)
        with self.assertRaises(ValueError):atp_equivalents(14,free_acid=1)

if __name__=='__main__':unittest.main()
