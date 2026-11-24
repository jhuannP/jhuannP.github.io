import unittest
from fractions import Fraction as Q
from .sections import annulus,cone_sums,polynomial_integral


class SectionsTests(unittest.TestCase):
    def test_geometry_examples(self):
        self.assertEqual(annulus(0,1,(0,1)),Q(1,3))
        self.assertEqual(annulus(0,1,(1,1),(0,1)),2)
        self.assertEqual(annulus(0,1,(2,0),(2,-1)),Q(5,3))
        self.assertEqual(annulus(0,2,(3,0),(1,0)),16)
        self.assertEqual(annulus(0,1,(1,1),(1,1)),0)

    def test_slicing_and_cubic_scaling(self):
        for L in (Q(1,2),Q(1),Q(2)):
            for h in (L,2*L,3*L):
                v=annulus(0,L,(h,0),(h,-1))
                self.assertEqual(v,h*L*L-L**3/3)
                for cut in (L/4,L/2,3*L/4):
                    self.assertEqual(v,annulus(0,cut,(h,0),(h,-1))+annulus(cut,L,(h,0),(h,-1)))
                for k in (Q(1,2),2,3):
                    self.assertEqual(annulus(0,k*L,(k*h,0),(k*h,-1)),k**3*v)

    def test_sums_and_error(self):
        for n in range(1,65):
            left,mid,right=cone_sums(n)
            self.assertLess(left,Q(1,3));self.assertGreater(right,Q(1,3))
            self.assertEqual(Q(1,3)-mid,Q(1,12*n*n))
            self.assertEqual(right-left,Q(1,n))

    def test_contracts(self):
        for args in [(0,1,(1,0),(2,0)),(0,1,(1,0),(0,-1)),(1,0,(1,0)),(0,1,(1.0,0))]:
            with self.assertRaises(ValueError):annulus(*args)
        for n in (0,-1,True,1.0):
            with self.assertRaises(ValueError):cone_sums(n)
        self.assertEqual(polynomial_integral((0,0,1),0,1),Q(1,3))


if __name__=='__main__':unittest.main()
