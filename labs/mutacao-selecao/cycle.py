"""Modelo haploide didático, probabilidades racionais e distribuição de um passo."""
from fractions import Fraction as Q
from itertools import product
from math import comb
import unittest


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use int ou Fraction exatos')
    return Q(x)


def cycle(p,s,mu):
    p,s,mu=map(rational,(p,s,mu))
    if not (0<=p<=1 and s>=0 and 0<=mu<=1):
        raise ValueError('p e mu em [0,1]; s >= 0')
    selected=(1+s)*p/(1+s*p)
    return selected,(1-mu)*selected


def offspring(m,p,s,mu):
    if type(m) is not int or not 1<=m<=20:
        raise ValueError('1 <= M <= 20 inteiro')
    _,q=cycle(p,s,mu)
    return [comb(m,k)*q**k*(1-q)**(m-k) for k in range(m+1)]


class Checks(unittest.TestCase):
    def test_example_and_order(self):
        self.assertEqual(cycle(Q(1,4),1,Q(1,4)),(Q(2,5),Q(3,10)))
        first_mutation=Q(3,16)
        swapped=cycle(first_mutation,1,0)[1]
        self.assertEqual(swapped,Q(6,19))
        self.assertNotEqual(swapped,Q(3,10))
        dist=offspring(4,Q(1,4),1,Q(1,4))
        self.assertEqual(dist[0],Q(2401,10000))

    def test_fixed_points_and_difference(self):
        for s,mu in product((Q(1,2),Q(1),Q(2)),(Q(0),Q(1,4),Q(1,2),Q(1))):
            self.assertEqual(cycle(0,s,mu)[1],0)
            star=1-mu*(1+s)/s
            if star>0:self.assertEqual(cycle(star,s,mu)[1],star)
            for p in (Q(k,10) for k in range(11)):
                f=cycle(p,s,mu)[1]
                self.assertEqual(f-p,p*(s-mu*(1+s)-s*p)/(1+s*p))
                self.assertTrue(0<=f<=1)
        self.assertEqual(cycle(Q(1,3),0,Q(1,4))[1],Q(1,4))

    def test_selection_by_weighted_counts(self):
        # Independently normalize contributions of an explicit initial census.
        for a,b in product(range(9),repeat=2):
            if a+b:
                selected=cycle(Q(a,a+b),1,0)[0]
                contributions=[2]*a+[1]*b
                self.assertEqual(selected,Q(sum(contributions[:a]),sum(contributions)))

    def test_binomial_against_enumeration_and_moments(self):
        for p,s,mu in product((Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)),
                              (Q(0),Q(1,2),Q(1)),(Q(0),Q(1,4),Q(1,2),Q(1))):
            q=cycle(p,s,mu)[1]
            for m in range(1,7):
                enumerated=[Q(0)]*(m+1)
                for bits in product((0,1),repeat=m):
                    weight=Q(1)
                    for bit in bits:weight*=q if bit else 1-q
                    enumerated[sum(bits)]+=weight
                dist=offspring(m,p,s,mu)
                self.assertEqual(dist,enumerated)
                self.assertEqual(sum(dist),1)
                mean=sum(Q(k,m)*v for k,v in enumerate(dist))
                variance=sum((Q(k,m)-q)**2*v for k,v in enumerate(dist))
                self.assertEqual(mean,q)
                self.assertEqual(variance,q*(1-q)/m)

    def test_contracts(self):
        for p,s,mu in [(True,1,0),(.5,1,0),(2,1,0),(0,-1,0),(0,1,2)]:
            with self.assertRaises(ValueError):cycle(p,s,mu)
        for m in (True,0,21,2.0):
            with self.assertRaises(ValueError):offspring(m,Q(1,4),1,Q(1,4))


if __name__=='__main__':
    print('Selecionada e após mutação:',cycle(Q(1,4),1,Q(1,4)))
    print('P(K=k), M=4:',offspring(4,Q(1,4),1,Q(1,4)))
    unittest.main()
