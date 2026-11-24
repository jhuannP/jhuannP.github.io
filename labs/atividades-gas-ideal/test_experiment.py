import unittest
from fractions import Fraction as Q
from itertools import product
from .experiment import state,equilibrium_square

class IdealActivityTests(unittest.TestCase):
    def test_reference_and_compression(self):
        s=state(Q(1,2),1)
        self.assertEqual((s["nA"],s["nB"],s["total"]),(Q(1,2),1,Q(3,2)))
        self.assertEqual((s["aA"],s["aB"],s["Q"]),(Q(1,3),Q(2,3),Q(4,3)))
        self.assertEqual(state(Q(1,2),4)["Q"],Q(16,3))
        self.assertEqual(equilibrium_square(Q(4,3),4),Q(1,13))
    def test_material_balance_and_activity_from_partial_pressure(self):
        for i,r in product(range(20),(Q(1,4),Q(1,2),1,2,4)):
            x=Q(i,20);s=state(x,r)
            self.assertEqual(2*s["nA"]+s["nB"],2)
            self.assertEqual(s["yA"]+s["yB"],1)
            self.assertEqual(s["aA"]+s["aB"],r)
            # Pressure calculation independent of the expanded Q(x,r) formula.
            pA=r*Q(20-i,20+i);pB=r*Q(2*i,20+i)
            self.assertEqual(s["Q"],pB**2/pA)
    def test_recover_rational_equilibria_and_monotonicity(self):
        for i,r in product(range(1,20),(Q(1,4),1,4)):
            x=Q(i,20);K=state(x,r)["Q"]
            self.assertEqual(equilibrium_square(K,r),x*x)
            self.assertLess(equilibrium_square(K,2*r),x*x)
            self.assertGreater(equilibrium_square(2*K,r),x*x)
        for r in (Q(1,4),1,4):
            qs=[state(Q(i,20),r)["Q"] for i in range(20)]
            self.assertTrue(all(a<b for a,b in zip(qs,qs[1:])))
    def test_pressure_units_and_standard_state_convention(self):
        P,pstd=Q(2),Q(1) # bars
        self.assertEqual(P/pstd,(100000*P)/(100000*pstd))
        for x,r in product((Q(1,4),Q(1,2),Q(3,4)),(1,2,4)):
            s=state(x,r);changed=state(x,r/ Q(2))
            self.assertEqual(changed["Q"],s["Q"]/2)
            self.assertEqual(equilibrium_square(s["Q"],r),
                             equilibrium_square(changed["Q"],r/Q(2)))
    def test_endpoints_and_contracts(self):
        self.assertEqual(state(0,1)["Q"],0)
        for x,r in [(-1,1),(1,1),(Q(3,2),1),(0,0),(True,1),(.5,1)]:
            with self.assertRaises(ValueError):state(x,r)
        for K,r in [(0,1),(-1,1),(1,0),(True,1),(1,1.)]:
            with self.assertRaises(ValueError):equilibrium_square(K,r)
