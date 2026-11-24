import unittest
import csv
from pathlib import Path
from fractions import Fraction as Q
from math import nan
from .experiment import planning, summarize

class ReplicateTests(unittest.TestCase):
    def test_known_values_and_variance_components(self):
        q=planning(4,3,2,1)
        self.assertEqual(q['correct_variance'],Q(13,6))
        self.assertEqual(q['naive_variance'],Q(5,6))
        self.assertEqual(q['icc'],Q(4,5));self.assertEqual(q['design_effect'],Q(13,5))
        for r in (1,3,8):
            self.assertEqual(planning(4,r,0,2)['design_effect'],1)
            self.assertEqual(planning(4,r,2,0)['design_effect'],r)
            self.assertEqual(planning(4,r,0,0)['correct_variance'],0)
            self.assertIsNone(planning(4,r,0,0)['icc'])
        self.assertEqual(planning(8,3,2,1)['correct_variance'],q['correct_variance']/2)

    def test_independent_covariance_matrix_sum(self):
        # Soma de covariâncias de todas as leituras, com pesos 1/(nr).
        for n in (1,2,5):
            for r in (1,2,4):
                for tau,sigma in ((0,1),(2,0),(2,1)):
                    observations=[(i,j) for i in range(n) for j in range(r)]
                    covariance_sum=sum(Q((tau*tau if i==k else 0)+(sigma*sigma if (i,j)==(k,l) else 0)) for i,j in observations for k,l in observations)
                    var_difference=2*covariance_sum/Q((n*r)**2)
                    self.assertEqual(planning(n,r,tau,sigma)['correct_variance'],var_difference)
                    self.assertGreaterEqual(var_difference,planning(n,r,tau,sigma)['naive_variance'])

    def test_nested_data_summary_and_duplicate_readings(self):
        c=[[8,10],[12,14]];t=[[12,14],[14,16]]
        grouped={'C':{},'T':{}}
        with (Path(__file__).parent/'data.csv').open() as handle:
            for row in csv.DictReader(handle):
                grouped[row['group']].setdefault(row['unit_id'],[]).append(float(row['signal']))
        self.assertEqual(list(grouped['C'].values()),c)
        self.assertEqual(list(grouped['T'].values()),t)
        q=summarize(c,t)
        self.assertEqual(q['control']['unit_means'],[9,13])
        self.assertEqual(q['treated']['unit_means'],[13,15])
        self.assertEqual(q['difference'],3);self.assertEqual(q['estimated_variance'],5)
        repeated=summarize([x*5 for x in c],[x*5 for x in t])
        self.assertEqual(q,repeated)
        shifted=summarize([[v+100 for v in row] for row in c],[[v+100 for v in row] for row in t])
        self.assertEqual(shifted['difference'],3);self.assertEqual(shifted['estimated_variance'],5)
        self.assertEqual(summarize(list(reversed(c)),list(reversed(t)))['difference'],3)

    def test_contract(self):
        for args in ((0,1,1,1),(1,0,1,1),(True,1,1,1),(2,1.0,1,1),(2,1,-1,1),(2,1,1.,1),(2,1,True,1)):
            with self.assertRaises(ValueError):planning(*args)
        for c,t in (([[1]],[[1],[2]]),([[],[1]],[[1],[2]]),([[nan],[1]],[[1],[2]]),([[True],[1]],[[1],[2]])):
            with self.assertRaises(ValueError):summarize(c,t)
