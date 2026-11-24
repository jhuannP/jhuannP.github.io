import unittest
from fractions import Fraction as Q
from .faraday import charge,deposition,required_charge

class FaradayTests(unittest.TestCase):
    def test_fixture_and_inventory(self):
        self.assertEqual(charge([(1,1930)]),1930)
        r=deposition(1930,Q(127,2),2,Q(4,5))
        self.assertEqual(r,dict(electron_mol=Q(1,50),product_mol=Q(1,125),mass_g=Q(127,250),target_C=1544,other_C=386))
        self.assertEqual(required_charge(Q(127,100),Q(127,2),2,Q(4,5)),4825)
        self.assertEqual(deposition(1930,Q(127,2),2)['mass_g'],Q(127,200))
        with self.assertRaises(ValueError):deposition(1930,Q(127,2),2,Q(4,5),available=Q(1,200))
        self.assertEqual(deposition(1930,Q(127,2),2,Q(4,5),available=Q(1,125)),r)

    def test_charge_additivity_and_schedule(self):
        self.assertEqual(charge([(2,600),(Q(1,2),1200)]),1800)
        for i in range(1,7):
            for t in range(1,21):
                self.assertEqual(charge([(i,t)]),charge([(i,Q(t,3)),(i,Q(2*t,3))]))
                self.assertEqual(charge([(i,t),(2*i,t)]),charge([(2*i,t),(i,t)]))
                self.assertEqual(charge([(2*i,t)]),2*charge([(i,t)]))

    def test_balances_and_inverse(self):
        for q in (100,500,1930,10000):
            for z in (1,2,3):
                for eta in (Q(1,5),Q(4,5),Q(1)):
                    for M in (Q(127,2),Q(587,10)):
                        r=deposition(q,M,z,eta)
                        self.assertEqual(r['product_mol']*z*96500,eta*q)
                        self.assertEqual(r['mass_g']/M,r['product_mol'])
                        self.assertEqual(r['target_C']+r['other_C'],q)
                        self.assertEqual(required_charge(r['mass_g'],M,z,eta),q)
        self.assertEqual(deposition(1930,100,2,0)['mass_g'],0)

    def test_contracts(self):
        for s in ([],[(True,1)],[(1.0,1)],[(1,-1)],[(1,86401)],[(1,2,3)]):
            with self.assertRaises(ValueError):charge(s)
        for z in (0,9,True,2.0):
            with self.assertRaises(ValueError):deposition(1,100,z)
        for eta in (-1,Q(11,10)):
            with self.assertRaises(ValueError):deposition(1,100,2,eta)
        with self.assertRaises(ValueError):required_charge(1,100,2,0)
        with self.assertRaises(ValueError):deposition(1,0,2)
