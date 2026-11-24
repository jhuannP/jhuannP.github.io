import unittest,math
from fractions import Fraction as F
from .cylinder import integral,midpoint,moments,point,inverse


class CylinderTests(unittest.TestCase):
    def test_cross_section_reference(self):
        volume,radial,vertical=moments()
        # At fixed z, quarter-annulus area coefficient is (3-z)/4.
        self.assertEqual(volume,integral((F(3,4),F(-1,4)),0,3))
        self.assertEqual(vertical,integral((0,F(3,4),F(-1,4)),0,3))
        # Integral of r² over quarter annulus, independently at fixed height.
        self.assertEqual(radial,integral((F(15,8),-1,F(1,8)),0,3))
        self.assertEqual((volume,radial,vertical),(F(9,8),F(9,4),F(9,8)))
        self.assertEqual(radial/volume,2);self.assertEqual(vertical/volume,1)

    def test_radial_quadrature_and_wrong_limit(self):
        for n in (1,2,4,8,16,31):
            err=midpoint(n)-F(9,8)
            wrong=midpoint(n,False)-F(5,6)
            self.assertEqual(err,F(3,16*n*n))
            self.assertEqual(wrong,F(1,24*n*n))
            self.assertEqual(err,4*(midpoint(2*n)-F(9,8)))
        self.assertEqual(midpoint(1),F(21,16))

    def test_cell_volume(self):
        # Remove common angular factor pi, q=Delta theta/pi.
        for a,b,q,h in [(1,2,F(1,2),3),(0,1,2,1),(2,3,F(1,4),2),(1,4,F(1,3),5)]:
            exact=(F(b*b-a*a)/2)*q*h
            local_mid=(F(a+b)/2)*(b-a)*q*h
            self.assertEqual(exact,local_mid)

    def test_points_and_local_volume(self):
        r,t,z=inverse(-1,math.sqrt(3),2)
        self.assertAlmostEqual(r,2);self.assertAlmostEqual(t,2*math.pi/3);self.assertEqual(z,2)
        for r in (.5,1,2):
            for t in (.1,.7,2,4,6):
                for z in (-1,3):
                    out=inverse(*point(r,t,z))
                    for x,y in zip(out,(r,t,z)):self.assertAlmostEqual(x,y)
        # Determinant of finite-difference coordinate columns, six chart points.
        for r in (.5,2):
            for t in (.3,2,5):
                q=(r,t,1);h=1e-5;cols=[]
                for j in range(3):
                    a=list(q);b=list(q);a[j]+=h;b[j]-=h
                    cols.append(tuple((x-y)/(2*h) for x,y in zip(point(*a),point(*b))))
                a,b,c=cols
                det=a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
                self.assertAlmostEqual(det,r,places=8)
        self.assertEqual(point(0,1,2),(0,0,2))
        with self.assertRaises(ValueError):inverse(0,0,2)

    def test_contracts(self):
        for n in (0,-1,True,1.5,10001):
            with self.assertRaises(ValueError):midpoint(n)
        with self.assertRaises(ValueError):midpoint(2,1)
        for q in [(-1,0,0),(True,0,0),(1,float('nan'),0),(1,1e7,0),(10**1000,0,0)]:
            with self.assertRaises(ValueError):point(*q)
        with self.assertRaises(ValueError):integral([1],2,1)

if __name__=='__main__':unittest.main()
