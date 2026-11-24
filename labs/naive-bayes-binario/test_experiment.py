import unittest
from importlib import import_module
from fractions import Fraction as Q
from itertools import product
from copy import deepcopy
m=import_module("labs.naive-bayes-binario.experiment")

class BernoulliNBTests(unittest.TestCase):
    def test_duplicate_information(self):
        rows=[(1,1)]*4+[(0,0)]+[(1,1)]+[(0,0)]*4;ys=[0]*5+[1]*5
        self.assertEqual(m.posterior(m.fit(rows,ys,0),(1,1))[0],Q(16,17))
        self.assertEqual(m.posterior(m.fit(rows,ys,1),(1,1))[0],Q(25,29))
        selected=[y for r,y in zip(rows,ys) if r==(1,1)]
        self.assertEqual(Q(selected.count(0),len(selected)),Q(4,5))
        self.assertEqual(m.posterior(m.fit([(r[0],) for r in rows],ys,0),(1,))[0],Q(4,5))
        self.assertEqual(m.posterior(m.fit(rows,ys,0),(1,0)),(Q(1,2),Q(1,2)))
    def test_enumerated_pseudocounts(self):
        for vals in product((0,1),repeat=6):
            rows=[vals[:2],vals[2:4],vals[4:]];ys=[0,0,1]
            for alpha in (0,1,2):
                model=m.fit(rows,ys,alpha)
                for query in product((0,1),repeat=2):
                    scores=[]
                    for c in (0,1):
                        group=[r for r,y in zip(rows,ys) if y==c];score=Q(len(group),3)
                        for j,x in enumerate(query):
                            hits=sum(r[j]==x for r in group)
                            score*=Q(hits+alpha,len(group)+2*alpha)
                        scores.append(score)
                    expected=None if not sum(scores) else tuple(s/sum(scores) for s in scores)
                    self.assertEqual(m.posterior(model,query),expected)
    def test_normalization_and_absence(self):
        model=m.fit([(1,0),(1,1),(0,1)],[0,0,1],1)
        for c in (0,1):
            total=Q(0)
            for q in product((0,1),repeat=2):
                likelihood=Q(1)
                for x,p in zip(q,model.theta[c]):likelihood*=p if x else 1-p
                total+=likelihood
            self.assertEqual(total,1)
        self.assertEqual(m.posterior(model,(0,0)),(Q(9,17),Q(8,17)))
    def test_permutation_replication_no_mutation(self):
        rows=[[1,0],[0,1],[1,1]];ys=[0,1,0];original=deepcopy((rows,ys))
        model=m.fit(rows,ys,Q(1,2))
        self.assertEqual(model,m.fit(rows[::-1],ys[::-1],Q(1,2)))
        self.assertEqual(model,m.fit(rows*3,ys*3,Q(3,2)))
        self.assertEqual((rows,ys),original)
        for q in product((0,1),repeat=2):
            other=m.fit([r[::-1] for r in rows],ys,Q(1,2))
            self.assertEqual(m.posterior(model,q),m.posterior(other,q[::-1]))
    def test_contracts_and_zero_evidence(self):
        for rows,ys,a in [([],[],1),([(1,)],[],1),([(1,)],[0],1),
          ([(1,),(0,1)],[0,1],1),([(True,),(0,)],[0,1],1),
          ([(1,),(0,)],[0,True],1),([(1,),(0,)],[0,1],.5),([(1,),(0,)],[0,1],-1)]:
            with self.assertRaises(ValueError):m.fit(rows,ys,a)
        model=m.fit([(0,0),(1,1)],[0,1],0)
        self.assertIsNone(m.posterior(model,(1,0)))
        for q in ((),(True,0),(2,0),(0,),(0,0,0)):
            with self.assertRaises(ValueError):m.posterior(model,q)
