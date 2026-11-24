import unittest
from fractions import Fraction as Q
from itertools import permutations
from .split import memorize,leave_group_out,temporal

class Tests(unittest.TestCase):
    def test_original_group_fixture(self):
        g=['A','A','B','B','C','C'];y=[0,2,8,10,16,18]
        a=memorize(g,y,[0,2,4],[1,3,5]);self.assertEqual(a['predictions'],[0,8,16]);self.assertEqual(a['mse'],4)
        results=[memorize(g,y,tr,te) for tr,te in leave_group_out(g)]
        self.assertEqual([r['fallback'] for r in results],[13,9,5])
        self.assertEqual([r['mse'] for r in results],[145,1,145])
        self.assertEqual(sum(r['sse'] for r in results)/6,97)
    def test_group_partition_and_row_order(self):
        g=['A','A','B','C','C'];y=[0,2,8,16,18]
        base=sum(memorize(g,y,tr,te)['sse'] for tr,te in leave_group_out(g))
        for order in permutations(range(5)):
            gg=[g[i] for i in order];yy=[y[i] for i in order];seen=[];sse=0
            for tr,te in leave_group_out(gg):
                self.assertFalse({gg[i] for i in tr}&{gg[i] for i in te})
                self.assertEqual(set(tr)|set(te),set(range(5)))
                seen.extend(te);sse+=memorize(gg,yy,tr,te)['sse']
            self.assertEqual(sorted(seen),list(range(5)));self.assertEqual(sse,base)
    def test_temporal_availability_and_expanding(self):
        self.assertEqual(temporal(10,8,2,2),(tuple(range(7)),(7,),(8,9)))
        count=0
        for n in range(4,16):
            for h in range(1,4):
                for cut in range(h,n):
                    tr,pu,te=temporal(n,cut,h,1)
                    self.assertEqual(set(tr)|set(pu),set(range(cut)))
                    self.assertTrue(all(t<cut and t+h<=cut for t in tr))
                    self.assertTrue(all(t<cut and t+h>cut for t in pu))
                    self.assertFalse(set(tr)&set(te));count+=1
        self.assertEqual(count,270)
        folds=[temporal(10,c,2,2) for c in (4,6,8)]
        self.assertTrue(set(folds[0][0])<set(folds[1][0])<set(folds[2][0]))
        # Ordem de origem sozinha aceitaria7; seu rótulo só chega em9.
        self.assertLess(7,8);self.assertGreater(7+2,8)
    def test_contracts(self):
        for args in [(10,8,2,3),(10,1,2,1),(10,8,0,1),(10,8,True,1),(2.,1,1,1)]:
            with self.assertRaises(ValueError):temporal(*args)
        for args in [(['A'],[0],[0],[0]),(['A','B'],[0,1],[0,0],[1]),
                     (['A','B'],[0,1],[True],[1]),(['A','B'],[0,1],[0],[2]),
                     (['A','B'],[0],[0],[1]),(['A','B'],[0.,1],[0],[1]),
                     (['A',''],[0,1],[0],[1])]:
            with self.assertRaises(ValueError):memorize(*args)
        with self.assertRaises(ValueError):leave_group_out(['A','A'])
