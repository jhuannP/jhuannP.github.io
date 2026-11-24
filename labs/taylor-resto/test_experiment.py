import math,unittest
from decimal import Decimal as D,localcontext
from fractions import Fraction as F
from .experiment import polynomial,tail,uniform_bound,model

class TaylorRemainderTests(unittest.TestCase):
    def test_decimal_exponential_independent_remainder_and_bounds(self):
        with localcontext() as ctx:
            ctx.prec=80
            for n in (0,1,2,5,10,12):
                for rho in (D('.25'),D('.5'),D('.75'),D(1)):
                    for u in (D(-1),D('-.1'),D(0),D('.1'),D(1)):
                        x=rho*u;P=sum(x**k/D(math.factorial(k)) for k in range(n+1)) if x else D(1)
                        R=x.exp()-P;s=model(n,float(rho),float(u))
                        self.assertAlmostEqual(s['polynomial'],float(P),places=14)
                        if R:self.assertLess(abs(D.from_float(s['remainder'])/R-1),D('2e-14'))
                        else:self.assertEqual(s['remainder'],0)
                        point=max(D(0),x).exp()*abs(x)**(n+1)/D(math.factorial(n+1))
                        uniform=rho.exp()*rho**(n+1)/D(math.factorial(n+1))
                        self.assertLessEqual(abs(R),point);self.assertLessEqual(point,uniform)
                        self.assertLessEqual(abs(s['normalized']),1+1e-14)

    def test_integral_remainder_independent_simpson_refinement(self):
        def simpson(n,x,m):
            f=lambda t:(1-t)**n*math.exp(x*t)
            return (f(0)+f(1)+4*sum(f(j/m) for j in range(1,m,2))+2*sum(f(j/m) for j in range(2,m,2)))/(3*m)
        for n in (0,2,6,12):
            for x in (-1.,-.5,.5,1.):
                target=tail(x,n)*math.factorial(n)/x**(n+1)
                a=abs(simpson(n,x,128)-target);b=abs(simpson(n,x,256)-target)
                self.assertLessEqual(b,a*.08+2e-15)
                self.assertLess(b,1e-7)

    def test_minimum_degree_and_uniform_convergence_ratio(self):
        with localcontext() as ctx:
            ctx.prec=60
            for radius in (D('.25'),D('.5'),D('.75'),D(1)):
                for p in range(2,7):
                    s=model(2,float(radius),.1,p);n=s['required'];eps=D(10)**(-p)
                    b=lambda j:radius.exp()*radius**(j+1)/D(math.factorial(j+1))
                    self.assertLessEqual(b(n),eps)
                    if n:self.assertGreater(b(n-1),eps)
                for n in range(12):self.assertAlmostEqual(uniform_bound(n+1,float(radius))/uniform_bound(n,float(radius)),float(radius)/(n+2),places=14)
        self.assertEqual(model()['required'],7)

    def test_rational_coefficients_zero_sign_and_contract(self):
        x=F(1,10);exact=sum(x**k/math.factorial(k) for k in range(3))
        self.assertEqual(exact,F(221,200));self.assertAlmostEqual(polynomial(.1,2),float(exact))
        for n in range(13):
            self.assertEqual(tail(0,n),0)
            self.assertEqual(model(n,.25,0)['local_bound'],0)
            self.assertEqual(tail(-.5,n)>0,(n+1)%2==0)
        for args in ((-1,1,.1,4),(13,1,.1,4),(2,.1,.1,4),(2,1,2,4),(2,1,.1,7),(2,float('nan'),.1,4)):
            with self.assertRaises(ValueError):model(*args)
