import unittest
from fractions import Fraction as Q
from .experiment import plane_projection,line_projection,dot

class DistanceTests(unittest.TestCase):
    def test_plane_projection_belongs_and_minimizes(self):
        n=(1,1,1);d=1;R=(1,1,1)
        result=plane_projection(R,n,d);H=result['foot']
        self.assertEqual(H,(Q(1,3),)*3)
        self.assertEqual(dot(n,H),d)
        self.assertEqual(result['squared_distance'],Q(4,3))
        for s in range(-3,4):
            for t in range(-3,4):
                T=(1-s-t,s,t)
                dist=sum((r-x)**2 for r,x in zip(R,T))
                offset=sum((h-x)**2 for h,x in zip(H,T))
                self.assertEqual(dist,result['squared_distance']+offset)

    def test_plane_rescaling_and_coordinate_units(self):
        R=(2,-1,3);n=(1,2,-1);d=3
        first=plane_projection(R,n,d)
        for scale in (-3,-1,2,5):
            other=plane_projection(R,tuple(scale*c for c in n),scale*d)
            self.assertEqual(other['foot'],first['foot'])
            self.assertEqual(other['squared_distance'],first['squared_distance'])
            self.assertEqual(other['residual'],scale*first['residual'])
        converted=plane_projection(tuple(100*r for r in R),n,100*d)
        self.assertEqual(converted['squared_distance'],10000*first['squared_distance'])

    def test_line_orthogonality_and_global_minimum(self):
        R=(3,4,0);P=(0,0,0);v=(1,0,0)
        r=line_projection(R,P,v)
        self.assertEqual(r['foot'],(3,0,0));self.assertEqual(r['squared_distance'],16)
        for v in ((1,0,0),(2,-1,2),(0,0,1)):
            result=line_projection(R,P,v)
            self.assertEqual(dot(result['residual'],v),0)
            for t in (Q(-2),Q(0),Q(1,2),Q(4)):
                T=tuple(t*c for c in v)
                self.assertEqual(sum((x-y)**2 for x,y in zip(R,T)),result['squared_distance']+sum((x-y)**2 for x,y in zip(result['foot'],T)))
        self.assertEqual(line_projection(R,P,(-2,0,0))['foot'],r['foot'])

    def test_zero_distance_and_contracts(self):
        self.assertEqual(plane_projection((1,0,0),(1,1,1),1)['squared_distance'],0)
        with self.assertRaises(ValueError):plane_projection((0,0,0),(0,0,0),1)
        with self.assertRaises(ValueError):line_projection((1,2,3),(0,0,0),(0,0,0))
        for R in ((1,2),(1,2,True),(1,2,.5)):
            with self.assertRaises(ValueError):plane_projection(R,(1,0,0),1)

if __name__=='__main__':unittest.main()
