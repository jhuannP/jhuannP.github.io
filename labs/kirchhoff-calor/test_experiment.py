import unittest
from fractions import Fraction as F
from .experiment import cp_integral,model

class KirchhoffTests(unittest.TestCase):
    def test_independent_quadrature_and_state_path(self):
        for t in range(250,651,25):
            for b in range(20,61,5):
                m=model(t,b);u=F(t-300)
                # Trapézio exato para Cp linear, separadamente para cada espécie.
                ha=u*(F(40)+F(40)+u/F(50))/2/1000
                hb=F(2)+u*F(b)/1000
                self.assertAlmostEqual(m['ha'],float(ha),places=13)
                self.assertAlmostEqual(m['hb'],float(hb),places=13)
                self.assertAlmostEqual(m['dh'],float(hb-ha),places=13)
                self.assertAlmostEqual(m['cycle'],m['dh'],places=13)
                self.assertAlmostEqual(m['error'],float(-u*u/F(100000)),places=13)
                self.assertGreater(m['cpa'],0);self.assertGreater(m['cpb'],0)

    def test_composition_reversal_and_derivative(self):
        for c0,slope in ((40,.02),(30,0)):
            for t1,t2,t3 in ((250,300,650),(650,450,250),(300,300,500)):
                a=cp_integral(c0,slope,t1,t3)
                self.assertAlmostEqual(a,cp_integral(c0,slope,t1,t2)+cp_integral(c0,slope,t2,t3),places=11)
                self.assertEqual(a,-cp_integral(c0,slope,t3,t1))
        for t in (275,350,500,625):
            m=model(t);h=.001
            derivative=(model(t+h)['dh']-model(t-h)['dh'])/(2*h)
            self.assertAlmostEqual(derivative,m['dcp']/1000,places=9)

    def test_reference_zero_and_units(self):
        m=model(300);self.assertEqual(m['dh'],2);self.assertEqual(m['constant'],2);self.assertEqual(m['error'],0)
        m=model(500);self.assertAlmostEqual(m['ha'],8.4);self.assertEqual(m['hb'],8)
        self.assertAlmostEqual(m['dh'],-.4);self.assertEqual(m['constant'],0);self.assertEqual(m['dcp'],-14)
        self.assertEqual(cp_integral(40,0,300,500),8000)
        self.assertAlmostEqual(cp_integral(40,.02,300,500),8400)

    def test_domain(self):
        for args in ((249,30),(651,30),(300,19),(300,61),(True,30),(float('nan'),30),(300,'30')):
            with self.assertRaises(ValueError):model(*args)
        with self.assertRaises(ValueError):cp_integral(1,-.1,300,650)
