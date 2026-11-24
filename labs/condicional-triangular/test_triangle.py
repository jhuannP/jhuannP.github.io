import unittest
from fractions import Fraction as Q
from .triangle import rectangle,given_x,given_y,band_x,marginal_x,marginal_y

class TriangleTests(unittest.TestCase):
    def test_rectangles_by_independent_cdf(self):
        # Integração na outra ordem: F(t,s)=integral_0^min(t,s) (3/2)(t²-y²)dy.
        def cdf(t,s):
            u=min(t,s)
            return Q(3,2)*t*t*u-u**3/2
        grid=[Q(i,4) for i in range(5)]
        intervals=[(a,b) for a in grid for b in grid if a<=b]
        for a,b in intervals:
            for c,d in intervals:
                actual=rectangle(a,b,c,d)
                self.assertEqual(actual,cdf(b,d)-cdf(a,d)-cdf(b,c)+cdf(a,c))
                self.assertTrue(0<=actual<=1)
        self.assertEqual(rectangle(0,1,0,1),1)
        self.assertEqual(rectangle(0,Q(1,2),Q(1,2),1),0)

    def test_conditionals_and_support(self):
        for k in range(1,9):
            x=Q(k,8)
            self.assertEqual(given_x(x,0,1),1)
            self.assertEqual(given_x(x,x,1),0)
            for j in range(9):
                s=Q(j,8)
                self.assertEqual(given_x(x,0,s),min(s,x)/x)
                self.assertEqual(given_x(x,0,s)+given_x(x,s,1),1)
        for k in range(8):
            y=Q(k,8)
            self.assertEqual(given_y(y,0,1),1)
            self.assertEqual(given_y(y,0,y),0)
        self.assertEqual(given_y(Q(1,2),Q(3,4),1),Q(7,12))
        self.assertEqual(marginal_x(Q(1,2)),Q(3,4))
        self.assertEqual(marginal_y(Q(1,2)),Q(9,8))

    def test_total_probability_and_mean(self):
        # Simpson exato para estes polinômios de grau até 3; não integra indicadores.
        def simpson(f,a,b):return (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6
        tail=lambda x:given_x(x,Q(1,2),1)*marginal_x(x)
        self.assertEqual(simpson(tail,Q(1,2),Q(1)),Q(5,16))
        self.assertEqual(simpson(lambda x:x/2*marginal_x(x),Q(0),Q(1)),Q(3,8))
        self.assertEqual(simpson(lambda y:y*marginal_y(y),Q(0),Q(1)),Q(3,8))

    def test_band_limits_and_dependence(self):
        self.assertEqual(band_x(Q(1,2),Q(3,4),Q(1,2),1),Q(4,19))
        self.assertEqual(rectangle(0,Q(1,2),Q(1,2),1),0)
        self.assertEqual(rectangle(0,Q(1,2),0,1)*rectangle(0,1,Q(1,2),1),Q(5,128))
        for h in [Q(1,2**k) for k in range(3,10)]:
            # P(Y>1/4 | |X-1/2|<=h)=1 - (3/4)/(3/2+2h²).
            p=band_x(Q(1,2)-h,Q(1,2)+h,Q(1,4),1)
            self.assertEqual(p,1-Q(3,4)/(Q(3,2)+2*h*h))
            self.assertLess(abs(p-Q(1,2)),h*h)

    def test_contracts_and_null_events(self):
        self.assertIsNone(given_x(0,0,1));self.assertIsNone(given_y(1,0,1))
        self.assertIsNone(band_x(Q(1,2),Q(1,2),0,1))
        self.assertEqual(rectangle(0,0,0,1),0)
        for bad in [True,0.5,'1/2',None]:
            with self.assertRaises(TypeError):given_x(bad,0,1)
        for args in [(-1,1,0,1),(1,0,0,1),(0,1,0,2)]:
            with self.assertRaises(ValueError):rectangle(*args)
        with self.assertRaises(ValueError):given_y(2,0,1)
        self.assertEqual(marginal_x(-1),0)

if __name__=='__main__':unittest.main()
