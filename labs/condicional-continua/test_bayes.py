from fractions import Fraction as Q
import unittest
from .density import (joint,marginal_x,rectangle,band_interval,
                      point_interval,posterior_x_density,posterior_x_interval)


def simpson_exact(f,a,b):
    # Independente das primitivas do módulo; exato para polinômios de grau <=3.
    a,b=Q(a),Q(b)
    return (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6


class BayesTests(unittest.TestCase):
    def test_posterior_against_nested_quadrature(self):
        grid=[Q(i,4) for i in range(5)]
        spans=[(a,b) for a in grid for b in grid if a<=b]
        for c in grid:
            for d in grid:
                if c>=d: continue
                evidence=simpson_exact(lambda y:simpson_exact(lambda x:joint(x,y),0,1),c,d)
                for a,b in spans:
                    joint_mass=simpson_exact(lambda y:simpson_exact(lambda x:joint(x,y),a,b),c,d)
                    posterior_mass=simpson_exact(lambda x:posterior_x_density(x,c,d),a,b)
                    self.assertEqual(posterior_mass,joint_mass/evidence)
                    self.assertEqual(posterior_x_interval(a,b,c,d),posterior_mass)
                self.assertEqual(posterior_x_interval(0,1,c,d),1)

    def test_bayes_factorization_for_points_and_events(self):
        for x in [Q(i,10) for i in range(11)]:
            for c,d in [(0,Q(1,4)),(Q(1,4),Q(3,4)),(Q(1,2),1)]:
                evidence=rectangle(0,1,c,d)
                self.assertEqual(posterior_x_density(x,c,d)*evidence,
                                 point_interval(x,c,d)*marginal_x(x))
        for a,b in [(0,Q(1,2)),(Q(1,4),Q(3,4)),(Q(1,2),1)]:
            self.assertEqual(posterior_x_interval(a,b,Q(1,2),1),
                             band_interval(a,b,Q(1,2),1)*rectangle(a,b,0,1)/Q(13,20))

    def test_example_means_and_selection(self):
        self.assertEqual(rectangle(0,Q(1,2),0,1),Q(7,20))
        self.assertEqual(rectangle(0,Q(1,2),Q(1,2),1),Q(1,4))
        self.assertEqual(band_interval(0,Q(1,2),Q(1,2),1),Q(5,7))
        self.assertEqual(posterior_x_interval(0,Q(1,2),Q(1,2),1),Q(5,13))
        prior=simpson_exact(lambda x:x*marginal_x(x),0,1)
        posterior=simpson_exact(lambda x:x*posterior_x_density(x,Q(1,2),1),0,1)
        self.assertEqual(prior,Q(3,5));self.assertEqual(posterior,Q(15,26))
        self.assertEqual(posterior-prior,-Q(3,130))
        likelihood=[point_interval(Q(i,20),Q(1,2),1) for i in range(21)]
        self.assertTrue(all(a>b for a,b in zip(likelihood,likelihood[1:])))

    def test_contracts_null_event_and_no_information(self):
        for x in [Q(i,10) for i in range(-1,12)]:
            self.assertEqual(posterior_x_density(x,0,1),marginal_x(x))
            self.assertIsNone(posterior_x_density(x,Q(1,2),Q(1,2)))
        self.assertIsNone(posterior_x_interval(0,1,0,0))
        self.assertEqual(posterior_x_interval(Q(1,2),Q(1,2),0,1),0)
        for args in [(0,1,0),(.5,0,1),(True,0,1),(0,-1,1)]:
            with self.assertRaises((TypeError,ValueError)):posterior_x_density(*args)
        for args in [(1,0,0,1),(0,1,1,0),(0,1,0,1.0)]:
            with self.assertRaises((TypeError,ValueError)):posterior_x_interval(*args)

if __name__=='__main__':unittest.main()
