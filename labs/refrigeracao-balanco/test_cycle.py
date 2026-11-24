import unittest
from fractions import Fraction as Q
from itertools import product
from .cycle import proposal,rates

class CycleTests(unittest.TestCase):
    def test_fixture(self):
        r=proposal(280,320,840,140)
        self.assertEqual((r['qh'],r['cop_r'],r['cop_h']),(980,6,7))
        self.assertEqual((r['work_min'],r['sgen'],r['excess_work']),(120,Q(1,16),20))
        self.assertEqual((r['cop_r_bound'],r['cop_h_bound']),(7,8))
        self.assertTrue(r['compatible'])

    def test_independent_constructed_reservoir_ledgers_81(self):
        # Prescribe cold entropy extraction and entropy addition, then heat rejection.
        for tc,gap,qc,sigma in product((240,280,300),(20,40,80),(120,840,1000),(Q(0),Q(1,100),Q(1,10))):
            th=tc+gap
            qh=(Q(qc,tc)+sigma)*th
            work=qh-qc
            r=proposal(tc,th,qc,work)
            self.assertEqual(r['qh'],qh);self.assertEqual(r['sgen'],sigma)
            self.assertEqual(r['qh']-r['qc']-r['work'],0)
            self.assertEqual(r['cop_h']-r['cop_r'],1)
            self.assertGreaterEqual(r['work'],r['work_min'])
            self.assertLessEqual(r['cop_r'],r['cop_r_bound'])
            self.assertEqual(r['excess_work'],th*sigma)

    def test_energy_balance_does_not_imply_second_law(self):
        for work in (0,80):
            r=proposal(280,320,840,work)
            self.assertEqual(r['qh'],840+work)
            self.assertLess(r['sgen'],0);self.assertFalse(r['compatible'])
        self.assertIsNone(proposal(280,320,840,0)['cop_r'])
        self.assertEqual(proposal(280,320,840,80)['sgen'],Q(-1,8))
        rev=proposal(280,320,840,120)
        self.assertEqual(rev['sgen'],0);self.assertEqual(rev['cop_r'],7)

    def test_scales_and_temperature_gap(self):
        base=proposal(280,320,840,140)
        for scale in (Q(1,10),Q(3),Q(7,2)):
            r=proposal(280,320,840*scale,140*scale)
            self.assertEqual(r['cop_r'],6);self.assertEqual(r['sgen'],scale*base['sgen'])
            self.assertEqual(r['work_min'],scale*120)
        warmer=proposal(280,360,840,240)
        self.assertEqual(warmer['cop_r_bound'],Q(7,2))
        self.assertEqual(warmer['sgen'],0)
        scaled_t=proposal(560,640,840,140)
        self.assertEqual(scaled_t['sgen'],base['sgen']/2)
        self.assertEqual(scaled_t['cop_r_bound'],7)

    def test_cycle_mean_rates_and_units(self):
        r=proposal(280,320,840,140)
        for duration in (Q(1,2),Q(2),Q(5)):
            power=rates(r,duration)
            for name in power:self.assertEqual(power[name]*duration,r[name])
            self.assertEqual(power['qh']-power['qc'],power['work'])
        self.assertEqual(rates(r,2),dict(qc=Q(420),qh=Q(490),work=Q(70),sgen=Q(1,32)))

    def test_contracts(self):
        for values in ((0,320,840,140),(320,320,840,140),(330,320,840,140),(280,320,0,140),(280,320,840,-1),(True,320,840,140),(280.,320,840,140)):
            with self.assertRaises(ValueError):proposal(*values)
        for duration in (0,-1,True,2.):
            with self.assertRaises(ValueError):rates(proposal(280,320,840,140),duration)

if __name__=='__main__':unittest.main()
