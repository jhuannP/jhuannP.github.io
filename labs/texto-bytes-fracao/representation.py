"""Representações originais: UTF-8 por bits e frações de float.
Sem arquivos ou dados externos. Execução esperada no ambiente declarado.
"""
from fractions import Fraction as Q
from unicodedata import normalize
from math import nextafter, inf, isclose
import sys
import unittest


def scalar_utf8(cp):
    if type(cp) is not int or not 0 <= cp <= 0x10FFFF or 0xD800 <= cp <= 0xDFFF:
        raise ValueError('Valor escalar Unicode necessário')
    if cp < 0x80: return bytes([cp])
    if cp < 0x800: return bytes([0xC0|(cp>>6),0x80|(cp&63)])
    if cp < 0x10000: return bytes([0xE0|(cp>>12),0x80|((cp>>6)&63),0x80|(cp&63)])
    return bytes([0xF0|(cp>>18),0x80|((cp>>12)&63),0x80|((cp>>6)&63),0x80|(cp&63)])


def finite_binary(value):
    if type(value) is not Q: raise TypeError('Use Fraction reduzida automaticamente')
    denominator=value.denominator
    return denominator&(denominator-1)==0


class Checks(unittest.TestCase):
    def test_utf8_all_unicode_scalars(self):
        tested=0
        for cp in range(0x110000):
            if 0xD800 <= cp <= 0xDFFF: continue
            manual=scalar_utf8(cp)
            standard=chr(cp).encode('utf-8')
            if manual != standard or manual.decode('utf-8') != chr(cp):
                self.fail('Divergência no valor escalar '+hex(cp))
            tested+=1
        self.assertEqual(tested,1112064)
        print('Valores escalares conferidos:',tested)

    def test_bytes_decoding_and_replacement(self):
        self.assertEqual('é'.encode('utf-8'),bytes([0xC3,0xA9]))
        self.assertEqual('é'.encode('latin-1'),bytes([0xE9]))
        self.assertEqual(bytes([0xC3,0xA9]).decode('latin-1'),'Ã©')
        self.assertEqual(bytes([0xFF]).decode('utf-8',errors='replace'),'�')
        self.assertNotEqual('�'.encode('utf-8'),bytes([0xFF]))
        for b in range(256):
            raw=bytes([b])
            if b<128: self.assertEqual(raw.decode('utf-8'),chr(b))
            else:
                with self.assertRaises(UnicodeDecodeError):raw.decode('utf-8')

    def test_normalization_is_not_encoding(self):
        pre='é'; decomposed='e'+chr(0x301)
        self.assertEqual(len(pre),1);self.assertEqual(len(decomposed),2)
        self.assertEqual(len(pre.encode('utf-8')),2)
        self.assertEqual(len(decomposed.encode('utf-8')),3)
        self.assertNotEqual(pre.encode('utf-8'),decomposed.encode('utf-8'))
        self.assertEqual(normalize('NFC',decomposed),pre)
        with self.assertRaises(UnicodeEncodeError):chr(0xD800).encode('utf-8')

    def test_binary_fractions_and_float_spacing(self):
        self.assertEqual(sys.float_info.radix,2)
        self.assertEqual(sys.float_info.mant_dig,53)
        cases=0
        for numerator in range(-10,11):
            for denominator in range(1,33):
                value=Q(numerator,denominator)
                self.assertEqual(Q(float(value))==value,finite_binary(value))
                cases+=1
        self.assertEqual(cases,672)
        self.assertEqual(Q(.125),Q(1,8))
        self.assertEqual(.1.as_integer_ratio(),(3602879701896397,2**55))
        self.assertEqual(Q(.1)-Q('0.1'),Q(1,5*2**55))
        self.assertNotEqual(.1+.2,.3)
        self.assertTrue(isclose(.1+.2,.3,rel_tol=1e-12,abs_tol=1e-12))
        self.assertEqual(nextafter(float(2**53),inf)-float(2**53),2.)
        self.assertEqual(int(float(2**53+1)),2**53)
        self.assertEqual(int(float(2**53+2)),2**53+2)

    def test_scalar_domain(self):
        for cp in (-1,True,0xD800,0xDFFF,0x110000,65.0):
            with self.assertRaises(ValueError):scalar_utf8(cp)
        with self.assertRaises(TypeError):finite_binary(.1)


if __name__=='__main__':
    print('Python:',sys.version.split()[0],'; radix/mant_dig:',sys.float_info.radix,sys.float_info.mant_dig)
    unittest.main()
