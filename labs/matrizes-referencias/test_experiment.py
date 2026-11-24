import unittest
from fractions import Fraction as Q
from itertools import product
from copy import deepcopy
from .experiment import shape, copy_rows, column_means, center_columns

class MatrixReferenceTests(unittest.TestCase):
    def test_example_and_identity(self):
        A = [[2,10],[4,14],[6,12]]
        before = deepcopy(A)
        B = center_columns(A)
        self.assertEqual(column_means(A), [4,12])
        self.assertEqual(B, [[-2,-2],[0,2],[2,0]])
        self.assertEqual(A, before)
        self.assertIsNot(A, B)
        for row in B:
            self.assertTrue(all(row is not original for original in A))
        B[0][0] = 99
        self.assertEqual(A, before)

    def test_reference_graph_and_shallow_copy(self):
        A = [[1,2],[3,4]]
        alias, outer, rows = A, A.copy(), copy_rows(A)
        self.assertIs(alias, A)
        self.assertIsNot(outer, A)
        self.assertIs(outer[0], A[0])
        self.assertIsNot(rows[0], A[0])
        alias[0][0] = 9
        self.assertEqual(outer[0][0], 9)
        self.assertEqual(rows[0][0], 1)
        outer[1] = [-1,-1]
        self.assertEqual(A[1], [3,4])
        bad = [[0,0]]*2
        good = [[0,0] for _ in range(2)]
        self.assertIs(bad[0], bad[1])
        self.assertIsNot(good[0], good[1])
        bad[0][1] = 7
        good[0][1] = 7
        self.assertEqual(bad, [[0,7],[0,7]])
        self.assertEqual(good, [[0,7],[0,0]])

    def test_exhaustive_tables_against_transposed_columns(self):
        for m,n in ((1,1),(1,3),(2,2),(3,2)):
            for flat in product((-1,0,2), repeat=m*n):
                A = [list(flat[i*n:(i+1)*n]) for i in range(m)]
                before = deepcopy(A)
                cols = list(zip(*A))
                means = [sum(map(Q,col))/len(col) for col in cols]
                expected = list(map(list, zip(*[[Q(x)-mean for x in col]
                    for col,mean in zip(cols,means)])))
                B = center_columns(A)
                self.assertEqual(B, expected)
                self.assertEqual(A, before)
                self.assertEqual(column_means(B), [0]*n)
                self.assertEqual(center_columns(B), B)
                self.assertTrue(all(B[i] is not B[j] for i in range(m) for j in range(i)))

    def test_offsets_and_shared_input_rows(self):
        A = [[Q(1,3),Q(2,5)],[Q(4,3),Q(7,5)]]
        B = center_columns(A)
        shifted = [[x+Q(j+1,7) for j,x in enumerate(row)] for row in A]
        self.assertEqual(center_columns(shifted), B)
        row = [2,3]
        shared = [row,row]
        copied, centered = copy_rows(shared), center_columns(shared)
        self.assertIsNot(copied[0], copied[1])
        self.assertIsNot(centered[0], centered[1])
        copied[0][0] = 10
        self.assertEqual(shared, [[2,3],[2,3]])

    def test_contracts_and_ragged_inputs(self):
        for A in ([],[[]],[[1],[2,3]],(1,2),[[True]],[[1.0]],[["2"]],[[[1]]],[[None]],[[1],()]):
            for fn in (shape,copy_rows,column_means,center_columns):
                with self.assertRaises(ValueError):
                    fn(A)
        self.assertEqual(shape([[0]]), (1,1))
        self.assertEqual(center_columns([[Q(1,3)]]), [[0]])
