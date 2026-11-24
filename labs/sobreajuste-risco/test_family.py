from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
import unittest
from .family import predict,mse,select,uniform_risk

class FamilyTests(unittest.TestCase):
    def test_preserved_reference(self):
        self.assertEqual(predict(Q(1,2),2),Q(-1,2))
        self.assertEqual(predict(Q(1,2),4),Q(-5,4))
        self.assertEqual(uniform_risk(2),Q(32,105))
        self.assertEqual(uniform_risk(4),Q(128,105))
        self.assertEqual(mse(2,((Q(1,2),Q(1,4)),)),Q(9,16))
    def test_training_cannot_identify_truth(self):
        for a,b in product((-3,0,2,4),repeat=2):
            train=tuple((Q(x),predict(x,b)) for x in (-1,0,1))
            self.assertEqual(mse(a,train),0)
            self.assertEqual(uniform_risk(a,b),uniform_risk(b,a))
            self.assertEqual(uniform_risk(a,b)==0,a==b)
    def test_independent_seven_node_quadrature(self):
        # Regra fechada7pontos; conferir momentos0..7 antes de usá-la.
        xs=tuple(Q(-1)+Q(j,3) for j in range(7))
        weights=tuple(Q(w,840) for w in (41,216,27,272,27,216,41))
        for degree in range(8):
            target=Q(0) if degree%2 else Q(1,degree+1)
            self.assertEqual(sum(w*x**degree for x,w in zip(xs,weights)),target)
        for a,b in product((-2,0,2),repeat=2):
            value=sum(w*(predict(x,a)-predict(x,b))**2 for x,w in zip(xs,weights))
            self.assertEqual(uniform_risk(a,b),value)
    def test_validation_and_tie_policy(self):
        for b in (0,2,4):
            val=tuple((x,predict(x,b)) for x in (Q(-1,2),Q(1,2)))
            self.assertEqual(select((0,2,4),val),b)
        # Só nós do treino: a primeira escolha vence empate, não evidência.
        train=tuple((x,Q(x*x)) for x in (-1,0,1))
        self.assertEqual(select((4,0,2),train),4)
        self.assertEqual(uniform_risk(0,2),Q(32,105))
    def test_old_snippet_and_challenge(self):
        ls=json.loads((Path(__file__).resolve().parents[2]/'content/lessons.json').read_text())
        l=next(x for x in ls if x['id']=='ml-sobreajuste')
        exec(l['python'],{});exec(l['codingPractice']['solution'],{})
    def test_contracts(self):
        for bad in (True,1.0,'1'):
            with self.assertRaises(TypeError):predict(bad,0)
        with self.assertRaises(ValueError):mse(0,())
        with self.assertRaises(ValueError):mse(0,((1,),))
        with self.assertRaises(ValueError):select((),((0,0),))
        with self.assertRaises(ValueError):select((0,),())
if __name__=='__main__':unittest.main()
