from copy import deepcopy
from decimal import Decimal as D,localcontext
from itertools import product
from math import log,isfinite
from pathlib import Path
import json
import unittest
import dense_net as net
from .trace import trace,decision,fixture

class ForwardTests(unittest.TestCase):
    def test_nonzero_reference(self):
        r=trace(fixture(),[log(3)/2,1])
        self.assertAlmostEqual(r['hidden'][0],.5,places=14)
        self.assertAlmostEqual(r['hidden'][1],-.5,places=14)
        self.assertAlmostEqual(r['logit'],2,places=14)
        self.assertAlmostEqual(r['probability'],.8807970779778824,places=14)
        self.assertEqual(r['parameter_count'],9)
        self.assertEqual(decision(r['probability']),1)
        self.assertEqual(decision(r['probability'],.9),0)
    def test_decimal_independent_reference(self):
        # Exp da Decimal em vez de math.tanh/ramificação sigmoid do núcleo.
        with localcontext() as ctx:
            ctx.prec=60
            for H in (1,2,4):
                model=net.initialize(H,42)
                for x in product((-1.,0.,1.),repeat=2):
                    actual=trace(model,x);hidden=[]
                    for row,b in zip(model['W'],model['b']):
                        s=sum(D(str(w))*D(str(v)) for w,v in zip(row,x))+D(str(b))
                        e=(2*s).exp();hidden.append((e-1)/(e+1))
                    z=sum(D(str(v))*h for v,h in zip(model['v'],hidden))+D(str(model['c']))
                    p=1/(1+(-z).exp())
                    self.assertAlmostEqual(actual['logit'],float(z),places=12)
                    self.assertAlmostEqual(actual['probability'],float(p),places=12)
                    for a,b in zip(actual['hidden'],hidden):self.assertAlmostEqual(a,float(b),places=12)
    def test_state_and_hidden_symmetries(self):
        model=fixture();before=deepcopy(model);x=[log(3)/2,1];saved=x[:]
        r=trace(model,x);self.assertEqual(model,before);self.assertEqual(x,saved)
        self.assertEqual(trace(model,x),r)
        # Permutar unidades e inverter sinais em tanh preservam o logit.
        perm={'W':model['W'][::-1],'b':model['b'][::-1],'v':model['v'][::-1],'c':model['c']}
        self.assertAlmostEqual(trace(perm,x)['logit'],r['logit'],places=14)
        flip=deepcopy(model);flip['W'][0]=[-w for w in flip['W'][0]];flip['b'][0]*=-1;flip['v'][0]*=-1
        self.assertAlmostEqual(trace(flip,x)['logit'],r['logit'],places=14)
        r['hidden'][0]=99;self.assertEqual(model,before)
    def test_extreme_logits_and_contracts(self):
        for bias,p in ((1000.,1.),(-1000.,0.)):
            model=fixture();model['v']=[0.,0.];model['c']=bias
            r=trace(model,[0.,0.]);self.assertTrue(isfinite(r['probability']));self.assertEqual(r['probability'],p)
        for bad in (True,'1',float('nan'),float('inf')):
            with self.assertRaises(ValueError):trace(fixture(),[bad,0])
        with self.assertRaises(ValueError):trace(fixture(),[1])
        broken=fixture();broken['W'][0]=[1.]
        with self.assertRaises(ValueError):trace(broken,[1,1])
        huge=fixture();huge['W'][0]=[1e308,0.]
        with self.assertRaises(ValueError):trace(huge,[1e308,0.])
        for p,t in ((-1,.5),(1.1,.5),(.5,0),(.5,1)):
            with self.assertRaises(ValueError):decision(p,t)
        self.assertEqual(decision(.5,.5),1)
    def test_preserved_snippet_and_challenge(self):
        ls=json.loads((Path(__file__).resolve().parents[2]/'content/lessons.json').read_text())
        l=next(x for x in ls if x['id']=='dl-forward')
        exec(l['python'],{});exec(l['codingPractice']['solution'],{})
if __name__=='__main__':unittest.main()
