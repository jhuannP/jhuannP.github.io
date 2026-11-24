import unittest
from .balance import balance

class BalanceTests(unittest.TestCase):
    def test_original_batch(self):
        a=balance(4,1)
        self.assertEqual((a['atp_gross'],a['atp_pfk'],a['atp_hexokinase'],a['atp_net']),(20,5,1,14))
        self.assertEqual(a['lactate'],10);self.assertEqual(a['carbon_in'],30)
        self.assertEqual(a['saving_vs_free'],4)
    def test_441_balances(self):
        for p in range(21):
            for f in range(21):
                a=balance(p,f)
                self.assertEqual(a['atp_net'],3*p+2*f)
                self.assertEqual(a['carbon_in'],a['carbon_out'])
                self.assertEqual(a['nadh_produced'],a['nadh_used'])
                self.assertEqual(a['atp_net']-a['atp_net_if_all_free'],p)
    def test_additivity_and_endpoints(self):
        for p,f in ((0,0),(0,7),(9,0),(4,1),(100,200)):
            for q,g in ((0,0),(1,2),(3,1)):
                left,right,total=balance(p,f),balance(q,g),balance(p+q,f+g)
                for key in total:self.assertEqual(total[key],left[key]+right[key])
        self.assertEqual(balance(0,1)['atp_net'],2)
        self.assertEqual(balance(1,0)['atp_net'],3)
    def test_contracts(self):
        for p,f in ((True,1),(1,False),(-1,1),(1.5,1),(1,'2'),(1000001,0)):
            with self.assertRaises(ValueError):balance(p,f)
