import unittest
from fractions import Fraction as Q
from .experiment import point_at,parameter,through

class LineTests(unittest.TestCase):
    def test_recover_parameter_and_collinearity(self):
        P=(1,2,-1)
        for v in ((2,-1,2),(0,0,1),(0,2,-1),(1,0,0)):
            for t in (Q(-3,2),0,Q(1,4),2):
                R=point_at(P,v,t)
                self.assertEqual(parameter(P,v,R),t)
                d=tuple(r-p for r,p in zip(R,P))
                cross=(d[1]*v[2]-d[2]*v[1],d[2]*v[0]-d[0]*v[2],d[0]*v[1]-d[1]*v[0])
                self.assertEqual(cross,(0,0,0))
        self.assertIsNone(parameter(P,(2,-1,2),(5,0,4)))

    def test_reparametrization_does_not_change_line(self):
        P=(1,2,-1);v=(2,-1,2)
        for scale in (-3,-1,2,5):
            w=tuple(scale*d for d in v)
            for t in (-2,0,3):
                R=point_at(P,v,t)
                self.assertEqual(parameter(P,w,R),Q(t,scale))
                P2=point_at(P,v,1)
                self.assertEqual(parameter(P2,v,R),t-1)

    def test_two_points_and_projection_counterexample(self):
        P,v=through((1,2,-1),(5,0,3))
        self.assertEqual(v,(4,-2,4))
        self.assertEqual(point_at(P,v,1),(5,0,3))
        self.assertEqual(point_at(P,v,0),P)
        R=(5,0,4);S=(5,0,3)
        self.assertEqual(R[:2],S[:2])
        self.assertIsNone(parameter(P,v,R))
        self.assertEqual(parameter(P,v,S),1)
        self.assertEqual(parameter((1,2,-1),(0,0,1),(1,2,8)),9)

    def test_contracts(self):
        with self.assertRaises(ValueError):point_at((0,0,0),(0,0,0),1)
        with self.assertRaises(ValueError):through((1,2,3),(1,2,3))
        for P in ((1,2),(1,2,True),(1,2,.5)):
            with self.assertRaises(ValueError):point_at(P,(1,0,0),1)

if __name__=='__main__':unittest.main()
