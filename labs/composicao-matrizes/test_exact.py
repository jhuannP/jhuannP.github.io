import unittest
from itertools import product as cases
from fractions import Fraction as Q
from .exact import product,apply

class CompositionTests(unittest.TestCase):
    def test_original_order_and_vectors(self):
        a=((2,0),(0,1));b=((1,1),(0,1))
        self.assertEqual(product(a,b),((2,2),(0,1)))
        self.assertEqual(product(b,a),((2,1),(0,1)))
        for x,y in cases(range(-3,4),repeat=2):
            self.assertEqual(apply(product(a,b),(x,y)),(2*x+2*y,y))
            self.assertEqual(apply(product(b,a),(x,y)),(2*x+y,y))

    def test_rectangular_case_against_direct_maps(self):
        b=((1,0),(0,1),(1,1));a=((1,0,1),(0,1,-1))
        self.assertEqual(product(a,b),((2,1),(-1,0)))
        self.assertEqual(product(b,a),((1,0,1),(0,1,-1),(1,1,0)))
        for x,y in cases(range(-3,4),repeat=2):
            self.assertEqual(apply(product(a,b),(x,y)),(2*x+y,-x))
            self.assertEqual(apply(a,apply(b,(x,y))),(2*x+y,-x))
        for u,v,w in cases(range(-2,3),repeat=3):
            self.assertEqual(apply(product(b,a),(u,v,w)),(u+w,v-w,u+v))

    def test_composition_reconstructed_from_basis_images(self):
        # Independent oracle for every ternary 2x2 pair: compose the column images.
        matrices=[(v[:2],v[2:]) for v in cases((-1,0,1),repeat=4)]
        for a in matrices:
            for b in matrices:
                columns=[apply(a,apply(b,e)) for e in ((1,0),(0,1))]
                expected=tuple(tuple(columns[j][i] for j in range(2)) for i in range(2))
                self.assertEqual(product(a,b),expected)

    def test_intermediate_coordinate_conversion(self):
        # P maps W coordinates to canonical coordinates; A_W=A*P and B_W=P^-1*B.
        a=((2,0),(0,1));b=((1,1),(0,1));p=((1,1),(0,1));pinv=((1,-1),(0,1))
        self.assertEqual(product(product(a,p),product(pinv,b)),product(a,b))
        self.assertNotEqual(product(product(a,p),b),product(a,b))
        # Same value on one vector does not prove maps equal.
        self.assertEqual(apply(product(a,b),(1,0)),apply(product(b,a),(1,0)))

    def test_contracts_and_no_mutation(self):
        a=[[Q(1,2),0],[0,1]];b=[[1],[2]]
        self.assertEqual(product(a,b),((Q(1,2),),(Q(2),)))
        self.assertEqual(a,[[Q(1,2),0],[0,1]])
        for bad in ([],[[]],[[1],[1,2]]):
            with self.assertRaises(ValueError):product(bad,((1,),))
        for bad in (True,.5,'1'):
            with self.assertRaises(TypeError):product(((bad,),),((1,),))
        with self.assertRaises(ValueError):product(((1,2),),((1,2),))
        with self.assertRaises(ValueError):apply(((1,2),),(1,))

if __name__=='__main__':unittest.main()
