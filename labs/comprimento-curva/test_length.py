import unittest
from fractions import Fraction as F
from decimal import Decimal, localcontext
from .length import point,speed,arc,sqrt_bounds,polygon

class LengthTests(unittest.TestCase):
    def test_identity_and_reparameterization(self):
        for i in range(101):
            t=F(i,100)
            self.assertEqual((3-3*t*t)**2+(6*t)**2,speed(t)**2)
            u=t
            # r(u²) has derivative (6u-6u⁵,12u³).
            self.assertEqual((6*u-6*u**5)**2+(12*u**3)**2,(2*u*speed(u*u))**2)
        self.assertEqual(arc(),4)
        self.assertEqual(arc(0,F(1,2)),F(13,8))
        self.assertEqual(arc(0,F(1,2))+arc(F(1,2),1),arc())
        self.assertEqual(point(1),(2,3))
        self.assertEqual(arc(F(2,3),F(2,3)),0)

    def test_independent_decimal_chords(self):
        with localcontext() as ctx:
            ctx.prec=65
            for n in (1,2,3,4,7,16,32):
                total=Decimal(0)
                for i in range(n):
                    a=Decimal(i)/Decimal(n);b=Decimal(i+1)/Decimal(n)
                    dx=3*(b-a)-(b**3-a**3);dy=3*(b*b-a*a)
                    total+=(dx*dx+dy*dy).sqrt()
                r=polygon(n,10)
                dec=lambda x:Decimal(x.numerator)/Decimal(x.denominator)
                self.assertLessEqual(dec(r['lower']),total)
                self.assertLessEqual(total,dec(r['upper']))
                self.assertLess(total,Decimal(4))
                self.assertLessEqual(r['upper']-r['lower'],F(n,10**10))

    def test_refinement_and_certified_roots(self):
        previous=polygon(1)
        for n in (2,4,8,16,32,64):
            current=polygon(n)
            self.assertGreater(current['lower'],previous['upper'])
            self.assertLess(current['upper'],4)
            self.assertLessEqual(4-current['lower'],F(9,n)+F(n,10**9))
            previous=current
        for q in (F(0),F(1),F(4),F(13),F(5,7),F(1001,13)):
            lo,hi=sqrt_bounds(q,8)
            self.assertLessEqual(lo*lo,q);self.assertLessEqual(q,hi*hi)
            self.assertLessEqual(hi-lo,F(1,10**8))

    def test_contract(self):
        for value in (True,1.0,'2',None):
            with self.assertRaises(TypeError): polygon(value)
        for value in (0,-1,4097):
            with self.assertRaises(ValueError): polygon(value)
        for value in (-1,F(3,2)):
            with self.assertRaises(ValueError): point(value)
        with self.assertRaises(ValueError): arc(1,0)
        with self.assertRaises(ValueError): polygon(2,0)
        with self.assertRaises(TypeError): polygon(2,True)
