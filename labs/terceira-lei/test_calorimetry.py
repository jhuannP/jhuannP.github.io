import unittest
from fractions import Fraction as Q
from .calorimetry import cp,cp_over_t,entropy,increment,phase_change

class CalorimetryTests(unittest.TestCase):
    def test_integral_against_independent_simpson(self):
        for ia in range(21):
            for ib in range(ia,21):
                a,b=Q(ia),Q(ib);mid=(a+b)/2
                # Integral exata da quadrática por Simpson, sem usar a primitiva.
                expected=(b-a)*(a*a+4*mid*mid+b*b)/3000
                self.assertEqual(increment(a,b),expected)
        self.assertEqual(cp(10),2);self.assertEqual(entropy(10),Q(2,3))
        self.assertEqual(entropy(20),Q(16,3))

    def test_zero_limit_and_scaling(self):
        self.assertEqual(cp(0),0);self.assertEqual(cp_over_t(0),0)
        self.assertEqual(entropy(0),0)
        previous=entropy(1)
        for n in range(1,31):
            T=Q(1,2**n)
            current=entropy(T)
            self.assertEqual(current,previous/8);previous=current
        for T in (1,2,5,10):self.assertEqual(entropy(2*T),8*entropy(T))

    def test_reference_and_additivity(self):
        for s0 in (0,Q(1,2),3):
            self.assertEqual(entropy(20,s0)-entropy(10,s0),Q(14,3))
        for a,b,c in ((0,5,20),(1,10,19),(Q(1,2),Q(3,2),Q(7,2))):
            self.assertEqual(increment(a,b)+increment(b,c),increment(a,c))
            self.assertGreaterEqual(increment(a,c),0)

    def test_supplied_phase_transition(self):
        self.assertEqual(phase_change(30,10),3)
        self.assertEqual(phase_change(-30,10),-3)
        self.assertEqual(entropy(10),Q(2,3))
        self.assertEqual(entropy(10)+phase_change(30,10),Q(11,3))
        self.assertEqual(entropy(20)+phase_change(30,10),Q(25,3))

    def test_contracts(self):
        for f in (cp,cp_over_t,entropy):
            for bad in (True,1.,'1',-1,21):
                with self.assertRaises(ValueError):f(bad)
        with self.assertRaises(ValueError):cp(1,alpha=-1)
        with self.assertRaises(ValueError):entropy(1,s0=-1)
        with self.assertRaises(ValueError):increment(2,1)
        with self.assertRaises(ValueError):phase_change(30,0)
        self.assertEqual(cp(20,alpha=0),0)
