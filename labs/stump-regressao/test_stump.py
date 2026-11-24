import unittest,itertools
from fractions import Fraction as Q
from .stump import fit,predict

class StumpTests(unittest.TestCase):
    def test_fixture_and_leaf_constraint(self):
        x=[0,1,2,3];y=[0,1,2,5]
        m=fit(x,y);self.assertEqual(m['cost'],2);self.assertEqual(m['threshold'],Q(5,2))
        self.assertEqual(predict(m,Q(5,2)),1);self.assertEqual(predict(m,Q(13,5)),5)
        self.assertEqual(fit(x,y,2)['cost'],5)
        self.assertIsNone(fit(x,y,3)['threshold'])
        self.assertEqual(fit([1,1],[0,2])['left'],1)
        self.assertIsNone(fit(x,[4]*4)['threshold'])
    def test_enumerated_predictions(self):
        # Independente da busca do ajuste: todas as partições viáveis, SSE pelas previsões.
        x=[0,0,1,2]
        for y in itertools.product((-1,0,2),repeat=4):
            for minimum in (1,2,3):
                candidates=[]
                for t in (None,Q(1,2),Q(3,2)):
                    groups=[list(range(4))] if t is None else [[i for i,z in enumerate(x) if z<=t],[i for i,z in enumerate(x) if z>t]]
                    if t is not None and min(map(len,groups))<minimum:continue
                    pred=[Q(0)]*4
                    for group in groups:
                        avg=Q(sum(y[i] for i in group),len(group))
                        for i in group:pred[i]=avg
                    candidates.append(sum((pred[i]-y[i])**2 for i in range(4)))
                m=fit(x,y,minimum)
                self.assertEqual(m['cost'],min(candidates))
                self.assertEqual(sum((predict(m,z)-v)**2 for z,v in zip(x,y)),m['cost'])
    def test_permutation_and_target_scaling(self):
        x=[0,1,2,3];y=[0,1,2,5];base=fit(x,y)
        for order in itertools.permutations(range(4)):
            self.assertEqual(fit([x[i] for i in order],[y[i] for i in order]),base)
        for a in (-3,-1,2,4):
            m=fit(x,[a*v+7 for v in y])
            self.assertEqual(m['threshold'],base['threshold']);self.assertEqual(m['cost'],a*a*base['cost'])
        self.assertEqual(x,[0,1,2,3]);self.assertEqual(y,[0,1,2,5])
    def test_contracts(self):
        for x,y,k in [([],[],1),([1],[1,2],1),([True],[1],1),([1.0],[1],1),([1],[1],True),([1],[1],0),([1],[1],101)]:
            with self.assertRaises(ValueError):fit(x,y,k)
