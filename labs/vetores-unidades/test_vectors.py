import unittest
from fractions import Fraction as Q
from itertools import product
from .vectors import vector, add, scale, dot, norm_squared, quarter_turn_axes, project


class VectorTests(unittest.TestCase):
    def test_work_and_displacement(self):
        start, end = (1,2),(4,6)
        dr = add(end,scale(-1,start))
        self.assertEqual(dr,(3,4))
        self.assertEqual(norm_squared(dr),25)
        self.assertEqual(dot((2,-1),dr),2)
        self.assertEqual(dot((-2,0),(3,0)),-6)
        self.assertEqual(dot((0,2),(3,0)),0)
        self.assertEqual(dot((2,-1),add((3,0),(0,4))),6-4)

    def test_quarter_turn_changes_components_preserves_geometry(self):
        vectors=list(product(range(-4,5),repeat=2))
        for a in vectors:
            transformed=quarter_turn_axes(a)
            self.assertEqual(transformed,(a[1],-a[0]))
            self.assertEqual(norm_squared(transformed),norm_squared(a))
            self.assertEqual(quarter_turn_axes(quarter_turn_axes(transformed)),(-a[1],a[0]))
            self.assertEqual(quarter_turn_axes(quarter_turn_axes(quarter_turn_axes(transformed))),a)
            for b in vectors:
                self.assertEqual(dot(transformed,quarter_turn_axes(b)),dot(a,b))
                # 2D Lagrange identity independently connects dot, determinant and lengths.
                self.assertEqual(dot(a,b)**2+(a[0]*b[1]-a[1]*b[0])**2,norm_squared(a)*norm_squared(b))

    def test_projection_residual_and_idempotence(self):
        for a in product(range(-2,3),repeat=2):
            for direction in product(range(-2,3),repeat=2):
                if direction==(0,0):continue
                parallel=project(a,direction)
                residual=add(a,scale(-1,parallel))
                self.assertEqual(dot(residual,direction),0)
                self.assertEqual(project(parallel,direction),parallel)
                self.assertEqual(project(a,scale(-3,direction)),parallel)
                self.assertEqual(norm_squared(a),norm_squared(parallel)+norm_squared(residual))
        self.assertEqual(project((2,-1),(3,4)),(Q(6,25),Q(8,25)))

    def test_affine_origin_and_unit_conversion(self):
        a,b=(Q(1,3),Q(2,5)),(Q(4,3),Q(-3,5))
        shift=(17,-25)
        self.assertEqual(add(add(b,shift),scale(-1,add(a,shift))),add(b,scale(-1,a)))
        self.assertEqual(Q(36)*1000/3600,10)
        F,dr=(2,-1),(3,4)
        # Same displacement represented in cm: numerical dot is 200 N cm = 2 J.
        self.assertEqual(dot(F,scale(100,dr))/100,dot(F,dr))
        self.assertEqual(add(a,b),(Q(5,3),Q(-1,5)))

    def test_dot_linearity(self):
        for a,b,c in [((1,2),(3,-4),(5,6)),((Q(1,3),0),(0,Q(1,5)),(-1,2))]:
            self.assertEqual(dot(a,add(b,c)),dot(a,b)+dot(a,c))
            self.assertEqual(dot(scale(Q(-2,3),a),b),Q(-2,3)*dot(a,b))
            self.assertEqual(dot(a,b),dot(b,a))

    def test_contracts_and_zero(self):
        for bad in [(),(1,), (1,2,3),'12',(True,0),(1.0,2),(1,'2')]:
            with self.subTest(bad=bad),self.assertRaises(ValueError):vector(bad)
        for bad in [True,1.0,'2']:
            with self.assertRaises(ValueError):scale(bad,(1,2))
        with self.assertRaises(ValueError):project((1,2),(0,0))
        self.assertEqual(project((0,0),(1,2)),(0,0))
        self.assertEqual(norm_squared((0,0)),0)

if __name__=='__main__':unittest.main()
