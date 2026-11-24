"""Conferências de primitivas; não é um integrador simbólico geral."""
import math
import unittest


def simpson(f,a,b,n):
    if type(n) is not int or not 2<=n<=10000 or n%2:
        raise ValueError('n par, de 2 a 10000')
    if not callable(f) or not math.isfinite(a) or not math.isfinite(b) or a>=b:
        raise ValueError('Função e limites finitos crescentes')
    h=(b-a)/n
    values=[f(a+i*h) for i in range(n+1)]
    if not all(math.isfinite(v) for v in values):raise ValueError('Integrando não finito')
    return h/3*(values[0]+values[-1]+4*sum(values[1:-1:2])+2*sum(values[2:-1:2]))


CASES=[
    (lambda x:math.sin(x)**2, lambda x:x/2-math.sin(2*x)/4),
    (lambda x:math.sin(x)**3*math.cos(x)**4,
     lambda x:-math.cos(x)**5/5+math.cos(x)**7/7),
    (lambda x:math.sin(x)**4*math.cos(x)**3,
     lambda x:math.sin(x)**5/5-math.sin(x)**7/7),
    (lambda x:math.sin(x)**2*math.cos(x)**2,
     lambda x:x/8-math.sin(4*x)/32),
    (lambda x:math.sin(3*x)**2,lambda x:x/2-math.sin(6*x)/12),
]
POINTS=(-1.3,-.7,.2,.8,1.4)


class Checks(unittest.TestCase):
    def test_derivatives_at_regular_points(self):
        h=1e-5
        for f,F in CASES:
            for x in POINTS:
                self.assertAlmostEqual((F(x+h)-F(x-h))/(2*h),f(x),delta=1e-8)

    def test_independent_quadrature(self):
        fixtures=[(CASES[0][0],0,math.pi,math.pi/2),
                  (CASES[1][0],0,math.pi/2,2/35),
                  (CASES[2][0],0,math.pi/2,2/35),
                  (CASES[3][0],0,math.pi/2,math.pi/16),
                  (lambda x:math.sin(x)*math.cos(x),0,math.pi,0)]
        for f,a,b,expected in fixtures:
            values=[simpson(f,a,b,n) for n in (128,256,512)]
            self.assertAlmostEqual(values[-1],expected,delta=2e-10)
        product_average=simpson(CASES[3][0],0,math.pi/2,512)/(math.pi/2)
        self.assertAlmostEqual(product_average,1/8,places=10)
        self.assertNotAlmostEqual(product_average,(1/2)*(1/2),places=3)

    def test_central_difference_refinement(self):
        f,F=CASES[0]
        errors=[max(abs((F(x+h)-F(x-h))/(2*h)-f(x)) for x in POINTS)
                for h in (.04,.02,.01)]
        for old,new in zip(errors,errors[1:]):self.assertTrue(3.9<old/new<4.1)

    def test_contracts(self):
        for n in (True,0,1,3,2.0,10002):
            with self.assertRaises(ValueError):simpson(math.sin,0,1,n)
        with self.assertRaises(ValueError):simpson(math.sin,1,0,10)
        with self.assertRaises(ValueError):simpson(lambda x:float('nan'),0,1,10)


if __name__=='__main__':
    f,F=CASES[0]
    print('Erros de diferença central:',
          [max(abs((F(x+h)-F(x-h))/(2*h)-f(x)) for x in POINTS) for h in (.04,.02,.01)])
    print('Integral ímpar:',simpson(CASES[1][0],0,math.pi/2,512),'versus',2/35)
    unittest.main()
