import itertools,unittest
from fractions import Fraction as Q
from .linear import apply,det,area,preimage_invertible
MATRICES=[((a,b),(c,d)) for a,b,c,d in itertools.product((-1,0,1),repeat=4)]

class LinearTests(unittest.TestCase):
    def test_original_and_singular_fibres(self):
        A=((2,1),(0,1));self.assertEqual(apply(A,(1,2)),(4,2))
        self.assertEqual(apply(A,(1,0)),(2,0));self.assertEqual(apply(A,(0,1)),(1,1))
        B=((1,2),(2,4));self.assertEqual(apply(B,(-2,1)),(0,0))
        for k in range(-10,11):
            t=Q(k,3);self.assertEqual(apply(B,(3-2*t,t)),(3,6))
        # Toda imagem tem segunda coordenada igual ao dobro da primeira.
        for x,y in itertools.product(range(-3,4),repeat=2):
            out=apply(B,(x,y));self.assertEqual(out[1],2*out[0]);self.assertNotEqual(out,(3,5))

    def test_linearity_and_columns(self):
        for A in MATRICES:
            col1,col2=apply(A,(1,0)),apply(A,(0,1))
            for x,y in itertools.product(range(-2,3),repeat=2):
                self.assertEqual(apply(A,(x,y)),tuple(x*u+y*v for u,v in zip(col1,col2)))
            u,v=(Q(1,2),-2),(3,Q(2,3));alpha,beta=Q(2,3),-3
            lhs=apply(A,tuple(alpha*x+beta*y for x,y in zip(u,v)))
            rhs=tuple(alpha*x+beta*y for x,y in zip(apply(A,u),apply(A,v)))
            self.assertEqual(lhs,rhs)

    def test_area_by_independent_polygons(self):
        polygons=[((0,0),(1,0),(1,1),(0,1)),((1,2),(3,1),(-1,4)),((0,0),(2,0),(0,-3))]
        for A in MATRICES:
            for polygon in polygons:
                transformed=tuple(apply(A,v) for v in polygon)
                self.assertEqual(area(transformed),det(A)*area(polygon))
        self.assertEqual(area(((0,0),(2,0),(3,1),(1,1))),2)

    def test_roundtrip_and_affine_counterexample(self):
        for A in MATRICES:
            if not det(A):continue
            for v in ((0,0),(1,2),(Q(1,3),Q(-2,5))):
                self.assertEqual(preimage_invertible(A,apply(A,v)),v)
        A=((2,1),(0,1));offset=(1,0)
        def affine(v):return tuple(x+b for x,b in zip(apply(A,v),offset))
        self.assertNotEqual(affine((0,0)),(0,0))
        self.assertNotEqual(affine((2,0)),tuple(2*x for x in affine((1,0))))

    def test_contracts_and_nonmutation(self):
        A=[[2,1],[0,1]];v=[1,2];apply(A,v)
        self.assertEqual(A,[[2,1],[0,1]]);self.assertEqual(v,[1,2])
        for bad in (True,1.,'1'):
            with self.assertRaises(ValueError):apply([[bad,0],[0,1]],v)
        with self.assertRaises(ValueError):apply([[1,0]],v)
        with self.assertRaises(ValueError):apply(A,[1])
        with self.assertRaises(ValueError):preimage_invertible([[1,2],[2,4]],(3,6))
        with self.assertRaises(ValueError):area(((0,0),(1,0)))
