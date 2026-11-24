import unittest
from fractions import Fraction as F
from math import exp,pi,sqrt
from .binomial import masses,exact,approximate,normal_area


def convolve(n,p):
    values=[F(1)]
    for _ in range(n):
        new=[F(0)]*(len(values)+1)
        for k,q in enumerate(values):new[k]+=q*(1-p);new[k+1]+=q*p
        values=new
    return tuple(values)


def integral(a,b,n=4096):
    h=(b-a)/n
    density=lambda x:exp(-x*x/2)/sqrt(2*pi)
    return h/3*(density(a)+density(b)+sum((4 if j%2 else 2)*density(a+j*h) for j in range(1,n)))


class CentralLimitTests(unittest.TestCase):
    def test_literal_examples(self):
        self.assertEqual(exact(16,F(1,2),6,10),F(25883,32768))
        self.assertEqual(exact(16,F(1,2),8,8),F(6435,32768))
        self.assertAlmostEqual(approximate(16,F(1,2),6,10,False),.6826894921370859)
        self.assertAlmostEqual(approximate(16,F(1,2),6,10),.7887004526662893)
        self.assertEqual(exact(100,F(1,100),upper=0),F(99,100)**100)
        self.assertGreater(abs(float(exact(100,F(1,100),upper=0))-approximate(100,F(1,100),upper=0)),.05)

    def test_independent_convolution_and_moments(self):
        for n in range(1,21):
            for p in [F(1,10),F(1,4),F(1,2),F(9,10)]:
                q=masses(n,p);self.assertEqual(q,convolve(n,p));self.assertEqual(sum(q),1)
                mean=sum(k*v for k,v in enumerate(q))
                variance=sum((k-mean)**2*v for k,v in enumerate(q))
                self.assertEqual(mean,n*p);self.assertEqual(variance,n*p*(1-p))
        self.assertEqual(masses(3,0),(1,0,0,0));self.assertEqual(masses(3,1),(0,0,0,1))

    def test_standardized_symmetric_fourth_moment(self):
        for n in [1,2,4,8,16,32]:
            q=masses(n,F(1,2))
            # Z=(2K-n)/sqrt(n); its squared/fourth moments need no irrational arithmetic.
            variance=sum(F((2*k-n)**2,n)*v for k,v in enumerate(q))
            fourth=sum(F((2*k-n)**4,n*n)*v for k,v in enumerate(q))
            self.assertEqual(variance,1)
            # Independent counting: n single fourth moments and 6*C(n,2) pairs.
            self.assertEqual(fourth,F(n+3*n*(n-1),n*n))
            self.assertEqual(fourth,3-F(2,n))

    def test_continuity_cells(self):
        p=F(1,2)
        area=sum(approximate(16,p,k,k) for k in range(6,11))
        self.assertAlmostEqual(area,approximate(16,p,6,10),places=14)
        self.assertEqual(approximate(16,p,8,8,False),0)
        self.assertGreater(exact(16,p,8,8),0)
        self.assertEqual(exact(16,p,-2,18),1)
        self.assertAlmostEqual(approximate(16,p),1)

    def test_gaussian_density_reference(self):
        for a,b in [(-1.25,1.25),(-1,1),(-2,-.25),(.25,2),(-.5,.5)]:
            self.assertAlmostEqual(normal_area(a,b),integral(a,b),places=12)
        self.assertGreater(normal_area(8,9),0) # erfc keeps this small positive tail.

    def test_contracts(self):
        for n,p in [(0,F(1,2)),(True,F(1,2)),(257,F(1,2)),(4,.5),(4,True),(4,F(-1,2)),(4,F(1,1001))]:
            with self.assertRaises(ValueError):masses(n,p)
        for p in [0,1]:
            with self.assertRaises(ValueError):approximate(4,p)
        for bounds in [(True,1),(1.0,2),(3,2)]:
            with self.assertRaises(ValueError):exact(4,F(1,2),*bounds)
        with self.assertRaises(ValueError):approximate(4,F(1,2),corrected=1)

if __name__=='__main__':unittest.main()
