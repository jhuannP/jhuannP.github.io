import unittest
from copy import deepcopy
from fractions import Fraction as Q
import dense_net as net
from .experiment import breakdown,fixture,two_paths

def coordinates(model):
    return [('W',j,k) for j in range(len(model['W'])) for k in range(2)]+[('b',j,None) for j in range(len(model['b']))]+[('v',j,None) for j in range(len(model['v']))]+[('c',None,None)]
def get(model,key):
    name,j,k=key
    return model[name] if j is None else model[name][j] if k is None else model[name][j][k]
def perturb(model,key,amount):
    a=deepcopy(model);name,j,k=key
    if j is None:a[name]+=amount
    elif k is None:a[name][j]+=amount
    else:a[name][j][k]+=amount
    return a

class BackpropBreakdownTests(unittest.TestCase):
    def test_exact_origin_example_and_no_mutation(self):
        m=fixture();old=deepcopy(m);s=breakdown(m,[[1,2],[-1,1]],[1,0])
        self.assertEqual([v['delta'] for v in s['records']],[-.25,.25])
        self.assertEqual(s['gradient'],dict(W=[[-1.,-.5],[.5,.25]],b=[0.,0.],v=[0.,0.],c=0.))
        self.assertEqual(m,old)
    def test_all_parameters_against_finite_differences(self):
        m=dict(W=[[.2,-.3],[.4,.1]],b=[.1,-.2],v=[.7,-.9],c=.05)
        X=[[1,2],[-1,1],[.5,-.25]];y=[1,0,1];h=1e-5
        for lam in (0,.03):
            g=breakdown(m,X,y,lam)['gradient']
            for key in coordinates(m):
                fd=(net.loss(perturb(m,key,h),X,y,lam)-net.loss(perturb(m,key,-h),X,y,lam))/(2*h)
                self.assertAlmostEqual(get(g,key),fd,delta=2e-9)
    def test_batch_reduction_and_penalty_once(self):
        X=[[1,2],[-1,1],[.5,-.25]];y=[1,0,1]
        for H in (1,2,3):
            m=net.initialize(H,42)
            for lam in (0,.1):
                g=breakdown(m,X,y,lam)['gradient'];repeat=breakdown(m,X+X,y+y,lam)['gradient']
                expected=net.gradients(m,X,y,lam)
                for key in coordinates(m):
                    self.assertAlmostEqual(get(g,key),get(repeat,key),delta=1e-12)
                    self.assertAlmostEqual(get(g,key),get(expected,key),delta=1e-12)
        a=breakdown(fixture(),[[1,2],[-1,1]],[1,0],.5)['gradient']
        self.assertEqual(a['v'],[1.,-.5]);self.assertEqual(a['b'],[0.,0.]);self.assertEqual(a['c'],0.)
    def test_shared_paths_by_exact_symmetric_difference(self):
        for u in (-2,-1,0,1,2):
            for h in (Q(1),Q(1,2),Q(1,10)):
                f=lambda x:x*x+3*x
                fd=(f(u+h)-f(u-h))/(2*h)
                self.assertEqual(fd,two_paths(u)['dz_du'])
        self.assertEqual(two_paths(2),dict(r=4,s=6,z=10,dz_du=7))
    def test_contracts_and_consistency(self):
        with self.assertRaises(ValueError):two_paths(True)
        for X,y,lam in [([],[],0),([[1,2]],[2],0),([[1]],[0],0),([[1,2]],[0],-1)]:
            with self.assertRaises(ValueError):breakdown(fixture(),X,y,lam)
