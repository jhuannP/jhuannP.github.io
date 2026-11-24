import unittest
from fractions import Fraction as Q
from itertools import product
from cost import inventory,limit_from_pyruvate


class CostTests(unittest.TestCase):
    def test_inventory_and_carbon(self):
        for g in (Q(0),Q(1,1000),Q(3,1000),Q(1,2),Q(2)):
            p,l=inventory(g),inventory(g,'lactate')
            self.assertEqual(p['ATP_carboxylase']+p['ATP_PGK'],p['ATP_total'])
            self.assertEqual(p['ATP_total']+p['GTP'],6*g)
            self.assertEqual(p['carbon_input']+p['carbon_temporarily_added'],8*g)
            self.assertEqual(8*g-p['carbon_released'],p['carbon_glucose'])
            self.assertEqual(p['NADH_net_used'],2*g)
            self.assertEqual(l['NADH_used'],l['NADH_from_lactate'])
            self.assertEqual(l['NADH_net_used'],0)
            self.assertEqual(l['ATP_total'],p['ATP_total'])

    def test_resource_ceiling_by_enumeration(self):
        # 625 stock sets; enumerate quarter-mol candidates independently of min formula.
        for stocks in product(range(5),repeat=4):
            feasible=[Q(k,4) for k in range(9)
                      if all(coef*Q(k,4)<=available for coef,available in zip((2,4,2,2),stocks))]
            result=limit_from_pyruvate(*stocks)
            self.assertEqual(result['ceiling'],max(feasible))
            self.assertTrue(all(v>=0 for v in result['remaining'].values()))
            self.assertTrue(result['limiting'])

    def test_example_and_scale(self):
        result=limit_from_pyruvate(2,4,1,2)
        self.assertEqual(result['ceiling'],Q(1,2))
        self.assertEqual(result['limiting'],['GTP'])
        self.assertEqual(result['remaining'],dict(pyruvate=1,ATP=2,GTP=0,NADH=1))
        for factor in (Q(1,1000),Q(1,2),Q(3)):
            self.assertEqual(limit_from_pyruvate(*(factor*x for x in (2,4,1,2)))['ceiling'],factor/2)

    def test_contracts(self):
        for g in (True,-1,1.0,'1',float('nan')):
            with self.assertRaises(ValueError): inventory(g)
        with self.assertRaises(ValueError):inventory(1,'glycerol')
        for stocks in [(2,4,-1,2),(2,4,True,2),(2,4,1,2.0)]:
            with self.assertRaises(ValueError):limit_from_pyruvate(*stocks)


if __name__=='__main__':unittest.main()
