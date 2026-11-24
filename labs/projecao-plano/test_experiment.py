import unittest
from fractions import Fraction as F
from itertools import product
from .experiment import P,U,V,N,dot,apply,project,model

class PlaneProjection(unittest.TestCase):
    def test_independent_gram_construction(self):
        a=tuple(zip(U,V));gram=tuple(tuple(dot(col1,col2) for col2 in (U,V)) for col1 in (U,V))
        self.assertEqual(gram,((2,1),(1,2)))
        determinant=gram[0][0]*gram[1][1]-gram[0][1]*gram[1][0]
        inverse=((F(gram[1][1],determinant),F(-gram[0][1],determinant)),(F(-gram[1][0],determinant),F(gram[0][0],determinant)))
        independent=tuple(tuple(sum(a[i][k]*inverse[k][l]*a[j][l] for k in range(2) for l in range(2)) for j in range(3)) for i in range(3))
        self.assertEqual(independent,P)
        self.assertEqual(tuple(zip(*P)),P)
        self.assertEqual(tuple(tuple(dot(row,col) for col in zip(*P)) for row in P),P)
        self.assertEqual(project(U),U);self.assertEqual(project(V),V);self.assertEqual(project(N),(0,0,0))

    def test_grid_and_closest_point_identity(self):
        for x,y,z in product(range(-2,3),repeat=3):
            for s in range(-2,3):
                r=model(x,y,z,s);b,p,res=r['b'],r['p'],r['residual']
                self.assertEqual(dot(p,N),0);self.assertEqual(dot(res,U),0);self.assertEqual(dot(res,V),0)
                self.assertEqual(tuple(a+c for a,c in zip(p,res)),b)
                self.assertEqual(r['b_squared'],r['p_squared']+r['residual_squared'])
                self.assertEqual(r['candidate_error_squared'],r['residual_squared']+2*s*s)
                self.assertEqual(tuple(r['coefficients'][0]*u+r['coefficients'][1]*v for u,v in zip(U,V)),p)
            for a,c in product(range(-2,3),repeat=2):
                q=tuple(a*u+c*v for u,v in zip(U,V));error=tuple(v-w for v,w in zip(b,q));delta=tuple(v-w for v,w in zip(p,q))
                self.assertEqual(dot(error,error),dot(res,res)+dot(delta,delta))

    def test_redundant_generators_and_naive_counterexample(self):
        for b in product(range(-2,3),repeat=3):
            r=model(*b);a,c=r['coefficients']
            for t in range(-2,3):
                recomposed=tuple((a-t)*u+(c-t)*v+t*(u+v) for u,v in zip(U,V))
                self.assertEqual(recomposed,r['p'])
        r=model();self.assertEqual(r['naive'],(1,1,2))
        self.assertEqual(r['naive_dot_u'],-1);self.assertEqual(r['naive_dot_v'],-1)

    def test_slice_and_contracts(self):
        for b in product(range(-2,3),repeat=3):
            for s in range(-2,3):
                r=model(*b,s);bp,pp,qp=r['points']
                self.assertAlmostEqual((bp[0]-pp[0])**2+(bp[1]-pp[1])**2,float(r['residual_squared']))
                self.assertAlmostEqual((bp[0]-qp[0])**2+(bp[1]-qp[1])**2,float(r['candidate_error_squared']))
        self.assertEqual(model(-1,-1,1,0)['p'],(0,0,0))
        self.assertEqual(model(1,0,1,0)['residual'],(0,0,0))
        for args in [(3,0,0,0),(True,0,0,0),(0,0,0,.5)]:
            with self.assertRaises(ValueError):model(*args)
