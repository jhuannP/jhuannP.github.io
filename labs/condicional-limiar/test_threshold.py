import unittest
from fractions import Fraction as Q
from .threshold import readout,cdf,posterior,bin_posterior,decomposition

class ThresholdTests(unittest.TestCase):
    def test_pushforward_by_preimages(self):
        # Exact rational cell lengths of X, not evaluation of a density at a point.
        for a in (Q(1,4),Q(1,2),Q(3,4)):
            grid=[Q(i,40) for i in range(41)]
            for y in (Q(-1),Q(0),Q(1,8),Q(1,2),Q(2)):
                mass=sum((r-l for l,r in zip(grid,grid[1:]) if readout((l+r)/2,a)<=y),Q(0))
                # Grid boundaries chosen to include each cutoff exactly.
                self.assertEqual(mass,cdf(y,a))
            self.assertEqual(cdf(0,a),a)
            self.assertEqual(a+(1-a),1)
    def test_atom_and_positive_branch(self):
        a=Q(1,2)
        r=posterior(0,a)
        self.assertEqual((r['mean'],r['variance']),(Q(1,4),Q(1,48)))
        r=posterior(Q(1,4),a)
        self.assertEqual((r['mean'],r['variance']),(Q(3,4),0))
        # Positive bins shrink around a reading to the deterministic inverse.
        for n in (10,20,100):
            y=Q(1,4);h=Q(1,n);left=a+y-h;right=a+y+h
            self.assertEqual((left+right)/2,r['mean'])
            self.assertLess((right-left)**2/12,Q(1,100))
    def test_bins_by_direct_moments(self):
        for a in (Q(1,4),Q(1,2),Q(3,4)):
            for k in range(1,9):
                b=(1-a)*Q(k,8)
                for include in (True,False):
                    r=bin_posterior(b,a,include)
                    l,u=r['lower'],r['upper']
                    mass=u-l;first=(u*u-l*l)/2;second=(u**3-l**3)/3
                    self.assertEqual(r['evidence'],mass)
                    self.assertEqual(r['mean'],first/mass)
                    self.assertEqual(r['variance'],second/mass-(first/mass)**2)
        self.assertEqual(bin_posterior(Q(1,4),Q(1,2))['mean'],Q(3,8))
        self.assertEqual(bin_posterior(Q(1,4),Q(1,2),False)['mean'],Q(5,8))
    def test_tower_and_variance_by_independent_quadrature(self):
        # Simpson is exact for the polynomials of degree <=2 on each branch.
        for j in range(1,20):
            a=Q(j,20);r=decomposition(a);v0=posterior(0,a)
            width=1-a
            m=[posterior(y,a)['mean'] for y in (width/4,width/2,3*width/4)]
            # Extrapolate the affine branch to endpoints (not assigning a posterior there).
            left=2*m[0]-m[1];right=2*m[2]-m[1]
            first=width*(left+4*m[1]+right)/6+a*v0['mean']
            second=width*(left**2+4*m[1]**2+right**2)/6+a*v0['mean']**2
            residual=a*v0['variance']
            self.assertEqual(first,Q(1,2))
            self.assertEqual(second-first**2,r['explained'])
            self.assertEqual(residual,r['residual'])
            self.assertEqual(residual+second-first**2,Q(1,12))
        self.assertEqual(decomposition(Q(1,2))['residual'],Q(1,96))
    def test_contracts(self):
        for a in (0,1,-1,True,0.5):
            with self.assertRaises(ValueError): cdf(0,a)
        for y in (-1,1):
            with self.assertRaises(ValueError): posterior(y,Q(1,2))
        self.assertIsNone(posterior(Q(1,2),Q(1,2)))
        for b in (0,-1,1):
            with self.assertRaises(ValueError): bin_posterior(b,Q(1,2))
        with self.assertRaises(ValueError): bin_posterior(Q(1,4),Q(1,2),1)
