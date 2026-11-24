import unittest
from itertools import product
from fractions import Fraction as Q
from .risk import risks,estimates

class RiskTests(unittest.TestCase):
    def test_sequence_enumeration_independent_of_binomial_weights(self):
        for n in range(1,7):
            for p in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)):
                r=risks(n,p)
                sums=[dict(mean=Q(0),mse=Q(0)) for _ in range(2)]
                total=Q(0)
                for seq in product((0,1),repeat=n):
                    weight=Q(1)
                    for x in seq:weight*=p if x else 1-p
                    total+=weight
                    # Literal rules, not calls to estimates, and weights per ordered sequence.
                    for j,t in enumerate((Q(sum(seq),n),Q(sum(seq)+1,n+2))):
                        sums[j]['mean']+=weight*t;sums[j]['mse']+=weight*(t-p)**2
                self.assertEqual(total,1)
                for j,key in enumerate(('sample','shrink')):
                    self.assertEqual(r[key]['mean'],sums[j]['mean'])
                    self.assertEqual(r[key]['mse'],sums[j]['mse'])
                    self.assertEqual(r[key]['mse'],r[key]['variance']+r[key]['bias']**2)

    def test_general_closed_risks(self):
        for n in (1,2,4,7,20,100):
            for p in (Q(0),Q(1,10),Q(1,4),Q(1,2),Q(9,10),Q(1)):
                r=risks(n,p)
                self.assertEqual(r['sample']['mse'],p*(1-p)/n)
                self.assertEqual(r['shrink']['bias'],(1-2*p)/(n+2))
                self.assertEqual(r['shrink']['mse'],(n*p*(1-p)+(1-2*p)**2)/(n+2)**2)

    def test_constant_risk_and_no_uniform_domination(self):
        for k in range(41):self.assertEqual(risks(4,Q(k,40))['shrink']['mse'],Q(1,36))
        r=risks(4,Q(1,2));self.assertEqual(r['sample']['mse'],Q(1,16))
        self.assertLess(r['shrink']['mse'],r['sample']['mse'])
        for p in (Q(0),Q(1,10),Q(9,10),Q(1)):
            r=risks(4,p);self.assertLess(r['sample']['mse'],r['shrink']['mse'])
        r=risks(4,Q(1,4))
        self.assertEqual((r['shrink']['bias'],r['shrink']['variance']),(Q(1,12),Q(1,48)))

    def test_estimate_endpoints_symmetry_and_consistency_bound(self):
        for n in (1,4,9,100):
            for k in range(n+1):
                a,t=estimates(n,k)
                self.assertTrue(0<t<1)
                self.assertEqual(estimates(n,n-k),(1-a,1-t))
            for p in (Q(0),Q(1,3),Q(1,2),Q(1)):
                self.assertLessEqual(risks(n,p)['shrink']['mse'],Q(n,4*(n+2)**2)+Q(1,(n+2)**2))
        self.assertEqual(estimates(4,0),(0,Q(1,6)))

    def test_contracts(self):
        for n in (0,101,True,2.0):
            with self.assertRaises(ValueError):risks(n,Q(1,2))
        for p in (-1,2,True,.5):
            with self.assertRaises(ValueError):risks(4,p)
        for k in (-1,5,True,1.0):
            with self.assertRaises(ValueError):estimates(4,k)
