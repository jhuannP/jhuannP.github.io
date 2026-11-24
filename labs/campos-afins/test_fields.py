from fractions import Fraction as Q
from itertools import product
import unittest
from .fields import Affine,quadratic_gradient,vortex

class FieldTests(unittest.TestCase):
    def test_reference(self):
        f=Affine(((2,-3),(1,-1)),(1,2))
        self.assertEqual(f.at((1,2)),(-3,1))
        self.assertEqual(f.operators(),(1,4))
        self.assertEqual(f.square((0,0),2),(4,16))
        self.assertEqual(quadratic_gradient(1,0,1,(1,2)),(2,4))
        self.assertEqual(2*Q(3,5)+4*Q(4,5),Q(22,5))
    def test_edge_integrals_vs_derivatives(self):
        # O código integra arestas; referência por traço/antissimetria × área.
        for a,b,c,e in product((-1,0,2),repeat=4):
            f=Affine(((a,b),(c,e)),(3,-2))
            for origin,L in (((0,0),1),((2,-3),Q(1,3)),((-1,4),2)):
                self.assertEqual(f.square(origin,L),((a+e)*L*L,(c-b)*L*L))
    def test_gradient_by_independent_polynomial(self):
        for a,b,c in product((-1,0,2),repeat=3):
            for x,y in ((0,0),(1,2),(-2,Q(1,2))):
                phi=lambda u,v:a*u*u+b*u*v+c*v*v
                h=Q(1,7)
                direct=((phi(x+h,y)-phi(x-h,y))/(2*h),
                        (phi(x,y+h)-phi(x,y-h))/(2*h))
                self.assertEqual(quadratic_gradient(a,b,c,(x,y)),direct)
                f=Affine(((2*a,b),(b,2*c)))
                self.assertEqual(f.operators(),(2*a+2*c,0))
    def test_domain_vortex_and_old_material(self):
        for x,y in ((1,0),(0,2),(-3,4),(Q(3,5),Q(4,5))):
            fx,fy=vortex((x,y))
            # Derivada da parametrização circular por ângulo é(-y,x).
            self.assertEqual(fx*(-y)+fy*x,1)
        with self.assertRaises(ValueError):vortex((0,0))
        import json
        from pathlib import Path
        ls=json.loads((Path(__file__).resolve().parents[2]/'content/lessons.json').read_text())
        l=next(x for x in ls if x['id']=='campos-operadores')
        exec(l['python'],{});exec(l['codingPractice']['solution'],{})
    def test_contracts(self):
        for value in (True,1.0,'1'):
            with self.assertRaises(TypeError):Affine(((value,0),(0,1)))
        with self.assertRaises(ValueError):Affine(((1,),))
        f=Affine(((1,0),(0,1)))
        with self.assertRaises(ValueError):f.at((1,))
        for side in (0,-1):
            with self.assertRaises(ValueError):f.square((0,0),side)
if __name__=='__main__':unittest.main()
