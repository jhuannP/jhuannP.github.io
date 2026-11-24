"""Modelo combinacional booleano; sem estado, tensão, ruído ou atraso físico."""
from itertools import product
import unittest


def bit(x):
    if type(x) is not int or x not in (0,1):
        raise ValueError('Bit inteiro0/1; bool e float rejeitados')
    return x


def half(a,b):
    a,b=map(bit,(a,b))
    return a^b,a&b  # Order is S,C; binary word is CS.


def full(a,b,carry):
    a,b,carry=map(bit,(a,b,carry))
    first,c1=half(a,b)
    result,c2=half(first,carry)
    return result,c1|c2


def ripple(a,b,carry=0):
    if not isinstance(a,(list,tuple)) or not isinstance(b,(list,tuple)) or len(a)!=len(b):
        raise ValueError('Duas listas/tuplas de mesmo tamanho')
    a,b=[bit(x) for x in a],[bit(x) for x in b]
    carry=bit(carry)
    output=[]
    for x,y in zip(a,b):
        s,carry=full(x,y,carry)
        output.append(s)
    return output+[carry]


def value(bits):
    return sum(bit(x)*(2**i) for i,x in enumerate(bits))


class Checks(unittest.TestCase):
    def test_half_and_truth_identities(self):
        for a,b in product((0,1),repeat=2):
            s,c=half(a,b)
            self.assertEqual(a+b,s+2*c)
            self.assertEqual(s,(a*(1-b))|((1-a)*b))
            self.assertEqual(1-(a&b),(1-a)|(1-b))
            self.assertEqual(1-(a|b),(1-a)&(1-b))
        self.assertEqual(half(1,1),(0,1))
        self.assertEqual(~0,-1)

    def test_full_eight_cases(self):
        for a,b,carry in product((0,1),repeat=3):
            s,c=full(a,b,carry)
            total=a+b+carry
            self.assertEqual((s,c),(total%2,total//2))
            majority=int(total>=2)
            self.assertEqual(c,majority)
            self.assertEqual(s,a^b^carry)
        self.assertEqual(full(1,1,1),(1,1))

    def test_four_bit_exhaustive(self):
        for a,b,carry in product(range(16),range(16),(0,1)):
            aa=[(a>>i)&1 for i in range(4)]
            bb=[(b>>i)&1 for i in range(4)]
            result=ripple(aa,bb,carry)
            self.assertEqual(len(result),5)
            self.assertEqual(value(result),a+b+carry)
            self.assertEqual(value(result[:4]),(a+b+carry)%16)
        self.assertEqual(ripple([1,1,0,0],[1,0,1,0]),[0,0,0,1,0])
        self.assertEqual(ripple([],[],1),[1])

    def test_contracts(self):
        for x in (True,False,0.,1.,-1,2,'1',None):
            with self.assertRaises(ValueError):half(x,0)
            with self.assertRaises(ValueError):full(0,0,x)
        for a,b in (([1],[1,0]),('1',[1]),([True],[0]),([1.],[0])):
            with self.assertRaises(ValueError):ripple(a,b)


if __name__=='__main__':
    for a,b in product((0,1),repeat=2):print('A,B:',a,b,'S,C:',half(a,b))
    unittest.main()
