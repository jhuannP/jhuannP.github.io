import unittest
from .experiment import sums,formulas,first_composite,polynomial,first_divisor

class InductionTests(unittest.TestCase):
    def test_formulas_against_direct_sums(self):
        for n in range(201):self.assertEqual(sums(n),formulas(n))
        self.assertEqual(sums(0),dict(linear=0,odd=0,squares=0))
        self.assertEqual(sums(4),dict(linear=10,odd=16,squares=30))

    def test_inductive_differences_and_positive_inequality(self):
        for k in range(201):
            a,b=formulas(k),formulas(k+1)
            self.assertEqual(b['linear']-a['linear'],k+1)
            self.assertEqual(b['odd']-a['odd'],2*k+1)
            self.assertEqual(b['squares']-a['squares'],(k+1)**2)
            self.assertGreaterEqual(2**k,k+1)

    def test_many_true_cases_do_not_prove_the_claim(self):
        for n in range(40):self.assertIsNone(first_divisor(polynomial(n)))
        self.assertEqual(first_composite(),(40,1681,41))
        self.assertEqual(41*41,polynomial(40))
        # A recorrência F(k+1)=F(k)+2k+2 não preserva primalidade.
        for k in range(40):self.assertEqual(polynomial(k+1)-polynomial(k),2*k+2)

    def test_contracts(self):
        for fn in (sums,formulas):
            for n in (-1,1001,True,.5):
                with self.assertRaises(ValueError):fn(n)
        with self.assertRaises(ValueError):polynomial(101)

if __name__=='__main__':unittest.main()
