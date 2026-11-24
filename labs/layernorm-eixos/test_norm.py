import unittest,random,math
from .norm import forward,backward

class NormTests(unittest.TestCase):
    def test_fixture_and_constant(self):
        s=forward([1,3],3)
        self.assertEqual(s['mean'],2);self.assertEqual(s['var'],1)
        self.assertEqual(s['z'],(-.5,.5))
        self.assertEqual(forward([1,3],3,[2,4],[1,0])['y'],(0,2))
        self.assertEqual(backward([1,3],[1,0],3)['dx'],(.1875,-.1875))
        self.assertEqual(forward([2,2],.1)['z'],(0,0))
        self.assertEqual(backward([2],[3],.1)['dx'],(0,))
    def test_invariants(self):
        for x in ([1,3],[2,-1,4],[1,2,4,8]):
            s=forward(x,.3)
            self.assertAlmostEqual(sum(s['z']),0)
            self.assertAlmostEqual(sum(v*v for v in s['z'])/len(x),s['var']/(s['var']+.3))
            for a in (1,2,3):
                q=forward([a*v+7 for v in x],a*a*.3)
                for z,w in zip(s['z'],q['z']):self.assertAlmostEqual(z,w)
            self.assertAlmostEqual(sum(backward(x,list(range(len(x))),.3)['dx']),0)
    def test_finite_difference_vjp(self):
        rng=random.Random(23)
        for n in range(2,6):
            for _ in range(10):
                x=[rng.uniform(-2,2) for _ in range(n)];u=[rng.uniform(-2,2) for _ in x]
                gamma=[rng.uniform(-1,2) for _ in x];beta=[rng.uniform(-1,1) for _ in x]
                g=backward(x,u,.2,gamma);h=1e-5
                def loss(a,c,d):return sum(v*w for v,w in zip(u,forward(a,.2,c,d)['y']))
                for key,values in [('dx',x),('dgamma',gamma),('dbeta',beta)]:
                    for j in range(n):
                        plus=values.copy();minus=values.copy();plus[j]+=h;minus[j]-=h
                        args1=[x,gamma,beta];args2=[x,gamma,beta];idx={'dx':0,'dgamma':1,'dbeta':2}[key]
                        args1[idx]=plus;args2[idx]=minus
                        fd=(loss(*args1)-loss(*args2))/(2*h)
                        self.assertAlmostEqual(fd,g[key][j],delta=1e-7)
    def test_contracts(self):
        for x,eps in [([],1),([True],1),([float('nan')],1),([1],0),([1],1e-15),([1e9],1)]:
            with self.assertRaises(ValueError):forward(x,eps)
        with self.assertRaises(ValueError):forward([1,2],1,gamma=[1])
        with self.assertRaises(ValueError):backward([1,2],[1],1)
