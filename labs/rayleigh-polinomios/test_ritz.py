import unittest
from fractions import Fraction as Q
from math import pi,sin,cos
from .ritz import F,G,rayleigh,trial,matrices,normalized_characteristic,ritz_values,evaluate

def simpson(f,n=2048):
    h=1/n
    return h/3*(f(0)+f(1)+4*sum(f(j*h) for j in range(1,n,2))+2*sum(f(j*h) for j in range(2,n,2)))

class RitzTests(unittest.TestCase):
    def test_exact_matrices(self):
        H,M=matrices()
        self.assertEqual(H,((Q(1,3),Q(1,15)),(Q(1,15),Q(2,105))))
        self.assertEqual(M,((Q(1,30),Q(1,140)),(Q(1,140),Q(1,630))))
        self.assertEqual(normalized_characteristic(),(1008,-112,1))
        self.assertEqual(rayleigh(F),10)
        self.assertEqual(rayleigh(trial(1,1)),Q(306,31))

    def test_quadrature_reference(self):
        for a,b in ((1,0),(1,1),(2,-1),(-1,3)):
            fun=lambda x:a*x*(1-x)+b*x*x*(1-x)**2
            df=lambda x:a*(1-2*x)+2*b*x*(1-x)*(1-2*x)
            value=simpson(lambda x:df(x)**2)/simpson(lambda x:fun(x)**2)
            self.assertLess(abs(value-float(rayleigh(trial(a,b)))),2e-9)

    def test_stationary_ritz_pair(self):
        H,M=matrices();low,high=ritz_values()
        self.assertGreater(low,pi*pi);self.assertLess(low,306/31);self.assertGreater(high,low)
        for lam in (low,high):
            v=(float(H[0][1])-lam*float(M[0][1]),-(float(H[0][0])-lam*float(M[0][0])))
            for i in range(2):
                residual=sum((float(H[i][j])-lam*float(M[i][j]))*v[j] for j in range(2))
                self.assertLess(abs(residual),1e-12)
            numerator=sum(v[i]*float(H[i][j])*v[j] for i in range(2) for j in range(2))
            denominator=sum(v[i]*float(M[i][j])*v[j] for i in range(2) for j in range(2))
            self.assertAlmostEqual(numerator/denominator,lam,places=10)

    def test_ground_state_identity(self):
        # Identidade específica verificada por quadratura separada; prova geral nas notas.
        def positive(x):
            if x==0 or x==1:return 0.
            u=x*(1-x);du=1-2*x;phi=sin(pi*x)
            return ((du*phi-u*pi*cos(pi*x))/phi)**2
        left=1/3-pi*pi/30
        self.assertGreater(left,0)
        self.assertAlmostEqual(simpson(positive),left,places=10)

    def test_scale_domain_and_nonzero(self):
        for a in range(-3,4):
            for b in range(-3,4):
                if a==b==0:continue
                p=trial(a,b)
                self.assertEqual(evaluate(p,0),0);self.assertEqual(evaluate(p,1),0)
                self.assertGreater(float(rayleigh(p)),pi*pi)
                self.assertEqual(rayleigh(tuple(-3*x for x in p)),rayleigh(p))
        for p in [(1,),(0,1),(0,0)]:
            with self.assertRaises(ValueError):rayleigh(p)
        for p in [(True,1),(0,.5),(0,'1')]:
            with self.assertRaises(TypeError):rayleigh(p)

if __name__=='__main__':unittest.main()
