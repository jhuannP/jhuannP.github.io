import unittest
from fractions import Fraction as Q
from itertools import product
from .chain import matrix,history,summary

class FiniteTests(unittest.TestCase):
    def test_literal_and_mean_closure_failure(self):
        laws=history(4,1,Q(1,4),(0,1,0,0,0),2)
        self.assertEqual(laws[1],tuple(Q(x,10000) for x in [2401,4116,2646,756,81]))
        self.assertEqual(summary(laws[1])['mean'],Q(3,10))
        self.assertEqual(summary(laws[2])['mean'],Q(62091,200000))
        plug_in=Q(9,26)
        self.assertGreater(plug_in,summary(laws[2])['mean'])
        self.assertNotEqual(laws[2],tuple(__import__('math').comb(4,k)*plug_in**k*(1-plug_in)**(4-k) for k in range(5)))

    def test_two_generations_by_microhistories(self):
        # Caminhos de bits completos e contribuições explicitadas, não produto matricial.
        for m,s,mu in product(range(1,5),[Q(0),Q(1)],[Q(0),Q(1,4)]):
            start=1;initial=[0]*(m+1);initial[start]=1
            def pool(i):
                weights=[1+s]*i+[Q(1)]*(m-i)
                return (1-mu)*sum(weights[:i])/sum(weights)
            q1=pool(start);expected=[Q(0)]*(m+1)
            for first in product((0,1),repeat=m):
                p1=Q(1)
                for bit in first:p1*=q1 if bit else 1-q1
                q2=pool(sum(first))
                for second in product((0,1),repeat=m):
                    p2=p1
                    for bit in second:p2*=q2 if bit else 1-q2
                    expected[sum(second)]+=p2
            self.assertEqual(history(m,s,mu,initial,2)[2],tuple(expected))

    def test_conditional_moments_and_total_variance(self):
        m=4;s=Q(1);mu=Q(1,4);T=matrix(m,s,mu)
        law=history(m,s,mu,(0,1,0,0,0),1)[1]
        qs=[(1-mu)*(1+s)*Q(i,m)/(1+s*Q(i,m)) for i in range(m+1)]
        for i,row in enumerate(T):
            z=summary(row);self.assertEqual(sum(row),1)
            self.assertEqual(z['mean'],qs[i]);self.assertEqual(z['variance'],qs[i]*(1-qs[i])/m)
        mean=sum(law[i]*qs[i] for i in range(m+1))
        conditional_noise=sum(law[i]*qs[i]*(1-qs[i])/m for i in range(m+1))
        between=sum(law[i]*(qs[i]-mean)**2 for i in range(m+1))
        self.assertEqual(summary(history(m,s,mu,law,1)[1])['variance'],conditional_noise+between)
        self.assertGreater(between,0)

    def test_absorption_bound_first_loss_and_survivors(self):
        for m,s,mu in product(range(1,7),[Q(0),Q(1)],[Q(1,4),Q(1,2),Q(1)]):
            initial=[0]*(m+1);initial[m]=1;T=matrix(m,s,mu)
            self.assertEqual(T[0],tuple([1]+[0]*m));self.assertLess(T[m][m],1)
            for row in T:self.assertGreaterEqual(row[0],mu**m)
            laws=history(m,s,mu,initial,6)
            for t in range(1,7):
                z=summary(laws[t]);before=laws[t-1]
                self.assertLessEqual(z['survival'],(1-mu**m)**t)
                self.assertGreaterEqual(z['loss_cdf'],before[0])
                # Incremento deCDF é primeiro ingresso emzero porquezero absorve.
                self.assertEqual(z['loss_cdf']-before[0],sum(before[i]*T[i][0] for i in range(1,m+1)))
                if z['survival']:self.assertEqual(z['mean'],z['survival']*z['survivor_mean'])
                else:self.assertIsNone(z['survivor_mean'])

    def test_neutral_boundaries_and_steps(self):
        for m in [1,2,4,8]:
            T=matrix(m,0,0);self.assertEqual(T[-1][-1],1)
            law=[Q(0)]*(m+1);law[1]=1
            for d in history(m,0,0,law,4):self.assertEqual(summary(d)['mean'],Q(1,m))
            self.assertEqual(history(m,0,0,law,0),(tuple(law),))

    def test_contracts(self):
        for args in [(0,1,Q(1,4)),(9,1,0),(True,1,0),(4,11,0),(4,-1,0),(4,1,2),(4,.5,0)]:
            with self.assertRaises(ValueError):matrix(*args)
        for initial in [(0,1),(-1,2,0,0,0),(0,0,0,0,0),(0,.5,.5,0,0)]:
            with self.assertRaises(ValueError):history(4,1,Q(1,4),initial,1)
        for steps in [-1,21,True,1.]:
            with self.assertRaises(ValueError):history(4,1,Q(1,4),(0,1,0,0,0),steps)
        with self.assertRaises(ValueError):summary([1])
