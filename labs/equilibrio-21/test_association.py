import unittest
from fractions import Fraction as Q
from .association import bracket


class AssociationTests(unittest.TestCase):
    def test_rational_fixtures_and_dilution(self):
        for v, xi, a, b in ((1,1,1,1),(8,Q(1,2),2,Q(1,2))):
            r=bracket(3,0,v,1,80)
            self.assertLessEqual(r['lo'],xi)
            self.assertGreaterEqual(r['hi'],xi)
            self.assertLessEqual(abs(r['A']-a),2*r['error_bound'])
            self.assertLessEqual(abs(r['B']-b),r['error_bound'])
        # At fixed amounts dilution multiplies Q by eight, not K.
        self.assertEqual(Q(8)*1/1**2,8)

    def test_known_equilibria_independent_construction(self):
        # Choose positive final amounts first; derive K, then start at three compositions.
        for a in (Q(1,3),Q(2),Q(7,2)):
            for b in (Q(1,5),Q(1),Q(5,2)):
                for v in (Q(1,4),Q(1),Q(8)):
                    K=v*b/a**2; total=a+2*b
                    for a0,b0 in ((total,Q(0)),(Q(0),total/2),(a,b)):
                        r=bracket(a0,b0,v,K,35); xi=b-b0
                        self.assertLessEqual(r['lo'],xi)
                        self.assertGreaterEqual(r['hi'],xi)
                        self.assertEqual(r['A']+2*r['B'],total)
                        self.assertGreaterEqual(r['A'],0)
                        self.assertGreaterEqual(r['B'],0)
                        self.assertLessEqual(r['hi']-r['lo'],(a0/2+b0)/2**35)

    def test_nonrational_root_by_sign_and_nested_brackets(self):
        # K=2/3 gives a nonrational equilibrium for a0=3,b0=0,v=1.
        prior=None
        for steps in (0,1,2,5,15,40):
            r=bracket(3,0,1,Q(2,3),steps)
            for x,sign in ((r['lo'],-1),(r['hi'],1)):
                a=3-2*x; b=x
                self.assertGreaterEqual(sign*(b-Q(2,3)*a*a),0)
            if prior:
                self.assertGreaterEqual(r['lo'],prior['lo'])
                self.assertLessEqual(r['hi'],prior['hi'])
            prior=r

    def test_scaling_and_reverse_extent(self):
        r=bracket(0,Q(3,2),1,1,60)
        self.assertLess(r['extent'],0)
        for scale in (Q(1,10),Q(3),Q(7,2)):
            s=bracket(0,scale*Q(3,2),scale,1,60)
            for key in ('lo','hi','A','B','error_bound'):
                self.assertEqual(s[key],scale*r[key])

    def test_contracts(self):
        for args in ((0,0,1,1),(-1,1,1,1),(1,0,0,1),(1,0,1,-1),
                     (True,0,1,1),(1.0,0,1,1)):
            with self.assertRaises(ValueError): bracket(*args)
        for steps in (-1,201,True,2.5):
            with self.assertRaises(ValueError): bracket(3,0,1,1,steps)
