import unittest
from fractions import Fraction as Q
from decimal import Decimal,ROUND_HALF_UP
from .experiment import sequence,rate_back,summary

class SuccessivePercentTests(unittest.TestCase):
    def test_polynomial_reference_and_scaling(self):
        for initial in (50,100,250):
            for a in (-100,-50,0,20,100):
                for b in (-100,-20,0,25,100):
                    trace=sequence(initial,[a,b]);net=Q(a)+b+Q(a*b,100)
                    self.assertEqual(100*(trace[-1]/initial-1),net)
                    self.assertEqual(trace[-1],sequence(initial,[b,a])[-1])
                    self.assertEqual(sequence(3*initial,[a,b])[-1],3*trace[-1])
        self.assertEqual(sequence(100,[20,-20]),[100,120,96])
        self.assertEqual(sequence(250,[20,-20])[-1],240)

    def test_inverse_and_zero_factor(self):
        for r in (-99,-50,-20,0,20,25,100):
            self.assertEqual(sequence(100,[r,rate_back(r)])[-1],100)
        self.assertEqual(rate_back(-20),25);self.assertEqual(rate_back(20),Q(-50,3))
        self.assertIsNone(rate_back(-100));self.assertIsNone(summary(100,-100,100)['recovery'])
        self.assertEqual(sequence(100,[-100,100]),[100,0,0])
        self.assertAlmostEqual(summary(100,20,-20)['recovery'],25/6)

    def test_rounding_changes_the_operation(self):
        def rounded(value,rate):return(value*(1+Decimal(rate)/100)).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
        x=Decimal('.02')
        self.assertEqual(rounded(rounded(x,20),50),Decimal('.03'))
        self.assertEqual(rounded(rounded(x,50),20),Decimal('.04'))
        self.assertEqual(sequence('.02',[20,50])[-1],Q(9,250))
        self.assertEqual(sequence('.02',[50,20])[-1],Q(9,250))

    def test_domain_and_identity(self):
        self.assertEqual(sequence(7,[]),[7]);self.assertEqual(sequence(7,[0,0]),[7,7,7])
        for initial,rates in [(0,[1]),(-1,[1]),(1,[-101]),(1,[float('nan')]),(float('inf'),[1])]:
            with self.assertRaises((ValueError,OverflowError)):sequence(initial,rates)

if __name__=='__main__':unittest.main()
