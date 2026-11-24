import unittest
from fractions import Fraction as F
from .experiment import boost,model

class LengthTests(unittest.TestCase):
    def test_fraction_events_from_constraints(self):
        for beta,gamma in ((F(0),F(1)),(F(3,5),F(5,4)),(F(-3,5),F(5,4)),(F(4,5),F(5,3)),(F(-4,5),F(5,3))):
            for L in (F(1,2),F(2),F(4)):
                for mode in (0,1):
                    m=model(float(beta),float(L),mode)
                    # Resolva a interseção da extremidade u=βτ+1/γ com a fatia escolhida.
                    u=1/gamma if mode==0 else (1/gamma)/(1-beta*beta)
                    tau=F(0) if mode==0 else beta*u
                    self.assertAlmostEqual(m['b'][0],float(tau),places=13)
                    self.assertAlmostEqual(m['b'][1],float(u),places=13)
                    self.assertAlmostEqual(m['lab_length'],float(L/gamma),places=13)
                    self.assertAlmostEqual(m['lab_span'],float(L*u),places=13)
                    self.assertAlmostEqual(m['delta_ct_prime'],float(L*gamma*(tau-beta*u)),places=13)
                    self.assertAlmostEqual(m['invariant_lab'],float(L*L*(tau*tau-u*u)),places=13)

    def test_inverse_invariance_and_worldlines(self):
        for i in range(-8,9):
            beta=i/10
            for L in (.5,1,2,4):
                for mode in (0,1):
                    m=model(beta,L,mode)
                    self.assertAlmostEqual(m['bp'][1],1,places=13)
                    self.assertAlmostEqual(m['b'][1]-beta*m['b'][0],1/m['gamma'],places=13)
                    back=boost(*m['bp'],-beta)
                    for a,b in zip(back,m['b']):self.assertAlmostEqual(a,b,places=13)
                    self.assertAlmostEqual(m['invariant_lab'],m['invariant_rest'],places=12)
                    if mode==0:self.assertEqual(m['delta_ct'],0)
                    else:self.assertAlmostEqual(m['delta_ct_prime'],0,places=13)

    def test_scale_sign_and_distinct_pairs(self):
        for mode in (0,1):
            m=model(.6,2,mode);scaled=model(.6,4,mode);negative=model(-.6,2,mode)
            for key in ('lab_length','lab_span','rest_span','delta_ct','delta_ct_prime'):
                self.assertAlmostEqual(scaled[key],2*m[key],places=13)
            self.assertAlmostEqual(scaled['invariant_lab'],4*m['invariant_lab'],places=13)
            self.assertEqual(m['lab_length'],negative['lab_length'])
            self.assertAlmostEqual(m['delta_ct'],-negative['delta_ct'],places=13)
            self.assertAlmostEqual(m['delta_ct_prime'],-negative['delta_ct_prime'],places=13)
        self.assertAlmostEqual(model()['lab_length'],1.6)
        self.assertAlmostEqual(model(mode=1)['lab_span'],2.5)
        self.assertFalse(model(mode=1)['simultaneous_lab'])
        for mode in (0,1):
            m=model(0,2,mode);self.assertTrue(m['simultaneous_lab']);self.assertTrue(m['simultaneous_rest']);self.assertEqual(m['lab_span'],2)

    def test_domain(self):
        for args in ((.9,2,0),(0,0,0),(0,5,0),(0,2,2),(True,2,0),(0,float('nan'),0)):
            with self.assertRaises(ValueError):model(*args)
        for beta in (-1,1,float('inf')):
            with self.assertRaises(ValueError):boost(0,1,beta)
