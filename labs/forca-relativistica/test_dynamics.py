import math
import unittest
from decimal import Decimal,localcontext
from .dynamics import trajectory,acceleration

class DynamicsTests(unittest.TestCase):
    def test_exact_rational_landmarks(self):
        # Triângulos 3-4-5 conferem pontos sem reutilizar sqrt do núcleo.
        for q,g,b,X,A in ((0,1,0,0,1),(3/4,5/4,3/5,1/4,64/125),(4/3,5/3,4/5,2/3,27/125)):
            z=trajectory(q)
            for key,value in (("gamma",g),("beta",b),("X",X),("A",A)):
                self.assertAlmostEqual(z[key],value,places=13)

    def test_high_precision_energy_and_small_displacement(self):
        with localcontext() as c:
            c.prec=70
            for text in ("0.00000001","0.001","0.25","0.75","2","10","10000"):
                q=Decimal(text);g=(1+q*q).sqrt();z=trajectory(float(q))
                for key,expected in (("gamma",g),("beta",q/g),("X",g-1),("A",1/g**3)):
                    self.assertTrue(math.isclose(z[key],float(expected),rel_tol=2e-14,abs_tol=1e-28))
                self.assertLess(z['beta'],1)
                self.assertGreaterEqual(z['X'],0)

    def test_trajectory_derivatives(self):
        h=1e-5
        for q in (0.1,0.3,0.75,1,4):
            z=trajectory(q);left=trajectory(q-h);right=trajectory(q+h)
            self.assertAlmostEqual((right['X']-left['X'])/(2*h),z['beta'],places=8)
            self.assertAlmostEqual((right['beta']-left['beta'])/(2*h),z['A'],places=8)
            self.assertAlmostEqual((right['gamma']-left['gamma'])/(2*h),z['beta'],places=8)

    def test_vector_momentum_derivative(self):
        # Diferencia p(v)=m gamma v numericamente, independente da inversa usada no núcleo.
        h=1e-6
        for b in ((0,0,0),(.6,0,0),(.2,-.3,.1)):
            for f in ((1,0,0),(0,1,0),(1,-2,3)):
                for m in (1,2):
                    a=acceleration(b,f,m)
                    def momentum(v):
                        g=1/math.sqrt(1-sum(x*x for x in v));return [m*g*x for x in v]
                    plus=momentum([x+h*y for x,y in zip(b,a)]);minus=momentum([x-h*y for x,y in zip(b,a)])
                    for i in range(3): self.assertAlmostEqual((plus[i]-minus[i])/(2*h),f[i],places=7)
        self.assertEqual(acceleration((0,0,0),(2,4,6),2),(1,2,3))

    def test_contracts(self):
        for q in (-1,10001,True,float('inf'),float('nan'),'2'):
            with self.assertRaises(ValueError):trajectory(q)
        for b,f,m in (((1,0,0),(1,0,0),1),((0,0,0),(1,0,0),0),((0,0),(1,0,0),1),((0,0,0),(float('inf'),0,0),1)):
            with self.assertRaises(ValueError):acceleration(b,f,m)
