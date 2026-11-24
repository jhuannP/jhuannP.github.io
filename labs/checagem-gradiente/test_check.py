from copy import deepcopy
import unittest
from .check import central,directional,compare
import dense_net as net

def quartic(t):
    a,b=t;return a**4/4+a*b+b*b/2

def grad(t):
    a,b=t;return (a**3+b,a+b)

class GradientChecks(unittest.TestCase):
    def test_quartic_exact_error_pattern(self):
        for point in ((1,2),(-2,1),(.5,-1)):
            for h in (.1,.01,.001):
                actual=central(quartic,point,h);truth=grad(point)
                self.assertAlmostEqual(actual[0],truth[0]+point[0]*h*h,delta=2e-10)
                self.assertAlmostEqual(actual[1],truth[1],delta=2e-10)
        self.assertAlmostEqual(central(quartic,(1,2),.1)[0]-3,.01,places=12)

    def test_all_network_parameters_and_missing_terms(self):
        X=[[.2,-.7],[.9,.3],[-.4,.8]];y=[0,1,1]
        for H,seed in ((2,42),(4,43)):
            model=net.initialize(H,seed);snapshot=deepcopy(model)
            paths=[('W',j,k) for j in range(H) for k in range(2)]+[(key,j) for key in ('b','v') for j in range(H)]+[('c',)]
            def get(m,p):
                for key in p:m=m[key]
                return m
            def unpack(theta):
                m=deepcopy(model)
                for path,value in zip(paths,theta):
                    node=m
                    for key in path[:-1]:node=node[key]
                    node[path[-1]]=value
                return m
            theta=tuple(get(model,p) for p in paths)
            for lam in (0,.07):
                objective=lambda t:net.loss(unpack(t),X,y,lam)
                analytic=tuple(get(net.gradients(model,X,y,lam),p) for p in paths)
                for h in (1e-4,1e-5,1e-6):
                    self.assertTrue(all(r['passed'] for r in compare(objective,theta,analytic,h,atol=1e-7,rtol=1e-4)))
                # Controlled fault: sum instead of mean of the data gradient.
                data=tuple(get(net.gradients(model,X,y,0),p) for p in paths)
                wrong=tuple(a+2*d for a,d in zip(analytic,data))
                self.assertTrue(any(not r['passed'] for r in compare(objective,theta,wrong)))
                if lam:
                    self.assertTrue(any(not r['passed'] for r in compare(objective,theta,data)))
            self.assertEqual(model,snapshot)

    def test_one_direction_can_hide_a_wrong_gradient(self):
        theta=(1,2);wrong=(4,2);h=1e-4
        self.assertAlmostEqual(directional(quartic,theta,(1,1),h),sum(wrong),delta=2e-8)
        self.assertFalse(all(r['passed'] for r in compare(quartic,theta,wrong,h)))
        self.assertAlmostEqual(directional(quartic,theta,(1,0),h),3,delta=2e-8)

    def test_nonsmooth_and_loss_rounding(self):
        relu=lambda t:max(t[0],0)
        self.assertEqual(central(relu,(0,),.1),(0.5,))
        self.assertEqual(central(relu,(0,),.01),(0.5,))
        shifted=lambda t:1e20+quartic(t)
        self.assertEqual(central(shifted,(1,2),1e-5),(0,0))
        self.assertFalse(all(r['passed'] for r in compare(shifted,(1,2),(3,3))))
        self.assertTrue(all(r['passed'] for r in compare(quartic,(0,0),(0,0))))

    def test_contracts_and_state(self):
        theta=[1,2];before=theta[:];central(quartic,theta,.01);self.assertEqual(theta,before)
        for bad in (0,-1,True,float('nan')):
            with self.assertRaises(ValueError):central(quartic,(1,2),bad)
        with self.assertRaises(ValueError):central(quartic,(),.01)
        with self.assertRaises(ValueError):compare(quartic,(1,2),(3,))
        with self.assertRaises(ValueError):compare(quartic,(1,2),(3,3),atol=-1)
        with self.assertRaises(ValueError):directional(quartic,(1,2),(0,0),.01)
        with self.assertRaises(ArithmeticError):central(lambda t:t[0]**2,(1e20,),1e-6)
        with self.assertRaises(ValueError):central(lambda t:float('inf'),(1,),.01)
        with self.assertRaises(ValueError):central(lambda t:0,(0,),1e308)
        with self.assertRaises(ValueError):compare(lambda t:-1e308*t[0],(0,),(1e308,),h=1e-6)

if __name__=='__main__':unittest.main()
