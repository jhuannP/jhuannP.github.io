from fractions import Fraction as Q
from itertools import product
import unittest
from .experiment import rates

class ActinRateBalanceTests(unittest.TestCase):
    def test_synthetic_stationary_example(self):
        r=rates(2)
        self.assertEqual(r["critical_plus"],1);self.assertEqual(r["critical_minus"],5)
        self.assertEqual(r["balance_c"],2)
        self.assertEqual((r["v_plus"],r["v_minus"],r["net"]),(3,-3,0))
        self.assertTrue(r["stationary_flow"]);self.assertFalse(r["both_balanced"])
    def test_quarter_grid_against_event_counts_in_four_seconds(self):
        for i in range(25):
            r=rates(Q(i,4))
            # Entradas menos saídas no intervalo; independente da forma v=k*c-d do código.
            self.assertEqual(r["v_plus"],Q(3*i-12,4))
            self.assertEqual(r["v_minus"],Q(i-20,4))
            self.assertEqual(r["net"],i-8)
            self.assertEqual(r["stationary_flow"],i==8)
    def test_general_balance_and_equal_critical_concentrations(self):
        for kp,km,dp,dm in product((1,2,3),repeat=4):
            cb=Q(dp+dm,kp+km);p=Q(dp,kp);m=Q(dm,km)
            r=rates(cb,kp,dp,km,dm)
            self.assertEqual(r["net"],0)
            self.assertTrue(min(p,m)<=cb<=max(p,m))
            self.assertEqual(r["both_balanced"],p==m)
            self.assertEqual(r["stationary_flow"],p!=m)
        for i in range(25):
            r=rates(Q(i,4),3,3,1,1)
            self.assertGreaterEqual(r["v_plus"]*r["v_minus"],0)
            self.assertEqual(r["stationary_flow"],False)
    def test_concentration_unit_change_and_rate_scale(self):
        for c in (0,Q(1,2),1,2,5):
            r=rates(c)
            converted=rates(Q(c)/1000000,3000000,3,1000000,5)
            for key in ("v_plus","v_minus","net"):
                self.assertEqual(r[key],converted[key])
            self.assertEqual(converted["balance_c"],r["balance_c"]/1000000)
            scaled=rates(c,6,6,2,10)
            self.assertEqual(scaled["balance_c"],r["balance_c"])
            self.assertEqual(scaled["net"],2*r["net"])
    def test_contracts_and_zero_off_limit(self):
        for args in ((-1,3,3,1,5),(1,0,3,1,5),(1,3,-1,1,5),(True,3,3,1,5),(1.0,3,3,1,5),(1,3,3,0,5)):
            with self.assertRaises(ValueError):rates(*args)
        r=rates(0,1,0,1,0)
        self.assertTrue(r["both_balanced"]);self.assertFalse(r["stationary_flow"])
