import unittest
from fractions import Fraction as Q
from itertools import product
from statistics import variance, pvariance, NormalDist
from .experiment import sample_variances, variance_risks, normal_interval

class EstimationTests(unittest.TestCase):
    def test_sample_reference_and_affine_transform(self):
        for values in ([1, 2, 3], [-2, 1, 4, 7], [3, 3], [Q(1, 2), Q(3, 2)]):
            r = sample_variances(values)
            self.assertEqual(r['divisor_n'], pvariance(list(map(Q, values))))
            self.assertEqual(r['divisor_n_minus_1'], variance(list(map(Q, values))))
            moved = sample_variances([2*x+10 for x in values])
            self.assertEqual(moved['divisor_n'], 4*r['divisor_n'])
            self.assertEqual(moved['divisor_n_minus_1'], 4*r['divisor_n_minus_1'])

    def test_risk_against_enumerated_samples(self):
        for n in range(2, 9):
            for p in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
                outcomes=[]
                for sample in product((0, 1), repeat=n):
                    weight=Q(1)
                    for x in sample: weight *= p if x else 1-p
                    outcomes.append((sample_variances(sample), weight))
                r = variance_risks(n, p); target=p*(1-p)
                for key in ('divisor_n', 'divisor_n_minus_1'):
                    mean = sum(s[key]*w for s,w in outcomes)
                    mse = sum((s[key]-target)**2*w for s,w in outcomes)
                    self.assertEqual(r[key]['mean'], mean); self.assertEqual(r[key]['mse'], mse)
                    self.assertEqual(r[key]['mse'], r[key]['variance']+r[key]['bias']**2)
                self.assertEqual(r['divisor_n_minus_1']['bias'], 0)
                self.assertEqual(r['divisor_n']['bias'], -target/n)
        r=variance_risks(4,Q(1,2))
        self.assertLess(r['divisor_n']['mse'], r['divisor_n_minus_1']['mse'])

    def test_interval_pivot_coverage_and_width(self):
        d=NormalDist()
        for level in (.9, .95, .99):
            for n in (4, 16, 64):
                r=normal_interval(5, 2, n, level)
                self.assertAlmostEqual(d.cdf(r['critical'])-d.cdf(-r['critical']), level)
                larger=normal_interval(5, 2, n*4, level)
                self.assertEqual(larger['margin'], r['margin']/2)
                for z in (-3, -1, 0, 1, 3):
                    interval=normal_interval(5+2*z/n**.5,2,n,level)
                    self.assertEqual(interval['lower']<=5<=interval['upper'], abs(z)<=r['critical'])
        self.assertGreater(normal_interval(5,2,4,.99)['margin'],normal_interval(5,2,4,.9)['margin'])

    def test_contracts(self):
        for values in ([], [1], [True, 1], [.5, 1]):
            with self.assertRaises(ValueError): sample_variances(values)
        for n,p in [(1,Q(1,2)),(True,Q(1,2)),(101,Q(1,2)),(4,.5),(4,Q(-1,2))]:
            with self.assertRaises(ValueError): variance_risks(n,p)
        for mean,sd,n,level in [(0,0,4,.95),(0,1,0,.95),(0,1,4,1),(True,1,4,.95),(0,float('nan'),4,.95)]:
            with self.assertRaises(ValueError): normal_interval(mean,sd,n,level)

if __name__ == '__main__': unittest.main()
