from fractions import Fraction as Q
import math
import unittest
from .wire import enclosed,reduced_bphi,reduced_field


class WireTests(unittest.TestCase):
    def test_enclosed_against_uniform_density_radial_integral(self):
        # Integral de J*2*pi*s ds; J=I/(pi*a*a).
        for a in (Q(1,500),Q(1,2),Q(3)):
            for current in (-7,0,6):
                for ratio in (Q(0),Q(1,4),Q(1,2),Q(1),Q(2),Q(5)):
                    r=a*ratio;limit=min(r,a);n=20;h=limit/n
                    integrated=sum((2*current/(a*a))*((i+Q(1,2))*h)*h for i in range(n))
                    self.assertEqual(enclosed(current,a,r),integrated)
                    if r:self.assertEqual(reduced_bphi(current,a,r)*r,integrated)

    def test_circulation_of_cartesian_field(self):
        current=Q(6);a=Q(1,500)
        for ratio in (.25,.5,1,2,5):
            r=float(a)*ratio;n=240;circulation=0
            for j in range(n):
                theta=2*math.pi*(j+.5)/n
                x,y=r*math.cos(theta),r*math.sin(theta)
                bx,by=reduced_field(current,a,Q(str(x)),Q(str(y)))
                circulation+=(-float(bx)*y+float(by)*x)*(2*math.pi/n)
            expected=2*math.pi*float(enclosed(current,a,Q(str(r))))
            self.assertAlmostEqual(circulation,expected,places=10)
            self.assertAlmostEqual(-circulation,-expected,places=10)

    def test_limits_scaling_and_example(self):
        a=Q(1,500);current=Q(6)
        self.assertEqual(reduced_bphi(current,a,0),0)
        self.assertEqual(reduced_field(current,a,0,0),(0,0))
        self.assertEqual(reduced_bphi(current,a,Q(1,1000)),1500)
        self.assertEqual(reduced_bphi(current,a,a),3000)
        self.assertEqual(reduced_bphi(current,a,Q(1,250)),1500)
        for eps in (Q(1,10),Q(1,1000),Q(1,10**12)):
            left=reduced_bphi(current,a,a*(1-eps))
            right=reduced_bphi(current,a,a*(1+eps))
            peak=reduced_bphi(current,a,a)
            self.assertEqual(left,peak*(1-eps))
            self.assertEqual(right,peak/(1+eps))
        for r in (a/4,a/2,a,2*a,4*a):
            self.assertEqual(reduced_bphi(-current,a,r),-reduced_bphi(current,a,r))
            self.assertEqual(reduced_bphi(2*current,a,r),2*reduced_bphi(current,a,r))
            self.assertEqual(reduced_bphi(current,3*a,3*r),reduced_bphi(current,a,r)/3)
        self.assertEqual(reduced_field(current,a,2*a,0),(0,1500))
        self.assertEqual(reduced_field(current,a,0,2*a),(-1500,0))
        # Contorno envolvendo duas correntes opostas tem I total=0,
        # mas no ponto central as componentes dos dois campos somam.
        d=Q(1,50);wire_a=Q(1,200)
        b1=reduced_field(3,wire_a,d,0)
        b2=reduced_field(-3,wire_a,-d,0)
        self.assertEqual(tuple(x+y for x,y in zip(b1,b2)),(0,300))

    def test_biot_savart_finite_segment_independent_reference(self):
        # Para linha fina -L<z<L, substitua z=r*tan(theta).
        # O integrando reduzido é I*cos(theta)/(2*r).
        I=3.;r=.4;n=400
        for ratio in (1,2,5,20,100):
            limit=math.atan(ratio);h=2*limit/n
            f=lambda theta:I*math.cos(theta)/(2*r)
            quad=h/3*(f(-limit)+f(limit)+sum((4 if i%2 else 2)*f(-limit+i*h) for i in range(1,n)))
            finite=(I/r)*ratio/math.sqrt(1+ratio*ratio)
            infinite=float(reduced_bphi(3,Q(1,10),Q(2,5)))
            self.assertAlmostEqual(quad,finite,places=9)
            self.assertLess(finite,infinite)
            if ratio==100:self.assertLess((infinite-finite)/infinite,5e-5)

    def test_contracts(self):
        for bad in (True,.5,"1/2",None):
            with self.assertRaises(TypeError):reduced_bphi(bad,1,1)
            with self.assertRaises(TypeError):reduced_field(1,1,bad,0)
        for a in (0,-1):
            with self.assertRaises(ValueError):enclosed(1,a,1)
        with self.assertRaises(ValueError):reduced_bphi(1,1,-1)
        self.assertEqual(reduced_field(0,1,0,0),(0,0))

if __name__=="__main__":unittest.main()
