import unittest
from decimal import Decimal, localcontext
from math import log
from .energy import affinity, coupled

class EnergyTests(unittest.TestCase):
    def test_decimal_reference(self):
        # Independent high precision logarithm, not float log repeated.
        with localcontext() as ctx:
            ctx.prec=70
            for ci in (0.125,1,3,8):
                for co in (0.25,1,5):
                    for z in (-2,-1,0,1,2):
                        psi=0.375
                        expected=(Decimal(str(ci))/Decimal(str(co))).ln()+Decimal(z)*Decimal(str(psi))
                        self.assertAlmostEqual(affinity(ci,co,z,psi),float(expected),places=13)
    def test_landmarks_and_signs(self):
        self.assertAlmostEqual(affinity(8,1,1,-log(16)),-log(2),places=14)
        self.assertAlmostEqual(affinity(8,1,-1,-log(16)),7*log(2),places=14)
        self.assertAlmostEqual(affinity(8,1,1,-log(8)),0,places=14)
        # Thermodynamic zero is checked by tolerance, not exact float equality.
        for k in range(-3,4):
            for z in (-2,-1,1,2):
                self.assertAlmostEqual(affinity(2.0**k,1,z,-k*log(2)/z),0,places=13)
    def test_reversal_scaling_and_extremes(self):
        for ci,co,z,psi in [(8,1,1,-2),(1,4,-1,0.2),(3,5,2,-0.8)]:
            a=affinity(ci,co,z,psi)
            self.assertAlmostEqual(affinity(co,ci,z,-psi),-a,places=13)
            for scale in (1e-6,2,1e6):
                self.assertAlmostEqual(affinity(ci*scale,co*scale,z,psi),a,places=13)
        self.assertAlmostEqual(affinity(1e300,1e-300),600*log(10),places=10)
    def test_coupled_by_event_sum(self):
        # Compare stoichiometric multiplication to an independently assembled event list.
        for t in (-2,0,2,4):
            for driver in (-3,-1,1):
                for n in (1,2,3,4):
                    events=[t*log(2)]+[driver*log(2) for _ in range(n)]
                    self.assertAlmostEqual(coupled(t*log(2),driver*log(2),n),sum(events),places=13)
        self.assertAlmostEqual(coupled(2*log(2),-log(2),2),0,places=14)
        self.assertLess(coupled(2*log(2),-log(2),3),0)
    def test_contracts(self):
        for args in [(0,1),(1,-1),(True,1),(float('nan'),1),(1,1,0.5),(1,1,9),(1,1,1,float('inf'))]:
            with self.assertRaises(ValueError): affinity(*args)
        for n in (0,-1,1.5,True,101):
            with self.assertRaises(ValueError): coupled(1,-1,n)

if __name__=='__main__': unittest.main()
