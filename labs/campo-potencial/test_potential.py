import unittest,itertools,math
from fractions import Fraction as Q
from .potential import phi,field,segment,path,vortex

class PotentialTests(unittest.TestCase):
    def test_reference_routes_and_original_example(self):
        self.assertEqual(path([(0,0),(1,2)]),9)
        self.assertEqual(path([(0,0),(1,0),(1,2)]),9)
        self.assertEqual(phi((1,2))-phi((0,0)),9)
        # Original phi=xy and diagonal r=(t,t) gives integral 2t =1.
        values=[2*Q(i,2) for i in range(3)]
        self.assertEqual((values[0]+4*values[1]+values[2])/6,1)
    def test_exact_segments_telescoping_and_reversal(self):
        points=list(itertools.product([-1,0,2],repeat=2));count=0
        for a,b in itertools.product(points,repeat=2):
            self.assertEqual(segment(a,b),phi(b)-phi(a))
            self.assertEqual(segment(b,a),-segment(a,b));count+=1
        self.assertEqual(count,81)
        for a,b,c in itertools.product(points[:3],repeat=3):
            self.assertEqual(path([a,b,c]),phi(c)-phi(a))
            self.assertEqual(path([a,b,c,a]),0)
    def test_circle_and_two_semicircles_by_geometry(self):
        def integrate(radius,start,end,n=128):
            h=(end-start)/n;values=[]
            for i in range(n+1):
                theta=start+i*h
                x,y=radius*math.cos(theta),radius*math.sin(theta)
                u,v=vortex(x,y)
                values.append(u*(-radius*math.sin(theta))+v*(radius*math.cos(theta)))
            return h/3*(values[0]+values[-1]+4*sum(values[1:-1:2])+2*sum(values[2:-1:2]))
        for radius in [.25,1,3]:
            for turns in [-2,-1,1,2]:self.assertAlmostEqual(integrate(radius,.3,.3+2*math.pi*turns),2*math.pi*turns,places=12)
        self.assertAlmostEqual(integrate(1,0,math.pi),math.pi)
        self.assertAlmostEqual(integrate(1,0,-math.pi),-math.pi)
        self.assertAlmostEqual(integrate(1,0,2*math.pi)+integrate(.5,2*math.pi,0),0)
    def test_local_angle_and_curl(self):
        h=1e-5
        for x,y in [(1.,0.),(2.,1.),(.5,-.3)]:
            u,v=vortex(x,y)
            # Local potential on x>0, atan(y/x), independent FD check.
            ux=(math.atan(y/(x+h))-math.atan(y/(x-h)))/(2*h)
            uy=(math.atan((y+h)/x)-math.atan((y-h)/x))/(2*h)
            self.assertAlmostEqual(u,ux,delta=2e-9);self.assertAlmostEqual(v,uy,delta=2e-9)
            qx=(vortex(x+h,y)[1]-vortex(x-h,y)[1])/(2*h)
            py=(vortex(x,y+h)[0]-vortex(x,y-h)[0])/(2*h)
            self.assertAlmostEqual(qx-py,0,delta=2e-9)
    def test_contracts_and_nonconservative_counterexample(self):
        # F=(0,x): unit-square integral 1 by the two vertical edges.
        self.assertEqual(Q(1)*1+Q(0)*(-1),1)
        for v in [(0,0),(True,1),(float('nan'),1),(float('inf'),1)]:
            with self.assertRaises(ValueError):vortex(*v)
        for vertices in [[],[(0,0)],[(0,0),(1,)],[(0,0),(.5,1)]]:
            with self.assertRaises(ValueError):path(vertices)
