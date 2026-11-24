import unittest
from itertools import product
from math import log
from energy import transfer,coupled,R,F


class EnergyTests(unittest.TestCase):
    def test_reference_by_activity_ratio(self):
        # Compare linear pH implementation to an independently formed activity ratio.
        for a,b,c,d,T in product((6,7,8),(6,7,8),(-.15,0,.05),(-.15,0,.05),(280,300,320)):
            expected=R*T*log(10.0**(-b)/10.0**(-a))+F*(d-c)
            self.assertAlmostEqual(transfer(a,b,c,d,T)['total'],expected,places=8)

    def test_reverse_additivity_and_gauge(self):
        states=[(7,0),(8,-.15),(6,.05)]
        for a,b,c in product(states,repeat=3):
            ab=transfer(a[0],b[0],a[1],b[1])['total']
            ba=transfer(b[0],a[0],b[1],a[1])['total']
            bc=transfer(b[0],c[0],b[1],c[1])['total']
            ac=transfer(a[0],c[0],a[1],c[1])['total']
            self.assertAlmostEqual(ab,-ba,places=9)
            self.assertAlmostEqual(ab+bc,ac,places=8)
            shifted=transfer(a[0],b[0],a[1]+2,b[1]+2)['total']
            self.assertAlmostEqual(ab,shifted,places=8)
        self.assertEqual(transfer(7,7,0,0)['total'],0)

    def test_contributions_and_coupling(self):
        x=transfer(7,8,0,-.15)
        self.assertLess(x['chemical'],0);self.assertLess(x['electric'],0)
        self.assertAlmostEqual(x['electric'],-14472.75,places=8)
        self.assertGreater(coupled(x['total'],2,50000),0)
        self.assertLess(coupled(x['total'],3,50000),0)
        # Opposing chemical/electrical tendencies do not guarantee downhill transport.
        self.assertGreater(transfer(7,8,0,.10)['total'],0)

    def test_contracts(self):
        for a,b,c,d,T in [(True,8,0,-.15,300),(7,8,0,-.15,0),(7,8,0,-.15,-1),
                          (7,8,0,float('nan'),300),(7,8,0,-.15,float('inf')),
                          ('7',8,0,-.15,300),(7,8,0,-.15,10**1000)]:
            with self.assertRaises(ValueError):transfer(a,b,c,d,T)
        for m,atp in [(0,50000),(-1,50000),(True,50000),(2.0,50000),(3,0),(3,-1)]:
            with self.assertRaises(ValueError):coupled(-20000,m,atp)


if __name__=='__main__':unittest.main()
