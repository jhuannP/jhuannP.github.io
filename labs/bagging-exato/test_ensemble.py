import unittest
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from math import factorial
from .ensemble import bootstrap_models,distribution,mean_variance,oob_predictions,variance_factor,fit,predict

class EnsembleTests(unittest.TestCase):
    def setUp(self):
        self.x=(0,1,2);self.y=(0,2,0);self.models=bootstrap_models(self.x,self.y)

    def test_exact_fixture_and_original_model(self):
        self.assertEqual(len(self.models),27)
        self.assertEqual(distribution(self.models,1),Counter({Q(0):8,Q(1):6,Q(2):13}))
        self.assertEqual(mean_variance(distribution(self.models,1)),(Q(32,27),Q(542,729)))
        original=fit(self.x,self.y)
        self.assertEqual(original['threshold'],Q(1,2))
        self.assertEqual(predict(original,1),1)

    def test_independent_multinomial_weights(self):
        # Ten unordered count vectors replace 27 ordered index sequences.
        count_vectors=[ks for ks in product(range(4),repeat=3) if sum(ks)==3]
        self.assertEqual(len(count_vectors),10)
        for query in (Q(k,2) for k in range(-2,5)):
            expected=Counter()
            for ks in count_vectors:
                ids=tuple(i for i,n in enumerate(ks) for _ in range(n))
                m=fit([self.x[i] for i in ids],[self.y[i] for i in ids])
                weight=factorial(3)
                for n in ks:weight//=factorial(n)
                expected[predict(m,query)]+=weight
            self.assertEqual(expected,distribution(self.models,query))
            self.assertEqual(sum(expected.values()),27)

    def test_two_independent_bootstraps_mean_variance(self):
        values=[predict(m,1) for ids,m in self.models]
        averages=[(a+b)/2 for a,b in product(values,repeat=2)]
        mean=sum(averages,Q(0))/len(averages)
        variance=sum((v-mean)**2 for v in averages)/len(averages)
        self.assertEqual(len(averages),729)
        self.assertEqual(mean,Q(32,27))
        self.assertEqual(variance,Q(271,729))

    def test_oob_exclusion_and_target_invariance(self):
        expected=((Q(7,4),8),(Q(0),8),(Q(7,4),8))
        self.assertEqual(oob_predictions(self.models,self.x),expected)
        for i in range(3):
            self.assertEqual(sum(i not in ids for ids,m in self.models),8)
            changed=list(self.y);changed[i]+=100
            new=bootstrap_models(self.x,changed)
            self.assertEqual(oob_predictions(new,self.x)[i],expected[i])
        mse=sum((pred-Q(y))**2 for (pred,n),y in zip(expected,self.y))/3
        self.assertEqual(mse,Q(27,8))
        self.assertEqual(oob_predictions(bootstrap_models([0],[2]),[0]),((None,0),))

    def test_shared_component_correlation_floor(self):
        # Independent symmetric A and eps_b; Z_b=A+eps_b. Var(Z_b)=2,cov=1.
        for size in range(1,5):
            values=[]
            for states in product((-1,1),repeat=size+1):
                common=states[0];eps=states[1:]
                values.append(sum((Q(common+e) for e in eps),Q(0))/size)
            mean=sum(values,Q(0))/len(values)
            variance=sum((v-mean)**2 for v in values)/len(values)
            self.assertEqual(mean,0)
            self.assertEqual(variance,1+Q(1,size))
            self.assertEqual(variance,2*variance_factor(size,Q(1,2)))
        self.assertEqual(variance_factor(100,1),1)
        self.assertEqual(variance_factor(100,0),Q(1,100))

    def test_contracts(self):
        for x,y in [([],[]),([1],[1,2]),([0]*5,[0]*5),([True],[0]),([1],[2.0])]:
            with self.assertRaises(ValueError):bootstrap_models(x,y)
        with self.assertRaises(ValueError):distribution(self.models,1.0)
        with self.assertRaises(ValueError):mean_variance(Counter())
        for size,rho in [(0,0),(True,0),(2,-1),(2,2),(2,.5)]:
            with self.assertRaises(ValueError):variance_factor(size,rho)

if __name__=='__main__':unittest.main()
