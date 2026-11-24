import unittest
from math import exp,factorial
from fractions import Fraction as Q
from itertools import product
from .walk import moments,run_means,trace

class Tests(unittest.TestCase):
    def test_original_fixture_and_observables(self):
        self.assertEqual(moments(5,4,1,1),dict(mean=15,variance=125))
        r=run_means(5,4,1,Q(1,2))
        self.assertEqual((r['lifetime'],r['net'],r['path'],r['steps']),(2,30,50,10))
        self.assertEqual(r['probabilities'],(Q(8,11),Q(2,11),Q(1,11)))
        self.assertEqual(trace(5,[1,1,-1,1]),dict(net=10,path=20,steps=4))
        self.assertEqual(moments(5,Q(5,2),Q(5,2),1),dict(mean=0,variance=125))
    def test_moments_vs_independent_poisson_enumeration(self):
        # Enumeração direta de N+ e N−,não usa fórmula de variância do código.
        mass=mean=second=0.
        for plus,minus in product(range(41),repeat=2):
            probability=exp(-5)*4**plus/factorial(plus)/factorial(minus)
            x=5*(plus-minus)
            mass+=probability;mean+=probability*x;second+=probability*x*x
        self.assertAlmostEqual(mass,1,places=12)
        model=moments(5,4,1,1)
        self.assertAlmostEqual(mean,float(model['mean']),places=10)
        self.assertAlmostEqual(second-mean*mean,float(model['variance']),places=9)
    def test_geometric_stopping_and_path_properties(self):
        r=run_means(5,4,1,Q(1,2));p=r['probabilities'][2];q=1-p;K=40
        mass=sum(p*q**n for n in range(K+1));truncated=sum(n*p*q**n for n in range(K+1))
        tail_expect=q**(K+1)*(K+1+q/p)
        self.assertEqual(mass+q**(K+1),1)
        self.assertEqual(truncated+tail_expect,r['steps'])
        for size in range(9):
            for signs in product([-1,1],repeat=size):
                z=trace(5,signs);self.assertLessEqual(abs(z['net']),z['path'])
                self.assertEqual(trace(5,[-s for s in signs])['net'],-z['net'])
        for d,a,b,c in [(2,3,1,1),(5,1,4,Q(1,2)),(1,0,2,3)]:
            x=run_means(d,a,b,c);reverse=run_means(d,b,a,c)
            self.assertEqual(reverse['net'],-x['net']);self.assertEqual(reverse['path'],x['path'])
            self.assertEqual(run_means(d,a,b,2*c)['lifetime'],x['lifetime']/2)
            self.assertEqual(moments(d,a,b,4)['variance'],4*moments(d,a,b,1)['variance'])
    def test_contracts(self):
        for args in [(0,4,1,1),(5,-1,1,1),(5,0,0,1),(5,4,1,0),(5,4,1,True),(5.,4,1,1)]:
            with self.assertRaises(ValueError):run_means(*args)
        for t in (-1,11,True,.5):
            with self.assertRaises(ValueError):moments(5,4,1,t)
        for signs in ([0],[True],[1.],[1]*101):
            with self.assertRaises(ValueError):trace(5,signs)
