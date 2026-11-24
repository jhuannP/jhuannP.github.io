import unittest
from fractions import Fraction as Q
from .experiment import plane_from_points,residual,intersect

class PlaneTests(unittest.TestCase):
    def test_plane_from_points_against_parametric_span(self):
        A=(1,0,0);B=(0,1,0);C=(0,0,1)
        n,d=plane_from_points(A,B,C)
        self.assertEqual((n,d),((1,1,1),1))
        for s in (Q(-1),Q(0),Q(1,2),Q(2)):
            for t in (Q(-1),Q(0),Q(1,2),Q(2)):
                R=(1-s-t,s,t)
                self.assertEqual(residual(n,d,R),0)
        self.assertNotEqual(residual(n,d,(0,0,0)),0)

    def test_three_line_incidence_cases(self):
        n=(1,2,-1);d=3
        r=intersect(n,d,(0,0,0),(1,0,0))
        self.assertEqual(r,dict(kind='unique',parameter=3,point=(3,0,0)))
        self.assertEqual(intersect(n,d,(0,0,0),(2,-1,0))['kind'],'parallel')
        self.assertEqual(intersect(n,d,(3,0,0),(2,-1,0))['kind'],'contained')
        for k in range(-3,4):self.assertEqual(residual(n,d,(3+2*k,-k,0)),0)

    def test_scaling_and_exact_substitution(self):
        for scale in (-3,-1,2,5):
            n=tuple(scale*c for c in (1,2,-1));d=3*scale
            for P,v in (((0,0,0),(1,0,0)),((0,0,0),(2,-1,0)),((3,0,0),(2,-1,0))):
                self.assertEqual(intersect(n,d,P,v),intersect((1,2,-1),3,P,v))
        for x in range(-2,3):
            for y in range(-2,3):
                r=intersect((1,2,-1),3,(x,y,0),(0,0,1))
                self.assertEqual(r['point'],(x,y,x+2*y-3))
                self.assertEqual(residual((1,2,-1),3,r['point']),0)

    def test_degeneracies_and_contracts(self):
        with self.assertRaises(ValueError):plane_from_points((0,0,0),(1,1,1),(2,2,2))
        with self.assertRaises(ValueError):residual((0,0,0),0,(1,2,3))
        with self.assertRaises(ValueError):intersect((1,0,0),1,(0,0,0),(0,0,0))
        for n in ((1,2),(1,2,True),(1,2,.5)):
            with self.assertRaises(ValueError):residual(n,1,(0,0,0))

if __name__=='__main__':unittest.main()
