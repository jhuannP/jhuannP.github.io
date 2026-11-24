from fractions import Fraction as Q
from itertools import product
from collections import Counter
import unittest
from .cluster import cluster

class ClusterTests(unittest.TestCase):
    def test_independent_identified_site_enumeration(self):
        # Primitive equiprobable draws: no comb or binomial formula in oracle.
        for n in range(6):
            for a in range(5):
                counts=Counter(sum(v<a for v in choices) for choices in product(range(4),repeat=n))
                result=cluster(n,Q(a,4))
                for k,row in enumerate(result):self.assertEqual(row['probability'],Q(counts[k],4**n))

    def test_normalization_moments_and_relative_scale(self):
        for n in range(13):
            for p in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)):
                rows=cluster(n,p)
                self.assertEqual(sum(r['probability'] for r in rows),1)
                mean=sum(r['heavy']*r['probability'] for r in rows)
                variance=sum((r['heavy']-mean)**2*r['probability'] for r in rows)
                self.assertEqual(mean,n*p);self.assertEqual(variance,n*p*(1-p))
                self.assertEqual(max(r['relative'] for r in rows),100)
                for r in rows:self.assertGreaterEqual(r['probability'],0)

    def test_example_and_charge_spacing(self):
        rows=cluster(2,Q(1,4));double=cluster(2,Q(1,4),z=2)
        self.assertEqual([r['probability'] for r in rows],[Q(9,16),Q(6,16),Q(1,16)])
        self.assertEqual([r['relative'] for r in rows],[100,Q(200,3),Q(100,9)])
        self.assertEqual([r['mz'] for r in rows],[100,102,104])
        self.assertEqual([r['mz'] for r in double],[50,51,52])
        self.assertEqual([r['relative'] for r in double],[r['relative'] for r in rows])
        self.assertNotEqual(sum(r['relative'] for r in rows),100)

    def test_shift_and_endpoints(self):
        for n in (0,1,2,4):
            for z in (1,2,3):
                a=cluster(n,Q(1,3),100,z);b=cluster(n,Q(1,3),112,z)
                self.assertEqual([y['mz']-x['mz'] for x,y in zip(a,b)],[Q(12,z)]*(n+1))
                self.assertEqual(sum(r['probability'] for r in cluster(n,0) if r['heavy']==0),1)
                self.assertEqual(sum(r['probability'] for r in cluster(n,1) if r['heavy']==n),1)

    def test_contracts(self):
        for n,p,m,z in ((-1,Q(1,4),100,1),(13,Q(1,4),100,1),(True,Q(1,4),100,1),(2,Q(1,4),0,1),(2,Q(5,4),100,1),(2,Q(1,4),100,0),(2,Q(1,4),100,True),(2,.25,100,1)):
            with self.assertRaises((TypeError,ValueError)):cluster(n,p,m,z)

if __name__=='__main__':unittest.main()
