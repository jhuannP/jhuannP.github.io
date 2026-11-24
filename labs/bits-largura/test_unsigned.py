import unittest
from .unsigned import encode,decode,wrap,pack16,unpack16

class UnsignedTests(unittest.TestCase):
    def test_bijection_all_words_to_ten_bits(self):
        count=0
        for w in range(1,11):
            seen=set()
            for n in range(2**w):
                bits=encode(n,w)
                self.assertEqual(bits,format(n,'0'+str(w)+'b'))
                self.assertEqual(len(bits),w);self.assertEqual(decode(bits),n)
                weighted=sum(int(bit)*2**i for i,bit in enumerate(reversed(bits)))
                self.assertEqual(weighted,n);seen.add(bits);count+=1
            self.assertEqual(len(seen),2**w)
        self.assertEqual(count,2046)

    def test_range_padding_and_modular_loss(self):
        self.assertEqual(encode(46),'00101110')
        self.assertEqual(decode('00001101'),13)
        self.assertEqual(decode('11111111'),255)
        self.assertEqual(format(300,'08b'),'100101100')
        with self.assertRaises(ValueError):encode(300)
        self.assertEqual(wrap(300),44);self.assertEqual(wrap(44),44)
        self.assertEqual(wrap(-1),255)
        for n in range(-100,400):
            self.assertEqual(wrap(n),n&255)
            self.assertEqual(wrap(n+256),wrap(n))

    def test_byte_orders_against_standard_library(self):
        for n in range(65536):
            for order in ('big','little'):
                packed=pack16(n,order)
                self.assertEqual(packed,n.to_bytes(2,order,signed=False))
                self.assertEqual(unpack16(packed,order),n)
        self.assertEqual(pack16(300,'big'),bytes([1,44]))
        self.assertEqual(pack16(300,'little'),bytes([44,1]))
        self.assertEqual(unpack16(bytes([44,1]),'big'),11265)

    def test_zero_extension_and_capacity(self):
        for n in range(256):
            self.assertEqual(encode(n,16),'00000000'+encode(n,8))
            self.assertEqual(decode(encode(n,16)),n)
        self.assertLess(2**8,300);self.assertLessEqual(300,2**9)
        for w in range(1,17):self.assertEqual(decode('1'*w),2**w-1)

    def test_contracts(self):
        for n,w in [(256,8),(-1,8),(1,0),(1,17)]:
            with self.assertRaises(ValueError):encode(n,w)
        for n,w in [(True,8),(1.,8),(1,True)]:
            with self.assertRaises(TypeError):encode(n,w)
        for bits in ['', '0b1','01 1','2','１','1'*17]:
            with self.assertRaises(ValueError):decode(bits)
        with self.assertRaises(TypeError):decode(1)
        for args in [(65536,'big'),(-1,'big'),(1,'other')]:
            with self.assertRaises(ValueError):pack16(*args)
        for data in [b'',b'123',[1,2]]:
            with self.assertRaises(ValueError):unpack16(data)

if __name__=='__main__':unittest.main()
