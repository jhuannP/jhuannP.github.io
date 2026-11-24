"""Seleção combinacional ideal, com tabelas finitas completas."""
from itertools import product
import unittest
from base import bit, mux, decodificar_endereco


def mux4(values,s1,s0):
    if len(values)!=4:raise ValueError('Quatro entradas')
    d0,d1,d2,d3=map(bit,values);s1,s0=map(bit,(s1,s0))
    return mux(mux(d0,d1,s0),mux(d2,d3,s0),s1)


def mux4_decode(values,s1,s0):
    if len(values)!=4:raise ValueError('Quatro entradas')
    values=tuple(map(bit,values));s1,s0=map(bit,(s1,s0))
    lines=decodificar_endereco(2*s1+s0)
    result=0
    for line,value in zip(lines,values):result|=line&value
    return result


def mux_word(a,b,s):
    if any(type(x) is not int for x in (a,b,s)):
        raise ValueError('Inteiros nativos')
    if not 0<=a<16 or not 0<=b<16:raise ValueError('Palavras de quatro bits')
    s=bit(s);mask=(-s)&15
    return ((~mask)&a)|(mask&b)


class Checks(unittest.TestCase):
    def test_mux2_full_truth_table(self):
        for a,b,s in product((0,1),repeat=3):
            self.assertEqual(mux(a,b,s),a if s==0 else b)

    def test_decoder_and_enable(self):
        for address,en in product(range(4),(0,1)):
            lines=decodificar_endereco(address,en)
            self.assertEqual(lines,[int(en==1 and i==address) for i in range(4)])
            self.assertEqual(sum(lines),en)

    def test_mux4_compositions(self):
        for values in product((0,1),repeat=4):
            for s1,s0 in product((0,1),repeat=2):
                reference=values[2*s1+s0]
                self.assertEqual(mux4(values,s1,s0),reference)
                self.assertEqual(mux4_decode(values,s1,s0),reference)

    def test_four_bit_words(self):
        for a,b,s in product(range(16),range(16),(0,1)):
            reference=a if s==0 else b
            self.assertEqual(mux_word(a,b,s),reference)
            assembled=sum(mux((a>>j)&1,(b>>j)&1,s)<<j for j in range(4))
            self.assertEqual(assembled,reference)
        self.assertNotEqual(1&12,mux_word(3,12,1))

    def test_contracts(self):
        for bad in (True,False,1.0,0.0,-1,2,'1'):
            with self.assertRaises(ValueError):mux(0,1,bad)
        for bad in (True,1.0,-1,4,'2'):
            with self.assertRaises(ValueError):decodificar_endereco(bad)
        for a,b,s in [(16,0,0),(0,-1,0),(0,0,2),(True,0,1),(0,0,1.0)]:
            with self.assertRaises(ValueError):mux_word(a,b,s)
        with self.assertRaises(ValueError):mux4([0,1],0,0)


if __name__=='__main__':unittest.main()
