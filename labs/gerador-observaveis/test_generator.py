import unittest,math
from fractions import Fraction as F
from decimal import Decimal,localcontext
from .generator import apply,transition,evaluate,polynomial


def add(a,b,scale=1):
    return polynomial([(a[i] if i<len(a) else 0)+scale*(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])


def multiply(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return polynomial(c)


def derivative(a):return polynomial([i*a[i] for i in range(1,len(a))] or [0])


class GeneratorTests(unittest.TestCase):
    def test_literal_eigen_observables(self):
        for coeff,n in [((1,),0),((0,1),1),((-1,0,1),2),((0,-3,0,1),3),((3,0,-6,0,1),4)]:
            f=polynomial(coeff)
            self.assertEqual(apply(f),polynomial([-2*n*x for x in f]))
            self.assertEqual(transition(f,F(1,2)),polynomial([F(1,2)**n*x for x in f]))
        self.assertEqual(apply((0,0,1)),(F(4),F(0),F(-4)))
        self.assertEqual(evaluate(apply((0,0,1)),2),-12)

    def test_semigroup_and_commutation(self):
        for f in [(1,),(0,1),(0,0,1),(1,-2,0,3),(2,0,1,-1,1),(0,0,0,0,0,1)]:
            for r in (F(0),F(1,3),F(1)):
                for s in (F(0),F(1,2),F(1)):
                    self.assertEqual(transition(transition(f,s),r),transition(f,r*s))
                self.assertEqual(apply(transition(f,r)),transition(apply(f),r))

    def test_product_rule_and_stationary_mean(self):
        fs=[(0,1),(0,0,1),(1,-2,1),(0,1,0,1)]
        for f in fs:
            self.assertEqual(transition(apply(f),0),(F(0),))
            for g in fs:
                left=add(add(apply(multiply(f,g)),multiply(f,apply(g)),-1),multiply(g,apply(f)),-1)
                right=polynomial([4*x for x in multiply(derivative(f),derivative(g))])
                self.assertEqual(left,right)
        self.assertEqual(transition((0,0,0,0,1),0),(F(3),))

    def test_small_time_against_decimal(self):
        # Exact P_t x² at x=2 is 1+3exp(-4t). No Euler step is used.
        for t in (F(1,10),F(1,20),F(1,40),F(1,80)):
            with localcontext() as ctx:
                ctx.prec=70;td=Decimal(t.numerator)/Decimal(t.denominator)
                ref=3*((-4*td).exp()-1)/td
            actual=3*math.expm1(-4*float(t))/float(t)
            self.assertAlmostEqual(actual,float(ref),places=13)
            self.assertGreater(actual,-12)
            self.assertLess(actual+12,24*float(t))

    def test_contracts(self):
        for c in [[],[True],[1.0],[0]*14]:
            with self.assertRaises(ValueError):apply(c)
        for args in [((1,),0,2),((1,),2,-1)]:
            with self.assertRaises(ValueError):apply(*args)
        for r in (-1,2,True,.5):
            with self.assertRaises(ValueError):transition((1,),r)
        self.assertEqual(apply((0,0,1),1,0),(F(0),F(0),F(-2)))
        for theta in (1,3):
            for sigma in (0,1,2):
                stationary=F(sigma*sigma,2*theta)
                self.assertEqual(apply((-stationary,0,1),theta,sigma),polynomial((2*theta*stationary,0,-2*theta)))

if __name__=='__main__':unittest.main()
