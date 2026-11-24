import unittest
from fractions import Fraction as Q
from itertools import product
from .experiment import fit,crossvalidate,choose,DATA,FOLDS

class CrossValidationRefitTests(unittest.TestCase):
    def test_hand_worked_fold_and_selection(self):
        s=crossvalidate(DATA,FOLDS)
        self.assertEqual(s['folds'][0]['fit'],dict(a=Q(1),b=Q(2)))
        self.assertEqual(s['folds'][0]['predictions'],[Q(-5),Q(7)])
        self.assertEqual([f['mse'] for f in s['folds']],[Q(8),Q(61,25),Q(205,169)])
        self.assertEqual(s['mse'],Q(49234,12675))
        result=choose(DATA,FOLDS)
        self.assertEqual(result['lam'],0);self.assertEqual(result['refit'],dict(a=Q(5,3),b=Q(17,7)))
        self.assertEqual(sum(len(f['validation']) for f in s['folds']),6)
    def test_fit_against_normal_equations(self):
        xs=(-1,0,2)
        for ys in product((-2,0,3),repeat=3):
            for lam in (0,1,4):
                n=3;sx=sum(xs);sy=sum(ys);sxx=sum(x*x for x in xs)+lam;sxy=sum(x*y for x,y in zip(xs,ys));det=n*sxx-sx*sx
                expected=dict(a=Q(sy*sxx-sx*sxy,det),b=Q(n*sxy-sx*sy,det))
                self.assertEqual(fit(list(zip(xs,ys)),lam),expected)
    def test_validation_targets_do_not_fit_their_own_fold(self):
        changed=list(DATA);changed[5]=(3,101)
        a,b=crossvalidate(DATA,FOLDS),crossvalidate(changed,FOLDS)
        self.assertEqual(a['folds'][0]['fit'],b['folds'][0]['fit'])
        self.assertEqual(a['folds'][0]['predictions'],b['folds'][0]['predictions'])
        self.assertNotEqual(a['folds'][0]['mse'],b['folds'][0]['mse'])
        self.assertNotEqual(a['folds'][1]['fit'],b['folds'][1]['fit'])
    def test_unequal_sizes_and_order_invariance(self):
        s=crossvalidate(DATA,((0,),(1,2),(3,4,5)))
        self.assertEqual(s['mse'],sum(len(f['validation'])*f['mse'] for f in s['folds'])/6)
        self.assertNotEqual(s['mse'],s['fold_mean'])
        self.assertEqual(s['mse'],crossvalidate(DATA,((5,4,3),(2,1),(0,)))['mse'])
    def test_contracts(self):
        for folds in [((0,1),(1,2,3,4,5)),((0,1),(2,3,4)),((0,1),(2,3,4,6)),((),(0,1,2,3,4,5)),((False,5),(1,4),(2,3))]:
            with self.assertRaises(ValueError):crossvalidate(DATA,folds)
        for lam in (-1,True,.5):
            with self.assertRaises(ValueError):fit(DATA,lam)
        with self.assertRaises(ValueError):fit(((1,2),(1,3)),0)
        self.assertEqual(fit(((1,2),(1,3)),1),dict(a=Q(5,2),b=Q(0)))
        with self.assertRaises(ValueError):choose(DATA,FOLDS,())
