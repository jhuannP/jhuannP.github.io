import unittest
from fractions import Fraction as Q
from .pentoses import REACTIONS,SUGAR_C,oxidative,apply,carbon_backbone,nadp_pool

class PentoseTests(unittest.TestCase):
    def test_each_reaction_balances_independently(self):
        for reaction,changes in REACTIONS.items():
            consumed=sum(-v*SUGAR_C.get(k,0) for k,v in changes.items() if v<0)
            formed=sum(v*SUGAR_C.get(k,0) for k,v in changes.items() if v>0)
            self.assertEqual(consumed,formed)
            self.assertEqual(changes.get('NADP',0)+changes.get('NADPH',0),0)
            start={k:-v for k,v in changes.items() if v<0}
            result=apply(start,reaction,1)
            self.assertEqual(carbon_backbone(result),carbon_backbone(start))
            self.assertEqual(nadp_pool(result),nadp_pool(start))

    def test_three_pentose_rearrangement(self):
        start={'G6P':3,'NADP':6};s=oxidative(start,3)
        self.assertEqual(s['Ru5P'],3);self.assertEqual(s['NADPH'],6);self.assertEqual(s['CO2'],3)
        for reaction,extent in [('isomerase',1),('epimerase',2),('transcetolase1',1),('transaldolase',1),('transcetolase2',1)]:
            s=apply(s,reaction,extent)
            self.assertEqual(carbon_backbone(s),18)
            self.assertEqual(nadp_pool(s),6)
        self.assertEqual(s['F6P'],2);self.assertEqual(s['GAP'],1)
        self.assertEqual(s['NADPH'],6);self.assertEqual(s['CO2'],3)
        self.assertEqual(6*2+3+3,18)
        for species in ['G6P','6PGL','6PG','Ru5P','R5P','X5P','S7P','E4P']:
            self.assertEqual(s[species],0)

    def test_cofactor_limited_and_nonmutation(self):
        start={'G6P':6,'NADP':9}
        result=oxidative(start,Q(9,2))
        self.assertEqual(result['G6P'],Q(3,2));self.assertEqual(result['Ru5P'],Q(9,2))
        self.assertEqual(result['CO2'],Q(9,2));self.assertEqual(result['NADPH'],9)
        self.assertEqual(result['NADP'],0)
        self.assertEqual(start,{'G6P':6,'NADP':9})
        with self.assertRaises(ValueError):oxidative(start,5)
        self.assertEqual(start,{'G6P':6,'NADP':9})

    def test_linear_scaling_and_bookkeeping_scope(self):
        for amount in [Q(0),Q(1,2),1,3,10]:
            r=oxidative({'G6P':amount,'NADP':2*amount},amount)
            self.assertEqual(r['NADPH'],2*amount)
            self.assertEqual(r['CO2'],amount)
            self.assertEqual(carbon_backbone(r),6*amount)
        # Cofatores têm seus carbonos intactos: não pertencem ao balanço de esqueleto.
        self.assertEqual(carbon_backbone({'NADPH':10}),0)
        self.assertEqual(nadp_pool({'NADPH':10}),10)
        with self.assertRaises(ValueError):apply({'Ru5P':3},'transcetolase1',1)

    def test_contracts(self):
        for start in [{'ATP':1},{'G6P':-1}]:
            with self.assertRaises(ValueError):oxidative(start,0)
        for bad in [True,1.0,'1']:
            with self.assertRaises(TypeError):oxidative({'G6P':bad},0)
        with self.assertRaises(ValueError):apply({},'unknown',0)
        with self.assertRaises(ValueError):oxidative({},-1)

if __name__=='__main__':unittest.main()
