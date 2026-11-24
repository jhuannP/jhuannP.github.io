import unittest
from fractions import Fraction as Q
from .field import contrast,rates

class FieldTests(unittest.TestCase):
    def test_fixtures_equal_mean(self):
        self.assertEqual(rates(1,1,1),dict(contrast=0,on=10,off=10))
        self.assertEqual(rates(Q(1,2),2,Q(1,2)),dict(contrast=Q(3,2),on=25,off=0))
        self.assertEqual(rates(Q(3,2),0,Q(3,2)),dict(contrast=-Q(3,2),on=0,off=25))
        for stim in ((1,1,1),(Q(1,2),2,Q(1,2)),(Q(3,2),0,Q(3,2))):
            self.assertEqual(sum(stim)/3,1)

    def test_grid_independent_weights_and_reflection(self):
        grid=[Q(i,4) for i in range(9)]
        for l in grid:
            for c in grid:
                for r in grid:
                    expected=sum(w*x for w,x in zip((-Q(1,2),Q(1),-Q(1,2)),(l,c,r)))
                    out=rates(l,c,r)
                    self.assertEqual(out['contrast'],expected)
                    self.assertEqual(out,rates(r,c,l))
                    self.assertGreaterEqual(out['on'],0);self.assertGreaterEqual(out['off'],0)
                    rev=rates(2-l,2-c,2-r)
                    self.assertEqual(out['on'],rev['off'])
                    self.assertEqual(out['off'],rev['on'])

    def test_uniform_shift_and_clipping(self):
        for a in range(5):
            for b in range(5):
                for c in range(5):
                    stim=(Q(a,4),Q(b,4),Q(c,4))
                    self.assertEqual(rates(*stim),rates(*(x+1 for x in stim)))
        # Linearidade de D não implica aditividade da saída com piso.
        A=(Q(3,4),0,Q(3,4));double=tuple(2*x for x in A)
        change=rates(*A)['on']-10
        self.assertNotEqual(rates(*double)['on']-10,2*change)
        self.assertEqual(contrast(*double),2*contrast(*A))

    def test_contracts(self):
        for stim in ((True,1,1),(0.5,1,1),(-1,1,1),(1,3,1)):
            with self.assertRaises(ValueError):rates(*stim)
        with self.assertRaises(ValueError):rates(1,1,1,baseline=-1)
        with self.assertRaises(ValueError):rates(1,1,1,gain=101)
        self.assertEqual(rates(0,2,0,baseline=0,gain=0)['on'],0)
