import unittest
from fractions import Fraction as F
from .ez import classify,priority,A,B,LEFT,RIGHT_E,RIGHT_Z

class EZTests(unittest.TestCase):
    def test_examples_and_ordering(self):
        self.assertEqual(classify(A,B,LEFT,RIGHT_E)['configuration'],'E')
        self.assertEqual(classify(A,B,LEFT,RIGHT_Z)['configuration'],'Z')
        self.assertEqual(classify(A,B,LEFT,RIGHT_E)['higher_indices'],(0,1))
        for right in (RIGHT_E,RIGHT_Z):
            expected=classify(A,B,LEFT,right)['configuration']
            self.assertEqual(classify(A,B,tuple(reversed(LEFT)),tuple(reversed(right)))['configuration'],expected)
            self.assertEqual(classify(B,A,right,LEFT)['configuration'],expected)

    def test_affine_invariance_exact(self):
        # Cross products acquire det(M); their product acquires det(M)².
        matrices=(((1,0),(0,1)),((0,-1),(1,0)),((-1,0),(0,1)),
                  ((2,1),(1,1)),((F(3,5),F(-4,5)),(F(4,5),F(3,5))),((1,2),(3,1)))
        for M in matrices:
            for shift in ((0,0),(F(1,3),-2),(7,5)):
                transform=lambda p:tuple(sum(M[i][j]*p[j] for j in range(2))+shift[i] for i in range(2))
                pair=lambda items:tuple((z,transform(pt)) for z,pt in items)
                det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
                for right in (RIGHT_E,RIGHT_Z):
                    base=classify(A,B,LEFT,right)
                    result=classify(transform(A),transform(B),pair(LEFT),pair(right))
                    self.assertEqual(result['configuration'],base['configuration'])
                    self.assertEqual(result['signed_areas'],tuple(det*x for x in base['signed_areas']))

    def test_atomic_number_pairs_and_diagram_sides(self):
        zs=(1,6,9,17,35,53)
        for z0 in zs:
            for z1 in zs:
                if z0==z1:continue
                self.assertEqual(priority(z0,z1),0 if z0>z1 else 1)
                left=((z0,(-1,1)),(z1,(-1,-1)))
                for right in (RIGHT_E,RIGHT_Z):
                    result=classify(A,B,left,right)['configuration']
                    # Independent horizontal diagram oracle based on selected y sides.
                    high_left_y=1 if z0>z1 else -1
                    high_right_y=-1 if right is RIGHT_E else 1
                    expected='Z' if high_left_y==high_right_y else 'E'
                    self.assertEqual(result,expected)

    def test_contract_and_unresolved_is_not_absent(self):
        with self.assertRaises(ValueError):priority(6,6)
        for bad in (True,9.0,'9',None):
            with self.assertRaises(TypeError):priority(bad,17)
        with self.assertRaises(ValueError):priority(0,17)
        with self.assertRaises(ValueError):classify(A,A,LEFT,RIGHT_E)
        with self.assertRaises(ValueError):classify(A,B,((17,(-1,0)),(9,(-1,-1))),RIGHT_E)
        with self.assertRaises(ValueError):classify(A,B,((17,(-1,1)),(9,(-2,2))),RIGHT_E)
        with self.assertRaises(ValueError):classify(A,B,((6,(-1,1)),(6,(-1,-1))),RIGHT_E)
