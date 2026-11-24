import unittest
from fractions import Fraction as Q
from itertools import product
from .features import feature,feature_at,dimensionless,comparison,OLS


class FeatureTests(unittest.TestCase):
    def test_training_and_information_loss(self):
        good,lost,gd,ld=comparison()
        self.assertEqual((good.slope,good.intercept,OLS.mse(good,gd)),(Q(1,2),0,0))
        self.assertEqual((lost.slope,lost.intercept,OLS.mse(lost,ld)),(Q(5,12),Q(4,3),Q(2,3)))
        self.assertEqual(lost.predict(4),3)
        # New state is an algebraic check, not a statistical generalization experiment.
        self.assertEqual(good.predict(feature(2,3)),9)
        self.assertEqual(lost.predict(9),Q(61,12))
        self.assertEqual(sum(lost.predict(x)-y for x,y in ld),0)
        self.assertEqual(sum(x*(lost.predict(x)-y) for x,y in ld),0)

    def test_units(self):
        # Independent equivalent physical observations across 2 mass x 3 speed units.
        for m,v in product((1,2,5),(-3,0,2)):
            for mass,mu in [(m,'kg'),(m*1000,'g')]:
                for velocity,vu in [(Q(v),'m/s'),(Q(v*100),'cm/s'),(Q(v*18,5),'km/h')]:
                    self.assertEqual(feature(mass,velocity,mu,vu),m*v*v)
        self.assertEqual(feature(1000,200,'g','cm/s'),4)
        self.assertEqual(Q(1000*200**2,4),10**7)

    def test_nondimensional_and_sign(self):
        for m,v,m0,v0 in product((1,2,3),(-4,-1,0,2),(1,2),(1,3)):
            pi=dimensionless(m,v,m0,v0)
            self.assertEqual(pi,feature(m,v)/(m0*v0*v0))
            self.assertEqual(Q(1,2)*pi,(Q(1,2)*m*v*v)/(m0*v0*v0))
            self.assertEqual(feature(m,v),feature(m,-v))
        self.assertEqual(dimensionless(2,3,2,3),1)

    def test_declared_availability(self):
        self.assertEqual(feature_at(1,2,0,1,1),4)
        for tm,tv,tp in [(0,2,1),(2,0,1),(0,1,0)]:
            with self.assertRaises(ValueError):feature_at(1,2,tm,tv,tp)
        # Metadata supplied by caller can be false; function cannot audit causal provenance.
        self.assertEqual(feature_at(1,2,-1,-1,0),4)

    def test_old_example_and_contracts(self):
        v=3;self.assertEqual(v*v,9);self.assertEqual(3**2,(-3)**2)
        for m in (0,-1):
            with self.assertRaises(ValueError):feature(m,2)
        with self.assertRaises(ValueError):feature(1,2,'lb','m/s')
        with self.assertRaises(ValueError):feature(1,2,'kg','mph')
        for x in (True,2.0,'2'):
            with self.assertRaises(TypeError):feature(1,x)
        with self.assertRaises(ValueError):dimensionless(1,2,0,1)
        with self.assertRaises(ValueError):dimensionless(1,2,1,-1)
