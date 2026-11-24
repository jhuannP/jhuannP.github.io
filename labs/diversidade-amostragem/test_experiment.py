import itertools
import unittest
from fractions import Fraction as F
from .experiment import expectation,model

class DiversitySamplingTests(unittest.TestCase):
    def test_all_small_collections_by_individual_subsets(self):
        # 255 coleções; 50624 subconjuntos de identidades, incluindo vazios.
        for counts in itertools.product(range(4),repeat=4):
            if not sum(counts):continue
            labels=[i for i,k in enumerate(counts) for _ in range(k)]
            for n in range(len(labels)+1):
                sums=[0]*4;richness_sum=0;number=0
                for subset in itertools.combinations(range(len(labels)),n):
                    present={labels[i] for i in subset}
                    number+=1;richness_sum+=len(present)
                    for i in present:sums[i]+=1
                r=expectation(counts,n)
                self.assertEqual(r['expected'],F(richness_sum,number))
                self.assertEqual(r['detection'],tuple(F(k,number) for k in sums))
                self.assertEqual(r['total_subsets'],number)
    def test_orders_are_nested_examples_not_expected_values(self):
        for pop in range(3):
            for order in range(3):
                previous=None
                for n in range(13):
                    r=model(pop,n,order)
                    self.assertEqual(sorted(r['indices']),list(range(12)))
                    self.assertEqual(sum(r['observed']),n)
                    self.assertEqual(len(r['selected']),n)
                    self.assertTrue(all(a<=b for a,b in zip(r['observed'],r['counts'])))
                    if previous:self.assertGreaterEqual(r['richness'],previous['richness'])
                    self.assertEqual(r['expected'],model(pop,n,0)['expected'])
                    previous=r
    def test_known_examples_and_boundaries(self):
        self.assertEqual(model()['expected'],F(433,165))
        self.assertEqual(model()['rare_probability'],F(1,3))
        self.assertEqual(model()['richness'],1);self.assertEqual(model(order=1)['richness'],4)
        for pop in range(3):
            self.assertEqual(model(pop,0)['expected'],0)
            self.assertEqual(model(pop,12)['expected'],4)
            self.assertEqual(model(pop,12)['rare_probability'],1)
        self.assertEqual(expectation((12,0),4)['detection'],(1,0))
        self.assertEqual(expectation((0,3,0),0)['expected'],0)
    def test_contract(self):
        for counts,n in [((),0),((0,0),0),((-1,3),1),((True,3),1),((1.,3),1),((2,3),-1),((2,3),6),((2,3),True),((2,3),.5)]:
            with self.assertRaises(ValueError):expectation(counts,n)
        for args in [(3,4,0),(0,4,3),(True,4,0),(0,13,0)]:
            with self.assertRaises(ValueError):model(*args)
