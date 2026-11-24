from fractions import Fraction as Q
from itertools import permutations, product
import unittest
from .measurement import summarize,corrected,rectangular_variance

class MeasurementTests(unittest.TestCase):
    def test_example_and_uncertainty_of_common_correction(self):
        x=[Q(49,5),10,Q(51,5)];saved=x.copy()
        s=corrected(x,Q(3,10),Q(1,10))
        self.assertEqual(x,saved)
        self.assertEqual(s['mean'],10)
        self.assertEqual(s['sample_variance'],Q(1,25))
        self.assertEqual(s['mean_variance'],Q(1,75))
        self.assertEqual(s['corrected_mean'],Q(97,10))
        self.assertEqual(s['combined_variance'],Q(7,300))
        # Common calibration term is not divided by the number of readings.
        self.assertEqual(s['combined_variance']-s['mean_variance'],Q(1,100))

    def test_pairwise_oracle(self):
        for n in (2,3,4):
            for x in product(range(-2,3),repeat=n):
                s=summarize(x)
                pair_sum=sum((x[i]-x[j])**2 for i in range(n) for j in range(i))
                self.assertEqual(s['sample_variance'],Q(pair_sum,n*(n-1)))
                self.assertEqual(s['mean_variance'],Q(pair_sum,n*n*(n-1)))

    def test_affine_units_and_permutation(self):
        x=(Q(49,5),Q(10),Q(51,5));base=summarize(x)
        for p in permutations(x):self.assertEqual(summarize(p),base)
        shifted=summarize([v+Q(3,10) for v in x])
        self.assertEqual(shifted['sample_variance'],base['sample_variance'])
        cm=corrected(x,Q(3,10),Q(1,10))
        mm=corrected([10*v for v in x],3,1)
        self.assertEqual(mm['corrected_mean'],10*cm['corrected_mean'])
        self.assertEqual(mm['combined_variance'],100*cm['combined_variance'])

    def test_equal_readings_do_not_clear_calibration(self):
        s=corrected([10]*12,Q(3,10),Q(1,10))
        self.assertEqual(s['mean_variance'],0)
        self.assertEqual(s['combined_variance'],Q(1,100))
        self.assertEqual(rectangular_variance(Q(1,20)),Q(1,1200))

    def test_contracts(self):
        for x in ([],[1],None,'12',[True,2],[1.,2],[Q(1),None]):
            with self.assertRaises(ValueError):summarize(x)
        for bad in (True,1.,'1',None):
            with self.assertRaises(ValueError):corrected([1,2],bad,0)
            with self.assertRaises(ValueError):rectangular_variance(bad)
        with self.assertRaises(ValueError):corrected([1,2],0,-1)
        with self.assertRaises(ValueError):rectangular_variance(-1)

if __name__=='__main__':unittest.main()
