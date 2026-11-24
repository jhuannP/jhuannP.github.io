import unittest
from fractions import Fraction as Q
from .noise import support,marginal,conditional,tail,lower_bin,bin_density

class NoiseTests(unittest.TestCase):
    def test_geometry_and_normalization(self):
        # Intersect x in [0,1] and e=z-x in [0,1], independent of formulas.
        for j in range(1,32):
            z=Q(j,16);r=conditional(z);a,b=r['lower'],r['upper']
            self.assertTrue(0<=a<b<=1)
            self.assertTrue(0<=z-a<=1 and 0<=z-b<=1)
            self.assertEqual((b-a)*r['density'],1)
            self.assertEqual(marginal(z),b-a)
            # Simpson integrates x and x² exactly for a uniform slice.
            mid=(a+b)/2
            mean=(b-a)*(a+4*mid+b)/6*r['density']
            second=(b-a)*(a*a+4*mid*mid+b*b)/6*r['density']
            self.assertEqual(r['mean'],mean)
            self.assertEqual(r['variance'],second-mean*mean)
    def test_reference_and_tails(self):
        self.assertEqual(conditional(Q(1,2))['mean'],Q(1,4))
        self.assertEqual(conditional(Q(3,2))['mean'],Q(3,4))
        self.assertEqual(conditional(Q(1,2))['variance'],Q(1,48))
        self.assertEqual(tail(Q(3,2),Q(3,4)),Q(1,2))
        self.assertEqual(tail(Q(1,2),Q(3,4)),0)
        for j in range(1,20):
            z=Q(j,10);a,b=support(z)
            self.assertEqual(tail(z,a),1);self.assertEqual(tail(z,b),0)
            self.assertEqual(conditional(z)['variance'],conditional(2-z)['variance'])
    def test_bins_by_independent_polynomial_integration(self):
        # Integrate x^k*(b-x) dx directly, rather than copying mean/variance.
        for j in range(1,21):
            b=Q(j,20);mom=[b**(k+2)/((k+1)*(k+2)) for k in range(3)]
            r=lower_bin(b)
            self.assertEqual(r['evidence'],mom[0])
            self.assertEqual(r['mean'],mom[1]/mom[0])
            self.assertEqual(r['variance'],mom[2]/mom[0]-(mom[1]/mom[0])**2)
            # Simpson verifies normalized triangular posterior independently.
            self.assertEqual(b*(bin_density(b,0)+4*bin_density(b,b/2)+bin_density(b,b))/6,1)
        r=lower_bin(Q(1,2))
        self.assertEqual((r['evidence'],r['mean'],r['variance']),(Q(1,8),Q(1,6),Q(1,72)))
    def test_tower_and_total_variance(self):
        # Simpson exact on each piece for polynomials of degree <=3.
        def integ(fun,a,b):return (b-a)*(fun(a)+4*fun((a+b)/2)+fun(b))/6
        def length(z):return z if z<=1 else 2-z
        mass=sum(integ(length,a,b) for a,b in [(Q(0),Q(1)),(Q(1),Q(2))])
        mean=sum(integ(lambda z:z/2*length(z),a,b) for a,b in [(Q(0),Q(1)),(Q(1),Q(2))])
        residual=sum(integ(lambda z:length(z)**3/12,a,b) for a,b in [(Q(0),Q(1)),(Q(1),Q(2))])
        variation=sum(integ(lambda z:(z/2-Q(1,2))**2*length(z),a,b) for a,b in [(Q(0),Q(1)),(Q(1),Q(2))])
        self.assertEqual(mass,1);self.assertEqual(mean,Q(1,2))
        self.assertEqual(residual,Q(1,24));self.assertEqual(variation,Q(1,24))
        self.assertEqual(residual+variation,Q(1,12))
    def test_endpoints_and_contracts(self):
        for z in [-2,0,2,4]:
            self.assertIsNone(conditional(z));self.assertIsNone(tail(z,0))
            self.assertEqual(marginal(z),0)
        for b in [-1,0,2]:
            with self.assertRaises(ValueError):lower_bin(b)
        for bad in [True,.5,'1/2',None]:
            with self.assertRaises(ValueError):conditional(bad)
            with self.assertRaises(ValueError):lower_bin(bad)
        self.assertEqual(bin_density(Q(1,2),Q(3,4)),0)
