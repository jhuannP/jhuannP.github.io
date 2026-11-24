import unittest
from fractions import Fraction as F
from .analysis import per_cell,fold
class ReporterTests(unittest.TestCase):
    def test_confounded_example_and_undefined_fold(self):
        self.assertEqual(per_cell(220,20,100),2)
        self.assertEqual(per_cell(70,20,50),1)
        self.assertEqual(fold(per_cell(220,20,100),per_cell(70,20,50)),2)
        self.assertEqual(fold(220,70),F(22,7))
        self.assertEqual(fold(200,50),4)
        self.assertEqual(per_cell(10,20,5),-2) # retain below-background result
        for t,ref in [(2,0),(2,-1),(-1,2)]:self.assertIsNone(fold(t,ref))
        self.assertEqual(fold(0,2),0)

    def test_recover_signal_and_invariances(self):
        # 300 synthetic populations; oracle is a specified q, not a second formula.
        for n in range(1,21):
            for q in [F(0),F(1,3),F(2)]:
                for b in [F(0),F(2),F(7),F(9),F(13)]:
                    raw=n*q+b
                    self.assertEqual(per_cell(raw,b,n),q)
                    self.assertEqual(per_cell(raw+17,b+17,n),q)
                    self.assertEqual(per_cell(3*raw,3*b,3*n),q)
        # Equal q can yield unequal raw and background-subtracted population totals.
        self.assertEqual(per_cell(120,20,50),per_cell(220,20,100))

    def test_contracts_and_population_average(self):
        for args in [(True,0,1),(1,.1,1),(1,0,'1')]:
            with self.assertRaises(TypeError):per_cell(*args)
        for args in [(-1,0,1),(1,-1,1),(1,0,0)]:
            with self.assertRaises(ValueError):per_cell(*args)
        # Averaging independent replicate means is not pooling cell counts.
        a,b=per_cell(1,0,1),per_cell(27,0,9)
        self.assertEqual((a+b)/2,2)
        self.assertEqual(per_cell(28,0,10),F(14,5))
if __name__=='__main__':unittest.main()
