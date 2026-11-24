import unittest
from fractions import Fraction as Q
from itertools import product
from .experiment import apply,multiply,inverse,coordinates,transition,representation,gram
I=((Q(1),Q(0)),(Q(0),Q(1)))

class BasisCoordinatesTests(unittest.TestCase):
    def test_reference(self):
        B=((1,1),(0,1));C=((2,0),(0,1));v=(3,2)
        self.assertEqual(coordinates(B,v),(1,2))
        self.assertEqual(coordinates(C,v),(Q(3,2),2))
        self.assertEqual(transition(B,C),((Q(1,2),Q(1,2)),(0,1)))
        self.assertEqual(gram(B),((1,1),(1,2)))
        self.assertEqual(representation(((2,0),(0,3)),B),((2,-1),(0,3)))

    def test_all_small_bases_reconstruct_and_preserve_norm(self):
        count=0
        for a,b,c,d in product((-1,0,1),repeat=4):
            if a*d-b*c==0:continue
            B=((a,b),(c,d));count+=1
            inv=inverse(B);G=gram(B)
            self.assertEqual(multiply(inv,B),I);self.assertEqual(multiply(B,inv),I)
            # Rows of inverse are dual to columns of B.
            for v in product((-2,0,3),repeat=2):
                z=coordinates(B,v)
                self.assertEqual(apply(B,z),v)
                Gz=apply(G,z)
                self.assertEqual(sum(x*y for x,y in zip(z,Gz)),sum(x*x for x in v))
        self.assertEqual(count,48)

    def test_transition_composition_and_operator_action(self):
        bases=(((1,1),(0,1)),((2,0),(0,1)),((0,-1),(1,0)))
        operators=(((2,0),(0,3)),((0,1),(1,0)),((1,2),(2,4)))
        for B,C,D in product(bases,repeat=3):
            self.assertEqual(multiply(transition(C,D),transition(B,C)),transition(B,D))
            self.assertEqual(multiply(transition(C,B),transition(B,C)),I)
        for B,A,v in product(bases,operators,((3,2),(-1,4),(0,0))):
            z=coordinates(B,v);out=apply(representation(A,B),z)
            self.assertEqual(apply(B,out),apply(A,v))

    def test_transpose_is_not_general_inverse(self):
        B=((1,1),(0,1));v=(3,2)
        self.assertEqual(apply(tuple(zip(*B)),v),(3,5))
        self.assertNotEqual(apply(tuple(zip(*B)),v),coordinates(B,v))
        orth=((0,-1),(1,0))
        self.assertEqual(inverse(orth),tuple(zip(*orth)))

    def test_contracts(self):
        for B in (((1,2),(2,4)),((0,0),(0,0)),[[1,2]],[[True,0],[0,1]],[[1.,0],[0,1]]):
            with self.assertRaises(ValueError):coordinates(B,(1,2))
        for v in ((1,),[1,2,3],(True,2),(1.,2)):
            with self.assertRaises(ValueError):coordinates(I,v)
