from fractions import Fraction as F
from itertools import product
import unittest
from .experiment import compare

class AggregationTests(unittest.TestCase):
    def test_exact_example_and_scale(self):
        rows=((9,10,72,90),(27,90,2,10))
        r=compare(rows)
        self.assertEqual(r['rates_a'],(F(9,10),F(3,10)))
        self.assertEqual(r['rates_b'],(F(4,5),F(1,5)))
        self.assertTrue(r['reversal'])
        self.assertEqual(r['common_a']-r['common_b'],F(1,10))
        self.assertEqual(compare(tuple(tuple(7*x for x in row) for row in rows)),r)

    def test_pooled_by_distinct_atoms(self):
        # Independently materialize each successful/unsuccessful object.
        row_options=[(a,na,b,nb) for na in range(1,4) for nb in range(1,4)
                     for a in range(na+1) for b in range(nb+1)]
        for rows in product(row_options, repeat=2):
            r=compare(rows)
            for label,si,ni in [('a',0,1),('b',2,3)]:
                atoms=[(g,i,i<row[si]) for g,row in enumerate(rows) for i in range(row[ni])]
                self.assertEqual(r['pooled_'+label], F(sum(x[2] for x in atoms),len(atoms)))
                self.assertEqual(r['pooled_'+label], sum(w*p for w,p in zip(r['weights_'+label],r['rates_'+label])))

    def test_common_weights_preserve_order(self):
        fractions=[F(0),F(1,4),F(1,2),F(3,4),F(1)]
        for a0,a1,b0,b1,w in product(fractions,repeat=5):
            rows=((a0.numerator*(4//a0.denominator),4,b0.numerator*(4//b0.denominator),4),
                  (a1.numerator*(4//a1.denominator),4,b1.numerator*(4//b1.denominator),4))
            r=compare(rows,w)
            self.assertEqual(r['common_a']-r['common_b'],w*(a0-b0)+(1-w)*(a1-b1))
            if a0>=b0 and a1>=b1:
                self.assertGreaterEqual(r['common_a'],r['common_b'])
            swapped=compare(rows[::-1],1-w)
            self.assertEqual(swapped['common_a'],r['common_a'])
            self.assertEqual(swapped['pooled_a'],r['pooled_a'])

    def test_contracts(self):
        for rows in [[],[(1,2,1,2)],[(0,0,1,2),(1,2,1,2)],[(3,2,1,2),(1,2,1,2)],[(True,2,1,2),(1,2,1,2)]]:
            with self.assertRaises(ValueError): compare(rows)
        for w in [True,.5,F(-1),F(2),None]:
            with self.assertRaises(ValueError): compare(((1,2,1,2),(1,2,1,2)),w)
