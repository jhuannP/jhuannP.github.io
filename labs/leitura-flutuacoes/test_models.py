import unittest
from fractions import Fraction as F
from itertools import product
from .models import independent,families,moments

class FluctuationTests(unittest.TestCase):
    def test_fixtures(self):
        a,b=independent(),families()
        self.assertEqual(moments(a),(F(15,8),F(105,64)))
        self.assertEqual(moments(b),(F(15,8),F(595,64)))
        self.assertEqual(b[0],F(2401,4096));self.assertEqual(sum(b[8:]),F(1,8))
        self.assertGreater(sum(b[8:]),sum(a[8:]))

    def test_enumeration(self):
        # Oracle separado: todos os resultados das moedas, sem convolução.
        for weights in ((1,2,4,8),(1,1,2),(2,3),(3,)):
            for p in (F(0),F(1,8),F(1,2),F(1)):
                expected=[F(0)]*(sum(weights)+1)
                for bits in product((0,1),repeat=len(weights)):
                    prob=F(1)
                    for bit in bits:prob*=p if bit else 1-p
                    expected[sum(w*b for w,b in zip(weights,bits))]+=prob
                self.assertEqual(families(weights,p),tuple(expected))

    def test_general_moments(self):
        for n in range(1,16):
            for p in (F(0),F(1,8),F(1,3),F(1)):
                self.assertEqual(moments(independent(n,p)),(n*p,n*p*(1-p)))
                self.assertEqual(families((1,)*n,p),independent(n,p))
        for weights in ((1,2,4,8),(2,2,3),(1,5)):
            for p in (F(1,8),F(1,2)):
                self.assertEqual(moments(families(weights,p)),(sum(weights)*p,sum(w*w for w in weights)*p*(1-p)))

    def test_heterogeneity(self):
        a=independent(15,F(0));b=independent(15,F(1,4))
        mixture=tuple((x+y)/2 for x,y in zip(a,b))
        self.assertEqual(moments(mixture),(F(15,8),F(315,64)))

    def test_contracts(self):
        for p in (True,-1,F(9,8),0.5):
            with self.assertRaises(ValueError):families(p=p)
        for w in ((),(0,),(True,),(101,)):
            with self.assertRaises(ValueError):families(w)
        for n in (0,31,True,1.5):
            with self.assertRaises(ValueError):independent(n)
        for law in ((),(F(1,2),),(F(-1),F(2)),(True,)):
            with self.assertRaises(ValueError):moments(law)
