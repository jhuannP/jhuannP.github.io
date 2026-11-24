import unittest,math,itertools
from fractions import Fraction as Q
from .poisson import pmf,moments,conditional_count

class PoissonTests(unittest.TestCase):
    def test_reference_and_moments_from_distribution(self):
        self.assertEqual(moments(2,1,3)['mean_t'],6)
        self.assertAlmostEqual(pmf(2,1,2),2*math.exp(-2))
        for mu in [.1,1,6,30,100]:
            probs=[pmf(mu,1,k) for k in range(701)]
            mean=sum(k*v for k,v in enumerate(probs))
            second=sum(k*k*v for k,v in enumerate(probs))
            self.assertAlmostEqual(sum(probs),1,places=13)
            self.assertAlmostEqual(mean,mu,places=11)
            self.assertAlmostEqual(second-mean*mean,mu,delta=1e-10)
    def test_independent_increment_convolution(self):
        # Sum over every split of a fixed final count: no simulation or infinite tail.
        for n in range(21):
            convolution=sum(pmf(2,Q(1,2),k)*pmf(2,1,n-k) for k in range(n+1))
            self.assertAlmostEqual(convolution,pmf(2,Q(3,2),n),places=14)
    def test_conditional_count_by_joint_ratio(self):
        for n in range(11):
            for k in range(n+1):
                joint=pmf(2,1,k)*pmf(2,2,n-k)
                expected=joint/pmf(2,3,n)
                self.assertAlmostEqual(float(conditional_count(n,1,3,k)),expected,places=13)
        self.assertEqual(conditional_count(6,1,3,0),Q(64,729))
        self.assertEqual(conditional_count(6,1,3,7),0)
    def test_conditional_negative_covariance_and_unconditional(self):
        probs=[conditional_count(6,1,3,k) for k in range(7)]
        self.assertEqual(sum(probs),1)
        mean=sum(k*v for k,v in enumerate(probs));other=sum((6-k)*v for k,v in enumerate(probs))
        cross=sum(k*(6-k)*v for k,v in enumerate(probs))
        self.assertEqual(mean,2);self.assertEqual(other,4)
        self.assertEqual(cross-mean*other,Q(-4,3))
        self.assertEqual(moments(2,1,3)['covariance'],2)
        # Independent increments U,V: E[U(U+V)] from first/second moments.
        eu,ev=2,4;eu2=2+2**2
        self.assertEqual(eu2+eu*ev-eu*(eu+ev),2)
    def test_zeros_and_contracts(self):
        self.assertEqual(pmf(2,0,0),1);self.assertEqual(pmf(2,0,1),0)
        self.assertEqual(conditional_count(6,0,3,0),1)
        self.assertEqual(conditional_count(6,3,3,6),1)
        self.assertEqual(conditional_count(0,1,3,0),1)
        for args in [(0,1,0),(1,-1,0),(1,101,0),(True,1,0),(1,1,-1),(1,1,True)]:
            with self.assertRaises(ValueError):pmf(*args)
        for args in [(2,1,0),(2,-1,3),(True,1,3)]:
            with self.assertRaises(ValueError):moments(*args)
        for args in [(6,1,0,0),(6,4,3,0),(6,.5,3,0)]:
            with self.assertRaises(ValueError):conditional_count(*args)
