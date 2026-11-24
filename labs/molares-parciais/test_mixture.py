import unittest
from fractions import Fraction as Q
from .mixture import state,add_B


class MolarTests(unittest.TestCase):
    def test_original_inventory(self):
        s=state(3,1)
        self.assertEqual((s['V'],s['ideal'],s['excess']),(357,360,-3))
        self.assertEqual((s['partialA'],s['partialB']),(Q(399,4),Q(231,4)))
        d=add_B(3,1,Q(1,2))
        self.assertEqual((d['actual'],d['linear'],d['remainder']),(29,Q(231,8),Q(1,8)))

    def test_extensivity_euler_and_gibbs_duhem(self):
        for a in range(5):
            for b in range(5):
                if a+b==0:continue
                s=state(a,b)
                self.assertEqual(s['V'],a*s['partialA']+b*s['partialB'])
                self.assertEqual(s['xA']*s['dpartialA_dxB']+s['xB']*s['dpartialB_dxB'],0)
                for k in (Q(1,2),2,3):
                    t=state(k*a,k*b)
                    self.assertEqual(t['V'],k*s['V'])
                    self.assertEqual(t['partialA'],s['partialA']);self.assertEqual(t['partialB'],s['partialB'])

    def test_derivative_as_limit_and_finite_remainder(self):
        for a in (1,2,3):
            for b in (1,2,3):
                s=state(a,b);N=a+b
                for d in (Q(1,2),Q(1,4),Q(1,8)):
                    r=add_B(a,b,d)
                    self.assertEqual(r['remainder'],4*a*a*d*d/(N*N*(N+d)))
                    self.assertGreater(r['remainder'],0)
                d=Q(1,10**6)
                quotient=(state(a,b+d)['V']-s['V'])/d
                self.assertLess(abs(quotient-s['partialB']),Q(1,10**6))

    def test_pure_limits_and_contracts(self):
        self.assertEqual(state(1,0)['partialA'],100)
        self.assertEqual(state(0,1)['partialB'],60)
        self.assertEqual(state(1,0)['partialB'],56) # limite de B infinitamente diluído em A
        for a,b in ((0,0),(-1,2),(True,1),(1.,2)):
            with self.assertRaises(ValueError):state(a,b)
        with self.assertRaises(ValueError):add_B(3,1,-1)


if __name__=='__main__':unittest.main()
