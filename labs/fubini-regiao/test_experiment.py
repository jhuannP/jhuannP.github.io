import unittest
from fractions import Fraction as Q
from .experiment import moment_dy_dx,moment_dx_dy,polynomial_integral,midpoint_example

class FubiniRegionTests(unittest.TestCase):
    def test_exact_moments_both_orders(self):
        for a in range(13):
            for b in range(13):
                self.assertEqual(moment_dy_dx(a,b),moment_dx_dy(a,b))
                self.assertGreater(moment_dy_dx(a,b),0)
        self.assertEqual(moment_dy_dx(0,0),Q(1,6))
        self.assertEqual(moment_dy_dx(1,0),Q(1,12))
        self.assertEqual(moment_dy_dx(0,1),Q(1,15))

    def test_example_and_wrong_mirrored_region(self):
        terms={(1,0):1,(0,1):2}
        self.assertEqual(polynomial_integral(terms),Q(13,60))
        self.assertEqual(polynomial_integral(terms,'dx_dy'),Q(13,60))
        wrong=polynomial_integral({(0,1):1,(1,0):2})
        self.assertEqual(wrong,Q(7,30));self.assertNotEqual(wrong,Q(13,60))
        # Área é preservada pelo espelhamento, portanto não detecta esta troca.
        self.assertEqual(moment_dy_dx(0,0),moment_dx_dy(0,0))
        x,y=Q(1,2),Q(3,8)
        self.assertTrue(x*x<=y<=x)
        self.assertFalse(y*y<=x<=y)

    def test_vertical_and_horizontal_membership(self):
        for i in range(17):
            for j in range(17):
                x,y=Q(i,16),Q(j,16)
                vertical=(0<=x<=1 and x*x<=y<=x)
                # x<=sqrt(y) equivale a x*x<=y para x>=0.
                horizontal=(0<=y<=1 and y<=x and x>=0 and x*x<=y)
                self.assertEqual(vertical,horizontal)

    def test_independent_midpoint_refinement(self):
        exact=13/60
        errors=[abs(midpoint_example(n)-exact) for n in (10,20,40)]
        self.assertGreater(errors[0],errors[1]);self.assertGreater(errors[1],errors[2])
        self.assertLess(errors[2],1e-4)

    def test_linearity_and_contract(self):
        self.assertEqual(polynomial_integral({(0,0):3,(1,0):-2}),3*Q(1,6)-2*Q(1,12))
        self.assertEqual(polynomial_integral({}),0)
        for a,b in [(-1,0),(0,21),(True,0),(1.,0)]:
            with self.assertRaises(ValueError):moment_dy_dx(a,b)
        for terms,order in [({(0,0):.5},'dy_dx'),({'x':1},'dy_dx'),({},'bad')]:
            with self.assertRaises(ValueError):polynomial_integral(terms,order)
        for n in (0,257,True,2.):
            with self.assertRaises(ValueError):midpoint_example(n)
