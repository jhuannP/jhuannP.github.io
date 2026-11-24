import unittest
from fractions import Fraction as Q
from .refine import euler,differences,table


class RefinementTests(unittest.TestCase):
    def test_recurrence_against_closed_solution(self):
        for n in range(1,65):
            y=Q(1)
            for _ in range(n):y-=y/n
            self.assertEqual(y,euler(n))
        self.assertEqual(euler(2),Q(1,4));self.assertEqual(euler(4),Q(81,256))

    def test_high_precision_errors_and_order(self):
        rows=table((16,32,64,128),60)
        for row in rows:
            self.assertTrue(1<row['observed_order']<1.1)
            self.assertLess(row['true_richardson_error'],row['true_fine_error'])
        for a,b in zip(rows,rows[1:]):
            self.assertTrue(1.9<float(a['true_fine_error']/b['true_fine_error'])<2.1)
            self.assertTrue(3.8<float(a['true_richardson_error']/b['true_richardson_error'])<4.3)
        self.assertEqual([round(float(r['true_fine_error']),13) for r in rows],
                         [round(float(r['true_fine_error']),13) for r in table((16,32,64,128),28)])

    def test_synthetic_order_and_cancellation(self):
        for p in (1,2,3,4):
            # q(h)=5+3h^p; exact difference ratio2^p, independently constructed.
            r=differences(8,5+Q(3,2**p),5+Q(3,4**p))
            self.assertAlmostEqual(r['observed_order'],p)
        self.assertEqual(differences(2,1,Q(1,2))['richardson_order1'],0)
        self.assertIsNone(differences(1,1,1)['observed_order'])
        self.assertIsNone(differences(0,1,0)['observed_order'])

    def test_contracts(self):
        for n in (0,-1,True,2.0,4097):
            with self.assertRaises(ValueError):euler(n)
        with self.assertRaises(ValueError):table((2048,))
        with self.assertRaises(ValueError):differences(1.,2,3)


if __name__=='__main__':unittest.main()
