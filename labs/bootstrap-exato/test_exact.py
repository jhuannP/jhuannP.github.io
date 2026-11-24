import unittest
from fractions import Fraction as Q
from itertools import product,permutations
from .exact import distribution,quantile


class ExactTests(unittest.TestCase):
    def test_multiplicity_and_original(self):
        r=distribution([1,1,4])
        self.assertEqual(r['counts'],{Q(1):8,Q(2):12,Q(3):6,Q(4):1})
        self.assertEqual((r['total'],r['mean'],r['variance']),(27,2,Q(2,3)))
        self.assertEqual(r['empirical_variance'],2)
        for x in set(permutations([1,1,4])):self.assertEqual(distribution(x),r)
        old=distribution([1,3]);self.assertEqual(old['counts'],{1:1,2:2,3:1})
        self.assertEqual(old['variance'],Q(1,2))
        self.assertNotEqual(distribution([1,4])['mean'],r['mean'])

    def test_moments_and_affine_changes(self):
        for n in range(1,5):
            for x in product((-1,0,2),repeat=n):
                r=distribution(x);mean=sum(map(Q,x))/n
                var=sum((Q(v)-mean)**2 for v in x)/n
                self.assertEqual(sum(r['counts'].values()),n**n)
                self.assertEqual(r['mean'],mean)
                self.assertEqual(r['variance'],var/n)
                y=tuple(-2*v+3 for v in x);s=distribution(y)
                self.assertEqual(s['mean'],-2*mean+3)
                self.assertEqual(s['variance'],4*r['variance'])

    def test_quantiles_and_degenerate_counterexample(self):
        r=distribution([1,1,4]);c=r['counts']
        self.assertEqual(quantile(c,Q(1,40)),1)
        self.assertEqual(quantile(c,Q(39,40)),4)
        for p in (0,Q(8,27),Q(20,27),1):
            q=quantile(c,p)
            self.assertGreaterEqual(sum(n for v,n in c.items() if v<=q)/27,float(p))
        deg=distribution([1,1,1])
        self.assertEqual(deg['counts'],{1:27});self.assertEqual(deg['variance'],0)
        self.assertEqual(quantile(deg['counts'],Q(39,40)),1)
        self.assertGreater(Q(199,100),1);self.assertGreater(Q(99,100)**3,Q(97,100))

    def test_contracts(self):
        for values in ([],[1]*7,[True],[1.0],'123'):
            with self.assertRaises(ValueError):distribution(values)
        for counts,p in (({},Q(1,2)),({1:0},Q(1,2)),({1:1},-1),({1:1},Q(11,10)),({True:1},Q(1,2))):
            with self.assertRaises(ValueError):quantile(counts,p)


if __name__=='__main__':unittest.main()
