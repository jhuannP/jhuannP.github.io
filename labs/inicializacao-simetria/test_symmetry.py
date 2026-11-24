import unittest
from fractions import Fraction as Q
from itertools import product
from copy import deepcopy
from dense_net import gradients,update,forward,initialize,loss
from .symmetry import paired,variance_factors


class InitializationTests(unittest.TestCase):
    def test_counterexample_outgoing_breaks_symmetry(self):
        m=paired((1.,2.));original=deepcopy(m);g=gradients(m,[[1.,0.]],[1.])
        self.assertEqual(g['W'],[[-.5,0.],[-1.,0.]])
        self.assertEqual(g['b'],[-.5,-1.]);self.assertEqual(g['v'],[0.,0.])
        self.assertEqual(g['c'],-.5)
        n=update(m,g,.1);self.assertEqual(n['W'],[[.05,0.],[.1,0.]])
        self.assertEqual(m,original)
        # Independent finite difference of loss for incoming coordinate W[1][0].
        h=1e-6;plus=deepcopy(m);minus=deepcopy(m)
        plus['W'][1][0]+=h;minus['W'][1][0]-=h
        derivative=(loss(plus,[[1.,0.]],[1.])-loss(minus,[[1.,0.]],[1.]))/(2*h)
        self.assertAlmostEqual(derivative,-1.,places=8)

    def test_symmetric_updates_and_zero_trap(self):
        m=paired((1.,1.));m['W']=[[.2,-.3],[.2,-.3]];m['b']=[.1,.1]
        X=[[1.,0.],[0.,1.]];y=[1.,0.]
        for _ in range(8):
            g=gradients(m,X,y)
            self.assertEqual(g['W'][0],g['W'][1]);self.assertEqual(g['v'][0],g['v'][1])
            m=update(m,g,.1)
            self.assertEqual(m['W'][0],m['W'][1]);self.assertEqual(m['b'][0],m['b'][1]);self.assertEqual(m['v'][0],m['v'][1])
        z=paired((0.,0.))
        for _ in range(8):z=update(z,gradients(z,[[1.,0.]],[1.]),.1)
        self.assertEqual((z['W'],z['b'],z['v']),([[0.,0.],[0.,0.]],[0.,0.],[0.,0.]))
        self.assertGreater(z['c'],0.)
        self.assertEqual(forward(z,[1,0])['probability'],forward(z,[-9,3])['probability'])

    def test_variance_reference(self):
        self.assertEqual(variance_factors(2,4),dict(weight_variance=Q(1,3),amplitude_squared=1,forward_factor=Q(2,3),backward_factor=Q(4,3)))
        self.assertEqual(variance_factors(4,1)['weight_variance'],Q(2,5))
        for i,o in product(range(1,9),repeat=2):
            d=variance_factors(i,o)
            self.assertEqual((d['forward_factor']+d['backward_factor'])/2,1)
            self.assertEqual(d['amplitude_squared']/3,d['weight_variance'])

    def test_variance_by_independent_enumeration(self):
        # Independent signs for weights and inputs: exact expectation, unit variances.
        for n in range(1,5):
            outputs=[]
            for signs in product((-1,1),repeat=2*n):
                outputs.append(sum(signs[i]*signs[n+i] for i in range(n)))
            mean=Q(sum(outputs),len(outputs))
            variance=sum((Q(v)-mean)**2 for v in outputs)/len(outputs)
            self.assertEqual(mean,0);self.assertEqual(variance,n)
            for out in (1,3,7):
                d=variance_factors(n,out)
                self.assertEqual(variance*d['weight_variance'],d['forward_factor'])
        # Correlated equal weights and equal inputs violate the product assumptions.
        correlated=[2*w*x for w,x in product((-1,1),repeat=2)]
        self.assertEqual(sum(v*v for v in correlated)/len(correlated),4)

    def test_existing_generator_and_contracts(self):
        for H,seed in product((1,4,16),(0,42,2**32-1)):
            a=initialize(H,seed);b=initialize(H,seed)
            self.assertEqual(a,b)
            self.assertTrue(all(abs(w)**2<=6/(2+H)+1e-12 for row in a['W'] for w in row))
            self.assertTrue(all(abs(v)**2<=6/(H+1)+1e-12 for v in a['v']))
        a=initialize(4,42);self.assertTrue(all(abs(w)<=1 for row in a['W'] for w in row))
        self.assertNotEqual(a,initialize(4,43))
        for i,o in [(0,1),(1,1001),(True,2),(1.,2)]:
            with self.assertRaises(ValueError):variance_factors(i,o)
        for out in [(1,),('1',2),(True,1),(float('inf'),1)]:
            with self.assertRaises(ValueError):paired(out)
