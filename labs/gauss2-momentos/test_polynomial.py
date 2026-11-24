import unittest,itertools
from fractions import Fraction as Q
from .polynomial import gauss2,integral

class GaussTests(unittest.TestCase):
    def test_cubics(self):
        for coeff in itertools.product(range(-2,3),repeat=4):
            for a,b in [(-1,1),(0,1),(2,5)]:
                self.assertEqual(gauss2(coeff,a,b),integral(coeff,a,b))
    def test_quartic_and_refinement(self):
        for a,b in [(-1,1),(0,1),(2,5)]:
            f=[2,-1,3,2,1]
            for n in (1,2,4,8):
                error=integral(f,a,b)-gauss2(f,a,b,n)
                self.assertEqual(error,Q((b-a)**5,180*n**4))
        f=[Q(1,9),0,Q(-2,3),0,1]
        self.assertEqual(gauss2(f,-1,1),0);self.assertEqual(integral(f,-1,1),Q(8,45))
        self.assertEqual(gauss2(f,-1,1,2),Q(1,6))
    def test_linearity_and_affine_mapping(self):
        f=[1,-2,0,3,2];g=[-1,0,2,1,-3]
        combined=[2*x-3*y for x,y in zip(f,g)]
        for n in (1,2,4):self.assertEqual(gauss2(combined,2,5,n),2*gauss2(f,2,5,n)-3*gauss2(g,2,5,n))
        self.assertEqual(gauss2([3],2,5),9)
        # (x−2)^4 em [2,5] versus t^4 em [0,1], dx=3dt.
        self.assertEqual(gauss2([16,-32,24,-8,1],2,5),3**5*gauss2([0,0,0,0,1],0,1))
    def test_contracts(self):
        for args in [([],0,1,1),([True],0,1,1),([1.0],0,1,1),([1],1,0,1),([1],0,1,True),([1],0,1,0),([1],0,1,33),([1]*10,0,1,1)]:
            with self.assertRaises(ValueError):gauss2(*args)
