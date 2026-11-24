import unittest,itertools
from fractions import Fraction as Q
from .metrics import metrics,threshold,empirical_cost,predictive_precision

class ClassificationMetricTests(unittest.TestCase):
    def test_reference_and_original(self):
        original=metrics([1,1,1,1,1,0],[1,1,1,0,0,1])
        self.assertEqual(original['precision'],Q(3,4));self.assertEqual(original['recall'],Q(3,5))
        y=[1,0,1,0,1,0,0,0];s=[Q(i,10) for i in [9,8,7,6,4,3,2,1]]
        r=threshold(y,s,Q(1,2))
        self.assertEqual([r[k] for k in ['TP','FP','FN','TN']],[2,2,1,3])
        self.assertEqual(r['accuracy'],Q(5,8));self.assertEqual(r['f1'],Q(4,7))
        self.assertEqual(empirical_cost(r,1,4),6)
        r=threshold(y,s,Q(2,5));self.assertEqual(r['precision'],Q(3,5))
        self.assertEqual(r['recall'],1);self.assertEqual(empirical_cost(r,1,4),2)
    def test_all_four_bit_sequences_against_set_intersections(self):
        count=0
        universe=set(range(4))
        for y,pred in itertools.product(itertools.product([0,1],repeat=4),repeat=2):
            r=metrics(y,pred);actual={i for i,a in enumerate(y) if a};chosen={i for i,a in enumerate(pred) if a}
            expected=[len(actual&chosen),len(chosen-actual),len(actual-chosen),len(universe-(actual|chosen))]
            self.assertEqual([r[k] for k in ['TP','FP','FN','TN']],expected)
            self.assertEqual(sum(r[k] for k in ['TP','FP','FN','TN']),4)
            self.assertEqual(r['accuracy'],Q(sum(a==b for a,b in zip(y,pred)),4));count+=1
        self.assertEqual(count,256)
    def test_threshold_ties_and_recall_monotonicity(self):
        y=[1,0,1,0];s=[Q(1,2),Q(1,2),Q(3,4),Q(1,4)]
        self.assertEqual(threshold(y,s,Q(1,2))['TP'],2)
        self.assertEqual(threshold(y,s,Q(1,2))['FP'],1)
        results=[threshold(y,s,Q(i,8)) for i in range(9,-1,-1)]
        self.assertEqual([r['TP'] for r in results],sorted(r['TP'] for r in results))
        self.assertEqual([r['FP'] for r in results],sorted(r['FP'] for r in results))
        # Preserving order with strictly increasing transform and matching threshold.
        self.assertEqual(threshold(y,s,Q(1,2)),threshold(y,[x*x for x in s],Q(1,4)))
    def test_prevalence_by_integer_population_counts(self):
        for prevalence,npos in [(Q(1,10),100),(Q(1,100),10)]:
            # N=1000; TPR=.8, FPR=.1; all counts integer.
            tp=npos*4//5;fp=(1000-npos)//10
            expected=Q(tp,tp+fp)
            self.assertEqual(predictive_precision(prevalence,Q(4,5),Q(1,10)),expected)
        self.assertEqual(predictive_precision(Q(1,10),Q(4,5),Q(1,10)),Q(8,17))
        self.assertEqual(predictive_precision(Q(1,100),Q(4,5),Q(1,10)),Q(8,107))
    def test_empty_denominators_and_contracts(self):
        r=metrics([0,0],[0,0]);self.assertIsNone(r['precision']);self.assertIsNone(r['recall']);self.assertIsNone(r['f1']);self.assertIsNone(r['balanced_accuracy'])
        r=metrics([1,0],[0,0]);self.assertIsNone(r['precision']);self.assertEqual(r['recall'],0);self.assertEqual(r['f1'],0)
        for args in [([],[]),([1],[1,0]),([True],[1]),([2],[0])]:
            with self.assertRaises(ValueError):metrics(*args)
        for args in [([1],[.5],Q(1,2)),([1],[2],Q(1,2)),([1],[],Q(1,2))]:
            with self.assertRaises(ValueError):threshold(*args)
        self.assertIsNone(predictive_precision(0,1,0))
        with self.assertRaises(ValueError):empirical_cost(metrics([1],[1]),-1,1)
