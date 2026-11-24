import unittest
from fractions import Fraction as Q
from itertools import permutations
from .triangles import area,sides2,similarity_ratio2,parallel_cut,transform,shadow_height,sub,cross

T=((0,0),(15,0),(0,20))
class SimilarityTests(unittest.TestCase):
    def test_literal_and_correspondence(self):
        small=parallel_cut(T,Q(3,5))
        self.assertEqual(small,((0,0),(9,0),(0,12)))
        self.assertEqual(sides2(T),(225,400,625))
        self.assertEqual(sides2(small),(81,144,225))
        self.assertEqual(similarity_ratio2(T,small),Q(9,25))
        self.assertEqual(area(T),150);self.assertEqual(area(small),54)
        self.assertEqual(area(T)-area(small),96)
        for p in permutations(range(3)):
            self.assertEqual(similarity_ratio2(tuple(T[i] for i in p),tuple(small[i] for i in p)),Q(9,25))
        self.assertIsNone(similarity_ratio2(T,(small[0],small[2],small[1])))

    def test_192_rigid_transforms_and_scales(self):
        # Razão obtida de distâncias; área conferida por determinante.
        for a in [1,2,3,4]:
            for h in [1,3]:
                base=((0,0),(a,0),(1,h))
                for k in [Q(1,4),Q(3,5),Q(7,3)]:
                    for rotation in range(4):
                        for reflect in [False,True]:
                            new=transform(base,k,rotation,reflect,(Q(5,7),-2))
                            self.assertEqual(similarity_ratio2(base,new),k*k)
                            self.assertEqual(area(new)/area(base),k*k)

    def test_cuts_by_independent_intersection(self):
        # Sistema2x2 da reta por D paralela a BC com o raio AC; sem construir E pela função.
        for tri in [T,((1,2),(8,4),(3,9)),((-2,4),(0,-3),(6,5))]:
            A,B,C=tri;v=sub(C,A);w=sub(C,B)
            for k in [Q(1,4),Q(3,5),Q(2,3)]:
                small=parallel_cut(tri,k);D=small[1];u=sub(D,A)
                t=cross(u,w)/cross(v,w)
                E=tuple(Q(A[i])+t*v[i] for i in range(2))
                self.assertEqual(E,small[2])
                self.assertEqual(cross(sub(small[2],D),w),0)
                self.assertEqual(similarity_ratio2(tri,small),k*k)

    def test_area_by_lattice_count(self):
        # Pick: área=I+B/2−1, enumeração de pontos interiores/fronteiriços.
        for a,b in [(3,4),(5,7),(9,12),(15,20)]:
            inside=boundary=0
            for x in range(a+1):
                for y in range(b+1):
                    v=b*x+a*y
                    if v>a*b:continue
                    if x==0 or y==0 or v==a*b:boundary+=1
                    else:inside+=1
            self.assertEqual(area(((0,0),(a,0),(0,b))),inside+Q(boundary,2)-1)

    def test_nonuniform_and_shadow(self):
        self.assertIsNone(similarity_ratio2(T,((0,0),(30,0),(0,60))))
        # Ambos retângulos, só um ângulo não basta.
        self.assertIsNone(similarity_ratio2(((0,0),(3,0),(0,4)),((0,0),(3,0),(0,5))))
        self.assertEqual(shadow_height(Q(9,5),Q(27,10),Q(21,2)),7)
        for unit in [1,100,1000]:
            self.assertEqual(shadow_height(Q(9,5)*unit,Q(27,10)*unit,Q(21,2)*unit),7*unit)

    def test_contracts(self):
        for tri in [((0,0),(1,1),(2,2)),((0,0),(0,0),(2,2)),(),((0,0),(1,2))]:
            with self.assertRaises(ValueError):area(tri)
        for k in [0,1,-1,2]:
            with self.assertRaises(ValueError):parallel_cut(T,k)
        with self.assertRaises(TypeError):parallel_cut(T,.6)
        with self.assertRaises(TypeError):area(((True,0),(1,0),(0,1)))
        with self.assertRaises(ValueError):transform(T,0)
        with self.assertRaises(ValueError):transform(T,1,4)
        with self.assertRaises(TypeError):transform(T,1,reflected=1)
        with self.assertRaises(ValueError):shadow_height(1,0,5)
