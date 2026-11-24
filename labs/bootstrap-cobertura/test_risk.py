"""Oráculos por sequências de coleta e posições de reamostragem."""
import unittest
from fractions import Fraction as Q
from itertools import product
from math import ceil
from .risk import audit, interval, distribution


class CoverageTests(unittest.TestCase):
    def test_three_observations(self):
        r = audit(3, Q(1, 4))
        self.assertEqual(r['weights'], (Q(27,64), Q(27,64), Q(9,64), Q(1,64)))
        self.assertEqual(r['coverage'], Q(9,16))
        self.assertEqual(r['expected_width'], Q(9,16))
        self.assertEqual(audit(3,Q(1,2))['coverage'],Q(3,4))

    def test_bootstrap_positions(self):
        # 20 (n,k) pares; percentis por estatísticas de ordem, sem CDF binomial.
        for n in range(1,6):
            for k in range(n+1):
                data = [1]*k+[0]*(n-k)
                values = sorted(Q(sum(data[i] for i in indices),n)
                                for indices in product(range(n), repeat=n))
                for alpha in [Q(1,20), Q(1,5), Q(1,2)]:
                    lo = values[ceil(alpha*len(values)/2)-1]
                    hi = values[ceil((1-alpha/2)*len(values))-1]
                    self.assertEqual(interval(n,k,alpha), (lo,hi))

    def test_original_sampling_sequences(self):
        # 5 tamanhos x 21 parâmetros; sequências externas independentes do binômio.
        for n in range(1,6):
            for j in range(21):
                p = Q(j,20); total=Q(0); cover=Q(0); width=Q(0)
                for data in product([0,1],repeat=n):
                    w=Q(1)
                    for x in data: w *= p if x else 1-p
                    lo,hi=interval(n,sum(data));total+=w
                    cover+=w*(lo<=p<=hi);width+=w*(hi-lo)
                r=audit(n,p)
                self.assertEqual(total,1);self.assertEqual(r['coverage'],cover)
                self.assertEqual(r['expected_width'],width)

    def test_closed_form_and_boundary(self):
        for j in range(1,100):
            p=Q(j,100)
            self.assertEqual(audit(3,p)['coverage'],3*p*(1-p))
        self.assertEqual(audit(3,0)['coverage'],1)
        self.assertEqual(audit(3,1)['coverage'],1)
        self.assertEqual(audit(3,Q(1,1000))['coverage'],Q(2997,1000000))
        # Complementar 0/1 preserva a cobertura e espelha intervalos.
        for n in range(1,6):
            self.assertEqual(audit(n,Q(1,4))['coverage'],audit(n,Q(3,4))['coverage'])
            for k in range(n+1):
                lo,hi=interval(n,k); a,b=interval(n,n-k)
                self.assertEqual((a,b),(1-hi,1-lo))

    def test_contracts(self):
        for n in [0,6,True,3.0]:
            with self.assertRaises(ValueError): distribution(n,Q(1,4))
        for p in [-1,2,True,.25]:
            with self.assertRaises(ValueError): audit(3,p)
        for k in [-1,4,True,1.0]:
            with self.assertRaises(ValueError): interval(3,k)
        for alpha in [0,1,True,.05]:
            with self.assertRaises(ValueError): interval(3,1,alpha)
