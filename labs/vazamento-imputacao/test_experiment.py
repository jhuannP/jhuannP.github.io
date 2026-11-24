from fractions import Fraction as F
import unittest
from .experiment import inspect

class LeakageImputationTests(unittest.TestCase):
    def test_independent_filled_records_and_scores(self):
        for q in range(11):
            for label in [0,1]:
                s=inspect(q,label)
                # Materialize the actual two test records after each imputation.
                proper=[q,F(0+2,2)];leaked=[q,F(0+2+q,3)]
                labels=[int(q>=2),label]
                for key,records in [('proper',proper),('leaked',leaked)]:
                    predicted=[0 if value<2 else 1 for value in records]
                    correct=sum(1 for p,y in zip(predicted,labels) if p==y)
                    self.assertEqual(s[key+'_prediction'],predicted[1])
                    self.assertEqual(s[key+'_accuracy'],F(correct,2))
                self.assertEqual(s['mean_train'],proper[1])
                self.assertEqual(s['mean_all'],leaked[1])

    def test_label_never_fits_state(self):
        previous=None
        for q in range(11):
            a=inspect(q,0);b=inspect(q,1)
            for key in ['mean_train','mean_all','proper_prediction','leaked_prediction']:
                self.assertEqual(a[key],b[key])
            self.assertEqual(a['mean_train'],1)
            if previous is not None:self.assertEqual(a['mean_all']-previous,F(1,3))
            previous=a['mean_all']

    def test_better_worse_and_same_are_possible(self):
        a=inspect(8,1);b=inspect(8,0)
        self.assertGreater(a['leaked_accuracy'],a['proper_accuracy'])
        self.assertLess(b['leaked_accuracy'],b['proper_accuracy'])
        for label in [0,1]:
            self.assertEqual(inspect(0,label)['leaked_accuracy'],inspect(0,label)['proper_accuracy'])
        self.assertEqual(inspect(1)['mean_all'],inspect(1)['mean_train'])
        self.assertEqual(inspect(4)['mean_all'],2)
        self.assertEqual(inspect(4)['leaked_prediction'],1)

    def test_contracts(self):
        for q in [True,-1,11,8.0,None,'8']:
            with self.assertRaises(ValueError):inspect(q)
        for label in [False,-1,2,1.0,None]:
            with self.assertRaises(ValueError):inspect(8,label)
