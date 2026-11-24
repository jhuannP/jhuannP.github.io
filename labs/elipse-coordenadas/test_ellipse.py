import unittest
from fractions import Fraction as Q
from itertools import product
from .ellipse import evaluate,reduce_definite,to_world,to_local


class EllipseTests(unittest.TestCase):
    def test_example_and_degeneracy(self):
        base=[36,-24,29,-120,140,20]
        r=reduce_definite(base)
        self.assertEqual(r['center'],(1,-2));self.assertEqual(r['rhs'],180);self.assertEqual(r['kind'],'elipse')
        self.assertEqual(reduce_definite(base[:-1]+[200])['kind'],'ponto')
        self.assertEqual(reduce_definite(base[:-1]+[201])['kind'],'vazio')
        self.assertEqual(to_world((1,-2),Q(3,5),Q(4,5),3,0),(Q(14,5),Q(2,5)))

    def test_constructed_centers_and_definite_cases(self):
        # Construct from independent weighted squares, then recover the center.
        for (c,s),(alpha,beta),(h,k),rho in product([(Q(1),Q(0)),(Q(3,5),Q(4,5)),(Q(-3,5),Q(4,5))],[(1,1),(2,5),(7,3)],list(product((-2,0,3),repeat=2)),(-1,0,1,2)):
            a=alpha*c*c+beta*s*s;b=2*c*s*(alpha-beta);cc=alpha*s*s+beta*c*c
            d=-2*a*h-b*k;e=-b*h-2*cc*k;f=a*h*h+b*h*k+cc*k*k-rho
            values=[a,b,cc,d,e,f];r=reduce_definite(values)
            self.assertEqual(r['center'],(h,k));self.assertEqual(r['rhs'],rho)
            self.assertEqual(r['kind'],'elipse' if rho>0 else 'ponto' if rho==0 else 'vazio')
            self.assertEqual(evaluate(values,h,k),-rho)

    def test_rational_parameter_points_and_coordinate_invariance(self):
        values=(36,-24,29,-120,140,20);center=(1,-2);c,s=Q(3,5),Q(4,5)
        parameters=[Q(i,2) for i in range(-10,11)]
        points=[(3*(1-t*t)/(1+t*t),4*t/(1+t*t)) for t in parameters]+[(-3,0)]
        for u,v in points:
            world=to_world(center,c,s,u,v)
            self.assertEqual(to_local(center,c,s,*world),(u,v))
            self.assertEqual(evaluate(values,*world),0)
            self.assertEqual(Q(u*u,9)+Q(v*v,4),1)
            self.assertEqual((world[0]-1)**2+(world[1]+2)**2,u*u+v*v)

    def test_polynomial_scaling_and_translation(self):
        values=(36,-24,29,-120,140,20)
        for factor in (-7,-1,Q(1,3),5):
            r=reduce_definite([factor*x for x in values])
            self.assertEqual(r['center'],(1,-2));self.assertEqual(r['kind'],'elipse')
        for x,y in product(range(-3,4),repeat=2):
            u,v=to_local((1,-2),Q(3,5),Q(4,5),x,y)
            self.assertEqual(evaluate(values,x,y),20*u*u+45*v*v-180)

    def test_contracts_and_scope(self):
        for values in [(1,0,-1,0,0,-1),(1,0,0,0,-1,0),(0,0,0,1,1,0),(True,0,1,0,0,-1),(1.0,0,1,0,0,-1)]:
            with self.assertRaises(ValueError):reduce_definite(values)
        with self.assertRaises(ValueError):to_world((0,0),1,1,1,0)
        with self.assertRaises(ValueError):evaluate((1,2),0,0)
