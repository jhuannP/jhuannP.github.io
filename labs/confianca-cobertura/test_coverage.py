import unittest
from fractions import Fraction as F
from itertools import product
from math import exp,pi,sqrt
from .coverage import known_sigma,normal_coverage,rademacher,repeated_rademacher


def integral(lo,hi,n=8192):
    # Independent quadrature of the Gaussian density; no CDF/erf call.
    h=(hi-lo)/n
    f=lambda x:exp(-x*x/2)/sqrt(2*pi)
    return h/3*(f(lo)+f(hi)+sum((4 if j%2 else 2)*f(lo+j*h) for j in range(1,n)))


class CoverageTests(unittest.TestCase):
    def test_literal_bounds_and_units(self):
        a=known_sigma(10,2,100)
        for key,value in [('se',.2),('margin',.392),('lower',9.608),('upper',10.392)]:
            self.assertAlmostEqual(a[key],value)
        for n in [1,4,9,25]:
            a=known_sigma(-3,2,n);b=known_sigma(-3,2,4*n)
            self.assertAlmostEqual(b['margin'],a['margin']/2)
            shifted=known_sigma(97,2,n)
            self.assertAlmostEqual(shifted['upper']-a['upper'],100)
            scaled=known_sigma(-30,20,n)
            self.assertAlmostEqual(scaled['lower'],10*a['lower'])

    def test_gaussian_integral_independent(self):
        for critical,bias,scale in [(1.96,0,1),(1,0,1),(2,0,1),(1.96,5,1),(1.96,0,2),(1.96,-1,1.5)]:
            expected=integral((-critical-bias)/scale,(critical-bias)/scale)
            self.assertAlmostEqual(normal_coverage(critical,bias,scale),expected,places=12)
        self.assertAlmostEqual(normal_coverage(),.950004209703559,places=14)
        self.assertAlmostEqual(normal_coverage(standardized_bias=5),normal_coverage(standardized_bias=-5),places=14)
        self.assertLess(normal_coverage(standardized_bias=5),.002)
        self.assertLess(normal_coverage(scale=2),.68)

    def test_complete_finite_enumeration(self):
        for n in range(1,11):
            for c in [F(1),F(49,25),F(2)]:
                hits=0
                for sample in product([-1,1],repeat=n):
                    # Compare actual mean and squared interval radius, separately from count law.
                    mean=F(sum(sample),n)
                    hits+=mean*mean<=c*c/n
                result=rademacher(n,c)
                self.assertEqual(result['coverage'],F(hits,2**n))
                self.assertEqual(sum(r['mass'] for r in result['rows']),1)
        rows=rademacher(4)['rows']
        self.assertEqual([r['mass'] for r in rows],[F(1,16),F(1,4),F(3,8),F(1,4),F(1,16)])
        self.assertEqual([r['covered'] for r in rows],[False,True,True,True,False])
        self.assertEqual(rademacher(4)['coverage'],F(7,8))
        self.assertEqual(rademacher(1)['coverage'],1)

    def test_dependence_countermodel(self):
        for n in range(1,13):
            for c in [F(1),F(49,25),F(2)]:
                hits=sum(F(sum([x]*n),n)**2<=c*c/n for x in [-1,1])
                self.assertEqual(repeated_rademacher(n,c),F(hits,2))
        self.assertEqual(repeated_rademacher(4),0)
        self.assertEqual(repeated_rademacher(4,F(2)),1) # Inclusion of boundary declared.

    def test_contracts(self):
        for n in [True,0,-1,1.5,129]:
            with self.assertRaises(ValueError):rademacher(n)
        for c in [True,0,-1,1.96]:
            with self.assertRaises(ValueError):rademacher(4,c)
        for args in [(1,0,1),(1,-1,1),(1,2,0),(float('nan'),2,4),(1,2,True)]:
            with self.assertRaises(ValueError):known_sigma(*args)
        for args in [(0,0,1),(2,0,0),(2,float('inf'),1),(True,0,1)]:
            with self.assertRaises(ValueError):normal_coverage(*args)

if __name__=='__main__':unittest.main()
