import unittest
from itertools import product
from .experiment import model

class TwosTests(unittest.TestCase):
    def test_all_words_against_modular_arithmetic(self):
        for a,b in product(range(16),repeat=2):
            r=model(a,b)
            self.assertEqual(r['result'],(a+b)%16)
            self.assertEqual(r['carry'],(a+b)//16)
            self.assertEqual(r['result_signed'],r['result']-16 if r['result']>=8 else r['result'])
            if not r['overflow']:self.assertEqual(r['result_signed'],r['exact'])
            self.assertEqual((r['result_signed']-r['exact'])%16,0)

    def test_overflow_three_independent_criteria(self):
        for a,b in product(range(16),repeat=2):
            r=model(a,b)
            same_sign=(a>=8)==(b>=8)
            changed_sign=(r['result']>=8)!=(a>=8)
            self.assertEqual(r['overflow'],same_sign and changed_sign)
            self.assertEqual(r['overflow'],bool(r['carries'][3]^r['carries'][4]))
            self.assertEqual(r['overflow'],not -8<=r['exact']<=7)

    def test_negation_and_flag_cases(self):
        for u in range(16):
            opposite=((u^15)+1)%16
            self.assertEqual((u+opposite)%16,0)
        self.assertEqual(((8^15)+1)%16,8) # -(-8) não cabe em quatro bits.
        for a,b,carry,overflow in ((7,1,0,True),(15,1,1,False),(8,8,1,True),(1,1,0,False)):
            r=model(a,b);self.assertEqual((r['carry'],r['overflow']),(carry,overflow))

    def test_contract(self):
        for x in (True,None,-1,16,1.,'7'):
            with self.assertRaises(ValueError):model(x,1)
            with self.assertRaises(ValueError):model(1,x)
