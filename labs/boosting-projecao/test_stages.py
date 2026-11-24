import unittest
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path
from learning_models import boost_fit,boost_predict
from .stages import fit,predict,STUMP

class BoostTests(unittest.TestCase):
    def test_closed_reference_and_validation_counterexample(self):
        m=fit([0,1,2,3],[0,0,2,2],10)
        for k,s in enumerate(m['history']):
            a=Q(1,2**k)
            self.assertEqual(s['pred'],(a,a,2-a,2-a))
            self.assertEqual(s['mse'],Q(1,4**k))
            self.assertEqual((predict(m,Q(3,2),k)-1)**2,(1-a)**2)
        self.assertEqual(m['history'][5]['mse'],Q(1,1024))

    def test_projection_and_existing_float_engine(self):
        # 27 targets x 3 steps x 6 updates = 486 stage comparisons.
        for y in product((-1,0,2),repeat=3):
            for eta in (Q(1,4),Q(1,2),Q(1)):
                m=fit([0,1,2],y,6,eta)
                native=boost_fit([0,1,2],y,6,float(eta))
                for v in (Q(-1),Q(1,2),Q(3)):
                    self.assertAlmostEqual(float(predict(m,v)),boost_predict(native,float(v)),places=11)
                for k,t in enumerate(m['trees']):
                    r=m['history'][k]['residual'];a=m['history'][k]['pred'];b=m['history'][k+1]['pred']
                    correction=tuple((v-u)/eta for u,v in zip(a,b))
                    norm=sum(v*v for v in correction)
                    self.assertEqual(sum(u*v for u,v in zip(r,correction)),norm)
                    old=3*m['history'][k]['mse'];new=3*m['history'][k+1]['mse']
                    self.assertEqual(new-old,-eta*(2-eta)*norm)
                    self.assertLessEqual(new,old)

    def test_tied_split_and_uninformative_input(self):
        m=fit([0,1,2,3],[0,2,0,2],1)
        self.assertEqual(m['trees'][0]['threshold'],Q(1,2))
        self.assertEqual(m['history'][1]['pred'],(Q(1,2),Q(7,6),Q(7,6),Q(7,6)))
        self.assertEqual(m['history'][1]['mse'],Q(3,4))
        m=fit([0,0],[0,2],8)
        self.assertTrue(all(s['mse']==1 for s in m['history']))
        self.assertTrue(all(t['threshold'] is None for t in m['trees']))

    def test_loss_derivative_independently(self):
        eps=Q(1,1000)
        for y,f in product((-2,0,3),repeat=2):
            loss=lambda z:(y-z)**2/2
            self.assertEqual(-(loss(f+eps)-loss(f-eps))/(2*eps),y-f)

    def test_old_material_and_contracts(self):
        lesson=next(x for x in json.loads((Path(__file__).resolve().parents[2]/'content/lessons.json').read_text()) if x['id']=='ml-boosting')
        exec(lesson['python'],{})
        exec(lesson['codingPractice']['solution'],{})
        self.assertEqual(predict(fit([0,1],[1,3],0),7),2)
        for rounds in (-1,51,True,1.0):
            with self.assertRaises(ValueError):fit([0],[1],rounds)
        for eta in (0,-1,2,True,'1',.5):
            with self.assertRaises(ValueError):fit([0],[1],eta=eta)
        for x,y in (([],[]),([1],[1,2]),(list(range(101)),list(range(101)))):
            with self.assertRaises(ValueError):fit(x,y)
        with self.assertRaises(ValueError):predict(fit([0],[1]),0,6)
