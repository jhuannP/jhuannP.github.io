import unittest
from fractions import Fraction as Q
from itertools import product
from .exchange import coordinates,exchange,det

class ExchangeTests(unittest.TestCase):
    def test_fixture(self):
        old=((1,1),(1,-1));new,alpha=exchange(old,(3,1),0)
        self.assertEqual(alpha,(2,1));self.assertEqual(det(old),-2);self.assertEqual(det(new),-4)
        self.assertEqual(coordinates(new,old[0]),(Q(1,2),-Q(1,2)))
        with self.assertRaises(ValueError):exchange(old,old[1],0)

    def test_integer_bases_and_coefficients(self):
        checked=0
        for a,b,c,d in product(range(-1,2),repeat=4):
            old=((a,b),(c,d));delta=a*d-b*c
            if not delta:continue
            for u,w in product(range(-2,3),repeat=2):
                v=(u*a+w*c,u*b+w*d)
                self.assertEqual(coordinates(old,v),(u,w))
                for j in (0,1):
                    coeff=(u,w)[j]
                    if not coeff:
                        with self.assertRaises(ValueError):exchange(old,v,j)
                        continue
                    new,alpha=exchange(old,v,j)
                    self.assertEqual(det(new),coeff*delta)
                    # Reconstrução escalar das duas colunas originais na nova família.
                    for target in old:
                        r,s=coordinates(new,target)
                        self.assertEqual((r*new[0][0]+s*new[1][0],r*new[0][1]+s*new[1][1]),target)
                    checked+=1
        self.assertEqual(checked,1920)

    def test_fractional_example(self):
        old=((Q(1,2),1),(1,Q(-1,3)));v=(Q(7,3),Q(-2,9))
        for j in (0,1):
            new,alpha=exchange(old,v,j)
            self.assertEqual(alpha,(Q(10,21),Q(44,21)))
            self.assertNotEqual(det(new),0)

    def test_contracts(self):
        for old,v,j in ((((1,2),(2,4)),(1,1),0),(((1,0),(0,1)),(True,1),0),(((1,0),(0,1)),(1.0,1),0),(((1,0),(0,1)),(1,1),True),(((1,0),(0,1)),(1,1),2)):
            with self.assertRaises(ValueError):exchange(old,v,j)
