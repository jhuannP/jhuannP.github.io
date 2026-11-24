import unittest,json
from itertools import product
from fractions import Fraction as Q
from pathlib import Path
from .baseline import fit_constant,score_constant

class BaselineTests(unittest.TestCase):
    def test_reference_and_heldout(self):
        train=(2,2,8);test=(5,7)
        self.assertEqual(fit_constant(train),4);self.assertEqual(fit_constant(train,'median'),2)
        self.assertEqual(score_constant(4,train),dict(mse=Q(8),mae=Q(8,3)))
        self.assertEqual(score_constant(2,train),dict(mse=Q(12),mae=Q(2)))
        self.assertEqual(score_constant(4,test)['mse'],5)
        self.assertEqual(score_constant(fit_constant(test),test)['mse'],1)
        self.assertEqual(score_constant(2,test)['mae'],4)
        self.assertEqual(score_constant(4,test)['mae'],2)

    def test_empirical_mean_identity_and_median_grid(self):
        for ys in product(range(-2,3),repeat=3):
            mean=fit_constant(ys);median=fit_constant(ys,'median')
            minimum=score_constant(mean,ys)['mse'];absolute=score_constant(median,ys)['mae']
            for c in map(Q,range(-3,4)):
                self.assertEqual(score_constant(c,ys)['mse'],minimum+(c-mean)**2)
                self.assertGreaterEqual(score_constant(c,ys)['mae'],absolute)

    def test_even_median_interval(self):
        ys=(1,9);self.assertEqual(fit_constant(ys,'median'),1)
        for c in (Q(1),Q(3,2),Q(5),Q(9)):
            self.assertEqual(score_constant(c,ys)['mae'],4)
        for c in (Q(0),Q(10)):
            self.assertGreater(score_constant(c,ys)['mae'],4)

    def test_units_scaling_shift_and_previous_examples(self):
        ys=(2,2,8);c=fit_constant(ys)
        for scale in (Q(1,10),Q(2),Q(1000)):
            shifted=tuple(scale*y+3 for y in ys);cc=fit_constant(shifted)
            self.assertEqual(cc,scale*c+3)
            self.assertEqual(score_constant(cc,shifted)['mse'],scale**2*score_constant(c,ys)['mse'])
            self.assertEqual(score_constant(cc,shifted)['mae'],scale*score_constant(c,ys)['mae'])
        root=Path(__file__).resolve().parents[2]
        l=next(l for l in json.loads((root/'content/lessons.json').read_text()) if l['id']=='ml-tarefa-alvo')
        exec(l['python'],{});exec(l['codingPractice']['solution'],{})

    def test_contracts(self):
        for ys in ((),(1.0,),(True,),(1,)*1001):
            with self.assertRaises(ValueError):fit_constant(ys)
        with self.assertRaises(ValueError):fit_constant((1,2),'unknown')
        with self.assertRaises(ValueError):score_constant(True,(1,2))
