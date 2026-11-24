"""Primeiros índices exatos para dois erros conhecidos; não detecta limites gerais."""
from fractions import Fraction as Q
from math import floor,ceil
import sys
import unittest


def tolerance(eps):
    if isinstance(eps,bool) or not isinstance(eps,(int,Q)) or eps<=0:
        raise ValueError('Tolerância racional positiva')
    return Q(eps)


def error(n):
    if isinstance(n,bool) or not isinstance(n,int) or n<1:
        raise ValueError('Índice inteiro >=1')
    return Q(1,n+1)


def first_index(eps,strict=True):
    eps=tolerance(eps)
    if not isinstance(strict,bool):raise ValueError('Comparador booleano')
    return max(1,floor(1/eps) if strict else ceil(1/eps)-1)


class Checks(unittest.TestCase):
    def test_minimal_indices_and_sampled_tails(self):
        for p in range(1,21):
            for q in range(1,21):
                eps=Q(p,q)
                for strict in (False,True):
                    n=first_index(eps,strict)
                    compare=(lambda e:e<eps) if strict else (lambda e:e<=eps)
                    self.assertTrue(all(compare(error(k)) for k in range(n,n+30)))
                    if n>1:self.assertFalse(compare(error(n-1)))
        self.assertEqual(first_index(Q(1,10)),10)
        self.assertEqual(first_index(Q(1,10),False),9)
        self.assertEqual(first_index(Q(3,20)),6)

    def test_recurrence_and_monotonicity(self):
        d=Q(1,2)
        for n in range(1,71):
            self.assertEqual(d,1-Q(1,2**n))
            self.assertLess(d,1)
            next_d=(d+1)/2
            self.assertGreater(next_d,d)
            self.assertEqual(next_d-d,(1-d)/2)
            d=next_d
            self.assertEqual(Q(n+1,n+2)-Q(n,n+1),Q(1,(n+1)*(n+2)))

    def test_oscillation_and_prefix(self):
        M=20
        prefix=lambda n:Q(n,n+1) if n<=M else Q((-1)**n)
        self.assertEqual([prefix(n) for n in range(1,M+1)],
                         [Q(n,n+1) for n in range(1,M+1)])
        self.assertEqual(prefix(22),1)
        self.assertEqual(prefix(23),-1)
        for n in range(1,101):
            self.assertEqual(abs(Q((-1)**n,n)),Q(1,n))
        self.assertEqual(floor(1/Q(1,10))+1,11)

    def test_float_cancellation(self):
        if (sys.float_info.radix,sys.float_info.mant_dig)!=(2,53):
            self.skipTest('Exemplo específico de float binário com53 bits')
        n=2**54
        exact=error(n)
        rounded=n/(n+1)
        self.assertGreater(exact,0)
        self.assertEqual(rounded,1.)
        self.assertEqual(1-rounded,0.)
        self.assertGreater(1/(n+1),0.)
        print('Formato float:',sys.float_info.radix,sys.float_info.mant_dig,
              'erro exato:',exact,'erro por subtração:',1-rounded)

    def test_contracts(self):
        for eps in (0,-1,True,.1,'1/10'):
            with self.assertRaises(ValueError):first_index(eps)
        for n in (0,-1,True,1.5):
            with self.assertRaises(ValueError):error(n)
        with self.assertRaises(ValueError):first_index(Q(1,10),'strict')


if __name__=='__main__':
    unittest.main()
