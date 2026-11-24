import unittest
from math import sqrt
try:
    from .experiment import ledger
except ImportError:
    from experiment import ledger

class WorkTests(unittest.TestCase):
    def test_reference(self):
        r=ledger(2,10,.1,3)
        self.assertEqual(r['initial_energy'],4);self.assertEqual(r['work_applied'],30)
        self.assertEqual(r['work_friction'],-6);self.assertEqual(r['final_energy'],28)
        self.assertAlmostEqual(r['speed'],sqrt(28));self.assertTrue(r['reached'])

    def test_stop_and_coast(self):
        r=ledger(2,0,.1,5)
        self.assertEqual(r['stop_distance'],2);self.assertEqual(r['travelled'],2)
        self.assertEqual(r['speed'],0);self.assertEqual(r['work_friction'],-4)
        self.assertFalse(r['reached']);self.assertTrue(r['stopped'])
        boundary=ledger(2,0,.1,2);self.assertTrue(boundary['reached']);self.assertTrue(boundary['stopped'])
        r=ledger(2,0,0,5);self.assertEqual(r['speed'],2);self.assertEqual(r['work_net'],0)

    def test_against_newton_and_energy_ledger(self):
        for mass in [1,2,3]:
            for force in [0,2,10,12]:
                for mu in [0,.1,.5,1]:
                    for distance in [0,.5,2,5]:
                        r=ledger(mass,force,mu,distance);a=force/mass-mu*10
                        if a<0:self.assertAlmostEqual(r['stop_distance'],4/(-2*a))
                        self.assertAlmostEqual(r['speed']**2,max(0,4+2*a*r['travelled']),places=10)
                        self.assertAlmostEqual(r['final_energy']-r['initial_energy'],r['work_net'],places=10)
                        self.assertGreaterEqual(r['final_energy'],0)

    def test_contracts(self):
        for args in [(0,10,.1,3),(2,-1,.1,3),(2,1,-.1,3),(2,1,0,-1),(True,1,0,1),(2,float('nan'),0,1)]:
            with self.assertRaises(ValueError):ledger(*args)

if __name__=='__main__':unittest.main()
