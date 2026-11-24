"""PA e PG: recorrência versus fórmula fechada, com frações exatas."""
from fractions import Fraction as Q
from itertools import product
import unittest


def data(kind,first,step,n):
    if kind not in ('pa','pg') or type(n) is not int or not 0<=n<=1000:
        raise ValueError('Tipo pa/pg e contagem inteira 0 <= n <= 1000')
    if any(isinstance(v,bool) or not isinstance(v,(int,Q)) for v in (first,step)):
        raise ValueError('Use int ou Fraction; sem float')
    return Q(first),Q(step)


def terms(kind,first,step,n):
    a,d=data(kind,first,step,n)
    result=[];value=a
    for _ in range(n):
        result.append(value)
        value=value+d if kind=='pa' else value*d
    return result


def nth(kind,first,step,n):
    a,d=data(kind,first,step,n)
    if n==0:raise ValueError('Índice do termo começa em 1')
    if n==1:return a
    return a+(n-1)*d if kind=='pa' else a*d**(n-1)


def total(kind,first,step,n):
    a,d=data(kind,first,step,n)
    if n==0:return Q(0)
    if kind=='pa':return n*(2*a+(n-1)*d)/2
    if d==1:return n*a
    return a*(1-d**n)/(1-d)


class Checks(unittest.TestCase):
    def test_closed_forms_against_recurrence(self):
        # 1470 prefixes, including zero initial term and negative/zero ratios.
        for kind,a,d,n in product(('pa','pg'),range(-2,3),
                                  (Q(-2),Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1),Q(2)),range(21)):
            seq=terms(kind,a,d,n)
            self.assertEqual(total(kind,a,d,n),sum(seq,Q(0)))
            if n:self.assertEqual(nth(kind,a,d,n),seq[-1])
            if n>1:
                self.assertTrue(all(y-x==d if kind=='pa' else y==d*x
                                    for x,y in zip(seq,seq[1:])))

    def test_original_examples_and_edge_cases(self):
        self.assertEqual(terms('pa',4,3,5),[4,7,10,13,16])
        self.assertEqual(total('pa',4,3,5),50)
        self.assertEqual(nth('pg',4,Q(3,2),5),Q(81,4))
        self.assertEqual(total('pg',4,Q(3,2),5),Q(211,4))
        self.assertEqual(terms('pg',7,0,4),[7,0,0,0])
        self.assertEqual(total('pg',7,1,4),28)
        self.assertEqual(nth('pg',6,Q(-1,2),4),Q(-3,4))
        self.assertEqual(8-total('pg',4,Q(1,2),4),Q(1,2))

    def test_sum_increment_and_finite_prefix(self):
        for kind,n in product(('pa','pg'),range(1,31)):
            self.assertEqual(total(kind,3,Q(-1,2),n)-total(kind,3,Q(-1,2),n-1),
                             nth(kind,3,Q(-1,2),n))
        def alternative(n):
            extra=1
            for j in range(1,6):extra*=n-j
            return nth('pa',4,3,n)+extra
        for n in range(1,6):self.assertEqual(alternative(n),nth('pa',4,3,n))
        self.assertEqual(alternative(6)-nth('pa',4,3,6),120)

    def test_contracts(self):
        for args in [('x',1,2,3),('pa',1,2,True),('pa',1,2,-1),
                     ('pg',1,2,1001),('pg',1,2.0,3),('pa',True,2,3)]:
            with self.assertRaises(ValueError):terms(*args)
        with self.assertRaises(ValueError):nth('pa',1,2,0)
        self.assertEqual(terms('pg',4,0,0),[])
        self.assertEqual(total('pg',4,1,0),0)


if __name__=='__main__':
    for kind,step in [('pa',Q(3)),('pg',Q(3,2))]:
        print(kind,terms(kind,4,step,5),'soma',total(kind,4,step,5))
    unittest.main()
