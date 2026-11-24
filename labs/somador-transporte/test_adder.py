import unittest,itertools
from .adder import full_adder,ripple,decode_signed

class RippleAdderTests(unittest.TestCase):
    def test_truth_table_by_arithmetic_division(self):
        for a,b,c in itertools.product((0,1),repeat=3):
            si,co=full_adder(a,b,c);integer=a+b+c
            self.assertEqual((si,co),(integer%2,integer//2))
            self.assertEqual(co,int(integer>=2))
    def test_exhaustive_words_and_prefix_invariant(self):
        count=0
        for width in range(1,7):
            for a,b,c in itertools.product(range(1<<width),range(1<<width),(0,1)):
                r=ripple(a,b,width,c);integer=a+b+c
                self.assertEqual(r['low'],integer%(1<<width))
                self.assertEqual(r['carry'],integer//(1<<width))
                for row in r['trace']:
                    j=row['index']+1;mask=(1<<j)-1
                    self.assertEqual((a&mask)+(b&mask)+c,row['prefix']+(1<<j)*row['carry_out'])
                count+=1
        self.assertEqual(count,10920)
    def test_signed_overflow_against_range(self):
        for a,b,c in itertools.product(range(16),range(16),(0,1)):
            r=ripple(a,b,4,c);integer=decode_signed(a,4)+decode_signed(b,4)+c
            self.assertEqual(bool(r['overflow']),not -8<=integer<=7)
            if not r['overflow']:self.assertEqual(decode_signed(r['low'],4),integer)
        a=ripple(7,1,4);b=ripple(15,1,4)
        self.assertEqual((a['low'],a['carry'],a['overflow']),(8,0,1))
        self.assertEqual((b['low'],b['carry'],b['overflow']),(0,1,0))
    def test_chain_examples_and_wider_words(self):
        r=ripple(15,1,4)
        self.assertEqual([x['carry_in'] for x in r['trace']],[0,1,1,1])
        self.assertEqual([x['carry_out'] for x in r['trace']],[1,1,1,1])
        self.assertEqual(ripple(5,6,4)['low'],11)
        for width in [8,12,16]:
            limit=(1<<width)-1
            for a,b,c in itertools.product([0,1,limit//2,limit],[0,1,limit//2,limit],(0,1)):
                r=ripple(a,b,width,c)
                self.assertEqual(r['low']+(1<<width)*r['carry'],a+b+c)
    def test_contracts(self):
        for args in [(True,0,0),(0,2,0),(0,0,-1)]:
            with self.assertRaises(ValueError):full_adder(*args)
        for args in [(-1,0,4),(16,0,4),(0,0,0),(0,0,17),(0,0,True),(.5,0,4),(0,0,4,2)]:
            with self.assertRaises(ValueError):ripple(*args)
