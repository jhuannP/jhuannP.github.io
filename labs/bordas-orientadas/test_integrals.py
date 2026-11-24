import unittest
from fractions import Fraction as Q
from itertools import product
from math import pi,sqrt
from .integrals import edge_integral,stokes_rectangle,gauss_box


class BoundaryTests(unittest.TestCase):
    def test_reference(self):
        s=stokes_rectangle(2,3,1,1,2)
        self.assertEqual(s['edges'],(4,42,-10,-24))
        self.assertEqual((s['circulation'],s['curl_flux']),(12,12))
        g=gauss_box((1,2,3),(2,3,4))
        self.assertEqual(tuple(g['faces'].values()),(-12,36,-16,40,-18,42))
        self.assertEqual((g['flux'],g['divergence_integral']),(72,72))
        self.assertEqual(sum(v for k,v in g['faces'].items() if k.endswith('high')),118)

    def test_direct_line_quadrature(self):
        # 108 graphs x 4 edges; midpoint exact for this affine field on each segment.
        for a,b,c,p,q in product((1,2,3),(1,2),(-1,0,2),(-1,0,2),(-2,1)):
            s=stokes_rectangle(a,b,c,p,q)
            verts=s['vertices']
            independent=[]
            for i in range(4):
                A,B=verts[i],verts[(i+1)%4]
                mid=tuple((A[j]+B[j])/2 for j in range(3));delta=tuple(B[j]-A[j] for j in range(3))
                f=(-mid[1],mid[0],mid[2])
                independent.append(sum(f[j]*delta[j] for j in range(3)))
            self.assertEqual(tuple(independent),s['edges'])
            self.assertEqual(sum(independent),2*a*b)
            # Graph normal area vector (-p,-q,1); ordinary area is not a*b.
            self.assertEqual(sum(independent),Q(2,1)/Q(1)*a*b)

    def test_orientation_and_area(self):
        for p,q in product((-2,0,3),repeat=2):
            up=stokes_rectangle(2,3,1,p,q);down=stokes_rectangle(2,3,1,p,q,-1)
            self.assertEqual(down['circulation'],-up['circulation'])
            self.assertEqual(down['curl_flux'],-up['curl_flux'])
        self.assertAlmostEqual(2/sqrt(6)*6*sqrt(6),12)
        self.assertNotAlmostEqual(2/sqrt(6)*6,12)
        self.assertEqual(edge_integral((0,0,1),(2,0,3)),4)
        self.assertEqual(edge_integral((2,0,3),(0,0,1)),-4)

    def test_six_faces_independent_midpoints(self):
        # 81 translated boxes, normals explicitly attached to each of six faces.
        for lower,a,b,c in product(((0,0,0),(1,2,3),(-2,3,-1)),(1,2,3),(1,3,4),(2,3,4)):
            sizes=(a,b,c);actual=gauss_box(lower,sizes);summed=Q(0)
            for axis in range(3):
                area=Q(1)
                for j in range(3):
                    if j!=axis:area*=sizes[j]
                for side in (0,1):
                    mid=[Q(lower[j])+Q(sizes[j],2) for j in range(3)]
                    mid[axis]=lower[axis]+side*sizes[axis]
                    normal=-1 if side==0 else 1
                    flux=normal*mid[axis]*area
                    summed+=flux
                    self.assertEqual(flux,actual['faces']['xyz'[axis]+('_low' if side==0 else '_high')])
            self.assertEqual(summed,actual['divergence_integral'])

    def test_old_material_and_contracts(self):
        R=1;circulation=2*pi*R*R
        self.assertAlmostEqual(circulation/pi,2)
        self.assertAlmostEqual(3*(4*pi/3),4*pi)
        self.assertEqual((2*pi*2**2)/(2*pi),4)
        for args in [(0,2,0,0,0),(2,-1,0,0,0)]:
            with self.assertRaises(ValueError):stokes_rectangle(*args)
        for orientation in [0,True,2]:
            with self.assertRaises(ValueError):stokes_rectangle(1,1,0,0,0,orientation)
        with self.assertRaises(ValueError):gauss_box((0,0,0),(1,0,1))
        with self.assertRaises(TypeError):stokes_rectangle(1.,1,0,0,0)
        with self.assertRaises(ValueError):edge_integral((0,0),(1,1,1))
