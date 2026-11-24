import unittest
from fractions import Fraction as F
from itertools import product
from .lloyd import lloyd

class LloydTests(unittest.TestCase):
    def test_local_and_global(self):
        x=(0,2,3,5,10)
        self.assertEqual(lloyd(x,(0,3))['inertia'],F(103,6))
        self.assertEqual(lloyd(x,(0,10))['inertia'],13)
        # Oracle independente: todas as 2^5 atribuições; recalcula médias e SSE.
        costs=[]
        for labels in product(range(2), repeat=5):
            groups=[[F(x[i]) for i in range(5) if labels[i]==j] for j in range(2)]
            costs.append(sum(sum((v-sum(g)/len(g))**2 for v in g) for g in groups if g))
        self.assertEqual(min(costs),13)

    def test_descent_and_mean_identity(self):
        for x in product(range(3),repeat=4):
            for initial in ((0,2),(0,0),(2,0)):
                r=lloyd(x,initial)
                for row in r['trace']:
                    self.assertGreaterEqual(row['before'], row['after_mean'])
                    self.assertGreaterEqual(row['after_mean'], row['after_assign'])
                    shift=sum(row['labels'].count(j)*(c-row['updated'][j])**2
                              for j,c in enumerate(row['centers']))
                    self.assertEqual(row['before']-row['after_mean'],shift)

    def test_affine_and_ties(self):
        x=(0,2,3,5,10);r=lloyd(x,(0,3))
        s=lloyd(tuple(3*v-7 for v in x),(-7,2))
        self.assertEqual(s['labels'],r['labels']);self.assertEqual(s['inertia'],9*r['inertia'])
        t=lloyd([0,2],[1,1]);self.assertEqual(t['labels'],(0,0))
        self.assertEqual(t['centers'],(1,1));self.assertEqual(t['inertia'],2)

    def test_contracts(self):
        for x,c in [([], [0]),([0],[]),([True],[0]),([0.5],[0]),([0],[float('inf')])]:
            with self.assertRaises(ValueError):lloyd(x,c)
        with self.assertRaises(RuntimeError):lloyd([0,2,3,5,10],[0,3],max_iter=1)
        for n in (True,0,1001,1.5):
            with self.assertRaises(ValueError):lloyd([0],[0],max_iter=n)
