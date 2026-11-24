from fractions import Fraction as F
from math import exp,expm1
import unittest
from .experiment import variance_ratio,inspect

class OUMean(unittest.TestCase):
    def test_independent_innovations_factorization(self):
        # Xi=rho^i Z0+sqrt(1-rho²)sum(rho^(i-j)Zj),Z independentes,var1.
        for n in range(1,21):
            for rho in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
                coefficient0=sum(rho**i for i in range(n))/n
                reference=coefficient0**2+(1-rho*rho)*sum((sum(rho**i for i in range(n-j))/n)**2 for j in range(1,n))
                self.assertAlmostEqual(variance_ratio(n,rho),float(reference),places=13)

    def test_covariance_double_sum_and_bounds(self):
        for n in [1,2,5,20,40]:
            for level in [5,10,50,100,200]:
                z=inspect(n,level);rho=z['rho']
                reference=sum(rho**abs(i-j) for i in range(n) for j in range(n))/(n*n)
                self.assertAlmostEqual(z['variance'],reference,places=13)
                self.assertGreaterEqual(z['neff'],1-1e-12);self.assertLessEqual(z['neff'],n+1e-12)
                self.assertGreaterEqual(z['sem'],z['iid_sem']-1e-12)
        self.assertAlmostEqual(variance_ratio(3,F(1,2)),F(11,18))
        self.assertEqual(variance_ratio(20,1),1)
        self.assertEqual(variance_ratio(20,0),.05)
        self.assertLess(2*(1-.5)/(1+.5),1) # aproximação assintótica inadmissível para n2

    def test_fixed_horizon_dense_sampling_limit(self):
        # Média contínua:dupla integral de C,obtida via quadratura de defasagens.
        for T in [1,4,10]:
            N=4096;h=T/N
            integral=2*h/(3*T*T)*sum((1 if j in (0,N) else 4 if j%2 else 2)*(T-j*h)*exp(-j*h) for j in range(N+1))
            analytic=2*(T+expm1(-T))/(T*T)
            self.assertAlmostEqual(integral,analytic,places=10)
            errors=[abs(variance_ratio(n,exp(-T/(n-1)))-analytic) for n in [20,200,2000]]
            self.assertGreater(errors[0],errors[1]);self.assertGreater(errors[1],errors[2])
            self.assertGreater(analytic,0)

    def test_contracts(self):
        for args in [(0,.5),(True,.5),(2,True),(2,-.1),(2,1.1),(2,float('nan'))]:
            with self.assertRaises(ValueError):variance_ratio(*args)
        for args in [(0,10),(41,10),(1,4),(1,201),(1,10.0)]:
            with self.assertRaises(ValueError):inspect(*args)
