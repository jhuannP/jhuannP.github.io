import unittest
from fractions import Fraction as Q
from itertools import product
from collective import analyze,internal_impulse


class CollectiveTests(unittest.TestCase):
    def test_two_body_reduced_mass(self):
        for m1,m2,v1,v2 in product((1,2,3),(1,2,3),range(-2,3),range(-2,3)):
            a=analyze((m1,m2),(0,4),(v1,v2))
            mu=Q(m1*m2,m1+m2)
            self.assertEqual(a['Krel'],mu*(v1-v2)**2/2)
            self.assertEqual(a['K'],a['Kcm']+a['Krel'])
            self.assertEqual(a['internal_momentum'],0)
            self.assertEqual(a['M']*a['V'],m1*v1+m2*v2)

    def test_translation_and_galilean_change(self):
        masses=(1,2,3);positions=(-2,1,4)
        for velocities in product((-2,0,3),repeat=3):
            a=analyze(masses,positions,velocities)
            for b in (-2,0,2):
                shifted=analyze(masses,tuple(x+5 for x in positions),tuple(v+b for v in velocities))
                self.assertEqual(shifted['R'],a['R']+5)
                self.assertEqual(shifted['V'],a['V']+b)
                self.assertEqual(shifted['Krel'],a['Krel'])
                self.assertEqual(shifted['relative_positions'],a['relative_positions'])
                self.assertEqual(shifted['K'],a['K']+b*a['P']+a['M']*b*b/2)

    def test_internal_impulse_preserves_momentum_not_energy(self):
        for v1,v2,J in product((-2,0,3),(-2,0,3),(-3,-1,0,1,3)):
            before=analyze((1,3),(0,4),(v1,v2))
            v=internal_impulse(1,3,v1,v2,J)
            after=analyze((1,3),(0,4),v)
            self.assertEqual(before['P'],after['P'])
            self.assertEqual(before['V'],after['V'])
        a=analyze((1,3),(0,4),(4,0))
        b=analyze((1,3),(0,4),internal_impulse(1,3,4,0,-3))
        self.assertEqual((a['R'],a['V'],a['K'],a['Kcm'],a['Krel']),(3,1,8,2,6))
        self.assertEqual(b['K'],2)

    def test_contracts(self):
        for args in [((),(),()),((1,),(0,1),(0,)),((0,),(0,),(0,)),((-1,),(0,),(0,)),
                     ((True,),(0,),(0,)),((1.0,),(0,),(0,)),((1,),(0,),(float('nan'),))]:
            with self.assertRaises(ValueError):analyze(*args)
        with self.assertRaises(ValueError):internal_impulse(0,1,0,0,1)


if __name__=='__main__':unittest.main()
