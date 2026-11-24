import unittest
from fractions import Fraction as Q
from itertools import product
from statistics import mean,median
from .summary import summarize,frequency_summary,combine_means,losses


class SummaryTests(unittest.TestCase):
    def test_original_and_one_observation_change(self):
        a=[1,2,3,4,10];b=[1,2,3,4,100]
        x,y=summarize(a),summarize(b)
        self.assertEqual((x['mean'],x['median'],x['range']),(4,3,9))
        self.assertEqual((y['mean'],y['median'],y['range']),(22,3,99))
        self.assertEqual(y['mean']-x['mean'],Q(100-10,5))
        self.assertEqual(summarize([1,2,12,4,10])['median'],4)
        self.assertEqual(a,[1,2,3,4,10])

    def test_frequency_algorithm_against_expanded_library_oracle(self):
        for n in range(1,6):
            for xs in product(range(-2,3),repeat=n):
                r=summarize(xs)
                self.assertEqual(r['mean'],mean(map(Q,xs)))
                self.assertEqual(r['median'],median(map(Q,xs)))
                self.assertEqual(r['n'],n)
                self.assertEqual(r['total'],sum(xs))
                self.assertEqual(summarize(tuple(reversed(xs))),r)
        r=frequency_summary({2:3,5:1,8:2,100:0})
        self.assertEqual((r['n'],r['mean'],r['median'],r['range']),(6,Q(9,2),Q(7,2),6))
        large=frequency_summary({2:10**9,8:10**9})
        self.assertEqual((large['n'],large['mean'],large['median']),(2*10**9,5,5))

    def test_affine_units_and_same_location_different_spread(self):
        xs=[Q(1,3),2,Q(7,3),5];base=summarize(xs)
        for scale in [Q(-2),Q(0),Q(3,2)]:
            offset=Q(5,7);r=summarize([scale*x+offset for x in xs])
            self.assertEqual(r['mean'],scale*base['mean']+offset)
            self.assertEqual(r['median'],scale*base['median']+offset)
            self.assertEqual(r['range'],abs(scale)*base['range'])
        a,b=summarize([4,4,4,4]),summarize([1,3,5,7])
        self.assertEqual((a['mean'],a['median']),(b['mean'],b['median']))
        self.assertNotEqual(a['range'],b['range'])

    def test_group_means_and_medians(self):
        xs=[2,4];ys=[10]*6
        result=combine_means([(len(xs),summarize(xs)['mean']),(len(ys),summarize(ys)['mean'])])
        self.assertEqual(result,summarize(xs+ys)['mean'])
        self.assertEqual(result,Q(33,4))
        self.assertNotEqual(result,Q(3+10,2))
        # Medians do not follow the weighted-mean identity.
        xs,ys=[0,0,100],[1,1,1]
        self.assertEqual(summarize(xs+ys)['median'],1)
        self.assertEqual(combine_means([(3,summarize(xs)['median']),(3,summarize(ys)['median'])]),Q(1,2))

    def test_loss_identities_and_median_minimizers(self):
        xs=[1,2,3,4,10];mu=Q(4);med=Q(3)
        self.assertEqual(losses(xs,mu),dict(absolute=Q(12),squared=Q(50)))
        self.assertEqual(losses(xs,med),dict(absolute=Q(11),squared=Q(55)))
        for c in [Q(i,2) for i in range(-2,25)]:
            self.assertEqual(losses(xs,c)['squared'],50+5*(c-4)**2)
            self.assertGreaterEqual(losses(xs,c)['absolute'],11)
        for c in [Q(2),Q(7,2),Q(5),Q(8)]:self.assertEqual(losses([2,8],c)['absolute'],6)
        self.assertGreater(losses([2,8],1)['absolute'],6)

    def test_contracts(self):
        for xs in [[],None,[True],[1.0],['2']]:
            with self.assertRaises(ValueError):summarize(xs)
        for f in [{},{1:0},{1:-1},{1:True},{1:1.0},{True:1}]:
            with self.assertRaises(ValueError):frequency_summary(f)
        for groups in [[],[(0,1)],[(True,1)],[(1,1.0)],[(1,)]]:
            with self.assertRaises(ValueError):combine_means(groups)
        with self.assertRaises(ValueError):losses([1],True)

if __name__=='__main__':unittest.main()
