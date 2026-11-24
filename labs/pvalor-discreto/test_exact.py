import unittest
from fractions import Fraction as F
from itertools import product
from .exact import law, upper_pvalues, rejection_mass

class ExactTests(unittest.TestCase):
    def test_five_coin_enumeration(self):
        outcomes = list(product((0, 1), repeat=5))
        null = law(5, F(1, 2))
        self.assertEqual(null, tuple(F(sum(sum(x)==k for x in outcomes), 32) for k in range(6)))
        pv = upper_pvalues(null)
        self.assertEqual(pv, (F(1), F(31,32), F(13,16), F(1,2), F(3,16), F(1,32)))
        self.assertEqual(rejection_mass(null,pv,F(1,20)), F(1,32))
        self.assertEqual(rejection_mass(null,pv,F(1,100)), 0)
        self.assertEqual(rejection_mass(law(5,F(3,4)),pv,F(1,20)), F(243,1024))

    def test_calibration_at_every_jump(self):
        for n in range(1, 13):
            for probability in (F(0), F(1,4), F(1,2), F(3,4), F(1)):
                null = law(n, probability); pv = upper_pvalues(null)
                for alpha in set(pv) | {F(0), F(1,100), F(1,20), F(1)}:
                    self.assertLessEqual(rejection_mass(null,pv,alpha), alpha)

    def test_two_independent_tests_by_1024_sequences(self):
        sequences = list(product((0,1),repeat=10))
        bad = sum(sum(x[:5])==5 or sum(x[5:])==5 for x in sequences)
        self.assertEqual(F(bad,1024), F(63,1024))
        null = law(5,F(1,2));pv=upper_pvalues(null)
        self.assertEqual(rejection_mass(null,pv,F(1,40)),0)
        self.assertGreater(F(bad,1024),F(1,20))

    def test_contracts(self):
        for n,p in ((True,F(1,2)), (0,F(1,2)), (21,F(1,2)), (5,0.5), (5,F(-1))):
            with self.assertRaises(ValueError): law(n,p)
        with self.assertRaises(ValueError): upper_pvalues((F(1,3),))
        with self.assertRaises(ValueError): rejection_mass((F(1),),(F(1),),0.05)

if __name__=='__main__': unittest.main()
