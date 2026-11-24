import unittest
from fractions import Fraction as Q
from .experiment import point,slope_y,slope_x,second_y,tangent_vector,rational_point

class ImplicitTests(unittest.TestCase):
    def test_tangent_against_parametric_derivative(self):
        for numerator in range(-20,21):
            t=Q(numerator,7);x,y=rational_point(t)
            self.assertEqual(x*x+y*y,25)
            tx,ty=tangent_vector(x,y)
            self.assertEqual(x*tx+y*ty,0)
            dx=-20*t/(1+t*t)**2
            dy=10*(1-t*t)/(1+t*t)**2
            self.assertEqual(x*dx+y*dy,0)
            if dx:self.assertEqual(slope_y(x,y),dy/dx)

    def test_second_derivative_by_explicit_branch(self):
        # y=s sqrt(25−x²): y″=−s*25/(25−x²)^(3/2).
        for x,y in ((3,4),(3,-4),(4,3),(4,-3),(0,5),(0,-5)):
            s=1 if y>0 else -1
            expected=-Q(s*25,abs(y)**3)
            self.assertEqual(second_y(x,y),expected)
            self.assertEqual(y*second_y(x,y)+slope_y(x,y)**2+1,0)

    def test_chart_switch_and_branches(self):
        self.assertEqual(slope_y(3,4),Q(-3,4))
        self.assertEqual(slope_y(3,-4),Q(3,4))
        self.assertEqual(slope_y(0,5),0)
        self.assertEqual(slope_x(5,0),0)
        with self.assertRaises(ValueError):slope_y(5,0)
        with self.assertRaises(ValueError):slope_x(0,5)

    def test_contracts(self):
        for pair in ((1,1),(0,0),(3.0,4),(True,0)):
            with self.assertRaises(ValueError):point(*pair)
        with self.assertRaises(ValueError):second_y(5,0)
        with self.assertRaises(ValueError):rational_point(.5)

if __name__=='__main__':unittest.main()
