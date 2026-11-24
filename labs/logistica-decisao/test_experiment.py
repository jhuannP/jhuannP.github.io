import math,unittest
from decimal import Decimal as D,localcontext
from .experiment import probability,binary_loss,decide,inspect

class LogisticDecisionTests(unittest.TestCase):
    def test_decimal_probabilities_and_stable_loss(self):
        with localcontext() as ctx:
            ctx.prec=90
            for z in (-40,-5,-1,0,1,5,40):
                q=D(z);p=1/(1+(-q).exp())
                self.assertAlmostEqual(probability(z),float(p),places=15)
                for y in (0,1):
                    expected=-(p.ln() if y else (1-p).ln())
                    self.assertLess(abs(D.from_float(binary_loss(z,y))/expected-1),D('5e-15'))
        self.assertGreater(binary_loss(40,1),0)
        self.assertGreater(binary_loss(-40,0),0)
        self.assertEqual(binary_loss(1000,0),1000);self.assertEqual(binary_loss(-1000,1),1000)
        self.assertEqual(decide(1000,1),0);self.assertEqual(decide(-1000,0),1)

    def test_gradients_by_independent_central_differences(self):
        for w in (-4.,-.5,0.,.5,4.):
            for b in (-3.,0.,3.):
                s=inspect(w,b);h=1e-5
                # Avaliação direta da probabilidade e log é segura nesta janela moderada.
                def raw(v,c):
                    return -sum(y*math.log(1/(1+math.exp(-(v*a+c))))+(1-y)*math.log(1-1/(1+math.exp(-(v*a+c)))) for a,y in zip((-2,-1,0,1,2),(0,1,0,1,1)))/5
                fd=[(raw(w+h,b)-raw(w-h,b))/(2*h),(raw(w,b+h)-raw(w,b-h))/(2*h)]
                for a,c in zip(s['gradient'],fd):self.assertAlmostEqual(a,c,delta=2e-7)

    def test_confusion_counts_by_hand_and_threshold_invariants(self):
        a=inspect(threshold=.5);b=inspect(threshold=.8);c=inspect(threshold=.2)
        self.assertEqual(a['counts'],dict(TN=1,FP=1,FN=1,TP=2))
        self.assertEqual(b['counts'],dict(TN=2,FP=0,FN=2,TP=1))
        self.assertEqual(c['counts'],dict(TN=1,FP=1,FN=0,TP=3))
        self.assertEqual(a['accuracy'],b['accuracy']);self.assertEqual(a['precision'],2/3)
        for w in (-2.,0.,2.):
            for bias in (-3.,0.,3.):
                states=[inspect(w,bias,0,t) for t in (0,.2,.5,.8,1)]
                for s in states:
                    self.assertEqual(sum(s['counts'].values()),5)
                    self.assertEqual(s['loss'],states[0]['loss']);self.assertEqual(s['gradient'],states[0]['gradient'])
                    self.assertEqual([r['p'] for r in s['rows']],[r['p'] for r in states[0]['rows']])
                    if s['boundary'] is not None:self.assertAlmostEqual(w*s['boundary']+bias,math.log(s['threshold']/(1-s['threshold'])))
                self.assertEqual(states[0]['counts']['FN'],0);self.assertEqual(states[-1]['counts']['FP'],0)
                for left,right in zip(states,states[1:]):
                    for k in ('TP','FP'):self.assertGreaterEqual(left['counts'][k],right['counts'][k])
        self.assertIsNone(inspect(0,-3)['precision']);self.assertEqual(inspect(0,0,0,.5)['decision'],1)

    def test_cost_rule_and_contracts(self):
        for fp in (1,2):
            for fn in (1,4):
                threshold=fp/(fp+fn)
                for p in (0,.1,.3,.5,.9,1):
                    risk1=fp*(1-p);risk0=fn*p
                    self.assertEqual(risk1<=risk0,p>=threshold)
        for args in ((5,0,0,.5),(0,4,0,.5),(1,0,3,.5),(1,0,0,-.1)):
            with self.assertRaises(ValueError):inspect(*args)
        for z,t in ((float('inf'),.5),(0,1.1),(0,float('nan'))):
            with self.assertRaises(ValueError):decide(z,t)
